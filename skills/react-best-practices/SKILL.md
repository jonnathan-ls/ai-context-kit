---
name: react-best-practices
description: React patterns, hooks discipline, component design and state management best practices. Use this skill whenever the user is building React components, managing state, writing custom hooks, or designing component architecture. Triggers on component, hooks, useState, useEffect, JSX, re-render, state management.
---

# React Best Practices

## Component Design Rules

| Rule | Description |
|------|-------------|
| **Single Responsibility** | One component = one purpose. If it needs a heading with two sub-sections to describe it, split it. |
| **Composition over inheritance** | Compose small components, never extend them |
| **Props down, events up** | Data flows down via props; actions flow up via callbacks |
| **No prop drilling past 2 levels** | Use Context or state management instead |
| **Named exports for components** | Default export only for route-level pages |

## Hooks Discipline

### Rules of Hooks (Non-Negotiable)
- Only call hooks at the top level — never inside loops, conditions, or nested functions
- Only call hooks from React functions — not plain JS functions

### Custom Hooks
- Extract if the same stateful logic appears in 2+ components
- Name must start with `use`
- Must return a stable, well-typed interface
- Keep side effects inside the hook, not in the component

### Hook Anti-Patterns
- ❌ `useEffect` with missing dependency array items
- ❌ `useEffect` for derived state (use `useMemo` instead)
- ❌ State for values that can be computed from other state
- ❌ `useCallback` / `useMemo` on everything (premature optimization)

## State Management

| Location | When to Use |
|----------|-------------|
| `useState` | Local UI state (toggle, input value) |
| `useReducer` | Complex local state with multiple sub-values |
| Context | Shared state without prop drilling (theme, auth, locale) |
| Server cache (React Query/SWR) | Async server data |
| Global store (Zustand/Jotai) | Cross-cutting client state not from server |

## Performance Checklist

```
[ ] Lists have stable, unique keys (not array index)
[ ] Heavy computations wrapped in useMemo
[ ] Callbacks passed to child components wrapped in useCallback
[ ] Large lists virtualized (react-window / tanstack-virtual)
[ ] Images use lazy loading
[ ] Code-split at route level (React.lazy + Suspense)
```

## File Structure Convention

```
components/
  ComponentName/
    index.tsx          ← public API
    ComponentName.tsx  ← implementation
    ComponentName.test.tsx
    ComponentName.module.css (if needed)
```

## Forbidden Patterns

- ❌ Direct DOM manipulation (`document.querySelector`) inside components
- ❌ Mutating state directly (`state.value = x` instead of `setState`)
- ❌ `any` type on props interfaces
- ❌ Inline object/array literals in JSX that cause unnecessary re-renders
- ❌ Components longer than ~150 lines — split them

