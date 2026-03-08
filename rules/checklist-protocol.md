---
priority: P0
trigger: always_on
description: Pre-response checklist and final validation gate before delivering any output
---

# Checklist Protocol

## Pre-Response Gate (Run Mentally Before Every Response)

```
┌─────────────────────────────────────────────────────┐
│ RESPONSE GATE                                       │
├─────────────────────────────────────────────────────┤
│ 1. Am I answering ONLY what was asked?              │
│ 2. Did the user ask for code? (if no → no code)     │
│ 3. Did the user ask to modify files? (if no → skip) │
│ 4. Am I confident this is correct?                  │
│ 5. Is every sentence necessary?                     │
│ 6. Am I staying on topic?                           │
│ 7. Am I echoing code that will be written to a file?│
└─────────────────────────────────────────────────────┘
If any gate fails → fix before sending.
```

## Code/File Output Protocol

| Step | Action |
|------|--------|
| 1 | **Describe** — state in plain text WHAT will change and WHERE |
| 2 | **Approve** — wait for explicit user approval (unless already approved) |
| 3 | **Apply** — execute the file operation directly |
| 4 | **Confirm** — one-line confirmation |

**Code Echo Ban:** Never print code in chat AND write it to a file. Apply directly.

## Script / Terminal Command Gate

Before running any terminal command that modifies state:

```
[ ] Does the user know this command will run?
[ ] Is the command reversible?
[ ] Is the exact command visible and readable to the user?
[ ] Are there destructive flags (--force, -rf, DROP, DELETE)?
```

If destructive flags present → state this explicitly before running.

## Final Validation (After Completing Any Task)

```
[ ] Task is fully complete — nothing half-done
[ ] No regressions introduced
[ ] Files not requested were not touched
[ ] Dependencies not requested were not added
[ ] Response is scoped to the request
```
