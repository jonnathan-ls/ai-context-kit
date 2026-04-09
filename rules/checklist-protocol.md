---
priority: P0
trigger: always_on
description: Pre-response checklist and final validation gate before delivering any output
---

# Checklist Protocol

## Execution Gate (Before State Changes)

Before running commands that modify state:

- Confirm the command is required for the user's request.
- Confirm the command is visible and understandable.
- Call out destructive flags explicitly (`--force`, `-rf`, `DROP`, `DELETE`).
- Prefer reversible and minimal actions.

## Response Gate (Before Reply)

- Answer only what was asked.
- Keep output concise and on-topic.
- Avoid repeating code that is already written to files.
- Be explicit about uncertainty when confidence is low.

## Post-Task Gate (Before Completion)

- Requested task is fully complete.
- No unintended files were changed.
- New errors introduced by edits were checked and handled.
- Outcome is clearly communicated to the user.
