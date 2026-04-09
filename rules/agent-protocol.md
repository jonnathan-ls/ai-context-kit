---
priority: P0
trigger: always_on
description: Agent & skill loading protocol — P0/P1/P2 enforcement, routing, activation checklist
---

# Agent Protocol

## Activation Principle

Agent activation is conditional, not mandatory.

- Question or simple task: execute directly.
- Specialized domain task: use one best-fit agent.
- Multi-domain task: use `orchestrator` or parallel subagents.

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

## Routing Flow

1. Classify request complexity and domain.
2. Decide if an agent is needed.
3. If needed, load only the selected agent file.
4. Read only relevant sections for the current task.
5. Execute.

## Skill Loading Rules

- Start with zero skills.
- Load a skill only when it clearly improves execution quality.
- Load at most 1-2 skills initially.
- Do not read full skill folders by default.

## Activation Announcement

```
> 🤖 **{agent-name}** · 🎯 **{skill-or-task}**
```

- Announce only when an agent is actually activated.
- For direct execution, skip announcement.

## Conflict Resolution

- Rule priority remains `P0 > P1 > P2`.
- When conflicts occur, choose the smallest safe scope of action.
