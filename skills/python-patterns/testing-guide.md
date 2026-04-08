# Python Testing Patterns

## Testing Strategy

| Type | Purpose | Tools |
|------|---------|-------|
| **Unit** | Business logic in isolation | pytest |
| **Integration** | API endpoints + real DB | pytest + httpx/TestClient |
| **E2E** | Full workflows | pytest + DB + external services |

## Async Testing

```python
# Use pytest-asyncio for async tests

import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/users")
        assert response.status_code == 200
```

### pytest.ini / pyproject.toml

```toml
[tool.pytest.ini_options]
asyncio_mode = "auto"  # auto-detect async tests
```

## Fixtures Strategy

```python
# Common fixtures:

@pytest.fixture
def db_session():
    # Provide test database session
    session = TestSessionLocal()
    try:
        yield session
    finally:
        session.rollback()
        session.close()

@pytest.fixture
def client(db_session):
    # Override real DB with test DB
    app.dependency_overrides[get_db] = lambda: db_session
    with TestClient(app) as c:
        yield c

@pytest.fixture
def authenticated_user(client, db_session):
    # Create user + return auth token
    ...
```

## Test Organization

```
tests/
├── unit/
│   ├── test_services.py    # Business logic
│   └── test_models.py      # Model methods
├── integration/
│   ├── test_users_api.py   # Endpoint tests
│   └── test_payments_api.py
└── conftest.py             # Shared fixtures
```

## Anti-Patterns

- ❌ Testing implementation details — test behavior and outcomes
- ❌ Mocking the database in integration tests — use a real test DB
- ❌ Fixtures that are too large — one fixture, one responsibility
- ❌ Skipping `asyncio_mode = auto` — leads to sync test running async code
- ❌ No `rollback()` in DB fixtures — tests pollute each other
