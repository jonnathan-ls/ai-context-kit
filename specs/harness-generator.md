---
name: harness-generator
version: 0.1.0
description: Skill to generate a portable repository harness under .ai-context with symlink integration.
status: draft
tags: harness, protocol, skills, rules, specs
---

# Harness Generator Spec

## Scope

- Create a new skill named `harness-generator`.
- Generate repository harness structure under `.ai-context`.
- Support interactive wizard input for profile capture.
- Produce core rules, skills, specs, manifest, and validation scripts.
- Create root symlinks `.agents` and `.claude` to internal harness paths.

## Non-scope

- Deep stack-specific scaffolding beyond core protocol files.
- MCP server runtime for dynamic context delivery.
- Automatic update/merge of existing user-authored harness content.

## Acceptance Criteria

- Generator script creates deterministic harness structure in target repository.
- Generated harness includes rules, skills, specs, config, and manifest.
- Validation script reports PASS/WARN/BLOCK and exits non-zero on BLOCK.
- Symlink creation is safe and fails on conflicting non-symlink paths.
- Output is concise and focused on senior engineering protocol behavior.

## Implementation Notes

- Keep templates short to control context budget.
- Use only Python standard library.
- Avoid mutating unrelated files outside target harness and optional symlinks.

## Validation

- Run generator against a temporary output path.
- Run generated validator and ensure PASS for valid structure.
- Run validator with broken files and confirm BLOCK behavior.
