# Harness Layout

The generated harness uses this minimal structure:

```text
.ai-context/
  MANIFEST.md
  README.md
  config/
    token-budget.md
    protocol.md
  rules/
    code-standards.md
    response-discipline.md
    socratic-gate.md
    workspace-guard.md
  skills/
    context-validator/SKILL.md
    spec-enforcer/SKILL.md
    evidence-checker/SKILL.md
  specs/
    _template.md
    harness-integration.md
```

Repository root integration:

- Optional: document how to point your AI tool to `.ai-context`.
- Optional symlinks:
  - `.agents` -> `.ai-context/agents`
  - `.claude` -> `.ai-context/claude`

Design principles:

- Keep generated docs short and actionable.
- Keep only core rules and skills in MVP.
- Enforce evidence-based validation before completion claims.
- Prefer deterministic checks over best-effort guesses.
