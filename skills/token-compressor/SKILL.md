---
version: 1.0.0
name: token-compressor
description: Deterministically compresses long logs/text into high-signal excerpts to free context window.
allowed-tools: Read, Bash, Grep
tags: token, compression
---

# Token Compressor

This skill reduces token overhead by compressing bulky inputs (logs, stack traces, long docs) while preserving evidence.

## When to Use

- The user pastes long logs.
- Tool output is huge.
- A file is too large to read fully.

## Compression Rules (Deterministic)

Apply these tactics in order:

1. **Keep evidence lines**
   - Always keep lines matching: `error`, `exception`, `traceback`, `fail`, `warning`, `fatal`.

2. **Keep structure**
   - Keep the first N lines (header/context) and last M lines (final error).

3. **Deduplicate noise**
   - Collapse repeated consecutive lines.
   - Collapse repeated blocks (same line repeated many times).

4. **Summarize the rest**
   - Replace large omitted blocks with a short note: `(… 3,421 lines omitted …)`.

## Tooling

If available, use the bundled compressor script:

```bash
python3 ~/.ai-context/skills/token-compressor/scripts/compress_text.py --help
```

## Output Format

```markdown
## Compressed Context

- Source: …
- Original: X lines
- Kept: Y lines
- Notes: …

```text
…compressed excerpt…
```
```

## Anti-Patterns

- Removing the exact error line.
- Keeping only a summary with no evidence.
- Dumping the entire log into the reasoning window.
