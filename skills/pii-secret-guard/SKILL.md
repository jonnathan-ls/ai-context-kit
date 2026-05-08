---
version: 1.0.0
name: pii-secret-guard
description: Detects and redacts secrets/PII before adding logs/files to prompts or memory.
allowed-tools: Read, Grep, Bash
tags: safety, privacy
---

# PII & Secret Guard

Prevent accidental leakage of sensitive data when copying logs, configs, or code into prompts or memory.

## What to Detect

- API keys, access tokens, private keys
- Passwords and connection strings
- Email addresses, phone numbers, addresses
- Internal hostnames or proprietary endpoints (when not required)

## Redaction Rules

- Replace sensitive substrings with `REDACTED`.
- Preserve structure (so debugging remains possible).
- Never store secrets in long-term memory.

## Heuristics (Common Patterns)

- `-----BEGIN (RSA|OPENSSH|EC) PRIVATE KEY-----`
- `AKIA...` (AWS access keys)
- `xox[pbar]-` (Slack tokens)
- `ghp_` / `github_pat_` (GitHub tokens)
- `.env` style lines: `KEY=...`, `TOKEN=...`, `PASSWORD=...`

## Anti-Patterns

- Posting full `.env` files.
- Copying entire cloud credentials blocks.
- Saving secrets in repo/user memory.
