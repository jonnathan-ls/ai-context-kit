---
version: 4.0.0
name: harness-generator
description: Generates a context-aware agent harness for a repository. Anchors agents via feed-forward (rules, specs, skills) and feedback (sensors, guardrails) so agents execute long-horizon tasks reliably. Generates AGENTS.md at the repository root for auto-discovery.
allowed-tools: Read, Write, Glob, Grep
tags: harness, protocol, quality, safety, architecture, agentic
---

# Harness Generator

Use this skill to generate a minimal agent harness tailored to the repository. The harness lives under `.harness/` and works standalone — no scripts, no dependencies.

This skill is a **protocol director**, not a fixed harness. It guides you to discover context through brief conversation, then generates a harness that fits the project. The harness is minimal, token-efficient, and adapts to the project.

## Core principles

```
HARNESS = FEED-FORWARD + FEEDBACK + LOOP PROTOCOL + MEMORY + EVOLUTION

Feed-forward  → rules, specs, skills (preventive)
Feedback      → linters, tests (reactive)
Loop protocol → atomic tasks, fresh context, explicit exit
Memory        → PROGRESS files, git discipline
Evolution     → every agent mistake becomes a rule
```

**When an agent fails, the environment is incomplete** — add the missing rule, sensor, or convention.

## When to use this skill

- New project or adding agentic workflows.
- Repository has no `.harness/` yet.
- User wants reliable long-horizon execution.

## What this skill generates

Minimal surface. Every file earns its place.

### Root entry point

| File | Purpose |
|------|---------|
| `AGENTS.md` | Universal AI entry point — directs any AI tool to `.harness/` |

### Core layer (always generated)

| File | Purpose |
|------|---------|
| `.harness/HARNESS.md` | Master document: profile, loop protocol, exit conditions |
| `.harness/rules/core.md` | Non-negotiable constraints |
| `.harness/rules/architecture.md` | Stack conventions and monorepo boundaries |
| `.harness/PROGRESS.json` | Feature index (root) — lightweight registry |
| `.harness/LEARNINGS.md` | Failure patterns → new rules |

### Sensor layer (always generated)

| File | Purpose |
|------|---------|
| `.harness/sensors/checklist.md` | Deterministic gate before declaring done |

### Spec layer (generated when features are non-trivial)

| File | Purpose |
|------|---------|
| `.harness/specs/PRD.md` | Product requirements |
| `.harness/specs/TECHNICAL.md` | Architecture decisions |

### Feature layer (one per active feature)

| File | Purpose |
|------|---------|
| `.harness/features/<id>/PROGRESS.json` | Feature state: tasks, session log, debt, inline contract |

### Archive layer (features marked DONE)

| File | Purpose |
|------|---------|
| `.harness/archive/<id>/PROGRESS.json` | Frozen snapshot — immutable record (AI source of truth) |
| `.harness/archive/<id>/README.md` | Human-readable summary generated at archive time |

### Optional / just-in-time

| File | Purpose |
|------|---------|
| `.harness/skills/*.md` | Created on second occurrence of a recurring pattern |
| `.harness/bootstrap.md` | Context reconstruction for complex monorepos |

---

## Execution flow

### Phase 1 — Discovery (no output yet)

Read the repository to infer the profile before asking questions. Inspect:

1. Root files (`package.json`, `go.mod`, `pyproject.toml`, `Cargo.toml`, etc.)
2. Directory structure (top 2 levels)
3. Existing `.harness/` or `.ai-context/` if present
4. CI config (`.github/workflows/`, `Dockerfile`, etc.)
5. Root `AGENTS.md`, `CLAUDE.md`, `.cursorrules` if they exist
6. Existing specs in root or `docs/`

Derive without asking: project type, stack, test runner, linter, conventions, sensor surface, whether specs should move to `.harness/specs/`.

**Migration protocol**: If `.ai-context/` or old harness exists:
1. Read existing files
2. Map old → new structure
3. Present migration plan; preserve human-written content
4. Merge existing `AGENTS.md` / `.cursorrules` rather than replace

### Phase 2 — Targeted interview (2–4 questions max)

Ask only what you cannot infer:

1. **Primary goal** — long-horizon autonomy, quality gates, safe refactoring, onboarding?
2. **Strictness** — balanced or strict?
3. **Sensor surface** — which available: tests, e2e, linter, type checker?
4. **Scope constraint** — anything the harness must never touch?
5. **Template** — inherit from existing `.harness/` in another repo?

After collecting answers, present a 5-bullet summary and ask for confirmation.

### Phase 3 — Manifest

Output a JSON block listing all files to generate:

```json
{
  "profile": {
    "type": "<app|api|library|monorepo|other>",
    "stack": "<language + framework>",
    "strictness": "<balanced|strict>",
    "sensors": ["<list>"],
    "goals": ["<primary>"],
    "template": "<base|nextjs-typescript|python-fastapi|go-stdlib|other>"
  },
  "files": [
    { "path": "AGENTS.md", "reason": "root entry point" },
    { "path": ".harness/HARNESS.md", "reason": "master loop protocol" },
    { "path": ".harness/rules/core.md", "reason": "non-negotiable constraints" },
    { "path": ".harness/rules/architecture.md", "reason": "stack conventions" },
    { "path": ".harness/PROGRESS.json", "reason": "feature index (root)" },
    { "path": ".harness/LEARNINGS.md", "reason": "failure patterns → rules" },
    { "path": ".harness/sensors/checklist.md", "reason": "deterministic gate" },
    { "path": ".harness/specs/PRD.md", "reason": "product requirements", "required": false },
    { "path": ".harness/specs/TECHNICAL.md", "reason": "architecture", "required": false },
    { "path": ".harness/bootstrap.md", "reason": "context reconstruction", "required": false }
  ]
}
```

### Phase 4 — File generation

For each file, output a fenced block:

```
FILE: <path>
[full file content]
```

No commentary inside fences. Keep each file under 350 lines. JSON must be valid.

If total output exceeds a single response, generate in phases:
1. `AGENTS.md` + core layer (`HARNESS.md`, `rules/`)
2. State layer (`PROGRESS.json`, `LEARNINGS.md`)
3. Sensor + optional files

### Phase 5 — Change plan and validation

Output a `CHANGE PLAN` (ordered idempotent steps with `mkdir -p`) and a `VALIDATION` checklist with exact commands for the discovered stack.

---

## Content guidelines per file

### `AGENTS.md` (root entry point)
- Under 60 lines. One-line project description.
- Mandatory first read: `.harness/HARNESS.md`
- Session protocol in 5 lines: load root index → current feature → task → implement → validate → update → stop
- Links to: `HARNESS.md`, `rules/core.md`, `PROGRESS.json` (root)
- Blocking signal: `If anything is unclear, emit BLOCK: <reason> and stop.`
- Do NOT paste full harness content — this is a pointer, not a dump.

### `.harness/HARNESS.md`
- Project profile (type, stack, sensor commands)
- Loop protocol: load root index → current feature → feature state → pick task → implement with sensor feedback → run checklist → update feature state → archive if done → stop
- Separate implement and validate sessions — never the same session
- Progressive context disclosure: load architecture.md/skills only when domain-relevant
- Exit conditions (all sensors green, or BLOCK)
- Blocking protocol (root cause + required human input)
- Human review cadence
- Token budget: 1/3 planning, 1/3 implementation, 1/3 review
- Evolution log: dated entries for new rules/sensors after failures
- Skill creation convention: when a pattern recurs, create `.harness/skills/<pattern>.md`

### `.harness/rules/core.md`
- Never declare done without running the full sensor checklist
- Never delete tests, never weaken assertions
- Never touch files outside declared scope without a new task entry
- Never guess a convention — read existing code or BLOCK
- Prefer smallest change that satisfies requirement
- Every file under 350 lines; split if exceeded
- Rules must be binary — no "try to" or "prefer"
- Stack-specific rules inferred from existing code

### `.harness/rules/architecture.md`
- Directory structure and ownership boundaries
- Canonical patterns (one ORM, one HTTP client, one way to do X)
- Dependency rules (what can import what)
- Naming conventions inferred from existing code
- Monorepo: package isolation, public API vs internal, shared deps rules

### `.harness/PROGRESS.json` (root index)
- Under 50 lines. This is an index, not full state.
- `current_feature`: pointer to active feature ID
- `features[]`: registry with `id`, `title`, `status` (IN_PROGRESS/DONE), `path` (features/ or archive/)
- `human_override[]`: active stakeholder input with `applied: false`
- `harness_version`: version string
- `evolution[]`: dated entries for harness changes
- **Critical rule**: agent NEVER reads all features. Only loads `current_feature`.

### `.harness/features/<id>/PROGRESS.json` (feature state)
- The actual work state. Small, focused, independent.
- `feature_id`, `title`, `status`
- `tasks[]`: id, title, status (TODO/IN_PROGRESS/DONE/BLOCKED), agent_type
- `tasks[].contract` (optional): commitments[], validation[], threshold — written by implement before coding
- `session_log[]`: timestamp, task_id, action, sensor_results, files_touched
- `debt[]`: id, description, priority
- `session_in_progress`: active, started_at, task_id, agent_type, last_heartbeat
- `deliveries[]`: date, task_id, title, files, location, output_format, validation_status
- Typical feature: 3-10 tasks, file stays under 100 lines.
- **When to create a new feature**: new capability, module, or major change. NOT every tiny task.

### `.harness/sensors/checklist.md`
- Deterministic gate. Agent runs every item before declaring done.
- Exact commands for discovered stack — no placeholders.
- Items: linter (exit 0), type checker (zero errors), tests (all pass), e2e (if present), no TODO/FIXME introduced, PROGRESS updated, no files outside scope, file size check (≤350 lines).

### `.harness/LEARNINGS.md`
- Pattern: [error description]
- When, Symptom, Root cause, Fix applied, Validation
- Review cadence: once per sprint or weekly. Convert human comments into guardrails.

### `.harness/skills/*.md` (just-in-time)
- Created when the same pattern appears a second time.
- One page: what problem it solves, when to apply, concrete steps, example.
- Stored in `.harness/skills/` and referenced from HARNESS.md evolution log.
- Monorepo: may have `packages/<name>/skills/` for package-specific conventions.

### `.harness/bootstrap.md` (optional)
- Ordered read list: HARNESS.md → root PROGRESS → feature PROGRESS → architecture.md
- Reconstruct state: root index → current_feature pointer → feature state
- Session crash recovery: check root index, then feature-level session_in_progress
- Health-check commands before starting work

---

## Design principles

1. **Feature-based sharding**: Root index <50 lines. Feature states <100 lines. Archive is immutable. Scales to 500+ features with constant token cost.

2. **JSON for mutable state, Markdown for documentation**: All state in JSON; all human docs in Markdown.

3. **Just-in-time context**: Surface instructions only when the agent reaches the relevant domain.

4. **Separate implement from validate**: Always different sessions. The implement agent is not the judge of its own output.

5. **Just-in-time skills**: Do not pre-populate skills. Create them when a pattern repeats.

6. **Evolution over perfection**: Every recurring mistake becomes a rule. Every human review comment repeated twice becomes a sensor.

---

## Anti-patterns (never generate these)

- **One-shot sessions**: implement, validate, and declare done in a single session
- **Soft rules**: "try to" or "prefer" — every rule must be binary
- **Stale state**: agents skip updating feature PROGRESS
- **Markdown for state**: using Markdown for PROGRESS instead of JSON
- **Phantom sensors**: generating sensors for tools not present in the project
- **CLI dependency**: harness that only works with a specific CLI
- **Fat files**: files over 350 lines — split them
- **Skill sprawl**: pre-creating more than 2 skills before the first task
- **Frontloaded context**: dumping entire harness into AGENTS.md or session start
- **Agent as judge**: letting agent decide correctness without external sensors
- **No spec_lines**: giving agent a 2000-line spec without line ranges
- **No learnings loop**: not capturing failures in LEARNINGS.md
- **Loading all features**: agent loads every feature's PROGRESS instead of just current one
- **Leaving done features in features/**: completed features not archived confuse the agent
- **Cross-feature dependencies**: tasks depending on other features without explicit BLOCK

---

## Feature documentation for humans

The harness prioritizes machine-readable state (JSON for AI), but humans need visibility into what was built.

**Rule: AI never reads generated human docs. The source of truth is always the feature PROGRESS.json + git history.**

When a feature is archived, the AI generates `archive/<id>/README.md` from the feature's PROGRESS.json. This file is **immutable** — generated once at archive time, never updated again.

For human review of completed features:
- **Source of truth**: `.harness/archive/<id>/PROGRESS.json` + git diff of the feature's commits
- **Human-readable summary**: `.harness/archive/<id>/README.md` — generated at archive time from PROGRESS.json
- **On-demand project view**: If the human wants a consolidated summary of all features, generate a temporary `.harness/FEATURES.md` from all archive/README.md files on request. This is a view, not state — can be deleted and re-generated.
- **Monorepo**: Package-level `README.md` inside the package directory is project documentation, not harness state.

Do NOT create wikis, HTML files, or living documents that the harness must keep synchronized. The AI's context budget is too scarce for that. Humans can read archive/README.md directly or request a generated summary when needed.

---

## Blocking conditions

Stop and emit `BLOCK: <reason>` when:

- Stack cannot be inferred and user has not answered discovery questions
- Target `.harness/` has conflicting existing structure — present diff and ask
- Required sensor (e.g., test runner) is unknown and cannot be assumed
- Repository has no tests and no linter — surface explicitly

---

## Output conventions

- Manifest first (JSON block)
- `AGENTS.md` second (root entry point)
- Core layer: `HARNESS.md`, `rules/core.md`, `rules/architecture.md`
- State layer: `PROGRESS.json`, `LEARNINGS.md`
- Sensor layer: `sensors/checklist.md`
- Spec layer (if required): `specs/PRD.md`, `specs/TECHNICAL.md`
- Feature layer: `features/<id>/PROGRESS.json`
- Archive layer: `archive/<id>/PROGRESS.json` + `archive/<id>/README.md`
- Optional: `bootstrap.md`
- Each file as `FILE: <path>` + fenced content (no commentary inside fences)
- Change plan: numbered, idempotent steps with `mkdir -p`
- Validation: exact commands for the discovered stack — no placeholders
- Token efficiency: generate in 2-3 phases if too large for one response
- Never generate empty files or placeholders — every file must be immediately usable
- JSON files must be valid JSON — verify before output
