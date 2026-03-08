---
name: refactoring-patterns
description: Safe refactoring techniques — extract, rename, decompose without breaking behavior
version: 1.0.0
---

# Refactoring Patterns

## Purpose

Apply safe, behavior-preserving transformations to existing code. Every refactoring step must leave the code working — no "refactor and fix bugs later."

## Core Rule

> **Never refactor and add features in the same commit.** One thing at a time.

## Technique Catalog

### Extract Function / Method
- When: block of code with a clear purpose buried in a larger function
- How: extract, name by intent, replace original with call
- Validate: same behavior, tests still pass

### Rename (Variable / Function / Class)
- When: name doesn't reflect current purpose
- How: IDE rename (updates all references), never find-replace
- Validate: no broken references, no shadowing

### Decompose Conditional
- When: complex `if/else` chains are hard to read
- How: extract each branch into a named function
- Validate: all branches still reachable, same logic

### Replace Magic Number / String
- When: raw literals in logic code
- How: extract to named constant at top of module
- Validate: all usages updated

### Remove Dead Code
- When: commented-out blocks, unused functions, orphan variables
- How: delete (not comment out) — version control has history
- Validate: no tests reference removed code

### Consolidate Duplicate Logic
- When: same logic appears 2+ times
- How: extract once, parameterize if needed, replace all occurrences
- Validate: edge cases of each call site are covered

## Pre-Refactor Checklist

```
[ ] Tests exist covering the code to be refactored
[ ] I understand what the code currently does
[ ] I can describe the refactoring in one sentence
[ ] The change is purely structural (no behavior change)
[ ] I have a way to verify nothing broke
```

## Anti-Patterns (Never Do)

- ❌ Refactoring without test coverage
- ❌ Renaming across repo with find-replace instead of IDE tooling
- ❌ "Refactoring" that changes behavior
- ❌ Refactoring in a branch that also adds features
- ❌ Extracting functions so small they add no clarity

