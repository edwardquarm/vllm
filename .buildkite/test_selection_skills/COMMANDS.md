# Test Selection Evaluation - Command Reference

## Primary Command

### Run Full Evaluation Workflow

**Command:**
```
/run_pr_evaluation <pr_number>
```

**Example:**
```
/run_pr_evaluation 43167
```

**What it does:**
Runs all 3 lanes of the evaluation workflow:
1. Collects Buildkite CI evidence for the PR
2. Replays the LLM test selector
3. Compares predictions vs actual failures

**Output:**
Results saved to `.buildkite/test_selection_skills/evaluation/pr_<pr_number>/`

---

## Alternative Commands

### Using bash wrapper directly
```bash
.buildkite/test_selection_skills/run.sh 43167
```

### Using Python script directly
```bash
.venv/bin/python .buildkite/test_selection_skills/scripts/run_evaluation_skill.py 43167
```

### Using the orchestration script
```bash
.buildkite/test_selection_skills/scripts/run_evaluation.sh 43167
```

---

## Lane-Specific Commands

### Lane 1 Only: Collect CI Evidence
```bash
.venv/bin/python .buildkite/test_selection_skills/scripts/collect_ci_evidence.py 43167
```

### Lane 2 Only: Replay LLM Selector
```bash
.venv/bin/python .buildkite/test_selection_skills/scripts/replay_selector.py 43167
```

### Lane 3 Only: Compare Results
```bash
.venv/bin/python .buildkite/test_selection_skills/scripts/compare_selector_vs_ci.py 43167 \
    --ci-evidence .buildkite/test_selection_skills/evidence/pr_43167/ci_evidence.json \
    --selector-replay .buildkite/test_selection_skills/replay/pr_43167/selector_replay.json
```

---

## Command Options for /run_pr_evaluation

| Option | Description |
|--------|-------------|
| `--repo <repo>` | Repository name (default: vllm-project/vllm) |
| `--output-dir <dir>` | Custom output directory |
| `--skip-lane-1` | Skip CI evidence collection |
| `--skip-lane-2` | Skip LLM selector replay |
| `--dry-run` | Run lanes 1-2 but skip lane 3 comparison |

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────┐
│  PR EVALUATION WORKFLOW COMMANDS                            │
├─────────────────────────────────────────────────────────────┤
│  Full evaluation:                                           │
│    /run_pr_evaluation 43167                                 │
│                                                             │
│  Re-run comparison only:                                    │
│    /run_pr_evaluation 43167 --skip-lane-1 --skip-lane-2     │
│                                                             │
│  View results:                                              │
│    cat .buildkite/test_selection_skills/evaluation/pr_43167/│
│        evaluation_summary.md                                │
│    cat .buildkite/test_selection_skills/evaluation/pr_43167/│
│        test_comparison_table.txt                            │
└─────────────────────────────────────────────────────────────┘
```
