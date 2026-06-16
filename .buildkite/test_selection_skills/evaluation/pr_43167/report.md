# PR #43167 — Test Selection Evaluation

> **Build**: [70063](https://buildkite.com/vllm/ci/builds/70063) · **Date**: 2026-06-04 · **Source**: Buildkite job logs

## Metrics

| Metric | Value |
|--------|-------|
| **Recall** | **0.0%** |
| **Precision** | **0.0%** |
| True Positives | 0 |
| False Negatives (CI failed, LLM missed) | 2 |
| False Positives (LLM selected, passed) | 7 |

## CI Failures — 2 test(s)

### ❌ Entrypoints Integration (API Server openai - Part 1)

*1 failed · 269 passed · 6 skipped*

- `entrypoints/openai/chat_completion/test_chat.py::test_invocations`

### ❌ Async Engine, Inputs, Utils, Worker, Config (CPU)

*1 failed · 657 passed · 253 skipped*

- `tokenizers_/test_mistral.py::TestMistralTokenizer::test_apply_chat_template[openai_request4-False-True-expected_output4-decoded_expected_output4-mistralai/Magistral-Small-2509]`

## LLM Selections — 7 target(s)

| | Target | Reason |
|--|--------|--------|
| ➖ | `tests/model_executor/test_eagle_quantization.py` | Modified test file - verifies quantization for EAGLE models after test removal |
| ➖ | `tests/model_executor/test_weight_utils.py` | Tests weight loading utilities including maybe_remap_kv_scale_name which was modified |
| ➖ | `tests/quantization/test_per_token_kv_cache.py` | Tests KV cache quantization - directly affected by kv_cache.py changes |
| ➖ | `tests/quantization/test_compressed_tensors.py` | Tests compressed-tensors quantization which uses get_cache_scale_mapper |
| ➖ | `tests/quantization/test_fp8.py` | Tests FP8 quantization config which had get_cache_scale method replaced |
| ➖ | `tests/quantization/test_configs.py` | Tests quantization config base classes modified in this PR |
| ➖ | `tests/basic_correctness/` | Large PR (31 files, 4+ directories) affecting core quantization infrastructure per Rule 5 |

## Gap Analysis

**Why the LLM missed:**
- The LLM traced the direct code path (KV cache loading → quantization tests) but didn't follow the side effect on API response serialization. `test_invocations` asserts on the exact set of keys in the response dict; the PR introduced a `moderation` field the test didn't expect.
- The tokenizer failure is indirect — changes to model loading during refactoring affected the chat template application path for Mistral.

**To improve coverage:**
- Include `entrypoints/openai/` tests whenever model loading or response serialization code changes, even if the change appears to be internal-only.
- Include tokenizer tests when core model initialization is refactored.

---
*Generated: 2026-06-15*
