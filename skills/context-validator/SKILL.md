---
version: 1.0.0
name: context-validator
description: Pre-flight context harness to verify goals, specs, and required files are present before complex work.
allowed-tools: Read, Glob, Grep, Bash
tags: harness, context, token
---

# Context Validator (Context Harness)

Use this skill as a **pre-flight harness** before any moderate/complex task. The goal is to prevent missing-context hallucinations and avoid token-wasting trial-and-error.

## When to Use

Trigger this harness when any of the following is true:

- The request is multi-step, multi-file, or ambiguous.
- The user asks to build/refactor/implement a feature.
- The task involves repo navigation (finding files/symbols).
- The task requires verification (tests/build) or has risk.

## Harness Checklist

### 1) Outcome & Scope

- What is the **end state** (observable result)?
- What is explicitly **out of scope**?
- What does “done” mean (acceptance criteria)?

### 2) Inputs & Constraints

- Identify required inputs: files, APIs, env vars, external services.
- Identify constraints: style rules, formatting, safety/compliance, deadlines.

### 3) Spec Readiness (Spec Gate)

- If the task is non-trivial, confirm a **spec exists** (or create one):
  - Scope / Non-scope
  - Acceptance criteria
  - Key design decisions
  - Validation plan

If no spec exists and the task is non-trivial: **BLOCK** implementation and switch to spec creation.

### 4) Context Sufficiency (Files & Evidence)

- Confirm you have read the **minimum set of files** required to act.
- If you need to navigate the repo:
  - Check `.ai-context/workspace-map.json` first (via Workspace Guard).
  - Prefer targeted reads over broad searches.

### 5) Validation Plan

Pick the smallest credible verification for the change:

- Static checks: lint/typecheck, `get_errors`
- Unit tests / integration tests
- Runtime sanity check

## Blocking Conditions

Mark as **BLOCK** and ask 1–2 targeted questions when:

- The end state is unclear.
- There are multiple valid interpretations.
- Required files/specs are missing.
- The action is destructive or irreversible.

## Output Format

Use this compact report before implementation:

```markdown
## Context Harness

Status: PASS | WARN | BLOCK

- Goal: …
- Scope: …
- Missing: …
- Files to read next (top 3): …
- Validation: …
```

## Anti-Patterns

- Starting implementation without a defined end state.
- Reading many files “just in case”.
- Guessing file locations instead of using the workspace map.
- Claiming completion without a validation step.
