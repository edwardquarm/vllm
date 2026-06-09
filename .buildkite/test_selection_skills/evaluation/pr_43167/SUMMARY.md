# PR #43167 Test Selection Evaluation - SUMMARY

## Quick Facts

| Metric | Value |
|--------|-------|
| PR Number | [#43167](https://github.com/vllm-project/vllm/pull/43167) |
| Title | Remove KV cache scale boilerplate from model weight loading methods |
| Buildkite Build | [70063](https://buildkite.com/vllm/ci/builds/70063) |
| Build Status | ❌ FAILED |
| **Coverage (Recall)** | **0.0%** |
| **Precision** | **0.0%** |
| True Positives | 0 |
| **False Negatives** | **141** (LLM missed) |
| False Positives | 7 (LLM selected but passed) |

## What Actually Failed

### ❌ Job 1: Async Engine, Inputs, Utils, Worker, Config (CPU)
**1 test failed:**
- `tests/tokenizers_/test_mistral.py::TestMistralTokenizer::test_apply_chat_template[...]`

### ❌ Job 2: Entrypoints Integration (API Server openai - Part 1)  
**140 tests failed:**
- All in `tests/entrypoints/openai/chat_completion/`
- Top failures:
  - `test_chat.py` (32 tests)
  - `test_serving_chat.py` (15 tests)
  - `test_chat_error.py` (13 tests)
  - `test_video.py` (13 tests)
  - `test_vision.py` (13 tests)
  - Plus 19 more test files

## What LLM Selected (All Passed ✓)

The LLM selected **7 test targets**, all focused on quantization:
1. ✓ `tests/model_executor/test_eagle_quantization.py`
2. ✓ `tests/model_executor/test_weight_utils.py`
3. ✓ `tests/quantization/test_per_token_kv_cache.py`
4. ✓ `tests/quantization/test_compressed_tensors.py`
5. ✓ `tests/quantization/test_fp8.py`
6. ✓ `tests/quantization/test_configs.py`
7. ✓ `tests/basic_correctness/`

## The Gap

```
PR Changes:        Internal API refactoring of KV cache scale loading
                   ↓
LLM Selected:      Low-level quantization & model executor tests ✓
                   ↓
What Broke:        High-level API integration layer ❌
                   • OpenAI chat completion API (140 tests)
                   • Tokenizer integration (1 test)
```

## Why The LLM Missed

1. **Focused on direct code changes** (kv_cache.py, quantization configs)
2. **Didn't consider downstream integration effects**
3. **No API entrypoint tests selected** despite model loading changes
4. **Missed tokenizer integration dependencies**

## Root Cause

The PR refactored how KV cache scales are loaded during model initialization:
- **Before:** Each model's `load_weights` method called `get_cache_scale`
- **After:** Centralized `get_cache_scale_mapper` at AutoWeightsLoader level

This internal change broke:
- Model initialization in API server context
- OpenAI-compatible chat completion endpoints  
- Tokenizer integration (indirect dependency)

## Key Lessons

### For Test Selection:
- ✅ **Test the entire call stack** for internal API refactoring
- ✅ **Include API entrypoints** when core model code changes
- ✅ **Consider integration layers** not just unit tests
- ✅ **"Boilerplate removal" needs broad testing**

### For This PR Specifically:
- Should have selected: `tests/entrypoints/openai/chat_completion/`
- Should have selected: `tests/tokenizers_/`
- The quantization tests were reasonable but insufficient

## Data Quality Note

✅ **High Quality Data**  
This evaluation used actual test execution results from Buildkite API logs, not inferred from pipeline configurations.

- Source: Buildkite Build 70063 job logs
- Method: Parsed pytest output from failed jobs
- Result: 141 concrete failing test names (not job-level estimates)

## Files Generated

1. `test_comparison_table.txt` - Visual comparison of LLM vs CI
2. `pr_43167_actual_failures.md` - Detailed failure breakdown
3. `evaluation_report.json` - Machine-readable metrics
4. `SUMMARY.md` - This file

---

**Generated:** 2026-06-09  
**Data Source:** Buildkite API (Build 70063)
