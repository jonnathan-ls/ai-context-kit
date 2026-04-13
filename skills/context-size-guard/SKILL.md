---
version: 1.0.0
name: context-size-guard
tag: meta
description: Visual, declarative tracking of .ai-context artifact sizes. KB measurements are listed in ALWAYS.md apontamentos. Before loading agents/skills, model checks cumulative KB (P0 baseline + new artifacts). Emits label and blocks > 80 KB until user authorizes.
---

# Context Size Guard

Explicit, readable tracking of context consumption. All KB sizes are pre-calculated
and published in ALWAYS.md (see **Context Size Audit** section). The model reads
these on every prompt and calculates cumulative load before deciding to load agents or skills.

## Thresholds

| Status | Total KB | Action |
|--------|----------|--------|
| 🟢 Safe   | ≤ 40 KB  | Continue normally |
| 🟡 Warn   | 41–80 KB | Continue with yellow label — alert user |
| 🔴 Block  | > 80 KB  | **Stop and request user authorization before proceeding** |

## KB Baseline

**P0 rules: ~48 KB** (always loaded, listed in ALWAYS.md)

## When You Load an Agent or Skill

1. Check its KB size in ALWAYS.md apontamentos
2. Calculate: **48 KB (baseline) + agent/skill KB**
3. If total ≤ 80 KB → load normally
4. If 41–80 KB → emit yellow label, continue
5. If > 80 KB → emit red block message and ask user before proceeding

## Output Label Format

**Green (safe):**
```
🟢 Context load: 56 KB (safe)
  Baseline: 48 KB | backend-specialist: 12 KB
```

**Yellow (warn):**
```
🟡 Context load: 78 KB (above recommended limit)
  Baseline: 48 KB | app-builder: 8 KB | orchestrator: 14 KB
  → Ask user: continue anyway?
```

**Red (block):**
```
🔴 Context load: 95 KB (EXCEEDS LIMIT — requires authorization)
  Baseline: 48 KB | remotion-best-practices: 8 KB | game-developer: 14 KB + other skills
  
→ Stop here. Output:

**Context overload detected.** This request would load 95 KB of artifacts.
The safe limit is 80 KB. This may degrade reasoning and waste tokens.

**Authorize anyway?** Reply `yes` / `authorize` to continue, or tell me which artifacts to skip.
```

## Key Principle

No hidden scripts. The model **sees the KB measurements in the rules** and acts
on them declaratively. Enforcement is transparent and always visible.
