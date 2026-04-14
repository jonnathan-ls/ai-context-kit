# AI Context Control

Quick reference for enabling/disabling AI context processing.

## Overview

Control whether AI tools process your context (skills, agents, rules, workflows) without removing the files.

**When to disable:**
- You want to save tokens and focus on pure AI reasoning
- Testing pure AI capability without framework interference
- Temporary focus session on specific tasks
- Manual control over context consumption

## Quick Commands

```bash
# Check status
aictx context status

# Disable context
aictx context disable
aictx sync  # Regenerate ALWAYS.md

# Enable context
aictx context enable
aictx sync  # Regenerate ALWAYS.md

# Toggle on/off
aictx context toggle
aictx sync
```

## What Happens

### When Enabled (Default)
- AI tools process all skills, agents, rules, and workflows
- ALWAYS.md contains full context protocol, meta-skills, and references
- Token consumption includes context processing

### When Disabled
- AI tools do not process any context from ~/.ai-context
- ALWAYS.md contains a minimal "disabled" stub
- Saves tokens on context processing overhead
- Pure AI reasoning without framework context

## State File

Context state persists in `.aictx_state.json`:

```json
{
  "context_enabled": true
}
```

This file is automatically created on first use.

## Example Sessions

### Session 1: Focus Mode
```bash
# Before a focused session
aictx context disable
aictx sync

# Work with AI for an hour
# No context processing, pure AI

# Done, re-enable
aictx context enable  
aictx sync
```

### Session 2: Token Optimization
```bash
# Check current state
aictx context status

# If working on multiple tasks that don't need context:
aictx context disable
aictx sync

# Disable for batch processing
# Process multiple requests without context overhead

# When ready to use full capabilities:
aictx context toggle
aictx sync
```

### Session 3: Testing
```bash
# Test AI reasoning without context
aictx context disable
aictx sync

# Run tests, iterate, verify behavior

# Switch back to full context when needed
aictx context enable
aictx sync
```

## Integration

The context state is checked by:
- `aictx sync` — generates disabled stub if context is off
- All AI tools reading ALWAYS.md — see the disabled notice

No manual ALWAYS.md editing needed — state management is automatic.

## Troubleshooting

**Q: My context is still loading**
- Run `aictx sync` after disabling/enabling to regenerate ALWAYS.md

**Q: How do I verify the state?**
- `aictx context status`
- `cat ~/.ai-context/.aictx_state.json`
- `head -20 ~/.ai-context/rules/ALWAYS.md` to see if disabled or full

**Q: Can I delete .aictx_state.json?**
- Yes, it will be recreated with default (enabled) on next run

**Q: Does this affect archived skills?**
- No, archived items are already excluded from ALWAYS.md regardless of this setting

## See Also

- [README.md](./README.md) — Full documentation
- `aictx context --help` — Command help
