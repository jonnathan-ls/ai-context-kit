---
version: 1.0.0
name: memory-curator
description: Governs what to store as user/session/repo memory while preventing noisy or sensitive memories.
allowed-tools: Read, Write
tags: memory, privacy, token
---

# Memory Curator

Store only durable, high-signal facts and avoid unsafe or noisy memory.

## What to Store

- Stable user preferences (formatting, constraints, recurring workflows)
- Repo conventions (build commands, code style, common paths)
- Proven fixes or lessons that are likely to repeat

## What NOT to Store

- Secrets (API keys, tokens, passwords)
- Personal data (emails, phone numbers, addresses)
- One-off debugging details unlikely to recur
- Large blobs (logs, long code)

## Hygiene Rules

- Prefer short bullet notes.
- Avoid duplication — update existing memory.
- If uncertain whether it is sensitive: do not store.

## Output

When creating memory, write it as a compact fact with a clear scope:

- user: preference
- repo: convention
- session: temporary plan/state
