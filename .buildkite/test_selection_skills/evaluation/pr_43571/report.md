# PR #43571 — Test Selection Evaluation

> **Build**: [69012](https://buildkite.com/vllm/ci/builds/69012) · **Date**: 2026-06-27

## Metrics

| Metric | Value |
|--------|-------|
| **Recall** | **100.0%** |
| **Precision** | **0.0%** |
| True Positives | 0 |
| False Negatives (CI failed, LLM missed) | 0 |
| False Positives (LLM selected, passed) | 1 |

## CI Test Results

| Failed | Passed | Skipped | Total |
|--------|--------|---------|-------|
| 0 | 0 | 0 | 0 |

**CI jobs:** 22 passed · 0 failed · 486 blocked · **254 test files**

## LLM vs CI Comparison Table

```
Test File                                                                                                                      LLM Selected  CI Result
======================================================================================================================================================
tests/.                                                                                                                        ✗             ✓ Passed 
tests/./compile                                                                                                                ✗             ✓ Passed 
tests/./compile/fullgraph                                                                                                      ✗             ✓ Passed 
tests/./compile/fullgraph/test_basic_correctness.py                                                                            ✗             ✓ Passed 
tests/./compile/test_wrapper.py                                                                                                ✗             ✓ Passed 
tests/./plugins_tests                                                                                                          ✗             ✓ Passed 
tests/./plugins_tests/test_io_processor_plugins.py                                                                             ✗             ✓ Passed 
tests/basic_correctness                                                                                                        ✗             ✓ Passed 
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
tests/config                                                                                                                   ✗             ✓ Passed 
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
tests/entrypoints                                                                                                              ✗             ✓ Passed 
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
tests/entrypoints/rpc                                                                                                          ✗             ✓ Passed 
tests/entrypoints/serve                                                                                                        ✗             ✓ Passed 
tests/entrypoints/serve/instrumentator                                                                                         ✗             ✓ Passed 
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
tests/models/quantization/test_gpt_oss.py                                                                                      ✓             ✓ Passed 
tests/models/quantization/test_nvfp4.py                                                                                        ✗             ✓ Passed 
tests/models/test_initialization.py                                                                                            ✗             ✓ Passed 
tests/models/test_initialization.py::test_can_initialize_small_subset                                                          ✗             ✓ Passed 
tests/models/test_oot_registration.py                                                                                          ✗             ✓ Passed 
tests/models/test_terratorch.py                                                                                                ✗             ✓ Passed 
tests/models/test_transformers.py                                                                                              ✗             ✓ Passed 
tests/models/test_utils.py                                                                                                     ✗             ✓ Passed 
tests/multimodal                                                                                                               ✗             ✓ Passed 
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
tests/reasoning                                                                                                                ✗             ✓ Passed 
tests/renderers                                                                                                                ✗             ✓ Passed 
tests/samplers                                                                                                                 ✗             ✓ Passed 
tests/so                                                                                                                       ✗             ✓ Passed 
tests/test_inputs.py                                                                                                           ✗             ✓ Passed 
tests/test_lm_eval_correctness.py                                                                                              ✗             ✓ Passed 
tests/test_outputs.py                                                                                                          ✗             ✓ Passed 
tests/test_pooling_params.py                                                                                                   ✗             ✓ Passed 
tests/test_ray_env.py                                                                                                          ✗             ✓ Passed 
tests/test_regression.py                                                                                                       ✗             ✓ Passed 
tests/tokenizers_                                                                                                              ✗             ✓ Passed 
tests/tool_parsers                                                                                                             ✗             ✓ Passed 
tests/tool_use                                                                                                                 ✗             ✓ Passed 
tests/transformers_utils                                                                                                       ✗             ✓ Passed 
tests/utils_                                                                                                                   ✗             ✓ Passed 
tests/v1                                                                                                                       ✗             ✓ Passed 
tests/v1/attention                                                                                                             ✗             ✓ Passed 
tests/v1/core                                                                                                                  ✗             ✓ Passed 
tests/v1/cudagraph                                                                                                             ✗             ✓ Passed 
tests/v1/cudagraph/test_cudagraph_dispatch.py                                                                                  ✗             ✓ Passed 
tests/v1/cudagraph/test_cudagraph_mode.py                                                                                      ✗             ✓ Passed 
tests/v1/determinism                                                                                                           ✗             ✓ Passed 
tests/v1/determinism/test_batch_invariance.py                                                                                  ✗             ✓ Passed 
tests/v1/determinism/test_batch_invariance.py::test_v1_generation_is_deterministic_across_batch_sizes_with_needle[FLASH_ATTN]  ✗             ✓ Passed 
tests/v1/determinism/test_batch_invariance.py::test_v1_generation_is_deterministic_across_batch_sizes_with_needle[TRITON_MLA]  ✗             ✓ Passed 
tests/v1/determinism/test_nvfp4_batch_invariant.py                                                                             ✗             ✓ Passed 
tests/v1/determinism/test_rms_norm_batch_invariant.py                                                                          ✗             ✓ Passed 
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

**Summary:** 254 total tests, 1 LLM selected, 0 CI failed

### Passing jobs

**✅ :docker: :smoking: Non-root smoke tests**

- (test paths unknown)

**✅ :docker: Build CPU image**

- (test paths unknown)

**✅ :docker: Build HPU image**

- (test paths unknown)

**✅ :docker: Build XPU image**

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

**✅ Generate and upload wheel indices**

- (test paths unknown)

**✅ Quantized Models Test**

- `tests/models`
- `tests/models/quantization`

**✅ bootstrap**

- (test paths unknown)

**✅ bootstrap**

- (test paths unknown)

## LLM Selections — 1 target(s)

### ➖ `tests/models/quantization/test_gpt_oss.py`

**Reason:** verify conditional import guard works on non-ROCm platforms

**Jobs (27):**

- 🔧 "Multi-Modal Models (Standard) 1: qwen2"
- 🔧 "Multi-Modal Models (Standard) 2: qwen3 + gemma"
- 🔧 "Multi-Modal Models (Standard) 3: llava + qwen2_vl"
- 🔧 "Multi-Modal Models (Standard) 4: other + whisper"
- 🔧 Basic Models Test (Other CPU) # 5min
- 🔧 Basic Models Tests (Extra Initialization) %N
- 🔧 Basic Models Tests (Initialization)
- 🔧 Basic Models Tests (Other)
- 🔧 Distributed Model Tests (2 GPUs)
- 🔧 Kernels (B200)
- 🔧 Language Models Test (Extended Generation) # 80min
- 🔧 Language Models Test (Extended Pooling)  # 36min
- 🔧 Language Models Test (MTEB)
- 🔧 Language Models Test (PPL)
- 🔧 Language Models Tests (Extra Standard) %N
- 🔧 Language Models Tests (Hybrid) %N
- 🔧 Language Models Tests (Standard)
- 🔧 Multi-Modal Models (Extended Generation 1)
- 🔧 Multi-Modal Models (Extended Generation 2)
- 🔧 Multi-Modal Models (Extended Generation 3)
- 🔧 Multi-Modal Models (Extended Pooling)
- 🔧 Multi-Modal Processor # 44min
- 🔧 Multi-Modal Processor (CPU)
- 🔧 Plugin Tests (2 GPUs)
- 🔧 Quantized Models Test
- 🔧 Transformers Backward Compatibility Models Test
- 🔧 Transformers Nightly Models

## Gap Analysis

LLM caught all CI failures — no gap to analyse.

---
*Generated: 2026-06-27 02:48 UTC*
