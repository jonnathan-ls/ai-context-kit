---
version: 1.0.0
name: spec-enforcer
description: Enforces “spec before code” on non-trivial tasks; blocks implementation until a spec exists.
allowed-tools: Read, Write, Glob, Grep
tags: spec, harness, safety
---

# Spec Enforcer

This skill enforces Specification-Driven Development (SDD): **no non-trivial code without a spec**.

## When to Enforce

Enforce a spec when the task is any of:

- multi-file
- new feature / refactor
- behavior changes with user impact
- integration with external services
- high-risk (security, money, data loss)

## What Counts as a Spec

A spec is a Markdown file (recommended under `specs/`) that includes:

- **Scope** / **Non-scope**
- **Acceptance criteria**
- **Key decisions** (trade-offs if relevant)
- **Validation plan**

## Enforcement Protocol

1. If no spec exists:
   - Create a minimal spec (or ask the user for approval to create it).
   - Do not implement yet.
2. If a spec exists:
   - Ensure every change maps to an acceptance criterion.
3. If the user insists on skipping the spec:
   - Proceed only for trivial changes (single-file, low-risk).

## Minimal Spec Template

```markdown
---
name: <spec-name>
version: 0.1.0
description: <one-line>
status: draft
---

# <Title>

## Scope

## Non-scope

## Acceptance Criteria

## Implementation Notes

## Validation
```
