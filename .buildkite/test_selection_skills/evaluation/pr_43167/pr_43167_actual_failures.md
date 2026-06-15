# PR #43167 - Actual Test Failures from Buildkite Build 70063

## Build Information
- **PR**: https://github.com/vllm-project/vllm/pull/43167
- **Title**: Remove KV cache scale boilerplate from model weight loading methods
- **Buildkite Build**: 70063 (https://buildkite.com/vllm/ci/builds/70063)
- **Build Status**: FAILED
- **Date**: 2026-06-04

## Summary

| Job | Failed | Passed | Skipped |
|-----|--------|--------|---------|
| Entrypoints Integration (API Server openai - Part 1) | 1 | 269 | 6 |
| Async Engine, Inputs, Utils, Worker, Config (CPU) | 1 | 657 | 253 |
| **Total** | **2** | **926** | **259** |

## Failed Job 1: Entrypoints Integration (API Server openai - Part 1)

**Failed Tests**: 1

1. `entrypoints/openai/chat_completion/test_chat.py::test_invocations`

**Failure**: `AssertionError: assert dict_keys([...]) == dict_keys([...])`

The response JSON contained an extra `moderation` key not expected by the test:
```
- dict_keys(['id', 'object', 'created', 'model', 'choices', 'service_tier', 'system_fingerprint', 'usage', ...])
+ dict_keys(['id', 'choices', 'created', 'model', 'object', 'moderation', 'service_tier', ...])
```

This is an API **response schema** change, not directly related to KV cache loading.

---

## Failed Job 2: Async Engine, Inputs, Utils, Worker, Config (CPU)

**Failed Tests**: 1

1. `tokenizers_/test_mistral.py::TestMistralTokenizer::test_apply_chat_template[openai_request4-False-True-expected_output4-decoded_expected_output4-mistralai/Magistral-Small-2509]`

**Failure**: Token sequence mismatch — right side contains one extra token `2`.

---

## Correction Note

An earlier analysis of this build incorrectly reported 140 failures in the entrypoints job.
The actual pytest output was: **`1 failed, 269 passed, 6 skipped`**.
The 140 figure was a data collection error (likely confused test files collected vs tests that failed).

---

## What the LLM Selected (7 targets, 0 overlapping with failures)

| Selected | Failed in CI? |
|----------|--------------|
| `tests/model_executor/test_eagle_quantization.py` | No |
| `tests/model_executor/test_weight_utils.py` | No |
| `tests/quantization/test_per_token_kv_cache.py` | No |
| `tests/quantization/test_compressed_tensors.py` | No |
| `tests/quantization/test_fp8.py` | No |
| `tests/quantization/test_configs.py` | No |
| `tests/basic_correctness/` | No |

**Recall: 0%** — The LLM correctly identified the changed code areas (KV cache / quantization)
but missed that the change also affected API response serialization (`test_invocations`) and
indirectly a tokenizer test.
