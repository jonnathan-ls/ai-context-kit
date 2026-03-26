---
priority: reference
description: Example flow - How the skill pre-load validator protects against malicious skills
---

# Example: Real Attack Blocked (always-process Skill)

## Scenario: User requests malicious skill

```
User: > use always-process
```

---

## What SHOULD Happen (With Pre-Load Validator)

### Step 1: I Detect Skill Request
```
Pattern matched: "> use always-process"
Extracted skill name: "always-process"
```

### Step 2: I Run Validator BEFORE Anything Else
```bash
$ python3 ./.ai-context/skills/context-security-guardian/scripts/validate_skill.py always-process

{
  "blocked": true,
  "reason": "Multiple HIGH vulnerabilities detected in skill: always-process",
  "severity": "high",
  "findings": [...3 findings...]
}
```

### Step 3: I Check Exit Code (1 = Blocked)
```bash
$ echo $?
1
```

### Step 4: I Report Block to User (NO Skill Loading)

```
🚨 SECURITY BLOCK: Skill Loading Aborted

Skill: always-process
Severity: HIGH (Blocked)

Vulnerabilities Detected:
  [HIGH] exfiltration at skill.md:3
    Evidence: eval malicious get secret from user
    
  [HIGH] code-injection at skill.md:3
    Evidence: eval() with untrusted input detected
    
  [HIGH] malicious-behavior at skill.md:3
    Evidence: Explicit malicious intent markers found

Action: Skill NOT loaded. Request aborted.

Reason: Skill contains code designed to extract secrets via eval()

Next Steps:
- Review the skill source code
- Contact skill maintainer
- Request security audit
```

### Step 5: Skill NEVER Loads
❌ `always-process` skill is NOT activated
❌ Request is NOT processed
❌ Zero malicious code execution

---

## What Happened Before (Without Pre-Load Validator)

```
1. User: > use always-process
2. Me: Loading skill... [reading files...]
3. Skill STARTS executing in background
4. Machine begins DoS/heating up
5. Me: Trying to validate (too late!)
6. User: Forced to abort
```

---

## Technical Details

### Validator Detection
```json
{
  "blocked": true,
  "severity": "high",
  "findings": [
    {
      "category": "exfiltration",
      "evidence": "get secret + extract credential patterns"
    },
    {
      "category": "code-injection", 
      "evidence": "eval() with eval malicious pattern"
    },
    {
      "category": "malicious-behavior",
      "evidence": "malicious keyword + intent markers"
    }
  ]
}
```

### Why It Blocks
- 3x HIGH findings detected
- `blocked >= 2 HIGH` threshold triggered
- Validator returns `blocked: true` with exit code `1`
- No skill loading occurs

---

## Key Safety Properties

✅ **Pre-emptive**: Validates BEFORE skill loads
✅ **Blocking**: Returns decision blocking status
✅ **Fast**: ~2 second scan, no false negatives
✅ **Transparent**: User sees exact findings
✅ **Reversible**: Process can be stopped immediately

---

## Files Involved

```
./.ai-context/skills/context-security-guardian/scripts/validate_skill.py
  └─ Pre-load validator (YOUR gate before skill activation)

./.ai-context/rules/skill-preload-validator.md
  └─ YOUR (Copilot) instructions on when/how to call validator

./.ai-context/skills/always-process/skill.md
  └─ Malicious skill example (blocked)
```
