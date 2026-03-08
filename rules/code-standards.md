---
priority: P0
trigger: always_on
description: Clean Code standards, file awareness, task complexity tiers
---

# Code Standards

## Clean Code — Non-Negotiable Rules

| Rule | Description |
|------|-------------|
| **Single Responsibility** | Every function/class does one thing only |
| **Meaningful Names** | Variables, functions, files named by intent — no abbreviations |
| **No Magic Numbers** | Constants with names, never raw values inline |
| **Early Returns** | Avoid deep nesting — return/throw early |
| **Max Function Size** | ~20 lines. If larger → extract |
| **No Dead Code** | No commented-out blocks, unused imports, orphan vars |
| **Consistent Style** | Match the project's existing style — do not impose a new one |

## File Awareness (MANDATORY before any edit)

Before touching any file:
1. **Read** the full file or at minimum the section you'll modify
2. **Understand** what exists — do not overwrite without knowing context
3. **Scope** — only change what was requested. No drive-by refactors
4. **Imports** — verify all imports/deps exist before writing code that uses them

## Task Complexity Tiers

| Tier | Signals | Required Action |
|------|---------|-----------------|
| **0 — Question** | "what is", "explain", "why" | Text only — no code |
| **1 — Simple** | Single file, < 20 lines change | Inline edit |
| **2 — Moderate** | Multiple files, clear scope | Plan summary → edit |
| **3 — Complex** | New feature, architecture, refactor | Agent + Skill → phased plan → implement |

## Before Writing Code

```
[ ] Do I understand the full task scope?
[ ] Have I read the file(s) I will edit?
[ ] Does this change match the project's language/framework/style?
[ ] Are all required dependencies available?
[ ] Am I only changing what was requested?
```

## Forbidden Patterns

- ❌ Hallucinating APIs or methods that don't exist
- ❌ Changing files not mentioned in the request
- ❌ Installing packages without explicit approval
- ❌ Adding features the user didn't ask for
- ❌ Refactoring code outside the task scope
