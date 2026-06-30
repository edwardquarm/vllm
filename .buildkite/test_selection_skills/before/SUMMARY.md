# Evaluation Summary — Before (v1 Instructions)

> Evaluated using `TEST_SELECTION.md` (Rules 1–5)

## Overall Results

| Metric                                    | Value        |
|-------------------------------------------|--------------|
| Total PRs evaluated                       | 58           |
| PRs with CI failures (recall measurable)  | 22           |
| PRs with no CI failures                   | 36           |
| **Average Recall** (on PRs with failures) | **0.2%**      |
| **Average Precision** (all PRs)           | **30.2%**     |
| PRs with recall > 0%                      | 1            |

**The LLM catches very few CI failures under v1.** Of 22 PRs where CI broke, only 1 had any recall at all. The rest show 0% — the LLM selected tests but none matched the actual failures, or it selected nothing relevant. The primary gap is hardware-specific jobs (AMD, Ascend NPU, Intel GPU, XPU) and subprocess/HTTP-based tests, which have no representation in the static import mapping.

---

## Per-PR Breakdown

| PR      | Recall | TP | FN  | FP | Notes                          |
|---------|--------|----|-----|----|--------------------------------|
| #39337  | 0%     | 0  | 15  | 0  | Missed all, no FP              |
| #39601  | 0%     | 0  | 129 | 1  | Large — 129 failures           |
| #40172  | 0%     | 0  | 18  | 4  |                                |
| #40392  | 0%     | 0  | 2   | 0  | Missed all, no FP              |
| #40717  | 0%     | 0  | 20  | 5  |                                |
| #41252  | 0%     | 0  | 6   | 6  |                                |
| #41261  | 5%     | 1  | 21  | 1  | ✅ Only PR with recall          |
| #41471  | 0%     | 0  | 8   | 4  |                                |
| #41802  | 0%     | 0  | 43  | 1  |                                |
| #41972  | 0%     | 0  | 24  | 3  |                                |
| #41979  | 0%     | 0  | 2   | 0  | Missed all, no FP              |
| #41991  | 0%     | 0  | 20  | 1  |                                |
| #42070  | 0%     | 0  | 3   | 3  |                                |
| #42083  | 0%     | 0  | 10  | 0  | Missed all, no FP              |
| #42129  | 0%     | 0  | 66  | 1  | Large — 66 failures            |
| #42224  | 0%     | 0  | 5   | 0  | Missed all, no FP              |
| #42288  | 0%     | 0  | 3   | 0  | Missed all, no FP              |
| #42343  | 0%     | 0  | 1   | 2  |                                |
| #43581  | 0%     | 0  | 6   | 3  |                                |
| #43720  | 0%     | 0  | 31  | 0  | Missed all, no FP              |
| #43824  | 0%     | 0  | 1   | 0  | Missed all, no FP              |
| #43838  | 0%     | 0  | 14  | 2  |                                |

---

## Most Frequently Missed Job Categories

| Missed Job Type                              | Count | Gap in Instructions         |
|----------------------------------------------|-------|-----------------------------|
| Kernels                                      | 41    | Partially covered — kernel subsets missing |
| Async Engine, Inputs, Utils, Worker, Config  | 40    | CPU variant not distinguished from GPU |
| PyTorch Compilation Unit Tests               | 26    | No rule for compilation jobs |
| Fusion and Compile Unit Tests                | 25    | Not mapped in instructions  |
| Spec Decode Draft Model                      | 23    | Rule 2 covers some paths, not all |
| Distributed DP Tests                         | 16    | No dedicated distributed rule |
| Distributed Model Tests                      | 15    | No dedicated distributed rule |
| Quantized MoE Test                           | 15    | Not mapped in instructions  |
| Model Executor                               | 14    | Not mapped in instructions  |
| V1 Core + KV + Metrics                       | 13    | No metrics/tracing rule in v1 |
| RayExecutorV2                                | 13    | Not mapped in instructions  |
| V1 Sample + Logits                           | 12    | Not mapped in instructions  |

---

## Root Causes

### 1. Hardware-specific tests have no test path mapping
AMD, Ascend NPU, Intel GPU, and XPU jobs fail regularly when shared code changes
but v1 has no rules for them. They appear as `[job] X` in the evaluation —
no corresponding pytest path exists for the LLM to select.

### 2. Subprocess and HTTP-based tests are invisible to import analysis
Tests like `test_openai_server.py` hit a running vLLM server via HTTP.
The import graph cannot see through subprocess or HTTP boundaries, so these
tests never appear in the candidate mapping.

### 3. CPU-variant jobs not distinguished
Jobs like 'Async Engine, Inputs, Utils, Worker, Config (CPU)' are separate
Buildkite jobs from their GPU counterparts. v1 treats them generically.

### 4. LLM (Haiku) is conservative
For many PRs the LLM selected 0–1 tests. Even when rules apply, Haiku
defaults to minimal output.
