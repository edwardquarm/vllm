#!/usr/bin/env python3
"""
Second Pass Agent — reviews an initial test selection against historical
failure patterns and outputs any additions.

Usage:
    python second_pass.py \
        --changed-files "vllm/engine/core.py\nvllm/v1/core/scheduler.py" \
        --initial-selection "tests/v1/core/ | v1 core changes\ntests/basic_correctness/ | fallback" \
        --patterns-file .buildkite/test_selection_skills/failure_patterns.json \
        --instructions .buildkite/SECOND_PASS.md
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path


MIN_FAILURE_COUNT = 2  # ignore one-off flukes


def normalize_source_area(filepath: str) -> str | None:
    """Map a changed file to its coarse source area key (matches generate_failure_patterns.py)."""
    f = filepath.strip().lstrip("/")
    if f.startswith("vllm/"):
        parts = f.split("/")
        if len(parts) >= 3 and parts[1] == "v1":
            return f"vllm/v1/{parts[2]}/"
        if len(parts) >= 2:
            return f"vllm/{parts[1]}/"
    if f.startswith("csrc/"):
        parts = f.split("/")
        return f"csrc/{parts[1]}/" if len(parts) >= 2 else "csrc/"
    if f in ("CMakeLists.txt", "setup.py", "pyproject.toml"):
        return f
    if f.startswith("requirements"):
        return "requirements/"
    return None


def is_hardware_only_job(job_name: str) -> bool:
    """Jobs that have no pytest path — structurally uncoverable."""
    hardware_markers = ["AMD:", "Ascend", "Intel GPU", "XPU", "ROCm", "HPU", "Neuron"]
    return any(m.lower() in job_name.lower() for m in hardware_markers)


def initial_selection_covers(test_path: str, initial_lines: list[str]) -> bool:
    """Check if the initial selection already covers this test path."""
    tp = test_path.rstrip("/")
    for line in initial_lines:
        selected = line.split("|")[0].strip().rstrip("/")
        if selected == tp or tp.startswith(selected) or selected.startswith(tp):
            return True
    return False


def build_patterns_context(
    changed_files: list[str],
    initial_lines: list[str],
    patterns: dict,
) -> str:
    """
    Build a compact context block showing which historical failures are
    NOT yet covered by the initial selection.
    """
    seen_areas: set[str] = set()
    blocks: list[str] = []

    for f in changed_files:
        area = normalize_source_area(f)
        if not area or area in seen_areas:
            continue
        seen_areas.add(area)

        area_data = patterns.get("by_source_area", {}).get(area)
        if not area_data:
            continue

        frequent_jobs = [
            j for j in area_data.get("frequently_failing_jobs", [])
            if j["failure_count"] >= MIN_FAILURE_COUNT
            and not is_hardware_only_job(j["job"])
        ]
        frequent_tests = [
            t for t in area_data.get("frequently_failing_tests", [])
            if t["failure_count"] >= MIN_FAILURE_COUNT
            and not initial_selection_covers(t["test_path"], initial_lines)
        ]

        if not frequent_jobs and not frequent_tests:
            continue

        block = [f"### {area}  ({area_data['total_prs_with_failures']} PRs with failures)"]

        if frequent_jobs:
            block.append("Frequently failing jobs:")
            for j in frequent_jobs[:5]:
                covered = "✓ covered" if initial_selection_covers(
                    j["job"], initial_lines) else "✗ NOT covered"
                block.append(f"  - {j['job']} ({j['failure_count']}x)  [{covered}]")

        if frequent_tests:
            block.append("Frequently failing test paths NOT in initial selection:")
            for t in frequent_tests[:5]:
                block.append(f"  - {t['test_path']} ({t['failure_count']}x)")

        blocks.append("\n".join(block))

    return "\n\n".join(blocks) if blocks else "No historical patterns found for changed areas."


def run_second_pass(
    changed_files: list[str],
    initial_selection: str,
    patterns: dict,
    instructions: str,
    model: str = "haiku",
) -> str:
    initial_lines = [
        l.strip() for l in initial_selection.splitlines()
        if l.strip() and "|" in l
    ]

    patterns_context = build_patterns_context(changed_files, initial_lines, patterns)

    prompt = f"""{instructions}

---

## Initial Selection (already chosen by primary selector)

{initial_selection if initial_selection.strip() else "NONE — primary selector chose nothing"}

---

## Changed Source Areas and Historical Failure Patterns

{patterns_context}

---

Now output any additions to the initial selection, or NONE if it is already complete.
"""

    result = subprocess.run(
        ["claude", "-p", prompt,
         "--model", model,
         "--allowedTools", "",
         "--output-format", "text"],
        capture_output=True, text=True
    )

    if result.returncode != 0:
        print(f"[second-pass] Claude error: {result.stderr.strip()}", file=sys.stderr)
        return ""

    return result.stdout.strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--changed-files",     required=True,  help="Newline-separated changed file paths")
    parser.add_argument("--initial-selection", required=True,  help="Initial 'path | reason' lines from primary selector")
    parser.add_argument("--patterns-file",     required=True,  type=Path)
    parser.add_argument("--instructions",      required=True,  type=Path)
    parser.add_argument("--model",             default="haiku")
    args = parser.parse_args()

    if not args.patterns_file.exists():
        print(f"[second-pass] patterns file not found: {args.patterns_file}", file=sys.stderr)
        sys.exit(0)  # non-fatal — skip second pass gracefully

    patterns     = json.loads(args.patterns_file.read_text())
    instructions = args.instructions.read_text()
    changed_files = [f for f in args.changed_files.splitlines() if f.strip()]

    additions = run_second_pass(
        changed_files=changed_files,
        initial_selection=args.initial_selection,
        patterns=patterns,
        instructions=instructions,
        model=args.model,
    )

    # Print additions to stdout so the caller can merge them
    print(additions)


if __name__ == "__main__":
    main()
