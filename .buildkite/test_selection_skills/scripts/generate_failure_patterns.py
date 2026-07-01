#!/usr/bin/env python3
"""
Generate failure_patterns.json from historical evaluation data.

For each source area (top-level vllm/ directory or key file), records which
CI jobs historically failed when that area was changed. The critic agent
uses this as a lookup table when reviewing test selections.

Usage:
    python generate_failure_patterns.py [--eval-dir <dir>] [--replay-dir <dir>] [--output <file>]
"""

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path


def normalize_source_area(filepath: str) -> str | None:
    """Map a changed file path to a coarse source area key."""
    f = filepath.lstrip("/")

    # vllm source — group by top 2 levels (e.g. vllm/attention, vllm/v1/core)
    if f.startswith("vllm/"):
        parts = f.split("/")
        if len(parts) >= 3 and parts[1] == "v1":
            return f"vllm/v1/{parts[2]}/"   # vllm/v1/core/, vllm/v1/engine/, ...
        if len(parts) >= 2:
            return f"vllm/{parts[1]}/"       # vllm/attention/, vllm/engine/, ...

    # C/CUDA source
    if f.startswith("csrc/"):
        parts = f.split("/")
        return f"csrc/{parts[1]}/" if len(parts) >= 2 else "csrc/"

    # Build / packaging
    if f in ("CMakeLists.txt", "setup.py", "pyproject.toml"):
        return f
    if f.startswith("requirements"):
        return "requirements/"

    # Docs, CI config — not interesting for failure patterns
    if f.startswith("docs/") or f.startswith(".buildkite/") or f.endswith(".md"):
        return None

    return None


def normalize_job_name(job: str) -> str:
    """Strip hardware suffixes like (mi300_1), (B200) etc."""
    return re.sub(r"\s*\([^)]*\)\s*$", "", job).strip()


def load_pr_data(eval_dir: Path, replay_dir: Path) -> list[dict]:
    """
    For each PR: load changed_files from replay and failing jobs from eval report.
    Returns list of {pr, changed_files, failing_jobs, failing_tests}.
    """
    records = []
    for pr_dir in sorted(eval_dir.iterdir()):
        pr_num = pr_dir.name.replace("pr_", "")
        report_path = pr_dir / "evaluation_report.json"
        if not report_path.exists():
            continue

        report = json.load(open(report_path))
        fns = report.get("false_negative_details", [])
        tps = report.get("true_positive_details", [])

        # Collect all CI failures (FN + TP matched failures)
        failing_jobs: set[str] = set()
        failing_tests: set[str] = set()
        for fn in fns:
            job = fn.get("job_name", "").strip()
            test = fn.get("failed_test", "").strip()
            if job:
                failing_jobs.add(normalize_job_name(job))
            if test and not test.startswith("[job]"):
                failing_tests.add(test)
        for tp in tps:
            matched = tp.get("matched_failure", "").strip()
            if matched and not matched.startswith("[job]"):
                failing_tests.add(matched)

        if not failing_jobs and not failing_tests:
            continue  # PR had no CI failures worth recording

        # Load changed files from replay (try both top-level and base-dir replays)
        changed_files: list[str] = []
        for candidate_replay in [
            replay_dir / f"pr_{pr_num}" / "selector_replay.json",
            replay_dir.parent / "replay" / f"pr_{pr_num}" / "selector_replay.json",
        ]:
            if candidate_replay.exists():
                replay = json.load(open(candidate_replay))
                changed_files = replay.get("changed_files", [])
                break

        if not changed_files:
            continue

        records.append({
            "pr": pr_num,
            "changed_files": changed_files,
            "failing_jobs": sorted(failing_jobs),
            "failing_tests": sorted(failing_tests),
        })

    return records


def build_patterns(records: list[dict]) -> dict:
    """
    Build pattern map: source_area -> {
        job_name -> {count, prs, co_occurring_areas}
    }
    """
    # source_area -> job_name -> {count, prs}
    area_to_jobs: dict[str, dict[str, dict]] = defaultdict(lambda: defaultdict(lambda: {"count": 0, "prs": []}))

    # source_area -> failing test paths
    area_to_tests: dict[str, dict[str, dict]] = defaultdict(lambda: defaultdict(lambda: {"count": 0, "prs": []}))

    for rec in records:
        source_areas = set()
        for f in rec["changed_files"]:
            area = normalize_source_area(f)
            if area:
                source_areas.add(area)

        for area in source_areas:
            for job in rec["failing_jobs"]:
                area_to_jobs[area][job]["count"] += 1
                area_to_jobs[area][job]["prs"].append(rec["pr"])
            for test in rec["failing_tests"]:
                area_to_tests[area][test]["count"] += 1
                area_to_tests[area][test]["prs"].append(rec["pr"])

    # Build final structure, sorted by failure frequency
    patterns = {}
    all_areas = sorted(set(area_to_jobs) | set(area_to_tests))

    for area in all_areas:
        jobs = area_to_jobs.get(area, {})
        tests = area_to_tests.get(area, {})

        top_jobs = sorted(
            [{"job": j, "failure_count": v["count"], "seen_in_prs": sorted(set(v["prs"]))}
             for j, v in jobs.items()],
            key=lambda x: -x["failure_count"]
        )
        top_tests = sorted(
            [{"test_path": t, "failure_count": v["count"], "seen_in_prs": sorted(set(v["prs"]))}
             for t, v in tests.items()],
            key=lambda x: -x["failure_count"]
        )

        patterns[area] = {
            "total_prs_with_failures": len({pr for j in jobs.values() for pr in j["prs"]}),
            "frequently_failing_jobs": top_jobs[:10],
            "frequently_failing_tests": top_tests[:10],
        }

    return patterns


def build_job_index(records: list[dict]) -> dict:
    """
    Reverse index: job_name -> which source areas most often change when this job fails.
    Useful for the critic agent to ask "AMD entrypoints failed — what usually caused it?"
    """
    job_to_areas: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))

    for rec in records:
        source_areas = set()
        for f in rec["changed_files"]:
            area = normalize_source_area(f)
            if area:
                source_areas.add(area)
        for job in rec["failing_jobs"]:
            for area in source_areas:
                job_to_areas[job][area] += 1

    index = {}
    for job, areas in sorted(job_to_areas.items()):
        index[job] = {
            "most_common_source_areas": sorted(
                [{"area": a, "co_occurrence_count": c} for a, c in areas.items()],
                key=lambda x: -x["co_occurrence_count"]
            )[:8]
        }
    return index


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--eval-dir",   default=".buildkite/test_selection_skills/evaluation", type=Path)
    parser.add_argument("--replay-dir", default=".buildkite/test_selection_skills/replay",     type=Path)
    parser.add_argument("--output",     default=".buildkite/test_selection_skills/failure_patterns.json", type=Path)
    args = parser.parse_args()

    print(f"Loading PR data from {args.eval_dir} ...")
    records = load_pr_data(args.eval_dir, args.replay_dir)
    print(f"  {len(records)} PRs with CI failures and known changed files")

    print("Building source-area → failure patterns ...")
    patterns = build_patterns(records)

    print("Building job → source-area reverse index ...")
    job_index = build_job_index(records)

    output = {
        "_meta": {
            "description": (
                "Historical CI failure patterns derived from offline evaluation runs. "
                "Maps source areas to jobs/tests that historically fail when those areas change. "
                "Used by the critic agent to identify gaps in test selections."
            ),
            "pr_count": len(records),
            "source_area_count": len(patterns),
            "how_to_use": (
                "Given a PR's changed files, look up each source area in 'by_source_area'. "
                "The 'frequently_failing_jobs' list tells you which CI jobs historically fail "
                "for that area — check whether the primary selector covered them. "
                "Use 'by_job' to ask the reverse question: given a known failing job type, "
                "what source areas usually caused it?"
            ),
        },
        "by_source_area": patterns,
        "by_job": job_index,
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\nWritten → {args.output}")
    print(f"  {len(patterns)} source areas")
    print(f"  {len(job_index)} job types indexed")

    # Print top patterns for a quick sanity check
    print("\nTop source areas by failure count:")
    top = sorted(patterns.items(), key=lambda x: -x[1]["total_prs_with_failures"])[:8]
    for area, data in top:
        jobs = [j["job"] for j in data["frequently_failing_jobs"][:3]]
        print(f"  {area:<35} {data['total_prs_with_failures']} PRs  →  {', '.join(jobs)}")


if __name__ == "__main__":
    main()
