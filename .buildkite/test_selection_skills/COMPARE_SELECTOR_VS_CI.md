---
name: compare_selector_vs_ci
description: Compare LLM selector predictions against actual CI failures for one historical vLLM PR and produce an evaluation report.
---

# Compare Selector vs CI Evidence

## Purpose

Use this skill for Lane 3 of offline historical PR evaluation: comparing the LLM-based test selector's predictions (from Lane 2) against actual Buildkite CI failures (from Lane 1) for the same historical PR.

## Inputs

Required:
- `pr_number`: historical GitHub PR number.
- `ci_evidence_path`: path to `ci_evidence.json` from Lane 1.
- `selector_replay_path`: path to `selector_replay.json` from Lane 2.

Optional:
- `output_dir`: directory for evaluation report. Default: `.buildkite/test_selection_skills/evaluation/pr_<pr_number>/`.

## Outputs

Write these files:
- `evaluation_report.json`: structured evaluation record.
- `evaluation_summary.md`: human-readable markdown report.
- `test_comparison_table.txt`: ASCII table with full CI job list.
- `PR<number>_Comparison.xlsx`: Excel file with 2 sheets.
- `gap_analysis.txt`: detailed analysis of missed failures.

The normalized JSON has this shape:
```json
{
  "pr_number": "<PR #>",
  "evaluation_status": "success | partial | error",
  "summary": {
    "true_positives": 0,
    "false_negatives": 0,
    "false_positives": 0,
    "coverage_rate": 0.0,
    "precision_rate": 0.0
  },
  "true_positive_details": [],
  "false_negative_details": [],
  "false_positive_details": [],
  "gap_analysis": [],
  "recommendations": [],
  "notes": []
}
```

## Metrics Definitions

| Metric | Formula | Target |
|--------|---------|--------|
| True Positives (TP) | Selected tests that failed | Maximize |
| False Negatives (FN) | Failures not selected | Minimize (critical) |
| False Positives (FP) | Selected tests that didn't fail | Acceptable for safety |
| Coverage (Recall) | TP / (TP + FN) | 1.0 (100%) |
| Precision | TP / (TP + FP) | High, but not at expense of coverage |

## Workflow

1. Load `ci_evidence.json` and `selector_replay.json`.
2. Extract failed tests and selected tests.
3. Classify each outcome as TP, FN, or FP.
4. Compute coverage and precision metrics.
5. Generate gap analysis for each false negative.
6. Generate actionable recommendations.
7. Write all output files.
8. Return summary with key metrics.

## Guardrails

- Do not invent matches.
- Do not penalize selector for extra tests if it caught all failures.
- Do not modify source files; this skill only produces reports.
- If CI evidence shows no failures, record as vacuous evaluation.
