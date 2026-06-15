# PR #43167 - Test Selection Evaluation

## Files in This Directory

- **`SUMMARY.md`** - Executive summary ⭐ **START HERE**
- **`test_comparison_table.txt`** - Visual comparison table
- **`evaluation_report.json`** - Machine-readable metrics
- **`pr_43167_actual_failures.md`** - Detailed failure breakdown with correction note
- **`evaluation_summary.md`** - Legacy summary (machine-generated format)
- **`complete_test_list.txt`** - Full list of tests from the Buildkite job

## Key Results

- Coverage (Recall): 0.0%
- Precision: 0.0%
- **Actual Failed Tests: 2** (corrected from earlier incorrect report of 141)
- LLM Selections: 7

## Correction Note

An earlier version of these files reported 141 test failures. The actual Buildkite logs
(`build 70063`) show only **2 failures** total:
1. `test_chat.py::test_invocations` (API response schema mismatch)
2. `test_mistral.py::test_apply_chat_template[...Magistral-Small-2509]` (token mismatch)

Generated: 2026-06-15
