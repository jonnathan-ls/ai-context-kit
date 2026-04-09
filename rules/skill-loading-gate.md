---
priority: P0
trigger: on_skill_load
description: Security gate that scans skills BEFORE they are loaded/processed. Blocks vulnerable skills from activation.
---

# Skill Loading Security Gate (P0)

Use security checks selectively based on artifact risk.

## Risk Tiers

| Tier | Artifact type | Validation |
|------|---------------|------------|
| Tier 0 | Built-in local skill, unchanged, trusted | No scan |
| Tier 1 | Local skill changed in branch/session | Lightweight validation once per session |
| Tier 2 | New, external, downloaded, or user-provided skill | Full scan (blocking) |

## When Validation Is Required

Run validation only for Tier 1 and Tier 2.

Skip validation for Tier 0 unless strict mode is enabled by user.

## Validation Commands

Tier 1:
```bash
python3 ./.ai-context/skills/context-security-guardian/scripts/validate_skill.py <skill-name>
```

Tier 2:
```bash
./.ai-context/scripts/scan-context-security --files skills/<skill-name>/SKILL.md
```

## Result Policy

| Finding | Action |
|---------|--------|
| **Critical** | ❌ Block activation |
| **2+ High** | ❌ Block activation |
| **1 High** | ⚠️ Warn and require explicit confirmation |
| **Medium/Low/None** | ✅ Continue |

## Caching


- Cache results by `<skill-name>:<hash>`.
- Do not re-scan unchanged artifacts in the same session.

## Reporting

- Report details only for blocked results or explicit user requests.
- Keep successful checks silent.

This rule applies to skill loading only. Broader artifact validation policy is defined in `skill-preload-validator.md`.
