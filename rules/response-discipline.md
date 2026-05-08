---
trigger: always_on
name: response-discipline
description: Enforces strict response boundaries, scope control, and token efficiency.
version: 1.0.0
priority: P0
tags: core, scope, token
---

# Response Discipline Protocol

## Core Directive

Respond only to what was asked.

## Scope Rules

Classify each request before responding (see canonical types in ALWAYS.md → REQUEST CLASSIFIER):

| Intent | Keywords | Output |
|--------|----------|--------|
| **Question** | "what is", "how", "why", "explain" | Direct explanation — no code unless asked |
| **Simple task** | "fix", "add", "change" | Targeted edit — no scope expansion |
| **Complex task** | "build", "create", "implement", "refactor" | Agent + skill → implement |
| **Plan** | "plan", "outline", "strategy" | Structured breakdown — no implementation |
| **Review** | "review", "check", "audit" | Findings and risks — no rewrites unless asked |

Hard boundaries:
- No scope expansion without user request.
- No unrelated refactors.
- No fabricated APIs or facts.

## Token Discipline

- Keep answers concise and direct.
- Remove repeated restatements and long preambles.
- Avoid duplicating code already written to files.

## File and Command Discipline

- If the user requested implementation, apply the change directly.
- Ask before destructive or ambiguous operations.
- Explicitly call out risky flags (`--force`, `-rf`, destructive SQL).

## Accuracy Gate

Before replying, verify:
- Facts are correct or marked uncertain.
- The response fully addresses the request.
- The output format matches intent (text vs code vs edits).
