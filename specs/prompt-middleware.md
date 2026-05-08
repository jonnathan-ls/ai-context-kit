---
name: prompt-middleware
version: 1.0.0
description: Request-to-context middleware pipeline for AI Context (harness, Smart Tags, token budgeting, and verification).
tags: middleware, harness, smart-tags, token
status: draft
---

# Prompt Middleware Specification

This specification defines how **AI Context** should behave as a lightweight *prompt middleware*.

The objective is to improve **quality** (fewer hallucinations, higher correctness) while improving **efficiency** (lower token overhead, fewer wasted tool calls).

## Goals

- Prevent “trial-and-error coding” caused by missing context.
- Enforce a clear pre-flight harness before complex work.
- Select only the **minimum necessary** rules/skills for a given request.
- Compress long logs and bulky context *without losing intent*.
- Require evidence-based verification when changes are applied.

## Non-Goals

- Building a full conversational UI, agent runtime, or model gateway.
- Running LLM-based summarization inside the CLI (middleware remains deterministic by default).

## Pipeline (Canonical)

The middleware pipeline is defined as:

1. **Ingest**: capture the user request + environment facts.
2. **Classify**: detect intent and domains (frontend/backend/tests/etc).
3. **Harness (Context Validator)**: verify the task is actionable.
4. **Smart Tags**: select only relevant rules/skills for the request.
5. **Context Ranking**: identify the smallest set of files to read.
6. **Token Budgeting**: cap reads and prefer targeted excerpts.
7. **Spec Gate (Spec Enforcer)**: ensure a spec exists before building.
8. **Implement**: apply minimal, targeted changes.
9. **Evidence Check**: validate with errors/tests/builds where appropriate.
10. **Report**: concise outcome + risks + next steps.

## Core Middleware Artifacts

### Manifests

- `.context-sizes.json`
  - Tracks baseline KB cost and per-resource sizes.
  - Used for token budgeting and context cost audits.

- `.aictx-manifest.json`
  - Machine-readable inventory of rules/skills/agents/workflows/specs.
  - Includes per-item tags and `size_kb` for selection.

### Smart Tags (Taxonomy)

Tags are **comma-separated** in frontmatter (`tags: a, b, c`).

Suggested top-level tags:

- `core` — always relevant, low-risk, high signal
- `token` — token budgeting, compression, context costs
- `harness` — pre-flight validation and gating
- `routing` — agent/skill activation, selection logic
- `quality` — clean code, correctness checks
- `safety` — destructive action gates, ambiguity handling
- `workspace` — repo navigation, mapping, file selection
- `spec` — spec creation/enforcement workflows

Rules and skills should declare tags so the middleware can select minimal subsets.

## Acceptance Criteria

- A “complex task” triggers a harness checklist before edits.
- Long/noisy inputs are compressed deterministically before action.
- Context selection prefers **ranked top-K** files over recursive scanning.
- Specs can be authored and then used as a contract for implementation.
- Sync produces updated manifests without breaking existing commands.

## Rollout

- Phase 1: tags + manifests + harness/spec skills
- Phase 2: CLI helpers for bundling/tag-based selection
- Phase 3: evals and regression fixtures for stable behavior
