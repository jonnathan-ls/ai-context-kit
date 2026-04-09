---
priority: P0
trigger: always_on
description: Clean Code standards, file awareness, task complexity tiers
---

# Code Standards

## Core Rules

| Rule | Description |
|------|-------------|
| **Single Responsibility** | Every function/class does one thing only |
| **Meaningful Names** | Variables, functions, files named by intent — no abbreviations |
| **Early Returns** | Avoid deep nesting — return/throw early |
| **No Magic Numbers** | Replace unexplained literals with named constants |
| **No Dead Code** | No commented-out blocks, unused imports, orphan vars |
| **Consistent Style** | Match the project's existing style — do not impose a new one |

## File Awareness

Before touching any file:
1. Read the target file or section to be changed.
2. Understand existing behavior before editing.
3. Keep scope limited to what was requested.
4. Verify required imports/dependencies exist.

## Task Complexity Tiers

| Tier | Signals | Required Action |
|------|---------|-----------------|
| **0 — Question** | "what is", "explain", "why" | Text only — no code |
| **1 — Simple** | Single file, < 20 lines change | Inline edit |
| **2 — Moderate** | Multiple files, clear scope | Plan summary → edit |
| **3 — Complex** | New feature, architecture, refactor | Agent + Skill → phased plan → implement |

## Pre-Edit Check

```
[ ] Do I understand the full task scope?
[ ] Have I read the file(s) I will edit?
[ ] Does this change match the project's language/framework/style?
[ ] Are all required dependencies available?
[ ] Am I only changing what was requested?
```
