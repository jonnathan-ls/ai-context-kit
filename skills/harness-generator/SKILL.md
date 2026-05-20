---
version: 1.0.0
name: harness-generator
description: Generates a portable repository-level harness under .ai-context using an interactive wizard, hybrid rule/skill selection, and deterministic validation scripts. Use this whenever the user wants a repository protocol that guides AI execution with senior-level quality, safety, and performance without depending on this source AI-Context.
allowed-tools: Read, Write, Bash, Glob, Grep
tags: harness, protocol, quality, safety, architecture, performance
---

# Harness Generator

Use this skill to create a clean, portable harness for a repository.

The harness is generated under `.ai-context` in the target repository and is designed to work standalone.

## When to use

- The user wants a protocol to guide future AI requests.
- The repository does not yet have a structured rules/skills/specs layout.
- The user asks for repeatable quality and safety gates.
- The user wants a lean setup that avoids context bloat.

## What this skill creates

- `.ai-context/rules/` with core governance rules.
- `.ai-context/skills/` with core operational skills.
- `.ai-context/specs/` with templates and integration guidance.
- `.ai-context/scripts/validate_harness.py` for deterministic checks.
- `.ai-context/MANIFEST.json` and `.ai-context/config/token-budget.json`.
- Optional symlinks at repo root:
  - `.agents` -> `.ai-context/agents`
  - `.claude` -> `.ai-context/claude`

## Execution flow

1. Run the generator in wizard mode.
2. Confirm hybrid selection defaults.
3. Generate harness artifacts.
4. Run validation script.
5. Fix WARN/BLOCK items before relying on the harness.

## Command

```bash
python3 skills/harness-generator/scripts/generate_harness.py --repo . --wizard
```

## Validation command

```bash
python3 .ai-context/scripts/validate_harness.py --repo . --harness .ai-context
```

## Output contract

The generated `MANIFEST.json` includes:

- project profile (type, stack, strictness)
- selected rules and skills
- file inventory for generated artifacts
- version and timestamp

## Blocking conditions

Stop and ask for confirmation when:

- target path already contains unrelated files
- symlink destination conflicts with existing non-symlink paths
- required metadata cannot be derived from the repository

## Anti-patterns

- Generating every available skill "just in case".
- Copying bulky references without a clear trigger.
- Skipping validation and claiming the harness is production-ready.
