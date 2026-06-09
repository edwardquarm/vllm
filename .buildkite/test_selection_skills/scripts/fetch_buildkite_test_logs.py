#!/usr/bin/env python3
"""Fetch actual test failures from Buildkite job logs.

This script fetches the raw logs from failed Buildkite jobs and parses
pytest output to extract the actual failing test names.

Usage:
    python fetch_buildkite_test_logs.py --org vllm --pipeline ci --build 70063
"""

import argparse
import json
import os
import re
import sys
import urllib.request
from typing import List, Dict, Tuple


def fetch_buildkite_api(url: str, api_token: str = None) -> Dict:
    """Fetch data from Buildkite API."""
    headers = {}
    if api_token:
        headers["Authorization"] = f"Bearer {api_token}"

    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=60) as response:
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as e:
        if e.code == 401:
            print(f"Buildkite API: Authentication required. Set BUILDKITE_API_TOKEN.", file=sys.stderr)
        elif e.code == 404:
            print(f"Buildkite API: Resource not found ({url})", file=sys.stderr)
        else:
            print(f"Buildkite API error ({e.code}): {e.reason}", file=sys.stderr)
        return {}
    except Exception as e:
        print(f"Buildkite API error: {e}", file=sys.stderr)
        return {}


def get_failed_jobs(org: str, pipeline: str, build_number: str, api_token: str = None) -> List[Dict]:
    """Get all failed jobs from a Buildkite build."""
    url = f"https://api.buildkite.com/v2/organizations/{org}/pipelines/{pipeline}/builds/{build_number}"
    build_data = fetch_buildkite_api(url, api_token)

    if not build_data:
        return []

    failed_jobs = []
    for job in build_data.get("jobs", []):
        if job.get("state") == "failed" and job.get("type") == "script":
            failed_jobs.append({
                "id": job.get("id"),
                "name": job.get("name"),
                "state": job.get("state"),
                "exit_status": job.get("exit_status"),
                "log_url": job.get("raw_log_url"),
            })

    return failed_jobs


def fetch_job_log(org: str, pipeline: str, build_number: str, job_id: str, api_token: str = None) -> str:
    """Fetch the raw log for a specific job."""
    url = f"https://api.buildkite.com/v2/organizations/{org}/pipelines/{pipeline}/builds/{build_number}/jobs/{job_id}/log"

    headers = {}
    if api_token:
        headers["Authorization"] = f"Bearer {api_token}"

    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=120) as response:
            log_data = json.loads(response.read().decode())
            return log_data.get("content", "")
    except Exception as e:
        print(f"Error fetching log for job {job_id}: {e}", file=sys.stderr)
        return ""


def parse_pytest_failures(log_content: str) -> List[str]:
    """Extract failed test names from pytest log output.

    Returns list of test identifiers in format: file.py::TestClass::test_function
    """
    # Remove ANSI color codes
    ansi_escape = re.compile(r'\x1b\[[0-9;]*m')
    clean_log = ansi_escape.sub('', log_content)

    failed_tests = []

    # Pattern 1: Lines with "test_xyz.py::test_name FAILED"
    # Matches: "test_file.py::TestClass::test_method[param] FAILED"
    pattern1 = r'([\w/_]+\.py::\S+)\s+FAILED'
    matches1 = re.findall(pattern1, clean_log)

    # Pattern 2: FAILED lines in summary section
    # Matches: "FAILED test_file.py::test_name - AssertionError..."
    pattern2 = r'FAILED\s+([\w/_]+\.py::\S+)'
    matches2 = re.findall(pattern2, clean_log)

    # Combine and deduplicate
    all_matches = matches1 + matches2

    # Extract base test name (remove parametrization details for deduplication)
    # But keep the full name for the final list
    seen_base = set()
    for match in all_matches:
        # Extract base name (without parameters)
        base_match = re.sub(r'\[.*?\]$', '', match)

        # Only add if we haven't seen this base test
        if base_match not in seen_base:
            failed_tests.append(match)
            seen_base.add(base_match)

    return failed_tests


def main():
    parser = argparse.ArgumentParser(description="Fetch actual test failures from Buildkite logs")
    parser.add_argument("--org", required=True, help="Buildkite organization")
    parser.add_argument("--pipeline", required=True, help="Buildkite pipeline")
    parser.add_argument("--build", required=True, help="Build number")
    parser.add_argument("--output", help="Output JSON file (default: stdout)")
    args = parser.parse_args()

    api_token = os.environ.get("BUILDKITE_API_TOKEN")
    if not api_token:
        print("Warning: BUILDKITE_API_TOKEN not set. API requests may fail.", file=sys.stderr)

    print(f"Fetching failed jobs for build {args.build}...", file=sys.stderr)
    failed_jobs = get_failed_jobs(args.org, args.pipeline, args.build, api_token)

    if not failed_jobs:
        print("No failed jobs found.", file=sys.stderr)
        result = {
            "build": args.build,
            "failed_jobs": [],
            "failed_tests": [],
            "total_failures": 0,
        }
        print(json.dumps(result, indent=2))
        return 0

    print(f"Found {len(failed_jobs)} failed jobs", file=sys.stderr)

    all_failed_tests = []
    job_details = []

    for job in failed_jobs:
        print(f"  Fetching log for: {job['name']}...", file=sys.stderr)
        log_content = fetch_job_log(args.org, args.pipeline, args.build, job['id'], api_token)

        if not log_content:
            print(f"    Warning: Could not fetch log", file=sys.stderr)
            job_details.append({
                "job_id": job['id'],
                "job_name": job['name'],
                "failed_tests": [],
                "test_count": 0,
                "log_fetched": False,
            })
            continue

        failed_tests = parse_pytest_failures(log_content)
        print(f"    Found {len(failed_tests)} failed tests", file=sys.stderr)

        job_details.append({
            "job_id": job['id'],
            "job_name": job['name'],
            "failed_tests": failed_tests,
            "test_count": len(failed_tests),
            "log_fetched": True,
        })

        # Add to global list with job context
        for test in failed_tests:
            all_failed_tests.append({
                "test_name": test,
                "job_id": job['id'],
                "job_name": job['name'],
            })

    result = {
        "org": args.org,
        "pipeline": args.pipeline,
        "build": args.build,
        "failed_jobs": job_details,
        "failed_tests": all_failed_tests,
        "total_failures": len(all_failed_tests),
    }

    # Output
    output_json = json.dumps(result, indent=2)
    if args.output:
        with open(args.output, 'w') as f:
            f.write(output_json)
        print(f"\nResults written to: {args.output}", file=sys.stderr)
    else:
        print(output_json)

    print(f"\n=== Summary ===", file=sys.stderr)
    print(f"Failed jobs: {len(failed_jobs)}", file=sys.stderr)
    print(f"Total failed tests: {len(all_failed_tests)}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
