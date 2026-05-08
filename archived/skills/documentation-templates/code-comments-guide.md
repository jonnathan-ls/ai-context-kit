# Code Comments Guide (JSDoc / TSDoc)

## When to Comment vs. When to Skip

| Comment | Skip Comment |
|---------|-------------|
| Business logic that isn't obvious | What the code clearly does |
| Complex algorithms | Simple getters/setters |
| Non-obvious side effects | Framework boilerplate |
| API contracts and invariants | Self-explanatory code |

> **Rule:** If you need a comment to explain a name, rename the function instead.

## JSDoc / TSDoc Template

```typescript
/**
 * Calculates the discounted price for a subscription tier.
 * Applies regional pricing rules before the discount.
 *
 * @param basePrice - Original price in cents
 * @param discountRate - Discount as a decimal (0.2 = 20% off)
 * @param region - ISO country code for regional pricing
 * @returns Final price in cents after discount and regional adjustment
 * @throws {InvalidDiscountError} When discountRate is outside 0-1 range
 *
 * @example
 * const price = calculatePrice(1000, 0.2, 'BR'); // 800
 */
```

## Comment Tags Reference

| Tag | Purpose | When to Use |
|-----|---------|-------------|
| `@param` | Document a parameter | All non-obvious parameters |
| `@returns` | Document return value | Non-void functions |
| `@throws` | Document thrown errors | Functions that throw |
| `@example` | Usage example | Public APIs |
| `@deprecated` | Mark as deprecated | Before removal |
| `@see` | Link to related code | Complex interactions |

## Anti-Patterns

- ❌ Commenting every line ("increment i by 1")
- ❌ Restating the function name ("gets the user")
- ❌ Leaving TODO comments older than 1 sprint
- ❌ Commenting out dead code (delete it — git has history)
