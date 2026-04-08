# API Endpoint Documentation Template

## Per-Endpoint Template

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

## Documentation Principles

| Principle | Description |
|-----------|-------------|
| **Always include an example** | A table without an example is incomplete |
| **List all status codes** | Document success and every error case |
| **Describe each field** | Type, required/optional, constraints |
| **Show the request AND response** | Never just one side |

## What to Document Per Endpoint

- HTTP method + path
- Brief one-line description
- Authentication required? (note it explicitly)
- Request body fields (table: name, type, required, description)
- Path/query parameters (same table format)
- All possible HTTP responses with descriptions
- At least one complete request + response example
