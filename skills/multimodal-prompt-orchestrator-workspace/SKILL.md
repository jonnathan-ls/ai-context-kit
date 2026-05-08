---
version: 0.1.0
name: multimodal-prompt-orchestrator-workspace
description: Workspace-oriented multimodal prompting workflow with eval folders and repeatable prompt iteration.
allowed-tools: Read, Glob, Grep, Bash
tags: multimodal, orchestration, workspace, evals
---

# Multimodal Prompt Orchestrator (Workspace)

Use this skill when prompts are being developed **inside a repo/workspace** and you want repeatable iteration using local references, eval folders, and structured outputs.

## When to Use

- There is an `iteration-*` directory with eval cases.
- You need a consistent structure for "with_skill" vs "without_skill" comparisons.
- The user wants a reproducible prompt workflow tied to artifacts.

## Workflow

1. Locate the active iteration folder (e.g., `iteration-1/`).
2. For each eval case:
   - Restate constraints.
   - Produce a base prompt + controlled variants.
   - Define what to store as outputs (filenames, metadata).
3. Keep prompts minimal and deterministic.

## Output Format

For each eval case:

- Goal: …
- Constraints: …
- Base prompt: …
- Variants (3 max): …
- What to save: …

## Notes

This skill is intentionally lightweight until the eval harness is formalized.