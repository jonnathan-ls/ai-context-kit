---
priority: P0
trigger: always_on
description: Workspace navigation guard — require workspace-map before deep repo search.
tags: workspace, harness, token
---

# Workspace Guard (P0)

> ⚠️ **Critical Rule**: Always check for the workspace map before initiating deep file searches or architectural changes.

## Protocol

1. **Detection**: At the start of any task involving file navigation, check if the file `.ai-context/workspace-map.json` exists in the project root.
   
2. **Missing Map Action**: 
   - If the file **DOES NOT** exist: You **MUST** activate the `workspace-mapper` skill immediately to generate it. Do not attempt to guess the project structure without it.
   - Inform the user: "Initiating workspace mapping to ensure processing precision."

3. **Active Map Action**:
   - If the file **EXISTS**: Read the first 100-200 lines of `.ai-context/workspace-map.json`.
   - Locate the desired file in the `summary.line_guide` object.
   - **Optimization**: Use the provided line number to perform a targeted `view_file` at that position in the JSON (read ~6 lines from there). This avoids loading the entire JSON.
   - Use the metadata (`description`, `type`) to filter which files should be included in your analysis Harness.

4. **Stale Map**:
   - If you detect that many files mentioned by the user are not in the map, or that the structure has changed drastically, execute the `workspace-mapper` skill to update the JSON.

## Goal
Avoid blind searches in the file system and ensure that the context injected into the Harness is as assertive as possible, saving tokens and preventing hallucination errors regarding file locations.
