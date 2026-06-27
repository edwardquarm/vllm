#!/usr/bin/env bash
# Run the evaluation pipeline for all PRs listed in prs.yaml.
#
# Usage:
#   ./run_all.sh [options]
#
# Options (passed through to run_evaluation.sh for every PR):
#   --skip-lane-1   skip CI evidence collection (reuse existing)
#   --skip-lane-2   skip LLM selector replay (reuse existing)
#   --skip-llm      run Lane 2 without calling claude
#   --model <m>     LLM model for Lane 2 (default: haiku)
#   --force         re-run PRs that already have a report.md
#
# Examples:
#   # Run all PRs (skip already-completed ones):
#   ./run_all.sh
#
#   # Re-run only Lane 3 for all PRs (fast, no LLM or API calls):
#   ./run_all.sh --skip-lane-1 --skip-lane-2
#
#   # Force re-run everything:
#   ./run_all.sh --force

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PR_LIST_FILE="$SCRIPT_DIR/prs.yaml"
RUNNER="$SCRIPT_DIR/scripts/run_evaluation.sh"

FORCE=1
PASS_THROUGH=()

while [[ $# -gt 0 ]]; do
    case "$1" in
        --force) FORCE=1; shift ;;
        *)       PASS_THROUGH+=("$1"); shift ;;
    esac
done

if [[ ! -f "$PR_LIST_FILE" ]]; then
    echo "Error: PR list not found at $PR_LIST_FILE"
    exit 1
fi

# Parse PR numbers from prs.yaml (lines matching "  - <number>")
PR_LIST=$(grep -E '^\s*-\s+[0-9]+' "$PR_LIST_FILE" | grep -oE '[0-9]+')

if [[ -z "$PR_LIST" ]]; then
    echo "Error: No PR numbers found in $PR_LIST_FILE"
    exit 1
fi

TOTAL=$(echo "$PR_LIST" | wc -l)
COUNT=0
SKIPPED=0
FAILED=0

echo "==========================================="
echo "  BATCH PR EVALUATION"
echo "==========================================="
echo "  PR list: $PR_LIST_FILE ($TOTAL PRs)"
[[ ${#PASS_THROUGH[@]} -gt 0 ]] && echo "  Options: ${PASS_THROUGH[*]}"
echo "==========================================="

for pr in $PR_LIST; do
    COUNT=$((COUNT + 1))
    REPORT="$SCRIPT_DIR/evaluation/pr_${pr}/report.md"

    if [[ "$FORCE" -eq 0 && -f "$REPORT" ]]; then
        echo "[$COUNT/$TOTAL] Skipping PR #$pr (report already exists; use --force to re-run)"
        SKIPPED=$((SKIPPED + 1))
        continue
    fi

    echo ""
    echo "[$COUNT/$TOTAL] ==============================="
    echo "  PR #$pr"
    echo "[$COUNT/$TOTAL] ==============================="

    if bash "$RUNNER" "$pr" "${PASS_THROUGH[@]}"; then
        echo "[$COUNT/$TOTAL] Done: PR #$pr"
    else
        echo "[$COUNT/$TOTAL] FAILED: PR #$pr (continuing...)"
        FAILED=$((FAILED + 1))
    fi
done

echo ""
echo "==========================================="
echo "  BATCH COMPLETE"
echo "==========================================="
echo "  Total:   $TOTAL"
echo "  Skipped: $SKIPPED (already had report)"
echo "  Failed:  $FAILED"
echo "  Done:    $((TOTAL - SKIPPED - FAILED))"
echo "==========================================="
