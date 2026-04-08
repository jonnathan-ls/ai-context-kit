# FastAPI Patterns

## async def vs def in Route Handlers

```
Use async def when:
├── Using async database drivers
├── Making async HTTP calls
├── I/O-bound operations
└── Want to handle concurrency

Use def when:
├── Blocking operations
├── Sync database drivers
├── CPU-bound work
└── FastAPI runs in threadpool automatically
```

## Dependency Injection

```
Use dependencies for:
├── Database sessions
├── Current user / Auth
├── Configuration
├── Shared resources

Benefits:
├── Testability (mock dependencies)
├── Clean separation
├── Automatic cleanup (yield)
```

### Dependency Pattern

```python
from fastapi import Depends

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users")
async def list_users(db: Session = Depends(get_db)):
    ...
```

## Pydantic v2 Integration

FastAPI + Pydantic are tightly integrated. Return type becomes response schema.

```python
@app.post("/users")
async def create(user: UserCreate) -> UserResponse:
    # user is already validated on entry
    # return type is serialized automatically
    ...
```

## Project Structure

```
Organize by layer (recommended for most projects):
├── routes/        # HTTP handlers — thin, delegate to service
├── services/      # Business logic — framework-agnostic
├── models/        # Database models (SQLAlchemy, etc.)
├── schemas/       # Pydantic models for request/response
└── dependencies/  # Shared deps (db session, auth)

Organize by feature (recommended for large projects):
├── users/
│   ├── routes.py
│   ├── service.py
│   └── schemas.py
└── products/
    └── ...
```

## Anti-Patterns

- ❌ Business logic in route handlers — put it in services
- ❌ `any` type on Pydantic models — define explicit schemas
- ❌ Synchronous ORM calls inside `async def` handlers without offloading
- ❌ Skipping response model — always declare return type for automatic validation
