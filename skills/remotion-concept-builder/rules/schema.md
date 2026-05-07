# How to Fill ConceptSchema

Type reference: `src/templates/ConceptSchema.ts`

## Required Fields

| Field | Type | Example |
|-------|------|---------|
| id | kebab-case string | "obsidian-cube" |
| title | PT-BR string | "Cubo de Obsidiana" |
| seriesType | "Concept" \| "Experiment" \| "Breakdown" | "Concept" |
| seriesNumber | 3-digit string | "001" |
| format | "short" \| "long" | "short" |
| durationInFrames | number | 300 (= 10s @ 30fps) |

## Format Reference

| format | dimensions | duration guide |
|--------|-----------|----------------|
| short | 1080×1920 (9:16) | 240–600 frames (8–20s) |
| long | 1920×1080 (16:9) | 9000–14400 frames (5–8min) |

## Phases

Every concept needs 3–5 phases. Ranges must be contiguous and cover 0 to durationInFrames.

Short format typical structure:
```ts
phases: [
  { name: "build",  range: [0, 90],   intensity: "low",    camera: "static" },
  { name: "rise",   range: [90, 180], intensity: "medium", camera: "zoomIn" },
  { name: "peak",   range: [180, 270],intensity: "peak",   camera: "orbit"  },
]
```

Rules:
- Always end with `intensity: "peak"` for the climax phase
- `camera: "static"` means no camera movement applied
- `effects[]` uses component names from vfx-catalog.md exactly

## Palette

Override only what differs from brand. Primary should stay #FF6B00.

```ts
palette: {
  accent: "#c8a0ff",  // concept-specific accent only
}
```

## End Card

Always include for short format:
```ts
endCard: {
  label: "Concept #001 — Cubo de Obsidiana",
  cta: "processo completo ↑",
}
```
