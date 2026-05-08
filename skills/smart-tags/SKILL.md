---
version: 1.0.0
name: smart-tags
description: Tag-based context selection to reduce tokens by loading only the rule/skill fragments relevant to the current request.
allowed-tools: Read, Glob, Grep
tags: token, routing, smart-tags
---

# Smart Tags (Dynamic Context Selection)

Smart Tags provide a lightweight mechanism for **selecting the minimum necessary context** for a request.

The core idea:

- Treat rules/skills as *addressable modules*.
- Assign tags (`tags:` in frontmatter).
- Load only what matches the request tags + core baseline.

## Tag Taxonomy (Recommended)

- `core` — always relevant behavioral constraints
- `routing` — agent/skill activation and orchestration
- `safety` — destructive operations, ambiguity gates
- `token` — budgeting, compression, context efficiency
- `workspace` — repo navigation and mapping
- `quality` — clean code, correctness, evidence
- `spec` — spec creation/enforcement

Domain tags (optional): `frontend`, `backend`, `tests`, `security`, `docs`, `devops`, `data`.

## Selection Algorithm

1. **Always include**: `core` (and language policy if applicable).
2. Detect request domains → add domain tags.
3. If request is long/noisy → add `token` and apply compression.
4. If task is moderate/complex → add `harness` + `spec`.
5. If repo navigation is required → add `workspace`.

## Practical Rules

- Prefer **file-level selection** first (pick which rules/skills to load).
- Use **section-level selection** only when a file is large.
- Never load more than you can justify.

## Output Format

```markdown
## Smart Tags

- Selected tags: core, token, workspace
- Included rules: response-discipline, workspace-guard
- Included skills: token-management, context-ranker
- Excluded: backend/security/etc (not relevant)
```

## Anti-Patterns

- Loading “everything” because it might help.
- Adding tags after you already started coding.
- Selecting tags that don’t change decisions.
