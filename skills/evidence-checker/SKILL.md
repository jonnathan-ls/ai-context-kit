---
version: 1.0.0
name: evidence-checker
description: Requires evidence (errors/tests/build) before claiming a fix is complete.
allowed-tools: Read, Grep, Bash
tags: quality, verification, safety
---

# Evidence Checker

Use this skill to prevent unverified claims and improve correctness.

## Evidence Hierarchy

Pick the smallest credible evidence for the change:

1. **Static**: `get_errors`, typecheck, lint
2. **Targeted tests**: unit/integration tests for touched modules
3. **Runtime smoke**: start app / run one critical flow

## Protocol

- Before finishing, answer:
  - What did I change?
  - What evidence shows it works?
  - What risk remains?

If you cannot validate:

- Say so explicitly.
- Provide the exact command(s) the user should run.

## Anti-Patterns

- “Should work” without evidence.
- Running the full test suite when a targeted test is enough.
- Fixing unrelated failures.
