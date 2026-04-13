# Context Size Guard (P0)

## Purpose

Track and measure the total KB of every `.ai-context` artifact being loaded for
the current prompt — rules, agents, skills, workflows — and emit a transparent
summary label. Block processing when the load exceeds safe thresholds until the
user grants explicit authorization.

Enforcement is **declarative and visual**: the model sees explicit KB measurements
in the ALWAYS.md apontamentos and acts on them. No hidden scripts or hooks.

## Thresholds

| Status | Threshold | Action |
|--------|-----------|--------|
| 🟢 Safe   | ≤ 40 KB cumulative | Continue normally |
| 🟡 Warn   | 41–80 KB cumulative | Continue with yellow label — alert user |
| 🔴 Block  | > 80 KB cumulative | Stop and request user authorization before proceeding |

## How It Works

1. **P0 rules baseline** — Always loaded, ~48 KB total (listed in ALWAYS.md)
2. **Selected agent** — Check size in apontamentos before loading
3. **Skills to load** — Check size in apontamentos before calling Skill tool
4. **Workflow invocation** — Check size in apontamentos before invoking

The cumulative total of all these determines whether to proceed or block.

## Measurement Method

Use simple shell commands to display KB of artifacts:

```bash
# P0 rules baseline
du -sk .ai-context/rules/*.md

# Before loading an agent
du -sk .ai-context/agents/agent-name.md

# Before loading a skill
du -sk .ai-context/skills/skill-name/SKILL.md
```

The model **reads these sizes from ALWAYS.md apontamentos** (they are updated
regularly) and calculates cumulative total before loading anything.

## Thresholds

| Status | Threshold | Action |
|--------|-----------|--------|
| 🟢 Safe   | ≤ 40 KB  | Emit green label — continue normally |
| 🟡 Warn   | 41–80 KB | Emit yellow label — continue with note |
| 🔴 Block  | > 80 KB  | Emit red label — **stop and request user authorization** |

## Required Output Label

Emit the label returned by the script at the **top of every response**, before
any other content:

```
🟢 Context load: 12.4 KB (within safe limit)
```

The label must always be present, even on green (safe) results, so the user
can always see how much context was loaded.

## Block Protocol

When the script exits with code `2` (block threshold exceeded):

1. Output the red label with the per-file breakdown.
2. Present the authorization prompt:

   > **Context overload detected.** Loading these artifacts would consume
   > **{total_kb} KB**, exceeding the safe limit of 80 KB.
   >
   > This may cause reasoning degradation and unnecessary token consumption.
   >
   > **Authorize anyway?** Reply `yes` to continue or `no` to cancel.
   > Alternatively, tell me which artifacts to drop.

3. Do **not** read or process any artifact until the user explicitly authorizes
   (`yes` / `proceed` / `authorize`).
4. If denied: respond using only what is already in memory (no new artifact
   reads) and inform the user what was skipped.

## Performance Notes

- The measurement script only calls `os.path.getsize()` — it does **not** read
  file content, so it has zero impact on context.
- Run once per prompt. Do not re-measure mid-response.
- If the script is unavailable (missing/broken), emit a fallback label:
  `⚠️ Context load: size unknown (measure_context.py unavailable)` and continue.

## Skill Reference

Full orchestration details: `skills/context-size-guard/SKILL.md`
