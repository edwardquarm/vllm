# PR #43571 — Test Selection Evaluation

> **Build**: [69012](https://buildkite.com/vllm/ci/builds/69012) · **Date**: 2026-06-30

## Metrics

| | Count | Meaning |
|---|---|---|
| ✅ **True Positives** | **0** | LLM selected a test that CI actually failed |
| ❌ **False Negatives** | **0** | CI failed a test the LLM did not select (missed failures) |
| ⚠️ **False Positives** | **1** | LLM selected a test that CI passed (no failure detected) |

| Metric | Value | Formula |
|---|---|---|
| **Recall** (did LLM catch failures?) | **N/A** *(no CI failures)* | TP / (TP + FN) |
| **Precision** (were LLM picks relevant?) | **0.0%** | TP / (TP + FP) |

## CI Test Results

| Failed | Passed | Skipped | Total |
|--------|--------|---------|-------|
| 0 | 0 | 0 | 0 |

**CI jobs:** 22 passed · 0 failed · 486 blocked · **495 test files**

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
tests/.buildkite                                                                                                               ✗             ✓ Passed 
tests/.buildkite/intel_jobs                                                                                                    ✗             ✓ Passed 
tests/.buildkite/intel_jobs/test-intel.yaml                                                                                    ✗             ✓ Passed 
tests/.buildkite/scripts                                                                                                       ✗             ✓ Passed 
tests/.buildkite/scripts/scheduled_integration_test                                                                            ✗             ✓ Passed 
tests/CMakeLists.txt                                                                                                           ✗             ✓ Passed 
tests/basic_correctness                                                                                                        ✗             ✓ Passed 
tests/basic_correctness/test_basic_correctness                                                                                 ✗             ✓ Passed 
tests/basic_correctness/test_basic_correctness.py                                                                              ✗             ✓ Passed 
tests/basic_correctness/test_cpu_offload                                                                                       ✗             ✓ Passed 
tests/basic_correctness/test_cpu_offload.py                                                                                    ✗             ✓ Passed 
tests/basic_correctness/test_cumem.py                                                                                          ✗             ✓ Passed 
tests/benchmarks                                                                                                               ✗             ✓ Passed 
tests/benchmarks/attention_benchmarks                                                                                          ✗             ✓ Passed 
tests/cmake                                                                                                                    ✗             ✓ Passed 
tests/cmake/cpu_extension.cmake                                                                                                ✗             ✓ Passed 
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
tests/compile/h100                                                                                                             ✗             ✓ Passed 
tests/compile/passes                                                                                                           ✗             ✓ Passed 
tests/compile/passes/distributed                                                                                               ✗             ✓ Passed 
tests/compile/passes/distributed/test_async_tp.py                                                                              ✗             ✓ Passed 
tests/compile/passes/distributed/test_fusion_all_reduce.py                                                                     ✗             ✓ Passed 
tests/compile/passes/distributed/test_sequence_parallelism.py                                                                  ✗             ✓ Passed 
tests/compile/passes/test_fusion_attn.py                                                                                       ✗             ✓ Passed 
tests/compile/passes/test_mla_attn_quant_fusion.py                                                                             ✗             ✓ Passed 
tests/compile/passes/test_silu_mul_quant_fusion.py                                                                             ✗             ✓ Passed 
tests/compile/test_wrapper.py                                                                                                  ✗             ✓ Passed 
tests/config                                                                                                                   ✗             ✓ Passed 
tests/conftest.py                                                                                                              ✗             ✓ Passed 
tests/csrc                                                                                                                     ✗             ✓ Passed 
tests/csrc/attention                                                                                                           ✗             ✓ Passed 
tests/csrc/attention/mla                                                                                                       ✗             ✓ Passed 
tests/csrc/cpu                                                                                                                 ✗             ✓ Passed 
tests/csrc/cpu/shm.cpp                                                                                                         ✗             ✓ Passed 
tests/csrc/mamba                                                                                                               ✗             ✓ Passed 
tests/csrc/minimax_reduce_rms_kernel.cu                                                                                        ✗             ✓ Passed 
tests/csrc/minimax_reduce_rms_kernel.h                                                                                         ✗             ✓ Passed 
tests/csrc/moe                                                                                                                 ✗             ✓ Passed 
tests/csrc/quantization                                                                                                        ✗             ✓ Passed 
tests/csrc/quantization/cutlass_w8a8                                                                                           ✗             ✓ Passed 
tests/csrc/quantization/cutlass_w8a8/moe                                                                                       ✗             ✓ Passed 
tests/csrc/quantization/fp4                                                                                                    ✗             ✓ Passed 
tests/csrc/quantization/w8a8                                                                                                   ✗             ✓ Passed 
tests/csrc/quantization/w8a8/cutlass                                                                                           ✗             ✓ Passed 
tests/csrc/quantization/w8a8/cutlass/moe                                                                                       ✗             ✓ Passed 
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
tests/distributed/test_events                                                                                                  ✗             ✓ Passed 
tests/distributed/test_events.py                                                                                               ✗             ✓ Passed 
tests/distributed/test_multi_node_assignment.py                                                                                ✗             ✓ Passed 
tests/distributed/test_multiproc_executor.py                                                                                   ✗             ✓ Passed 
tests/distributed/test_multiproc_executor.py::test_multiproc_executor_multi_node                                               ✗             ✓ Passed 
tests/distributed/test_nccl_symm_mem_allreduce.py                                                                              ✗             ✓ Passed 
tests/distributed/test_packed_tensor.py                                                                                        ✗             ✓ Passed 
tests/distributed/test_pipeline_parallel.py                                                                                    ✗             ✓ Passed 
tests/distributed/test_pp_cudagraph.py                                                                                         ✗             ✓ Passed 
tests/distributed/test_pynccl                                                                                                  ✗             ✓ Passed 
tests/distributed/test_pynccl.py                                                                                               ✗             ✓ Passed 
tests/distributed/test_ray_v2_executor.py                                                                                      ✗             ✓ Passed 
tests/distributed/test_ray_v2_executor_e2e.py                                                                                  ✗             ✓ Passed 
tests/distributed/test_shm_broadcast.py                                                                                        ✗             ✓ Passed 
tests/distributed/test_shm_buffer.py                                                                                           ✗             ✓ Passed 
tests/distributed/test_shm_storage.py                                                                                          ✗             ✓ Passed 
tests/distributed/test_symm_mem_allreduce.py                                                                                   ✗             ✓ Passed 
tests/distributed/test_torchrun_example.py                                                                                     ✗             ✓ Passed 
tests/distributed/test_torchrun_example_moe.py                                                                                 ✗             ✓ Passed 
tests/distributed/test_utils                                                                                                   ✗             ✓ Passed 
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
tests/entrypoints/openai/correctness/test_lmeval.py                                                                            ✗             ✓ Passed 
tests/entrypoints/openai/correctness/test_lmeval.py::test_lm_eval_accuracy_v1_engine                                           ✗             ✓ Passed 
tests/entrypoints/openai/responses                                                                                             ✗             ✓ Passed 
tests/entrypoints/openai/speech_to_text                                                                                        ✗             ✓ Passed 
tests/entrypoints/openai/test_multi_api_servers.py                                                                             ✗             ✓ Passed 
tests/entrypoints/openai/tool_parsers                                                                                          ✗             ✓ Passed 
tests/entrypoints/pooling                                                                                                      ✗             ✓ Passed 
tests/entrypoints/rpc                                                                                                          ✗             ✓ Passed 
tests/entrypoints/serve                                                                                                        ✗             ✓ Passed 
tests/entrypoints/serve/instrumentator                                                                                         ✗             ✓ Passed 
tests/entrypoints/test_chat_utils                                                                                              ✗             ✓ Passed 
tests/entrypoints/test_chat_utils.py                                                                                           ✗             ✓ Passed 
tests/evals                                                                                                                    ✗             ✓ Passed 
tests/evals/gpt_oss                                                                                                            ✗             ✓ Passed 
tests/evals/gpt_oss/test_gpqa_correctness.py                                                                                   ✗             ✓ Passed 
tests/evals/gsm8k                                                                                                              ✗             ✓ Passed 
tests/evals/gsm8k/test_gsm8k_correctness.py                                                                                    ✗             ✓ Passed 
tests/examples                                                                                                                 ✗             ✓ Passed 
tests/examples/basic                                                                                                           ✗             ✓ Passed 
tests/examples/basic/offline_inference                                                                                         ✗             ✓ Passed 
tests/examples/features                                                                                                        ✗             ✓ Passed 
tests/examples/features/data_parallel                                                                                          ✗             ✓ Passed 
tests/examples/features/data_parallel/data_parallel_offline.py                                                                 ✗             ✓ Passed 
tests/examples/features/torchrun                                                                                               ✗             ✓ Passed 
tests/examples/features/torchrun/torchrun_dp_example_offline.py                                                                ✗             ✓ Passed 
tests/examples/generate                                                                                                        ✗             ✓ Passed 
tests/examples/generate/multimodal                                                                                             ✗             ✓ Passed 
tests/examples/others                                                                                                          ✗             ✓ Passed 
tests/examples/others/tensorize_vllm_model.py                                                                                  ✗             ✓ Passed 
tests/examples/pooling                                                                                                         ✗             ✓ Passed 
tests/examples/pooling/embed                                                                                                   ✗             ✓ Passed 
tests/examples/pooling/embed/vision_embedding_offline.py                                                                       ✗             ✓ Passed 
tests/examples/rl                                                                                                              ✗             ✓ Passed 
tests/ir                                                                                                                       ✗             ✓ Passed 
tests/kernels                                                                                                                  ✗             ✓ Passed 
tests/kernels/attention                                                                                                        ✗             ✓ Passed 
tests/kernels/attention/test_attention_selector.py                                                                             ✗             ✓ Passed 
tests/kernels/attention/test_cpu_attn.py                                                                                       ✗             ✓ Passed 
tests/kernels/attention/test_cutlass_mla_decode.py                                                                             ✗             ✓ Passed 
tests/kernels/attention/test_deepgemm_attention.py                                                                             ✗             ✓ Passed 
tests/kernels/attention/test_flashinfer.py                                                                                     ✗             ✓ Passed 
tests/kernels/attention/test_flashinfer_mla_decode.py                                                                          ✗             ✓ Passed 
tests/kernels/attention/test_flashinfer_trtllm_attention.py                                                                    ✗             ✓ Passed 
tests/kernels/core                                                                                                             ✗             ✓ Passed 
tests/kernels/core/test_minimax_reduce_rms.py                                                                                  ✗             ✓ Passed 
tests/kernels/helion                                                                                                           ✗             ✓ Passed 
tests/kernels/ir                                                                                                               ✗             ✓ Passed 
tests/kernels/ir'                                                                                                              ✗             ✓ Passed 
tests/kernels/mamba                                                                                                            ✗             ✓ Passed 
tests/kernels/moe                                                                                                              ✗             ✓ Passed 
tests/kernels/moe/test_batched_deepgemm.py                                                                                     ✗             ✓ Passed 
tests/kernels/moe/test_block_int8.py                                                                                           ✗             ✓ Passed 
tests/kernels/moe/test_cpu_fused_moe.py                                                                                        ✗             ✓ Passed 
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
tests/kernels/quantization/test_rocm_skinny_gemms.py                                                                           ✗             ✓ Passed 
tests/kernels/quantization/test_silu_mul_nvfp4_quant.py                                                                        ✗             ✓ Passed 
tests/kernels/test_awq_int4_to_int8.py                                                                                         ✗             ✓ Passed 
tests/kernels/test_awq_int4_to_int8.py"                                                                                        ✗             ✓ Passed 
tests/kernels/test_concat_mla_q.py                                                                                             ✗             ✓ Passed 
tests/kernels/test_onednn.py                                                                                                   ✗             ✓ Passed 
tests/kernels/test_top_k_per_row.py                                                                                            ✗             ✓ Passed 
tests/lora                                                                                                                     ✗             ✓ Passed 
tests/lora/test_chatglm3_tp.py                                                                                                 ✗             ✓ Passed 
tests/lora/test_default_mm_loras.py                                                                                            ✗             ✓ Passed 
tests/lora/test_fused_moe_lora_kernel.py                                                                                       ✗             ✓ Passed 
tests/lora/test_gptoss_tp.py                                                                                                   ✗             ✓ Passed 
tests/lora/test_layers.py                                                                                                      ✗             ✓ Passed 
tests/lora/test_llama_tp.py                                                                                                    ✗             ✓ Passed 
tests/lora/test_llm_with_multi_loras.py                                                                                        ✗             ✓ Passed 
tests/lora/test_mixtral.py                                                                                                     ✗             ✓ Passed 
tests/lora/test_olmoe_tp.py                                                                                                    ✗             ✓ Passed 
tests/lora/test_punica_ops.py                                                                                                  ✗             ✓ Passed 
tests/lora/test_punica_ops_fp8.py                                                                                              ✗             ✓ Passed 
tests/lora/test_quant_model.py                                                                                                 ✗             ✓ Passed 
tests/lora/test_qwen35_densemodel_lora.py                                                                                      ✗             ✓ Passed 
tests/model_executor                                                                                                           ✗             ✓ Passed 
tests/model_executor/model_loader                                                                                              ✗             ✓ Passed 
tests/model_executor/model_loader/test_sharded_state_loader.py                                                                 ✗             ✓ Passed 
tests/models                                                                                                                   ✗             ✓ Passed 
tests/models/language                                                                                                          ✗             ✓ Passed 
tests/models/language/generation                                                                                               ✗             ✓ Passed 
tests/models/language/generation/test_common.py                                                                                ✗             ✓ Passed 
tests/models/language/generation_ppl_test                                                                                      ✗             ✓ Passed 
tests/models/language/pooling                                                                                                  ✗             ✓ Passed 
tests/models/language/pooling/test_classification.py                                                                           ✗             ✓ Passed 
tests/models/language/pooling/test_embedding.py                                                                                ✗             ✓ Passed 
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
tests/models/registry.py                                                                                                       ✗             ✓ Passed 
tests/models/test_initialization.py                                                                                            ✗             ✓ Passed 
tests/models/test_initialization.py::test_can_initialize_small_subset                                                          ✗             ✓ Passed 
tests/models/test_oot_registration.py                                                                                          ✗             ✓ Passed 
tests/models/test_registry.py                                                                                                  ✗             ✓ Passed 
tests/models/test_terratorch.py                                                                                                ✗             ✓ Passed 
tests/models/test_transformers.py                                                                                              ✗             ✓ Passed 
tests/models/test_utils.py                                                                                                     ✗             ✓ Passed 
tests/models/test_vision.py                                                                                                    ✗             ✓ Passed 
tests/multimodal                                                                                                               ✗             ✓ Passed 
tests/plugins                                                                                                                  ✗             ✓ Passed 
tests/plugins/lora_resolvers                                                                                                   ✗             ✓ Passed 
tests/plugins_tests                                                                                                            ✗             ✓ Passed 
tests/plugins_tests/test_bge_m3_sparse_io_processor_plugins.py                                                                 ✗             ✓ Passed 
tests/plugins_tests/test_io_processor_plugins.py                                                                               ✗             ✓ Passed 
tests/plugins_tests/test_platform_plugins.py                                                                                   ✗             ✓ Passed 
tests/plugins_tests/test_scheduler_plugins.py                                                                                  ✗             ✓ Passed 
tests/plugins_tests/test_stats_logger_plugins.py                                                                               ✗             ✓ Passed 
tests/plugins_tests/test_terratorch_io_processor_plugins.py                                                                    ✗             ✓ Passed 
tests/quantization                                                                                                             ✗             ✓ Passed 
tests/quantization/test_blackwell_moe.py                                                                                       ✗             ✓ Passed 
tests/quantization/test_compressed_tensors.py                                                                                  ✗             ✓ Passed 
tests/quantization/test_compressed_tensors.py::test_compressed_tensors_w8a8_logprobs                                           ✗             ✓ Passed 
tests/quantization/test_cpu_wna16.py                                                                                           ✗             ✓ Passed 
tests/quantization/test_cpu_wna16.py"                                                                                          ✗             ✓ Passed 
tests/quantization/test_cutlass_w4a16.py                                                                                       ✗             ✓ Passed 
tests/reasoning                                                                                                                ✗             ✓ Passed 
tests/renderers                                                                                                                ✗             ✓ Passed 
tests/requirements                                                                                                             ✗             ✓ Passed 
tests/requirements/test                                                                                                        ✗             ✓ Passed 
tests/requirements/test/nightly-torch.txt                                                                                      ✗             ✓ Passed 
tests/rocm                                                                                                                     ✗             ✓ Passed 
tests/rocm/aiter                                                                                                               ✗             ✓ Passed 
tests/samplers                                                                                                                 ✗             ✓ Passed 
tests/setup.py                                                                                                                 ✗             ✓ Passed 
tests/standalone_tests                                                                                                         ✗             ✓ Passed 
tests/standalone_tests/lazy_imports.py                                                                                         ✗             ✓ Passed 
tests/standalone_tests/python_only_compile.sh                                                                                  ✗             ✓ Passed 
tests/test_config                                                                                                              ✗             ✓ Passed 
tests/test_inputs.py                                                                                                           ✗             ✓ Passed 
tests/test_lm_eval_correctness.py                                                                                              ✗             ✓ Passed 
tests/test_logger                                                                                                              ✗             ✓ Passed 
tests/test_outputs.py                                                                                                          ✗             ✓ Passed 
tests/test_pooling_params.py                                                                                                   ✗             ✓ Passed 
tests/test_ray_env.py                                                                                                          ✗             ✓ Passed 
tests/test_regression                                                                                                          ✗             ✓ Passed 
tests/test_regression.py                                                                                                       ✗             ✓ Passed 
tests/test_sequence                                                                                                            ✗             ✓ Passed 
tests/test_vllm_port                                                                                                           ✗             ✓ Passed 
tests/tokenizers_                                                                                                              ✗             ✓ Passed 
tests/tool_parsers                                                                                                             ✗             ✓ Passed 
tests/tool_use                                                                                                                 ✗             ✓ Passed 
tests/tools                                                                                                                    ✗             ✓ Passed 
tests/tools/install_deepgemm.sh                                                                                                ✗             ✓ Passed 
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
tests/v1/engine/test_engine_core_client.py                                                                                     ✗             ✓ Passed 
tests/v1/engine/test_engine_core_client.py::test_kv_cache_events_dp                                                            ✗             ✓ Passed 
tests/v1/engine/test_llm_engine.py                                                                                             ✗             ✓ Passed 
tests/v1/engine/test_preprocess_error_handling.py                                                                              ✗             ✓ Passed 
tests/v1/executor                                                                                                              ✗             ✓ Passed 
tests/v1/executor'                                                                                                             ✗             ✓ Passed 
tests/v1/kv_connector                                                                                                          ✗             ✓ Passed 
tests/v1/kv_connector/nixl_integration                                                                                         ✗             ✓ Passed 
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
tests/vllm                                                                                                                     ✗             ✓ Passed 
tests/vllm/_aiter_ops.py                                                                                                       ✗             ✓ Passed 
tests/vllm/_custom_ops.py                                                                                                      ✗             ✓ Passed 
tests/vllm/beam_search.py                                                                                                      ✗             ✓ Passed 
tests/vllm/compilation                                                                                                         ✗             ✓ Passed 
tests/vllm/config                                                                                                              ✗             ✓ Passed 
tests/vllm/config/attention.py                                                                                                 ✗             ✓ Passed 
tests/vllm/config/compilation.py                                                                                               ✗             ✓ Passed 
tests/vllm/config/model.py                                                                                                     ✗             ✓ Passed 
tests/vllm/config/parallel.py                                                                                                  ✗             ✓ Passed 
tests/vllm/distributed                                                                                                         ✗             ✓ Passed 
tests/vllm/distributed/device_communicators                                                                                    ✗             ✓ Passed 
tests/vllm/distributed/device_communicators/cpu_communicator.py                                                                ✗             ✓ Passed 
tests/vllm/distributed/eplb                                                                                                    ✗             ✓ Passed 
tests/vllm/distributed/kv_transfer                                                                                             ✗             ✓ Passed 
tests/vllm/distributed/kv_transfer/kv_connector                                                                                ✗             ✓ Passed 
tests/vllm/distributed/kv_transfer/kv_connector/v1                                                                             ✗             ✓ Passed 
tests/vllm/distributed/kv_transfer/kv_connector/v1/multi_connector.py                                                          ✗             ✓ Passed 
tests/vllm/distributed/kv_transfer/kv_connector/v1/nixl_connector.py                                                           ✗             ✓ Passed 
tests/vllm/distributed/kv_transfer/kv_connector/v1/offloading                                                                  ✗             ✓ Passed 
tests/vllm/distributed/kv_transfer/kv_connector/v1/offloading_connector.py                                                     ✗             ✓ Passed 
tests/vllm/distributed/parallel_state.py                                                                                       ✗             ✓ Passed 
tests/vllm/engine                                                                                                              ✗             ✓ Passed 
tests/vllm/engine/arg_utils.py                                                                                                 ✗             ✓ Passed 
tests/vllm/entrypoints                                                                                                         ✗             ✓ Passed 
tests/vllm/entrypoints/openai                                                                                                  ✗             ✓ Passed 
tests/vllm/envs.py                                                                                                             ✗             ✓ Passed 
tests/vllm/executor                                                                                                            ✗             ✓ Passed 
tests/vllm/inputs                                                                                                              ✗             ✓ Passed 
tests/vllm/ir                                                                                                                  ✗             ✓ Passed 
tests/vllm/kernels                                                                                                             ✗             ✓ Passed 
tests/vllm/lora                                                                                                                ✗             ✓ Passed 
tests/vllm/model_executor                                                                                                      ✗             ✓ Passed 
tests/vllm/model_executor/kernels                                                                                              ✗             ✓ Passed 
tests/vllm/model_executor/layers                                                                                               ✗             ✓ Passed 
tests/vllm/model_executor/layers/activation.py                                                                                 ✗             ✓ Passed 
tests/vllm/model_executor/layers/attention                                                                                     ✗             ✓ Passed 
tests/vllm/model_executor/layers/attention/attention.py                                                                        ✗             ✓ Passed 
tests/vllm/model_executor/layers/fla                                                                                           ✗             ✓ Passed 
tests/vllm/model_executor/layers/fla/ops                                                                                       ✗             ✓ Passed 
tests/vllm/model_executor/layers/fused_moe                                                                                     ✗             ✓ Passed 
tests/vllm/model_executor/layers/fused_moe/cutlass_moe.py                                                                      ✗             ✓ Passed 
tests/vllm/model_executor/layers/fused_moe/flashinfer_a2a_prepare_finalize.py                                                  ✗             ✓ Passed 
tests/vllm/model_executor/layers/fused_moe/flashinfer_cutlass_moe.py                                                           ✗             ✓ Passed 
tests/vllm/model_executor/layers/layernorm.py                                                                                  ✗             ✓ Passed 
tests/vllm/model_executor/layers/mamba                                                                                         ✗             ✓ Passed 
tests/vllm/model_executor/layers/mamba/lamport_workspace.py                                                                    ✗             ✓ Passed 
tests/vllm/model_executor/layers/mamba/linear_attn.py                                                                          ✗             ✓ Passed 
tests/vllm/model_executor/layers/mamba/ops                                                                                     ✗             ✓ Passed 
tests/vllm/model_executor/layers/quantization                                                                                  ✗             ✓ Passed 
tests/vllm/model_executor/layers/quantization/compressed_tensors                                                               ✗             ✓ Passed 
tests/vllm/model_executor/layers/quantization/compressed_tensors/schemes                                                       ✗             ✓ Passed 
tests/vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py                       ✗             ✓ Passed 
tests/vllm/model_executor/layers/quantization/cpu_wna16.py                                                                     ✗             ✓ Passed 
tests/vllm/model_executor/layers/quantization/gptq_marlin.py                                                                   ✗             ✓ Passed 
tests/vllm/model_executor/layers/quantization/input_quant_fp8.py                                                               ✗             ✓ Passed 
tests/vllm/model_executor/layers/quantization/kernels                                                                          ✗             ✓ Passed 
tests/vllm/model_executor/layers/quantization/kernels/mixed_precision                                                          ✗             ✓ Passed 
tests/vllm/model_executor/layers/quantization/kernels/mixed_precision/cpu.py                                                   ✗             ✓ Passed 
tests/vllm/model_executor/layers/quantization/kernels/scaled_mm                                                                ✗             ✓ Passed 
tests/vllm/model_executor/layers/quantization/kernels/scaled_mm/cpu.py                                                         ✗             ✓ Passed 
tests/vllm/model_executor/layers/quantization/modelopt.py                                                                      ✗             ✓ Passed 
tests/vllm/model_executor/layers/quantization/mxfp4.py                                                                         ✗             ✓ Passed 
tests/vllm/model_executor/layers/quantization/turboquant                                                                       ✗             ✓ Passed 
tests/vllm/model_executor/layers/quantization/utils                                                                            ✗             ✓ Passed 
tests/vllm/model_executor/layers/quantization/utils/flashinfer_utils.py                                                        ✗             ✓ Passed 
tests/vllm/model_executor/layers/rotary_embedding                                                                              ✗             ✓ Passed 
tests/vllm/model_executor/model_loader                                                                                         ✗             ✓ Passed 
tests/vllm/model_executor/model_loader/sharded_state_loader.py                                                                 ✗             ✓ Passed 
tests/vllm/model_executor/models                                                                                               ✗             ✓ Passed 
tests/vllm/model_executor/models/deepseek_v2.py                                                                                ✗             ✓ Passed 
tests/vllm/model_executor/models/gpt_oss.py                                                                                    ✗             ✓ Passed 
tests/vllm/model_executor/models/llama4.py                                                                                     ✗             ✓ Passed 
tests/vllm/model_executor/models/mlp_speculator.py                                                                             ✗             ✓ Passed 
tests/vllm/model_executor/models/qwen.py                                                                                       ✗             ✓ Passed 
tests/vllm/model_executor/models/qwen2.py                                                                                      ✗             ✓ Passed 
tests/vllm/model_executor/models/qwen3.py                                                                                      ✗             ✓ Passed 
tests/vllm/model_executor/models/qwen3_5.py                                                                                    ✗             ✓ Passed 
tests/vllm/model_executor/models/qwen3_5_mtp.py                                                                                ✗             ✓ Passed 
tests/vllm/model_executor/models/qwen3_dflash.py                                                                               ✗             ✓ Passed 
tests/vllm/model_executor/models/qwen3_next.py                                                                                 ✗             ✓ Passed 
tests/vllm/model_executor/models/qwen3_next_mtp.py                                                                             ✗             ✓ Passed 
tests/vllm/model_executor/models/whisper.py                                                                                    ✗             ✓ Passed 
tests/vllm/multimodal                                                                                                          ✗             ✓ Passed 
tests/vllm/platforms                                                                                                           ✗             ✓ Passed 
tests/vllm/platforms/cpu.py                                                                                                    ✗             ✓ Passed 
tests/vllm/platforms/cuda.py                                                                                                   ✗             ✓ Passed 
tests/vllm/platforms/rocm.py                                                                                                   ✗             ✓ Passed 
tests/vllm/plugins                                                                                                             ✗             ✓ Passed 
tests/vllm/sampling_metadata.py                                                                                                ✗             ✓ Passed 
tests/vllm/transformers_utils                                                                                                  ✗             ✓ Passed 
tests/vllm/transformers_utils/configs                                                                                          ✗             ✓ Passed 
tests/vllm/transformers_utils/configs/qwen3_5.py                                                                               ✗             ✓ Passed 
tests/vllm/transformers_utils/configs/qwen3_5_moe.py                                                                           ✗             ✓ Passed 
tests/vllm/transformers_utils/configs/speculators                                                                              ✗             ✓ Passed 
tests/vllm/utils                                                                                                               ✗             ✓ Passed 
tests/vllm/utils/deep_gemm.py                                                                                                  ✗             ✓ Passed 
tests/vllm/utils/flashinfer.py                                                                                                 ✗             ✓ Passed 
tests/vllm/utils/import_utils.py                                                                                               ✗             ✓ Passed 
tests/vllm/v1                                                                                                                  ✗             ✓ Passed 
tests/vllm/v1/attention                                                                                                        ✗             ✓ Passed 
tests/vllm/v1/attention/backends                                                                                               ✗             ✓ Passed 
tests/vllm/v1/attention/backends/flashinfer.py                                                                                 ✗             ✓ Passed 
tests/vllm/v1/attention/backends/flex_attention.py                                                                             ✗             ✓ Passed 
tests/vllm/v1/attention/backends/mla                                                                                           ✗             ✓ Passed 
tests/vllm/v1/attention/backends/mla/aiter_triton_mla.py                                                                       ✗             ✓ Passed 
tests/vllm/v1/attention/backends/mla/cutlass_mla.py                                                                            ✗             ✓ Passed 
tests/vllm/v1/attention/backends/mla/flashinfer_mla.py                                                                         ✗             ✓ Passed 
tests/vllm/v1/attention/backends/mla/rocm_aiter_mla.py                                                                         ✗             ✓ Passed 
tests/vllm/v1/attention/backends/rocm_aiter_fa.py                                                                              ✗             ✓ Passed 
tests/vllm/v1/attention/backends/rocm_aiter_unified_attn.py                                                                    ✗             ✓ Passed 
tests/vllm/v1/attention/backends/rocm_attn.py                                                                                  ✗             ✓ Passed 
tests/vllm/v1/attention/backends/triton_attn.py                                                                                ✗             ✓ Passed 
tests/vllm/v1/attention/backends/turboquant_attn.py                                                                            ✗             ✓ Passed 
tests/vllm/v1/attention/backends/utils.py                                                                                      ✗             ✓ Passed 
tests/vllm/v1/attention/ops                                                                                                    ✗             ✓ Passed 
tests/vllm/v1/attention/ops/triton_turboquant_decode.py                                                                        ✗             ✓ Passed 
tests/vllm/v1/attention/ops/triton_turboquant_store.py                                                                         ✗             ✓ Passed 
tests/vllm/v1/attention/selector.py                                                                                            ✗             ✓ Passed 
tests/vllm/v1/core                                                                                                             ✗             ✓ Passed 
tests/vllm/v1/core/sched                                                                                                       ✗             ✓ Passed 
tests/vllm/v1/cudagraph_dispatcher.py                                                                                          ✗             ✓ Passed 
tests/vllm/v1/distributed                                                                                                      ✗             ✓ Passed 
tests/vllm/v1/engine                                                                                                           ✗             ✓ Passed 
tests/vllm/v1/engine/llm_engine.py                                                                                             ✗             ✓ Passed 
tests/vllm/v1/executor                                                                                                         ✗             ✓ Passed 
tests/vllm/v1/executor/abstract.py                                                                                             ✗             ✓ Passed 
tests/vllm/v1/executor/multiproc_executor.py                                                                                   ✗             ✓ Passed 
tests/vllm/v1/executor/ray_executor_v2.py                                                                                      ✗             ✓ Passed 
tests/vllm/v1/executor/uniproc_executor.py                                                                                     ✗             ✓ Passed 
tests/vllm/v1/sample                                                                                                           ✗             ✓ Passed 
tests/vllm/v1/spec_decode                                                                                                      ✗             ✓ Passed 
tests/vllm/v1/worker                                                                                                           ✗             ✓ Passed 
tests/vllm/v1/worker/cpu_model_runner.py                                                                                       ✗             ✓ Passed 
tests/vllm/v1/worker/cpu_worker.py                                                                                             ✗             ✓ Passed 
tests/vllm/v1/worker/gpu                                                                                                       ✗             ✓ Passed 
tests/vllm/v1/worker/gpu/spec_decode                                                                                           ✗             ✓ Passed 
tests/vllm/v1/worker/gpu_model_runner.py                                                                                       ✗             ✓ Passed 
tests/vllm/v1/worker/gpu_worker.py                                                                                             ✗             ✓ Passed 
tests/vllm/v1/worker/kv_connector_model_runner_mixin.py                                                                        ✗             ✓ Passed 
tests/vllm/worker                                                                                                              ✗             ✓ Passed 
tests/vllm/worker/worker_base.py                                                                                               ✗             ✓ Passed 
tests/weight_loading                                                                                                           ✗             ✓ Passed 
```

**Summary:** 495 total tests, 1 LLM selected, 0 CI failed

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
- `tests/vllm`
- `tests/vllm/_aiter_ops.py`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/layers`
- `tests/vllm/model_executor/model_loader`
- `tests/vllm/model_executor/model_loader/sharded_state_loader.py`
- `tests/vllm/model_executor/models`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`
- `tests/vllm/v1`
- `tests/vllm/v1/attention`
- `tests/vllm/v1/attention/backends`
- `tests/vllm/v1/attention/selector.py`

**✅ Generate and upload wheel indices**

- (test paths unknown)

**✅ Quantized Models Test**

- `tests/models`
- `tests/models/quantization`
- `tests/vllm`
- `tests/vllm/_aiter_ops.py`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/layers`
- `tests/vllm/model_executor/layers/quantization`
- `tests/vllm/model_executor/model_loader`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`

**✅ bootstrap**

- (test paths unknown)

**✅ bootstrap**

- (test paths unknown)

## LLM Selections — 1 target(s)

### ➖ `tests/models/quantization/test_gpt_oss.py`

**Reason:** test file itself was modified with import guard

**Jobs (42):**

- 🔧 AMD: Basic Models Tests (Extra Initialization) %N
- 🔧 AMD: Basic Models Tests (Initialization)
- 🔧 AMD: Basic Models Tests (Other)
- 🔧 AMD: Language Models Test (Extended Generation)
- 🔧 AMD: Language Models Test (Extended Pooling)
- 🔧 AMD: Language Models Tests (Extra Standard) %N
- 🔧 AMD: Language Models Tests (Hybrid) %N
- 🔧 AMD: Language Models Tests (Standard)
- 🔧 AMD: Multi-Modal Models (Extended Generation 1)
- 🔧 AMD: Multi-Modal Models (Standard) 1: qwen2
- 🔧 AMD: Multi-Modal Models (Standard) 2: qwen3 + gemma
- 🔧 AMD: Multi-Modal Models (Standard) 3: llava + qwen2_vl
- 🔧 AMD: Multi-Modal Models (Standard) 4: other + whisper
- 🔧 Basic Models Test (Other CPU)
- 🔧 Basic Models Tests (Extra Initialization) %N
- 🔧 Basic Models Tests (Initialization)
- 🔧 Basic Models Tests (Other)
- 🔧 CPU-Language Generation and Pooling Model Tests
- 🔧 CPU-Multi-Modal Model Tests %N
- 🔧 Distributed Model Tests (2 GPUs)
- 🔧 Kernels (B200)
- 🔧 Language Models Test (Extended Generation)
- 🔧 Language Models Test (Extended Pooling)
- 🔧 Language Models Test (MTEB)
- 🔧 Language Models Test (PPL)
- 🔧 Language Models Tests (Extra Standard) %N
- 🔧 Language Models Tests (Hybrid) %N
- 🔧 Language Models Tests (Standard)
- 🔧 Multi-Modal Models (Extended Generation 1)
- 🔧 Multi-Modal Models (Extended Generation 2)
- 🔧 Multi-Modal Models (Extended Generation 3)
- 🔧 Multi-Modal Models (Extended Pooling)
- 🔧 Multi-Modal Models (Standard) 1: qwen2
- 🔧 Multi-Modal Models (Standard) 2: qwen3 + gemma
- 🔧 Multi-Modal Models (Standard) 3: llava + qwen2_vl
- 🔧 Multi-Modal Models (Standard) 4: other + whisper
- 🔧 Multi-Modal Processor
- 🔧 Multi-Modal Processor (CPU)
- 🔧 Plugin Tests (2 GPUs)
- 🔧 Quantized Models Test
- 🔧 Transformers Backward Compatibility Models Test
- 🔧 Transformers Nightly Models

## Gap Analysis

LLM caught all CI failures — no gap to analyse.

---
*Generated: 2026-06-30 06:40 UTC*
