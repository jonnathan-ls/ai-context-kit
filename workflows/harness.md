---
description: Context harness command. Runs a pre-flight checklist before moderate/complex work to prevent missing-context errors.
---

# /harness - Context Harness (Pre-Flight)

$ARGUMENTS

---

## Purpose

Use `/harness` to run a **pre-flight context checklist** before implementing moderate/complex tasks. The goal is to:

- Prevent missing-context hallucinations
- Reduce wasted token spend
- Require a clear end state and validation plan

---

## Behavior

When `/harness` is triggered:

1. Identify the request type (question vs task) and complexity.
2. If moderate/complex, apply `context-validator` and produce a PASS/WARN/BLOCK report.
3. If the task is non-trivial, enforce a minimal spec gate (`spec-enforcer`).
4. Propose the smallest validation step (errors/tests/build).

---

## Output Format

```markdown
## Context Harness

Status: PASS | WARN | BLOCK

- Goal: …
- Scope: …
- Missing: …
- Files to read next (top 3): …
- Spec: present | missing
- Validation: …
```

---

## Examples

```
/harness implement token-compressed log pipeline
/harness refactor CLI sync command
/harness investigate failing tests
```
