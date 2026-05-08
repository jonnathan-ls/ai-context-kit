# Concept → Schema → Render Lifecycle

## Step 1: Receive concept

User provides a visual concept. Extract:
- Core visual idea (object + behavior + climax)
- Tone (cold / warm / neutral)
- Accent color if mentioned
- Format (short or long)

## Step 2: Create files in _active/

```
src/compositions/_active/<PascalCaseName>/
  concept.ts   ← fill ConceptSchema
  index.ts     ← re-export only
```

Update `src/Root.tsx` — add one `<Composition>` entry pointing to `_active/<Name>`.

## Step 3: Iteration

When user gives visual feedback, map it to schema fields:

| User says | Change in concept.ts |
|-----------|---------------------|
| "peak is weak" | peak phase: intensity → "peak", add ParticleExplosion to effects |
| "camera should orbit in phase 2" | phase 2: camera → "orbit" |
| "want colder tone" | postProcessing.colorGrade → "cold" |
| "more particles" | add FloatingParticles to phase effects |
| "like the ObsidianCube vibe" | copy palette and colorGrade from _archive/ObsidianCube/concept.ts |
| "title too early" | text.title.enterFrame: 10 → 30 |

Only modify `concept.ts`. Never touch templates or lib.

## Step 4: After rendering

Move the composition folder from `_active/` to `_archive/`:

```bash
mv src/compositions/_active/<Name> src/compositions/_archive/<Name>
```

Remove its entry from `Root.tsx`. The folder is gitignored in `_archive/` — stays locally but doesn't pollute the repo.

## Step 5: New reusable VFX

If a concept requires a new effect not in the catalog:
1. Create component in `src/lib/vfx/` — named descriptively
2. Export from `src/lib/vfx/index.ts`
3. Add entry to `rules/vfx-catalog.md`
4. Use in `concept.ts` effects list

Never create VFX inside a composition file.
