---
priority: P0
trigger: always_on
description: Agent & skill loading protocol — P0/P1/P2 enforcement, routing, activation checklist
---

# Agent Protocol

## Two-Layer Loading Protocol

**Layer 1 — Meta-Skills (always first, before any agent):**
`skill-extractor`, `knowledge-integrator`, `study-notes-writer`, `intelligent-routing`

**Layer 2 — Domain Skills (after agent selection via frontmatter):**
Agent activated → read `skills:` frontmatter → read SKILL.md → apply domain rules.

## Enforcement Order (MANDATORY)

```
1. Load Meta-Skills (Layer 1)
2. Classify request (REQUEST CLASSIFIER)
3. Select agent via intelligent-routing
4. Read agent .md + load agent skills (Layer 2)
5. Apply ALL rules
6. Announce: > 🤖 agent-name · 🎯 skill-name
7. Respond
```

**Never skip steps.** Jumping from step 1 to step 7 is a protocol violation.

## Agent Selection Rules

| Signal | Result |
|--------|--------|
| Frontend/UI/React/Next.js | `frontend-specialist` |
| API/server/database/backend | `backend-specialist` |
| Bug/error/broken behavior | `debugger` |
| Performance/optimization | `performance-optimizer` |
| Architecture/system design | `orchestrator` |
| Security/vulnerability | `security-auditor` |
| Tests/QA | `qa-automation-engineer` |
| Documentation | `documentation-writer` |
| Multi-domain | Multiple agents — announce all |
| Unclear | Apply `intelligent-routing` to resolve |

## Activation Announcement Format

```
> 🤖 **{agent}** · 🎯 **{skill}**
```

- Emit **before** the response content, always
- If no domain agent applies: omit the label
- If multiple agents: list all — `> 🤖 **backend-specialist** · 🤖 **security-auditor**`

## Selective Skill Reading

- Read `SKILL.md` first — then only sections relevant to the request
- Do NOT read all files in a skill folder by default
- Rule priority: **P0 > P1 > P2** — higher level always wins conflicts
