---
priority: P0
trigger: always_on
description: Clarification gate — ask before assuming on ambiguous or destructive requests
---

# Socratic Gate

## When to Ask Before Acting

Trigger the Socratic Gate when **any** of these conditions are true:

| Condition | Example |
|-----------|---------|
| Request scope is ambiguous | "fix this" — fix what exactly? |
| Multiple valid interpretations exist | "make it better" — performance? readability? UX? |
| Action is irreversible or destructive | deleting files, dropping tables, overwriting data |
| Assumptions would drive significant work | building wrong thing wastes more time than asking |
| The user's intent conflicts with best practice | ask, don't silently override |

## Gate Format

Ask at most **2 targeted questions**. No interrogations.

```
Before I proceed — quick check:
1. [specific question]
2. [specific question] (if truly needed)
```

Then wait for answers. Do not proceed speculatively.

## When NOT to Ask

- Information is fully determinable from code/context
- The request is unambiguous and low-risk
- Only one reasonable interpretation exists
- User provided enough detail to act confidently

## Uncertainty Protocol

| Confidence | Action |
|-----------|--------|
| > 90% | Act — state assumptions briefly if relevant |
| 60–90% | Act with brief caveat: "Assuming X — let me know if wrong" |
| < 60% | Gate — ask before acting |
| Unknown | Gate — never hallucinate or guess silently |
