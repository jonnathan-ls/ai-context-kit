---
version: 0.1.0
name: multimodal-prompt-orchestrator
description: Framework for orchestrating multimodal prompt iterations (image/video/audio) with clear constraints, verification, and minimal token waste.
allowed-tools: Read, Glob, Grep
tags: multimodal, orchestration, prompts
---

# Multimodal Prompt Orchestrator

Use this skill when a request involves **prompting media models** (image/video/audio) and benefits from an iterative, constraints-first prompt workflow.

## When to Use

- The user asks to generate or refine prompts for images/videos/audio.
- The request requires multiple outputs/variants.
- The user provides prior generations and wants improvements.

## Workflow

1. Clarify the deliverable (format, aspect ratio, duration, language, platform constraints).
2. Extract hard constraints (must-haves / must-not-haves).
3. Draft a compact baseline prompt.
4. Add a small set of controlled variants (3–5) with one change each.
5. If outputs exist, run a short critique loop and update only the minimal parts of the prompt.

## Output Template

Provide prompts in this format:

- **Base prompt**: …
- **Negatives / avoid**: …
- **Variants**:
  - V1 (change: …): …
  - V2 (change: …): …

## Anti-Patterns

- Adding style fluff before constraints are locked.
- Changing multiple variables per iteration.
- Letting prompts become unbounded essays (token waste).