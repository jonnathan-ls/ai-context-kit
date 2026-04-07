---
name: testing-patterns
description: Testing strategy and implementation specialist. Use this skill whenever the user needs to write tests, design a test suite, choose between unit/integration/E2E testing, fix flaky tests, set up mocking, or improve test coverage. Triggers on "write tests", "unit test", "integration test", "E2E test", "mocking", "test coverage", "flaky test", "test setup", "jest", "vitest", "pytest", "testing pyramid", "test data", "test organization". Covers all test levels with AAA pattern, mock strategies, and anti-pattern detection.
---

# Testing Patterns

Principles and patterns for reliable, maintainable test suites. Covers all levels of the testing pyramid with concrete decisions for when to use each approach.

## When to Use

- User needs to write unit, integration, or E2E tests
- User is deciding which test type to use for a specific scenario
- User has flaky tests and needs a diagnosis
- User needs to set up mocking or test data strategies
- User wants to improve coverage without writing low-value tests

## Testing Pyramid

```
         /\
        /  \       E2E (Few) — Critical user flows only
       /----\
      /      \     Integration (Some) — API endpoints, DB queries, service boundaries
     /--------\
    /          \   Unit (Many) — Pure functions, business logic, edge cases
   /____________\
```

Maintain this ratio. Inverting it produces slow, brittle suites that developers stop trusting.

## Test Type Selection

| Type | Best For | Speed | Cost of Maintenance |
|------|----------|-------|---------------------|
| **Unit** | Pure functions, business logic, edge cases | < 50ms each | Low |
| **Integration** | API endpoints, database queries, service contracts | Medium | Medium |
| **E2E** | Critical user journeys (login, checkout, signup) | Slow | High |

## AAA Pattern (Mandatory Structure)

Every test follows Arrange → Act → Assert:

```typescript
it('should return discounted price when coupon is valid', () => {
  // Arrange
  const cart = buildCart({ total: 100 });
  const coupon = buildCoupon({ discountRate: 0.2 });

  // Act
  const result = applyDiscount(cart, coupon);

  // Assert
  expect(result.total).toBe(80);
});
```

## Unit Test Principles

### What to Test

| Test | Skip |
|------|------|
| Business logic and edge cases | Framework internals |
| Error and boundary conditions | Simple getters/setters |
| Pure function outputs | Third-party library behavior |

### Good Unit Test Properties

- [ ] Runs in under 100ms
- [ ] No external dependencies (network, DB, filesystem)
- [ ] Same result every run (deterministic)
- [ ] Fails for exactly one reason
- [ ] Name describes the scenario, not the implementation

## Integration Test Principles

### What to Test

| Area | Focus |
|------|-------|
| API endpoints | Request/response contracts, status codes |
| Database operations | Queries, transactions, constraints |
| External service calls | Contract validation, error handling |

### Setup and Teardown

```typescript
beforeAll(async () => {
  await db.connect();
});

beforeEach(async () => {
  await db.seed(testFixtures);
});

afterEach(async () => {
  await db.truncate();
});

afterAll(async () => {
  await db.disconnect();
});
```

## Mocking Strategy

### When to Mock

| Mock | Keep Real |
|------|-----------|
| External APIs and HTTP calls | The code under test |
| Filesystem (unit tests) | In-memory data stores |
| Time (`Date.now()`, timers) | Pure functions |
| Third-party services | Core business logic |

### Mock Types

| Type | Use | Example |
|------|-----|---------|
| **Stub** | Return controlled values | `mockFn.mockReturnValue(42)` |
| **Spy** | Track calls without changing behavior | `jest.spyOn(service, 'send')` |
| **Mock** | Set expectations and verify calls | Full mock object |
| **Fake** | Lightweight real implementation | In-memory repository |

## Test Data Strategies

| Approach | Use When | Example |
|----------|----------|---------|
| **Factory** | Need varied test objects | `buildUser({ role: 'admin' })` |
| **Fixture** | Need stable, shared datasets | JSON files for DB seeds |
| **Builder** | Complex objects with many options | Fluent `UserBuilder().withRole('admin').build()` |

Principles:
- Use realistic data (not "foo", "bar", "test")
- Randomize non-essential fields with a library like `faker`
- Keep test data minimal — only what the test actually needs

## Test Organization

### Naming Conventions

| Pattern | Example |
|---------|---------|
| `should [behavior] when [condition]` | `should return 404 when user not found` |
| `given [context], when [action], then [outcome]` | `given invalid token, when accessing /api, then returns 401` |

### File Structure

```
src/
├── auth/
│   ├── auth.service.ts
│   └── auth.service.test.ts   ← co-located unit tests
tests/
├── integration/
│   └── auth.api.test.ts       ← integration tests
└── e2e/
    └── login.spec.ts          ← E2E tests
```

## Anti-Patterns

- **Do not** test implementation details — test observable behavior.
- **Do not** write tests that depend on execution order — each test must be independent.
- **Do not** ignore flaky tests — fix the root cause (race condition, shared state, timing).
- **Do not** skip cleanup — leaked state between tests causes false failures.
- **Do not** mock the code under test itself — mocking defeats the purpose.
- **Do not** aim for 100% coverage at the expense of test quality — meaningful tests over line counts.
- **Do not** duplicate test logic — extract shared setup into `beforeEach` or factory functions.

## Verification Criteria

A well-tested codebase satisfies:
- [ ] Unit tests cover all business logic edge cases
- [ ] Integration tests verify API contracts and DB operations
- [ ] E2E tests cover at least the 3 most critical user flows
- [ ] No flaky tests in CI
- [ ] Test names describe behavior, not implementation
