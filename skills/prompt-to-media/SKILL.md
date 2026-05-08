---
version: 0.1.0
name: prompt-to-media
description: Converts product/creative intent into media-model prompts (image/video/voice) with constraints, negatives, and variant strategy.
allowed-tools: Read, Glob, Grep
tags: multimodal, prompts, media
---

# Prompt to Media

Use this skill to turn a short brief into a **production-ready media prompt** while keeping it compact and controllable.

## When to Use

- The user has a brief and needs prompts for tools/models.
- You need to generate multiple prompt variants quickly.
- You need to add negatives and format constraints.

## Prompt Checklist

- Output type (image/video/audio)
- Format constraints (aspect ratio, duration, fps)
- Subject + key actions
- Environment + lighting
- Camera / composition (if relevant)
- Style (bounded)
- Negatives / exclusions

## Variant Strategy

Generate up to 3 variants:

- V1: baseline
- V2: change composition/camera only
- V3: change style only

## Anti-Patterns

- Overly long prompts.
- Too many style adjectives.
- Changing multiple axes at once.