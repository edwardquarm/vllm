# PR #{{PR_NUMBER}} — Test Selection Evaluation

> **Build**: [{{BUILD_NUMBER}}]({{BUILD_URL}}) · **Date**: {{DATE}}

## Metrics

| Metric | Value |
|--------|-------|
| **Recall** | **{{RECALL}}** |
| **Precision** | **{{PRECISION}}** |
| True Positives | {{TP}} |
| False Negatives (CI failed, LLM missed) | {{FN}} |
| False Positives (LLM selected, passed) | {{FP}} |

## CI Test Results

| Failed | Passed | Skipped | Total |
|--------|--------|---------|-------|
| {{FAILED}} | {{PASSED}} | {{SKIPPED}} | {{TOTAL}} |

**CI jobs:** {{N_PASSED_JOBS}} passed · {{N_FAILED_JOBS}} failed · {{N_BLOCKED_JOBS}} blocked · **{{N_TEST_FILES}} test files**

## LLM vs CI Comparison Table

```
Test File                                                                                                                      LLM Selected  CI Result
======================================================================================================================================================
{{TEST_FILE_ROW}}
```

**Summary:** {{N_TOTAL_TESTS}} total tests, {{N_LLM_SELECTED}} LLM selected, {{N_CI_FAILED}} CI failed

### Failed jobs

**❌ {{JOB_NAME}}** — {{N}} test(s) failed

- `{{TEST_ID}}`

### Passing jobs

- ✅ {{JOB_NAME}}

## LLM Selections — {{SELECTION_COUNT}} target(s)

<!--
✅ = LLM selected AND CI failed (true positive)
➖ = LLM selected, CI passed or did not run
-->

| | Target | Reason |
|--|--------|--------|
| ✅ | `{{TARGET}}` | {{REASON}} |
| ➖ | `{{TARGET}}` | {{REASON}} |

## Gap Analysis

**Why the LLM missed:**
- {{MISSED_REASON}}

**To improve coverage:**
- {{IMPROVEMENT}}

---
*Generated: {{DATE}}*
