---
name: study-notes-writer
description: Proactive study notes generator. Use this skill whenever a technical concept has been explained and understood in a learning or educational interaction. Triggers on "entendi", "faz sentido", explicit study note requests, or when expert-educator completes an explanation. Converts knowledge established in chat into structured, persistent Markdown notes inside a studies/ directory, organized by domain and numbered sequentially.
---

# Study Notes Writer

Proactive scribe for learning sessions. When a concept is solidified in chat, converts it into concise, imperative, student-voice notes — not professor summaries.

## When to Activate

Activate proactively when any of these signals appear:

| Signal | Example |
|--------|---------|
| Comprehension confirmed | "entendi", "faz sentido", "got it", "makes sense" |
| Explanation concluded | `expert-educator` finishes a Feynman explanation |
| Q&A block ends | A topic-specific back-and-forth reaches a conclusion |
| Explicit request | "salva isso como nota", "create a study note" |

Do NOT activate on every message. Only when a knowledge block is genuinely consolidated.

## Execution Protocol

1. **Announce** — Tell the user a study note is about to be created/updated.
2. **Search** — Use `Glob` or `Read` to list existing directories and files under `studies/`.
3. **Decide** — Place the note in an existing domain folder or create a new one.
4. **Write** — Create or update the `.md` file with the content standard below.
5. **Confirm** — Report the file path to the user.

## Note Content Standard

Write in the **student's active voice** — as if the student is writing in their own notebook. Not lecture transcripts.

```
✅  "poll() monitors multiple file descriptors simultaneously."
❌  "poll() is a syscall that the professor explained can be used to..."
```

### Standard File Structure

```markdown
# [Topic Name] — Study Notes

## What It Is / What It Does
- [Direct, imperative statement]
- [Direct, imperative statement]

## How It Works
- [Step or principle 1]
- [Step or principle 2]

## Critical Rules / Constraints
- **[Rule Name]:** [Consequence if violated]

## Common Traps (Do Not Forget)
- [Pitfall 1 — stated directly]
- [Pitfall 2 — stated directly]

## Next Learning Step
- Study next: [Related concept to explore]
```

## File and Folder Conventions

### Directory Structure

```
studies/
├── 01-http-protocol/
│   ├── 01-overview.md
│   └── 02-methods-and-status.md
├── 02-sockets/
│   └── 01-port-binding.md
└── 03-databases/
    ├── 01-acid-properties.md
    └── 02-indexes.md
```

### Naming Rules

| Element | Convention |
|---------|-----------|
| Domain folder | `NN-domain-name/` — kebab-case, numbered to preserve learning order |
| File inside folder | `NN-topic-name.md` — numbered sequentially within the domain |
| Case style | Always kebab-case with hyphens — never underscores |

### Folder Decision Protocol

1. Search `studies/` for existing domain folders.
2. If the topic fits an existing domain → add file at next available number.
3. If the topic is a new domain → create a new numbered domain folder.
4. If a file on the same topic already exists → update it instead of creating a duplicate.
5. Keep folders at 3-8 files. If over 8, suggest a subdivision to the user.

## Integration with Other Skills

| Skill | Relationship |
|-------|-------------|
| `expert-educator` | Primary partner — notes follow after each Feynman explanation |
| `knowledge-integrator` | Complementary — `knowledge-integrator` updates project docs; this skill generates learner notes |
| `brainstorming` | If a brainstorm crystallizes a concept, notes can capture it |

## Anti-Patterns

- **Do not** write in the professor's voice. Notes belong to the student.
- **Do not** copy the chat verbatim. Distill to essential, actionable statements.
- **Do not** create duplicate notes. Always check if the topic file exists first.
- **Do not** activate on every message. Only when a knowledge block is genuinely complete.
- **Do not** skip the domain folder structure. Flat `studies/` directories become unnavigable.
