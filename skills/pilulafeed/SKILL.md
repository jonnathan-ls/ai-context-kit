---
name: pilulafeed
description: Executes the PilulaFeed automated publishing pipeline in chat-driven mode. Claude acts as the LLM layer for all agents. No external API needed. Invokes with `/pilulafeed --spec <file>`.
license: MIT
compatibility: requires Read, Write, Bash tools; executes in pilulafeed-pipeline directory
metadata:
  author: Claude Code
  version: "1.0"
  generatedBy: "1.0"
---

# PilulaFeed Chat-Driven Pipeline Runner

## Overview

You are the orchestrator for the PilulaFeed publishing pipeline. Instead of making external LLM API calls,
you execute the entire pipeline here in the chat using your reasoning capabilities. Each stage produces
JSON artifacts that feed into the next stage. You maintain a structured execution log as you go.

**Project directory:** `~/projects/to-do/pilulafeed-pipeline/`

## Input

User provides:
```
/pilulafeed --spec openspec/minha-ideia.openspec.yaml
```

Your task: Read the `.openspec` file, execute all 10 stages, and produce complete output artifacts.

## Execution Flow

### Stage 1: Spec Parsing & Hash Generation

**Action:**
1. Read the `.openspec` YAML file from the path provided
2. Validate it has required fields: `topic`, `category`, `format`, `tone`, `target_duration_sec`, `a_b_hooks`, `dry_run`
3. Generate `spec_hash` as SHA-256 of the canonicalized YAML content
4. Create output directory structure:
   - `output/<spec_hash>/`
   - `logs/<spec_hash>/`

**Output artifact:** Internal state. Log the hash.

---

### Stage 2: Curation Agent

**Input:** The `.openspec` file's `topic`, `category`, `suggested_sources`

**Your task:** Generate a realistic `CuratedEvidencePack` by reasoning about the topic.

You should:
- Invent 3–5 plausible references (URLs with titles and sources like "Hacker News", "Blog", "Research")
- Extract 5–8 key factual claims from your knowledge about the topic
- Assign confidence scores: claims with strong backing get 0.8–1.0, weaker ones get 0.5–0.7
- Mark `low_confidence: false` if you have ≥3 references, else `true`

**Output file:** `output/<spec_hash>/curated-evidence.json`

```json
{
  "spec_hash": "<hash>",
  "topic": "<from spec>",
  "category": "<from spec>",
  "references": [
    {
      "url": "https://example.com/article",
      "title": "Article Title",
      "source": "Blog | Hacker News | Research",
      "fetched_at": "2026-04-07T23:00:00Z"
    }
  ],
  "key_claims": [
    {
      "text": "Factual claim about the topic",
      "confidence": 0.85,
      "sources": ["https://example.com/article"],
      "requires_review": false
    }
  ],
  "low_confidence": false
}
```

**Write file using Write tool.**

---

### Stage 3: Script Agent

**Input:** The `CuratedEvidencePack` from Stage 2 + the `.openspec`

**Your task:** Generate a compelling script with two hook variants (A/B).

You should:
- Variant A: curiosity/question-based hook (max 15 words)
- Variant B: statement/data-based hook (max 15 words)
- Both share the same development (2–3 sentences of core content)
- Both share the same CTA (call-to-action, max 10 words)
- Convert into `ScriptFramePlan[]` — break the script into 6–10 frames (short video) or 5–12 (carousel)
  with narrative purpose and estimated duration

Respect the `target_duration_sec` from the spec. Hook frames get ~15% of total duration, CTA gets ~10%,
development frames split the rest evenly.

**Output file:** `output/<spec_hash>/script-variants.json`

```json
{
  "variants": [
    {
      "variant": "A",
      "hook": "Ever wondered how AI actually learns?",
      "development": "Machine learning isn't magic—it's pattern matching at scale. Neural networks adjust weights to minimize error. The more data, the sharper the patterns.",
      "cta": "Follow for more AI insights"
    },
    {
      "variant": "B",
      "hook": "AI algorithms process 1M decisions per second",
      "development": "Here's why that matters. Traditional programs follow explicit rules. AI systems learn rules from data instead. Speed + adaptability = the future of software.",
      "cta": "Subscribe to stay ahead"
    }
  ],
  "frame_plans": [
    {
      "variant": "A",
      "frames": [
        {
          "frame_id": "f01",
          "narrative_purpose": "Hook — grab attention with curiosity",
          "content_summary": "Ever wondered how AI actually learns?",
          "duration_ms": 3500
        },
        {
          "frame_id": "f02",
          "narrative_purpose": "Explanation — pattern matching",
          "content_summary": "Machine learning isn't magic—it's pattern matching at scale",
          "duration_ms": 4000
        }
      ]
    }
  ]
}
```

**Write file using Write tool.**

---

### Stage 4: FrameComposer Agent

**Input:** `ScriptFramePlan[]` from Stage 3 + `.openspec`

**Your task:** Convert each frame narrative into a complete `FrameSpec` with layout, animation, and design cues.

For each frame, you assign:
- `layout_template`: HeroText (text-heavy), SplitContent (left text/right visual), FullBleedVisual (full bg), ListReveal (bullet points), OutroCTA (final CTA)
- `animation.entrance`: slide-up, fade-in, zoom-punch, or typewriter
- `animation.exit`: slide-left, fade-out, or dissolve
- `typography`: headline_style (display-xl, display-lg, body-em), accent_color (primary, secondary, alert)
- `visual_hint`: descriptive string (≥5 words) for background treatment, e.g., "dark gradient with hexagonal grid overlay"
- `transition_to_next`: how to move to next frame

**Rules:**
- First frame: HeroText or FullBleedVisual
- Last frame: OutroCTA
- No 2 consecutive frames use the same entrance animation
- Total duration across all frames ≈ `target_duration_sec ± 2 seconds`

**Output file:** `output/<spec_hash>/frame-plan.json`

```json
[
  {
    "frame_id": "f01",
    "duration_ms": 3500,
    "layout_template": "HeroText",
    "content": {
      "headline": "Ever wondered how AI learns?",
      "body": "The journey from data to intelligence",
      "visual_hint": "dark gradient background with subtle circuit pattern overlay"
    },
    "animation": {
      "entrance": "slide-up",
      "exit": "slide-left",
      "in_frame_motion": []
    },
    "typography": {
      "headline_style": "display-xl",
      "accent_color": "primary"
    },
    "audio_cue": "beat-drop",
    "transition_to_next": "cross-dissolve"
  }
]
```

**Write file using Write tool.**

---

### Stage 5: Design Agent

**Input:** `FramePlan` from Stage 4

**Your task:** Translate each frame spec into a `DesignBlueprint` using design system tokens ONLY.

**Design tokens available:**
- Colors: `brand-dark` (#0D0D0D), `brand-accent` (#FF3C3C), `text-primary` (#FFFFFF), `text-muted` (#AAAAAA)
- Typography: `display-xl` (72px bold), `display-lg` (56px bold), `body-em` (28px medium), `caption` (18px regular)
- Animation presets: `SlideUpEntrance`, `ZoomPunchEntrance`, `FadeInEntrance`, `TypewriterEntrance`, `DissolveExit`, `SlideLeftExit`
- Backgrounds: `DarkGradientBG`, `AccentFloodBG`, `ParticleBurstBG`, `HexGridBG`

**Critical rule:** NO raw hex colors or pixel values. All references must be token names.

**Output file:** `output/<spec_hash>/design-blueprint.json`

```json
{
  "spec_hash": "<hash>",
  "frames": [
    {
      "frame_id": "f01",
      "background": "brand-dark",
      "background_component": "DarkGradientBG",
      "headline_style": "display-xl",
      "headline_color": "text-primary",
      "body_style": "body-em",
      "body_color": "text-primary",
      "accent_color": "brand-accent",
      "animation": {
        "entrance_preset": "SlideUpEntrance",
        "exit_preset": "SlideLeftExit"
      },
      "layout_component": "HeroText"
    }
  ]
}
```

**Write file using Write tool.**

---

### Stage 6: Dev Agent (Code Generation)

**Input:** `DesignBlueprint` from Stage 5

**Your task:** Generate TypeScript Remotion composition code that renders all frames.

**Guidelines:**
- Only import from `../../design-system/` paths
- Each frame becomes a `<Sequence>` with correct `durationInFrames` (duration_ms / 1000 * 30)
- Use the correct layout component (HeroText, SplitContent, etc.)
- Pass color tokens as props, not raw hex values
- Total `durationInFrames` must match sum of all frame durations

**Output file:** `output/<spec_hash>/composition.tsx`

**Write file using Write tool.**

---

### Stage 7: Video Rendering (Skip for now)

Since you're running in chat, skip Remotion rendering. Just log that it was skipped.

---

### Stage 8: QA Agent

**Input:** `CuratedEvidencePack` (stage 2), `design-blueprint` (stage 5)

**Your task:** Generate a `QualityReport` with factual accuracy and policy safety checks.

Evaluate:
- **Factual accuracy:** Score 0–1 (≥0.7 = pass)
- **Visual quality:** Score 0–1 (≥0.7 = pass)
- **Policy safe:** true/false

**Output file:** `output/<spec_hash>/quality-report.json`

```json
{
  "spec_hash": "<hash>",
  "factual_score": 0.85,
  "visual_score": 0.9,
  "policy_safe": true,
  "approved": true,
  "rejection_reasons": [],
  "route_to_stage": null
}
```

**Write file using Write tool.**

---

### Stage 9: Compliance Agent

**Input:** The script content

**Your task:** Generate `ComplianceReport`.

**Output file:** `output/<spec_hash>/compliance-report.json`

```json
{
  "spec_hash": "<hash>",
  "platform": "instagram",
  "policy_safe": true,
  "violations": [],
  "quarantined": false
}
```

**Write file using Write tool for each platform (instagram, tiktok, youtube).**

---

### Stage 10: Publishing Agent

**Input:** All previous artifacts + `dry_run` flag

**Your task:** Generate `PublicationJob[]` records.

If `dry_run: true`: Set status to `"dry_run"`.

**Output file:** `output/<spec_hash>/publication-jobs.json`

```json
[
  {
    "spec_hash": "<hash>",
    "platform": "instagram",
    "status": "dry_run"
  },
  {
    "spec_hash": "<hash>",
    "platform": "tiktok",
    "status": "dry_run"
  },
  {
    "spec_hash": "<hash>",
    "platform": "youtube",
    "status": "dry_run"
  }
]
```

**Write file using Write tool.**

---

## Execution Log

**After all stages, create `logs/<spec_hash>/execution.json`:**

```json
[
  {
    "agent_id": "CurationAgent",
    "status": "success",
    "duration_ms": 3421,
    "spec_hash": "<hash>",
    "attempt_number": 1,
    "artifact_path": "output/<hash>/curated-evidence.json"
  }
]
```

**Write file using Write tool.**

---

## Output Summary

Once all stages complete, print a markdown summary with all artifact paths.

---

## Guardrails

**You MUST:**
- ✅ Read the `.openspec` file completely
- ✅ Generate realistic, factual content
- ✅ Write all output files with proper JSON formatting
- ✅ Log every stage
- ✅ Keep timestamps ISO 8601 format

**You MUST NOT:**
- ❌ Call external APIs
- ❌ Skip any of the 10 stages
- ❌ Write raw hex values to DesignBlueprint output
- ❌ Publish to actual social media
