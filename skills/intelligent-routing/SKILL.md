---
name: intelligent-routing
description: Automatic agent selection and intelligent task routing. Use this skill on every user request to silently analyze intent, detect domains, assess complexity, and select the best specialist agent without requiring explicit user commands. Triggers automatically — no user keyword needed. Handles single-domain tasks (direct agent), multi-domain tasks (orchestrator), and edge cases like vague requests or contradictory signals. Always announces the selected agent before responding.
---

# Intelligent Routing

Automatic project manager. Analyzes every user request and selects the best specialist agent without requiring explicit commands — silently, before the first response word.

## Execution Protocol (Every Request)

Apply these steps before responding to any request:

1. **Classify** — Determine request type (question, task, plan, review).
2. **Detect domains** — Match keywords to domain categories.
3. **Assess complexity** — Simple (1 domain), moderate (2 domains), complex (3+ or unclear).
4. **Select agent(s)** — Use the matrix below.
5. **Announce** — Output the agent label before the response.
6. **Respond** — Deliver with the selected specialist's knowledge applied.

Never skip step 5. Transparent selection builds trust and is easy to override.

## Agent Selection Matrix

| Intent | Keywords | Agent(s) |
|--------|----------|----------|
| Authentication / Security | login, auth, jwt, password, hash, token, session | `security-auditor` + `backend-specialist` |
| UI / Components | button, card, layout, component, style, CSS, React, Vue | `frontend-specialist` |
| Mobile | screen, navigation, touch, gesture, React Native, Flutter, iOS, Android | `mobile-developer` |
| API / Server | endpoint, route, API, REST, POST, GET, express, fastapi | `backend-specialist` |
| Database | schema, migration, query, table, SQL, Prisma, MongoDB | `database-architect` |
| Bug / Error | error, bug, broken, not working, crash, fix, issue | `debugger` |
| Tests | test, coverage, unit, e2e, jest, vitest, playwright, cypress | `test-engineer` |
| Deployment | deploy, production, CI/CD, docker, nginx, pm2, release | `devops-engineer` |
| Vulnerability | security review, vulnerability, exploit, pentest, OWASP | `security-auditor` + `penetration-tester` |
| Performance | slow, optimize, performance, speed, cache, lag | `performance-optimizer` |
| Requirements | user story, backlog, MVP, requirements, acceptance criteria | `product-owner` |
| SEO / Analytics | SEO, meta, sitemap, robots, analytics, ranking | `seo-specialist` |
| Game Dev | unity, godot, phaser, game, multiplayer | `game-developer` |
| Architecture | design system, architecture, scale, trade-off, ADR | `orchestrator` |
| New Feature / Build | build, create, implement, new app, scaffold | `orchestrator` → ask first |
| Multi-domain | 2+ categories detected | `orchestrator` |

## Complexity Assessment

| Level | Signals | Action |
|-------|---------|--------|
| **Simple** | Single file, one domain, clear task | Auto-invoke single agent |
| **Moderate** | 2 files, 2 domains max, clear requirements | Auto-invoke 2 agents sequentially |
| **Complex** | 3+ domains, unclear requirements, architectural decisions | Auto-invoke `orchestrator` |

## Announcement Format

Always emit before the response body:

```
> 🤖 **frontend-specialist** · 🎯 **nextjs-react-expert**
```

If multiple agents: list all on one line.
If no domain agent applies: omit the label entirely.

## Edge Cases

| Situation | Handling |
|-----------|----------|
| Generic question ("how does X work?") | Answer directly, no agent label |
| Vague request ("make it better") | Apply Socratic Gate — ask 1-2 targeted questions first |
| Contradictory signals ("add mobile to the web app") | Ask: "Responsive web or native mobile app?" |
| User explicitly names an agent | Override auto-selection, use what the user specified |
| Unclear domain after analysis | Default to `orchestrator` |

## Interaction Rules

| Do | Avoid |
|----|-------|
| Analyze silently before responding | Announcing "I'm analyzing your request..." |
| Inform which agent is being applied | Verbose meta-commentary |
| Override when user specifies an agent | Ignoring explicit user preferences |
| Fall back to orchestrator for complex tasks | Guessing on multi-domain without orchestration |

## Integration

- **Socratic Gate**: Auto-routing does not bypass it. Vague or destructive requests still require clarification first.
- **P0 Rules**: Always processed before routing — routing happens after P0 gates pass.
- **CLAUDE.md / ALWAYS.md**: Explicit routing rules there override intelligent-routing defaults.

## Anti-Patterns

- **Do not** skip the announcement step — users should know which expertise is being applied.
- **Do not** route to `orchestrator` for simple, single-domain tasks — it adds unnecessary overhead.
- **Do not** auto-invoke multi-agent for tasks that are actually simple but use technical vocabulary.
- **Do not** ignore explicit agent mentions from the user — they always override auto-selection.
- **Do not** attempt routing on pure conversational messages with no actionable task.
