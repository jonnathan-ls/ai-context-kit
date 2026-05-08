---
description: Context compaction command. Produces a stable, high-signal summary and compresses bulky logs to reduce context window pressure.
---

# /compact - Context Compaction

$ARGUMENTS

---

## Purpose

Use `/compact` when the conversation is getting long or noisy. The goal is to:

- Reduce context window pressure
- Preserve critical decisions and evidence
- Drop failed attempts and redundant history

---

## When to Use

- After multiple failed iterations or lots of back-and-forth.
- After pasting large logs/tool output.
- Before starting a new but related subtask.

Rule of thumb: compact proactively once the context feels "heavy" (often around ~60%+ full in tools that show usage).

---

## Behavior

1. Preserve the execution kernel:
   - Goal
   - Scope / non-scope
   - Key decisions
   - Files touched / relevant locations
   - Current state (what works / what fails)
2. Keep evidence:
   - Exact error messages
   - Stack traces (compressed)
3. Drop noise:
   - Repeated attempts
   - Verbose explanations that did not change decisions
4. If logs are large, compress them using `token-compressor` rules (keep errors, keep head/tail, mark omissions).

---

## Output Format

```markdown
## Compacted State

- Goal: …
- Scope: …
- Decisions: …
- Evidence: …
- Files/Areas: …
- Next steps: …
- Dropped: …
```

---

## Examples

```
/compact keep only decisions, files edited, and failing error output
/compact focus on tests that passed/failed and the current hypothesis
```
