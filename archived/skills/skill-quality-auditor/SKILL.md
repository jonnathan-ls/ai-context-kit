---
name: skill-quality-auditor
description: Audit and score the quality of skills under .ai-context/skills, generate a ranked JSON report, and produce a local HTML dashboard. Use this whenever the user asks to evaluate skill quality, find weak skills, compare skills, or prioritize skill improvements.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
version: 1.0.0
---

# Skill Quality Auditor

Use this skill to evaluate the quality of existing skills and classify them as `poor`, `fair`, or `good` with a 0-100 score.

## Goal

Produce an objective, reproducible quality assessment for skills found in `.ai-context/skills`.

## Output Contract

Always generate:

1. A consolidated JSON file with ranking and per-skill diagnostics.
2. A static HTML dashboard file generated locally from the same JSON.

If the user does not provide paths, default to:

- Skills root: `./.ai-context/skills`
- JSON output: `./.ai-context/skills/skill-quality-auditor/reports/skills-quality-report.json`
- HTML output: `./.ai-context/skills/skill-quality-auditor/reports/skills-quality-dashboard.html`

## Mandatory Process

1. Discover target skills in the root folder (directories containing `SKILL.md`).
2. Evaluate each skill using the weighted rubric in this file.
3. Record per-criterion evidence, not only scores.
4. Classify quality band:
  - `poor` for score < 60
  - `fair` for score 60-79
  - `good` for score >= 80
5. Save the consolidated JSON.
6. Generate a static HTML dashboard from the same JSON.
7. Present a summary with:
   - Top 5 strongest skills
  - Skills classified as `poor`
   - Top recurring improvement actions

## Scoring Rubric (0-100)

Apply these dimensions and weights exactly:

- **Metadata & Frontmatter (20)**
  - Has valid frontmatter block
  - Includes `name` and `description`
  - `name` is kebab-case and consistent with folder intent
- **Trigger Description Quality (15)**
  - Description states what the skill does
  - Description states when to use it
  - Description is specific enough to trigger reliably
- **Instruction Clarity & Structure (20)**
  - Clear headings and logical sections
  - Step-by-step or checklist structure for execution
  - Low ambiguity and minimal contradictions
- **Actionability & Reusability (15)**
  - Instructions are operational (do X, then Y)
  - Includes reusable patterns/templates/examples when helpful
- **Resource Consistency (10)**
  - Mentions to `scripts/`, `references/`, `assets/` match actual files
  - Avoids dead references
- **Safety & Non-surprise (10)**
  - No malicious behavior guidance
  - Includes boundaries/guardrails for risky actions when applicable
- **Verifiability & Evals Readiness (10)**
  - Clear success criteria or verification guidance
  - Evals/tests mentioned when objective evaluation is expected

## Evidence Rules

For each criterion, include:

- `score`
- `max_score`
- `status`: `good`, `attention`, or `critical`
- `evidence`: array of concise findings grounded in actual file content

Never return only a raw score without evidence.

## Execution Command

Prefer running the bundled script for deterministic scoring:

```bash
python3 ./.ai-context/skills/skill-quality-auditor/scripts/audit_skills.py \
  --skills-root ./.ai-context/skills \
  --output-json ./.ai-context/skills/skill-quality-auditor/reports/skills-quality-report.json \
  --output-html ./.ai-context/skills/skill-quality-auditor/reports/skills-quality-dashboard.html \
  --exclude skill-quality-auditor
```

If custom paths are requested, adapt the command accordingly.

## Reporting Format in Conversation

After generating files, provide this concise structure:

1. `Executive summary`
2. `Poor-quality skills`
3. `Top improvement opportunities`
4. `Generated files`

Keep the conversation concise; full details stay in JSON and dashboard.

## Notes

- Prioritize deterministic checks over subjective judgment when possible.
- If a criterion is uncertain, lower confidence and record why.
- Do not modify audited skills unless explicitly asked to fix them.
