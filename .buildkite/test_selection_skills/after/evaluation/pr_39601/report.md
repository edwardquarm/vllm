# PR #39601 — Test Selection Evaluation

> **Build**: [67339](https://buildkite.com/vllm/ci/builds/67339) · **Date**: 2026-06-30

## Metrics

| | Count | Meaning |
|---|---|---|
| ✅ **True Positives** | **0** | LLM selected a test that CI actually failed |
| ❌ **False Negatives** | **129** | CI failed a test the LLM did not select (missed failures) |
| ⚠️ **False Positives** | **1** | LLM selected a test that CI passed (no failure detected) |

| Metric | Value | Formula |
|---|---|---|
| **Recall** (did LLM catch failures?) | **0.0%** | TP / (TP + FN) |
| **Precision** (were LLM picks relevant?) | **0.0%** | TP / (TP + FP) |

## CI Test Results

| Failed | Passed | Skipped | Total |
|--------|--------|---------|-------|
| 0 | 0 | 0 | 0 |

**CI jobs:** 213 passed · 22 failed · 16 blocked · **501 test files**

## LLM vs CI Comparison Table

```
Test File                                                                                                                      LLM Selected  CI Result
======================================================================================================================================================
[job] :docker: Build XPU image                                                                                                 ✗             ✗ Failed 
[job] Kernels Quantization Test 1                                                                                              ✗             ✗ Failed 
[job] Kernels Quantization Test 2                                                                                              ✗             ✗ Failed 
[job] Torch Nightly Basic Models Tests (Extra Initialization) 1                                                                ✗             ✗ Failed 
[job] Torch Nightly Basic Models Tests (Extra Initialization) 2                                                                ✗             ✗ Failed 
[job] XPU server test                                                                                                          ✗             ✗ Failed 
tests/.                                                                                                                        ✗             ✓ Passed 
tests/./compile                                                                                                                ✗             ✓ Passed 
tests/./compile/fullgraph                                                                                                      ✗             ✓ Passed 
tests/./compile/fullgraph/test_basic_correctness.py                                                                            ✗             ✓ Passed 
tests/./compile/test_wrapper.py                                                                                                ✗             ✓ Passed 
tests/./plugins_tests                                                                                                          ✗             ✓ Passed 
tests/./plugins_tests/test_io_processor_plugins.py                                                                             ✗             ✓ Passed 
tests/.buildkite                                                                                                               ✗             ✗ Failed 
tests/.buildkite/intel_jobs                                                                                                    ✗             ✗ Failed 
tests/.buildkite/intel_jobs/test-intel.yaml                                                                                    ✗             ✗ Failed 
tests/.buildkite/scripts                                                                                                       ✗             ✓ Passed 
tests/.buildkite/scripts/scheduled_integration_test                                                                            ✗             ✓ Passed 
tests/CMakeLists.txt                                                                                                           ✗             ✓ Passed 
tests/basic_correctness                                                                                                        ✗             ✗ Failed 
tests/basic_correctness/test_basic_correctness                                                                                 ✗             ✓ Passed 
tests/basic_correctness/test_basic_correctness.py                                                                              ✗             ✓ Passed 
tests/basic_correctness/test_cpu_offload                                                                                       ✗             ✓ Passed 
tests/basic_correctness/test_cpu_offload.py                                                                                    ✗             ✓ Passed 
tests/basic_correctness/test_cumem.py                                                                                          ✗             ✓ Passed 
tests/benchmarks                                                                                                               ✗             ✓ Passed 
tests/benchmarks/attention_benchmarks                                                                                          ✗             ✓ Passed 
tests/cmake                                                                                                                    ✗             ✓ Passed 
tests/cmake/cpu_extension.cmake                                                                                                ✗             ✓ Passed 
tests/compile                                                                                                                  ✗             ✗ Failed 
tests/compile/correctness_e2e                                                                                                  ✗             ✓ Passed 
tests/compile/correctness_e2e/test_async_tp.py                                                                                 ✗             ✓ Passed 
tests/compile/correctness_e2e/test_sequence_parallel.py                                                                        ✗             ✓ Passed 
tests/compile/fullgraph                                                                                                        ✗             ✗ Failed 
tests/compile/fullgraph/test_basic_correctness.py                                                                              ✗             ✓ Passed 
tests/compile/fullgraph/test_full_graph.py                                                                                     ✗             ✗ Failed 
tests/compile/fullgraph/test_full_graph.py::test_fp8_kv_scale_compile                                                          ✗             ✗ Failed 
tests/compile/fusions_e2e                                                                                                      ✗             ✓ Passed 
tests/compile/fusions_e2e/test_tp1_quant.py                                                                                    ✗             ✓ Passed 
tests/compile/fusions_e2e/test_tp2_ar_rms.py                                                                                   ✗             ✓ Passed 
tests/compile/fusions_e2e/test_tp2_async_tp.py                                                                                 ✗             ✓ Passed 
tests/compile/h100                                                                                                             ✗             ✓ Passed 
tests/compile/passes                                                                                                           ✗             ✗ Failed 
tests/compile/passes/distributed                                                                                               ✗             ✗ Failed 
tests/compile/passes/distributed/test_async_tp.py                                                                              ✗             ✓ Passed 
tests/compile/passes/distributed/test_fusion_all_reduce.py                                                                     ✗             ✗ Failed 
tests/compile/passes/distributed/test_sequence_parallelism.py                                                                  ✗             ✓ Passed 
tests/compile/passes/test_fusion_attn.py                                                                                       ✗             ✗ Failed 
tests/compile/passes/test_mla_attn_quant_fusion.py                                                                             ✗             ✗ Failed 
tests/compile/passes/test_silu_mul_quant_fusion.py                                                                             ✗             ✗ Failed 
tests/compile/test_wrapper.py                                                                                                  ✗             ✓ Passed 
tests/config                                                                                                                   ✗             ✓ Passed 
tests/conftest.py                                                                                                              ✗             ✓ Passed 
tests/csrc                                                                                                                     ✗             ✗ Failed 
tests/csrc/attention                                                                                                           ✗             ✗ Failed 
tests/csrc/attention/mla                                                                                                       ✗             ✗ Failed 
tests/csrc/cpu                                                                                                                 ✗             ✓ Passed 
tests/csrc/cpu/shm.cpp                                                                                                         ✗             ✓ Passed 
tests/csrc/mamba                                                                                                               ✗             ✓ Passed 
tests/csrc/minimax_reduce_rms_kernel.cu                                                                                        ✗             ✓ Passed 
tests/csrc/minimax_reduce_rms_kernel.h                                                                                         ✗             ✓ Passed 
tests/csrc/moe                                                                                                                 ✗             ✓ Passed 
tests/csrc/quantization                                                                                                        ✗             ✗ Failed 
tests/csrc/quantization/cutlass_w8a8                                                                                           ✗             ✗ Failed 
tests/csrc/quantization/cutlass_w8a8/moe                                                                                       ✗             ✗ Failed 
tests/csrc/quantization/fp4                                                                                                    ✗             ✗ Failed 
tests/csrc/quantization/w8a8                                                                                                   ✗             ✓ Passed 
tests/csrc/quantization/w8a8/cutlass                                                                                           ✗             ✓ Passed 
tests/csrc/quantization/w8a8/cutlass/moe                                                                                       ✗             ✓ Passed 
tests/cuda                                                                                                                     ✗             ✓ Passed 
tests/cuda/test_cuda_context.py                                                                                                ✗             ✓ Passed 
tests/cuda/test_platform_no_cuda_init.py                                                                                       ✗             ✓ Passed 
tests/detokenizer                                                                                                              ✗             ✓ Passed 
tests/distributed                                                                                                              ✗             ✗ Failed 
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
tests/distributed/test_torchrun_example.py                                                                                     ✗             ✗ Failed 
tests/distributed/test_torchrun_example_moe.py                                                                                 ✗             ✗ Failed 
tests/distributed/test_utils                                                                                                   ✗             ✓ Passed 
tests/distributed/test_utils.py                                                                                                ✗             ✓ Passed 
tests/distributed/test_weight_transfer.py                                                                                      ✗             ✓ Passed 
tests/engine                                                                                                                   ✗             ✓ Passed 
tests/entrypoints                                                                                                              ✗             ✗ Failed 
tests/entrypoints/llm                                                                                                          ✗             ✓ Passed 
tests/entrypoints/llm/test_collective_rpc.py                                                                                   ✗             ✓ Passed 
tests/entrypoints/llm/test_generate.py                                                                                         ✗             ✓ Passed 
tests/entrypoints/llm/test_struct_output_generate.py                                                                           ✗             ✓ Passed 
tests/entrypoints/offline_mode                                                                                                 ✗             ✓ Passed 
tests/entrypoints/openai                                                                                                       ✗             ✗ Failed 
tests/entrypoints/openai/chat_completion                                                                                       ✗             ✓ Passed 
tests/entrypoints/openai/chat_completion/test_oot_registration.py                                                              ✗             ✓ Passed 
tests/entrypoints/openai/completion                                                                                            ✗             ✓ Passed 
tests/entrypoints/openai/completion/test_tensorizer_entrypoint.py                                                              ✗             ✓ Passed 
tests/entrypoints/openai/correctness                                                                                           ✗             ✗ Failed 
tests/entrypoints/openai/correctness/test_lmeval.py                                                                            ✗             ✗ Failed 
tests/entrypoints/openai/correctness/test_lmeval.py::test_lm_eval_accuracy_v1_engine                                           ✗             ✗ Failed 
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
tests/examples                                                                                                                 ✗             ✗ Failed 
tests/examples/basic                                                                                                           ✗             ✓ Passed 
tests/examples/basic/offline_inference                                                                                         ✗             ✓ Passed 
tests/examples/features                                                                                                        ✗             ✗ Failed 
tests/examples/features/data_parallel                                                                                          ✗             ✗ Failed 
tests/examples/features/data_parallel/data_parallel_offline.py                                                                 ✗             ✗ Failed 
tests/examples/features/torchrun                                                                                               ✗             ✓ Passed 
tests/examples/features/torchrun/torchrun_dp_example_offline.py                                                                ✗             ✓ Passed 
tests/examples/generate                                                                                                        ✗             ✓ Passed 
tests/examples/generate/multimodal                                                                                             ✗             ✓ Passed 
tests/examples/others                                                                                                          ✗             ✓ Passed 
tests/examples/others/tensorize_vllm_model.py                                                                                  ✗             ✓ Passed 
tests/examples/pooling                                                                                                         ✗             ✓ Passed 
tests/examples/pooling/embed                                                                                                   ✗             ✓ Passed 
tests/examples/pooling/embed/vision_embedding_offline.py                                                                       ✗             ✓ Passed 
tests/examples/rl                                                                                                              ✗             ✗ Failed 
tests/ir                                                                                                                       ✗             ✓ Passed 
tests/kernels                                                                                                                  ✗             ✗ Failed 
tests/kernels/attention                                                                                                        ✗             ✗ Failed 
tests/kernels/attention/test_attention_selector.py                                                                             ✗             ✗ Failed 
tests/kernels/attention/test_cpu_attn.py                                                                                       ✗             ✓ Passed 
tests/kernels/attention/test_cutlass_mla_decode.py                                                                             ✗             ✗ Failed 
tests/kernels/attention/test_deepgemm_attention.py                                                                             ✗             ✓ Passed 
tests/kernels/attention/test_flashinfer.py                                                                                     ✗             ✗ Failed 
tests/kernels/attention/test_flashinfer_mla_decode.py                                                                          ✗             ✗ Failed 
tests/kernels/attention/test_flashinfer_trtllm_attention.py                                                                    ✗             ✗ Failed 
tests/kernels/core                                                                                                             ✗             ✓ Passed 
tests/kernels/core/test_minimax_reduce_rms.py                                                                                  ✗             ✓ Passed 
tests/kernels/helion                                                                                                           ✗             ✓ Passed 
tests/kernels/ir                                                                                                               ✗             ✓ Passed 
tests/kernels/ir'                                                                                                              ✗             ✓ Passed 
tests/kernels/mamba                                                                                                            ✗             ✓ Passed 
tests/kernels/moe                                                                                                              ✗             ✗ Failed 
tests/kernels/moe/test_batched_deepgemm.py                                                                                     ✗             ✓ Passed 
tests/kernels/moe/test_block_int8.py                                                                                           ✗             ✓ Passed 
tests/kernels/moe/test_cpu_fused_moe.py                                                                                        ✗             ✓ Passed 
tests/kernels/moe/test_cutedsl_moe.py                                                                                          ✗             ✗ Failed 
tests/kernels/moe/test_cutlass_moe.py                                                                                          ✗             ✓ Passed 
tests/kernels/moe/test_deepep_deepgemm_moe.py                                                                                  ✗             ✓ Passed 
tests/kernels/moe/test_deepep_moe.py                                                                                           ✗             ✓ Passed 
tests/kernels/moe/test_deepgemm.py                                                                                             ✗             ✓ Passed 
tests/kernels/moe/test_flashinfer.py                                                                                           ✗             ✗ Failed 
tests/kernels/moe/test_flashinfer_moe.py                                                                                       ✗             ✗ Failed 
tests/kernels/moe/test_gpt_oss_triton_kernels.py                                                                               ✗             ✓ Passed 
tests/kernels/moe/test_modular_oai_triton_moe.py                                                                               ✗             ✓ Passed 
tests/kernels/moe/test_moe.py                                                                                                  ✗             ✓ Passed 
tests/kernels/moe/test_moe_layer.py                                                                                            ✗             ✓ Passed 
tests/kernels/moe/test_mxfp4_moe.py                                                                                            ✗             ✗ Failed 
tests/kernels/moe/test_nvfp4_moe.py                                                                                            ✗             ✗ Failed 
tests/kernels/moe/test_ocp_mx_moe.py                                                                                           ✗             ✗ Failed 
tests/kernels/moe/test_triton_moe_no_act_mul.py                                                                                ✗             ✓ Passed 
tests/kernels/moe/test_triton_moe_ptpc_fp8.py                                                                                  ✗             ✓ Passed 
tests/kernels/quantization                                                                                                     ✗             ✗ Failed 
tests/kernels/quantization/test_block_fp8.py                                                                                   ✗             ✓ Passed 
tests/kernels/quantization/test_cutlass_scaled_mm.py                                                                           ✗             ✗ Failed 
tests/kernels/quantization/test_flashinfer_nvfp4_scaled_mm.py                                                                  ✗             ✗ Failed 
tests/kernels/quantization/test_flashinfer_scaled_mm.py                                                                        ✗             ✗ Failed 
tests/kernels/quantization/test_mxfp4_qutlass.py                                                                               ✗             ✗ Failed 
tests/kernels/quantization/test_nvfp4_quant.py                                                                                 ✗             ✗ Failed 
tests/kernels/quantization/test_nvfp4_qutlass.py                                                                               ✗             ✗ Failed 
tests/kernels/quantization/test_nvfp4_scaled_mm.py                                                                             ✗             ✗ Failed 
tests/kernels/quantization/test_rocm_skinny_gemms.py                                                                           ✗             ✓ Passed 
tests/kernels/quantization/test_silu_mul_nvfp4_quant.py                                                                        ✗             ✗ Failed 
tests/kernels/test_awq_int4_to_int8.py                                                                                         ✗             ✓ Passed 
tests/kernels/test_awq_int4_to_int8.py"                                                                                        ✗             ✓ Passed 
tests/kernels/test_concat_mla_q.py                                                                                             ✗             ✓ Passed 
tests/kernels/test_onednn.py                                                                                                   ✗             ✓ Passed 
tests/kernels/test_top_k_per_row.py                                                                                            ✗             ✗ Failed 
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
tests/models                                                                                                                   ✗             ✗ Failed 
tests/models/language                                                                                                          ✗             ✓ Passed 
tests/models/language/generation                                                                                               ✗             ✓ Passed 
tests/models/language/generation/test_common.py                                                                                ✗             ✓ Passed 
tests/models/language/generation_ppl_test                                                                                      ✗             ✓ Passed 
tests/models/language/pooling                                                                                                  ✗             ✓ Passed 
tests/models/language/pooling/test_classification.py                                                                           ✗             ✓ Passed 
tests/models/language/pooling/test_embedding.py                                                                                ✗             ✓ Passed 
tests/models/language/pooling_mteb_test                                                                                        ✗             ✓ Passed 
tests/models/multimodal                                                                                                        ✗             ✗ Failed 
tests/models/multimodal/generation                                                                                             ✗             ✗ Failed 
tests/models/multimodal/generation/test_common.py                                                                              ✗             ✗ Failed 
tests/models/multimodal/generation/test_memory_leak.py                                                                         ✗             ✓ Passed 
tests/models/multimodal/generation/test_phi4siglip.py                                                                          ✗             ✓ Passed 
tests/models/multimodal/generation/test_qwen2_5_vl.py                                                                          ✗             ✓ Passed 
tests/models/multimodal/generation/test_qwen2_vl.py                                                                            ✗             ✓ Passed 
tests/models/multimodal/generation/test_ultravox.py                                                                            ✗             ✓ Passed 
tests/models/multimodal/generation/test_vit_cudagraph.py                                                                       ✗             ✓ Passed 
tests/models/multimodal/generation/test_whisper.py                                                                             ✗             ✓ Passed 
tests/models/multimodal/pooling                                                                                                ✗             ✓ Passed 
tests/models/multimodal/processing                                                                                             ✗             ✗ Failed 
tests/models/multimodal/processing/test_tensor_schema.py                                                                       ✗             ✓ Passed 
tests/models/multimodal/test_mapping.py                                                                                        ✗             ✗ Failed 
tests/models/quantization                                                                                                      ✗             ✗ Failed 
tests/models/quantization/test_nvfp4.py                                                                                        ✗             ✗ Failed 
tests/models/registry.py                                                                                                       ✗             ✓ Passed 
tests/models/test_initialization.py                                                                                            ✗             ✗ Failed 
tests/models/test_initialization.py::test_can_initialize_small_subset                                                          ✗             ✓ Passed 
tests/models/test_oot_registration.py                                                                                          ✗             ✓ Passed 
tests/models/test_registry.py                                                                                                  ✗             ✓ Passed 
tests/models/test_terratorch.py                                                                                                ✗             ✓ Passed 
tests/models/test_transformers.py                                                                                              ✗             ✗ Failed 
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
tests/quantization                                                                                                             ✗             ✗ Failed 
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
tests/setup.py                                                                                                                 ✗             ✗ Failed 
tests/standalone_tests                                                                                                         ✗             ✗ Failed 
tests/standalone_tests/lazy_imports.py                                                                                         ✗             ✓ Passed 
tests/standalone_tests/python_only_compile.sh                                                                                  ✗             ✗ Failed 
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
tests/tool_parsers/test_glm4_moe_tool_parser.py                                                                                ✓             ✓ Passed 
tests/tool_use                                                                                                                 ✗             ✓ Passed 
tests/tools                                                                                                                    ✗             ✓ Passed 
tests/tools/install_deepgemm.sh                                                                                                ✗             ✓ Passed 
tests/transformers_utils                                                                                                       ✗             ✓ Passed 
tests/utils_                                                                                                                   ✗             ✓ Passed 
tests/v1                                                                                                                       ✗             ✗ Failed 
tests/v1/attention                                                                                                             ✗             ✓ Passed 
tests/v1/core                                                                                                                  ✗             ✗ Failed 
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
tests/v1/e2e                                                                                                                   ✗             ✗ Failed 
tests/v1/e2e/general                                                                                                           ✗             ✓ Passed 
tests/v1/e2e/general/test_async_scheduling.py                                                                                  ✗             ✓ Passed 
tests/v1/e2e/general/test_context_length.py                                                                                    ✗             ✓ Passed 
tests/v1/e2e/general/test_min_tokens.py                                                                                        ✗             ✓ Passed 
tests/v1/e2e/spec_decode                                                                                                       ✗             ✗ Failed 
tests/v1/e2e/spec_decode/test_spec_decode.py                                                                                   ✗             ✓ Passed 
tests/v1/e2e/test_hybrid_chunked_prefill.py                                                                                    ✗             ✓ Passed 
tests/v1/engine                                                                                                                ✗             ✓ Passed 
tests/v1/engine/test_engine_core_client.py                                                                                     ✗             ✓ Passed 
tests/v1/engine/test_engine_core_client.py::test_kv_cache_events_dp                                                            ✗             ✓ Passed 
tests/v1/engine/test_llm_engine.py                                                                                             ✗             ✓ Passed 
tests/v1/engine/test_preprocess_error_handling.py                                                                              ✗             ✓ Passed 
tests/v1/executor                                                                                                              ✗             ✗ Failed 
tests/v1/executor'                                                                                                             ✗             ✗ Failed 
tests/v1/kv_connector                                                                                                          ✗             ✗ Failed 
tests/v1/kv_connector/nixl_integration                                                                                         ✗             ✓ Passed 
tests/v1/kv_connector/unit                                                                                                     ✗             ✗ Failed 
tests/v1/kv_offload                                                                                                            ✗             ✗ Failed 
tests/v1/logits_processors                                                                                                     ✗             ✗ Failed 
tests/v1/metrics                                                                                                               ✗             ✗ Failed 
tests/v1/sample                                                                                                                ✗             ✗ Failed 
tests/v1/shutdown                                                                                                              ✗             ✓ Passed 
tests/v1/spec_decode                                                                                                           ✗             ✗ Failed 
tests/v1/spec_decode/test_acceptance_length.py                                                                                 ✗             ✓ Passed 
tests/v1/spec_decode/test_max_len.py                                                                                           ✗             ✓ Passed 
tests/v1/spec_decode/test_probabilistic_rejection_sampler_utils.py                                                             ✗             ✓ Passed 
tests/v1/spec_decode/test_speculators_dflash.py                                                                                ✗             ✓ Passed 
tests/v1/spec_decode/test_synthetic_rejection_sampler_utils.py                                                                 ✗             ✓ Passed 
tests/v1/structured_output                                                                                                     ✗             ✓ Passed 
tests/v1/test_oracle.py                                                                                                        ✗             ✗ Failed 
tests/v1/test_outputs.py                                                                                                       ✗             ✗ Failed 
tests/v1/test_request.py                                                                                                       ✗             ✗ Failed 
tests/v1/test_serial_utils.py                                                                                                  ✗             ✓ Passed 
tests/v1/tracing                                                                                                               ✗             ✓ Passed 
tests/v1/worker                                                                                                                ✗             ✗ Failed 
tests/v1/worker/test_worker_memory_snapshot.py                                                                                 ✗             ✓ Passed 
tests/vllm                                                                                                                     ✗             ✗ Failed 
tests/vllm/_aiter_ops.py                                                                                                       ✗             ✗ Failed 
tests/vllm/_custom_ops.py                                                                                                      ✗             ✓ Passed 
tests/vllm/beam_search.py                                                                                                      ✗             ✓ Passed 
tests/vllm/compilation                                                                                                         ✗             ✗ Failed 
tests/vllm/config                                                                                                              ✗             ✓ Passed 
tests/vllm/config/attention.py                                                                                                 ✗             ✓ Passed 
tests/vllm/config/compilation.py                                                                                               ✗             ✓ Passed 
tests/vllm/config/model.py                                                                                                     ✗             ✓ Passed 
tests/vllm/config/parallel.py                                                                                                  ✗             ✓ Passed 
tests/vllm/distributed                                                                                                         ✗             ✗ Failed 
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
tests/vllm/model_executor                                                                                                      ✗             ✗ Failed 
tests/vllm/model_executor/kernels                                                                                              ✗             ✓ Passed 
tests/vllm/model_executor/layers                                                                                               ✗             ✗ Failed 
tests/vllm/model_executor/layers/activation.py                                                                                 ✗             ✗ Failed 
tests/vllm/model_executor/layers/attention                                                                                     ✗             ✗ Failed 
tests/vllm/model_executor/layers/attention/attention.py                                                                        ✗             ✗ Failed 
tests/vllm/model_executor/layers/fla                                                                                           ✗             ✓ Passed 
tests/vllm/model_executor/layers/fla/ops                                                                                       ✗             ✓ Passed 
tests/vllm/model_executor/layers/fused_moe                                                                                     ✗             ✗ Failed 
tests/vllm/model_executor/layers/fused_moe/cutlass_moe.py                                                                      ✗             ✗ Failed 
tests/vllm/model_executor/layers/fused_moe/flashinfer_a2a_prepare_finalize.py                                                  ✗             ✗ Failed 
tests/vllm/model_executor/layers/fused_moe/flashinfer_cutlass_moe.py                                                           ✗             ✗ Failed 
tests/vllm/model_executor/layers/layernorm.py                                                                                  ✗             ✗ Failed 
tests/vllm/model_executor/layers/mamba                                                                                         ✗             ✓ Passed 
tests/vllm/model_executor/layers/mamba/lamport_workspace.py                                                                    ✗             ✓ Passed 
tests/vllm/model_executor/layers/mamba/linear_attn.py                                                                          ✗             ✓ Passed 
tests/vllm/model_executor/layers/mamba/ops                                                                                     ✗             ✓ Passed 
tests/vllm/model_executor/layers/quantization                                                                                  ✗             ✗ Failed 
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
tests/vllm/model_executor/layers/quantization/utils                                                                            ✗             ✗ Failed 
tests/vllm/model_executor/layers/quantization/utils/flashinfer_utils.py                                                        ✗             ✗ Failed 
tests/vllm/model_executor/layers/rotary_embedding                                                                              ✗             ✓ Passed 
tests/vllm/model_executor/model_loader                                                                                         ✗             ✗ Failed 
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
tests/vllm/platforms                                                                                                           ✗             ✗ Failed 
tests/vllm/platforms/cpu.py                                                                                                    ✗             ✓ Passed 
tests/vllm/platforms/cuda.py                                                                                                   ✗             ✗ Failed 
tests/vllm/platforms/rocm.py                                                                                                   ✗             ✗ Failed 
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
tests/vllm/v1                                                                                                                  ✗             ✗ Failed 
tests/vllm/v1/attention                                                                                                        ✗             ✗ Failed 
tests/vllm/v1/attention/backends                                                                                               ✗             ✗ Failed 
tests/vllm/v1/attention/backends/flashinfer.py                                                                                 ✗             ✗ Failed 
tests/vllm/v1/attention/backends/flex_attention.py                                                                             ✗             ✓ Passed 
tests/vllm/v1/attention/backends/mla                                                                                           ✗             ✗ Failed 
tests/vllm/v1/attention/backends/mla/aiter_triton_mla.py                                                                       ✗             ✓ Passed 
tests/vllm/v1/attention/backends/mla/cutlass_mla.py                                                                            ✗             ✗ Failed 
tests/vllm/v1/attention/backends/mla/flashinfer_mla.py                                                                         ✗             ✗ Failed 
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
tests/vllm/v1/attention/selector.py                                                                                            ✗             ✗ Failed 
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
tests/vllm/v1/sample                                                                                                           ✗             ✗ Failed 
tests/vllm/v1/spec_decode                                                                                                      ✗             ✗ Failed 
tests/vllm/v1/worker                                                                                                           ✗             ✗ Failed 
tests/vllm/v1/worker/cpu_model_runner.py                                                                                       ✗             ✓ Passed 
tests/vllm/v1/worker/cpu_worker.py                                                                                             ✗             ✓ Passed 
tests/vllm/v1/worker/gpu                                                                                                       ✗             ✗ Failed 
tests/vllm/v1/worker/gpu/spec_decode                                                                                           ✗             ✗ Failed 
tests/vllm/v1/worker/gpu_model_runner.py                                                                                       ✗             ✓ Passed 
tests/vllm/v1/worker/gpu_worker.py                                                                                             ✗             ✓ Passed 
tests/vllm/v1/worker/kv_connector_model_runner_mixin.py                                                                        ✗             ✓ Passed 
tests/vllm/worker                                                                                                              ✗             ✓ Passed 
tests/vllm/worker/worker_base.py                                                                                               ✗             ✓ Passed 
tests/weight_loading                                                                                                           ✗             ✓ Passed 
```

**Summary:** 501 total tests, 1 LLM selected, 129 CI failed

### Failed jobs

**❌ :docker: Build XPU image** — 1 test(s) failed

- `[job] :docker: Build XPU image`

**❌ Ascend NPU Test** — 1 test(s) failed

- `tests/basic_correctness`

**❌ Distributed Torchrun + Examples (4 GPUs)** — 9 test(s) failed

- `tests/distributed`
- `tests/distributed/test_torchrun_example.py`
- `tests/distributed/test_torchrun_example_moe.py`
- `tests/examples`
- `tests/examples/features`
- `tests/examples/features/data_parallel`
- `tests/examples/features/data_parallel/data_parallel_offline.py`
- `tests/examples/rl`
- `tests/vllm/distributed`

**❌ Fusion and Compile Unit Tests (2xB200)** — 15 test(s) failed

- `tests/compile`
- `tests/compile/fullgraph`
- `tests/compile/fullgraph/test_full_graph.py`
- `tests/compile/fullgraph/test_full_graph.py::test_fp8_kv_scale_compile`
- `tests/compile/passes`
- `tests/compile/passes/distributed`
- `tests/compile/passes/distributed/test_fusion_all_reduce.py`
- `tests/compile/passes/test_fusion_attn.py`
- `tests/compile/passes/test_mla_attn_quant_fusion.py`
- `tests/compile/passes/test_silu_mul_quant_fusion.py`
- `tests/vllm/compilation`
- `tests/vllm/model_executor/layers/activation.py`
- `tests/vllm/model_executor/layers/attention`
- `tests/vllm/model_executor/layers/attention/attention.py`
- `tests/vllm/model_executor/layers/layernorm.py`

**❌ Kernels (B200)** — 45 test(s) failed

- `tests/csrc/attention`
- `tests/csrc/attention/mla`
- `tests/csrc/quantization`
- `tests/csrc/quantization/cutlass_w8a8`
- `tests/csrc/quantization/cutlass_w8a8/moe`
- `tests/csrc/quantization/fp4`
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
- `tests/models/quantization/test_nvfp4.py`
- `tests/vllm/model_executor/layers/fused_moe`
- `tests/vllm/model_executor/layers/fused_moe/cutlass_moe.py`
- `tests/vllm/model_executor/layers/fused_moe/flashinfer_a2a_prepare_finalize.py`
- `tests/vllm/model_executor/layers/fused_moe/flashinfer_cutlass_moe.py`
- `tests/vllm/model_executor/layers/quantization/utils`
- `tests/vllm/model_executor/layers/quantization/utils/flashinfer_utils.py`
- `tests/vllm/platforms/cuda.py`
- `tests/vllm/v1/attention`
- `tests/vllm/v1/attention/backends`
- `tests/vllm/v1/attention/backends/flashinfer.py`
- `tests/vllm/v1/attention/backends/mla`
- `tests/vllm/v1/attention/backends/mla/cutlass_mla.py`
- `tests/vllm/v1/attention/backends/mla/flashinfer_mla.py`
- `tests/vllm/v1/attention/selector.py`

**❌ Kernels Quantization Test 1** — 1 test(s) failed

- `[job] Kernels Quantization Test 1`

**❌ Kernels Quantization Test 2** — 1 test(s) failed

- `[job] Kernels Quantization Test 2`

**❌ Multi-Modal Models (Extended Generation 3)** — 5 test(s) failed

- `tests/models`
- `tests/models/multimodal`
- `tests/models/multimodal/generation`
- `tests/models/multimodal/generation/test_common.py`
- `tests/vllm`

**❌ Python-only Installation** — 3 test(s) failed

- `tests/setup.py`
- `tests/standalone_tests`
- `tests/standalone_tests/python_only_compile.sh`

**❌ Quantization** — 2 test(s) failed

- `tests/csrc`
- `tests/quantization`

**❌ Quantized Models Test** — 8 test(s) failed

- `tests/models/quantization`
- `tests/vllm/_aiter_ops.py`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/layers`
- `tests/vllm/model_executor/layers/quantization`
- `tests/vllm/model_executor/model_loader`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`

**❌ Spec Decode Draft Model** — 1 test(s) failed

- `tests/vllm/v1/sample`

**❌ Spec Decode Draft Model Nightly B200** — 8 test(s) failed

- `tests/v1`
- `tests/v1/e2e`
- `tests/v1/e2e/spec_decode`
- `tests/vllm/v1`
- `tests/vllm/v1/spec_decode`
- `tests/vllm/v1/worker`
- `tests/vllm/v1/worker/gpu`
- `tests/vllm/v1/worker/gpu/spec_decode`

**❌ Torch Nightly Basic Models Tests (Extra Initialization) 1** — 1 test(s) failed

- `[job] Torch Nightly Basic Models Tests (Extra Initialization) 1`

**❌ Torch Nightly Basic Models Tests (Extra Initialization) 2** — 1 test(s) failed

- `[job] Torch Nightly Basic Models Tests (Extra Initialization) 2`

**❌ Transformers Backward Compatibility Models Test** — 4 test(s) failed

- `tests/models/multimodal/processing`
- `tests/models/multimodal/test_mapping.py`
- `tests/models/test_initialization.py`
- `tests/models/test_transformers.py`

**❌ V1 Core + KV + Metrics** — 12 test(s) failed

- `tests/entrypoints`
- `tests/entrypoints/openai`
- `tests/entrypoints/openai/correctness`
- `tests/entrypoints/openai/correctness/test_lmeval.py`
- `tests/entrypoints/openai/correctness/test_lmeval.py::test_lm_eval_accuracy_v1_engine`
- `tests/v1/executor`
- `tests/v1/executor'`
- `tests/v1/kv_connector`
- `tests/v1/kv_connector/unit`
- `tests/v1/kv_offload`
- `tests/v1/metrics`
- `tests/v1/worker`

**❌ V1 Sample + Logits** — 5 test(s) failed

- `tests/v1/logits_processors`
- `tests/v1/sample`
- `tests/v1/test_oracle.py`
- `tests/v1/test_outputs.py`
- `tests/v1/test_request.py`

**❌ V1 Spec Decode** — 1 test(s) failed

- `tests/v1/spec_decode`

**❌ XPU V1 test** — 4 test(s) failed

- `tests/.buildkite`
- `tests/.buildkite/intel_jobs`
- `tests/.buildkite/intel_jobs/test-intel.yaml`
- `tests/v1/core`

**❌ XPU server test** — 1 test(s) failed

- `[job] XPU server test`

### Passing jobs

**✅ 2 Node Test (4 GPUs)**

- `tests/distributed`
- `tests/distributed/test_multi_node_assignment.py`
- `tests/examples`
- `tests/examples/features`
- `tests/examples/features/data_parallel`
- `tests/examples/features/data_parallel/data_parallel_offline.py`
- `tests/vllm`
- `tests/vllm/distributed`
- `tests/vllm/engine`
- `tests/vllm/executor`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/models`

**✅ :docker: Build CPU arm64 image**

- (test paths unknown)

**✅ :docker: Build CPU image**

- (test paths unknown)

**✅ :docker: Build HPU image**

- (test paths unknown)

**✅ :docker: Build image**

- (test paths unknown)

**✅ :docker: build image torch nightly**

- (test paths unknown)

**✅ AMD: :docker: build image**

- (test paths unknown)

**✅ AMD: Engine (1 GPU) (mi300_1)**

- (test paths unknown)

**✅ AMD: Entrypoints Integration (API Server 2) (mi300_1)**

- (test paths unknown)

**✅ AMD: Entrypoints Integration (API Server openai - Part 1) (mi300_1)**

- (test paths unknown)

**✅ AMD: Entrypoints Integration (API Server openai - Part 2) (mi300_1)**

- (test paths unknown)

**✅ AMD: Entrypoints Integration (API Server openai - Part 3) (mi300_1)**

- (test paths unknown)

**✅ AMD: Entrypoints Integration (LLM) (mi300_1)**

- (test paths unknown)

**✅ AMD: Kernels Quantization Test 1 (mi300_1)**

- (test paths unknown)

**✅ AMD: Kernels Quantization Test 2 (mi300_1)**

- (test paths unknown)

**✅ AMD: Language Models Test (Extended Pooling) (mi300_1)**

- (test paths unknown)

**✅ AMD: Language Models Tests (Hybrid) 1 (mi300_1)**

- (test paths unknown)

**✅ AMD: Language Models Tests (Hybrid) 2 (mi300_1)**

- (test paths unknown)

**✅ AMD: Multi-Modal Models (Extended Generation 1) (mi300_1)**

- (test paths unknown)

**✅ AMD: Multi-Modal Models (Standard) 1: qwen2 (mi300_1)**

- (test paths unknown)

**✅ AMD: Multi-Modal Models (Standard) 2: qwen3 + gemma (mi300_1)**

- (test paths unknown)

**✅ AMD: Multi-Modal Models (Standard) 3: llava + qwen2_vl (mi300_1)**

- (test paths unknown)

**✅ AMD: Samplers Test (mi250_1)**

- (test paths unknown)

**✅ AMD: V1 Sample + Logits (mi300_1)**

- (test paths unknown)

**✅ AMD: e2e Scheduling (1 GPU) (mi250_1)**

- (test paths unknown)

**✅ Acceptance Length Test (Large Models)**

- `tests/v1`
- `tests/v1/spec_decode`
- `tests/v1/spec_decode/test_acceptance_length.py`
- `tests/vllm`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/models`
- `tests/vllm/model_executor/models/mlp_speculator.py`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`
- `tests/vllm/v1`
- `tests/vllm/v1/spec_decode`

**✅ Arm CPU Test**

- (test paths unknown)

**✅ Async Engine, Inputs, Utils, Worker**

- `tests/detokenizer`
- `tests/multimodal`
- `tests/utils_`
- `tests/vllm`

**✅ Async Engine, Inputs, Utils, Worker, Config (CPU)**

- `tests/config`
- `tests/multimodal`
- `tests/reasoning`
- `tests/renderers`
- `tests/standalone_tests`
- `tests/standalone_tests/lazy_imports.py`
- `tests/test_inputs.py`
- `tests/test_outputs.py`
- `tests/test_pooling_params.py`
- `tests/test_ray_env.py`
- `tests/tokenizers_`
- `tests/tool_parsers`
- `tests/transformers_utils`
- `tests/vllm`

**✅ AsyncTP Correctness Tests (2xH100)**

- `tests/compile`
- `tests/compile/correctness_e2e`
- `tests/compile/correctness_e2e/test_async_tp.py`

**✅ AsyncTP Correctness Tests (B200)**

- `tests/compile`
- `tests/compile/correctness_e2e`
- `tests/compile/correctness_e2e/test_async_tp.py`

**✅ Attention Benchmarks Smoke Test (B200)**

- `tests/benchmarks`
- `tests/benchmarks/attention_benchmarks`
- `tests/vllm`
- `tests/vllm/v1`
- `tests/vllm/v1/attention`

**✅ Basic Correctness**

- `tests/basic_correctness`
- `tests/basic_correctness/test_basic_correctness`
- `tests/basic_correctness/test_basic_correctness.py`
- `tests/basic_correctness/test_cpu_offload`
- `tests/basic_correctness/test_cpu_offload.py`
- `tests/basic_correctness/test_cumem.py`
- `tests/vllm`

**✅ Basic Models Test (Other CPU)**

- `tests/models`
- `tests/models/test_utils.py`
- `tests/models/test_vision.py`
- `tests/vllm`

**✅ Basic Models Tests (Extra Initialization) 1**

- (test paths unknown)

**✅ Basic Models Tests (Extra Initialization) 2**

- (test paths unknown)

**✅ Basic Models Tests (Initialization)**

- `tests/models`
- `tests/models/registry.py`
- `tests/models/test_initialization.py`
- `tests/models/test_initialization.py::test_can_initialize_small_subset`
- `tests/vllm`

**✅ Basic Models Tests (Other)**

- `tests/models`
- `tests/models/test_registry.py`
- `tests/models/test_terratorch.py`
- `tests/models/test_transformers.py`
- `tests/vllm`

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
- `tests/vllm`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/layers`
- `tests/vllm/v1`
- `tests/vllm/v1/attention`

**✅ Batch Invariance (H100)**

- `tests/v1`
- `tests/v1/determinism`
- `tests/v1/determinism/test_batch_invariance.py`
- `tests/v1/determinism/test_batch_invariance.py::test_v1_generation_is_deterministic_across_batch_sizes_with_needle[FLASH_ATTN]`
- `tests/v1/determinism/test_batch_invariance.py::test_v1_generation_is_deterministic_across_batch_sizes_with_needle[TRITON_MLA]`
- `tests/v1/determinism/test_rms_norm_batch_invariant.py`
- `tests/vllm`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/layers`
- `tests/vllm/v1`
- `tests/vllm/v1/attention`

**✅ Benchmarks CLI Test**

- `tests/benchmarks`
- `tests/vllm`

**✅ CPU-Compatibility Tests**

- `tests/cmake`
- `tests/cmake/cpu_extension.cmake`
- `tests/setup.py`
- `tests/vllm`
- `tests/vllm/platforms`
- `tests/vllm/platforms/cpu.py`

**✅ CPU-Distributed Tests (DP+TP)**

- (test paths unknown)

**✅ CPU-Distributed Tests (PP+TP)**

- (test paths unknown)

**✅ CPU-Kernel Tests**

- `tests/CMakeLists.txt`
- `tests/cmake`
- `tests/cmake/cpu_extension.cmake`
- `tests/csrc`
- `tests/csrc/cpu`
- `tests/kernels`
- `tests/kernels/attention`
- `tests/kernels/attention/test_cpu_attn.py`
- `tests/kernels/moe`
- `tests/kernels/moe/test_cpu_fused_moe.py`
- `tests/kernels/test_awq_int4_to_int8.py`
- `tests/kernels/test_awq_int4_to_int8.py"`
- `tests/kernels/test_onednn.py`
- `tests/vllm`
- `tests/vllm/_custom_ops.py`

**✅ CPU-Language Generation and Pooling Model Tests**

- `tests/csrc`
- `tests/csrc/cpu`
- `tests/models`
- `tests/models/language`
- `tests/models/language/generation`
- `tests/models/language/pooling`
- `tests/vllm`

**✅ CPU-Multi-Modal Model Tests 1**

- (test paths unknown)

**✅ CPU-Multi-Modal Model Tests 2**

- (test paths unknown)

**✅ CPU-Multi-Modal Model Tests 3**

- (test paths unknown)

**✅ CPU-Quantization Model Tests**

- `tests/csrc`
- `tests/csrc/cpu`
- `tests/quantization`
- `tests/quantization/test_compressed_tensors.py`
- `tests/quantization/test_compressed_tensors.py::test_compressed_tensors_w8a8_logprobs`
- `tests/quantization/test_cpu_wna16.py`
- `tests/quantization/test_cpu_wna16.py"`
- `tests/vllm`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/layers`
- `tests/vllm/model_executor/layers/quantization`
- `tests/vllm/model_executor/layers/quantization/compressed_tensors`
- `tests/vllm/model_executor/layers/quantization/compressed_tensors/schemes`
- `tests/vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8.py`
- `tests/vllm/model_executor/layers/quantization/cpu_wna16.py`
- `tests/vllm/model_executor/layers/quantization/gptq_marlin.py`
- `tests/vllm/model_executor/layers/quantization/kernels`
- `tests/vllm/model_executor/layers/quantization/kernels/mixed_precision`
- `tests/vllm/model_executor/layers/quantization/kernels/mixed_precision/cpu.py`
- `tests/vllm/model_executor/layers/quantization/kernels/scaled_mm`
- `tests/vllm/model_executor/layers/quantization/kernels/scaled_mm/cpu.py`

**✅ CrossLayer KV layout Distributed NixlConnector PD accuracy tests (4 GPUs)**

- `tests/v1`
- `tests/v1/kv_connector`
- `tests/v1/kv_connector/nixl_integration`
- `tests/vllm`
- `tests/vllm/distributed`
- `tests/vllm/distributed/kv_transfer`
- `tests/vllm/distributed/kv_transfer/kv_connector`
- `tests/vllm/distributed/kv_transfer/kv_connector/v1`
- `tests/vllm/distributed/kv_transfer/kv_connector/v1/nixl_connector.py`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`

**✅ Cudagraph**

- `tests/v1`
- `tests/v1/cudagraph`
- `tests/v1/cudagraph/test_cudagraph_dispatch.py`
- `tests/v1/cudagraph/test_cudagraph_mode.py`
- `tests/vllm`
- `tests/vllm/compilation`
- `tests/vllm/config`
- `tests/vllm/config/compilation.py`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`
- `tests/vllm/v1`
- `tests/vllm/v1/cudagraph_dispatcher.py`

**✅ DP EP Distributed NixlConnector PD accuracy tests (4 GPUs)**

- `tests/v1`
- `tests/v1/kv_connector`
- `tests/v1/kv_connector/nixl_integration`
- `tests/vllm`
- `tests/vllm/distributed`
- `tests/vllm/distributed/kv_transfer`
- `tests/vllm/distributed/kv_transfer/kv_connector`
- `tests/vllm/distributed/kv_transfer/kv_connector/v1`
- `tests/vllm/distributed/kv_transfer/kv_connector/v1/nixl_connector.py`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`

**✅ DeepSeek V2-Lite Accuracy**

- (test paths unknown)

**✅ DeepSeek V2-Lite Prefetch Offload Accuracy (H100)**

- (test paths unknown)

**✅ Distributed Comm Ops**

- `tests/distributed`
- `tests/distributed/test_comm_ops.py`
- `tests/distributed/test_shm_broadcast.py`
- `tests/distributed/test_shm_buffer.py`
- `tests/distributed/test_shm_storage.py`
- `tests/vllm`
- `tests/vllm/distributed`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`

**✅ Distributed Compile + Comm (4 GPUs)**

- `tests/compile`
- `tests/compile/fullgraph`
- `tests/compile/fullgraph/test_basic_correctness.py`
- `tests/distributed`
- `tests/distributed/test_events`
- `tests/distributed/test_events.py`
- `tests/distributed/test_multiproc_executor.py`
- `tests/distributed/test_multiproc_executor.py::test_multiproc_executor_multi_node`
- `tests/distributed/test_pynccl`
- `tests/distributed/test_pynccl.py`
- `tests/distributed/test_symm_mem_allreduce.py`
- `tests/vllm`
- `tests/vllm/distributed`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`

**✅ Distributed Compile + RPC Tests (2 GPUs)**

- `tests/.`
- `tests/./compile`
- `tests/./compile/fullgraph`
- `tests/./compile/fullgraph/test_basic_correctness.py`
- `tests/./compile/test_wrapper.py`
- `tests/compile`
- `tests/compile/fullgraph`
- `tests/compile/fullgraph/test_basic_correctness.py`
- `tests/compile/test_wrapper.py`
- `tests/entrypoints`
- `tests/entrypoints/llm`
- `tests/entrypoints/llm/test_collective_rpc.py`
- `tests/vllm`
- `tests/vllm/compilation`
- `tests/vllm/distributed`
- `tests/vllm/engine`
- `tests/vllm/executor`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`
- `tests/vllm/v1`
- `tests/vllm/v1/engine`
- `tests/vllm/v1/worker`
- `tests/vllm/worker`
- `tests/vllm/worker/worker_base.py`

**✅ Distributed Compile Unit Tests (2xH100)**

- `tests/compile`
- `tests/compile/passes`
- `tests/compile/passes/distributed`
- `tests/vllm`
- `tests/vllm/compilation`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/layers`

**✅ Distributed DP Tests (2 GPUs)**

- `tests/entrypoints`
- `tests/entrypoints/openai`
- `tests/entrypoints/openai/test_multi_api_servers.py`
- `tests/v1`
- `tests/v1/distributed`
- `tests/v1/distributed/test_async_llm_dp.py`
- `tests/v1/distributed/test_eagle_dp.py`
- `tests/v1/distributed/test_external_lb_dp.py`
- `tests/vllm`
- `tests/vllm/distributed`
- `tests/vllm/engine`
- `tests/vllm/executor`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`
- `tests/vllm/v1`
- `tests/vllm/v1/engine`
- `tests/vllm/v1/worker`
- `tests/vllm/worker`
- `tests/vllm/worker/worker_base.py`

**✅ Distributed DP Tests (4 GPUs)**

- `tests/distributed`
- `tests/distributed/test_utils`
- `tests/distributed/test_utils.py`
- `tests/v1`
- `tests/v1/distributed`
- `tests/v1/distributed/test_async_llm_dp.py`
- `tests/v1/distributed/test_eagle_dp.py`
- `tests/v1/distributed/test_external_lb_dp.py`
- `tests/v1/distributed/test_hybrid_lb_dp.py`
- `tests/v1/distributed/test_internal_lb_dp.py`
- `tests/v1/engine`
- `tests/v1/engine/test_engine_core_client.py`
- `tests/v1/engine/test_engine_core_client.py::test_kv_cache_events_dp`
- `tests/vllm`
- `tests/vllm/distributed`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`

**✅ Distributed FlashInfer NixlConnector PD accuracy (4 GPUs)**

- `tests/v1`
- `tests/v1/kv_connector`
- `tests/v1/kv_connector/nixl_integration`
- `tests/vllm`
- `tests/vllm/distributed`
- `tests/vllm/distributed/kv_transfer`
- `tests/vllm/distributed/kv_transfer/kv_connector`
- `tests/vllm/distributed/kv_transfer/kv_connector/v1`
- `tests/vllm/distributed/kv_transfer/kv_connector/v1/nixl_connector.py`

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

**✅ Distributed NixlConnector PD accuracy (4 GPUs)**

- `tests/v1`
- `tests/v1/kv_connector`
- `tests/v1/kv_connector/nixl_integration`
- `tests/vllm`
- `tests/vllm/distributed`
- `tests/vllm/distributed/kv_transfer`
- `tests/vllm/distributed/kv_transfer/kv_connector`
- `tests/vllm/distributed/kv_transfer/kv_connector/v1`
- `tests/vllm/distributed/kv_transfer/kv_connector/v1/nixl_connector.py`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`

**✅ Distributed Tests (2 GPUs)(B200)**

- `tests/distributed`
- `tests/distributed/test_context_parallel.py`
- `tests/distributed/test_nccl_symm_mem_allreduce.py`
- `tests/v1`
- `tests/v1/distributed`
- `tests/v1/distributed/test_dbo.py`

**✅ Distributed Tests (2 GPUs)(H100)**

- `tests/distributed`
- `tests/distributed/test_context_parallel.py`
- `tests/distributed/test_packed_tensor.py`
- `tests/distributed/test_weight_transfer.py`
- `tests/v1`
- `tests/v1/distributed`
- `tests/v1/distributed/test_dbo.py`

**✅ Distributed Tests (4 GPUs)(A100)**

- `tests/basic_correctness`
- `tests/distributed`
- `tests/distributed/test_custom_all_reduce.py`
- `tests/lora`
- `tests/lora/test_mixtral.py`
- `tests/vllm`

**✅ Distributed Tests (8 GPUs)(H100)**

- `tests/examples`
- `tests/examples/features`
- `tests/examples/features/torchrun`
- `tests/examples/features/torchrun/torchrun_dp_example_offline.py`
- `tests/vllm`
- `tests/vllm/config`
- `tests/vllm/config/parallel.py`
- `tests/vllm/distributed`
- `tests/vllm/v1`
- `tests/vllm/v1/engine`
- `tests/vllm/v1/engine/llm_engine.py`
- `tests/vllm/v1/executor`
- `tests/vllm/v1/executor/uniproc_executor.py`
- `tests/vllm/v1/worker`
- `tests/vllm/v1/worker/gpu_worker.py`

**✅ Distributed Torchrun + Shutdown Tests (2 GPUs)**

- `tests/distributed`
- `tests/v1`
- `tests/v1/shutdown`
- `tests/v1/worker`
- `tests/v1/worker/test_worker_memory_snapshot.py`
- `tests/vllm`
- `tests/vllm/distributed`
- `tests/vllm/engine`
- `tests/vllm/executor`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`
- `tests/vllm/v1`
- `tests/vllm/v1/engine`
- `tests/vllm/v1/worker`
- `tests/vllm/worker`
- `tests/vllm/worker/worker_base.py`

**✅ Docker Build Metadata**

- (test paths unknown)

**✅ EPLB Algorithm**

- `tests/distributed`
- `tests/distributed/test_eplb_algo.py`
- `tests/distributed/test_eplb_utils.py`
- `tests/vllm`
- `tests/vllm/distributed`
- `tests/vllm/distributed/eplb`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`

**✅ EPLB Execution**

- `tests/distributed`
- `tests/distributed/test_eplb_execute.py`
- `tests/distributed/test_eplb_spec_decode.py`
- `tests/vllm`
- `tests/vllm/distributed`
- `tests/vllm/distributed/eplb`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`

**✅ Elastic EP Scaling Test**

- `tests/distributed`
- `tests/distributed/test_elastic_ep.py`
- `tests/vllm`
- `tests/vllm/compilation`
- `tests/vllm/distributed`
- `tests/vllm/engine`
- `tests/vllm/executor`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`

**✅ Engine**

- `tests/engine`
- `tests/test_config`
- `tests/test_logger`
- `tests/test_sequence`
- `tests/test_vllm_port`
- `tests/vllm`

**✅ Engine (1 GPU)**

- `tests/v1`
- `tests/v1/engine`
- `tests/v1/engine/test_preprocess_error_handling.py`
- `tests/vllm`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`
- `tests/vllm/v1`
- `tests/vllm/v1/engine`

**✅ Entrypoints Integration (API Server 2)**

- `tests/entrypoints`
- `tests/entrypoints/rpc`
- `tests/entrypoints/serve`
- `tests/entrypoints/serve/instrumentator`
- `tests/tool_use`
- `tests/vllm`

**✅ Entrypoints Integration (API Server openai - Part 1)**

- `tests/entrypoints`
- `tests/entrypoints/openai`
- `tests/entrypoints/openai/chat_completion`
- `tests/entrypoints/test_chat_utils`
- `tests/vllm`

**✅ Entrypoints Integration (API Server openai - Part 2)**

- `tests/entrypoints`
- `tests/entrypoints/openai`
- `tests/entrypoints/openai/completion`
- `tests/entrypoints/openai/speech_to_text`
- `tests/entrypoints/test_chat_utils`
- `tests/entrypoints/test_chat_utils.py`
- `tests/vllm`

**✅ Entrypoints Integration (API Server openai - Part 3)**

- `tests/entrypoints`
- `tests/entrypoints/openai`
- `tests/entrypoints/test_chat_utils`
- `tests/vllm`

**✅ Entrypoints Integration (LLM)**

- `tests/entrypoints`
- `tests/entrypoints/llm`
- `tests/entrypoints/llm/test_generate.py`
- `tests/entrypoints/offline_mode`
- `tests/vllm`

**✅ Entrypoints Integration (Pooling)**

- `tests/entrypoints`
- `tests/entrypoints/pooling`
- `tests/vllm`

**✅ Entrypoints Integration (Responses API)**

- `tests/entrypoints`
- `tests/entrypoints/openai`
- `tests/entrypoints/openai/responses`
- `tests/vllm`

**✅ Entrypoints Integration (Speech to Text)**

- (test paths unknown)

**✅ Entrypoints Unit Tests**

- `tests/entrypoints`
- `tests/entrypoints/openai`
- `tests/entrypoints/openai/tool_parsers`
- `tests/vllm`
- `tests/vllm/entrypoints`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`

**✅ Examples**

- `tests/examples`
- `tests/vllm`
- `tests/vllm/entrypoints`
- `tests/vllm/multimodal`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`

**✅ Extract Hidden States Integration**

- (test paths unknown)

**✅ Fusion E2E Config Sweep (B200)**

- `tests/compile`
- `tests/compile/fusions_e2e`
- `tests/compile/fusions_e2e/test_tp1_quant.py`

**✅ Fusion E2E Config Sweep (H100)**

- `tests/compile`
- `tests/compile/fusions_e2e`
- `tests/compile/fusions_e2e/test_tp1_quant.py`
- `tests/csrc`
- `tests/csrc/quantization`
- `tests/vllm`
- `tests/vllm/compilation`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/layers`
- `tests/vllm/model_executor/layers/activation.py`
- `tests/vllm/model_executor/layers/attention`
- `tests/vllm/model_executor/layers/attention/attention.py`
- `tests/vllm/model_executor/layers/layernorm.py`
- `tests/vllm/model_executor/layers/quantization`
- `tests/vllm/model_executor/layers/quantization/input_quant_fp8.py`

**✅ Fusion E2E Quick (H100)**

- `tests/compile`
- `tests/compile/fusions_e2e`
- `tests/compile/fusions_e2e/test_tp1_quant.py`
- `tests/csrc`
- `tests/csrc/quantization`
- `tests/vllm`
- `tests/vllm/compilation`
- `tests/vllm/model_executor`
- `tests/vllm/v1`
- `tests/vllm/v1/attention`

**✅ Fusion E2E TP2 (B200)**

- `tests/compile`
- `tests/compile/fusions_e2e`
- `tests/compile/fusions_e2e/test_tp2_ar_rms.py`
- `tests/compile/fusions_e2e/test_tp2_async_tp.py`
- `tests/csrc`
- `tests/csrc/quantization`
- `tests/vllm`
- `tests/vllm/compilation`
- `tests/vllm/model_executor`
- `tests/vllm/v1`
- `tests/vllm/v1/attention`

**✅ Fusion E2E TP2 AR-RMS Config Sweep (H100)**

- `tests/compile`
- `tests/compile/fusions_e2e`
- `tests/compile/fusions_e2e/test_tp2_ar_rms.py`
- `tests/csrc`
- `tests/csrc/quantization`
- `tests/vllm`
- `tests/vllm/compilation`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/layers`
- `tests/vllm/model_executor/layers/activation.py`
- `tests/vllm/model_executor/layers/attention`
- `tests/vllm/model_executor/layers/attention/attention.py`
- `tests/vllm/model_executor/layers/layernorm.py`
- `tests/vllm/model_executor/layers/quantization`
- `tests/vllm/model_executor/layers/quantization/input_quant_fp8.py`

**✅ Fusion E2E TP2 AsyncTP Config Sweep (H100)**

- `tests/compile`
- `tests/compile/fusions_e2e`
- `tests/compile/fusions_e2e/test_tp2_async_tp.py`
- `tests/csrc`
- `tests/csrc/quantization`
- `tests/vllm`
- `tests/vllm/compilation`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/layers`
- `tests/vllm/model_executor/layers/activation.py`
- `tests/vllm/model_executor/layers/attention`
- `tests/vllm/model_executor/layers/attention/attention.py`
- `tests/vllm/model_executor/layers/layernorm.py`
- `tests/vllm/model_executor/layers/quantization`
- `tests/vllm/model_executor/layers/quantization/input_quant_fp8.py`

**✅ Fusion E2E TP2 Quick (H100)**

- `tests/compile`
- `tests/compile/fusions_e2e`
- `tests/compile/fusions_e2e/test_tp2_ar_rms.py`
- `tests/compile/fusions_e2e/test_tp2_async_tp.py`
- `tests/csrc`
- `tests/csrc/quantization`
- `tests/vllm`
- `tests/vllm/compilation`
- `tests/vllm/model_executor`
- `tests/vllm/v1`
- `tests/vllm/v1/attention`

**✅ GH200 Test**

- (test paths unknown)

**✅ GPQA Eval (GPT-OSS) (B200)**

- `tests/csrc`
- `tests/evals`
- `tests/evals/gpt_oss`
- `tests/evals/gpt_oss/test_gpqa_correctness.py`
- `tests/vllm`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/layers`
- `tests/vllm/model_executor/layers/quantization`

**✅ GPQA Eval (GPT-OSS) (H100)**

- `tests/csrc`
- `tests/evals`
- `tests/evals/gpt_oss`
- `tests/evals/gpt_oss/test_gpqa_correctness.py`
- `tests/vllm`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/layers`
- `tests/vllm/model_executor/layers/quantization`

**✅ Hybrid SSM NixlConnector PD accuracy tests (4 GPUs)**

- `tests/v1`
- `tests/v1/kv_connector`
- `tests/v1/kv_connector/nixl_integration`
- `tests/vllm`
- `tests/vllm/distributed`
- `tests/vllm/distributed/kv_transfer`
- `tests/vllm/distributed/kv_transfer/kv_connector`
- `tests/vllm/distributed/kv_transfer/kv_connector/v1`
- `tests/vllm/distributed/kv_transfer/kv_connector/v1/nixl_connector.py`

**✅ Intel HPU Test**

- (test paths unknown)

**✅ Kernels Attention Test 1**

- (test paths unknown)

**✅ Kernels Attention Test 2**

- (test paths unknown)

**✅ Kernels Core Operation Test**

- `tests/csrc`
- `tests/kernels`
- `tests/kernels/core`
- `tests/kernels/test_concat_mla_q.py`
- `tests/kernels/test_top_k_per_row.py`
- `tests/vllm`
- `tests/vllm/_aiter_ops.py`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/layers`
- `tests/vllm/model_executor/layers/rotary_embedding`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`

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
- `tests/tools`
- `tests/tools/install_deepgemm.sh`
- `tests/vllm`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/layers`
- `tests/vllm/model_executor/layers/fused_moe`
- `tests/vllm/model_executor/layers/quantization`
- `tests/vllm/utils`
- `tests/vllm/utils/deep_gemm.py`

**✅ Kernels FP8 MoE Test (1 H100)**

- `tests/kernels`
- `tests/kernels/moe`
- `tests/kernels/moe/test_block_int8.py`
- `tests/kernels/moe/test_cutlass_moe.py`
- `tests/kernels/moe/test_flashinfer.py`
- `tests/kernels/moe/test_gpt_oss_triton_kernels.py`
- `tests/kernels/moe/test_modular_oai_triton_moe.py`
- `tests/kernels/moe/test_moe.py`
- `tests/kernels/moe/test_triton_moe_no_act_mul.py`
- `tests/kernels/moe/test_triton_moe_ptpc_fp8.py`

**✅ Kernels FP8 MoE Test (2 H100s)**

- `tests/kernels`
- `tests/kernels/moe`
- `tests/kernels/moe/test_deepep_deepgemm_moe.py`
- `tests/kernels/moe/test_deepep_moe.py`

**✅ Kernels Fp4 MoE Test (B200)**

- `tests/kernels`
- `tests/kernels/moe`
- `tests/kernels/moe/test_cutedsl_moe.py`
- `tests/kernels/moe/test_flashinfer_moe.py`
- `tests/kernels/moe/test_nvfp4_moe.py`
- `tests/kernels/moe/test_ocp_mx_moe.py`

**✅ Kernels FusedMoE Layer Test (2 B200s)**

- `tests/csrc`
- `tests/csrc/moe`
- `tests/csrc/quantization`
- `tests/csrc/quantization/cutlass_w8a8`
- `tests/csrc/quantization/cutlass_w8a8/moe`
- `tests/kernels`
- `tests/kernels/moe`
- `tests/kernels/moe/test_moe_layer.py`
- `tests/vllm`
- `tests/vllm/config`
- `tests/vllm/distributed`
- `tests/vllm/distributed/device_communicators`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/layers`
- `tests/vllm/model_executor/layers/fused_moe`
- `tests/vllm/model_executor/layers/quantization`

**✅ Kernels FusedMoE Layer Test (2 H100s)**

- `tests/csrc`
- `tests/csrc/moe`
- `tests/csrc/quantization`
- `tests/csrc/quantization/cutlass_w8a8`
- `tests/csrc/quantization/cutlass_w8a8/moe`
- `tests/kernels`
- `tests/kernels/moe`
- `tests/kernels/moe/test_moe_layer.py`
- `tests/vllm`
- `tests/vllm/config`
- `tests/vllm/distributed`
- `tests/vllm/distributed/device_communicators`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/layers`
- `tests/vllm/model_executor/layers/fused_moe`
- `tests/vllm/model_executor/layers/quantization`

**✅ Kernels Helion Test**

- `tests/kernels`
- `tests/kernels/helion`
- `tests/vllm`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`
- `tests/vllm/utils`
- `tests/vllm/utils/import_utils.py`

**✅ Kernels KDA Test**

- (test paths unknown)

**✅ Kernels Mamba Test**

- `tests/csrc`
- `tests/csrc/mamba`
- `tests/kernels`
- `tests/kernels/mamba`
- `tests/vllm`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/layers`
- `tests/vllm/model_executor/layers/mamba`
- `tests/vllm/model_executor/layers/mamba/ops`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`

**✅ Kernels MiniMax Reduce RMS Test (2 GPUs)**

- `tests/csrc`
- `tests/csrc/minimax_reduce_rms_kernel.cu`
- `tests/csrc/minimax_reduce_rms_kernel.h`
- `tests/kernels`
- `tests/kernels/core`
- `tests/kernels/core/test_minimax_reduce_rms.py`
- `tests/vllm`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/layers`
- `tests/vllm/model_executor/layers/mamba`
- `tests/vllm/model_executor/layers/mamba/lamport_workspace.py`
- `tests/vllm/model_executor/layers/mamba/linear_attn.py`

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

**✅ LM Eval Large Models (4 GPUs)(H100)**

- `tests/csrc`
- `tests/test_lm_eval_correctness.py`
- `tests/vllm`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/layers`
- `tests/vllm/model_executor/layers/quantization`

**✅ LM Eval Large Models (B200, EP)**

- (test paths unknown)

**✅ LM Eval Large Models (H200)**

- `tests/evals`
- `tests/evals/gsm8k`
- `tests/evals/gsm8k/test_gsm8k_correctness.py`

**✅ LM Eval Qwen3.5 Models (B200)**

- `tests/evals`
- `tests/evals/gsm8k`
- `tests/evals/gsm8k/test_gsm8k_correctness.py`
- `tests/vllm`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/layers`
- `tests/vllm/model_executor/layers/fla`
- `tests/vllm/model_executor/layers/fla/ops`
- `tests/vllm/model_executor/models`
- `tests/vllm/model_executor/models/qwen3_5.py`
- `tests/vllm/model_executor/models/qwen3_5_mtp.py`
- `tests/vllm/model_executor/models/qwen3_next.py`
- `tests/vllm/model_executor/models/qwen3_next_mtp.py`
- `tests/vllm/transformers_utils`
- `tests/vllm/transformers_utils/configs`
- `tests/vllm/transformers_utils/configs/qwen3_5.py`
- `tests/vllm/transformers_utils/configs/qwen3_5_moe.py`

**✅ LM Eval Small Models**

- `tests/csrc`
- `tests/evals`
- `tests/evals/gsm8k`
- `tests/evals/gsm8k/test_gsm8k_correctness.py`
- `tests/vllm`
- `tests/vllm/_aiter_ops.py`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/layers`
- `tests/vllm/model_executor/layers/quantization`
- `tests/vllm/model_executor/model_loader`
- `tests/vllm/model_executor/models`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`
- `tests/vllm/v1`
- `tests/vllm/v1/attention`
- `tests/vllm/v1/attention/backends`
- `tests/vllm/v1/attention/selector.py`

**✅ LM Eval Small Models (B200)**

- `tests/csrc`
- `tests/evals`
- `tests/evals/gsm8k`
- `tests/evals/gsm8k/test_gsm8k_correctness.py`
- `tests/vllm`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/layers`
- `tests/vllm/model_executor/layers/quantization`

**✅ LM Eval TurboQuant KV Cache**

- `tests/evals`
- `tests/evals/gsm8k`
- `tests/evals/gsm8k/test_gsm8k_correctness.py`
- `tests/vllm`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/layers`
- `tests/vllm/model_executor/layers/quantization`
- `tests/vllm/model_executor/layers/quantization/turboquant`
- `tests/vllm/v1`
- `tests/vllm/v1/attention`
- `tests/vllm/v1/attention/backends`
- `tests/vllm/v1/attention/backends/turboquant_attn.py`
- `tests/vllm/v1/attention/ops`
- `tests/vllm/v1/attention/ops/triton_turboquant_decode.py`
- `tests/vllm/v1/attention/ops/triton_turboquant_store.py`

**✅ Language Models Test (Extended Generation)**

- `tests/models`
- `tests/models/language`
- `tests/models/language/generation`
- `tests/vllm`

**✅ Language Models Test (Extended Pooling)**

- `tests/models`
- `tests/models/language`
- `tests/models/language/pooling`
- `tests/vllm`

**✅ Language Models Test (MTEB)**

- `tests/models`
- `tests/models/language`
- `tests/models/language/pooling_mteb_test`
- `tests/vllm`

**✅ Language Models Test (PPL)**

- `tests/models`
- `tests/models/language`
- `tests/models/language/generation_ppl_test`
- `tests/vllm`
- `tests/vllm/_aiter_ops.py`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/layers`
- `tests/vllm/model_executor/layers/fla`
- `tests/vllm/model_executor/layers/fla/ops`
- `tests/vllm/model_executor/models`
- `tests/vllm/model_executor/models/qwen.py`
- `tests/vllm/model_executor/models/qwen2.py`
- `tests/vllm/model_executor/models/qwen3.py`
- `tests/vllm/model_executor/models/qwen3_5.py`
- `tests/vllm/model_executor/models/qwen3_5_mtp.py`
- `tests/vllm/model_executor/models/qwen3_next.py`
- `tests/vllm/model_executor/models/qwen3_next_mtp.py`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`
- `tests/vllm/transformers_utils`
- `tests/vllm/transformers_utils/configs`
- `tests/vllm/transformers_utils/configs/qwen3_5.py`
- `tests/vllm/transformers_utils/configs/qwen3_5_moe.py`
- `tests/vllm/v1`
- `tests/vllm/v1/attention`
- `tests/vllm/v1/attention/backends`
- `tests/vllm/v1/attention/backends/flex_attention.py`
- `tests/vllm/v1/attention/backends/rocm_aiter_fa.py`
- `tests/vllm/v1/attention/backends/rocm_aiter_unified_attn.py`
- `tests/vllm/v1/attention/backends/rocm_attn.py`
- `tests/vllm/v1/attention/backends/triton_attn.py`
- `tests/vllm/v1/attention/ops`

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
- `tests/vllm`

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
- `tests/vllm`
- `tests/vllm/lora`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`

**✅ MRCR Eval Small Models**

- (test paths unknown)

**✅ Metrics, Tracing (2 GPUs)**

- `tests/v1`
- `tests/v1/tracing`
- `tests/vllm`

**✅ MoE Refactor Integration Test (B200 - TEMPORARY)**

- `tests/evals`
- `tests/evals/gsm8k`
- `tests/evals/gsm8k/test_gsm8k_correctness.py`

**✅ MoE Refactor Integration Test (B200 DP - TEMPORARY)**

- `tests/evals`
- `tests/evals/gsm8k`
- `tests/evals/gsm8k/test_gsm8k_correctness.py`

**✅ MoE Refactor Integration Test (H100 - TEMPORARY)**

- `tests/evals`
- `tests/evals/gsm8k`
- `tests/evals/gsm8k/test_gsm8k_correctness.py`

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
- `tests/vllm`
- `tests/vllm/v1`
- `tests/vllm/v1/attention`
- `tests/vllm/v1/core`
- `tests/vllm/v1/core/sched`
- `tests/vllm/v1/worker`
- `tests/vllm/v1/worker/gpu`
- `tests/vllm/v1/worker/gpu_worker.py`

**✅ Model Runner V2 Distributed (2 GPUs)**

- `tests/basic_correctness`
- `tests/basic_correctness/test_basic_correctness.py`
- `tests/v1`
- `tests/v1/distributed`
- `tests/v1/distributed/test_async_llm_dp.py`
- `tests/v1/distributed/test_eagle_dp.py`
- `tests/vllm`
- `tests/vllm/v1`
- `tests/vllm/v1/worker`
- `tests/vllm/v1/worker/gpu`
- `tests/vllm/v1/worker/gpu_worker.py`

**✅ Model Runner V2 Examples**

- `tests/examples`
- `tests/examples/basic`
- `tests/examples/basic/offline_inference`
- `tests/examples/features`
- `tests/examples/generate`
- `tests/examples/generate/multimodal`
- `tests/examples/others`
- `tests/examples/others/tensorize_vllm_model.py`
- `tests/examples/pooling`
- `tests/examples/pooling/embed`
- `tests/examples/pooling/embed/vision_embedding_offline.py`
- `tests/vllm`
- `tests/vllm/v1`
- `tests/vllm/v1/core`
- `tests/vllm/v1/core/sched`
- `tests/vllm/v1/worker`
- `tests/vllm/v1/worker/gpu`
- `tests/vllm/v1/worker/gpu_worker.py`

**✅ Model Runner V2 Pipeline Parallelism (4 GPUs)**

- `tests/distributed`
- `tests/distributed/test_pipeline_parallel.py`
- `tests/distributed/test_pp_cudagraph.py`
- `tests/vllm`
- `tests/vllm/v1`
- `tests/vllm/v1/worker`
- `tests/vllm/v1/worker/gpu`
- `tests/vllm/v1/worker/gpu_worker.py`

**✅ Model Runner V2 Spec Decode**

- `tests/v1`
- `tests/v1/e2e`
- `tests/v1/e2e/spec_decode`
- `tests/v1/e2e/spec_decode/test_spec_decode.py`
- `tests/v1/spec_decode`
- `tests/v1/spec_decode/test_max_len.py`
- `tests/v1/spec_decode/test_probabilistic_rejection_sampler_utils.py`
- `tests/v1/spec_decode/test_synthetic_rejection_sampler_utils.py`
- `tests/vllm`
- `tests/vllm/v1`
- `tests/vllm/v1/worker`
- `tests/vllm/v1/worker/gpu`
- `tests/vllm/v1/worker/gpu_worker.py`

**✅ Multi-Modal Accuracy Eval (Small Models)**

- `tests/test_lm_eval_correctness.py`
- `tests/vllm`
- `tests/vllm/inputs`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/model_loader`
- `tests/vllm/multimodal`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`
- `tests/vllm/v1`
- `tests/vllm/v1/core`

**✅ Multi-Modal Models (Extended Generation 1)**

- `tests/models`
- `tests/models/multimodal`
- `tests/models/multimodal/generation`
- `tests/models/multimodal/test_mapping.py`
- `tests/vllm`

**✅ Multi-Modal Models (Extended Generation 2)**

- `tests/models`
- `tests/models/multimodal`
- `tests/models/multimodal/generation`
- `tests/models/multimodal/generation/test_common.py`
- `tests/vllm`

**✅ Multi-Modal Models (Extended Pooling)**

- `tests/models`
- `tests/models/multimodal`
- `tests/models/multimodal/pooling`
- `tests/vllm`

**✅ Multi-Modal Models (Standard) 1: qwen2**

- `tests/models`
- `tests/models/multimodal`
- `tests/models/multimodal/generation`
- `tests/models/multimodal/generation/test_common.py`
- `tests/models/multimodal/generation/test_ultravox.py`
- `tests/vllm`

**✅ Multi-Modal Models (Standard) 2: qwen3 + gemma**

- `tests/models`
- `tests/models/multimodal`
- `tests/models/multimodal/generation`
- `tests/models/multimodal/generation/test_common.py`
- `tests/models/multimodal/generation/test_qwen2_5_vl.py`
- `tests/models/multimodal/generation/test_vit_cudagraph.py`
- `tests/vllm`

**✅ Multi-Modal Models (Standard) 3: llava + qwen2_vl**

- `tests/models`
- `tests/models/multimodal`
- `tests/models/multimodal/generation`
- `tests/models/multimodal/generation/test_common.py`
- `tests/models/multimodal/generation/test_qwen2_vl.py`
- `tests/models/multimodal/test_mapping.py`
- `tests/vllm`

**✅ Multi-Modal Models (Standard) 4: other + whisper**

- `tests/models`
- `tests/models/multimodal`
- `tests/models/multimodal/generation`
- `tests/models/multimodal/generation/test_memory_leak.py`
- `tests/models/multimodal/generation/test_whisper.py`
- `tests/models/multimodal/test_mapping.py`
- `tests/vllm`

**✅ Multi-Modal Processor**

- `tests/models`
- `tests/models/multimodal`
- `tests/models/multimodal/processing`
- `tests/models/multimodal/processing/test_tensor_schema.py`
- `tests/models/registry.py`
- `tests/vllm`

**✅ Multi-Modal Processor (CPU)**

- `tests/models`
- `tests/models/multimodal`
- `tests/models/multimodal/processing`
- `tests/models/registry.py`
- `tests/vllm`

**✅ MultiConnector (Nixl+Offloading) PD accuracy (2 GPUs)**

- `tests/v1`
- `tests/v1/kv_connector`
- `tests/v1/kv_connector/nixl_integration`
- `tests/vllm`
- `tests/vllm/distributed`
- `tests/vllm/distributed/kv_transfer`
- `tests/vllm/distributed/kv_transfer/kv_connector`
- `tests/vllm/distributed/kv_transfer/kv_connector/v1`
- `tests/vllm/distributed/kv_transfer/kv_connector/v1/multi_connector.py`
- `tests/vllm/distributed/kv_transfer/kv_connector/v1/nixl_connector.py`
- `tests/vllm/distributed/kv_transfer/kv_connector/v1/offloading`
- `tests/vllm/distributed/kv_transfer/kv_connector/v1/offloading_connector.py`

**✅ MultiConnector (Nixl+Offloading) PD edge cases (2 GPUs)**

- `tests/v1`
- `tests/v1/kv_connector`
- `tests/v1/kv_connector/nixl_integration`
- `tests/vllm`
- `tests/vllm/distributed`
- `tests/vllm/distributed/kv_transfer`
- `tests/vllm/distributed/kv_transfer/kv_connector`
- `tests/vllm/distributed/kv_transfer/kv_connector/v1`
- `tests/vllm/distributed/kv_transfer/kv_connector/v1/multi_connector.py`
- `tests/vllm/distributed/kv_transfer/kv_connector/v1/nixl_connector.py`
- `tests/vllm/distributed/kv_transfer/kv_connector/v1/offloading`
- `tests/vllm/distributed/kv_transfer/kv_connector/v1/offloading_connector.py`

**✅ NixlConnector PD + Spec Decode acceptance (2 GPUs)**

- `tests/v1`
- `tests/v1/kv_connector`
- `tests/v1/kv_connector/nixl_integration`
- `tests/vllm`
- `tests/vllm/distributed`
- `tests/vllm/distributed/kv_transfer`
- `tests/vllm/distributed/kv_transfer/kv_connector`
- `tests/vllm/distributed/kv_transfer/kv_connector/v1`
- `tests/vllm/distributed/kv_transfer/kv_connector/v1/nixl_connector.py`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`
- `tests/vllm/v1`
- `tests/vllm/v1/worker`
- `tests/vllm/v1/worker/kv_connector_model_runner_mixin.py`

**✅ OpenAI API Correctness**

- `tests/csrc`
- `tests/entrypoints`
- `tests/entrypoints/openai`
- `tests/entrypoints/openai/correctness`
- `tests/vllm`
- `tests/vllm/entrypoints`
- `tests/vllm/entrypoints/openai`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/models`
- `tests/vllm/model_executor/models/whisper.py`

**✅ Pipeline + Context Parallelism (4 GPUs)**

- `tests/distributed`
- `tests/distributed/test_pipeline_parallel.py`
- `tests/distributed/test_pp_cudagraph.py`
- `tests/vllm`
- `tests/vllm/_aiter_ops.py`
- `tests/vllm/distributed`
- `tests/vllm/engine`
- `tests/vllm/executor`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/layers`
- `tests/vllm/model_executor/models`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`
- `tests/vllm/v1`
- `tests/vllm/v1/attention`
- `tests/vllm/v1/attention/backends`
- `tests/vllm/v1/attention/selector.py`

**✅ Platform Tests (CUDA)**

- `tests/cuda`
- `tests/cuda/test_cuda_context.py`
- `tests/cuda/test_platform_no_cuda_init.py`
- `tests/vllm`

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
- `tests/plugins_tests/test_io_processor_plugins.py`
- `tests/plugins_tests/test_platform_plugins.py`
- `tests/plugins_tests/test_scheduler_plugins.py`
- `tests/plugins_tests/test_stats_logger_plugins.py`
- `tests/plugins_tests/test_terratorch_io_processor_plugins.py`
- `tests/vllm`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`
- `tests/vllm/plugins`

**✅ PyTorch Compilation Passes Unit Tests**

- `tests/compile`
- `tests/compile/passes`
- `tests/vllm`

**✅ PyTorch Compilation Unit Tests**

- `tests/compile`
- `tests/csrc`
- `tests/vllm`
- `tests/vllm/compilation`
- `tests/vllm/config`
- `tests/vllm/config/compilation.py`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/layers`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`
- `tests/vllm/v1`
- `tests/vllm/v1/attention`
- `tests/vllm/v1/cudagraph_dispatcher.py`
- `tests/vllm/v1/worker`

**✅ PyTorch Compilation Unit Tests (H100)**

- `tests/compile`
- `tests/compile/h100`
- `tests/vllm`

**✅ PyTorch Fullgraph**

- `tests/compile`
- `tests/compile/fullgraph`
- `tests/compile/fullgraph/test_full_graph.py`
- `tests/csrc`
- `tests/vllm`
- `tests/vllm/compilation`
- `tests/vllm/config`
- `tests/vllm/config/compilation.py`
- `tests/vllm/model_executor`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`
- `tests/vllm/v1`
- `tests/vllm/v1/attention`

**✅ PyTorch Fullgraph Smoke Test**

- `tests/compile`
- `tests/csrc`
- `tests/vllm`
- `tests/vllm/compilation`
- `tests/vllm/config`
- `tests/vllm/config/compilation.py`
- `tests/vllm/model_executor`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`
- `tests/vllm/v1`
- `tests/vllm/v1/attention`

**✅ Pytorch Nightly Dependency Override Check**

- `tests/requirements`
- `tests/requirements/test`
- `tests/requirements/test/nightly-torch.txt`
- `tests/vllm`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`

**✅ Quantized MoE Test (B200)**

- `tests/quantization`
- `tests/quantization/test_blackwell_moe.py`
- `tests/vllm`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/layers`
- `tests/vllm/model_executor/layers/fused_moe`
- `tests/vllm/model_executor/layers/quantization`
- `tests/vllm/model_executor/layers/quantization/compressed_tensors`
- `tests/vllm/model_executor/layers/quantization/modelopt.py`
- `tests/vllm/model_executor/layers/quantization/mxfp4.py`
- `tests/vllm/model_executor/models`
- `tests/vllm/model_executor/models/deepseek_v2.py`
- `tests/vllm/model_executor/models/gpt_oss.py`
- `tests/vllm/model_executor/models/llama4.py`
- `tests/vllm/v1`
- `tests/vllm/v1/attention`
- `tests/vllm/v1/attention/backends`
- `tests/vllm/v1/attention/backends/flashinfer.py`

**✅ Qwen3-30B-A3B-FP8 DP4 Async EPLB Accuracy**

- (test paths unknown)

**✅ Qwen3-30B-A3B-FP8-block Accuracy**

- (test paths unknown)

**✅ Qwen3-30B-A3B-FP8-block Accuracy (B200)**

- (test paths unknown)

**✅ Ray Dependency Compatibility Check**

- `tests/requirements`
- `tests/setup.py`
- `tests/vllm`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`

**✅ RayExecutorV2 (4 GPUs)**

- `tests/basic_correctness`
- `tests/basic_correctness/test_basic_correctness.py`
- `tests/distributed`
- `tests/distributed/test_pipeline_parallel.py`
- `tests/distributed/test_ray_v2_executor.py`
- `tests/distributed/test_ray_v2_executor_e2e.py`
- `tests/vllm`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`
- `tests/vllm/v1`
- `tests/vllm/v1/executor`
- `tests/vllm/v1/executor/abstract.py`
- `tests/vllm/v1/executor/multiproc_executor.py`
- `tests/vllm/v1/executor/ray_executor_v2.py`

**✅ Regression**

- `tests/test_regression`
- `tests/test_regression.py`
- `tests/vllm`

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

- `tests/conftest.py`
- `tests/samplers`
- `tests/vllm`
- `tests/vllm/_aiter_ops.py`
- `tests/vllm/beam_search.py`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/layers`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`
- `tests/vllm/sampling_metadata.py`
- `tests/vllm/v1`
- `tests/vllm/v1/sample`

**✅ Sequence Parallel Correctness Tests (2 GPUs)**

- `tests/compile`
- `tests/compile/correctness_e2e`
- `tests/compile/correctness_e2e/test_sequence_parallel.py`
- `tests/vllm`
- `tests/vllm/compilation`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/layers`
- `tests/vllm/v1`
- `tests/vllm/v1/cudagraph_dispatcher.py`
- `tests/vllm/v1/worker`

**✅ Sequence Parallel Correctness Tests (2xH100)**

- `tests/compile`
- `tests/compile/correctness_e2e`
- `tests/compile/correctness_e2e/test_sequence_parallel.py`

**✅ Spec Decode Eagle**

- `tests/v1`
- `tests/v1/e2e`
- `tests/v1/e2e/spec_decode`
- `tests/vllm`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/layers`
- `tests/vllm/model_executor/model_loader`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`
- `tests/vllm/v1`
- `tests/vllm/v1/sample`
- `tests/vllm/v1/spec_decode`
- `tests/vllm/v1/worker`
- `tests/vllm/v1/worker/gpu`
- `tests/vllm/v1/worker/gpu/spec_decode`

**✅ Spec Decode Eagle Nightly B200**

- `tests/v1`
- `tests/v1/e2e`
- `tests/v1/e2e/spec_decode`
- `tests/vllm`
- `tests/vllm/v1`
- `tests/vllm/v1/spec_decode`
- `tests/vllm/v1/worker`
- `tests/vllm/v1/worker/gpu`
- `tests/vllm/v1/worker/gpu/spec_decode`

**✅ Spec Decode MTP hybrid (B200)**

- (test paths unknown)

**✅ Spec Decode Ngram + Suffix**

- `tests/v1`
- `tests/v1/e2e`
- `tests/v1/e2e/spec_decode`
- `tests/vllm`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/layers`
- `tests/vllm/model_executor/model_loader`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`
- `tests/vllm/v1`
- `tests/vllm/v1/sample`
- `tests/vllm/v1/spec_decode`
- `tests/vllm/v1/worker`
- `tests/vllm/v1/worker/gpu`
- `tests/vllm/v1/worker/gpu/spec_decode`

**✅ Spec Decode Speculators + MTP**

- `tests/v1`
- `tests/v1/e2e`
- `tests/v1/e2e/spec_decode`
- `tests/vllm`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/layers`
- `tests/vllm/model_executor/model_loader`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`
- `tests/vllm/transformers_utils`
- `tests/vllm/transformers_utils/configs`
- `tests/vllm/transformers_utils/configs/speculators`
- `tests/vllm/v1`
- `tests/vllm/v1/sample`
- `tests/vllm/v1/spec_decode`
- `tests/vllm/v1/worker`
- `tests/vllm/v1/worker/gpu`
- `tests/vllm/v1/worker/gpu/spec_decode`

**✅ Spec Decode Speculators + MTP Nightly B200**

- `tests/v1`
- `tests/v1/e2e`
- `tests/v1/e2e/spec_decode`
- `tests/vllm`
- `tests/vllm/transformers_utils`
- `tests/vllm/transformers_utils/configs`
- `tests/vllm/transformers_utils/configs/speculators`
- `tests/vllm/v1`
- `tests/vllm/v1/spec_decode`
- `tests/vllm/v1/worker`
- `tests/vllm/v1/worker/gpu`
- `tests/vllm/v1/worker/gpu/spec_decode`

**✅ Speculators Correctness**

- (test paths unknown)

**✅ Torch Nightly Basic Models Tests (Initialization)**

- (test paths unknown)

**✅ Torch Nightly Language Models Tests (Extra Standard) 1**

- (test paths unknown)

**✅ Torch Nightly Language Models Tests (Extra Standard) 2**

- (test paths unknown)

**✅ Torch Nightly Language Models Tests (Hybrid) 1**

- (test paths unknown)

**✅ Torch Nightly Language Models Tests (Hybrid) 2**

- (test paths unknown)

**✅ Torch Nightly Language Models Tests (Standard)**

- (test paths unknown)

**✅ V1 Core + KV + Metrics**

- `tests/entrypoints`
- `tests/entrypoints/openai`
- `tests/entrypoints/openai/correctness`
- `tests/entrypoints/openai/correctness/test_lmeval.py`
- `tests/entrypoints/openai/correctness/test_lmeval.py::test_lm_eval_accuracy_v1_engine`
- `tests/v1`
- `tests/v1/core`
- `tests/v1/executor`
- `tests/v1/executor'`
- `tests/v1/kv_connector`
- `tests/v1/kv_connector/unit`
- `tests/v1/kv_offload`
- `tests/v1/metrics`
- `tests/v1/worker`
- `tests/vllm`

**✅ V1 Others (CPU)**

- `tests/v1`
- `tests/v1/structured_output`
- `tests/v1/test_serial_utils.py`
- `tests/vllm`

**✅ V1 Sample + Logits**

- `tests/v1`
- `tests/v1/logits_processors`
- `tests/v1/sample`
- `tests/v1/test_oracle.py`
- `tests/v1/test_outputs.py`
- `tests/v1/test_request.py`
- `tests/vllm`

**✅ V1 attention (B200)**

- `tests/v1`
- `tests/v1/attention`
- `tests/vllm`
- `tests/vllm/config`
- `tests/vllm/config/attention.py`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/layers`
- `tests/vllm/model_executor/layers/attention`
- `tests/vllm/v1`
- `tests/vllm/v1/attention`

**✅ V1 attention (H100)**

- `tests/v1`
- `tests/v1/attention`
- `tests/vllm`
- `tests/vllm/config`
- `tests/vllm/config/attention.py`
- `tests/vllm/model_executor`
- `tests/vllm/model_executor/layers`
- `tests/vllm/model_executor/layers/attention`
- `tests/vllm/v1`
- `tests/vllm/v1/attention`

**✅ V1 e2e (2 GPUs)**

- `tests/v1`
- `tests/v1/e2e`
- `tests/v1/e2e/spec_decode`
- `tests/v1/e2e/spec_decode/test_spec_decode.py`
- `tests/vllm`

**✅ V1 e2e (4 GPUs)**

- `tests/v1`
- `tests/v1/e2e`
- `tests/v1/e2e/spec_decode`
- `tests/v1/e2e/spec_decode/test_spec_decode.py`
- `tests/vllm`

**✅ V1 e2e (4xH100)**

- `tests/v1`
- `tests/v1/e2e`
- `tests/v1/e2e/test_hybrid_chunked_prefill.py`
- `tests/vllm`
- `tests/vllm/v1`
- `tests/vllm/v1/attention`
- `tests/vllm/v1/attention/backends`
- `tests/vllm/v1/attention/backends/utils.py`
- `tests/vllm/v1/worker`
- `tests/vllm/v1/worker/gpu_model_runner.py`

**✅ Weight Loading Multiple GPU**

- `tests/vllm`
- `tests/weight_loading`

**✅ bootstrap**

- (test paths unknown)

**✅ bootstrap**

- (test paths unknown)

**✅ e2e Core (1 GPU)**

- `tests/v1`
- `tests/v1/e2e`
- `tests/v1/e2e/general`
- `tests/vllm`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`
- `tests/vllm/v1`

**✅ e2e Scheduling (1 GPU)**

- `tests/v1`
- `tests/v1/e2e`
- `tests/v1/e2e/general`
- `tests/v1/e2e/general/test_async_scheduling.py`
- `tests/vllm`
- `tests/vllm/platforms`
- `tests/vllm/platforms/rocm.py`
- `tests/vllm/v1`

**✅ vLLM IR Tests**

- `tests/ir`
- `tests/kernels`
- `tests/kernels/ir`
- `tests/kernels/ir'`
- `tests/vllm`
- `tests/vllm/ir`
- `tests/vllm/kernels`

## LLM Selections — 1 target(s)

### ➖ `tests/tool_parsers/test_glm4_moe_tool_parser.py`

**Reason:** directly tests the refactored method and FunctionTool support

**Jobs (1):**

- 🔧 Async Engine, Inputs, Utils, Worker, Config (CPU)

## Gap Analysis

**Why the LLM missed:**
- LLM selections covered `tool_parsers` but failures occurred in `.buildkite`, `[job] :docker: Build XPU image`, `[job] Kernels Quantization Test 1`, `[job] Kernels Quantization Test 2`, `[job] Torch Nightly Basic Models Tests (Extra Initialization) 1`, `[job] Torch Nightly Basic Models Tests (Extra Initialization) 2`, `[job] XPU server test`, `basic_correctness`, `compile`, `csrc`, `distributed`, `entrypoints`, `examples`, `kernels`, `models`, `quantization`, `setup.py`, `standalone_tests`, `v1`, `vllm`
- `tests/models` (job: Multi-Modal Models (Extended Generation 3)) was not covered by any selection
- `tests/models/multimodal` (job: Multi-Modal Models (Extended Generation 3)) was not covered by any selection
- `tests/models/multimodal/generation` (job: Multi-Modal Models (Extended Generation 3)) was not covered by any selection
- `tests/models/multimodal/generation/test_common.py` (job: Multi-Modal Models (Extended Generation 3)) was not covered by any selection
- `tests/vllm` (job: Multi-Modal Models (Extended Generation 3)) was not covered by any selection
- `[job] Kernels Quantization Test 2` (job: Kernels Quantization Test 2) was not covered by any selection
- `tests/basic_correctness` (job: Ascend NPU Test) was not covered by any selection
- `[job] XPU server test` (job: XPU server test) was not covered by any selection
- `tests/v1` (job: Spec Decode Draft Model Nightly B200) was not covered by any selection
- `tests/v1/e2e` (job: Spec Decode Draft Model Nightly B200) was not covered by any selection
- `tests/v1/e2e/spec_decode` (job: Spec Decode Draft Model Nightly B200) was not covered by any selection
- `tests/vllm/v1` (job: Spec Decode Draft Model Nightly B200) was not covered by any selection
- `tests/vllm/v1/spec_decode` (job: Spec Decode Draft Model Nightly B200) was not covered by any selection
- `tests/vllm/v1/worker` (job: Spec Decode Draft Model Nightly B200) was not covered by any selection
- `tests/vllm/v1/worker/gpu` (job: Spec Decode Draft Model Nightly B200) was not covered by any selection
- `tests/vllm/v1/worker/gpu/spec_decode` (job: Spec Decode Draft Model Nightly B200) was not covered by any selection
- `tests/models/quantization` (job: Quantized Models Test) was not covered by any selection
- `tests/vllm/_aiter_ops.py` (job: Quantized Models Test) was not covered by any selection
- `tests/vllm/model_executor` (job: Quantized Models Test) was not covered by any selection
- `tests/vllm/model_executor/layers` (job: Quantized Models Test) was not covered by any selection
- `tests/vllm/model_executor/layers/quantization` (job: Quantized Models Test) was not covered by any selection
- `tests/vllm/model_executor/model_loader` (job: Quantized Models Test) was not covered by any selection
- `tests/vllm/platforms` (job: Quantized Models Test) was not covered by any selection
- `tests/vllm/platforms/rocm.py` (job: Quantized Models Test) was not covered by any selection
- `tests/csrc` (job: Quantization) was not covered by any selection
- `tests/quantization` (job: Quantization) was not covered by any selection
- `[job] Kernels Quantization Test 1` (job: Kernels Quantization Test 1) was not covered by any selection
- `tests/csrc/attention` (job: Kernels (B200)) was not covered by any selection
- `tests/csrc/attention/mla` (job: Kernels (B200)) was not covered by any selection
- `tests/csrc/quantization` (job: Kernels (B200)) was not covered by any selection
- `tests/csrc/quantization/cutlass_w8a8` (job: Kernels (B200)) was not covered by any selection
- `tests/csrc/quantization/cutlass_w8a8/moe` (job: Kernels (B200)) was not covered by any selection
- `tests/csrc/quantization/fp4` (job: Kernels (B200)) was not covered by any selection
- `tests/kernels` (job: Kernels (B200)) was not covered by any selection
- `tests/kernels/attention` (job: Kernels (B200)) was not covered by any selection
- `tests/kernels/attention/test_attention_selector.py` (job: Kernels (B200)) was not covered by any selection
- `tests/kernels/attention/test_cutlass_mla_decode.py` (job: Kernels (B200)) was not covered by any selection
- `tests/kernels/attention/test_flashinfer.py` (job: Kernels (B200)) was not covered by any selection
- `tests/kernels/attention/test_flashinfer_mla_decode.py` (job: Kernels (B200)) was not covered by any selection
- `tests/kernels/attention/test_flashinfer_trtllm_attention.py` (job: Kernels (B200)) was not covered by any selection
- `tests/kernels/moe` (job: Kernels (B200)) was not covered by any selection
- `tests/kernels/moe/test_cutedsl_moe.py` (job: Kernels (B200)) was not covered by any selection
- `tests/kernels/moe/test_flashinfer.py` (job: Kernels (B200)) was not covered by any selection
- `tests/kernels/moe/test_flashinfer_moe.py` (job: Kernels (B200)) was not covered by any selection
- `tests/kernels/moe/test_mxfp4_moe.py` (job: Kernels (B200)) was not covered by any selection
- `tests/kernels/moe/test_nvfp4_moe.py` (job: Kernels (B200)) was not covered by any selection
- `tests/kernels/moe/test_ocp_mx_moe.py` (job: Kernels (B200)) was not covered by any selection
- `tests/kernels/quantization` (job: Kernels (B200)) was not covered by any selection
- `tests/kernels/quantization/test_cutlass_scaled_mm.py` (job: Kernels (B200)) was not covered by any selection
- `tests/kernels/quantization/test_flashinfer_nvfp4_scaled_mm.py` (job: Kernels (B200)) was not covered by any selection
- `tests/kernels/quantization/test_flashinfer_scaled_mm.py` (job: Kernels (B200)) was not covered by any selection
- `tests/kernels/quantization/test_mxfp4_qutlass.py` (job: Kernels (B200)) was not covered by any selection
- `tests/kernels/quantization/test_nvfp4_quant.py` (job: Kernels (B200)) was not covered by any selection
- `tests/kernels/quantization/test_nvfp4_qutlass.py` (job: Kernels (B200)) was not covered by any selection
- `tests/kernels/quantization/test_nvfp4_scaled_mm.py` (job: Kernels (B200)) was not covered by any selection
- `tests/kernels/quantization/test_silu_mul_nvfp4_quant.py` (job: Kernels (B200)) was not covered by any selection
- `tests/kernels/test_top_k_per_row.py` (job: Kernels (B200)) was not covered by any selection
- `tests/models/quantization/test_nvfp4.py` (job: Kernels (B200)) was not covered by any selection
- `tests/vllm/model_executor/layers/fused_moe` (job: Kernels (B200)) was not covered by any selection
- `tests/vllm/model_executor/layers/fused_moe/cutlass_moe.py` (job: Kernels (B200)) was not covered by any selection
- `tests/vllm/model_executor/layers/fused_moe/flashinfer_a2a_prepare_finalize.py` (job: Kernels (B200)) was not covered by any selection
- `tests/vllm/model_executor/layers/fused_moe/flashinfer_cutlass_moe.py` (job: Kernels (B200)) was not covered by any selection
- `tests/vllm/model_executor/layers/quantization/utils` (job: Kernels (B200)) was not covered by any selection
- `tests/vllm/model_executor/layers/quantization/utils/flashinfer_utils.py` (job: Kernels (B200)) was not covered by any selection
- `tests/vllm/platforms/cuda.py` (job: Kernels (B200)) was not covered by any selection
- `tests/vllm/v1/attention` (job: Kernels (B200)) was not covered by any selection
- `tests/vllm/v1/attention/backends` (job: Kernels (B200)) was not covered by any selection
- `tests/vllm/v1/attention/backends/flashinfer.py` (job: Kernels (B200)) was not covered by any selection
- `tests/vllm/v1/attention/backends/mla` (job: Kernels (B200)) was not covered by any selection
- `tests/vllm/v1/attention/backends/mla/cutlass_mla.py` (job: Kernels (B200)) was not covered by any selection
- `tests/vllm/v1/attention/backends/mla/flashinfer_mla.py` (job: Kernels (B200)) was not covered by any selection
- `tests/vllm/v1/attention/selector.py` (job: Kernels (B200)) was not covered by any selection
- `tests/v1/spec_decode` (job: V1 Spec Decode) was not covered by any selection
- `tests/models/multimodal/processing` (job: Transformers Backward Compatibility Models Test) was not covered by any selection
- `tests/models/multimodal/test_mapping.py` (job: Transformers Backward Compatibility Models Test) was not covered by any selection
- `tests/models/test_initialization.py` (job: Transformers Backward Compatibility Models Test) was not covered by any selection
- `tests/models/test_transformers.py` (job: Transformers Backward Compatibility Models Test) was not covered by any selection
- `tests/.buildkite` (job: XPU V1 test) was not covered by any selection
- `tests/.buildkite/intel_jobs` (job: XPU V1 test) was not covered by any selection
- `tests/.buildkite/intel_jobs/test-intel.yaml` (job: XPU V1 test) was not covered by any selection
- `tests/v1/core` (job: XPU V1 test) was not covered by any selection
- `tests/vllm/v1/sample` (job: Spec Decode Draft Model) was not covered by any selection
- `tests/distributed` (job: Distributed Torchrun + Examples (4 GPUs)) was not covered by any selection
- `tests/distributed/test_torchrun_example.py` (job: Distributed Torchrun + Examples (4 GPUs)) was not covered by any selection
- `tests/distributed/test_torchrun_example_moe.py` (job: Distributed Torchrun + Examples (4 GPUs)) was not covered by any selection
- `tests/examples` (job: Distributed Torchrun + Examples (4 GPUs)) was not covered by any selection
- `tests/examples/features` (job: Distributed Torchrun + Examples (4 GPUs)) was not covered by any selection
- `tests/examples/features/data_parallel` (job: Distributed Torchrun + Examples (4 GPUs)) was not covered by any selection
- `tests/examples/features/data_parallel/data_parallel_offline.py` (job: Distributed Torchrun + Examples (4 GPUs)) was not covered by any selection
- `tests/examples/rl` (job: Distributed Torchrun + Examples (4 GPUs)) was not covered by any selection
- `tests/vllm/distributed` (job: Distributed Torchrun + Examples (4 GPUs)) was not covered by any selection
- `tests/entrypoints` (job: V1 Core + KV + Metrics) was not covered by any selection
- `tests/entrypoints/openai` (job: V1 Core + KV + Metrics) was not covered by any selection
- `tests/entrypoints/openai/correctness` (job: V1 Core + KV + Metrics) was not covered by any selection
- `tests/entrypoints/openai/correctness/test_lmeval.py` (job: V1 Core + KV + Metrics) was not covered by any selection
- `tests/entrypoints/openai/correctness/test_lmeval.py::test_lm_eval_accuracy_v1_engine` (job: V1 Core + KV + Metrics) was not covered by any selection
- `tests/v1/executor` (job: V1 Core + KV + Metrics) was not covered by any selection
- `tests/v1/executor'` (job: V1 Core + KV + Metrics) was not covered by any selection
- `tests/v1/kv_connector` (job: V1 Core + KV + Metrics) was not covered by any selection
- `tests/v1/kv_connector/unit` (job: V1 Core + KV + Metrics) was not covered by any selection
- `tests/v1/kv_offload` (job: V1 Core + KV + Metrics) was not covered by any selection
- `tests/v1/metrics` (job: V1 Core + KV + Metrics) was not covered by any selection
- `tests/v1/worker` (job: V1 Core + KV + Metrics) was not covered by any selection
- `tests/v1/logits_processors` (job: V1 Sample + Logits) was not covered by any selection
- `tests/v1/sample` (job: V1 Sample + Logits) was not covered by any selection
- `tests/v1/test_oracle.py` (job: V1 Sample + Logits) was not covered by any selection
- `tests/v1/test_outputs.py` (job: V1 Sample + Logits) was not covered by any selection
- `tests/v1/test_request.py` (job: V1 Sample + Logits) was not covered by any selection
- `[job] :docker: Build XPU image` (job: :docker: Build XPU image) was not covered by any selection
- `tests/compile` (job: Fusion and Compile Unit Tests (2xB200)) was not covered by any selection
- `tests/compile/fullgraph` (job: Fusion and Compile Unit Tests (2xB200)) was not covered by any selection
- `tests/compile/fullgraph/test_full_graph.py` (job: Fusion and Compile Unit Tests (2xB200)) was not covered by any selection
- `tests/compile/fullgraph/test_full_graph.py::test_fp8_kv_scale_compile` (job: Fusion and Compile Unit Tests (2xB200)) was not covered by any selection
- `tests/compile/passes` (job: Fusion and Compile Unit Tests (2xB200)) was not covered by any selection
- `tests/compile/passes/distributed` (job: Fusion and Compile Unit Tests (2xB200)) was not covered by any selection
- `tests/compile/passes/distributed/test_fusion_all_reduce.py` (job: Fusion and Compile Unit Tests (2xB200)) was not covered by any selection
- `tests/compile/passes/test_fusion_attn.py` (job: Fusion and Compile Unit Tests (2xB200)) was not covered by any selection
- `tests/compile/passes/test_mla_attn_quant_fusion.py` (job: Fusion and Compile Unit Tests (2xB200)) was not covered by any selection
- `tests/compile/passes/test_silu_mul_quant_fusion.py` (job: Fusion and Compile Unit Tests (2xB200)) was not covered by any selection
- `tests/vllm/compilation` (job: Fusion and Compile Unit Tests (2xB200)) was not covered by any selection
- `tests/vllm/model_executor/layers/activation.py` (job: Fusion and Compile Unit Tests (2xB200)) was not covered by any selection
- `tests/vllm/model_executor/layers/attention` (job: Fusion and Compile Unit Tests (2xB200)) was not covered by any selection
- `tests/vllm/model_executor/layers/attention/attention.py` (job: Fusion and Compile Unit Tests (2xB200)) was not covered by any selection
- `tests/vllm/model_executor/layers/layernorm.py` (job: Fusion and Compile Unit Tests (2xB200)) was not covered by any selection
- `[job] Torch Nightly Basic Models Tests (Extra Initialization) 1` (job: Torch Nightly Basic Models Tests (Extra Initialization) 1) was not covered by any selection
- `[job] Torch Nightly Basic Models Tests (Extra Initialization) 2` (job: Torch Nightly Basic Models Tests (Extra Initialization) 2) was not covered by any selection
- `tests/setup.py` (job: Python-only Installation) was not covered by any selection
- `tests/standalone_tests` (job: Python-only Installation) was not covered by any selection
- `tests/standalone_tests/python_only_compile.sh` (job: Python-only Installation) was not covered by any selection

**To improve coverage:**
- Add `tests/.buildkite/` (or relevant sub-paths) to selections when related code changes
- Add `tests/[job] :docker: Build XPU image/` (or relevant sub-paths) to selections when related code changes
- Add `tests/[job] Kernels Quantization Test 1/` (or relevant sub-paths) to selections when related code changes
- Add `tests/[job] Kernels Quantization Test 2/` (or relevant sub-paths) to selections when related code changes
- Add `tests/[job] Torch Nightly Basic Models Tests (Extra Initialization) 1/` (or relevant sub-paths) to selections when related code changes
- Add `tests/[job] Torch Nightly Basic Models Tests (Extra Initialization) 2/` (or relevant sub-paths) to selections when related code changes
- Add `tests/[job] XPU server test/` (or relevant sub-paths) to selections when related code changes
- Add `tests/basic_correctness/` (or relevant sub-paths) to selections when related code changes
- Add `tests/compile/` (or relevant sub-paths) to selections when related code changes
- Add `tests/csrc/` (or relevant sub-paths) to selections when related code changes
- Add `tests/distributed/` (or relevant sub-paths) to selections when related code changes
- Add `tests/entrypoints/` (or relevant sub-paths) to selections when related code changes
- Add `tests/examples/` (or relevant sub-paths) to selections when related code changes
- Add `tests/kernels/` (or relevant sub-paths) to selections when related code changes
- Add `tests/models/` (or relevant sub-paths) to selections when related code changes
- Add `tests/quantization/` (or relevant sub-paths) to selections when related code changes
- Add `tests/setup.py/` (or relevant sub-paths) to selections when related code changes
- Add `tests/standalone_tests/` (or relevant sub-paths) to selections when related code changes
- Add `tests/v1/` (or relevant sub-paths) to selections when related code changes
- Add `tests/vllm/` (or relevant sub-paths) to selections when related code changes

---
*Generated: 2026-06-30 06:36 UTC*
