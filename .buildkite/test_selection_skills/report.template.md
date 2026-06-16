# PR #{{PR_NUMBER}} — Test Selection Evaluation

> **Build**: [{{BUILD_NUMBER}}]({{BUILD_URL}}) · **Date**: {{DATE}} · **Source**: {{DATA_SOURCE}}

## Metrics

| Metric | Value |
|--------|-------|
| **Recall** | **{{RECALL}}** |
| **Precision** | **{{PRECISION}}** |
| True Positives | {{TP}} |
| False Negatives (CI failed, LLM missed) | {{FN}} |
| False Positives (LLM selected, passed) | {{FP}} |

## CI Failures — {{FAILURE_COUNT}} test(s)

<!--
One sub-section per failed CI job. Repeat the block below for each.
If the build passed entirely, write: "No failures — build passed."
-->

### ❌ {{JOB_NAME}}

*{{FAILED}} failed · {{PASSED}} passed · {{SKIPPED}} skipped*

- `{{TEST_ID}}` — {{FAILURE_SUMMARY}}

## LLM Selections — {{SELECTION_COUNT}} target(s)

<!--
✅ = LLM selected AND CI failed (true positive)
➖ = LLM selected, CI passed or did not run (not a caught failure)
-->

| | Target | Reason |
|--|--------|--------|
| ✅ | `{{TARGET}}` | {{REASON}} |
| ➖ | `{{TARGET}}` | {{REASON}} |

## Gap Analysis

<!--
Explain WHY the LLM missed failures and what this teaches us about improving
the selection strategy. Be specific about the failure mode.
-->

**Why the LLM missed:**
- {{MISSED_REASON}}

**To improve coverage:**
- {{IMPROVEMENT}}

---
*Generated: {{DATE}}*
