# Skill: run_pr_evaluation

**Command:** `/run_pr_evaluation <pr_number> [--repo <repo>] [--output-dir <dir>] [--skip-lane-1] [--skip-lane-2] [--dry-run]`

**Description:** Run the complete 3-lane offline evaluation workflow for a historical vLLM PR.

## What this skill does

This skill evaluates how well the LLM-based test selector would have caught actual CI failures for a historical PR. It:

1. **Lane 1**: Collects actual Buildkite CI failures for the PR
2. **Lane 2**: Replays the LLM selector to see what tests it would have chosen
3. **Lane 3**: Compares the two to compute coverage and precision metrics

## Usage Examples

```bash
# Full evaluation of PR #43167
/run_pr_evaluation 43167

# Evaluate with custom output directory
/run_pr_evaluation 43167 --output-dir /path/to/output

# Re-run comparison only (use existing lane 1 & 2 data)
/run_pr_evaluation 43167 --skip-lane-1 --skip-lane-2

# Collect evidence and replay selector, but skip comparison
/run_pr_evaluation 43167 --dry-run
```

## Output

After completion, find results in `.buildkite/test_selection_skills/evaluation/pr_<number>/`:

- `evaluation_report.json` - Structured metrics
- `evaluation_summary.md` - Markdown summary
- `test_comparison_table.txt` - ASCII table with full CI job list
- `PR<number>_Comparison.xlsx` - Excel file (2 sheets)
- `gap_analysis.txt` - Missed failures analysis

## Implementation

This skill is implemented by:
- `.buildkite/test_selection_skills/scripts/run_evaluation_skill.py` (orchestrator)
- `.buildkite/test_selection_skills/scripts/collect_ci_evidence.py` (Lane 1)
- `.buildkite/test_selection_skills/scripts/replay_selector.py` (Lane 2)
- `.buildkite/test_selection_skills/scripts/compare_selector_vs_ci.py` (Lane 3)
