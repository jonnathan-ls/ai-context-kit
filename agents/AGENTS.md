# Agent Discovery Index

Quick reference for selecting the right agent. Maintained alongside `ALWAYS.md`.

## Routing Table

| Agent | Domain | Trigger Keywords | Tools | Primary Skills |
|-------|--------|------------------|-------|----------------|
| `backend-specialist` | Server / API | backend, server, api, endpoint, database, auth | R/W | nodejs-best-practices, python-patterns, api-patterns, database-design |
| `code-archaeologist` | Legacy / Refactor | legacy, refactor, spaghetti code, analyze repo, explain codebase | R/W | refactoring-patterns, code-review-checklist |
| `database-architect` | Database | database, sql, schema, migration, query, postgres, index, table | R/W | database-design |
| `debugger` | Bug / Error | bug, error, crash, not working, broken, investigate, fix | R/W | systematic-debugging |
| `devops-engineer` | Deployment | deploy, production, server, pm2, ssh, release, rollback, ci/cd | R/W | deployment-procedures, server-management |
| `documentation-writer` | Docs | README, API docs, changelog — **explicit request only** | R/W | documentation-templates |
| `explorer-agent` | Discovery | audit, investigate, analyze repo, architecture overview | Read+special | architecture, plan-writing |
| `frontend-specialist` | UI / Frontend | component, react, vue, ui, ux, css, tailwind, responsive | R/W | react-best-practices, tailwind-patterns, frontend-design |
| `game-developer` | Games | unity, godot, unreal, phaser, three.js, game engine, 2d, 3d, vr | R/W | game-development |
| `mobile-developer` | Mobile | mobile, react native, flutter, ios, android, app store, expo | R/W | mobile-design |
| `orchestrator` | Multi-agent | complex, multi-domain, orchestrate, parallel, coordinate | R/W+Agent | parallel-agents, architecture |
| `penetration-tester` | Offensive Security | pentest, exploit, attack, hack, breach, pwn, redteam, offensive | R/W | vulnerability-scanner, red-team-tactics |
| `performance-optimizer` | Performance | performance, optimize, speed, slow, memory, cpu, benchmark, lighthouse | R/W | performance-profiling |
| `product-manager` | Product / Requirements | requirements, user story, acceptance criteria, product specs | Read | plan-writing, brainstorming |
| `product-owner` | Strategy / Backlog | backlog, MVP, PRD, stakeholder, roadmap | Read | plan-writing, brainstorming |
| `project-planner` | Planning | plan new project, major feature, file structure, dependency graph | Read | app-builder, plan-writing |
| `qa-automation-engineer` | E2E / Automation | e2e, automated test, pipeline, playwright, cypress, regression | R/W | webapp-testing, testing-patterns |
| `security-auditor` | Defensive Security | security, vulnerability, owasp, xss, injection, auth, encrypt, supply chain | R/W | vulnerability-scanner, red-team-tactics |
| `seo-specialist` | SEO / GEO | seo, lighthouse, core web vitals, e-e-a-t, AI search, citation | R/W | seo-fundamentals, geo-fundamentals |
| `test-engineer` | Testing / TDD | test, spec, coverage, jest, pytest, playwright, e2e, unit test | R/W | testing-patterns, tdd-workflow |

> **R/W** = Read, Grep, Glob, Bash, Edit, Write

## Selection Rules

- **Single domain** → use one best-fit agent from the table above
- **Multi-domain** (e.g., security + backend + deploy) → use `orchestrator`
- **Unclear domain** → load `intelligent-routing` skill to resolve
- **No agent needed** → text-only questions, small targeted edits

## Agent Overlap Reference

When two agents seem relevant, use this to decide:

| Scenario | Choose |
|----------|--------|
| Fix a bug in backend code | `debugger` |
| Refactor legacy backend architecture | `code-archaeologist` |
| Build a new API endpoint from scratch | `backend-specialist` |
| Deploy the API to production | `devops-engineer` |
| Audit API for security vulnerabilities | `security-auditor` |
| Actively exploit a vulnerability | `penetration-tester` |
| Add tests for the API | `test-engineer` |
| Run E2E test suite in CI | `qa-automation-engineer` |
| Write tests with TDD from scratch | `test-engineer` |
| Define what the API should do | `product-manager` |
| Prioritize which APIs to build | `product-owner` |
| Plan the full API project | `project-planner` |

## Maintenance

This file is maintained manually. After adding or updating agents, run:

```bash
aictx sync
```
