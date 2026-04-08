# Python Background Tasks

## Selection Guide

| Solution | Best For |
|----------|----------|
| **BackgroundTasks** (FastAPI) | Simple, in-process, fire-and-forget |
| **Celery** | Distributed, complex workflows, retry logic |
| **ARQ** | Async, Redis-based, simpler than Celery |
| **RQ** | Simple Redis queue, easy to reason about |
| **Dramatiq** | Actor-based, simpler API than Celery |

## Decision Tree

```
How complex is the task?
│
├── Quick, in-process, no persistence needed
│   └── FastAPI BackgroundTasks
│
├── Needs retry logic or persistence
│   ├── Async codebase → ARQ
│   └── Sync codebase → RQ or Celery
│
├── Complex workflows (chains, chords, groups)
│   └── Celery
│
└── Actor-based model preferred
    └── Dramatiq
```

## FastAPI BackgroundTasks Pattern

```python
from fastapi import BackgroundTasks

async def send_welcome_email(email: str):
    # fire and forget
    ...

@app.post("/users")
async def create_user(
    user: UserCreate,
    background_tasks: BackgroundTasks
):
    db_user = create(user)
    background_tasks.add_task(send_welcome_email, user.email)
    return db_user
```

## When NOT to Use BackgroundTasks

- Task must survive a server restart
- Task takes more than a few seconds
- Task needs retry on failure
- Multiple workers needed for throughput

## Celery Checklist

- [ ] Broker configured (Redis or RabbitMQ)
- [ ] Result backend configured if results needed
- [ ] `max_retries` set on tasks that can fail
- [ ] `task_time_limit` set to prevent zombie tasks
- [ ] Worker monitored (Flower or Prometheus)
