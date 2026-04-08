---
name: python-patterns
description: Python development principles and decision-making. Framework selection, async patterns, type hints, project structure. Use this skill whenever the user is building Python applications, choosing frameworks, applying type hints, or designing project structure. Triggers on Python, FastAPI, Django, asyncio, type hints, Pydantic, pip, virtual environment.
---

# Python Patterns

> Python development principles and decision-making for 2025.
> **Learn to THINK, not memorize patterns.**

---

## How to Use This Skill

- ASK user for framework preference when unclear
- Choose async vs sync based on CONTEXT
- Read only the files relevant to the task

## Reference Files

| Need | File |
|------|------|
| Choose framework | [framework-selection.md](framework-selection.md) |
| Async vs sync decision | [async-patterns.md](async-patterns.md) |
| FastAPI patterns | [fastapi-guide.md](fastapi-guide.md) |
| Django patterns | [django-guide.md](django-guide.md) |
| Background tasks | [background-tasks.md](background-tasks.md) |
| Testing strategy | [testing-guide.md](testing-guide.md) |

---

## Type Hints Strategy

### When to Type

```
Always type:
├── Function parameters
├── Return types
├── Class attributes
├── Public APIs

Can skip:
├── Local variables (let inference work)
├── One-off scripts
├── Tests (usually)
```

### Common Type Patterns

```python
# Optional → might be None
from typing import Optional
def find_user(id: int) -> Optional[User]: ...

# Union → one of multiple types
def process(data: str | dict) -> None: ...

# Generic collections
def get_items() -> list[Item]: ...
def get_mapping() -> dict[str, int]: ...
```

### Pydantic for Validation

```
Use Pydantic when:
├── API request/response models
├── Configuration/settings
├── Data validation
└── Serialization

Benefits:
├── Runtime validation
├── Auto-generated JSON schema
├── Works with FastAPI natively
└── Clear error messages
```

---

## Project Structure Principles

```
Small project / Script:
├── main.py
├── utils.py
└── requirements.txt

Medium API:
├── app/
│   ├── main.py
│   ├── models/
│   ├── routes/
│   ├── services/
│   └── schemas/
├── tests/
└── pyproject.toml

Large application:
├── src/
│   └── myapp/
│       ├── core/
│       ├── api/
│       ├── services/
│       └── models/
├── tests/
└── pyproject.toml
```

---

## Error Handling Principles

```
In FastAPI:
├── Create custom exception classes
├── Register exception handlers
├── Return consistent error format
└── Log without exposing internals

Pattern:
├── Raise domain exceptions in services
├── Catch and transform in handlers
└── Client gets clean error response
```

### Error Response Philosophy

```
Include:
├── Error code (programmatic)
├── Message (human readable)
├── Details (field-level when applicable)
└── NOT stack traces (security)
```

---

## Anti-Patterns

- ❌ Default to Django for simple APIs — use FastAPI
- ❌ Use sync libraries in async code
- ❌ Skip type hints for public APIs
- ❌ Put business logic in routes/views
- ❌ Ignore N+1 queries
- ❌ Mix async and sync carelessly

---

## Decision Checklist

Before implementing:

- [ ] **Asked user about framework preference?**
- [ ] **Chosen framework for THIS context?** (not just default)
- [ ] **Decided async vs sync?** → see [async-patterns.md](async-patterns.md)
- [ ] **Planned type hint strategy?**
- [ ] **Defined project structure?**
- [ ] **Planned error handling?**
- [ ] **Considered background tasks?** → see [background-tasks.md](background-tasks.md)

> **Remember**: Python patterns are about decision-making for YOUR specific context. Don't copy code — think about what serves your application best.
