---
version: 1.0.0
name: remotion-concept-builder
description: Use when building or iterating on Remotion VFX concept compositions for the channel. Covers concept schema, brand identity, VFX catalog, and iterative workflow. Triggers on: concept, vfx, composition, visual fx, schema, iteração, conceito visual, narrativa.
metadata:
  tags: remotion, vfx, concept, brand, channel
---

## When to use

Load this skill whenever the user asks to create, modify, or iterate on a VFX concept composition for the channel.

## Process

1. Read [rules/workflow.md](rules/workflow.md) — understand the full concept-to-render lifecycle
2. Read [rules/brand.md](rules/brand.md) — never guess colors, fonts, or grades
3. Read [rules/schema.md](rules/schema.md) — fill ConceptSchema correctly
4. Read [rules/vfx-catalog.md](rules/vfx-catalog.md) — choose effects from catalog only

## Hard rules

- Never hardcode colors or fonts — always use Brand values from `src/lib/brand.ts`
- Never create a VFX component inside a composition — if it has reuse potential, it goes in `src/lib/vfx/`
- Each composition has exactly 2 files: `concept.ts` and `index.ts`
- New compositions go in `src/compositions/_active/` — never directly in `src/compositions/`
- After rendering, the composition moves to `src/compositions/_archive/` (gitignored)
- For iteration requests (visual feedback), only modify `concept.ts` — never touch the template
