# ATS - Automatic Test Selection Evaluation

**ATS (Automatic Test Selection)** - Offline evaluation workflow for LLM-based test selector.

Offline evaluation workflow for the LLM-based test selector.

## Quick Start

### Run Full Evaluation for a PR

```bash
# Using the skill command
/run_pr_evaluation 43167

# Or using bash directly
.buildkite/test_selection_skills/run.sh 43167
```

## Workflow Overview

| Lane | Skill | What It Does |
|------|-------|--------------|
| 1 | `collect_buildkite_ci_evidence` | Fetches actual CI failures from Buildkite |
| 2 | `replay_llm_selector_for_historical_pr` | Replays LLM selector to see what it would pick |
| 3 | `compare_selector_vs_ci` | Compares predictions vs actual failures |

## Output Files

After running, find results in `.buildkite/test_selection_skills/evaluation/pr_<number>/`:

- `evaluation_report.json` - Structured metrics
- `evaluation_summary.md` - Markdown summary
- `test_comparison_table.txt` - ASCII table showing:
  - **All tests run by Buildkite CI** (with PASS/FAIL status)
  - **All tests selected by LLM**
  - **Comparison**: Did LLM select a subset? Did it miss failures?
- `PR<number>_Comparison.xlsx` - Excel (2 sheets: Lane Comparison + CI Jobs)

## Important Note: Test Run Data

The comparison table shows **all tests run by CI** when test run data is available. Currently:

- **Test failures** are automatically collected from Buildkite
- **Full test run list** requires manual population (Buildkite Test Engine API integration pending)

To populate test run data manually:
1. Run Lane 1 and Lane 2
2. Edit `evidence/pr_<number>/ci_evidence.json` and add test data to `tests_run` array
3. Re-run Lane 3: `python scripts/compare_selector_vs_ci.py <pr_number> --ci-evidence ... --selector-replay ...`

## Commands

```bash
# Full evaluation
/run_pr_evaluation <pr_number>

# Example
/run_pr_evaluation 43167

# With options
/run_pr_evaluation 43167 --skip-lane-1 --skip-lane-2  # Re-run comparison only
```

## Requirements

- `gh` CLI authenticated
- `claude` CLI authenticated
- Python `.venv` with `openpyxl` (for Excel output)

## Skill Files

- `RUN_EVALUATION.md` - Main skill definition
- `COLLECT_BUILDKITE_CI_EVIDENCE.md` - Lane 1 skill
- `REPLAY_LLM_SELECTOR_FOR_HISTORICAL_PR.md` - Lane 2 skill
- `COMPARE_SELECTOR_VS_CI.md` - Lane 3 skill

## Scripts

- `scripts/run_evaluation_skill.py` - Orchestrator
- `scripts/collect_ci_evidence.py` - Lane 1
- `scripts/replay_selector.py` - Lane 2
- `scripts/compare_selector_vs_ci.py` - Lane 3
- `run.sh` - Bash wrapper
