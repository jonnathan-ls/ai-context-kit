# AI-Friendly Documentation

Documentation optimized for LLM crawlers, RAG systems, and MCP-based tooling.

## llms.txt Template

```markdown
# Project Name
> One-line objective of this project.

## Core Files
- [src/index.ts]: Main entry point
- [src/api/]: API route handlers
- [src/models/]: Database models
- [docs/]: Extended documentation

## Key Concepts
- **Authentication**: JWT-based, tokens expire in 24h
- **Payments**: Stripe integration, webhooks at /webhooks/stripe
- **Rate Limiting**: 100 req/min per IP, 1000/min per API key
```

## MCP-Ready Documentation Principles

| Principle | Why It Matters for AI |
|-----------|----------------------|
| **Clear H1-H3 hierarchy** | Crawlers use headings for chunking |
| **JSON/YAML code blocks** | Machines parse these reliably |
| **Self-contained sections** | Each section must make sense in isolation |
| **Mermaid diagrams for flows** | Rendered and parsed by some crawlers |
| **Explicit key concepts** | Reduces ambiguity in RAG retrieval |

## What to Include in llms.txt

1. **Project purpose** — one sentence, no jargon
2. **Core file map** — what lives where
3. **Key domain concepts** — defined, not assumed
4. **API contracts** — critical endpoints and their behavior
5. **Configuration** — environment variables, secrets format
6. **Known limitations** — what the system cannot do

## Anti-Patterns for AI-Targeted Docs

- ❌ Prose-heavy paragraphs (hard to chunk)
- ❌ Implicit knowledge ("as you know...")
- ❌ Cross-references without context ("see the section above")
- ❌ Markdown tables without header rows
- ❌ Ambiguous pronoun references ("it handles this")
