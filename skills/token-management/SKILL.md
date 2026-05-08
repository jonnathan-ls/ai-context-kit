---
version: 1.0.0
name: token-management
description: Token-efficient request processing without reducing task quality. Use this skill whenever the user request is long, multi-part, repetitive, or likely to consume high context window. Also use when optimizing prompts, reducing token costs, preserving output fidelity, or handling large conversational history. Trigger even if the user does not explicitly mention tokens when context compression would improve efficiency.
allowed-tools: Read, Glob, Grep, Bash
tags: token, context, workflow
---

# Token Management

Optimize token usage while preserving the exact intent, constraints, and expected output quality of the user request.

## Core Objective

Produce the same final work quality with or without this skill. The difference must be lower token overhead, faster convergence, and cleaner context flow.

## Non-Negotiable Principles

1. Preserve intent exactly. Never drop user goals, acceptance criteria, constraints, or safety requirements.
2. Compress structure, not meaning. Reduce verbosity and duplication, not substance.
3. Prefer deterministic extraction. Convert long requests into concise, traceable task blocks.
4. Avoid repeated reasoning loops. Reuse stable summaries instead of re-expanding prior context.

## Key Reality: Context Cost Is Multiplicative

In many chat-based LLM tools, each new user message is processed against the *current active context window* (system + rules + skills + files + history). This makes cost and latency feel non-linear:

- One extra message can trigger a re-read of the full context window.
- Large context also reduces quality ("lost in the middle"): models tend to overweight the start and end of long contexts and under-attend the middle.

Practical implication: keep the execution kernel short, stable, and near the top of the conversation.

## Practical Tactics (High ROI)

Apply these tactics before (and during) execution:

1. **Start fresh for unrelated tasks**
	- If the next task is unrelated, prefer a new thread/session instead of dragging history forward.

2. **Reduce bootstrap overhead**
	- Keep always-on docs minimal.
	- Prefer on-demand skills/workflows over putting everything into a single always-loaded file.

3. **Batch requests to avoid micro-turns**
	- Favor one well-scoped message over many small follow-ups.
	- If needed, use `intent-expander` or `spec-normalizer` to consolidate requirements.

4. **Plan first, then implement**
	- Use `context-validator` (harness) + `spec-enforcer` (spec gate) to prevent expensive rework.

5. **Be precise with file targets**
	- Point to exact files/symbols when possible.
	- Prefer workspace-map guided navigation over broad repo-wide searching.

6. **Paste only the minimum context**
	- Avoid full PDFs/threads when only a section matters.
	- Prefer excerpts + links/pointers.

7. **Compact early (before you hit limits)**
	- When context grows large (rule of thumb: ~60%+ full or multiple failed iterations), create a stable summary.
	- Use `token-compressor` for logs/tool output before reasoning.

8. **Avoid multi-agent unless it truly parallelizes work**
	- Each extra agent/session repeats bootstrap overhead.
	- Only parallelize independent subtasks that can be merged cleanly.

9. **Use the cheapest capable model (when selectable)**
	- Reserve expensive models for critical, multi-step reasoning.
	- Use cheaper models for search, classification, formatting, and simple edits.

10. **Turn learnings into on-demand guidance**
	- When a pattern repeats, encode it into a skill/workflow.
	- Keep always-on rules as an index/constitution, not a dumping ground.

## Token Optimization Workflow

### 1. Extract the Execution Kernel

Create a compact task brief before acting:

- Objective: What outcome is required.
- Inputs: Files, data, references, environment facts.
- Constraints: Rules, policies, formatting, scope boundaries.
- Deliverables: Exact outputs expected.
- Validation: How completion will be verified.

If the request includes noise, preserve only information that changes implementation decisions.

### 2. Classify Context by Priority

Tag context into three levels:

- Critical: Required for correctness or safety.
- Supporting: Useful for quality but not mandatory.
- Redundant: Repeated or non-impactful details.

Keep Critical always, keep Supporting in compressed form, remove Redundant.

### 3. Apply Compression Tactics

Use these tactics in order:

1. Deduplicate repeated requirements.
2. Replace verbose paragraphs with precise bullet points.
3. Convert narrative history into a short state snapshot.
4. Keep references as pointers instead of full inlining when possible.
5. Use stable labels for recurring constraints (for example: Scope, Safety, Output Format).

### 4. Budget Tokens by Stage

Allocate token budget intentionally:

- Discovery: Minimal, only what is needed to remove uncertainty.
- Implementation: Focus on concrete edits and verification evidence.
- Reporting: Concise summary of what changed, why, and what was validated.

Do not spend more tokens on explanation than on task execution when the user asked for implementation.

### 5. Response Compaction Rules

When replying:

- Lead with outcomes, then critical details.
- Avoid repeating unchanged plans.
- Avoid restating full instructions already satisfied.
- Use short, direct phrasing.
- Include only actionable next steps.

## Fidelity Safeguards

Before finalizing, confirm all required elements survived compression:

- User goal is unchanged.
- Scope constraints were honored.
- Required files and symbols were addressed.
- Safety and policy constraints were preserved.
- Expected format of the final answer was followed.

If any item is missing, restore relevant context before proceeding.

## Anti-Patterns to Avoid

- Over-compression that removes edge cases.
- Generic summaries that hide acceptance criteria.
- Re-reading large files repeatedly without need.
- Excessive verbose commentary during straightforward tasks.
- Expanding into unsolicited architecture or refactors.

## Execution Checklist

Use this quick checklist during task execution:

- Is this sentence required to complete the user request?
- Is this tool call necessary and scoped?
- Am I repeating context that already exists in a stable summary?
- Am I preserving correctness while reducing verbosity?

If any answer is no, compress further before proceeding.

## Example Trigger Prompts

- "Optimize this long prompt so the AI spends fewer tokens but does the same job."
- "I have a huge request with repeated constraints. Keep quality but reduce token usage."
- "Create a strategy to minimize context window usage without losing requirements."
- "Refactor my AI workflow to avoid token waste across multi-step tasks."

## Expected Behavior

When this skill is active, the AI should:

1. Build a compact execution kernel.
2. Remove redundancy aggressively but safely.
3. Execute with identical functional outcomes.
4. Report with concise, high-signal output.
