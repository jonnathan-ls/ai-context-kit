# Technical Specification Templates

These templates are standard structures you (the SDD Expert) must use when drafting Technical Specifications based on PRD requirements. They are optimized for downstream consumption by AI coding agents.

---

## 1. System Architecture Specification (`architecture-spec.md`)
**Use when detailing high-level technical decisions, data models, tech stack, and overall flow.**

```markdown
# [Project Name] - System Architecture Spec

## 1. Goal
What this architecture enables (refer to PRD goals).

## 2. Technology Stack & Tooling
- Frontend:
- Backend:
- Database:
- AI Providers/Models:
- Infrastructure/Deployment:

## 3. High-Level System Design
Describe the main moving parts. Use Mermaid.js sequence or class diagrams if useful.

## 4. Core Data Entities
List the primary data models, schemas, relationships, and constraints.
- `Entity A`: Description, primary fields.
- `Entity B`: Description, foreign keys, constraints.

## 5. Security & Authentication Requirements
- Auth flows:
- Data compliance/privacy considerations:

## 6. Non-Functional Decisions
- Scalability, Logging, Error boundaries.
```

---

## 2. API Contract & Integration Specification (`api-spec.md`)
**Use when focusing on communication boundaries (REST, GraphQL, tRPC, WebSockets).**

```markdown
# [Feature/Service Name] - API Contract Spec

## 1. Overview
The purpose of this boundary.

## 2. Endpoints / Mutations
List every needed operation.

### [Method] `/path/to/resource` (e.g., POST `/api/v1/users`)
- **Description:** What it does.
- **Authorization:** Who can call this (roles).
- **Request Payload:** JSON Schema / Types.
  ```json
  {
    "field": "type"
  }
  ```
- **Response Shape (Success):** JSON Schema / Types.
- **Error States & Status Codes:** Ex: `400 Bad Request` if field X is missing.

## 3. Third-Party Integrations
Describe limits, rate-limits, caching, webhooks for external tools (e.g., Stripe, LLM APIs).
```

---

## 3. AI/Agent Workflow Specification (`agent-workflow-spec.md`)
**CRITICAL for AI-assisted products. Defines agent logic, prompts, tools, and error recovery.**

```markdown
# [Agent Name] - Workflow Spec

## 1. Identity & Purpose
- **System Role:** The persona or job of the agent.
- **Trigger Condition:** When does this agent run? User action? Cron job?

## 2. State & Memory Management
- **Short-term Memory (Context Window):** What context is passed in every call?
- **Long-term Memory (Vector DB/Relational):** What does the agent remember across sessions?

## 3. Available Tools (Functions/Functions Calling)
List tools the agent has access to, with descriptions.
- `Tool A`: Parameters, constraints.
- `Tool B`: State changes it triggers.

## 4. Workflow Lifecycle
Describe the sequence (e.g., User Prompt \-> RAG Context Retrieval \-> LLM Call \-> Tool Execution \-> Final Answer).
*Include a Mermaid Flowchart.*

## 5. Fallback & Failure Modes
- What if the LLM refuses to answer (Safety triggers)?
- What if the tool fails? Define retry logic.
- Token limit strategies (Truncation, Summarization).
```

---

## 4. Component & Feature Specification (`component-spec.md`)
**Use for granular frontend or backend features. Highly detailed for specific coding agents.**

```markdown
# [Component/Feature Name] - Component Spec

## 1. Scope
What this component specifically does.

## 2. State & Data Dependencies
- Local State (e.g., expanded/collapsed).
- Global State (e.g., user profile, cart).
- Prop definitions (if UI) or Interface definitions (if Backend logic module).

## 3. Business Logic & Edge Cases
Detailed "If/Then" logic.
- Scenario A: Result A
- Scenario B: Result B

## 4. Technical Constraints
- Performance considerations (e.g., debouncing inputs).
- Accessibility (a11y) requirements.
- Error handling behavior.
```

## How to Apply These Templates
1. Tailor the sections to the specific PRD context. You don't need every section if it's not applicable, but you *must* cover edge cases, data structures, and constraints.
2. Produce markdown directly in the appropriate folder for coding agents to read.