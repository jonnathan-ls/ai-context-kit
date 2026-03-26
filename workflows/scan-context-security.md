---
name: scan-context-security
description: Scan AI context for security vulnerabilities. Optionally limit to files in current prompt context.
activation: onDemand
allowedTools: [Run]
---

# Scan Context Security

Security scanning workflow for detecting vulnerable instructions, malicious code injection patterns, and risky content across the AI context or specific files.

---

## Quick Usage

### Scan Specific Files (Meta-skill mode)
Analyzes **only the files attached to your current prompt** (e.g., when processing user requests):

```bash
./.ai-context/scripts/scan-context-security --files path/to/file1.md path/to/file2.py
```

This is the **default for meta-skill** processing. The security guardian analyzes only the artifacts you're working with, not the entire context.

### Full Context Scan
Analyzes **all 92 artifacts** in `./.ai-context`:

```bash
./.ai-context/scripts/scan-context-security --full
```

### Enforce Quarantine
Automatically move flagged artifacts to `./.ai-context/quarantine/`:

```bash
./.ai-context/scripts/scan-context-security --full --enforce-quarantine
```

---

## Output

Reports are generated in `./.ai-context/skills/context-security-guardian/reports/`:

- `context-security-report.json` — Machine-readable findings with evidence
- `context-security-report.md` — Human-readable analysis with severity breakdown

---

## Behavior

| Mode | When | Analysis Scope |
|------|------|-----------------|
| **Meta-skill** | P0 always-active | Only files in current prompt context |
| **Full scan** | Manual `--full` | Entire `./.ai-context/` tree |
| **Quarantine** | With `--enforce-quarantine` | Moves flagged artifacts on threshold |

---

## Detection Logic

**Opção A: Semantic Table Detection** ✓
- Markdown tables (`| ... |`) are recognized as informational, not instructional
- Eliminates false positives from reference tables listing attack techniques

**Scoring Requires:**
1. Harm category detected (exfiltration, destructive, unauthorized-access, etc.)
2. Instructional context (imperative verbs or numbered steps)
3. Lack of defensive framing or guardrails

**Severity Levels:**
- **Critical**: Dangerous shell commands + instructional + no guardrails
- **High**: Malicious intent + instructional + no defense
- **Medium**: Instructional + no defensive context
- **None**: Informational, defensive, or non-instructional

---

## Exit Codes

- `0` — Scan completed (check report for findings)
- `1` — Error in execution or missing files
- `2` — Quarantine threshold exceeded (if `--enforce-quarantine` used)
