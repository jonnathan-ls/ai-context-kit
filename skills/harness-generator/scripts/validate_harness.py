#!/usr/bin/env python3
"""Validate generated harness structure and integration links."""

from __future__ import annotations

import argparse
from pathlib import Path

REQUIRED_FILES = [
    "MANIFEST.json",
    "README.md",
    "config/token-budget.json",
    "config/protocol.md",
    "rules/code-standards.md",
    "rules/response-discipline.md",
    "rules/socratic-gate.md",
    "rules/workspace-guard.md",
    "skills/context-validator/SKILL.md",
    "skills/spec-enforcer/SKILL.md",
    "skills/evidence-checker/SKILL.md",
    "specs/_template.md",
    "specs/harness-integration.md",
    "scripts/validate_harness.py",
]


def evaluate(repo: Path, harness: Path) -> tuple[str, list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    for rel in REQUIRED_FILES:
        if not (harness / rel).exists():
            errors.append(f"missing required file: {rel}")

    for link_name, target_suffix in ((".agents", ".ai-context/agents"), (".claude", ".ai-context/claude")):
        link_path = repo / link_name
        if not link_path.exists() and not link_path.is_symlink():
            warnings.append(f"optional link not found: {link_name}")
            continue

        if not link_path.is_symlink():
            errors.append(f"expected symlink: {link_name}")
            continue

        resolved_target = str(link_path.resolve())
        if not resolved_target.endswith(target_suffix):
            errors.append(f"unexpected symlink target for {link_name}: {resolved_target}")

    status = "PASS"
    if errors:
        status = "BLOCK"
    elif warnings:
        status = "WARN"

    return status, errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate generated harness")
    parser.add_argument("--repo", default=".", help="Repository root")
    parser.add_argument("--harness", default=".ai-context", help="Harness directory path")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    harness = (repo / args.harness).resolve()

    status, errors, warnings = evaluate(repo, harness)
    print(f"Status: {status}")
    for error in errors:
        print(f"ERROR: {error}")
    for warning in warnings:
        print(f"WARN: {warning}")

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
