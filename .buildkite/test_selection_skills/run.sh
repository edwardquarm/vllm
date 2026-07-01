#!/bin/bash
# Quick wrapper to run the PR evaluation workflow
#
# Usage:
#   ./run.sh <pr_number> [options]
#
# Options:
#   --second-pass    After normal evaluation, run the second pass agent and
#                    score its additions against the actual CI failures.
#                    Reuses existing replay — no LLM call for Lane 2.
#   Any other flags are passed through to run_evaluation_skill.py
#
# Examples:
#   ./run.sh 43167
#   ./run.sh 43167 --second-pass
#   ./run.sh 43167 --skip-lane-1 --second-pass

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
PYTHON="$REPO_ROOT/.venv/bin/python"

if [ -z "${1:-}" ]; then
    echo "Usage: $0 <pr_number> [--second-pass] [other options]"
    echo "Example: $0 43167 --second-pass"
    exit 1
fi

PR_NUMBER="$1"
shift

SECOND_PASS=0
PASS_THROUGH=()

for arg in "$@"; do
    if [ "$arg" = "--second-pass" ]; then
        SECOND_PASS=1
        PASS_THROUGH+=("--with-second-pass")
    else
        PASS_THROUGH+=("$arg")
    fi
done

# Run evaluation (with --with-second-pass wired through if requested)
"$PYTHON" "$SCRIPT_DIR/scripts/run_evaluation_skill.py" "$PR_NUMBER" "${PASS_THROUGH[@]}"

# Optionally run the second pass agent and score the result
if [ "$SECOND_PASS" -eq 1 ]; then
    echo ""
    echo "========================================="
    echo "  SECOND PASS AGENT TEST"
    echo "========================================="

    REPLAY_FILE="$SCRIPT_DIR/replay/pr_${PR_NUMBER}/selector_replay.json"
    EVAL_FILE="$SCRIPT_DIR/evaluation/pr_${PR_NUMBER}/evaluation_report.json"
    PATTERNS_FILE="$SCRIPT_DIR/failure_patterns.json"
    SECOND_PASS_SCRIPT="$SCRIPT_DIR/after/second_pass.py"
    SECOND_PASS_INSTRUCTIONS="$SCRIPT_DIR/after/SECOND_PASS.md"

    for f in "$REPLAY_FILE" "$EVAL_FILE" "$PATTERNS_FILE" "$SECOND_PASS_SCRIPT" "$SECOND_PASS_INSTRUCTIONS"; do
        if [ ! -f "$f" ]; then
            echo "Missing: $f — skipping second pass test."
            exit 0
        fi
    done

    # Extract initial selection and changed files from replay
    CHANGED_FILES=$("$PYTHON" -c "
import json, sys
d = json.load(open('$REPLAY_FILE'))
print('\n'.join(d.get('changed_files', [])))
")
    INITIAL_SELECTION=$("$PYTHON" -c "
import json, sys
d = json.load(open('$REPLAY_FILE'))
tests = d.get('llm_selected_tests', [])
reasons = d.get('selection_reasons', [])
for i, t in enumerate(tests):
    ident = t.get('identifier', t) if isinstance(t, dict) else t
    reason = reasons[i] if i < len(reasons) else 'selected'
    print(f'{ident} | {reason}')
" 2>/dev/null || true)

    echo "Changed files:"
    echo "$CHANGED_FILES" | sed 's/^/  /'
    echo ""
    echo "Initial selection (Lane 2 output):"
    if [ -z "$INITIAL_SELECTION" ]; then
        echo "  (none)"
    else
        echo "$INITIAL_SELECTION" | sed 's/^/  /'
    fi
    echo ""
    echo "Running second pass agent..."
    echo ""

    ADDITIONS=$("$PYTHON" "$SECOND_PASS_SCRIPT" \
        --changed-files "$CHANGED_FILES" \
        --initial-selection "$INITIAL_SELECTION" \
        --patterns-file "$PATTERNS_FILE" \
        --instructions "$SECOND_PASS_INSTRUCTIONS" \
        --model haiku 2>/dev/null || true)

    echo "Second pass output:"
    echo "$ADDITIONS" | sed 's/^/  /'
    echo ""

    # Score: check which additions were actually in the FN list
    IS_NONE=$(echo "$ADDITIONS" | grep -ic '^[[:space:]]*NONE' || true)
    if [ "$IS_NONE" -gt 0 ]; then
        echo "Result: second pass made no additions."
    else
        echo "Scoring additions against actual CI failures..."
        "$PYTHON" - << PYEOF
import json, sys

additions_raw = """$ADDITIONS"""
eval_report = json.load(open("$EVAL_FILE"))

fns = {fn.get("failed_test","").rstrip("/") for fn in eval_report.get("false_negative_details", [])}

print(f"  Actual FNs in evaluation: {len(fns)}")
print()

correct, wrong, total = 0, 0, 0
for line in additions_raw.strip().splitlines():
    if "|" not in line or "NONE" in line.upper(): continue
    path = line.split("|")[0].strip().rstrip("/")
    reason = line.split("|")[1].strip() if "|" in line else ""
    total += 1
    # Check if this addition covers any FN (prefix match)
    covered = any(fn == path or fn.startswith(path) or path.startswith(fn) for fn in fns)
    mark = "✅ TP" if covered else "❌ FP"
    if covered: correct += 1
    else: wrong += 1
    print(f"  {mark}  {path}  —  {reason}")

print()
if total > 0:
    print(f"  Second pass precision: {correct}/{total} additions were correct ({correct*100//total}%)")
else:
    print("  No additions to score.")
PYEOF
    fi

    echo ""
    echo "========================================="
fi
