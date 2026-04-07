---
name: documentation-templates
description: Documentation templates and structure specialist. Use this skill whenever the user needs to write or improve documentation — README files, API references, code comments, changelogs, ADRs, or AI-friendly docs. Triggers on "write a README", "document this API", "add a changelog", "create an ADR", "how to comment this code", "llms.txt", "document the project", "improve the docs". Provides ready-to-use Markdown templates with structure principles and examples.
---

# Documentation Templates

Templates and structural guidelines for every common documentation type. Start from the right template, adapt to the project's needs, and follow the principles for scannable, maintainable docs.

## When to Use

- User needs to write or improve a README
- User needs an API endpoint documentation template
- User wants to document code with JSDoc/TSDoc
- User needs a changelog structure (Keep a Changelog)
- User is creating an Architecture Decision Record (ADR)
- User needs AI-crawler-friendly documentation (`llms.txt`, MCP-ready content)

## Template 1 — README

### Essential Sections

| Section | Purpose |
|---------|---------|
| **Title + One-liner** | What is this? |
| **Quick Start** | Running in under 5 minutes |
| **Features** | What can I do with it? |
| **Configuration** | How to customize |
| **API Reference** | Link to detailed docs |
| **Contributing** | How to help |
| **License** | Legal |

### README Template

```markdown
# Project Name

Brief one-line description.

## Quick Start

\`\`\`bash
npm install
npm run dev
\`\`\`

## Features

- Feature 1
- Feature 2

## Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| PORT | Server port | 3000 |
| DATABASE_URL | Database connection string | — |

## Documentation

- API Reference: docs/api.md
- Architecture: docs/architecture.md

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

MIT
```

## Template 2 — API Endpoint Documentation

### Per-Endpoint Template

```markdown
## POST /users

Create a new user account.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| email | string | Yes | User email address |
| name | string | Yes | Display name |

**Response:**
- `201 Created` — User created, returns user object
- `400 Bad Request` — Validation error
- `409 Conflict` — Email already registered

**Example:**
\`\`\`json
POST /users
{ "email": "user@example.com", "name": "Jane" }

201 Created
{ "id": "usr_123", "email": "user@example.com", "name": "Jane" }
\`\`\`
```

## Template 3 — Code Comments (JSDoc/TSDoc)

### When to Comment

| Comment | Skip Comment |
|---------|-------------|
| Business logic that isn't obvious | What the code clearly does |
| Complex algorithms | Simple getters/setters |
| Non-obvious side effects | Framework boilerplate |
| API contracts and invariants | Self-explanatory code |

### JSDoc/TSDoc Template

```typescript
/**
 * Calculates the discounted price for a subscription tier.
 * Applies regional pricing rules before the discount.
 *
 * @param basePrice - Original price in cents
 * @param discountRate - Discount as a decimal (0.2 = 20% off)
 * @param region - ISO country code for regional pricing
 * @returns Final price in cents after discount and regional adjustment
 * @throws {InvalidDiscountError} When discountRate is outside 0-1 range
 *
 * @example
 * const price = calculatePrice(1000, 0.2, 'BR'); // 800
 */
```

## Template 4 — Changelog (Keep a Changelog)

```markdown
# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added
- New feature description

## [1.2.0] - 2026-03-15

### Added
- User profile avatars

### Changed
- Improved search response time by 40%

### Fixed
- Resolved race condition in payment processing

### Deprecated
- Legacy `/v1/auth` endpoints (use `/v2/auth`)

## [1.0.0] - 2026-01-01

### Added
- Initial release
```

## Template 5 — Architecture Decision Record (ADR)

```markdown
# ADR-001: Use PostgreSQL as Primary Database

## Status
Accepted

## Context
The application requires ACID transactions for payment data.
NoSQL options evaluated (MongoDB, DynamoDB) do not provide
sufficient transactional guarantees for financial operations.

## Decision
Use PostgreSQL 16 as the primary database. Redis retained
for session storage and rate limiting only.

## Consequences

**Positive:**
- Full ACID compliance for payment records
- Strong ecosystem (Prisma ORM, pgvector for AI features)

**Negative:**
- Higher operational complexity vs. serverless DB options
- Schema migrations required for structural changes
```

## Template 6 — AI-Friendly Documentation

### llms.txt Template

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

### MCP-Ready Documentation Principles

- Clear H1-H3 hierarchy (crawlers use headings for chunking)
- JSON/YAML code blocks for data structures (machines parse these)
- Self-contained sections (each section should make sense in isolation)
- Mermaid diagrams for flows (rendered by some crawlers)

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
