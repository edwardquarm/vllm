# PR #44036 — Test Selection Evaluation

> **Build**: [69606](https://buildkite.com/vllm/ci/builds/69606) · **Date**: 2026-06-27

## Metrics

| Metric | Value |
|--------|-------|
| **Recall** | **0.0%** |
| **Precision** | **0.0%** |
| True Positives | 0 |
| False Negatives (CI failed, LLM missed) | 23 |
| False Positives (LLM selected, passed) | 1 |

## CI Test Results

| Failed | Passed | Skipped | Total |
|--------|--------|---------|-------|
| 0 | 0 | 0 | 0 |

**CI jobs:** 183 passed · 4 failed · 141 blocked · **254 test files**

## LLM vs CI Comparison Table

```
Test File                                                                                                                      LLM Selected  CI Result
======================================================================================================================================================
[job] Ascend NPU Test                                                                                                          ✗             ✗ Failed 
tests/.                                                                                                                        ✗             ✓ Passed 
tests/./compile                                                                                                                ✗             ✓ Passed 
tests/./compile/fullgraph                                                                                                      ✗             ✓ Passed 
tests/./compile/fullgraph/test_basic_correctness.py                                                                            ✗             ✓ Passed 
tests/./compile/test_wrapper.py                                                                                                ✗             ✓ Passed 
tests/./plugins_tests                                                                                                          ✗             ✓ Passed 
tests/./plugins_tests/test_io_processor_plugins.py                                                                             ✗             ✓ Passed 
tests/basic_correctness                                                                                                        ✓             ✓ Passed 
tests/basic_correctness/test_basic_correctness.py                                                                              ✗             ✓ Passed 
tests/basic_correctness/test_cpu_offload.py                                                                                    ✗             ✓ Passed 
tests/basic_correctness/test_cumem.py                                                                                          ✗             ✓ Passed 
tests/benchmarks                                                                                                               ✗             ✓ Passed 
tests/compile                                                                                                                  ✗             ✓ Passed 
tests/compile/correctness_e2e                                                                                                  ✗             ✓ Passed 
tests/compile/correctness_e2e/test_async_tp.py                                                                                 ✗             ✓ Passed 
tests/compile/correctness_e2e/test_sequence_parallel.py                                                                        ✗             ✓ Passed 
tests/compile/fullgraph                                                                                                        ✗             ✓ Passed 
tests/compile/fullgraph/test_basic_correctness.py                                                                              ✗             ✓ Passed 
tests/compile/fullgraph/test_full_graph.py                                                                                     ✗             ✓ Passed 
tests/compile/fullgraph/test_full_graph.py::test_fp8_kv_scale_compile                                                          ✗             ✓ Passed 
tests/compile/fusions_e2e                                                                                                      ✗             ✓ Passed 
tests/compile/fusions_e2e/test_tp1_quant.py                                                                                    ✗             ✓ Passed 
tests/compile/fusions_e2e/test_tp2_ar_rms.py                                                                                   ✗             ✓ Passed 
tests/compile/fusions_e2e/test_tp2_async_tp.py                                                                                 ✗             ✓ Passed 
tests/compile/passes                                                                                                           ✗             ✓ Passed 
tests/compile/passes/distributed                                                                                               ✗             ✓ Passed 
tests/compile/passes/distributed/test_fusion_all_reduce.py                                                                     ✗             ✓ Passed 
tests/compile/passes/test_fusion_attn.py                                                                                       ✗             ✓ Passed 
tests/compile/passes/test_mla_attn_quant_fusion.py                                                                             ✗             ✓ Passed 
tests/compile/passes/test_silu_mul_quant_fusion.py                                                                             ✗             ✓ Passed 
tests/config                                                                                                                   ✗             ✗ Failed 
tests/cuda                                                                                                                     ✗             ✓ Passed 
tests/cuda/test_cuda_context.py                                                                                                ✗             ✓ Passed 
tests/cuda/test_platform_no_cuda_init.py                                                                                       ✗             ✓ Passed 
tests/detokenizer                                                                                                              ✗             ✓ Passed 
tests/distributed                                                                                                              ✗             ✓ Passed 
tests/distributed/test_comm_ops.py                                                                                             ✗             ✓ Passed 
tests/distributed/test_context_parallel.py                                                                                     ✗             ✓ Passed 
tests/distributed/test_custom_all_reduce.py                                                                                    ✗             ✓ Passed 
tests/distributed/test_distributed_oot.py                                                                                      ✗             ✓ Passed 
tests/distributed/test_elastic_ep.py                                                                                           ✗             ✓ Passed 
tests/distributed/test_eplb_algo.py                                                                                            ✗             ✓ Passed 
tests/distributed/test_eplb_execute.py                                                                                         ✗             ✓ Passed 
tests/distributed/test_eplb_spec_decode.py                                                                                     ✗             ✓ Passed 
tests/distributed/test_eplb_utils.py                                                                                           ✗             ✓ Passed 
tests/distributed/test_events.py                                                                                               ✗             ✓ Passed 
tests/distributed/test_multi_node_assignment.py                                                                                ✗             ✓ Passed 
tests/distributed/test_multiproc_executor.py::test_multiproc_executor_multi_node                                               ✗             ✓ Passed 
tests/distributed/test_nccl_symm_mem_allreduce.py                                                                              ✗             ✓ Passed 
tests/distributed/test_packed_tensor.py                                                                                        ✗             ✓ Passed 
tests/distributed/test_pipeline_parallel.py                                                                                    ✗             ✓ Passed 
tests/distributed/test_pp_cudagraph.py                                                                                         ✗             ✓ Passed 
tests/distributed/test_pynccl.py                                                                                               ✗             ✓ Passed 
tests/distributed/test_ray_v2_executor.py                                                                                      ✗             ✓ Passed 
tests/distributed/test_ray_v2_executor_e2e.py                                                                                  ✗             ✓ Passed 
tests/distributed/test_shm_broadcast.py                                                                                        ✗             ✓ Passed 
tests/distributed/test_shm_buffer.py                                                                                           ✗             ✓ Passed 
tests/distributed/test_shm_storage.py                                                                                          ✗             ✓ Passed 
tests/distributed/test_symm_mem_allreduce.py                                                                                   ✗             ✓ Passed 
tests/distributed/test_utils.py                                                                                                ✗             ✓ Passed 
tests/distributed/test_weight_transfer.py                                                                                      ✗             ✓ Passed 
tests/engine                                                                                                                   ✗             ✓ Passed 
tests/entrypoints                                                                                                              ✗             ✗ Failed 
tests/entrypoints/llm                                                                                                          ✗             ✓ Passed 
tests/entrypoints/llm/test_collective_rpc.py                                                                                   ✗             ✓ Passed 
tests/entrypoints/llm/test_generate.py                                                                                         ✗             ✓ Passed 
tests/entrypoints/llm/test_struct_output_generate.py                                                                           ✗             ✓ Passed 
tests/entrypoints/offline_mode                                                                                                 ✗             ✓ Passed 
tests/entrypoints/openai                                                                                                       ✗             ✓ Passed 
tests/entrypoints/openai/chat_completion                                                                                       ✗             ✓ Passed 
tests/entrypoints/openai/chat_completion/test_oot_registration.py                                                              ✗             ✓ Passed 
tests/entrypoints/openai/completion                                                                                            ✗             ✓ Passed 
tests/entrypoints/openai/completion/test_tensorizer_entrypoint.py                                                              ✗             ✓ Passed 
tests/entrypoints/openai/correctness                                                                                           ✗             ✓ Passed 
tests/entrypoints/openai/correctness/test_lmeval.py::test_lm_eval_accuracy_v1_engine                                           ✗             ✓ Passed 
tests/entrypoints/openai/responses                                                                                             ✗             ✓ Passed 
tests/entrypoints/openai/speech_to_text                                                                                        ✗             ✓ Passed 
tests/entrypoints/openai/test_multi_api_servers.py                                                                             ✗             ✓ Passed 
tests/entrypoints/openai/tool_parsers                                                                                          ✗             ✓ Passed 
tests/entrypoints/pooling                                                                                                      ✗             ✓ Passed 
tests/entrypoints/rpc                                                                                                          ✗             ✗ Failed 
tests/entrypoints/serve                                                                                                        ✗             ✗ Failed 
tests/entrypoints/serve/instrumentator                                                                                         ✗             ✗ Failed 
tests/entrypoints/test_chat_utils.py                                                                                           ✗             ✓ Passed 
tests/evals                                                                                                                    ✗             ✓ Passed 
tests/evals/gpt_oss                                                                                                            ✗             ✓ Passed 
tests/evals/gpt_oss/test_gpqa_correctness.py                                                                                   ✗             ✓ Passed 
tests/evals/gsm8k                                                                                                              ✗             ✓ Passed 
tests/evals/gsm8k/test_gsm8k_correctness.py                                                                                    ✗             ✓ Passed 
tests/ir                                                                                                                       ✗             ✓ Passed 
tests/kernels                                                                                                                  ✗             ✓ Passed 
tests/kernels/attention                                                                                                        ✗             ✓ Passed 
tests/kernels/attention/test_attention_selector.py                                                                             ✗             ✓ Passed 
tests/kernels/attention/test_cutlass_mla_decode.py                                                                             ✗             ✓ Passed 
tests/kernels/attention/test_deepgemm_attention.py                                                                             ✗             ✓ Passed 
tests/kernels/attention/test_flashinfer.py                                                                                     ✗             ✓ Passed 
tests/kernels/attention/test_flashinfer_mla_decode.py                                                                          ✗             ✓ Passed 
tests/kernels/attention/test_flashinfer_trtllm_attention.py                                                                    ✗             ✓ Passed 
tests/kernels/core                                                                                                             ✗             ✓ Passed 
tests/kernels/core/test_minimax_reduce_rms.py                                                                                  ✗             ✓ Passed 
tests/kernels/helion                                                                                                           ✗             ✓ Passed 
tests/kernels/ir                                                                                                               ✗             ✓ Passed 
tests/kernels/mamba                                                                                                            ✗             ✓ Passed 
tests/kernels/moe                                                                                                              ✗             ✓ Passed 
tests/kernels/moe/test_batched_deepgemm.py                                                                                     ✗             ✓ Passed 
tests/kernels/moe/test_block_fp8.py                                                                                            ✗             ✓ Passed 
tests/kernels/moe/test_block_int8.py                                                                                           ✗             ✓ Passed 
tests/kernels/moe/test_cutedsl_moe.py                                                                                          ✗             ✓ Passed 
tests/kernels/moe/test_cutlass_moe.py                                                                                          ✗             ✓ Passed 
tests/kernels/moe/test_deepep_deepgemm_moe.py                                                                                  ✗             ✓ Passed 
tests/kernels/moe/test_deepep_moe.py                                                                                           ✗             ✓ Passed 
tests/kernels/moe/test_deepgemm.py                                                                                             ✗             ✓ Passed 
tests/kernels/moe/test_flashinfer.py                                                                                           ✗             ✓ Passed 
tests/kernels/moe/test_flashinfer_moe.py                                                                                       ✗             ✓ Passed 
tests/kernels/moe/test_gpt_oss_triton_kernels.py                                                                               ✗             ✓ Passed 
tests/kernels/moe/test_modular_oai_triton_moe.py                                                                               ✗             ✓ Passed 
tests/kernels/moe/test_moe.py                                                                                                  ✗             ✓ Passed 
tests/kernels/moe/test_moe_layer.py                                                                                            ✗             ✓ Passed 
tests/kernels/moe/test_mxfp4_moe.py                                                                                            ✗             ✓ Passed 
tests/kernels/moe/test_nvfp4_moe.py                                                                                            ✗             ✓ Passed 
tests/kernels/moe/test_ocp_mx_moe.py                                                                                           ✗             ✓ Passed 
tests/kernels/moe/test_triton_moe_no_act_mul.py                                                                                ✗             ✓ Passed 
tests/kernels/moe/test_triton_moe_ptpc_fp8.py                                                                                  ✗             ✓ Passed 
tests/kernels/quantization                                                                                                     ✗             ✓ Passed 
tests/kernels/quantization/test_block_fp8.py                                                                                   ✗             ✓ Passed 
tests/kernels/quantization/test_cutlass_scaled_mm.py                                                                           ✗             ✓ Passed 
tests/kernels/quantization/test_flashinfer_nvfp4_scaled_mm.py                                                                  ✗             ✓ Passed 
tests/kernels/quantization/test_flashinfer_scaled_mm.py                                                                        ✗             ✓ Passed 
tests/kernels/quantization/test_mxfp4_qutlass.py                                                                               ✗             ✓ Passed 
tests/kernels/quantization/test_nvfp4_quant.py                                                                                 ✗             ✓ Passed 
tests/kernels/quantization/test_nvfp4_qutlass.py                                                                               ✗             ✓ Passed 
tests/kernels/quantization/test_nvfp4_scaled_mm.py                                                                             ✗             ✓ Passed 
tests/kernels/quantization/test_silu_mul_nvfp4_quant.py                                                                        ✗             ✓ Passed 
tests/kernels/test_top_k_per_row.py                                                                                            ✗             ✓ Passed 
tests/lora                                                                                                                     ✗             ✓ Passed 
tests/lora/test_chatglm3_tp.py                                                                                                 ✗             ✓ Passed 
tests/lora/test_gptoss_tp.py                                                                                                   ✗             ✓ Passed 
tests/lora/test_llama_tp.py                                                                                                    ✗             ✓ Passed 
tests/lora/test_llm_with_multi_loras.py                                                                                        ✗             ✓ Passed 
tests/lora/test_mixtral.py                                                                                                     ✗             ✓ Passed 
tests/lora/test_olmoe_tp.py                                                                                                    ✗             ✓ Passed 
tests/lora/test_qwen35_densemodel_lora.py                                                                                      ✗             ✓ Passed 
tests/model_executor                                                                                                           ✗             ✓ Passed 
tests/model_executor/model_loader                                                                                              ✗             ✓ Passed 
tests/model_executor/model_loader/test_sharded_state_loader.py                                                                 ✗             ✓ Passed 
tests/models                                                                                                                   ✗             ✓ Passed 
tests/models/language                                                                                                          ✗             ✓ Passed 
tests/models/language/generation                                                                                               ✗             ✓ Passed 
tests/models/language/generation_ppl_test                                                                                      ✗             ✓ Passed 
tests/models/language/pooling                                                                                                  ✗             ✓ Passed 
tests/models/language/pooling_mteb_test                                                                                        ✗             ✓ Passed 
tests/models/multimodal                                                                                                        ✗             ✓ Passed 
tests/models/multimodal/generation                                                                                             ✗             ✓ Passed 
tests/models/multimodal/generation/test_common.py                                                                              ✗             ✓ Passed 
tests/models/multimodal/generation/test_memory_leak.py                                                                         ✗             ✓ Passed 
tests/models/multimodal/generation/test_phi4siglip.py                                                                          ✗             ✓ Passed 
tests/models/multimodal/generation/test_qwen2_5_vl.py                                                                          ✗             ✓ Passed 
tests/models/multimodal/generation/test_qwen2_vl.py                                                                            ✗             ✓ Passed 
tests/models/multimodal/generation/test_ultravox.py                                                                            ✗             ✓ Passed 
tests/models/multimodal/generation/test_vit_cudagraph.py                                                                       ✗             ✓ Passed 
tests/models/multimodal/generation/test_whisper.py                                                                             ✗             ✓ Passed 
tests/models/multimodal/pooling                                                                                                ✗             ✓ Passed 
tests/models/multimodal/processing                                                                                             ✗             ✓ Passed 
tests/models/multimodal/processing/test_tensor_schema.py                                                                       ✗             ✓ Passed 
tests/models/multimodal/test_mapping.py                                                                                        ✗             ✓ Passed 
tests/models/quantization                                                                                                      ✗             ✓ Passed 
tests/models/quantization/test_nvfp4.py                                                                                        ✗             ✓ Passed 
tests/models/test_initialization.py                                                                                            ✗             ✓ Passed 
tests/models/test_initialization.py::test_can_initialize_small_subset                                                          ✗             ✓ Passed 
tests/models/test_oot_registration.py                                                                                          ✗             ✓ Passed 
tests/models/test_terratorch.py                                                                                                ✗             ✓ Passed 
tests/models/test_transformers.py                                                                                              ✗             ✓ Passed 
tests/models/test_utils.py                                                                                                     ✗             ✓ Passed 
tests/multimodal                                                                                                               ✗             ✗ Failed 
tests/plugins                                                                                                                  ✗             ✓ Passed 
tests/plugins/lora_resolvers                                                                                                   ✗             ✓ Passed 
tests/plugins_tests                                                                                                            ✗             ✓ Passed 
tests/plugins_tests/test_bge_m3_sparse_io_processor_plugins.py                                                                 ✗             ✓ Passed 
tests/plugins_tests/test_platform_plugins.py                                                                                   ✗             ✓ Passed 
tests/plugins_tests/test_scheduler_plugins.py                                                                                  ✗             ✓ Passed 
tests/plugins_tests/test_stats_logger_plugins.py                                                                               ✗             ✓ Passed 
tests/plugins_tests/test_terratorch_io_processor_plugins.py                                                                    ✗             ✓ Passed 
tests/quantization                                                                                                             ✗             ✓ Passed 
tests/quantization/test_blackwell_moe.py                                                                                       ✗             ✓ Passed 
tests/quantization/test_cutlass_w4a16.py                                                                                       ✗             ✓ Passed 
tests/reasoning                                                                                                                ✗             ✗ Failed 
tests/renderers                                                                                                                ✗             ✗ Failed 
tests/samplers                                                                                                                 ✗             ✓ Passed 
tests/so                                                                                                                       ✗             ✓ Passed 
tests/test_inputs.py                                                                                                           ✗             ✗ Failed 
tests/test_lm_eval_correctness.py                                                                                              ✗             ✓ Passed 
tests/test_outputs.py                                                                                                          ✗             ✗ Failed 
tests/test_pooling_params.py                                                                                                   ✗             ✗ Failed 
tests/test_ray_env.py                                                                                                          ✗             ✗ Failed 
tests/test_regression.py                                                                                                       ✗             ✓ Passed 
tests/tokenizers_                                                                                                              ✗             ✗ Failed 
tests/tool_parsers                                                                                                             ✗             ✗ Failed 
tests/tool_use                                                                                                                 ✗             ✗ Failed 
tests/transformers_utils                                                                                                       ✗             ✗ Failed 
tests/utils_                                                                                                                   ✗             ✓ Passed 
tests/v1                                                                                                                       ✗             ✗ Failed 
tests/v1/attention                                                                                                             ✗             ✓ Passed 
tests/v1/core                                                                                                                  ✗             ✓ Passed 
tests/v1/cudagraph                                                                                                             ✗             ✓ Passed 
tests/v1/cudagraph/test_cudagraph_dispatch.py                                                                                  ✗             ✓ Passed 
tests/v1/cudagraph/test_cudagraph_mode.py                                                                                      ✗             ✓ Passed 
tests/v1/determinism                                                                                                           ✗             ✗ Failed 
tests/v1/determinism/test_batch_invariance.py                                                                                  ✗             ✗ Failed 
tests/v1/determinism/test_batch_invariance.py::test_v1_generation_is_deterministic_across_batch_sizes_with_needle[FLASH_ATTN]  ✗             ✗ Failed 
tests/v1/determinism/test_batch_invariance.py::test_v1_generation_is_deterministic_across_batch_sizes_with_needle[TRITON_MLA]  ✗             ✗ Failed 
tests/v1/determinism/test_nvfp4_batch_invariant.py                                                                             ✗             ✓ Passed 
tests/v1/determinism/test_rms_norm_batch_invariant.py                                                                          ✗             ✗ Failed 
tests/v1/distributed                                                                                                           ✗             ✓ Passed 
tests/v1/distributed/test_async_llm_dp.py                                                                                      ✗             ✓ Passed 
tests/v1/distributed/test_dbo.py                                                                                               ✗             ✓ Passed 
tests/v1/distributed/test_eagle_dp.py                                                                                          ✗             ✓ Passed 
tests/v1/distributed/test_external_lb_dp.py                                                                                    ✗             ✓ Passed 
tests/v1/distributed/test_hybrid_lb_dp.py                                                                                      ✗             ✓ Passed 
tests/v1/distributed/test_internal_lb_dp.py                                                                                    ✗             ✓ Passed 
tests/v1/e2e                                                                                                                   ✗             ✓ Passed 
tests/v1/e2e/general                                                                                                           ✗             ✓ Passed 
tests/v1/e2e/general/test_async_scheduling.py                                                                                  ✗             ✓ Passed 
tests/v1/e2e/general/test_context_length.py                                                                                    ✗             ✓ Passed 
tests/v1/e2e/general/test_min_tokens.py                                                                                        ✗             ✓ Passed 
tests/v1/e2e/spec_decode                                                                                                       ✗             ✓ Passed 
tests/v1/e2e/spec_decode/test_spec_decode.py                                                                                   ✗             ✓ Passed 
tests/v1/e2e/test_hybrid_chunked_prefill.py                                                                                    ✗             ✓ Passed 
tests/v1/engine                                                                                                                ✗             ✓ Passed 
tests/v1/engine/test_engine_core_client.py::test_kv_cache_events_dp                                                            ✗             ✓ Passed 
tests/v1/engine/test_llm_engine.py                                                                                             ✗             ✓ Passed 
tests/v1/engine/test_preprocess_error_handling.py                                                                              ✗             ✓ Passed 
tests/v1/executor                                                                                                              ✗             ✓ Passed 
tests/v1/kv_connector                                                                                                          ✗             ✓ Passed 
tests/v1/kv_connector/unit                                                                                                     ✗             ✓ Passed 
tests/v1/kv_offload                                                                                                            ✗             ✓ Passed 
tests/v1/logits_processors                                                                                                     ✗             ✓ Passed 
tests/v1/metrics                                                                                                               ✗             ✓ Passed 
tests/v1/sample                                                                                                                ✗             ✓ Passed 
tests/v1/shutdown                                                                                                              ✗             ✓ Passed 
tests/v1/spec_decode                                                                                                           ✗             ✓ Passed 
tests/v1/spec_decode/test_acceptance_length.py                                                                                 ✗             ✓ Passed 
tests/v1/spec_decode/test_max_len.py                                                                                           ✗             ✓ Passed 
tests/v1/spec_decode/test_probabilistic_rejection_sampler_utils.py                                                             ✗             ✓ Passed 
tests/v1/spec_decode/test_speculators_dflash.py                                                                                ✗             ✓ Passed 
tests/v1/spec_decode/test_synthetic_rejection_sampler_utils.py                                                                 ✗             ✓ Passed 
tests/v1/structured_output                                                                                                     ✗             ✓ Passed 
tests/v1/test_oracle.py                                                                                                        ✗             ✓ Passed 
tests/v1/test_outputs.py                                                                                                       ✗             ✓ Passed 
tests/v1/test_request.py                                                                                                       ✗             ✓ Passed 
tests/v1/test_serial_utils.py                                                                                                  ✗             ✓ Passed 
tests/v1/tracing                                                                                                               ✗             ✓ Passed 
tests/v1/worker                                                                                                                ✗             ✓ Passed 
tests/v1/worker/test_worker_memory_snapshot.py                                                                                 ✗             ✓ Passed 
```

**Summary:** 254 total tests, 1 LLM selected, 23 CI failed

### Failed jobs

**❌ Ascend NPU Test** — 1 test(s) failed

- `[job] Ascend NPU Test`

**❌ Async Engine, Inputs, Utils, Worker, Config (CPU)** — 11 test(s) failed

- `tests/config`
- `tests/multimodal`
- `tests/reasoning`
- `tests/renderers`
- `tests/test_inputs.py`
- `tests/test_outputs.py`
- `tests/test_pooling_params.py`
- `tests/test_ray_env.py`
- `tests/tokenizers_`
- `tests/tool_parsers`
- `tests/transformers_utils`

**❌ Batch Invariance (H100)** — 6 test(s) failed

- `tests/v1`
- `tests/v1/determinism`
- `tests/v1/determinism/test_batch_invariance.py`
- `tests/v1/determinism/test_batch_invariance.py::test_v1_generation_is_deterministic_across_batch_sizes_with_needle[FLASH_ATTN]`
- `tests/v1/determinism/test_batch_invariance.py::test_v1_generation_is_deterministic_across_batch_sizes_with_needle[TRITON_MLA]`
- `tests/v1/determinism/test_rms_norm_batch_invariant.py`

**❌ Entrypoints Integration (API Server 2)** — 5 test(s) failed

- `tests/entrypoints`
- `tests/entrypoints/rpc`
- `tests/entrypoints/serve`
- `tests/entrypoints/serve/instrumentator`
- `tests/tool_use`

### Passing jobs

**✅ :docker: :smoking: Non-root smoke tests**

- (test paths unknown)

**✅ :docker: Build CPU image**

- (test paths unknown)

**✅ :docker: Build HPU image**

- (test paths unknown)

**✅ :docker: Build arm64 image**

- (test paths unknown)

**✅ :docker: Build image**

- (test paths unknown)

**✅ :memo: Annotate ROCm wheel release**

- (test paths unknown)

**✅ :python: Build vLLM ROCm Wheel - x86_64**

- (test paths unknown)

**✅ :rocm: Build ROCm Base Image & Wheels**

- (test paths unknown)

**✅ :s3: Upload ROCm Wheels to S3**

- (test paths unknown)

**✅ AMD: :docker: build image**

- (test paths unknown)

**✅ AMD: Engine (1 GPU) (mi325_1)**

- (test paths unknown)

**✅ AMD: Entrypoints Integration (API Server 2) (mi325_1)**

- (test paths unknown)

**✅ AMD: Entrypoints Integration (API Server openai - Part 1) (mi325_1)**

- (test paths unknown)

**✅ AMD: Entrypoints Integration (API Server openai - Part 2) (mi325_1)**

- (test paths unknown)

**✅ AMD: Entrypoints Integration (API Server openai - Part 3) (mi325_1)**

- (test paths unknown)

**✅ AMD: Entrypoints Integration (LLM) (mi325_1)**

- (test paths unknown)

**✅ AMD: Kernels Quantization Test 1 (mi325_1)**

- (test paths unknown)

**✅ AMD: Kernels Quantization Test 2 (mi325_1)**

- (test paths unknown)

**✅ AMD: Language Models Tests (Hybrid) 1 (mi325_1)**

- (test paths unknown)

**✅ AMD: Language Models Tests (Hybrid) 2 (mi325_1)**

- (test paths unknown)

**✅ AMD: Multi-Modal Models (Standard) 1: qwen2 (mi325_1)**

- (test paths unknown)

**✅ AMD: Multi-Modal Models (Standard) 2: qwen3 + gemma (mi325_1)**

- (test paths unknown)

**✅ AMD: Multi-Modal Models (Standard) 3: llava + qwen2_vl (mi325_1)**

- (test paths unknown)

**✅ AMD: Samplers Test (mi250_1)**

- (test paths unknown)

**✅ AMD: V1 Sample + Logits (mi325_1)**

- (test paths unknown)

**✅ AMD: e2e Scheduling (1 GPU) (mi250_1)**

- (test paths unknown)

**✅ Arm CPU Test**

- (test paths unknown)

**✅ Async Engine, Inputs, Utils, Worker**

- `tests/detokenizer`
- `tests/multimodal`
- `tests/utils_`

**✅ Basic Correctness**

- `tests/basic_correctness`
- `tests/basic_correctness/test_basic_correctness.py`
- `tests/basic_correctness/test_cpu_offload.py`
- `tests/basic_correctness/test_cumem.py`

**✅ Basic Models Test (Other CPU)**

- (test paths unknown)

**✅ Basic Models Tests (Extra Initialization) 1**

- (test paths unknown)

**✅ Basic Models Tests (Extra Initialization) 2**

- (test paths unknown)

**✅ Basic Models Tests (Initialization)**

- `tests/models`
- `tests/models/test_initialization.py::test_can_initialize_small_subset`

**✅ Basic Models Tests (Other)**

- `tests/models`
- `tests/models/test_terratorch.py`

**✅ Batch Invariance (A100)**

- (test paths unknown)

**✅ Batch Invariance (B200)**

- `tests/v1`
- `tests/v1/determinism`
- `tests/v1/determinism/test_batch_invariance.py`
- `tests/v1/determinism/test_batch_invariance.py::test_v1_generation_is_deterministic_across_batch_sizes_with_needle[FLASH_ATTN]`
- `tests/v1/determinism/test_batch_invariance.py::test_v1_generation_is_deterministic_across_batch_sizes_with_needle[TRITON_MLA]`
- `tests/v1/determinism/test_nvfp4_batch_invariant.py`
- `tests/v1/determinism/test_rms_norm_batch_invariant.py`

**✅ Benchmarks CLI Test**

- `tests/benchmarks`

**✅ Bootstrap**

- (test paths unknown)

**✅ Build wheel - aarch64 - CPU**

- (test paths unknown)

**✅ Build wheel - aarch64 - CUDA 12.9**

- (test paths unknown)

**✅ Build wheel - aarch64 - CUDA 13.0**

- (test paths unknown)

**✅ Build wheel - x86_64 - CPU**

- (test paths unknown)

**✅ Build wheel - x86_64 - CUDA 12.9**

- (test paths unknown)

**✅ Build wheel - x86_64 - CUDA 13.0**

- (test paths unknown)

**✅ CPU-Compatibility Tests**

- (test paths unknown)

**✅ CPU-Distributed Tests (DP+TP)**

- (test paths unknown)

**✅ CPU-Distributed Tests (PP+TP)**

- (test paths unknown)

**✅ CPU-Kernel Tests**

- (test paths unknown)

**✅ CPU-Language Generation and Pooling Model Tests**

- (test paths unknown)

**✅ CPU-ModelRunnerV2 Tests**

- (test paths unknown)

**✅ CPU-Multi-Modal Model Tests 1**

- (test paths unknown)

**✅ CPU-Multi-Modal Model Tests 2**

- (test paths unknown)

**✅ CPU-Multi-Modal Model Tests 3**

- (test paths unknown)

**✅ CPU-Quantization Model Tests**

- (test paths unknown)

**✅ CrossLayer KV layout Distributed NixlConnector PD accuracy tests (4 GPUs)**

- (test paths unknown)

**✅ Cudagraph**

- `tests/v1`
- `tests/v1/cudagraph`
- `tests/v1/cudagraph/test_cudagraph_dispatch.py`
- `tests/v1/cudagraph/test_cudagraph_mode.py`

**✅ DP EP Distributed NixlConnector PD accuracy tests (4 GPUs)**

- (test paths unknown)

**✅ Deepseek V4 Kernel Test (B200)**

- (test paths unknown)

**✅ Deepseek V4 Kernel Test (H100)**

- (test paths unknown)

**✅ Distributed Comm Ops**

- `tests/distributed`
- `tests/distributed/test_comm_ops.py`
- `tests/distributed/test_shm_broadcast.py`
- `tests/distributed/test_shm_buffer.py`
- `tests/distributed/test_shm_storage.py`

**✅ Distributed Compile + Comm (4 GPUs)**

- `tests/compile`
- `tests/compile/fullgraph`
- `tests/compile/fullgraph/test_basic_correctness.py`
- `tests/distributed`
- `tests/distributed/test_events.py`
- `tests/distributed/test_multiproc_executor.py::test_multiproc_executor_multi_node`
- `tests/distributed/test_pynccl.py`
- `tests/distributed/test_symm_mem_allreduce.py`

**✅ Distributed Compile + RPC Tests (2 GPUs)**

- `tests/.`
- `tests/./compile`
- `tests/./compile/fullgraph`
- `tests/./compile/fullgraph/test_basic_correctness.py`
- `tests/./compile/test_wrapper.py`
- `tests/entrypoints`
- `tests/entrypoints/llm`
- `tests/entrypoints/llm/test_collective_rpc.py`

**✅ Distributed Compile Unit Tests (2xH100)**

- `tests/compile`
- `tests/compile/passes`
- `tests/compile/passes/distributed`

**✅ Distributed DP Tests (2 GPUs)**

- `tests/entrypoints`
- `tests/entrypoints/openai`
- `tests/entrypoints/openai/test_multi_api_servers.py`
- `tests/v1`
- `tests/v1/distributed`
- `tests/v1/distributed/test_async_llm_dp.py`
- `tests/v1/distributed/test_eagle_dp.py`
- `tests/v1/distributed/test_external_lb_dp.py`

**✅ Distributed DP Tests (4 GPUs)**

- `tests/distributed`
- `tests/distributed/test_utils.py`
- `tests/v1`
- `tests/v1/distributed`
- `tests/v1/distributed/test_async_llm_dp.py`
- `tests/v1/distributed/test_eagle_dp.py`
- `tests/v1/distributed/test_external_lb_dp.py`
- `tests/v1/distributed/test_hybrid_lb_dp.py`
- `tests/v1/distributed/test_internal_lb_dp.py`
- `tests/v1/engine`
- `tests/v1/engine/test_engine_core_client.py::test_kv_cache_events_dp`

**✅ Distributed FlashInfer NixlConnector PD accuracy (4 GPUs)**

- (test paths unknown)

**✅ Distributed Model Tests (2 GPUs)**

- `tests/basic_correctness`
- `tests/model_executor`
- `tests/model_executor/model_loader`
- `tests/model_executor/model_loader/test_sharded_state_loader.py`
- `tests/models`
- `tests/models/language`
- `tests/models/multimodal`
- `tests/models/multimodal/generation`
- `tests/models/multimodal/generation/test_phi4siglip.py`
- `tests/models/multimodal/generation/test_whisper.py`
- `tests/models/test_transformers.py`

**✅ Distributed NixlConnector PD accuracy (4 GPUs)**

- (test paths unknown)

**✅ Distributed Tests (8 GPUs)(H100)**

- (test paths unknown)

**✅ Distributed Torchrun + Examples (4 GPUs)**

- (test paths unknown)

**✅ Distributed Torchrun + Shutdown Tests (2 GPUs)**

- `tests/v1`
- `tests/v1/shutdown`
- `tests/v1/worker`
- `tests/v1/worker/test_worker_memory_snapshot.py`

**✅ Docker Build Metadata**

- (test paths unknown)

**✅ EPLB Algorithm**

- `tests/distributed`
- `tests/distributed/test_eplb_algo.py`
- `tests/distributed/test_eplb_utils.py`

**✅ EPLB Execution**

- (test paths unknown)

**✅ Elastic EP Scaling Test**

- `tests/distributed`
- `tests/distributed/test_elastic_ep.py`

**✅ Engine**

- `tests/engine`

**✅ Engine (1 GPU)**

- `tests/v1`
- `tests/v1/engine`
- `tests/v1/engine/test_preprocess_error_handling.py`

**✅ Entrypoints Integration (API Server openai - Part 1)**

- `tests/entrypoints`
- `tests/entrypoints/openai`
- `tests/entrypoints/openai/chat_completion`

**✅ Entrypoints Integration (API Server openai - Part 2)**

- `tests/entrypoints`
- `tests/entrypoints/openai`
- `tests/entrypoints/openai/completion`
- `tests/entrypoints/openai/speech_to_text`
- `tests/entrypoints/test_chat_utils.py`

**✅ Entrypoints Integration (API Server openai - Part 3)**

- `tests/entrypoints`
- `tests/entrypoints/openai`

**✅ Entrypoints Integration (LLM)**

- `tests/entrypoints`
- `tests/entrypoints/llm`
- `tests/entrypoints/llm/test_generate.py`
- `tests/entrypoints/offline_mode`

**✅ Entrypoints Integration (Pooling)**

- `tests/entrypoints`
- `tests/entrypoints/pooling`

**✅ Entrypoints Integration (Responses API)**

- `tests/entrypoints`
- `tests/entrypoints/openai`
- `tests/entrypoints/openai/responses`

**✅ Entrypoints Integration (Speech to Text)**

- (test paths unknown)

**✅ Entrypoints Unit Tests**

- `tests/entrypoints`
- `tests/entrypoints/openai`
- `tests/entrypoints/openai/tool_parsers`

**✅ Examples**

- (test paths unknown)

**✅ Extract Hidden States Integration**

- (test paths unknown)

**✅ Fusion E2E Config Sweep (H100)**

- `tests/compile`
- `tests/compile/fusions_e2e`
- `tests/compile/fusions_e2e/test_tp1_quant.py`

**✅ Fusion E2E Quick (H100)**

- `tests/compile`
- `tests/compile/fusions_e2e`
- `tests/compile/fusions_e2e/test_tp1_quant.py`

**✅ Fusion E2E TP2 (B200)**

- `tests/compile`
- `tests/compile/fusions_e2e`
- `tests/compile/fusions_e2e/test_tp2_ar_rms.py`
- `tests/compile/fusions_e2e/test_tp2_async_tp.py`

**✅ Fusion E2E TP2 AR-RMS Config Sweep (H100)**

- `tests/compile`
- `tests/compile/fusions_e2e`
- `tests/compile/fusions_e2e/test_tp2_ar_rms.py`

**✅ Fusion E2E TP2 AsyncTP Config Sweep (H100)**

- `tests/compile`
- `tests/compile/fusions_e2e`
- `tests/compile/fusions_e2e/test_tp2_async_tp.py`

**✅ Fusion E2E TP2 Quick (H100)**

- `tests/compile`
- `tests/compile/fusions_e2e`
- `tests/compile/fusions_e2e/test_tp2_ar_rms.py`
- `tests/compile/fusions_e2e/test_tp2_async_tp.py`

**✅ Fusion and Compile Unit Tests (2xB200)**

- `tests/compile`
- `tests/compile/fullgraph`
- `tests/compile/fullgraph/test_full_graph.py::test_fp8_kv_scale_compile`
- `tests/compile/passes`
- `tests/compile/passes/distributed`
- `tests/compile/passes/distributed/test_fusion_all_reduce.py`
- `tests/compile/passes/test_fusion_attn.py`
- `tests/compile/passes/test_mla_attn_quant_fusion.py`
- `tests/compile/passes/test_silu_mul_quant_fusion.py`

**✅ Generate and upload wheel indices**

- (test paths unknown)

**✅ Hybrid SSM NixlConnector PD accuracy tests (4 GPUs)**

- (test paths unknown)

**✅ Kernels (B200)**

- `tests/kernels`
- `tests/kernels/attention`
- `tests/kernels/attention/test_attention_selector.py`
- `tests/kernels/attention/test_cutlass_mla_decode.py`
- `tests/kernels/attention/test_flashinfer.py`
- `tests/kernels/attention/test_flashinfer_mla_decode.py`
- `tests/kernels/attention/test_flashinfer_trtllm_attention.py`
- `tests/kernels/moe`
- `tests/kernels/moe/test_cutedsl_moe.py`
- `tests/kernels/moe/test_flashinfer.py`
- `tests/kernels/moe/test_flashinfer_moe.py`
- `tests/kernels/moe/test_mxfp4_moe.py`
- `tests/kernels/moe/test_nvfp4_moe.py`
- `tests/kernels/moe/test_ocp_mx_moe.py`
- `tests/kernels/quantization`
- `tests/kernels/quantization/test_cutlass_scaled_mm.py`
- `tests/kernels/quantization/test_flashinfer_nvfp4_scaled_mm.py`
- `tests/kernels/quantization/test_flashinfer_scaled_mm.py`
- `tests/kernels/quantization/test_mxfp4_qutlass.py`
- `tests/kernels/quantization/test_nvfp4_quant.py`
- `tests/kernels/quantization/test_nvfp4_qutlass.py`
- `tests/kernels/quantization/test_nvfp4_scaled_mm.py`
- `tests/kernels/quantization/test_silu_mul_nvfp4_quant.py`
- `tests/kernels/test_top_k_per_row.py`
- `tests/models`
- `tests/models/quantization`
- `tests/models/quantization/test_nvfp4.py`

**✅ Kernels Attention Test 1**

- (test paths unknown)

**✅ Kernels Attention Test 2**

- (test paths unknown)

**✅ Kernels Core Operation Test**

- `tests/kernels`
- `tests/kernels/core`

**✅ Kernels DeepGEMM Test (H100)**

- `tests/kernels`
- `tests/kernels/attention`
- `tests/kernels/attention/test_deepgemm_attention.py`
- `tests/kernels/moe`
- `tests/kernels/moe/test_batched_deepgemm.py`
- `tests/kernels/moe/test_deepgemm.py`
- `tests/kernels/quantization`
- `tests/kernels/quantization/test_block_fp8.py`
- `tests/quantization`
- `tests/quantization/test_cutlass_w4a16.py`

**✅ Kernels FusedMoE Layer Test (2 B200s)**

- `tests/kernels`
- `tests/kernels/moe`
- `tests/kernels/moe/test_moe_layer.py`

**✅ Kernels FusedMoE Layer Test (2 H100s)**

- `tests/kernels`
- `tests/kernels/moe`
- `tests/kernels/moe/test_moe_layer.py`

**✅ Kernels Helion Test**

- `tests/kernels`
- `tests/kernels/helion`

**✅ Kernels KDA Test**

- (test paths unknown)

**✅ Kernels Mamba Test**

- `tests/kernels`
- `tests/kernels/mamba`

**✅ Kernels MiniMax Reduce RMS Test (2 GPUs)**

- `tests/kernels`
- `tests/kernels/core`
- `tests/kernels/core/test_minimax_reduce_rms.py`

**✅ Kernels MoE Test 1**

- (test paths unknown)

**✅ Kernels MoE Test 2**

- (test paths unknown)

**✅ Kernels MoE Test 3**

- (test paths unknown)

**✅ Kernels MoE Test 4**

- (test paths unknown)

**✅ Kernels MoE Test 5**

- (test paths unknown)

**✅ Kernels Quantization Test 1**

- (test paths unknown)

**✅ Kernels Quantization Test 2**

- (test paths unknown)

**✅ LM Eval Small Models**

- `tests/evals`
- `tests/evals/gsm8k`
- `tests/evals/gsm8k/test_gsm8k_correctness.py`
- `tests/test_lm_eval_correctness.py`

**✅ LM Eval TurboQuant KV Cache**

- `tests/evals`
- `tests/evals/gsm8k`
- `tests/evals/gsm8k/test_gsm8k_correctness.py`

**✅ Language Models Tests (Extra Standard) 1**

- (test paths unknown)

**✅ Language Models Tests (Extra Standard) 2**

- (test paths unknown)

**✅ Language Models Tests (Hybrid) 1**

- (test paths unknown)

**✅ Language Models Tests (Hybrid) 2**

- (test paths unknown)

**✅ Language Models Tests (Standard)**

- `tests/models`
- `tests/models/language`

**✅ LoRA 1**

- (test paths unknown)

**✅ LoRA 2**

- (test paths unknown)

**✅ LoRA 3**

- (test paths unknown)

**✅ LoRA 4**

- (test paths unknown)

**✅ LoRA TP (Distributed)**

- `tests/lora`
- `tests/lora/test_chatglm3_tp.py`
- `tests/lora/test_gptoss_tp.py`
- `tests/lora/test_llama_tp.py`
- `tests/lora/test_llm_with_multi_loras.py`
- `tests/lora/test_olmoe_tp.py`
- `tests/lora/test_qwen35_densemodel_lora.py`

**✅ MRCR Eval Small Models**

- (test paths unknown)

**✅ Metrics, Tracing (2 GPUs)**

- `tests/v1`
- `tests/v1/tracing`

**✅ Model Executor**

- `tests/entrypoints`
- `tests/entrypoints/openai`
- `tests/entrypoints/openai/completion`
- `tests/entrypoints/openai/completion/test_tensorizer_entrypoint.py`
- `tests/model_executor`

**✅ Model Runner V2 Core Tests**

- `tests/entrypoints`
- `tests/entrypoints/llm`
- `tests/entrypoints/llm/test_struct_output_generate.py`
- `tests/v1`
- `tests/v1/e2e`
- `tests/v1/e2e/general`
- `tests/v1/e2e/general/test_async_scheduling.py`
- `tests/v1/e2e/general/test_context_length.py`
- `tests/v1/e2e/general/test_min_tokens.py`
- `tests/v1/engine`
- `tests/v1/engine/test_llm_engine.py`

**✅ Model Runner V2 Distributed (2 GPUs)**

- `tests/basic_correctness`
- `tests/basic_correctness/test_basic_correctness.py`
- `tests/v1`
- `tests/v1/distributed`
- `tests/v1/distributed/test_async_llm_dp.py`
- `tests/v1/distributed/test_eagle_dp.py`

**✅ Model Runner V2 Examples**

- (test paths unknown)

**✅ Model Runner V2 Pipeline Parallelism (4 GPUs)**

- `tests/distributed`
- `tests/distributed/test_pipeline_parallel.py`
- `tests/distributed/test_pp_cudagraph.py`

**✅ Model Runner V2 Spec Decode**

- `tests/v1`
- `tests/v1/e2e`
- `tests/v1/e2e/spec_decode`
- `tests/v1/e2e/spec_decode/test_spec_decode.py`
- `tests/v1/spec_decode`
- `tests/v1/spec_decode/test_max_len.py`
- `tests/v1/spec_decode/test_probabilistic_rejection_sampler_utils.py`
- `tests/v1/spec_decode/test_synthetic_rejection_sampler_utils.py`

**✅ Multi-Modal Accuracy Eval (Small Models)**

- (test paths unknown)

**✅ Multi-Modal Models (Standard) 1: qwen2**

- (test paths unknown)

**✅ Multi-Modal Models (Standard) 2: qwen3 + gemma**

- (test paths unknown)

**✅ Multi-Modal Models (Standard) 3: llava + qwen2_vl**

- (test paths unknown)

**✅ Multi-Modal Models (Standard) 4: other + whisper**

- (test paths unknown)

**✅ Multi-Modal Processor**

- (test paths unknown)

**✅ Multi-Modal Processor (CPU)**

- `tests/models`
- `tests/models/multimodal`
- `tests/models/multimodal/processing`

**✅ MultiConnector (Nixl+Offloading) PD accuracy (2 GPUs)**

- (test paths unknown)

**✅ MultiConnector (Nixl+Offloading) PD edge cases (2 GPUs)**

- (test paths unknown)

**✅ NixlConnector PD + Spec Decode acceptance (2 GPUs)**

- (test paths unknown)

**✅ OpenAI API Correctness**

- `tests/entrypoints`
- `tests/entrypoints/openai`
- `tests/entrypoints/openai/correctness`

**✅ Pipeline + Context Parallelism (4 GPUs)**

- `tests/distributed`
- `tests/distributed/test_pipeline_parallel.py`
- `tests/distributed/test_pp_cudagraph.py`

**✅ Platform Tests (CUDA)**

- `tests/cuda`
- `tests/cuda/test_cuda_context.py`
- `tests/cuda/test_platform_no_cuda_init.py`

**✅ Plugin Tests (2 GPUs)**

- `tests/.`
- `tests/./plugins_tests`
- `tests/./plugins_tests/test_io_processor_plugins.py`
- `tests/distributed`
- `tests/distributed/test_distributed_oot.py`
- `tests/entrypoints`
- `tests/entrypoints/openai`
- `tests/entrypoints/openai/chat_completion`
- `tests/entrypoints/openai/chat_completion/test_oot_registration.py`
- `tests/models`
- `tests/models/test_oot_registration.py`
- `tests/plugins`
- `tests/plugins/lora_resolvers`
- `tests/plugins_tests`
- `tests/plugins_tests/test_bge_m3_sparse_io_processor_plugins.py`
- `tests/plugins_tests/test_platform_plugins.py`
- `tests/plugins_tests/test_scheduler_plugins.py`
- `tests/plugins_tests/test_stats_logger_plugins.py`
- `tests/plugins_tests/test_terratorch_io_processor_plugins.py`

**✅ PyTorch Compilation Passes Unit Tests**

- `tests/compile`
- `tests/compile/passes`

**✅ PyTorch Compilation Unit Tests**

- `tests/so`

**✅ PyTorch Compilation Unit Tests (H100)**

- (test paths unknown)

**✅ PyTorch Fullgraph**

- `tests/compile`
- `tests/compile/fullgraph`
- `tests/compile/fullgraph/test_full_graph.py`

**✅ PyTorch Fullgraph Smoke Test**

- `tests/so`

**✅ Pytorch Nightly Dependency Override Check**

- (test paths unknown)

**✅ Quantization**

- `tests/quantization`

**✅ Quantized MoE Test (B200)**

- `tests/quantization`
- `tests/quantization/test_blackwell_moe.py`

**✅ Quantized Models Test**

- `tests/models`
- `tests/models/quantization`

**✅ Ray Dependency Compatibility Check**

- (test paths unknown)

**✅ RayExecutorV2 (4 GPUs)**

- `tests/basic_correctness`
- `tests/basic_correctness/test_basic_correctness.py`
- `tests/distributed`
- `tests/distributed/test_pipeline_parallel.py`
- `tests/distributed/test_ray_v2_executor.py`
- `tests/distributed/test_ray_v2_executor_e2e.py`

**✅ Regression**

- `tests/test_regression.py`

**✅ Rust Frontend Cargo Style + Clippy**

- (test paths unknown)

**✅ Rust Frontend Cargo Tests**

- (test paths unknown)

**✅ Rust Frontend Core Correctness**

- (test paths unknown)

**✅ Rust Frontend Distributed**

- (test paths unknown)

**✅ Rust Frontend OpenAI Coverage**

- (test paths unknown)

**✅ Rust Frontend Serve/Admin Coverage**

- (test paths unknown)

**✅ Rust Frontend Tool Use**

- (test paths unknown)

**✅ Samplers Test**

- `tests/samplers`

**✅ Sequence Parallel Correctness Tests (2 GPUs)**

- `tests/compile`
- `tests/compile/correctness_e2e`
- `tests/compile/correctness_e2e/test_sequence_parallel.py`

**✅ Spec Decode Draft Model**

- `tests/v1`
- `tests/v1/e2e`
- `tests/v1/e2e/spec_decode`

**✅ Spec Decode Eagle**

- `tests/v1`
- `tests/v1/e2e`
- `tests/v1/e2e/spec_decode`

**✅ Spec Decode Ngram + Suffix**

- `tests/v1`
- `tests/v1/e2e`
- `tests/v1/e2e/spec_decode`

**✅ Spec Decode Speculators + MTP**

- `tests/v1`
- `tests/v1/e2e`
- `tests/v1/e2e/spec_decode`

**✅ V1 Core + KV + Metrics**

- `tests/entrypoints`
- `tests/entrypoints/openai`
- `tests/entrypoints/openai/correctness`
- `tests/entrypoints/openai/correctness/test_lmeval.py::test_lm_eval_accuracy_v1_engine`
- `tests/v1`
- `tests/v1/core`
- `tests/v1/executor`
- `tests/v1/kv_connector`
- `tests/v1/kv_connector/unit`
- `tests/v1/kv_offload`
- `tests/v1/metrics`
- `tests/v1/worker`

**✅ V1 Others (CPU)**

- `tests/v1`
- `tests/v1/core`
- `tests/v1/kv_connector`
- `tests/v1/kv_connector/unit`
- `tests/v1/metrics`
- `tests/v1/structured_output`
- `tests/v1/test_serial_utils.py`

**✅ V1 Sample + Logits**

- `tests/v1`
- `tests/v1/logits_processors`
- `tests/v1/sample`
- `tests/v1/test_oracle.py`
- `tests/v1/test_outputs.py`
- `tests/v1/test_request.py`

**✅ V1 Spec Decode**

- `tests/v1`
- `tests/v1/spec_decode`

**✅ V1 attention (B200)**

- `tests/v1`
- `tests/v1/attention`

**✅ V1 attention (H100)**

- `tests/v1`
- `tests/v1/attention`

**✅ bootstrap**

- (test paths unknown)

**✅ e2e Core (1 GPU)**

- `tests/v1`
- `tests/v1/e2e`
- `tests/v1/e2e/general`

**✅ e2e Scheduling (1 GPU)**

- `tests/v1`
- `tests/v1/e2e`
- `tests/v1/e2e/general`
- `tests/v1/e2e/general/test_async_scheduling.py`

**✅ vLLM IR Tests**

- `tests/ir`
- `tests/kernels`
- `tests/kernels/ir`

## LLM Selections — 1 target(s)

### ➖ `tests/basic_correctness/`

**Reason:** requirements/cuda.txt dependency version bump (Rule 3)

**Jobs (5):**

- 🔧 Basic Correctness
- 🔧 Distributed Model Tests (2 GPUs)
- 🔧 Distributed Tests (4 GPUs)(A100)
- 🔧 Model Runner V2 Distributed (2 GPUs)
- 🔧 RayExecutorV2 (4 GPUs)

## Gap Analysis

**Why the LLM missed:**
- LLM selections covered `basic_correctness` but failures occurred in `[job] Ascend NPU Test`, `config`, `entrypoints`, `multimodal`, `reasoning`, `renderers`, `test_inputs.py`, `test_outputs.py`, `test_pooling_params.py`, `test_ray_env.py`, `tokenizers_`, `tool_parsers`, `tool_use`, `transformers_utils`, `v1`
- `tests/tokenizers_` (job: Async Engine, Inputs, Utils, Worker, Config (CPU)) was not covered by any selection
- `tests/test_pooling_params.py` (job: Async Engine, Inputs, Utils, Worker, Config (CPU)) was not covered by any selection
- `tests/multimodal` (job: Async Engine, Inputs, Utils, Worker, Config (CPU)) was not covered by any selection
- `tests/test_ray_env.py` (job: Async Engine, Inputs, Utils, Worker, Config (CPU)) was not covered by any selection
- `tests/tool_parsers` (job: Async Engine, Inputs, Utils, Worker, Config (CPU)) was not covered by any selection
- `tests/test_inputs.py` (job: Async Engine, Inputs, Utils, Worker, Config (CPU)) was not covered by any selection
- `tests/transformers_utils` (job: Async Engine, Inputs, Utils, Worker, Config (CPU)) was not covered by any selection
- `tests/renderers` (job: Async Engine, Inputs, Utils, Worker, Config (CPU)) was not covered by any selection
- `tests/config` (job: Async Engine, Inputs, Utils, Worker, Config (CPU)) was not covered by any selection
- `tests/test_outputs.py` (job: Async Engine, Inputs, Utils, Worker, Config (CPU)) was not covered by any selection
- `tests/reasoning` (job: Async Engine, Inputs, Utils, Worker, Config (CPU)) was not covered by any selection
- `[job] Ascend NPU Test` (job: Ascend NPU Test) was not covered by any selection
- `tests/v1/determinism/test_batch_invariance.py` (job: Batch Invariance (H100)) was not covered by any selection
- `tests/v1/determinism/test_batch_invariance.py::test_v1_generation_is_deterministic_across_batch_sizes_with_needle[FLASH_ATTN]` (job: Batch Invariance (H100)) was not covered by any selection
- `tests/v1/determinism/test_batch_invariance.py::test_v1_generation_is_deterministic_across_batch_sizes_with_needle[TRITON_MLA]` (job: Batch Invariance (H100)) was not covered by any selection
- `tests/v1` (job: Batch Invariance (H100)) was not covered by any selection
- `tests/v1/determinism/test_rms_norm_batch_invariant.py` (job: Batch Invariance (H100)) was not covered by any selection
- `tests/v1/determinism` (job: Batch Invariance (H100)) was not covered by any selection
- `tests/tool_use` (job: Entrypoints Integration (API Server 2)) was not covered by any selection
- `tests/entrypoints/rpc` (job: Entrypoints Integration (API Server 2)) was not covered by any selection
- `tests/entrypoints` (job: Entrypoints Integration (API Server 2)) was not covered by any selection
- `tests/entrypoints/serve` (job: Entrypoints Integration (API Server 2)) was not covered by any selection
- `tests/entrypoints/serve/instrumentator` (job: Entrypoints Integration (API Server 2)) was not covered by any selection

**To improve coverage:**
- Add `tests/[job] Ascend NPU Test/` (or relevant sub-paths) to selections when related code changes
- Add `tests/config/` (or relevant sub-paths) to selections when related code changes
- Add `tests/entrypoints/` (or relevant sub-paths) to selections when related code changes
- Add `tests/multimodal/` (or relevant sub-paths) to selections when related code changes
- Add `tests/reasoning/` (or relevant sub-paths) to selections when related code changes
- Add `tests/renderers/` (or relevant sub-paths) to selections when related code changes
- Add `tests/test_inputs.py/` (or relevant sub-paths) to selections when related code changes
- Add `tests/test_outputs.py/` (or relevant sub-paths) to selections when related code changes
- Add `tests/test_pooling_params.py/` (or relevant sub-paths) to selections when related code changes
- Add `tests/test_ray_env.py/` (or relevant sub-paths) to selections when related code changes
- Add `tests/tokenizers_/` (or relevant sub-paths) to selections when related code changes
- Add `tests/tool_parsers/` (or relevant sub-paths) to selections when related code changes
- Add `tests/tool_use/` (or relevant sub-paths) to selections when related code changes
- Add `tests/transformers_utils/` (or relevant sub-paths) to selections when related code changes
- Add `tests/v1/` (or relevant sub-paths) to selections when related code changes

---
*Generated: 2026-06-27 02:48 UTC*
