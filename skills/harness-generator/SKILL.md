---
version: 2.0.0
name: harness-generator
description: Generates a context-aware, MD-only agent harness for a repository. The harness anchors agents to a stable operational environment using feed-forward (rules, specs, skills) and feedback (sensors, guardrails, contracts) so agents can execute long-horizon tasks reliably without constant human steering. Generates AGENTS.md at the repository root so any AI tool (Claude Code, Codex, Gemini CLI, Windsurf, Cursor, etc.) auto-discovers the harness.
allowed-tools: Read, Write, Glob, Grep
tags: harness, protocol, quality, safety, architecture, performance, agentic, resilience
---

# Harness Generator

Use this skill to generate a complete agent harness tailored to the target repository's stack and context. The harness is placed under `.harness/` and works standalone — no external scripts, no dependencies on this CLI.

A harness is **not** just rules and skills. It is the full operational environment that anchors the agent: feed-forward guidance before execution, feedback sensors that verify output, a loop protocol that keeps each session focused, progress memory that survives across sessions, and an evolution mechanism that turns every failure into a permanent fix.

## Core concepts (from which everything is derived)

```
HARNESS = FEED-FORWARD + FEEDBACK + LOOP PROTOCOL + MEMORY + EVOLUTION

Feed-forward  → rules, specs, skills, architecture docs (preventive, before execution)
Feedback      → linters, tests, type checkers, review agents (reactive, after execution)
Loop protocol → atomic tasks, fresh context per iteration, explicit exit condition
Memory        → progress files, session handoff docs, git discipline
Evolution     → every agent mistake becomes a rule; harness improves continuously
```

The bottleneck is never the model's intelligence. It is the quality of the environment in which the model operates.

## Mindset: the skill-issue reframe

Before generating anything, internalize this:

> *"There is a pattern engineers fall into: the agent does something dumb, the engineer blames the model, and the blame gets filed under 'wait for the next version'. The harness engineering mindset rejects that default. The failure is usually legible — the agent didn't know about a convention, so you add it. The agent ran a destructive command, so you add a hook that blocks it. Every mistake becomes an opportunity to improve the harness."*

The agent you are generating a harness for is not broken. The environment is incomplete. Your job is to complete it.

Also: **every time a human has to type "continue" to an agent is a harness failure** — the harness did not give the agent enough context to know how to proceed on its own.

## When to invoke this skill

- Starting a new project or adding agentic workflows to an existing one.
- The repository has no `.harness/` structure yet, or it is incomplete.
- The user wants agents to handle long-horizon tasks reliably (features, sprints, full-stack work).
- The user wants a resilient integration protocol so agents and humans collaborate without chaos.

## What this skill generates

Minimal surface — no bloat. Every file must earn its place.

### Root entry point (always generated)

| File | Purpose |
|------|---------|
| `AGENTS.md` | Universal AI entry point at repo root — directs any AI tool to `.harness/` and states the session protocol |

### Core layer (always generated)

| File | Purpose |
|------|---------|
| `.harness/HARNESS.md` | Master document: profile, loop protocol, exit conditions, evolution log |
| `.harness/rules/core.md` | Non-negotiable constraints the agent must never violate |
| `.harness/rules/architecture.md` | Stack conventions, patterns, anti-patterns for this project |
| `.harness/skills/implement.md` | How to execute a task: plan → implement → self-verify loop |
| `.harness/skills/validate.md` | Separate validation mission: sensors, contracts, scoring |
| `.harness/PROGRESS.json` | Concise session state (JSON format — model-safe, corruption-resistant) |
| `.harness/CONTRACTS.json` | Handoff contracts between implement and validate agents (JSON format) |
| `.harness/LEARNINGS.md` | Agent failure patterns → new rules (human review cycle) |

### Sensor layer (generated when stack supports it)

| File | Purpose |
|------|---------|
| `.harness/sensors/checklist.md` | Deterministic gate the agent runs before declaring done |
| `.harness/sensors/review-agents.md` | Parallel persona-scoped review prompts (correctness / security / simplicity) |
| `.harness/sensors/metrics.md` | Token distribution: 1/3 planning, 1/3 implementation, 1/3 review (Ryan/OpenAI pattern) |

### Optional bootstrap (generated when project is complex or monorepo)

| File | Purpose |
|------|---------|
| `.harness/bootstrap.md` | Context reconstruction for new sessions — orients a fresh agent in under 10 reads |

### Project specs layer (for project specifications, not protocol)

| File | Purpose |
|------|---------|
| `.harness/specs/PRD.md` | Product requirements document (optional — if project has spec) |
| `.harness/specs/TECHNICAL.md` | Technical specification (optional — if project has spec) |
| `.harness/specs/SPRINTS.json` | Sprint breakdown with spec_lines ranges (Anthropic V2 pattern) |

### Deliverables layer (IN/OUT flow)

| File | Purpose |
|------|---------|
| `.harness/DELIVERIES.md` | History of deliverables with traceability (what was delivered, when, where) |
| `.harness/DELIVERIES.json` | Machine-readable delivery log for automation and metrics |

## Execution flow

Follow these steps exactly. Do not skip or reorder.

### Phase 1 — Discovery (no output yet)

Read the repository to infer the profile before asking any questions. Inspect:

1. Root files (`package.json`, `pyproject.toml`, `go.mod`, `Cargo.toml`, `Makefile`, etc.)
2. Directory structure (top 2 levels via Glob)
3. Existing `.harness/` or `.ai-context/` if present
4. CI config (`.github/workflows/`, `Dockerfile`, etc.)
5. Root `AGENTS.md`, `CLAUDE.md`, `.cursorrules` if they exist — read the existing AI conventions
6. Check for existing specs: `PRD.md`, `TECHNICAL.md`, `SPRINTS.json` in root or `docs/`

Derive without asking: project type, primary language/stack, test runner, linter, existing conventions, current sensor surface, whether the project has existing specs that should be moved to `.harness/specs/`.

### Phase 2 — Targeted interview (2–4 questions max)

Ask only what you cannot infer. Candidate questions — use only what is genuinely unknown:

1. **Primary goal for the harness** — long-horizon autonomy, quality gates, safe refactoring, onboarding agents to an existing codebase, or other?
2. **Strictness** — balanced (agents can make judgment calls) or strict (every decision must match a documented convention)?
3. **Sensor surface** — which of these are available or desired: unit tests, integration tests, e2e (Playwright/Cypress), linter, type checker, custom CI scripts?
4. **Scope constraint** — anything the harness must never touch or generate (e.g., migration files, secrets, infra)?

After collecting answers, present a 5-bullet summary and ask for confirmation before generating.

> Token efficiency principle: do not frontload every instruction into the agent at session start. The harness must surface context progressively — rules and architecture docs are loaded on demand via `AGENTS.md` imports, not dumped wholesale into the context window.

### Phase 3 — Manifest

Output a JSON block:

```json
{
  "profile": {
    "type": "<app|api|library|monorepo|other>",
    "stack": "<language + framework>",
    "strictness": "<balanced|strict>",
    "sensors": ["<list of available sensors>"],
    "goals": ["<primary goals>"]
  },
  "files": [
    { "path": "AGENTS.md", "reason": "universal AI entry point at repo root" },
    { "path": ".harness/HARNESS.md", "reason": "master loop protocol" },
    { "path": ".harness/rules/core.md", "reason": "non-negotiable constraints" },
    { "path": ".harness/PROGRESS.json", "reason": "session state (JSON format, model-safe)" },
    { "path": ".harness/CONTRACTS.json", "reason": "handoff contracts (JSON format)" },
    { "path": ".harness/LEARNINGS.md", "reason": "agent failure patterns → new rules" }
  ]
}
```

### Phase 4 — File generation

For each file in the manifest output a fenced block with this exact header:

```
FILE: AGENTS.md
[full file content]
```

or

```
FILE: .harness/HARNESS.md
[full file content]
```

or

```
FILE: .harness/PROGRESS.json
[full file content]
```

No commentary inside code fences. Keep each file under 350 lines. JSON files must be valid JSON — use a linter to verify before output.

### Phase 5 — Change plan and validation

Output a `CHANGE PLAN` (ordered idempotent steps) and a `VALIDATION` checklist.

---

## File content specifications

When generating each file, follow these templates exactly. Adapt content to the discovered profile — never generate generic boilerplate that ignores the stack.

### `AGENTS.md` (root — universal AI entry point)

This file is read automatically by Claude Code, OpenAI Codex, Gemini CLI, Windsurf, Cursor, and other AI tools before any session. It must be concise (under 60 lines) and actionable.

Must contain:

- One-line description of the project
- **Mandatory first read**: `Read .harness/HARNESS.md before doing anything else in this repository.`
- The session protocol in 5 lines or less (load PROGRESS → pick one task → contract → implement → validate → update PROGRESS → stop)
- Direct links to the 3 most critical harness files: `HARNESS.md`, `rules/core.md`, `PROGRESS.json`
- The blocking signal: `If anything is unclear, emit BLOCK: <reason> and stop. Do not guess.`
- **Do NOT** paste the full harness content here — this file is a pointer, not a dump

Example structure:

```markdown
# AGENTS

This repository uses an agent harness located in `.harness/`.

## Mandatory bootstrap

Before writing any code, read:
1. `.harness/HARNESS.md` — session protocol and project profile
2. `.harness/rules/core.md` — non-negotiable constraints
3. `.harness/PROGRESS.json` — current state and task backlog

## Session protocol (summary)

1. Load PROGRESS.json → understand current state
2. Pick ONE atomic task from the backlog
3. Create a CONTRACTS.json entry before writing code
4. Implement → run sensors after each meaningful change
5. Run full sensor checklist before declaring done
6. Update PROGRESS.json and CONTRACTS.json
7. Stop — do not chain tasks in a single session

## Blocking

If scope, conventions, or requirements are unclear: emit `BLOCK: <reason>` and stop.
Do not guess. Do not proceed without resolving the block.
```

### `.harness/HARNESS.md`

Must contain:

- **Project profile** (type, stack, sensor surface, sensor commands)
- **Loop protocol**: the step-by-step ritual every agent session must follow
  1. Load `PROGRESS.json` — understand current state before writing a line
  2. Pick exactly one atomic task from the backlog
  3. Create or update `CONTRACTS.json` entry for this task (agree the contract before coding)
  4. Implement with continuous sensor feedback (run linter/tests after each meaningful change)
  5. Run the full sensor checklist — do NOT declare done until all gates pass
  6. Update `PROGRESS.json` with what was done, what passed, what is pending
  7. Stop — do not continue to the next task in the same session
- **Progressive context disclosure**: do not load all harness docs at session start — load architecture.md and skills only when their domain becomes relevant to the current task
- **Exit conditions**: the only valid reasons to stop the loop (all sensors green, or explicit BLOCK)
- **Blocking protocol**: when to stop and surface a BLOCK with root cause + required human input
- **Human review cadence**: define when a human must review before the loop continues (e.g., after each sprint, before merging a PR, after a BLOCK is resolved)
- **Evolution log**: dated entries when a new rule or sensor is added because of an agent failure

### `.harness/rules/core.md`

Non-negotiable rules. Must include:

- Never declare a task done without running the full sensor checklist
- Never delete tests, never weaken assertions — if a test is wrong, fix the test and document why
- Never touch files outside the task's declared scope without creating a new task entry first
- Never guess a convention — if uncertain, read the existing code or ask via BLOCK
- Prefer the smallest possible change that satisfies the requirement
- Every new pattern introduced must be consistent across the entire codebase — no local coherence optimizations (e.g., do not create a local helper when a shared one exists)
- Every file introduced must stay under 350 lines — if a file grows beyond this, split it before the session ends
- Rules must be binary — avoid "try to" or "prefer" language; if it cannot be enforced deterministically, it belongs in a sensor, not a rule
- Add rules specific to the discovered stack (e.g., for TypeScript: no `any`, parse-don't-validate at boundaries; for Python: no bare `except`, typed signatures on all public functions)

### `.harness/rules/architecture.md`

Stack-specific architecture conventions. Derived from discovery. Must cover:

- Directory structure and ownership boundaries
- Canonical patterns for this stack (one ORM, one HTTP client, one async helper, one way to do X — enforce singularity)
- Dependency rules (what can import what; package privacy if monorepo)
- File size hard limit: 350 lines (keeps each file within agent context efficiency range)
- Naming conventions inferred from reading existing code — never invent conventions
- If monorepo: package isolation rules, which packages are public API vs internal, how cross-package imports are governed

### `.harness/skills/implement.md`

The implement agent's mission protocol. Must cover:

- Pre-flight: load PROGRESS.json → load CONTRACTS.json → load architecture.md only for the domain being touched
- Task selection: pick ONE atomic task; if too large to complete with sensor-green output in one session, split it first and update the backlog before writing any code
- Implementation loop: code → lint → test → fix → repeat until sensors are green
- Self-correction: if a sensor fails, fix the root cause — never disable the sensor, skip the check, or mark the task done while a sensor is red
- Handoff: write CONTRACTS.json entry before stopping — explicit list of what was built and what the validate agent must verify item by item
- Update PROGRESS.json session log before stopping
- Context discipline: do not load files unrelated to the current task; agent context is scarce and must be preserved

### `.harness/skills/validate.md`

The validate agent's mission protocol. Must cover:

- Its mission is exclusively to validate — never modify implementation code; if a fix is needed, write it to the failure report and stop
- Load the CONTRACTS.json entry for the current task — do not validate anything not on the contract
- Verify each contract item deterministically (run tests, check linter, verify behavior end-to-end)
- Score each item: PASS / FAIL / PARTIAL with evidence (test output, linter output, observed behavior)
- If any item fails: write a structured failure report to PROGRESS.json — include item, expected result, actual result, suggested root cause — then stop
- If all items pass: mark the task PASSED in CONTRACTS.json and DONE in PROGRESS.json
- The validate agent runs in a separate session with a fresh context — it is not a sub-agent of the implement agent

### `.harness/PROGRESS.json`

Session state in JSON format — this is the harness's external memory. JSON is preferred over Markdown because models corrupt JSON files less frequently (Anthropic pattern). Every agent reads it first; every agent updates it before stopping.

Must contain:

```json
{
  "current_sprint": { "id": "sprint-1", "goal": "...", "deadline": "YYYY-MM-DD" },
  "tasks": [
    { "id": "task-1", "title": "...", "status": "TODO|IN_PROGRESS|DONE|BLOCKED", "agent_type": "implement|validate" }
  ],
  "session_log": [
    { "timestamp": "YYYY-MM-DDTHH:mm:ssZ", "task_id": "task-1", "action": "...", "sensor_results": "...", "files_touched": ["..."] }
  ],
  "debt": [
    { "id": "debt-1", "description": "...", "priority": "low|medium|high" }
  ],
  "evolution": [
    { "date": "YYYY-MM-DD", "symptom": "...", "root_cause": "...", "fix_applied": "..." }
  ]
}
```

Keep it minimal — only the current sprint and active tasks. Archive completed sprints to `PROGRESS_ARCHIVE.json` to avoid bloating the file.

### `.harness/CONTRACTS.json`

Handoff contracts between implement and validate agents in JSON format. This is the mechanism that prevents the validate agent from hallucinating extra requirements and prevents the implement agent from declaring victory prematurely.

```json
{
  "contracts": [
    {
      "task_id": "task-1",
      "title": "...",
      "implement_commitments": ["item 1", "item 2"],
      "validate_items": ["item 1", "item 2"],
      "passing_threshold": "all unit tests green, linter clean, no type errors",
      "status": "OPEN|IN_PROGRESS|VALIDATING|PASSED|FAILED"
    }
  ]
}
```

The contract is written by the implement agent before coding starts and agreed with the human if in strict mode. The validate agent cannot add items — if scope changes, a new task entry is created.

### `.harness/sensors/checklist.md`

Deterministic gate — the agent is not the judge of its own output. External tools are. The agent must run every item on this checklist before declaring done. Must list:

- Run linter → exit 0 required (state exact command for discovered stack)
- Run type checker → zero errors (state exact command)
- Run test suite → all tests pass (state exact command; include coverage threshold if project has one)
- Run e2e / integration tests → pass (only if project has them; state command)
- No TODO/FIXME introduced in files touched by this task
- `PROGRESS.json` session log updated
- `CONTRACTS.json` entry status updated
- No files modified outside the task's declared scope (verify via `git diff --name-only`)
- File size check: no file touched exceeds 350 lines

The checklist must use the exact commands discovered for the project's stack — no placeholder commands.

### `.harness/sensors/review-agents.md`

Parallel review agent prompts — each persona runs in its own session with its own fresh context. This is not a sub-agent; it is a separate agent invoked after implementation, before the validate agent runs.

Each persona section must:

- State its mission in one sentence
- Name the exact harness documents it checks against (`architecture.md`, `core.md`, etc.)
- Define what constitutes a P1 (blocks merge) vs P2 (non-blocking, logged to debt) finding
- Produce a structured finding report: `{ persona, task_id, findings: [{severity, file, line, description, expected}] }`

Default personas — generate only those relevant to the discovered project profile:

- **correctness**: Does the implementation match the contract? Are edge cases handled? Are error paths covered?
- **security**: Are secrets handled safely? Are inputs validated at boundaries? Are destructive operations guarded?
- **simplicity**: Is there duplicated logic? Are files approaching the 350-line limit? Are shared utilities used instead of local re-implementations?
- **performance** (only if latency/scale is a stated goal): Are there obvious N+1 queries, unbounded loops, missing indexes?
- **resilience** (only for network/API code): Are there timeouts and retries on every external call? Are failures surfaced correctly?

Human review cadence: review agents run on every push (or on every task completion if no CI). A human reviews P1 findings before the loop continues.

### `.harness/LEARNINGS.md`

Agent failure patterns → new rules. This is the human review cycle (Ryan/OpenAI pattern: "garbage collection day").

Structure:

```markdown
# Learnings

## Pattern: [error description]
- **When**: [date]
- **Symptom**: what the agent did wrong
- **Root cause**: missing rule, missing sensor, ambiguous convention
- **Fix applied**: which rule/sensor was added
- **Validation**: how we verified the fix works

## Pattern: ...
```

Review cadence: once per sprint (or once per week on active projects). Convert human review comments into automatic guardrails.

### `.harness/bootstrap.md` (optional — generate for complex projects and monorepos)

Context reconstruction — orients a fresh agent in under 10 file reads. Must cover:

- The ordered read list: which 3–5 files give the most orientation value (HARNESS.md → PROGRESS.json → architecture.md → the most recently changed domain file)
- How to reconstruct current state from `PROGRESS.json` and `git log --oneline -20` in a new session
- The health-check commands to run before starting work (all sensors green = safe to proceed)
- What a BLOCKED state looks like in PROGRESS.json and how to handle it

---

### `.harness/specs/SPRINTS.json` (optional — for projects with detailed specs)

Sprint breakdown with spec_lines ranges (Anthropic V2 pattern). This prevents the agent from reading the entire spec and exploding context.

```json
{
  "sprints": [
    {
      "id": "sprint-1",
      "title": "...",
      "status": "PENDING|IN_PROGRESS|DONE",
      "spec_lines": "17-53",
      "files_to_touch": ["src/auth/login.ts:1-200"],
      "acceptance_criteria": ["..."],
      "hints": ["look for pattern X in file Y"],
      "security_phases": ["validate input", "sanitize output"]
    }
  ]
}
```

### `.harness/DELIVERIES.md` (IN/OUT flow)

History of deliverables with traceability. This answers: what was delivered, when, where, and by whom.

```markdown
# Deliveries

## [YYYY-MM-DD] Sprint 1 Complete
- **Delivered**: Login with email/password
- **Files**: `src/auth/login.ts`, `src/auth/types.ts`
- **Location**: `/auth/login` route
- **Output format**: TypeScript components
- **Traceability**: Task ID task-1, Contract ID contract-1
- **Validation**: All sensors green, evaluator PASSED

## ...
```

### `.harness/DELIVERIES.json` (machine-readable)

```json
{
  "deliveries": [
    {
      "date": "YYYY-MM-DD",
      "sprint_id": "sprint-1",
      "task_id": "task-1",
      "contract_id": "contract-1",
      "title": "Login with email/password",
      "files": ["src/auth/login.ts", "src/auth/types.ts"],
      "location": "/auth/login",
      "output_format": "TypeScript components",
      "validation_status": "PASSED",
      "sensor_results": {"linter": "clean", "tests": "all_pass"}
    }
  ]
}
```

This enables:
- Rastreabilidade de entregáveis
- Metrics on what was delivered when
- Automated rollback by file location
- Output format consistency tracking

---

## Harness evolution protocol

Every agent harness must be a living document. Include this protocol verbatim in `.harness/HARNESS.md`:

```
WHEN an agent makes a recurring mistake:
  1. Identify the root cause (missing rule, missing sensor, ambiguous convention)
  2. Add the minimum fix to the appropriate file (rule, architecture, sensor, checklist)
  3. Log the change in the Evolution Log in PROGRESS.json: date | symptom | root cause | fix applied
  4. Add a pattern entry to LEARNINGS.md
  5. Do NOT patch downstream behavior — fix the source document

WHEN a human gives the same code review comment more than once:
  → That comment is a missing rule. Add it to core.md or architecture.md.
  → That check is a missing sensor. Add it to checklist.md or review-agents.md.
  → Eliminate the need for that comment permanently.

GARBAGE COLLECTION (Ryan/OpenAI pattern): Once per sprint (or once per week on active projects):
  → Review PROGRESS.json debt entries
  → Review LEARNINGS.md patterns
  → Triage: which debt items, if fixed, would eliminate recurring sensor failures?
  → Schedule the top 1–2 as atomic tasks in the next sprint
  → Remove debt entries that were resolved

TOKEN DISTRIBUTION (Ryan/OpenAI pattern):
  → 1/3 planning and curation (PRD, spec generation, sprint breakdown)
  → 1/3 documentation and implementation (code writing)
  → 1/3 review and tests (review agents, test execution)

NEVER wait for the next model version. Fix the harness.
```

---

## Anti-patterns (never generate these)

- **One-shot sessions**: a skill that implements, validates, and declares done in a single session — separate implement from validate, always in different sessions
- **Soft rules**: rules that say "try to" or "prefer" — every rule must be binary and deterministically verifiable; soft guidance belongs in architecture.md as context, not as a rule
- **Stale PROGRESS.json**: a harness where agents skip updating PROGRESS.json — this breaks the memory layer and forces the next session to waste tokens reconstructing state
- **Markdown for state**: using Markdown for PROGRESS or CONTRACTS instead of JSON — models corrupt Markdown files more frequently; JSON is the preferred format for state (Anthropic pattern)
- **Phantom sensors**: generating a Playwright sensor for a CLI tool, a type-checker sensor for a language with no type checker, or any sensor command that would fail on a fresh clone
- **CLI dependency**: a harness that only works when the AI-Context CLI is installed — it must be standalone Markdown that any AI can read
- **Fat files**: files over 350 lines — split; large files are context waste and hurt agent reliability
- **Skill sprawl**: more than 6 skills in `.harness/skills/` — improve existing skills before adding new ones; centralize leverage
- **Frontloaded context**: dumping the entire harness into `AGENTS.md` or into the session start — surface context progressively, just-in-time, when the agent reaches the relevant domain (Ryan/OpenAI pattern)
- **Agent as judge**: letting the agent decide if its own output is correct without running external sensors — the agent is not the judge; the linter, the test runner, the type checker are
- **No spec_lines**: giving the agent a 2000-line spec without spec_lines ranges — the agent will read the entire file and explode context; always use spec_lines ranges (Anthropic V2 pattern)
- **No learnings loop**: not capturing agent failures in LEARNINGS.md — this prevents the harness from evolving; every recurring mistake must become a rule

---

## Blocking conditions

Stop and emit `BLOCK: <reason>` when:

- The stack cannot be inferred and the user has not answered the discovery questions
- The target `.harness/` already contains a harness with conflicting structure — present a diff and ask before overwriting
- A required sensor (e.g., test runner) is unknown and cannot be safely assumed from the repository
- The repository has no tests and no linter — surface this explicitly; generating a sensor checklist for a project with no sensors is misleading

---

## Output conventions

- Manifest first (JSON block)
- `AGENTS.md` second (root entry point — always the first file output)
- Core layer next: `HARNESS.md`, `rules/core.md`, `rules/architecture.md`, `skills/implement.md`, `skills/validate.md`
- State layer: `PROGRESS.json`, `CONTRACTS.json`, `LEARNINGS.md`
- Sensor layer: `checklist.md`, `review-agents.md`, `metrics.md`
- Optional layers: `bootstrap.md`, `specs/` (PRD, TECHNICAL, SPRINTS.json), `DELIVERIES.md`, `DELIVERIES.json`
- Each file as `FILE: <path>` + fenced content (no commentary inside fences)
- Change plan: numbered, idempotent, copy-pastable steps — include `mkdir -p` for new directories
- Validation: exact commands for the discovered stack (no placeholder commands like `<your-test-runner>`)
- Token efficiency: total output should be completable in a single response — if too large, generate `AGENTS.md` + core layer + state layer first and offer to continue with sensor layer and optional files
- Never generate a file that is empty or contains only placeholders — every generated file must be immediately usable
- JSON files must be valid JSON — verify before output
