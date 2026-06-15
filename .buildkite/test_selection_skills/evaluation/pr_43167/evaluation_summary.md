# Evaluation for PR #43167

Coverage: 0.0%

## False Negatives (2)
- entrypoints/openai/chat_completion/test_chat.py::test_invocations
- tokenizers_/test_mistral.py::TestMistralTokenizer::test_apply_chat_template[openai_request4-False-True-expected_output4-decoded_expected_output4-mistralai/Magistral-Small-2509]

## False Positives (7)
- tests/model_executor/test_eagle_quantization.py
- tests/model_executor/test_weight_utils.py
- tests/quantization/test_per_token_kv_cache.py
- tests/quantization/test_compressed_tensors.py
- tests/quantization/test_fp8.py
- tests/quantization/test_configs.py
- tests/basic_correctness/
