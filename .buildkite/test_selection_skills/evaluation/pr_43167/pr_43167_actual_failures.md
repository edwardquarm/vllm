# PR #43167 - Actual Test Failures from Buildkite Build 70063

## Build Information
- **PR**: https://github.com/vllm-project/vllm/pull/43167
- **Title**: Remove KV cache scale boilerplate from model weight loading methods  
- **Buildkite Build**: 70063 (https://buildkite.com/vllm/ci/builds/70063)
- **Build Status**: FAILED
- **Date**: 2026-06-04

## Summary
- **Total Failed Jobs**: 2
- **Total Failed Tests**: 141

## Failed Job 1: Async Engine, Inputs, Utils, Worker, Config (CPU)

**Failed Tests**: 1

1. `tests/tokenizers_/test_mistral.py::TestMistralTokenizer::test_apply_chat_template[openai_request4-False-True-expected_output4-decoded_expected_output4-mistralai/Magistral-Small-2509]`

**Failure Type**: Assertion error in tokenizer chat template application

---

## Failed Job 2: Entrypoints Integration (API Server openai - Part 1)

**Failed Tests**: 140

All failures are in the `tests/entrypoints/openai/chat_completion/` directory:

### Test Files Affected:
- test_audio.py (5 tests)
- test_audio_in_video.py (3 tests)  
- test_batched_chat_completions.py (2 tests)
- test_chat.py (32 tests) ⚠️ **Most failures**
- test_chat_completion.py (4 tests)
- test_chat_completion_with_mixed_audio_embeds.py (2 tests)
- test_chat_completion_with_mixed_image_embeds.py (2 tests)
- test_chat_completion_with_prompt_embeds.py (8 tests)
- test_chat_echo.py (3 tests)
- test_chat_error.py (13 tests)
- test_chat_logit_bias_validation.py (1 test)
- test_completion_with_function_calling.py (6 tests)
- test_completion_with_image_embeds.py (1 test)
- test_default_mm_loras.py (1 test)
- test_enable_force_include_usage.py (1 test)
- test_root_path.py (1 test)
- test_serving_chat.py (15 tests)
- test_serving_chat_stream_harmony.py (2 tests)
- test_structured_outputs_choice_chat_logprobs.py (1 test)
- test_thinking_token_budget.py (4 tests)
- test_thinking_token_budget_validation.py (6 tests)
- test_video.py (13 tests)
- test_vision.py (13 tests)
- test_vision_embeds.py (2 tests)

### Pattern Analysis:
The failures are concentrated in **OpenAI API chat completion endpoints**, particularly:
- Chat completion with various features (streaming, n-parameter, structured outputs, etc.)
- Multi-modal inputs (vision, audio, video)
- Function/tool calling
- Thinking token budgets
- Prompt embeddings

---

## Root Cause Analysis

The PR changed KV cache scale loading from individual `get_cache_scale` calls in each model's `load_weights` to a centralized `get_cache_scale_mapper` at the top level. This appears to have caused:

1. **Tokenizer-related failure**: Likely indirect - the mistral tokenizer test may be sensitive to model loading changes
2. **Widespread API integration failures**: 140 tests in entrypoints suggest the changes affected how models are initialized/loaded in the API server, breaking the OpenAI-compatible chat completion API

The failures are NOT in quantization tests (which the LLM selector chose), but in:
- Tokenizer integration
- API entrypoint integration with model loading

This is a classic case where refactoring internal APIs (KV cache loading) had unexpected downstream effects on higher-level integration points.

