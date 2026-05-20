#!/usr/bin/env python3
"""Generate a portable repository harness under .ai-context."""

from __future__ import annotations

import argparse
import json
import os
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List

GENERATOR_VERSION = "0.1.0"

RULE_FILES: Dict[str, str] = {
    "response-discipline.md": """# Response Discipline\n\n## Core directive\n\n- Answer exactly what was requested.\n- Avoid scope expansion without user request.\n- Use concise, verifiable statements.\n\n## Delivery checklist\n\n- State what changed.\n- State evidence used for validation.\n- State residual risks if validation is partial.\n""",
    "code-standards.md": """# Code Standards\n\n## Engineering baseline\n\n- Single responsibility by function/module.\n- Early return to avoid deep nesting.\n- No dead code or unrelated refactors.\n- Keep naming explicit and intention-revealing.\n\n## Change discipline\n\n- Read before edit.\n- Edit smallest possible surface.\n- Verify only relevant behavior.\n""",
    "socratic-gate.md": """# Socratic Gate\n\nAsk up to two targeted questions before acting when:\n\n- request is ambiguous\n- action is destructive or irreversible\n- required context is missing\n\nIf confidence is high and impact is low, proceed with explicit assumptions.\n""",
    "workspace-guard.md": """# Workspace Guard\n\nBefore deep file scans:\n\n1. Check if `.ai-context/workspace-map.json` exists.\n2. If missing, generate a workspace map before broad exploration.\n3. Prefer targeted reads over recursive scans.\n""",
}

SKILL_FILES: Dict[str, str] = {
    "context-validator/SKILL.md": """---\nversion: 1.0.0\nname: context-validator\ndescription: Run a compact pre-flight harness before moderate/complex tasks to confirm goal, scope, missing inputs, and validation path.\n---\n\n# Context Validator\n\n## Output\n\nStatus: PASS | WARN | BLOCK\n\n- Goal\n- Scope\n- Missing\n- Files to read next (top 3)\n- Validation\n\n## Blocking conditions\n\n- Unclear end state\n- Multiple valid interpretations\n- Missing key files or spec for non-trivial changes\n""",
    "spec-enforcer/SKILL.md": """---\nversion: 1.0.0\nname: spec-enforcer\ndescription: Enforce spec-before-code for non-trivial tasks.\n---\n\n# Spec Enforcer\n\nRequire a spec before coding if the task is multi-file, high-risk, or behavior-changing.\n\nMinimum spec sections:\n\n- Scope\n- Non-scope\n- Acceptance criteria\n- Validation\n""",
    "evidence-checker/SKILL.md": """---\nversion: 1.0.0\nname: evidence-checker\ndescription: Require practical evidence before marking a task complete.\n---\n\n# Evidence Checker\n\nUse the smallest credible evidence:\n\n1. static checks\n2. targeted tests\n3. runtime smoke\n\nNever claim success without naming the evidence used.\n""",
}

SPEC_FILES: Dict[str, str] = {
    "_template.md": """---\nname: <spec-name>\nversion: 0.1.0\ndescription: <one-line>\nstatus: draft\n---\n\n# <Title>\n\n## Scope\n\n## Non-scope\n\n## Acceptance Criteria\n\n## Implementation Notes\n\n## Validation\n""",
    "harness-integration.md": """# Harness Integration\n\nUse this repository harness as the primary protocol for AI-guided work.\n\n## Required flow\n\n1. run context-validator for moderate/complex requests\n2. enforce spec for non-trivial implementation\n3. validate with evidence before completion\n\n## Root links\n\n- .agents -> .ai-context/agents\n- .claude -> .ai-context/claude\n""",
}

README_CONTENT = """# Repository Harness\n\nThis harness provides a compact protocol for AI-assisted engineering work.\n\n## Quick start\n\n1. Review `.ai-context/rules/`\n2. Use `.ai-context/skills/context-validator` before moderate/complex tasks\n3. Keep specs under `.ai-context/specs/`\n4. Run validation:\n\n```bash\npython3 .ai-context/scripts/validate_harness.py --repo . --harness .ai-context\n```\n\n## Notes\n\n- This harness is intentionally minimal for low context cost.\n- Expand only when repeated demand proves value.\n"""

PROTOCOL_CONTENT = """# Protocol Summary\n\nPriority:\n\n1. rules\n2. skills\n3. specs\n\nExecution contract:\n\n- gather minimum context\n- avoid speculative implementation\n- enforce evidence before completion\n"""

VALIDATOR_TEMPLATE = """#!/usr/bin/env python3\n\"\"\"Validate generated harness structure and integration links.\"\"\"\n\nfrom __future__ import annotations\n\nimport argparse\nfrom pathlib import Path\n\nREQUIRED_FILES = [\n    \"MANIFEST.json\",\n    \"README.md\",\n    \"config/token-budget.json\",\n    \"config/protocol.md\",\n    \"rules/code-standards.md\",\n    \"rules/response-discipline.md\",\n    \"rules/socratic-gate.md\",\n    \"rules/workspace-guard.md\",\n    \"skills/context-validator/SKILL.md\",\n    \"skills/spec-enforcer/SKILL.md\",\n    \"skills/evidence-checker/SKILL.md\",\n    \"specs/_template.md\",\n    \"specs/harness-integration.md\",\n]\n\ndef check(repo: Path, harness: Path) -> int:\n    errors = []\n    warnings = []\n\n    for rel in REQUIRED_FILES:\n        if not (harness / rel).exists():\n            errors.append(f\"missing required file: {rel}\")\n\n    for link_name, target_suffix in ((\".agents\", \".ai-context/agents\"), (\".claude\", \".ai-context/claude\")):\n        link_path = repo / link_name\n        if not link_path.exists() and not link_path.is_symlink():\n            warnings.append(f\"optional link not found: {link_name}\")\n            continue\n        if not link_path.is_symlink():\n            errors.append(f\"expected symlink: {link_name}\")\n            continue\n        target = str(link_path.resolve())\n        if not target.endswith(target_suffix):\n            errors.append(f\"unexpected symlink target for {link_name}: {target}\")\n\n    status = \"PASS\"\n    if errors:\n        status = \"BLOCK\"\n    elif warnings:\n        status = \"WARN\"\n\n    print(f\"Status: {status}\")\n    for item in errors:\n        print(f\"ERROR: {item}\")\n    for item in warnings:\n        print(f\"WARN: {item}\")\n\n    return 1 if errors else 0\n\ndef main() -> int:\n    parser = argparse.ArgumentParser(description=\"Validate generated harness\")\n    parser.add_argument(\"--repo\", default=\".\", help=\"Repository root\")\n    parser.add_argument(\"--harness\", default=\".ai-context\", help=\"Harness directory\")\n    args = parser.parse_args()\n\n    repo = Path(args.repo).resolve()\n    harness = (repo / args.harness).resolve()\n    return check(repo, harness)\n\nif __name__ == \"__main__\":\n    raise SystemExit(main())\n"""


@dataclass
class Profile:
    project_name: str
    project_type: str
    primary_stack: str
    strictness: str


def detect_stack(repo: Path) -> str:
    if (repo / "package.json").exists():
        return "node"
    if (repo / "pyproject.toml").exists() or (repo / "requirements.txt").exists():
        return "python"
    if (repo / "go.mod").exists():
        return "go"
    if (repo / "Cargo.toml").exists():
        return "rust"
    return "generic"


def detect_type(repo: Path) -> str:
    if (repo / "apps").exists() and (repo / "packages").exists():
        return "monorepo"
    if (repo / "src").exists():
        return "application"
    return "repository"


def prompt_with_default(label: str, default: str) -> str:
    raw = input(f"{label} [{default}]: ").strip()
    return raw if raw else default


def build_profile(repo: Path, wizard: bool, args: argparse.Namespace) -> Profile:
    inferred_name = repo.name
    inferred_type = detect_type(repo)
    inferred_stack = detect_stack(repo)

    if not wizard:
        return Profile(
            project_name=args.project_name or inferred_name,
            project_type=args.project_type or inferred_type,
            primary_stack=args.primary_stack or inferred_stack,
            strictness=args.strictness,
        )

    print("Harness Generator Wizard")
    print("Press Enter to accept defaults.")
    project_name = prompt_with_default("Project name", args.project_name or inferred_name)
    project_type = prompt_with_default("Project type", args.project_type or inferred_type)
    primary_stack = prompt_with_default("Primary stack", args.primary_stack or inferred_stack)
    strictness = prompt_with_default("Strictness (balanced|strict)", args.strictness)

    return Profile(
        project_name=project_name,
        project_type=project_type,
        primary_stack=primary_stack,
        strictness=strictness,
    )


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def ensure_output_dir(path: Path, force: bool) -> None:
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
        return

    if not path.is_dir():
        raise ValueError(f"Output path is not a directory: {path}")

    existing = [item for item in path.iterdir() if item.name not in {".DS_Store"}]
    if existing and not force:
        raise ValueError(
            f"Output directory is not empty: {path}. Use --force to continue."
        )


def maybe_link(root: Path, link_name: str, target: Path) -> None:
    link_path = root / link_name
    target_rel = os.path.relpath(target, root)

    if link_path.is_symlink():
        if os.readlink(link_path) == target_rel:
            return
        link_path.unlink()
    elif link_path.exists():
        raise ValueError(f"Cannot create symlink {link_name}; path already exists")

    link_path.symlink_to(target_rel)


def collect_inventory(output_dir: Path) -> List[Dict[str, str]]:
    inventory: List[Dict[str, str]] = []
    for path in sorted(output_dir.rglob("*")):
        if path.is_file():
            inventory.append(
                {
                    "path": str(path.relative_to(output_dir)),
                    "size_bytes": str(path.stat().st_size),
                }
            )
    return inventory


def generate(repo: Path, output_rel: str, profile: Profile, create_links: bool, force: bool) -> Path:
    output_dir = (repo / output_rel).resolve()
    ensure_output_dir(output_dir, force=force)

    for name, content in RULE_FILES.items():
        write_file(output_dir / "rules" / name, content)

    for rel, content in SKILL_FILES.items():
        write_file(output_dir / "skills" / rel, content)

    for name, content in SPEC_FILES.items():
        write_file(output_dir / "specs" / name, content)

    write_file(output_dir / "README.md", README_CONTENT)
    write_file(output_dir / "config" / "protocol.md", PROTOCOL_CONTENT)
    write_file(
        output_dir / "config" / "token-budget.json",
        json.dumps(
            {
                "version": 1,
                "soft_limit_kb": 40,
                "hard_limit_kb": 80,
                "mode": profile.strictness,
            },
            indent=2,
        ),
    )
    write_file(output_dir / "scripts" / "validate_harness.py", VALIDATOR_TEMPLATE)

    # Placeholder targets for root-level symlinks requested by the user.
    (output_dir / "agents").mkdir(parents=True, exist_ok=True)
    (output_dir / "claude").mkdir(parents=True, exist_ok=True)

    manifest = {
        "version": GENERATOR_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "profile": {
            "project_name": profile.project_name,
            "project_type": profile.project_type,
            "primary_stack": profile.primary_stack,
            "strictness": profile.strictness,
        },
        "selected": {
            "rules": sorted(RULE_FILES.keys()),
            "skills": sorted(SKILL_FILES.keys()),
            "specs": sorted(SPEC_FILES.keys()),
        },
        "inventory": collect_inventory(output_dir),
    }
    write_file(output_dir / "MANIFEST.json", json.dumps(manifest, indent=2))

    if create_links:
        maybe_link(repo, ".agents", output_dir / "agents")
        maybe_link(repo, ".claude", output_dir / "claude")

    return output_dir


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a repository harness")
    parser.add_argument("--repo", default=".", help="Repository root path")
    parser.add_argument("--output-dir", default=".ai-context", help="Harness folder")
    parser.add_argument("--wizard", action="store_true", help="Enable interactive wizard")
    parser.add_argument("--project-name", help="Project name override")
    parser.add_argument("--project-type", help="Project type override")
    parser.add_argument("--primary-stack", help="Primary stack override")
    parser.add_argument(
        "--strictness",
        default="balanced",
        choices=["balanced", "strict"],
        help="Protocol strictness",
    )
    parser.add_argument("--no-symlinks", action="store_true", help="Skip root symlinks")
    parser.add_argument("--force", action="store_true", help="Allow non-empty output directory")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo = Path(args.repo).resolve()
    if not repo.exists() or not repo.is_dir():
        raise SystemExit(f"Invalid repository path: {repo}")

    profile = build_profile(repo, wizard=args.wizard, args=args)
    output_dir = generate(
        repo=repo,
        output_rel=args.output_dir,
        profile=profile,
        create_links=not args.no_symlinks,
        force=args.force,
    )

    print("Harness generated successfully")
    print(f"Path: {output_dir}")
    print("Next: python3 .ai-context/scripts/validate_harness.py --repo . --harness .ai-context")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
