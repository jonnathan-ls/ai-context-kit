---
name: documentation-templates
description: Documentation templates and structure specialist. Use this skill whenever the user needs to write or improve documentation — README files, API references, code comments, changelogs, ADRs, or AI-friendly docs. Triggers on "write a README", "document this API", "add a changelog", "create an ADR", "how to comment this code", "llms.txt", "document the project", "improve the docs". Provides ready-to-use Markdown templates with structure principles and examples.
---

# Documentation Templates

Templates and structural guidelines for every common documentation type. Start from the right template, adapt to the project's needs, and follow the principles for scannable, maintainable docs.

## Template Index

| Template | File | When to Use |
|----------|------|-------------|
| README | [readme-template.md](readme-template.md) | New project or missing README |
| API Endpoint | [api-docs-template.md](api-docs-template.md) | Document REST endpoints |
| Code Comments | [code-comments-guide.md](code-comments-guide.md) | JSDoc/TSDoc, when to comment |
| Changelog | [changelog-template.md](changelog-template.md) | Release history tracking |
| ADR | [adr-template.md](adr-template.md) | Architecture Decision Records |
| AI-Friendly Docs | [ai-friendly-docs.md](ai-friendly-docs.md) | llms.txt, MCP-ready content |

## Structure Principles

| Principle | Why |
|-----------|-----|
| **Scannable** | Most readers skim first — headers, lists, tables |
| **Examples first** | Show the output before explaining the mechanism |
| **Progressive detail** | Simple → Complex (don't front-load complexity) |
| **Up to date** | Outdated docs are worse than no docs |
| **One source of truth** | Avoid duplicating content across files |

## Anti-Patterns

- **Do not** copy-paste templates verbatim. Adapt every section to the actual project.
- **Do not** write documentation for code that is self-explanatory.
- **Do not** maintain separate docs that duplicate what is in the README.
- **Do not** leave `[placeholder]` sections in published documentation.
- **Do not** omit examples from API documentation — a table without an example is incomplete.
