# Architecture Decision Record (ADR) Template

ADRs capture significant architectural decisions with context and rationale, so future maintainers understand *why*, not just *what*.

## Template

```markdown
# ADR-001: [Short Title of Decision]

## Status
Draft | Proposed | Accepted | Deprecated | Superseded by ADR-XXX

## Context
[Describe the situation that led to this decision. What forces are at play?
What constraints exist? What is the problem being solved?]

## Decision
[State the decision clearly in one or two sentences.]
[Describe the approach chosen.]

## Consequences

**Positive:**
- [Benefit 1]
- [Benefit 2]

**Negative:**
- [Trade-off or cost 1]
- [Trade-off or cost 2]

**Neutral:**
- [Side effect that is neither good nor bad]
```

## Example

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

## Numbering Convention

- Use sequential integers: `ADR-001`, `ADR-002`, etc.
- Store in `/docs/adr/` or `/architecture/decisions/`.
- Never delete ADRs — deprecate or supersede them instead.
- Link superseding ADRs back to the original.
