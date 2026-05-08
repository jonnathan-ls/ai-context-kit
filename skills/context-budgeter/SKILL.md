---
version: 1.0.0
name: context-budgeter
description: Enforces token/read budgets per phase to prevent context bloat and keep execution efficient.
allowed-tools: Read, Glob, Grep, Bash
tags: token, budgeting
---

# Context Budgeter

Use this skill to keep context usage predictable and prevent runaway token costs.

## Budget by Phase

### Discovery

- Goal: remove ambiguity with minimal reads
- Default budget:
  - 1–3 files
  - 50–200 lines each
  - Prefer workspace map + targeted reads

### Implementation

- Goal: implement the smallest correct change
- Default budget:
  - read only files you will edit + immediate dependencies
  - avoid broad scans

### Verification

- Goal: evidence-based confidence
- Default budget:
  - run the smallest relevant check (errors/tests/build)
  - avoid full test suites unless needed

## Guardrails

- If you exceed the Discovery budget, stop and:
  - ask 1–2 clarifying questions, or
  - apply compression (see `token-compressor`), or
  - pick a narrower hypothesis and re-rank.

## Output Format

```markdown
## Context Budget

- Phase: Discovery | Implementation | Verification
- Budget: …
- Current spend: …
- Next action: …
```
