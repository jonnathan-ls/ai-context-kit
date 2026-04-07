---
name: app-builder
description: Full-stack application building orchestrator. Use this skill whenever the user wants to build a new application from scratch or add major features to an existing one. Triggers on "build an app", "create a project", "make a SaaS", "scaffold a Next.js app", "build an API", "create a mobile app", "new project", "build a clone of", "start an app from scratch". Detects project type, selects the appropriate tech stack, scaffolds the structure, and coordinates specialist agents for each domain.
---

# App Builder

Full-stack application orchestrator. Translates a natural language request into a concrete project plan, selects the right tech stack, and coordinates specialist agents to build each layer.

## When to Use

- User wants to build a new application from scratch
- User describes an app idea and needs a complete starting point
- User wants scaffolding for a specific project type
- User needs to add a major feature that requires coordinating multiple domains

## Execution Flow

```
Step 1 → DETECT     : Identify project type from user description
Step 2 → STACK      : Select tech stack (2026 defaults or user preference)
Step 3 → PLAN       : Generate file structure and task breakdown
Step 4 → COORDINATE : Assign domains to specialist agents
Step 5 → BUILD      : Execute in dependency order
Step 6 → VERIFY     : Confirm structure and report next steps
```

## Project Type Detection

| User Description | Project Type | Primary Stack |
|-----------------|-------------|---------------|
| "web app", "full-stack", "dashboard" | Next.js Full-Stack | Next.js + Prisma + PostgreSQL |
| "SaaS", "subscription", "payments" | SaaS Product | Next.js + Stripe + Clerk |
| "landing page", "marketing site" | Static Site | Next.js + Tailwind |
| "REST API", "backend only" | Express API | Express + JWT + PostgreSQL |
| "Python API", "FastAPI" | Python API | FastAPI + SQLAlchemy |
| "mobile app", "iOS + Android" | React Native | Expo + Zustand |
| "cross-platform mobile" | Flutter | Flutter + Riverpod |
| "desktop app" | Electron | Electron + React |
| "browser extension" | Chrome Extension | Chrome MV3 |
| "CLI tool" | Node CLI | Node.js + Commander |
| "monorepo" | Monorepo | Turborepo + pnpm |

## Template Reference

Read only the template that matches the detected project type from the `templates/` directory.

| Template | Path |
|----------|------|
| Next.js Full-Stack | templates/nextjs-fullstack/TEMPLATE.md |
| Next.js SaaS | templates/nextjs-saas/TEMPLATE.md |
| Next.js Static | templates/nextjs-static/TEMPLATE.md |
| Express API | templates/express-api/TEMPLATE.md |
| Python FastAPI | templates/python-fastapi/TEMPLATE.md |
| React Native | templates/react-native-app/TEMPLATE.md |
| Flutter | templates/flutter-app/TEMPLATE.md |
| Electron Desktop | templates/electron-desktop/TEMPLATE.md |
| Chrome Extension | templates/chrome-extension/TEMPLATE.md |
| CLI Tool | templates/cli-tool/TEMPLATE.md |
| Monorepo | templates/monorepo-turborepo/TEMPLATE.md |

## Agent Coordination

| Domain | Agent | When to Invoke |
|--------|-------|---------------|
| Database schema | `database-architect` | When project has persistent data |
| API routes | `backend-specialist` | When project has server-side logic |
| UI components | `frontend-specialist` | When project has user interface |
| Auth flow | `security-auditor` + `backend-specialist` | When project has authentication |
| Deployment | `devops-engineer` | When project needs CI/CD or hosting config |
| Tests | `test-engineer` | After core structure is scaffolded |

## Build Example

```
User: "Build an Instagram clone with photo sharing and likes"

App Builder Process:
1. DETECT  → Social media app with media upload
2. STACK   → Next.js + Prisma + Cloudinary + Clerk
3. PLAN    → Schema (users, posts, likes, follows)
             API (12 endpoints)
             Pages (feed, profile, upload)
             Components (PostCard, Feed, LikeButton)
4. AGENTS  → database-architect, backend-specialist, frontend-specialist
5. BUILD   → Schema first, then API, then UI
6. VERIFY  → Report created files and next steps
```

## Guardrails

- Always confirm the project type and stack with the user before scaffolding.
- Do not install packages without listing them explicitly first.
- Do not create files outside the project directory.
- Prefer battle-tested defaults (listed above) over novel stacks unless user specifies otherwise.
- If requirements are ambiguous (> 2 interpretations possible), apply the Socratic Gate before building.

## Anti-Patterns

- **Do not** start scaffolding before confirming the project type — wrong assumptions waste significant effort.
- **Do not** generate an entire application in one shot without a plan — coordinate agents in dependency order.
- **Do not** choose an exotic stack to be clever — users need maintainable, well-documented defaults.
- **Do not** skip the verify step — users need to know what was created and what to do next.
- **Do not** ignore security from the start — auth, input validation, and env var handling must be in the initial scaffold.
