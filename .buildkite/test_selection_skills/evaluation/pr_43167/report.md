# PR #43167 — Test Selection Evaluation

> **Build**: [70063](https://buildkite.com/vllm/ci/builds/70063) · **Date**: 2026-06-16 · **Source**: Buildkite job logs (patched)

## Metrics

| Metric | Value |
|--------|-------|
| **Recall** | **0.0%** |
| **Precision** | **0.0%** |
| True Positives | 0 |
| False Negatives (CI failed, LLM missed) | 2 |
| False Positives (LLM selected, passed) | 7 |

## CI Failures — 2 test(s)

*Across failing jobs: 2 failed · 926 passed · 259 skipped*

### ❌ Entrypoints Integration (API Server openai - Part 1)

- `entrypoints/openai/chat_completion/test_chat.py::test_invocations`

### ❌ Async Engine, Inputs, Utils, Worker, Config (CPU)

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
- not in candidate mapping

**To improve coverage:**
- *(fill in after reviewing the failure patterns above)*

---
*Generated: 2026-06-16 04:35 UTC*
