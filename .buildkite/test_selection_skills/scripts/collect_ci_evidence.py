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
    # Strip job ID fragment (e.g., "70063#019e942c-..." -> "70063")
    build_number = parts[1].split("#")[0]
    return (org_pipeline[0], org_pipeline[1], build_number)


def extract_buildkite_jobs_from_statuses(statuses: list) -> list[dict]:
    """Extract all Buildkite job information from GitHub commit statuses."""
    jobs = []
    seen_builds = set()

    for status in statuses:
        context = status.get("context", "")
        if not context.startswith("buildkite/"):
            continue

        target_url = status.get("target_url", "")
        if not target_url:
            continue

        # Extract org, pipeline, build from URL
        parsed = parse_buildkite_build_url(target_url)
        if not parsed:
            continue

        org, pipeline, build_number = parsed
        build_key = f"{org}/{pipeline}/{build_number}"
        if build_key in seen_builds:
            continue
        seen_builds.add(build_key)

        jobs.append({
            "build_url": target_url,
            "org": org,
            "pipeline": pipeline,
            "build_number": build_number,
            "job_name": context.replace("buildkite/", ""),
            "state": status.get("state", "unknown"),
        })

    return jobs


def normalize_ci_evidence(pr_number: int, repo: str, buildkite_builds: list[dict], github_statuses: dict, test_run_data: dict = None, all_tests_run: list = None) -> dict:
    """Normalize collected evidence into standard format."""
    builds = []
    jobs_failed = []
    jobs_run = []

    for build in buildkite_builds:
        builds.append({
            "build_id": build.get("id", ""),
            "build_number": str(build.get("number", "")),
            "pipeline": f"{build.get('organization', {}).get('slug', '')}/{build.get('pipeline', {}).get('slug', '')}",
            "url": build.get("url", ""),
            "commit": build.get("commit_id", ""),
            "branch": build.get("branch_name", ""),
            "state": build.get("state", ""),
            "started_at": build.get("started_at", ""),
            "finished_at": build.get("finished_at", ""),
        })

        # Extract all jobs from the build
        for job in build.get("jobs", []):
            if job.get("state") == "failed":
                jobs_failed.append({
                    "job_id": job.get("id", ""),
                    "name": job.get("name", ""),
                    "state": job.get("state", "unknown"),
                    "exit_status": job.get("exit_status", 1),
                    "url": job.get("url", ""),
                })
            jobs_run.append({
                "job_id": job.get("id", ""),
                "name": job.get("name", ""),
                "state": job.get("state", "unknown"),
                "exit_status": job.get("exit_status", 0),
                "url": job.get("url", ""),
            })

    # Process test executions
    tests_run = []
    tests_failed = []
    failed_test_list = []

    if all_tests_run:
        tests_run = all_tests_run
        for test in all_tests_run:
            test_state = test.get("state") or test.get("status", "unknown")
            test_name = test.get("test_name", "")
            test_id = test.get("test_id", test.get("id", test_name))

            # Only include actual test executions (exclude collected runs with no state)
            if test_name and test_state != "unknown":
                test_info = {
                    "test_id": test_id,
                    "test_name": test_name,
                    "file": test.get("file", test_name.split("::")[0] if "::" in test_name else test_name),
                    "state": test_state,
                    "job_id": test.get("job_id", ""),
                }

                if test_state == "failed":
                    tests_failed.append(test_info)
                    failed_entry = {
                        "identifier": test_name,
                        "file": test_info["file"],
                        "function": test_name.split("::")[-1] if "::" in test_name else "",
                        "job_id": test_info["job_id"],
                        "job_name": next((job["name"] for job in jobs_run if job.get("job_id") == test_info["job_id"]), ""),
                        "state": test_state,
                        "failure_details": test.get("failure_details", {})
                    }
                    failed_test_list.append(failed_entry)
                tests_run.append(test_info)

    # Determine status
    status = "success"
    notes = []

    if not buildkite_builds and not github_statuses.get("statuses"):
        status = "no_results"
        notes = ["No Buildkite build or GitHub statuses found for this PR"]
    elif not builds:
        status = "no_build"
        notes = ["GitHub statuses found, but no Buildkite build data was fetched"]
    elif not tests_run:
        status = "partial"
        notes = ["Buildkite build(s) found, but no test run data from Buildkite Test Engine"]
    else:
        notes = []

    # Add standard notes
    notes.append(f"Evidence collected on {datetime.now(timezone.utc).isoformat()}")
    notes.append(f"Buildkite builds found: {len(builds)}")
    notes.append(f"Total tests run: {len(tests_run)}")
    notes.append(f"Failed tests: {len(tests_failed)}")

    return {
        "pr_number": str(pr_number),
        "repo": repo,
        "status": status,
        "buildkite_builds": builds,
        "jobs_run": jobs_run,
        "jobs_failed": jobs_failed,
        "tests_run": tests_run,
        "tests_failed": tests_failed,
        "failed_test_list": failed_test_list,
        "tests_run_count": len(tests_run),
        "artifacts": [],
        "notes": notes,
    }


def fetch_test_runs_from_buildkite(org: str, pipeline: str, build_number: str) -> tuple[dict, list]:
    """Fetch test runs from Buildkite Test Engine using fetch_buildkite_tests.py script."""
    try:
        script_dir = Path(__file__).parent
        fetch_script = script_dir / "fetch_buildkite_tests.py"

        if not fetch_script.exists():
            print(f"  Error: fetch_buildkite_tests.py not found at {fetch_script}", file=sys.stderr)
            return {}, []

        # Call the fetch script with subprocess
        cmd = [
            sys.executable,
            str(fetch_script),
            "--org", org,
            "--pipeline", pipeline,
            "--build", str(build_number)
        ]

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)

        if result.returncode != 0:
            print(f"  Error fetching test runs: {result.stderr}", file=sys.stderr)
            return {}, []

        # Parse JSON output from the script
        data = json.loads(result.stdout)

        # Extract test executions
        test_runs = data.get("test_runs", [])
        all_tests = data.get("tests", [])

        print(f"  Found {len(test_runs)} test runs with {len(all_tests)} test executions")
        return {"test_runs": test_runs}, all_tests

    except subprocess.TimeoutExpired:
        print(f"  Timeout fetching test runs", file=sys.stderr)
    except json.JSONDecodeError as e:
        print(f"  Error parsing test run data: {e}", file=sys.stderr)
    except Exception as e:
        print(f"  Could not fetch test runs: {e}", file=sys.stderr)
    return {}, []


def main():
    parser = argparse.ArgumentParser(description="Collect Buildkite CI evidence for a historical PR")
    parser.add_argument("pr_number", type=int, help="PR number to collect evidence for")
    parser.add_argument("--repo", type=str, default="vllm-project/vllm", help="Repository name")
    parser.add_argument("--output-dir", type=str, default=None, help="Output directory")
    parser.add_argument("--skip-test-runs", action="store_true",
                        help="Skip fetching test run data from Buildkite Test Engine")
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

    # Find all Buildkite builds from statuses
    buildkite_jobs = extract_buildkite_jobs_from_statuses(statuses.get("statuses", []))
    print(f"  Found {len(buildkite_jobs)} Buildkite jobs in statuses", file=sys.stderr)

    buildkite_builds = []
    all_tests_run = []
    test_run_data = {}

    for job in buildkite_jobs:
        print(f"  Fetching Buildkite build: {job['org']}/{job['pipeline']}/builds/{job['build_number']}", file=sys.stderr)
        api_token = os.environ.get("BUILDKITE_API_TOKEN")
        buildkite_build = fetch_buildkite_build(job["org"], job["pipeline"], job["build_number"], api_token)
        if buildkite_build:
            buildkite_builds.append(buildkite_build)

            # Fetch test runs unless explicitly skipped
            if not args.skip_test_runs:
                print(f"  Fetching test runs for build {job['org']}/{job['pipeline']}/{job['build_number']}...", file=sys.stderr)
                build_test_run_data, build_tests_run = fetch_test_runs_from_buildkite(job["org"], job["pipeline"], job["build_number"])
                if build_test_run_data:
                    test_run_data = build_test_run_data
                all_tests_run.extend(build_tests_run)
            else:
                print("  Skipping test run data collection (--skip-test-runs)", file=sys.stderr)

    # Normalize evidence
    print("  Normalizing evidence...", file=sys.stderr)
    evidence = normalize_ci_evidence(pr_number, repo, buildkite_builds, statuses, test_run_data, all_tests_run)

    # Write output
    if args.output_dir:
        output_dir = Path(args.output_dir)
    else:
        output_dir = Path(f".buildkite/test_selection_skills/evidence/pr_{pr_number}")

    output_dir.mkdir(parents=True, exist_ok=True)

    evidence_path = output_dir / "ci_evidence.json"
    evidence_path.write_text(json.dumps(evidence, indent=2) + "\n")
    print(f"  Evidence written to: {evidence_path}", file=sys.stderr)

    # Print summary
    print(f"\n=== Summary ===", file=sys.stderr)
    print(f"Status: {evidence['status']}", file=sys.stderr)
    print(f"Builds found: {len(evidence['buildkite_builds'])}", file=sys.stderr)
    print(f"Tests run: {evidence['tests_run_count']}", file=sys.stderr)
    print(f"Failed tests: {len(evidence['failed_test_list'])}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())