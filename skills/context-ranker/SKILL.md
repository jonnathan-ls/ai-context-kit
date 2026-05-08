---
version: 1.0.0
name: context-ranker
description: Ranks candidate files and decides what to read first using workspace-map and lightweight heuristics.
allowed-tools: Read, Glob, Grep
tags: workspace, context, token
---

# Context Ranker

Use this skill to reduce token waste by **reading fewer files, earlier**.

## Core Principle

Start from the smallest evidence that can confirm/deny a hypothesis.

## Workflow

1. **Start with the workspace map**
   - Read `.ai-context/workspace-map.json` (first ~200 lines).
   - Use `summary.line_guide` to jump directly to file metadata.

2. **Generate candidates**
   - Prefer files explicitly named by the user.
   - Otherwise, shortlist by keyword matching in filenames and directories.

3. **Rank (Top-K)**

Score files by:

- name match (strong)
- directory relevance (medium)
- description/type match (medium)
- size penalty (prefer smaller)

Default K:

- simple task: 1–3 files
- moderate: 3–5 files
- complex: 5–8 files (only with strong justification)

4. **Read surgically**
   - Start with the smallest relevant range.
   - Expand only when needed.

## Output Format

```markdown
## Context Ranking

Top files to read next:
1. path/to/file.ext — why
2. path/to/file.ext — why
3. path/to/file.ext — why
```

## Anti-Patterns

- Reading many files before forming a hypothesis.
- Searching broadly before consulting the workspace map.
- Re-reading the same large file multiple times.
