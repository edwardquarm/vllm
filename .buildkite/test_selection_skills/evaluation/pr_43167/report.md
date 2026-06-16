# PR #43167 — Test Selection Evaluation

> **Build**: [70063](https://buildkite.com/vllm/ci/builds/70063) · **Date**: 2026-06-16

## Metrics

| Metric | Value |
|--------|-------|
| **Recall** | **0.0%** |
| **Precision** | **0.0%** |
| True Positives | 0 |
| False Negatives (CI failed, LLM missed) | 2 |
| False Positives (LLM selected, passed) | 7 |

## CI Test Results

| Failed | Passed | Skipped | Total |
|--------|--------|---------|-------|
| 2 | 926 | 259 | 1187 |

**CI jobs:** 64 passed · 3 failed · 305 blocked

### Failed jobs

**❌ Entrypoints Integration (API Server openai - Part 1)** — 1 test(s) failed

- `entrypoints/openai/chat_completion/test_chat.py::test_invocations`

**❌ Async Engine, Inputs, Utils, Worker, Config (CPU)** — 1 test(s) failed

- `tokenizers_/test_mistral.py::TestMistralTokenizer::test_apply_chat_template[openai_request4-False-True-expected_output4-decoded_expected_output4-mistralai/Magistral-Small-2509]`

### Passing jobs

- ✅ bootstrap
- ✅ :docker: :smoking: Non-root smoke tests
- ✅ :docker: Build CPU image
- ✅ :docker: Build HPU image
- ✅ :docker: Build image
- ✅ Basic Correctness
- ✅ Benchmarks CLI Test
- ✅ Distributed Compile Unit Tests (2xH100)
- ✅ Fusion E2E Quick (H100)
- ✅ Fusion E2E TP2 (B200)
- ✅ Fusion E2E TP2 Quick (H100)
- ✅ Fusion and Compile Unit Tests (2xB200)
- ✅ Sequence Parallel Correctness Tests (2 GPUs)
- ✅ Pipeline + Context Parallelism (4 GPUs)
- ✅ Entrypoints Integration (API Server 2)
- ✅ Entrypoints Integration (API Server openai - Part 1)
- ✅ Entrypoints Integration (API Server openai - Part 2)
- ✅ Entrypoints Integration (API Server openai - Part 3)
- ✅ Entrypoints Integration (LLM)
- ✅ Entrypoints Integration (Pooling)
- ✅ Entrypoints Integration (Responses API)
- ✅ Entrypoints Integration (Speech to Text)
- ✅ Kernels DeepGEMM Test (H100)
- ✅ Kernels FusedMoE Layer Test (2 B200s)
- ✅ Kernels FusedMoE Layer Test (2 H100s)
- ✅ Kernels Quantization Test 1
- ✅ Kernels Quantization Test 2
- ✅ LM Eval Small Models
- ✅ Async Engine, Inputs, Utils, Worker
- ✅ Async Engine, Inputs, Utils, Worker, Config (CPU)
- ✅ Batch Invariance (A100)
- ✅ Batch Invariance (B200)
- ✅ Batch Invariance (H100)
- ✅ Metrics, Tracing (2 GPUs)
- ✅ Regression
- ✅ V1 Core + KV + Metrics
- ✅ V1 Sample + Logits
- ✅ V1 Spec Decode
- ✅ Model Executor
- ✅ Basic Models Test (Other CPU)
- ✅ Basic Models Tests (Extra Initialization) 1
- ✅ Basic Models Tests (Extra Initialization) 2
- ✅ Basic Models Tests (Initialization)
- ✅ Basic Models Tests (Other)
- ✅ Distributed Model Tests (2 GPUs)
- ✅ Language Models Tests (Extra Standard) 1
- ✅ Language Models Tests (Extra Standard) 2
- ✅ Language Models Tests (Hybrid) 1
- ✅ Language Models Tests (Hybrid) 2
- ✅ Language Models Tests (Standard)
- ✅ Multi-Modal Models (Standard) 1: qwen2
- ✅ Multi-Modal Models (Standard) 2: qwen3 + gemma
- ✅ Multi-Modal Models (Standard) 4: other + whisper
- ✅ Multi-Modal Processor
- ✅ Multi-Modal Processor (CPU)
- ✅ PyTorch Compilation Passes Unit Tests
- ✅ PyTorch Compilation Unit Tests
- ✅ PyTorch Compilation Unit Tests (H100)
- ✅ PyTorch Fullgraph
- ✅ PyTorch Fullgraph Smoke Test
- ✅ Quantization
- ✅ Quantized MoE Test (B200)
- ✅ Quantized Models Test
- ✅ Samplers Test

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
- *(fill in after reviewing the failures above)*

**To improve coverage:**
- *(fill in)*

---
*Generated: 2026-06-16 04:47 UTC*
