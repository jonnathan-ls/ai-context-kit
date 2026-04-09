---
priority: P0
trigger: on_context_load
enforcement: optional_strict_mode
description: Optional strict-mode validation for context artifacts. Default flow uses risk-based checks.
---

# Context Validation Policy (P0)

## Default Mode

Do not validate every artifact on every request.

Use risk-based validation from `skill-loading-gate.md` and `pre-request-skill-blocker.md`.

## Strict Mode

Enable strict validation only when one of these is true:
- User explicitly asks for strict security checks.
- Auditing or hardening `.ai-context` artifacts.
- Executing unknown external scripts.

When strict mode is enabled, validate artifact loads with:

```bash
python3 ./.ai-context/skills/context-security-guardian/scripts/validate_skill.py <artifact-name>
```

## Blocking Thresholds

- Block if any `critical` finding exists.
- Block if two or more `high` findings exist.
- Otherwise continue and report only when requested.

## Performance Rules

- Cache results by artifact hash for the session.
- Reuse previous safe result for unchanged artifacts.
- Keep successful checks silent by default.


