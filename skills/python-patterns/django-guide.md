# Django Patterns (2025)

## Django Async (Django 5.0+)

```
Django supports async in:
├── Async views
├── Async middleware
├── Async ORM (limited, improving)
└── ASGI deployment

When to use async in Django:
├── External API calls
├── WebSocket (Channels)
├── High-concurrency views
└── Background task triggering
```

## Model Design

```
Fat models, thin views:
├── Put business logic in model methods and managers
├── Use managers for common queries
├── Abstract base classes for shared fields (created_at, updated_at)
├── Custom model managers for filtered querysets
```

## View Patterns

| Scenario | Use |
|----------|-----|
| Simple CRUD | Class-based views (ListView, DetailView, etc.) |
| Custom logic | Function-based views |
| REST API | ViewSets with DRF |

## Query Optimization

```
ORM performance rules:
├── select_related()   → ForeignKey / OneToOne relations
├── prefetch_related() → ManyToMany / reverse FK relations
├── .only()            → Fetch specific fields only
├── .defer()           → Exclude heavy fields
└── avoid N+1          → Always check query count in dev
```

## Settings Organization

```python
# Split by environment:
settings/
├── base.py      # Common to all environments
├── local.py     # Development overrides
├── production.py  # Production overrides
└── test.py      # Test-specific settings
```

## Anti-Patterns

- ❌ Business logic in views — use model methods or service layer
- ❌ Direct database calls in templates — use context processors or template tags
- ❌ Raw SQL without parameterization — use ORM or `cursor.execute()` with params
- ❌ Ignoring N+1 queries — use Django Debug Toolbar in development
- ❌ Synchronous ORM in async views — use `sync_to_async` wrapper
