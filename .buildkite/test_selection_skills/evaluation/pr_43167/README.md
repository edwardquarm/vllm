# PR #43167 - Test Selection Evaluation

## Overview
This directory contains the complete evaluation of LLM-based test selection for PR #43167, comparing what the LLM selected versus what actually failed in Buildkite CI.

**Key Result:** 0% coverage - LLM selected quantization tests, but actual failures were in API integration layer.

## Files in This Directory

### 📊 Quick Start
- **`SUMMARY.md`** - Executive summary with key metrics and insights ⭐ **START HERE**
- **`test_comparison_table.txt`** - Visual side-by-side comparison of LLM vs CI

### 📋 Detailed Analysis  
- **`pr_43167_actual_failures.md`** - Comprehensive failure breakdown with root cause analysis
- **`complete_test_list.txt`** - All 141 failed tests (1 tokenizer + 140 entrypoints)
- **`evaluation_report.json`** - Machine-readable evaluation metrics

### 📈 Legacy Files
- `evaluation_summary.md` - Original summary (before actual test extraction)
- `PR43167_Comparison.xlsx` - Excel export (before actual test extraction)

## Key Findings

### What Failed (141 tests)
1. **Tokenizer Integration** (1 test)
   - `tests/tokenizers_/test_mistral.py`

2. **API Entrypoints** (140 tests)
   - All in `tests/entrypoints/openai/chat_completion/`
   - Affecting: chat, vision, audio, video, function calling, etc.

### What LLM Selected (7 targets, all passed)
- `tests/model_executor/test_eagle_quantization.py`
- `tests/model_executor/test_weight_utils.py`
- `tests/quantization/*` (4 files)
- `tests/basic_correctness/`

### The Gap
```
Internal API Refactoring
        ↓
LLM Selected: Low-level tests (quantization) ✓
        ↓
What Actually Broke: High-level integration (API endpoints) ❌
```

## Data Quality

✅ **HIGH QUALITY** - Extracted from actual Buildkite build logs
- Source: Buildkite API, Build 70063
- Method: Parsed pytest output from job logs
- Result: 141 concrete test names with full pytest paths

This is NOT inferred from pipeline YAML configs - these are the actual tests that ran and failed.

## Metrics

| Metric | Value |
|--------|-------|
| Coverage (Recall) | 0.0% |
| Precision | 0.0% |
| True Positives | 0 |
| False Negatives | 141 |
| False Positives | 7 |

## Key Lesson

**Internal API refactoring requires testing the entire call stack.**

When you change how models are initialized (even just "removing boilerplate"), you need to test:
- ✅ Direct callers (quantization tests) - LLM got this
- ❌ Integration layer (API entrypoints) - LLM missed this
- ❌ Indirect dependencies (tokenizers) - LLM missed this

## Questions?

See `SUMMARY.md` for a quick overview, or `pr_43167_actual_failures.md` for detailed analysis.

---
Generated: 2026-06-09
Data Source: Buildkite API Build 70063
