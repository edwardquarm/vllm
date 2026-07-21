# Evaluation Summary — After (v2 Instructions)

> Evaluated using `TEST_SELECTION_v2.md` (Rules 1–9)
> Baseline: `before/SUMMARY.md` using `TEST_SELECTION.md` (Rules 1–5)

## How to Read This Report

The LLM selector reads a PR diff and predicts which CI tests will fail. We compare those
predictions against what actually failed in Buildkite CI.

| Term | Meaning | Impact |
|------|---------|--------|
| **TP (True Positive)**  | LLM selected it AND CI failed it | ✅ Correct prediction |
| **FN (False Negative)** | LLM did NOT select it BUT CI failed it | ❌ Missed failure — dangerous |
| **FP (False Positive)** | LLM selected it BUT CI passed it | ⚠️ Wasted test run — costly, not dangerous |
| **Recall** | `TP / (TP + FN)` — fraction of real failures the LLM caught | Higher = safer |
| **Precision** | `TP / (TP + FP)` — fraction of selections that were real failures | Higher = less waste |

**Ideal state: FN = 0, FP as low as possible.**
FN = 0 means every real CI failure was predicted — you can safely skip everything else.
FP just wastes compute; FN ships bugs. A "select everything" selector achieves FN = 0 trivially
but saves nothing — the goal is FN = 0 with minimal FP.

---

## What the Second Pass Does

The second pass is an additive review step that runs after the primary LLM selector.
It does not redo the initial selection from scratch. Instead, it checks whether the
primary selector missed tests that historically fail for the source areas changed by
the PR.

For each changed `vllm/`, `csrc/`, dependency, or build/config area, the second pass
looks up historical failure patterns generated from past PRs. It then asks whether any
frequently failing CI jobs or test paths are not already covered by the primary
selection.

The second pass only adds a test when all of these are true:

- The changed source area has a historical failure pattern for that test/job.
- The pattern occurred at least two times, so one-off failures are ignored.
- The job maps to a real selectable test path.
- The primary selector did not already cover that path.

Hardware-only jobs such as AMD, Ascend, Intel GPU, XPU, ROCm, HPU, and Neuron jobs are
not added when they have no pytest path mapping. Those jobs are treated as structurally
uncoverable by this selector.

In short: the primary selector predicts tests from the current diff, while the second
pass checks that prediction against historical failure data and appends only missing,
repeatable, selectable coverage.

---

## Overall Results vs Before

| Metric                                    | Before (v1)  | After (v2)   | Change        |
|-------------------------------------------|--------------|--------------|---------------|
| Total PRs evaluated                       | 58           | 58           | —             |
| PRs with CI failures (recall measurable)  | 22           | 33           | +11            |
| **Average Recall** (on PRs with failures) | **0.2%**     | **2.8%**     | **+2.6%**     |
| **Average Precision** (all PRs)           | **30.2%**    | **13.0%**    | **-17.2%**    |
| PRs with recall > 0%                      | 1            | 8            | +7            |

**v2 rules produced a small but measurable improvement.** Recall improved from 0.2% to 2.8% and PRs with any recall rose from 1 to 8. However, 24 of 33 PRs with CI failures still show 0% recall — the new rules alone are not sufficient.

---

## Per-PR Comparison (PRs with CI failures)

| PR      | Before Recall | After Recall | Before TP/FN/FP | After TP/FN/FP | Change              |
|---------|---------------|--------------|-----------------|----------------|---------------------|
| #39337  | 0%            | 7%           | 0/15/0          | 1/13/3         | **Improved** ✅      |
| #39601  | 0%            | 0%           | 0/129/1         | 0/129/1        | —                   |
| #40172  | 0%            | 0%           | 0/18/4          | 0/18/7         | FP +3               |
| #40392  | 0%            | 0%           | 0/2/0           | 0/2/12         | FP +12              |
| #40717  | 0%            | 0%           | 0/20/5          | 0/20/3         | FP -2               |
| #41252  | 0%            | 0%           | 0/6/6           | 0/6/4          | FP -2               |
| #41261  | 5%            | 0%           | 1/21/1          | 0/22/1         | **Regressed** ⚠️    |
| #41471  | 0%            | 0%           | 0/8/4           | 0/8/7          | FP +3               |
| #41802  | 0%            | 0%           | 0/43/1          | 0/43/1         | —                   |
| #41972  | 0%            | 0%           | 0/24/3          | 0/24/5         | FP +2               |
| #41979  | 0%            | 50%          | 0/2/0           | 1/1/9          | **Improved** ✅      |
| #41991  | 0%            | 0%           | 0/20/1          | 0/20/1         | —                   |
| #42070  | 0%            | 0%           | 0/3/3           | 0/3/3          | —                   |
| #42083  | 0%            | 0%           | 0/10/0          | 0/10/3         | FP +3               |
| #42129  | 0%            | 2%           | 0/66/1          | 1/65/1         | **Improved** ✅      |
| #42224  | 0%            | 0%           | 0/5/0           | 0/5/0          | —                   |
| #42288  | 0%            | 0%           | 0/3/0           | 0/3/5          | FP +5               |
| #42343  | 0%            | 0%           | 0/1/2           | 0/0/6          | FP +4               |
| #43167  | 0%            | 20%          | 0/0/0           | 1/4/5          | **Improved** ✅      |
| #43230  | 0%            | 1%           | 0/0/1           | 1/105/0        | **Improved** ✅      |
| #43260  | 0%            | 7%           | 0/0/3           | 1/13/3         | **Improved** ✅      |
| #43325  | 0%            | 0%           | 0/0/4           | 0/8/4          | —                   |
| #43339  | 0%            | 0%           | 0/0/0           | 0/21/6         | FP +6               |
| #43358  | 0%            | 0%           | 0/0/6           | 0/16/3         | FP -3               |
| #43383  | 0%            | 0%           | 0/0/1           | 0/3/5          | FP +4               |
| #43543  | 0%            | 0%           | 0/0/6           | 0/10/6         | —                   |
| #43581  | 0%            | 0%           | 0/6/3           | 0/6/3          | —                   |
| #43720  | 0%            | 3%           | 0/31/0          | 1/29/3         | **Improved** ✅      |
| #43824  | 0%            | 0%           | 0/1/0           | 0/1/0          | —                   |
| #43838  | 0%            | 0%           | 0/14/2          | 0/14/4         | FP +2               |
| #44036  | 0%            | 3%           | 0/0/1           | 1/30/0         | **Improved** ✅      |
| #44244  | 0%            | 0%           | 0/0/6           | 0/59/6         | —                   |
| #44484  | 0%            | 0%           | 0/0/3           | 0/9/2          | FP -1               |
| #44999  | 0%            | 0%           | 0/0/1           | 0/10/11        | FP +10              |

---

## What Improved

### PR #43260 — 0% → 7%
- Selected `tests/renderers/` matched `tests/renderers` — tests rendering/tokenization logic modified in params.py

### PR #39337 — 0% → 7%
- Selected `tests/v1/e2e/` matched `tests/v1/e2e` — v1 worker/scheduler now use vllm_config.use_v2_model_runner property

### PR #42129 — 0% → 2%
- Selected `tests/basic_correctness/` matched `tests/basic_correctness` — safety net for early initialization code changes (Rule 4)

### PR #43720 — 0% → 3%
- Selected `tests/basic_correctness/` matched `tests/basic_correctness` — core engine initialization touched, safety net

### PR #41979 — 0% → 50%
- Selected `tests/basic_correctness/` matched `tests/basic_correctness` — large refactor safety net (Rule 5)

### PR #44036 — 0% → 3%
- Selected `tests/basic_correctness/` matched `tests/basic_correctness` — requirements/cuda.txt changed, dependency version bump (Rule 3)

### PR #43167 — 0% → 20%
- Selected `tests/models/` matched `tests/models` — 24 model files changed, need model-level quantization tests (Rule 2)

### PR #43230 — 0% → 1%
- Selected `tests/basic_correctness/` matched `tests/basic_correctness` — requirements file change (Rule 3)

## What Regressed

### PR #41261 — 5% → 0% ⚠️
- v1 had TP: `tests/basic_correctness/` matched `tests/basic_correctness`

---

## Root Cause Analysis — Why Recall Remains Near Zero

### 1. Hardware-specific jobs have no test path mapping (~40% of misses)
AMD, Ascend NPU, Intel GPU, XPU jobs have no pytest path — they appear as
`[job] X` and cannot be selected regardless of instruction quality.

### 2. LLM (Haiku) under-selects
For 25+ PRs the LLM selected 0–1 tests. New rules added guidance but Haiku
still defaults to conservative output. A stronger model would apply rules more aggressively.

### 3. Path matching was too strict (now fixed)
Directory selections like `tests/v1/core/` did not match individual files within
that directory. Fixed by removing the `break` in `classify_selections()` so all
files within a matched directory are correctly counted as covered.

### 4. Job-to-path mapping gaps in YAML
Many Buildkite jobs are not in the test-area YAML. Even correct LLM selections
appear as false negatives when the job cannot be scored.

## Most Frequently Missed Job Categories (v2)

| Missed Job Type                                    | Count |
|----------------------------------------------------|-------|
| Kernels                                            | 87    |
| Async Engine, Inputs, Utils, Worker, Config        | 82    |
| Fusion and Compile Unit Tests                      | 34    |
| PyTorch Compilation Unit Tests                     | 31    |
| Model Executor                                     | 29    |
| Entrypoints Integration                            | 27    |
| Kernels FP8 MoE Test                               | 20    |
| AMD: Entrypoints Integration (API Server openai - Part 2) | 20    |
| Multi-Modal Models                                 | 19    |
| Distributed Torchrun + Examples                    | 18    |
| Batch Invariance                                   | 18    |
| Spec Decode Draft Model Nightly B200               | 17    |
| Distributed DP Tests                               | 16    |
| Quantized MoE Test                                 | 16    |
| Distributed Model Tests                            | 15    |
