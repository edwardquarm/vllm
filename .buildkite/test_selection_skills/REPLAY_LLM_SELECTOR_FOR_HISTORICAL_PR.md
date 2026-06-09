---
name: replay_llm_selector_for_historical_pr
description: Replay the LLM-based test selector offline for one historical vLLM PR and write normalized selected-test evidence for comparison.
---

# Replay LLM Selector for Historical PR

## Purpose

Use this skill for Lane 2 of offline historical PR evaluation: replaying the LLM-based test selector against the inputs from a historical PR. The resulting record captures what the selector would have chosen so it can later be compared against historical Buildkite CI evidence.

## Inputs

Required:
- `pr_number`: historical GitHub PR number to evaluate.
- Historical changed files and/or diff for the PR.
- Test dependency input (generated candidate mapping from `build_test_mapping.py`).
- Test selection rules from `.buildkite/TEST_SELECTION.md`.

Optional:
- `repo`: repository name. Default: `vllm-project/vllm`.
- `output_dir`: directory for replay inputs and outputs. Default: `.buildkite/test_selection_skills/replay/pr_<pr_number>/`.

## Outputs

Write these files:
- `selector_replay.json`: normalized replay record.
- `inputs/changed_files.txt`: changed files used for replay.
- `inputs/diff.patch`: diff used for replay.
- `inputs/candidate_mapping.md`: generated test dependency input.
- `inputs/test_selection_rules.md`: copy of selection rules.
- `raw_selector_output.txt`: exact LLM selector output.

The normalized JSON has this shape:
```json
{
  "pr_number": "<PR #>",
  "repo": "vllm-project/vllm",
  "status": "success | partial | missing_inputs | error",
  "changed_files": [],
  "diff_summary": "",
  "llm_selected_tests": [],
  "selection_reasons": [],
  "notes": []
}
```

## Status Values

- `success`: selector replay completed with selected tests.
- `partial`: selector replay completed but output was incomplete.
- `missing_inputs`: required replay inputs were unavailable.
- `error`: replay failed.

## Workflow

1. Fetch PR details (changed files, diff, base/head refs).
2. Generate candidate mapping using `build_test_mapping.py --files`.
3. Read `TEST_SELECTION.md` rules.
4. Construct LLM selector prompt.
5. Run LLM selector offline via `claude -p --model haiku`.
6. Parse selected tests and reasons.
7. Write `selector_replay.json`.
8. Return summary with selected test count and input quality.

## Guardrails

- Do not guess missing selector inputs.
- Do not invent test names or directories.
- Preserve selector's original granularity.
- If selector returns `NONE`, record empty list with reason in notes.
