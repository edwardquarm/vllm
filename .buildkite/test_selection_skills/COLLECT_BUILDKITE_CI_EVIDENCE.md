---
name: collect_buildkite_ci_evidence
description: Collect historical Buildkite CI evidence for one vLLM PR and write normalized failure evidence for offline test-selection evaluation.
---

# Collect Buildkite CI Evidence

## Purpose

Use this skill for Lane 1 of offline historical PR evaluation: collecting the actual CI outcome for a historical PR from Buildkite. The resulting evidence is used later to compare against an offline replay of the LLM test selector.

## Inputs

Required:
- `pr_number`: historical GitHub PR number to evaluate.

Optional:
- `repo`: repository name. Default: `vllm-project/vllm`.
- `output_dir`: directory for normalized and raw records. Default: `.buildkite/test_selection_skills/evidence/pr_<pr_number>/`.

## Outputs

Write these files:
- `ci_evidence.json`: normalized evidence record.
- `raw/`: raw Buildkite MCP responses.

The normalized JSON has this shape:
```json
{
  "pr_number": "<PR #>",
  "repo": "vllm-project/vllm",
  "status": "success | partial | no_results | error",
  "buildkite_builds": [],
  "jobs_run": [],
  "jobs_failed": [],
  "tests_run": [],
  "tests_failed": [],
  "failed_test_list": [],
  "artifacts": [],
  "notes": []
}
```

## Status Values

- `success`: PR-linked Buildkite results found with test-level failures.
- `partial`: CI results found, but only job-level data available.
- `no_results`: no Buildkite results tied to the PR.
- `error`: querying or parsing failed.

## Workflow

1. Confirm the `pr_number` and output directory.
2. Query Buildkite MCP server for builds associated with the PR.
3. Extract build references, jobs, job outcomes, and test results.
4. Normalize failed tests into `failed_test_list`.
5. Write `ci_evidence.json`.
6. Return summary with status, build count, failed job count, failed test count.

## Guardrails

- Do not guess missing failed tests.
- Do not collapse failed jobs into failed tests unless test-level evidence supports it.
- Preserve useful references (build URL, job name, exit status, retry attempt).
- Record missing or ambiguous data in `notes`.
