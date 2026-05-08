---
version: 1.0.0
name: intent-expander
description: Expands short/vague requests into an implementation-ready mini-spec aligned with the repo conventions.
allowed-tools: Read, Glob, Grep
tags: spec, planning, quality
---

# Intent Expander

Translate vague user input (e.g., “add a button”) into a concrete, testable mini-spec.

## When to Use

- The request is too short to implement safely.
- Multiple UI/behavior interpretations exist.
- The user describes outcomes but not details.

## Expansion Workflow

1. **Restate the outcome** (1 sentence)
2. **Identify ambiguities** that affect implementation
3. **Ask up to 2 questions** (Socratic Gate)
4. **Read the local design system / conventions**
   - Search for existing components/tokens/patterns before inventing new ones.
5. Produce a **mini-spec** (below)

## Mini-Spec Template

```markdown
## Mini Spec

- Goal:
- User-facing behavior:
- States & edge cases:
- Accessibility:
- Non-goals:
- Files likely touched:
- Validation:
```

## Anti-Patterns

- Designing new UI patterns without checking existing components.
- Coding directly from a vague request without clarifying questions.
- Expanding scope beyond what the user asked.
