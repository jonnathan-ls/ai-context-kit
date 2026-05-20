# Harness Layout

The generated harness uses this minimal structure:

```text
.ai-context/
  MANIFEST.json
  README.md
  config/
    token-budget.json
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
  scripts/
    validate_harness.py
  agents/
  claude/
```

Repository root integration:

- `.agents` symlink to `.ai-context/agents`
- `.claude` symlink to `.ai-context/claude`

Design principles:

- Keep generated docs short and actionable.
- Keep only core rules and skills in MVP.
- Enforce evidence-based validation before completion claims.
- Prefer deterministic checks over best-effort guesses.
