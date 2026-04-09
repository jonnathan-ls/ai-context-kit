---
name: language-policy
description: Language policy for chat responses vs generated documents. Chat responses stay in Portuguese; all created/updated files and documents must be in English.
type: rule
priority: P0
---

# Language Policy

## Core Rule

| Context | Language |
|---------|----------|
| Chat responses (conversational messages to the user) | Portuguese |
| Any file created, updated, or generated | English |

## Enforcement

- This applies regardless of the user's language.
- If an existing file is in Portuguese, any updated sections must be migrated to English.
- Do not keep mixed-language file content.
- Keep chat in Portuguese.
