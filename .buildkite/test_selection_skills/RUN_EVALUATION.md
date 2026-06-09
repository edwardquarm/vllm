---
name: run_pr_evaluation
description: Run the complete 3-lane offline evaluation workflow for a historical PR (collect CI evidence, replay LLM selector, compare results).
---

# Run PR Evaluation Workflow

**Skill Name:** `run_pr_evaluation`

## Usage

Invoke this skill to run the complete 3-lane evaluation workflow for a historical PR.

### Command Format

```
/run_pr_evaluation <pr_number> [options]
```

### Required Argument

- `pr_number` - The GitHub PR number to evaluate (e.g., `43167`)

### Optional Arguments

- `--repo` - Repository name (default: `vllm-project/vllm`)
- `--output-dir` - Custom output directory (default: `.buildkite/test_selection_skills/evaluation/pr_<number>/`)
- `--skip-lane-1` - Skip CI evidence collection (use existing evidence)
- `--skip-lane-2` - Skip LLM selector replay (use existing replay)
- `--dry-run` - Run lanes 1 and 2 but skip lane 3 comparison

## Examples

### Evaluate a PR (full workflow)
```
/run_pr_evaluation 43167
```

### Evaluate with custom repo
```
/run_pr_evaluation 43167 --repo vllm-project/vllm
```

### Re-run comparison only (use existing lane 1 and 2 data)
```
/run_pr_evaluation 43167 --skip-lane-1 --skip-lane-2
```

### Collect evidence only (no comparison)
```
/run_pr_evaluation 43167 --dry-run
```

## What This Skill Does

When invoked, this skill executes all three lanes:

### Lane 1: Collect CI Evidence
- Fetches PR details from GitHub
- Queries Buildkite for the CI build associated with the PR
- Extracts failed jobs and test-level failures
- Writes `ci_evidence.json` to evidence directory

### Lane 2: Replay LLM Selector
- Fetches changed files and diff from GitHub
- Generates candidate test mapping using static import analysis
- Runs LLM selector with `TEST_SELECTION.md` rules
- Writes `selector_replay.json` to replay directory

### Lane 3: Compare Results
- Loads CI evidence and selector replay
- Classifies into True Positives, False Negatives, False Positives
- Computes coverage and precision metrics
- Generates:
  - `evaluation_report.json` (structured data)
  - `evaluation_summary.md` (markdown report)
  - `test_comparison_table.txt` (ASCII table with full CI job list)
  - `PR<number>_Comparison.xlsx` (Excel with 2 sheets)
  - `gap_analysis.txt` (missed failures analysis)

## Output Files

After completion, find all outputs in:
```
.buildkite/test_selection_skills/evaluation/pr_<pr_number>/
```

| File | Description |
|------|-------------|
| `evaluation_report.json` | Structured evaluation metrics |
| `evaluation_summary.md` | Human-readable summary |
| `test_comparison_table.txt` | ASCII table with LLM vs CI comparison |
| `PR<number>_Comparison.xlsx` | Excel file (2 sheets: Lane Comparison + CI Jobs) |
| `gap_analysis.txt` | Analysis of missed failures |

## Prerequisites

- `gh` CLI authenticated
- `claude` CLI authenticated
- Python `.venv` with project dependencies
- Buildkite MCP server access (for test-level failures)

## Skill Implementation

This skill is implemented by the following components:

1. **Skill definition:** `.buildkite/test_selection_skills/RUN_EVALUATION.md` (this file)
2. **Orchestration script:** `.buildkite/test_selection_skills/scripts/run_evaluation.sh`
3. **Lane scripts:**
   - `scripts/collect_ci_evidence.py` (Lane 1)
   - `scripts/replay_selector.py` (Lane 2)
   - `scripts/compare_selector_vs_ci.py` (Lane 3)

## Related Skills

- `collect_buildkite_ci_evidence` - Lane 1 only
- `replay_llm_selector_for_historical_pr` - Lane 2 only
- `compare_selector_vs_ci` - Lane 3 only
