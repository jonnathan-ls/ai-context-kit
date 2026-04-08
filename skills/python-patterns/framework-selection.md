# Python Framework Selection

## Decision Tree

```
What are you building?
│
├── API-first / Microservices
│   └── FastAPI (async, modern, fast)
│
├── Full-stack web / CMS / Admin
│   └── Django (batteries-included)
│
├── Simple / Script / Learning
│   └── Flask (minimal, flexible)
│
├── AI/ML API serving
│   └── FastAPI (Pydantic, async, uvicorn)
│
└── Background workers
    └── Celery + any framework
```

## Comparison

| Factor | FastAPI | Django | Flask |
|--------|---------|--------|-------|
| **Best for** | APIs, microservices | Full-stack, CMS | Simple, learning |
| **Async** | Native | Django 5.0+ | Via extensions |
| **Admin** | Manual | Built-in | Via extensions |
| **ORM** | Choose your own | Django ORM | Choose your own |
| **Learning curve** | Low | Medium | Low |

## Questions to Ask Before Choosing

1. Is this API-only or full-stack?
2. Does it need an admin interface?
3. Is the team familiar with async?
4. Does existing infrastructure impose constraints?

## Anti-Patterns

- ❌ Default to Django for simple APIs (FastAPI may be better)
- ❌ Default to FastAPI for full-stack with admin needs (Django includes this)
- ❌ Choose Flask for production APIs requiring validation (use FastAPI + Pydantic)
