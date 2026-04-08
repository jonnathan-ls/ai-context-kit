# Python Async Patterns

## When to Use Async

```
async def is better when:
├── I/O-bound operations (database, HTTP, file)
├── Many concurrent connections
├── Real-time features
├── Microservices communication
└── FastAPI/Starlette/Django ASGI

def (sync) is better when:
├── CPU-bound operations
├── Simple scripts
├── Legacy codebase
├── Team unfamiliar with async
└── Blocking libraries (no async version)
```

## The Golden Rule

```
I/O-bound → async (waiting for external)
CPU-bound → sync + multiprocessing (computing)

Don't:
├── Mix sync and async carelessly
├── Use sync libraries in async code
└── Force async for CPU work
```

## Async Library Selection

| Need | Async Library |
|------|---------------|
| HTTP client | httpx |
| PostgreSQL | asyncpg |
| Redis | aioredis / redis-py async |
| File I/O | aiofiles |
| Database ORM | SQLAlchemy 2.0 async, Tortoise |

## Common Mistakes

- ❌ Calling `requests` inside an `async def` — use `httpx` instead
- ❌ Using `time.sleep()` in async code — use `asyncio.sleep()`
- ❌ Running CPU-heavy loops in async functions — offload to `ProcessPoolExecutor`
- ❌ `await`-ing inside a `list()` comprehension without `asyncio.gather`
