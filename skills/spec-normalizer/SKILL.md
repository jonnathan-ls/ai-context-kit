---
version: 1.0.0
name: spec-normalizer
description: Converts a request into a minimal, testable spec (scope, acceptance criteria, validation) for coding.
allowed-tools: Read, Write, Glob, Grep
tags: spec, planning
---

# Spec Normalizer

Convert an unstructured request into a **minimal spec** that is clear enough for an implementation agent.

## Steps

1. Extract goal, constraints, and non-goals.
2. Convert “wants” into measurable acceptance criteria.
3. Identify key files and dependencies.
4. Define validation steps.

## Output

Produce a spec draft suitable to save under `specs/<name>.md`.

## Spec Skeleton

```markdown
---
name: <spec-name>
version: 0.1.0
description: <one line>
tags: <comma-separated>
status: draft
---

# <Title>

## Scope

## Non-scope

## Acceptance Criteria

## Risks / Open Questions

## Implementation Plan (High Level)

## Validation
```

## Anti-Patterns

- Writing prose without acceptance criteria.
- Skipping validation.
- Turning the spec into a full PRD when not required.
