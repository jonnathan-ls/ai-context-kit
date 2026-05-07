# Channel Brand Reference

## Colors

| Token | Hex | Use |
|-------|-----|-----|
| background | #0A0A0A | All composition backgrounds |
| primary | #FF6B00 | Orange — channel signature, titles, accents |
| text | #F5F5F5 | Body text, subtitles |
| surface | #2A2A2A | Secondary surfaces |

Source of truth: `src/lib/brand.ts` → `Brand.colors`

## Fonts

| Token | Font | Use |
|-------|------|-----|
| display | Bebas Neue | Titles, HUD labels, series numbers |
| body | Inter | Subtitles, descriptions |
| mono | JetBrains Mono | Technical HUD, BPM counters, data labels |

Source of truth: `src/lib/brand.ts` → `Brand.fonts`

## Post-Processing Defaults

| Property | Default | Options |
|----------|---------|---------|
| colorGrade | "cinematic" | cinematic, noir, warm, cold, vintage, vibrant, horror, dream, none |
| filmGrain | 0.1 | 0–1 |
| vignette | 0.5 | 0–1 |

Source of truth: `src/lib/brand.ts` → `SceneDefaults.postProcessing`

## Identity Rules

- Orange (#FF6B00) is mandatory in every composition — as glow, accent, title, or core element
- Background is always deep black (#0A0A0A) — never white, never light
- Accent color per piece can differ (e.g. purple for silk concept) but primary stays #FF6B00
- Style: dark, cinematic, premium — never colorful, never childish
