---
version: 1.0.0
name: harness-generator
description: Generates a portable, MD-only repository harness using AI-guided protocol logic (no scripts). Use this whenever the user wants a protocol that guides AI execution with senior-level quality, safety, and performance without depending on AI-Context or local automation.
allowed-tools: Read, Write, Glob, Grep
tags: harness, protocol, quality, safety, architecture, performance
---

# Harness Generator

Use this skill to create a clean, portable, MD-only harness for a repository.

The harness is generated under `.ai-context` in the target repository and is designed to work standalone.

## When to use

- The user wants a protocol to guide future AI requests.
- The repository does not yet have a structured rules/skills/specs layout.
- The user asks for repeatable quality and safety gates.
- The user wants a lean setup that avoids context bloat.

## What this skill creates

- `.ai-context/rules/` with core governance rules.
- `.ai-context/skills/` with core operational skills.
- `.ai-context/specs/` with templates and integration guidance.
- `.ai-context/MANIFEST.md` and `.ai-context/config/token-budget.md`.
- Optional root links to expose the harness to AI tools:
	- `.agents` -> `.ai-context/agents`
	- `.claude` -> `.ai-context/claude`

## Execution flow

1. Start a full wizard interview with the user (see Wizard section).
2. Summarize the decisions and get confirmation.
3. Select the minimal set of rules, skills, and specs (hybrid selection).
4. Generate the harness files as `FILE: path` blocks.
5. Provide a minimal validation checklist and symlink steps.

## Output format

Always output:

1. A `MANIFEST` block (JSON-like) with `profile`, `selected`, and `files`.
2. One `FILE: <path>` block per file.
3. A `CHANGE PLAN` with exact steps.
4. A `VALIDATION` checklist.

## Output contract

The generated `MANIFEST` must include:

- project profile (type, stack, strictness)
- selected rules and skills
- file inventory for generated artifacts
- version and timestamp

## Blocking conditions

Stop and ask for confirmation when:

- target path already contains unrelated files
- symlink destination conflicts with existing non-symlink paths
- required metadata cannot be derived from the repository

## Anti-patterns

- Generating every available skill "just in case".
- Copying bulky references without a clear trigger.
- Skipping validation and claiming the harness is production-ready.

## AI-first usage (MD-only)

This skill is intentionally authored so an LLM can *use the skill text itself* (the `SKILL.md` and the small templates in `references/`) to *generate a harness mentally* and then output the files as content blocks for the user to apply. Do not require any scripts.

When you (the model) are using this skill to produce a harness for a target repository, follow this strict flow:

1. Discovery: read the provided `profile` (if any) and the repository summary (or ask for the top 3 files to inspect). If missing, infer stack by file names.
2. Clarify: ask up to 2 targeted questions if the end-state, scope, or required files are ambiguous. If a blocking condition remains, return `BLOCK` and list the missing inputs.
3. Select minimal items: choose at most 3 rules and 3 skills for the MVP harness. Explain why each was chosen in one sentence and ask the user to confirm the selection.
4. Produce file manifest: return a JSON-like `MANIFEST` describing `files: [{path, reason}]` and `profile` + `selected` lists.
5. For each file in the manifest, output the full file content inside a fenced block with a header line exactly like: `FILE: <relative/path>` followed by the file content. Example:

```
FILE: .ai-context/rules/code-standards.md
# Code Standards
# ...rest of file content...
```

6. Provide a `CHANGE PLAN`: list the exact actions the user (or an automation) should take to apply the harness (create folder, write files, create symlinks). Keep it minimal and idempotent.
7. Provide a short `VALIDATION` checklist the AI will use after creation (which commands to run or what to check). If you have no runtime access, list the exact validator expectations so a human can run them.

Do NOT run or depend on any generator during this flow. The AI's output must be self-contained: file contents + manifest + plan + validation instructions.

### Output conventions for models

- Always include the manifest first as a JSON block.
- Then include each file as `FILE: path` + fenced content (no extra commentary inside the code fences).
- Keep each file under 500 lines when possible; if longer, provide a TOC and deliver only the most relevant sections.
- Use conservative token budgets: prefer targeted small files over dumping large reference docs.

## Wizard interview (required)

Run this wizard step-by-step. Ask each question separately and wait for the answer before moving on.

Required questions:

1. Project type (app, api, library, monorepo, other).
2. Primary stack and language (e.g., node, python, go, rust, frontend).
3. Strictness level (balanced or strict).
4. Primary goals (quality, safety, performance, scalability, resilience, product speed).
5. Scope boundaries (what the harness must include and must not include).
6. Known constraints or existing conventions to respect (style, tests, architecture).
7. Required tool integrations (if any) for `.agents` or `.claude` usage.

After collecting answers:

- Summarize the decisions in 5-7 bullets.
- Propose the hybrid selection defaults (rules/skills/specs).
- Ask for confirmation before generating files.

If you want, I can convert the existing templates into explicit `FILE:` content blocks inside `references/` (ready-made snippets) so the model can paste them verbatim into the target repo when generating the harness.
