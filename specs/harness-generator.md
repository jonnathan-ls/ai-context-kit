---
name: harness-generator
version: 0.1.0
description: Skill to generate a portable MD-only repository harness under .ai-context with wizard-driven inputs.
status: draft
tags: harness, protocol, skills, rules, specs
---

# Harness Generator Spec

## Scope

- Create a new skill named `harness-generator`.
- Generate repository harness structure under `.ai-context`.
- Provide a wizard-driven interview flow to capture protocol requirements.
- Produce core rules, skills, specs, manifest, and validation checklist (MD-only).
- Provide AI-first output format (`MANIFEST` + `FILE:` blocks + plan + validation).

## Non-scope

- Deep stack-specific scaffolding beyond core protocol files.
- MCP server runtime for dynamic context delivery.
- Automatic update/merge of existing user-authored harness content.
- Scripted generation or validation.

## Acceptance Criteria

- AI output defines the harness using `FILE:` blocks with full content.
- Generated harness includes rules, skills, specs, config, and manifest.
- Validation checklist is included in the AI output.
- Output is concise and focused on senior engineering protocol behavior.
- The wizard flow collects all required inputs before generation.

## Implementation Notes

- Keep templates short to control context budget.
- Do not rely on scripts or external tooling.
- Avoid mutating unrelated files outside target harness.

## Validation

- Check that the AI output includes MANIFEST + FILE blocks + change plan.
- Confirm the harness structure is complete and minimal.
- Confirm the validation checklist is present and actionable.
