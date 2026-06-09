#!/bin/bash
# Quick wrapper to run the PR evaluation workflow
# Usage: .buildkite/test_selection_skills/run.sh <pr_number>

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
PYTHON="$REPO_ROOT/.venv/bin/python"

if [ -z "$1" ]; then
    echo "Usage: $0 <pr_number>"
    echo "Example: $0 43167"
    exit 1
fi

exec "$PYTHON" "$SCRIPT_DIR/scripts/run_evaluation_skill.py" "$@"
