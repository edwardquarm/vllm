#!/usr/bin/env python3
"""
Fetch Buildkite test run data using the MCP tools (fallback to REST API).

This script uses the MCP `list_test_runs` tool as a primary method and falls back
to the Buildkite REST API if the MCP tool fails.
"""

import argparse
import json
import os
import sys
import urllib.error
from typing import Any, Dict


def fetch_test_runs_mcp(org_slug: str, pipeline_slug: str) -> Dict[str, Any]:
    """Fetch test runs using the MCP `list_test_runs` tool (hardcoded test_suite_slug)."""
    from claude_toolkit.tools import CPTool

    # Guess test_suite_slug = pipeline_slug (common convention)
    test_suite_slug = pipeline_slug

    try:
        # Try MCP list_test_runs tool
        tool = CPTool.get_tool("mcp__buildkite_litellm__buildkite_mcp_server-list_test_runs")
        result = tool.invoke({
            "org_slug": org_slug,
            "test_suite_slug": test_suite_slug,
            "per_page": 100  # Fetch recent test runs
        })

        if "items" in result:
            # Extract all test executions
            all_tests = []
            for run in result["items"]:
                if "test_executions" in run:
                    all_tests.extend(run["test_executions"])
                elif "executions" in run:
                    all_tests.extend(run["executions"])

            return {
                "test_runs": result["items"],
                "all_tests": sorted({test.get("test_name", "") for test in all_tests}),
                "tests": all_tests
            }
    except Exception as e:
        print(f"MCP tool failed: {e}", file=sys.stderr)

    return {}


def fetch_test_runs_rest(org_slug: str, pipeline_slug: str, build_number: str) -> Dict[str, Any]:
    """Fetch test runs using the Buildkite REST API (fallback)."""
    api_token = os.environ.get("BUILDKITE_API_TOKEN")
    url = f"https://api.buildkite.com/v2/organizations/{org_slug}/pipelines/{pipeline_slug}/builds/{build_number}/test_runs"
    headers = {"Authorization": f"Bearer {api_token}"} if api_token else {}

    try:
        import urllib.request
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as response:
            test_runs = json.loads(response.read().decode())
            all_tests = []
            for run in test_runs:
                if "test_executions" in run:
                    all_tests.extend(run["test_executions"])
                elif "executions" in run:
                    all_tests.extend(run["executions"])

            return {
                "test_runs": test_runs,
                "all_tests": sorted({test.get("test_name", "") for test in all_tests}),
                "tests": all_tests
            }
    except urllib.error.HTTPError as e:
        if e.code == 401:
            print("Error: Authentication required. Set BUILDKITE_API_TOKEN.", file=sys.stderr)
        elif e.code == 404:
            print(f"Error: No test runs found for build {org_slug}/{pipeline_slug}/{build_number}.", file=sys.stderr)
        else:
            print(f"Error: Buildkite API error ({e.code}): {e.reason}", file=sys.stderr)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

    return {}


def main():
    parser = argparse.ArgumentParser(description="Fetch Buildkite test run data")
    parser.add_argument("org_slug", nargs="?", help="Buildkite organization slug")
    parser.add_argument("pipeline_slug", nargs="?", help="Buildkite pipeline slug")
    parser.add_argument("build_number", nargs="?", help="Build number")
    parser.add_argument("--org", dest="org_slug_flag", help="Buildkite organization slug")
    parser.add_argument("--pipeline", dest="pipeline_slug_flag", help="Buildkite pipeline slug")
    parser.add_argument("--build", dest="build_number_flag", help="Build number")

    args = parser.parse_args()
    org_slug = args.org_slug_flag or args.org_slug
    pipeline_slug = args.pipeline_slug_flag or args.pipeline_slug
    build_number = args.build_number_flag or args.build_number

    if not org_slug or not pipeline_slug or not build_number:
        parser.error("org, pipeline, and build number are required")

    # Try MCP tools first (works if we're in a Claude session with MCP access)
    data = fetch_test_runs_mcp(org_slug, pipeline_slug)

    if not data:
        # Fall back to REST API
        data = fetch_test_runs_rest(org_slug, pipeline_slug, build_number)

    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
