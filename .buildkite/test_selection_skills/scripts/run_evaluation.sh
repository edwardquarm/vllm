#!/usr/bin/env bash
# Run the full 3-lane PR evaluation pipeline from the shell.
#
# Usage:
#   ./scripts/run_evaluation.sh <pr_number> [options]
#
# Options:
#   --skip-lane-1        Skip CI evidence collection (reuse existing)
#   --skip-lane-2        Skip LLM selector replay (reuse existing)
#   --skip-llm           Run Lane 2 without calling claude (--skip-llm)
#   --model <model>      Model for Lane 2 (default: $ATS_SELECTOR_MODEL or haiku)
#   --repo <repo>        GitHub repo (default: vllm-project/vllm)
#   --output-dir <dir>   Custom output directory for Lane 3
#
# Examples:
#   # Full run (LLM required for Lane 2):
#   ./scripts/run_evaluation.sh 43167
#
#   # Run Lane 1 + 3, skip LLM (Lane 2 must already have a replay):
#   ./scripts/run_evaluation.sh 43167 --skip-lane-2
#
#   # Run all lanes but skip LLM call inside Lane 2:
#   ./scripts/run_evaluation.sh 43167 --skip-llm
#
#   # Use a specific model:
#   ./scripts/run_evaluation.sh 43167 --model qwen-3-5-397b-a100

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILLS_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
REPO_ROOT="$(cd "$SKILLS_DIR/../.." && pwd)"
PYTHON="$REPO_ROOT/.venv/bin/python"

# ---------- defaults ----------
PR_NUMBER=""
REPO="vllm-project/vllm"
SKIP_LANE_1=0
SKIP_LANE_2=0
SKIP_LLM=0
MODEL="${ATS_SELECTOR_MODEL:-haiku}"
OUTPUT_DIR=""

# ---------- parse args ----------
while [[ $# -gt 0 ]]; do
    case "$1" in
        --skip-lane-1) SKIP_LANE_1=1; shift ;;
        --skip-lane-2) SKIP_LANE_2=1; shift ;;
        --skip-llm)    SKIP_LLM=1;    shift ;;
        --model)       MODEL="$2";    shift 2 ;;
        --repo)        REPO="$2";     shift 2 ;;
        --output-dir)  OUTPUT_DIR="$2"; shift 2 ;;
        -*)  echo "Unknown option: $1"; exit 1 ;;
        *)
            if [[ -z "$PR_NUMBER" ]]; then
                PR_NUMBER="$1"
            fi
            shift
            ;;
    esac
done

if [[ -z "$PR_NUMBER" ]]; then
    echo "Usage: $0 <pr_number> [options]"
    echo "  --skip-lane-1   skip CI evidence collection"
    echo "  --skip-lane-2   skip LLM selector replay"
    echo "  --skip-llm      run Lane 2 without calling claude"
    echo "  --model <m>     model for Lane 2 (default: haiku)"
    echo "  --repo <r>      repo (default: vllm-project/vllm)"
    echo "  --output-dir <d> custom output dir"
    exit 1
fi

if [[ ! -x "$PYTHON" ]]; then
    echo "Error: Python not found at $PYTHON"
    echo "Run: uv venv --python 3.12 && source .venv/bin/activate"
    exit 1
fi

EVIDENCE_DIR="$SKILLS_DIR/evidence/pr_${PR_NUMBER}"
REPLAY_DIR="$SKILLS_DIR/replay/pr_${PR_NUMBER}"
EVAL_DIR="${OUTPUT_DIR:-$SKILLS_DIR/evaluation/pr_${PR_NUMBER}}"
CI_EVIDENCE="$EVIDENCE_DIR/ci_evidence.json"
SELECTOR_REPLAY="$REPLAY_DIR/selector_replay.json"

echo "============================================================"
echo "  PR EVALUATION WORKFLOW"
echo "============================================================"
echo "  PR:     #$PR_NUMBER"
echo "  Repo:   $REPO"
echo "  Output: $EVAL_DIR"
echo "============================================================"

# ---------- Lane 1: collect CI evidence ----------
if [[ "$SKIP_LANE_1" -eq 1 ]]; then
    echo ""
    echo ">>> Skipping Lane 1 (using existing evidence at $CI_EVIDENCE)"
else
    echo ""
    echo ">>> Lane 1: Collecting Buildkite CI evidence..."
    "$PYTHON" "$SCRIPT_DIR/collect_ci_evidence.py" "$PR_NUMBER" --repo "$REPO"
    echo "✓ Lane 1 complete"
fi

# ---------- Lane 2: replay LLM selector ----------
if [[ "$SKIP_LANE_2" -eq 1 ]]; then
    echo ""
    echo ">>> Skipping Lane 2 (using existing replay at $SELECTOR_REPLAY)"
else
    echo ""
    echo ">>> Lane 2: Replaying LLM test selector (model: $MODEL)..."
    LANE2_ARGS=("$PR_NUMBER" "--repo" "$REPO" "--model" "$MODEL")
    if [[ "$SKIP_LLM" -eq 1 ]]; then
        LANE2_ARGS+=("--skip-llm")
        echo "    (LLM call skipped via --skip-llm)"
    fi
    "$PYTHON" "$SCRIPT_DIR/replay_selector.py" "${LANE2_ARGS[@]}"
    echo "✓ Lane 2 complete"
fi

# ---------- Lane 3: compare selector vs CI ----------
echo ""
echo ">>> Lane 3: Comparing selector vs CI results..."

if [[ ! -f "$CI_EVIDENCE" ]]; then
    echo "✗ CI evidence not found at $CI_EVIDENCE"
    echo "  Re-run without --skip-lane-1, or check the PR number."
    exit 1
fi

if [[ ! -f "$SELECTOR_REPLAY" ]]; then
    echo "✗ Selector replay not found at $SELECTOR_REPLAY"
    echo "  Re-run without --skip-lane-2."
    exit 1
fi

LANE3_ARGS=("$PR_NUMBER"
    "--ci-evidence"      "$CI_EVIDENCE"
    "--selector-replay"  "$SELECTOR_REPLAY")
if [[ -n "$OUTPUT_DIR" ]]; then
    LANE3_ARGS+=("--output-dir" "$OUTPUT_DIR")
fi

"$PYTHON" "$SCRIPT_DIR/compare_selector_vs_ci.py" "${LANE3_ARGS[@]}"
echo "✓ Lane 3 complete"

echo ""
echo "============================================================"
echo "  EVALUATION COMPLETE"
echo "============================================================"
echo "  Results: $EVAL_DIR/"
echo "    evaluation_report.json"
echo "    report.md"
echo "============================================================"
