---
version: 1.0.0
name: query-router
description: Maps a user request to intent, domains, Smart Tags, and the minimal set of agents/skills to load.
allowed-tools: Read, Glob, Grep
tags: routing, token
---

# Query Router

This skill standardizes how to translate an unstructured user request into an actionable execution brief.

## Inputs

- User request text
- Environment constraints (OS, repo, tooling)
- Project conventions (rules and active skills)

## Routing Steps

1. **Intent**: question | task | plan | review
2. **Domains**: frontend | backend | tests | security | devops | docs | architecture
3. **Complexity**:
   - simple: 1 domain, clear scope
   - moderate: 2 domains or multiple files
   - complex: 3+ domains or ambiguous
4. **Smart Tags**: select minimal tags needed.
5. **Agent & Skills**: choose minimal agent/skills set that changes implementation decisions.
6. **Harness**: for moderate/complex, run `context-validator` pre-flight.

## Output Format

```markdown
## Routing Result

- Intent: …
- Domains: …
- Complexity: …
- Tags: …
- Agent(s): …
- Skills to load: …
- Clarifying questions (0–2): …
```

## Notes

- Favor fewer skills. If you can do it well without loading a skill, skip it.
- If the request is “build/implement/refactor” and no spec exists, route to `spec-normalizer`/`sdd-expert` before code.
