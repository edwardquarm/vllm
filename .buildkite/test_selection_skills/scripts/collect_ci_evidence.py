#!/usr/bin/env python3
"""Collect Buildkite CI evidence for a historical PR (Lane 1).

Usage:
    python collect_ci_evidence.py <pr_number> [--repo <repo>] [--output-dir <dir>]
"""

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def run_gh_api(endpoint: str) -> dict:
    """Run a GitHub API call using the gh CLI."""
    cmd = ["gh", "api", endpoint]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"GitHub API error: {result.stderr}", file=sys.stderr)
        return {}
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        return {}


def fetch_buildkite_build(org: str, pipeline: str, build_number: str, api_token: str | None = None) -> dict:
    """Fetch Buildkite build details from the API."""
    url = f"https://api.buildkite.com/v2/organizations/{org}/pipelines/{pipeline}/builds/{build_number}"
    headers = {}
    if api_token:
        headers["Authorization"] = f"Bearer {api_token}"

    try:
        import urllib.request
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as response:
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as e:
        if e.code == 401:
            print("Buildkite API: Authentication required. Set BUILDKITE_API_TOKEN.", file=sys.stderr)
        else:
            print(f"Buildkite API error ({e.code}): {e.reason}", file=sys.stderr)
        return {}
    except Exception as e:
        print(f"Buildkite API error: {e}", file=sys.stderr)
        return {}


def parse_buildkite_build_url(url: str) -> tuple[str, str, str] | None:
    """Parse Buildkite URL to extract org, pipeline, build number."""
    if not url.startswith("https://buildkite.com/"):
        return None
    parts = url.replace("https://buildkite.com/", "").split("/builds/")
    if len(parts) != 2:
        return None
    org_pipeline = parts[0].split("/")
    if len(org_pipeline) != 2:
        return None
    return (org_pipeline[0], org_pipeline[1], parts[1])


def extract_failed_jobs_from_statuses(statuses: list) -> list[dict]:
    """Extract failed job information from GitHub commit statuses."""
    failed_jobs = []
    seen_jobs = set()

    for status in statuses:
        context = status.get("context", "")
        if not context.startswith("buildkite/ci/pr/"):
            continue
        job_name = context.replace("buildkite/ci/pr/", "")
        if not job_name or job_name == "ci":
            continue
        if job_name in seen_jobs:
            continue
        seen_jobs.add(job_name)

        target_url = status.get("target_url", "")
        job_id = target_url.split("#")[-1] if "#" in target_url else None

        failed_jobs.append({
            "job_id": job_id,
            "name": job_name,
            "state": "failed",
            "exit_status": 1,
            "url": target_url,
            "build_id": None,
            "retry_attempt": None,
        })

    return failed_jobs


def normalize_ci_evidence(pr_number: int, repo: str, buildkite_build: dict, github_statuses: dict, test_run_data: dict = None, all_tests_run: list = None) -> dict:
    """Normalize collected evidence into standard format."""
    builds = []
    if buildkite_build:
        builds.append({
            "build_id": buildkite_build.get("id", ""),
            "build_number": str(buildkite_build.get("number", "")),
            "pipeline": f"{buildkite_build.get('organization', {}).get('slug', '')}/{buildkite_build.get('pipeline', {}).get('slug', '')}",
            "url": buildkite_build.get("url", ""),
            "commit": buildkite_build.get("commit_id", ""),
            "branch": buildkite_build.get("branch_name", ""),
            "state": buildkite_build.get("state", ""),
            "started_at": buildkite_build.get("started_at", ""),
            "finished_at": buildkite_build.get("finished_at", ""),
        })

    failed_statuses = github_statuses.get("statuses", [])
    jobs_failed = extract_failed_jobs_from_statuses(failed_statuses)

    # Extract tests run from test run data
    tests_run = all_tests_run if all_tests_run else []
    tests_failed = []
    if test_run_data and 'executions' in test_run_data:
        for exec_item in test_run_data.get('executions', []):
            test_info = {
                "test_id": exec_item.get("test_id", ""),
                "test_name": exec_item.get("test_name", ""),
                "file": exec_item.get("file", ""),
                "state": exec_item.get("state", ""),
            }
            if not tests_run:  # Only add if we don't have all_tests_run
                tests_run.append(test_info)
            if exec_item.get("state") == "failed":
                tests_failed.append(test_info)

    # Determine status
    status = "success" if (test_run_data or tests_run or jobs_failed) else "partial"
    notes = []

    if not buildkite_build and not github_statuses and not tests_run:
        status = "no_results"
        notes.append("No Buildkite or GitHub status data found for this PR")

    notes.append(f"Evidence collected on {datetime.now(timezone.utc).isoformat()}")
    notes.append(f"Tests run from Buildkite Test Engine: {len(tests_run)}")

    return {
        "pr_number": str(pr_number),
        "repo": repo,
        "status": status,
        "buildkite_builds": builds,
        "jobs_run": jobs_failed,
        "jobs_failed": jobs_failed,
        "tests_run": tests_run,
        "tests_failed": tests_failed,
        "failed_test_list": tests_failed,  # Use test-level failures
        "tests_run_count": len(tests_run),
        "artifacts": [],
        "notes": notes,
    }


def fetch_test_runs_from_buildkite(org: str, pipeline: str, build_number: str) -> tuple[dict, list]:
    """Fetch test runs from Buildkite Test Engine using subprocess to call MCP.

    Returns:
        (test_run_data, list of all tests run)
    """
    try:
        # Use claude to call the Buildkite MCP server
        import subprocess
        prompt = f"""Use the Buildkite MCP server to get test run data.
Call get_build_analytics with:
  org_slug: "{org}"
  pipeline_slug: "{pipeline}"
  build_number: "{build_number}"

Return ONLY the raw JSON response, nothing else."""

        result = subprocess.run(
            ["claude", "-p", "--model", "haiku", prompt],
            capture_output=True, text=True, timeout=60
        )
        if result.returncode == 0:
            # Try to parse the response
            import re
            json_match = re.search(r'\{.*\}', result.stdout, re.DOTALL)
            if json_match:
                test_data = json.loads(json_match.group())
                # Extract test executions
                tests = []
                if 'test_runs' in test_data:
                    for run in test_data['test_runs']:
                        tests.append({
                            "test_id": run.get("test_id", ""),
                            "test_name": run.get("test_name", ""),
                            "file": run.get("file", ""),
                            "state": run.get("state", "passed")
                        })
                return test_data, tests
    except Exception as e:
        print(f"  Could not fetch test runs: {e}", file=sys.stderr)
    return {}, []


def main():
    parser = argparse.ArgumentParser(description="Collect Buildkite CI evidence for a historical PR")
    parser.add_argument("pr_number", type=int, help="PR number to collect evidence for")
    parser.add_argument("--repo", type=str, default="vllm-project/vllm", help="Repository name")
    parser.add_argument("--output-dir", type=str, default=None, help="Output directory")
    parser.add_argument("--fetch-test-runs", action="store_true",
                        help="Fetch full test run data from Buildkite Test Engine")
    args = parser.parse_args()

    pr_number = args.pr_number
    repo = args.repo

    print(f"Collecting CI evidence for PR #{pr_number}...", file=sys.stderr)

    # Fetch PR details
    print(f"  Fetching PR #{pr_number} from GitHub...", file=sys.stderr)
    pr_data = run_gh_api(f"repos/{repo}/pulls/{pr_number}")
    if not pr_data:
        print(f"Error: Could not fetch PR #{pr_number}", file=sys.stderr)
        sys.exit(1)

    commit = pr_data.get("merge_commit_sha") or pr_data.get("head", {}).get("sha")
    if not commit:
        print("Error: Could not determine commit SHA for PR", file=sys.stderr)
        sys.exit(1)
    print(f"  Commit: {commit}", file=sys.stderr)

    # Fetch commit statuses
    print("  Fetching GitHub commit statuses...", file=sys.stderr)
    statuses = run_gh_api(f"repos/{repo}/commits/{commit}/status")

    # Find and fetch Buildkite build
    buildkite_build = {}
    build_url = None
    for status in statuses.get("statuses", []):
        if status.get("context") == "buildkite/ci/pr":
            build_url = status.get("target_url")
            break

    all_tests_run = []
    test_run_data = {}

    if build_url:
        parsed = parse_buildkite_build_url(build_url)
        if parsed:
            org, pipeline, build_num = parsed
            print(f"  Fetching Buildkite build: {org}/{pipeline}/builds/{build_num}", file=sys.stderr)
            api_token = os.environ.get("BUILDKITE_API_TOKEN")
            if api_token:
                print("  Using authenticated Buildkite API access", file=sys.stderr)
            else:
                print("  No BUILDKITE_API_TOKEN; using public data", file=sys.stderr)
            buildkite_build = fetch_buildkite_build(org, pipeline, build_num, api_token)

            # Fetch test runs if requested
            if args.fetch_test_runs:
                print(f"  Fetching test runs from Buildkite Test Engine...", file=sys.stderr)
                test_run_data, all_tests_run = fetch_test_runs_from_buildkite(org, pipeline, build_num)
                print(f"  Found {len(all_tests_run)} tests run", file=sys.stderr)

    # Normalize evidence
    print("  Normalizing evidence...", file=sys.stderr)
    evidence = normalize_ci_evidence(pr_number, repo, buildkite_build, statuses, test_run_data, all_tests_run)

    # Write output
    if args.output_dir:
        output_dir = Path(args.output_dir)
    else:
        output_dir = Path(f".buildkite/test_selection_skills/evidence/pr_{pr_number}")

    output_dir.mkdir(parents=True, exist_ok=True)

    evidence_path = output_dir / "ci_evidence.json"
    evidence_path.write_text(json.dumps(evidence, indent=2) + "\n")
    print(f"  Evidence written to: {evidence_path}", file=sys.stderr)

    # Write raw data
    raw_dir = output_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    if buildkite_build:
        (raw_dir / f"build_{buildkite_build.get('number', 'unknown')}.json").write_text(
            json.dumps(buildkite_build, indent=2) + "\n"
        )
    if statuses:
        (raw_dir / "github_statuses.json").write_text(json.dumps(statuses, indent=2) + "\n")
    if test_run_data:
        (raw_dir / "test_run_data.json").write_text(json.dumps(test_run_data, indent=2) + "\n")

    # Print summary
    print(f"\n=== Summary ===", file=sys.stderr)
    print(f"Status: {evidence['status']}", file=sys.stderr)
    print(f"Builds found: {len(evidence['buildkite_builds'])}", file=sys.stderr)
    print(f"Tests run: {evidence['tests_run_count']}", file=sys.stderr)
    print(f"Failed jobs: {len(evidence['jobs_failed'])}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
