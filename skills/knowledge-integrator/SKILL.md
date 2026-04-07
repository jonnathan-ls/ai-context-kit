---
name: knowledge-integrator
description: Documentation synchronization specialist. Use this skill whenever a structural decision, architectural change, new persona, business pivot, or important rule has been established in the chat and the project's base documentation files may now be outdated. Triggers on "update the docs", "we decided to change", "new rule going forward", "add this to the architecture", "our persona changed", "keep the docs in sync". Identifies impacted files, generates a precise diff proposal, and waits for explicit user approval before applying any changes.
---

# Knowledge Integrator

Proactive documentation synchronization guardian. Detects when chat decisions diverge from the project's source-of-truth files and surfaces exact update proposals — never modifying files without explicit approval.

## When to Use

- An architectural decision was made in chat (e.g., "we're switching to PostgreSQL")
- A new business rule was established (e.g., "payments are now handled by Stripe")
- A persona or target audience changed
- A UI/UX guideline was defined or revised
- A significant convention was agreed upon that isn't yet in the docs
- The user says "remember this going forward" or "add this to our docs"

## Execution Protocol

Follow these steps in order every time:

1. **Identify** — Determine what structural knowledge was just established in the chat.
2. **Search** — Use `Read`, `Glob`, or `Grep` to locate the actual documentation files affected (check `/docs`, `/architecture`, root `.md` files, `CLAUDE.md`, `README.md`, etc.).
3. **Diff** — For each impacted file, produce a precise before/after proposal showing exactly what to add, change, or remove.
4. **Report** — Output the Knowledge Integration Alert (see format below).
5. **Wait** — Do NOT modify any file until the user explicitly approves.
6. **Apply** — After approval, execute the patch using `Edit` or `Write`.

## Knowledge Integration Alert Format

```
### Knowledge Integration Alert

**Established Decision:**
[One-sentence summary of the new rule, decision, or discovery]

**Outdated Documentation:**
- `path/to/file.md` — [What is now stale and why]
- `path/to/other.md` — [What section needs revision]

**Proposed Updates (awaiting approval):**

File: `path/to/file.md` — Section: "Architecture"
- REMOVE: "We use MongoDB for all data storage."
- ADD: "Primary database is PostgreSQL (migrated Q2 2026). MongoDB retained for legacy event logs only."

---
Reply "Approved" or adjust the proposals above, and I will apply the changes.
```

## Detection Triggers

Proactively activate this skill when the user says or implies:

| Signal | Example |
|--------|---------|
| Decision language | "We decided to...", "Going forward we will..." |
| Rule establishment | "From now on, always...", "The rule is..." |
| Change announcement | "We're switching to...", "We dropped X in favor of Y" |
| Explicit doc request | "Add this to the docs", "Update the README" |
| Persona update | "Our new target user is...", "The audience changed to..." |

## File Discovery Strategy

When searching for impacted files:

```
1. Check root: README.md, CLAUDE.md, .ai-context/
2. Check /docs, /architecture, /specs directories
3. Grep for the keyword or concept being changed
4. List all .md files at the project root
```

Example search pattern:
```bash
grep -r "MongoDB" docs/ README.md --include="*.md" -l
```

## Scope Rules

| Allowed | Not Allowed |
|---------|-------------|
| Propose exact text changes | Modify files without approval |
| Read any documentation file | Invent documentation that doesn't exist |
| Suggest new sections or files | Create files without approval |
| Report what is stale and why | Act on low-confidence signals without asking |

## Integration with Other Skills

- **`study-notes-writer`**: Complementary — `study-notes-writer` generates learner notes; `knowledge-integrator` updates project documentation.
- **`expert-educator`**: After a technical explanation, check if project docs need updating.
- **`brainstorming`**: After decisions solidify from a brainstorm session, surface impacted docs.

## Anti-Patterns

- **Do not** modify files silently. Every change requires an explicit approval signal from the user.
- **Do not** activate on every message. Only trigger when a genuine structural decision was made.
- **Do not** guess file paths. Search and verify they exist before including them in the report.
- **Do not** propose stylistic or cosmetic changes. Only sync structural, factual, or rule-based knowledge.
- **Do not** generate fictional documentation. Proposals must be grounded in what was actually decided in the conversation.
