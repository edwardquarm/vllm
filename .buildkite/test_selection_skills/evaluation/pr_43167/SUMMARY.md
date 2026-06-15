# PR #43167 Test Selection Evaluation - SUMMARY

## Quick Facts

| Metric | Value |
|--------|-------|
| PR Number | #43167 |
| Buildkite Build | [70063](https://buildkite.com/vllm/ci/builds/70063) |
| **Coverage (Recall)** | **0.0%** |
| **Precision** | **0.0%** |
| True Positives | 0 |
| **False Negatives** | **2** (LLM missed) |
| False Positives | 7 (LLM selected, did not fail in CI) |

> **Correction**: An earlier version of this report stated 141 failures. The actual Buildkite
> logs show `1 failed, 269 passed, 6 skipped` for the entrypoints job and `1 failed, 657 passed,
> 253 skipped` for the CPU job. Total actual failures: **2**.

## What Actually Failed (2 tests)

### ❌ Entrypoints Integration (API Server openai - Part 1)
**1 test failed:**
- `entrypoints/openai/chat_completion/test_chat.py::test_invocations`

**Failure detail**: `AssertionError` — response `dict_keys` mismatch. The response JSON had an
extra `moderation` field the test didn't expect. This is a response schema change, not a KV
cache logic failure.

**Job stats**: 1 failed, 269 passed, 6 skipped

### ❌ Async Engine, Inputs, Utils, Worker, Config (CPU)
**1 test failed:**
- `tokenizers_/test_mistral.py::TestMistralTokenizer::test_apply_chat_template[openai_request4-False-True-expected_output4-decoded_expected_output4-mistralai/Magistral-Small-2509]`

**Failure detail**: Token sequence mismatch — expected list has one fewer token (missing `2`
at end). Indirect failure from model loading changes.

**Job stats**: 1 failed, 657 passed, 253 skipped (Retry 2 of 2)

## What LLM Selected (7 targets)

- [ ] `tests/model_executor/test_eagle_quantization.py` - Modified test file
- [ ] `tests/model_executor/test_weight_utils.py` - Tests maybe_remap_kv_scale_name
- [ ] `tests/quantization/test_per_token_kv_cache.py` - KV cache quantization
- [ ] `tests/quantization/test_compressed_tensors.py` - Uses get_cache_scale_mapper
- [ ] `tests/quantization/test_fp8.py` - FP8 quantization config changes
- [ ] `tests/quantization/test_configs.py` - Quantization config base classes
- [ ] `tests/basic_correctness/` - Rule 5 broad coverage for large PR

None of the 7 selected tests overlapped with either actual failure.

## Analysis

The LLM correctly identified the changed code areas (KV cache loading, quantization configs)
but missed two failure modes:

1. **API response schema side effect** — the PR touched model serialization paths, and
   `test_invocations` asserts on the exact set of keys in the response dict. The LLM didn't
   consider that internal model-loading changes can affect response serialization.

2. **Indirect tokenizer failure** — the Mistral tokenizer test failed likely due to a change in
   how the model is initialized during the chat template application path.

**To catch these in future runs**: include `entrypoints/openai/` tests when any model loading
or response serialization code changes, and include tokenizer tests when core model init changes.

---
Generated: 2026-06-15 (corrected from initial report)
