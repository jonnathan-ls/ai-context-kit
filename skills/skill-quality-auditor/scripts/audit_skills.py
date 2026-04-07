#!/usr/bin/env python3
import argparse
import datetime
import json
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Fix 5: Tag-aware rubric — default weights for domain-specific skills
DEFAULT_RUBRIC = {
    "metadata_frontmatter": 20,
    "trigger_description": 15,
    "instruction_clarity": 20,
    "actionability_reusability": 15,
    "resource_consistency": 10,
    "safety_non_surprise": 10,
    "verifiability_evals": 10,
}

# Meta-skills legitimately skip evals and resource bundles;
# their primary value is in triggering precision and clear instructions.
META_RUBRIC = {
    "metadata_frontmatter": 20,
    "trigger_description": 25,  # +10: trigger accuracy is the core value of a meta-skill
    "instruction_clarity": 20,
    "actionability_reusability": 15,
    "resource_consistency": 5,  # -5: meta-skills often have no bundled resources by design
    "safety_non_surprise": 10,
    "verifiability_evals": 5,   # -5: meta-skills are harder to unit-test
}

RECOMMENDATION_TEMPLATES = {
    "metadata_frontmatter": "Fix frontmatter: ensure `name`, kebab-case, and folder alignment",
    "trigger_description": "Improve `description`: add explicit when-to-use trigger context and examples",
    "instruction_clarity": "Add structure: numbered steps, checkboxes (`- [ ]`), headings, or tables",
    "actionability_reusability": "Add reusable examples, code blocks, or output templates",
    "resource_consistency": "Fix or remove broken references to scripts/, references/, or assets/",
    "safety_non_surprise": "Add safety constraints: approval gates, guardrails, or policy notes",
    "verifiability_evals": "Add evals/ directory with test cases and verification criteria",
}


# Fix 2: Improved frontmatter parser — handles block scalars (> and |) gracefully
def parse_frontmatter(text: str) -> Tuple[Dict[str, str], bool, List[str]]:
    """Returns (data, has_frontmatter, warnings)."""
    warnings: List[str] = []
    if not text.startswith("---\n"):
        return {}, False, warnings
    end_idx = text.find("\n---\n", 4)
    if end_idx == -1:
        return {}, False, warnings

    fm_block = text[4:end_idx]
    data: Dict[str, str] = {}
    lines = fm_block.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if ":" not in line:
            i += 1
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()

        if value in (">", "|", ">-", "|-", ">+", "|+"):
            warnings.append(
                f"Field `{key}` uses a block scalar (`{value}`). "
                "Use a single-line value for broader YAML compatibility."
            )
            continuation: List[str] = []
            i += 1
            while i < len(lines) and (
                lines[i].startswith("  ") or lines[i].startswith("\t") or lines[i] == ""
            ):
                continuation.append(lines[i].strip())
                i += 1
            data[key] = " ".join(part for part in continuation if part)
        else:
            data[key] = value
            i += 1

    return data, True, warnings


def kebab_case(value: str) -> bool:
    return bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", value or ""))


def status_for(score: int, max_score: int) -> str:
    ratio = score / max_score if max_score else 0
    if ratio >= 0.8:
        return "good"
    if ratio >= 0.5:
        return "attention"
    return "critical"


def quality_band(total_score: int) -> str:
    if total_score < 60:
        return "poor"
    if total_score < 80:
        return "fair"
    return "good"


@dataclass
class CriterionResult:
    score: int
    max_score: int
    status: str
    evidence: List[str]


@dataclass
class SkillResult:
    skill_name: str
    skill_path: str
    total_score: int
    max_score: int
    quality_band: str
    skill_tag: str
    criteria: Dict[str, CriterionResult]
    critical_issues: List[str]
    recommendations: List[str]


def score_metadata(
    folder_name: str,
    frontmatter: Dict[str, str],
    has_frontmatter: bool,
    fm_warnings: List[str],
    max_score: int,
) -> CriterionResult:
    score = 0
    evidence = []

    if has_frontmatter:
        score += 6
        evidence.append("Frontmatter block is present.")
    else:
        evidence.append("Missing or invalid frontmatter block.")

    # Fix 2: surface YAML block-scalar warnings as evidence
    for w in fm_warnings:
        evidence.append(f"YAML warning: {w}")
        score = max(0, score - 2)

    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")

    if name:
        score += 4
        evidence.append("`name` field is present.")
    else:
        evidence.append("Missing required `name` field.")

    if description:
        score += 4
        evidence.append("`description` field is present.")
    else:
        evidence.append("Missing required `description` field.")

    if name and kebab_case(name):
        score += 3
        evidence.append("`name` is kebab-case.")
    elif name:
        evidence.append("`name` is not kebab-case.")

    if name and (name == folder_name or name in folder_name or folder_name in name):
        score += 3
        evidence.append("`name` appears consistent with folder intent.")
    elif name:
        evidence.append("`name` appears misaligned with folder intent.")

    return CriterionResult(
        score=min(max(score, 0), max_score),
        max_score=max_score,
        status=status_for(score, max_score),
        evidence=evidence,
    )


def score_trigger_description(frontmatter: Dict[str, str], max_score: int) -> CriterionResult:
    score = 0
    evidence = []

    description = frontmatter.get("description", "")
    desc_low = description.lower()

    if description:
        score += 5
        evidence.append("Description is present.")
    else:
        evidence.append("Description is missing.")

    if any(
        token in desc_low
        for token in ["use when", "whenever", "when the user", "when to use", "triggers on", "use this"]
    ):
        score += 5
        evidence.append("Description includes trigger context.")
    else:
        evidence.append("Description lacks explicit trigger context.")

    word_count = len(description.split())
    if word_count >= 10:
        score += min(5, max_score - score - 0)
        evidence.append(f"Description has sufficient detail ({word_count} words).")
    elif description:
        evidence.append(f"Description may be too short for reliable triggering ({word_count} words).")

    return CriterionResult(
        score=min(score, max_score),
        max_score=max_score,
        status=status_for(score, max_score),
        evidence=evidence,
    )


# Fix 1: Structure detection now recognizes checklists, tables, and code blocks
def score_instruction_clarity(body: str, max_score: int) -> CriterionResult:
    score = 0
    evidence = []

    headings = len(re.findall(r"^##+\s+", body, flags=re.MULTILINE))
    numbered_steps = len(re.findall(r"^\d+\.\s+", body, flags=re.MULTILINE))
    checkboxes = len(re.findall(r"^[-*]\s+\[[ xX]\]", body, flags=re.MULTILINE))
    table_lines = len(re.findall(r"^\|.+\|", body, flags=re.MULTILINE))

    if headings >= 3:
        score += 8
        evidence.append(f"Structured headings found ({headings}).")
    elif headings > 0:
        score += 4
        evidence.append(f"Some headings found ({headings}), but structure is shallow.")
    else:
        evidence.append("No section headings found.")

    # Step-like structures: numbered steps OR checklists OR tables each qualify
    structure_items = numbered_steps + checkboxes + (1 if table_lines >= 2 else 0)
    if structure_items >= 3:
        score += 8
        parts = []
        if numbered_steps:
            parts.append(f"{numbered_steps} numbered steps")
        if checkboxes:
            parts.append(f"{checkboxes} checkboxes")
        if table_lines >= 2:
            parts.append(f"{table_lines} table rows")
        evidence.append(f"Step-by-step or checklist structure present ({', '.join(parts)}).")
    elif structure_items > 0:
        score += 4
        evidence.append("Partial structure found (numbered steps, checkboxes, or table).")
    else:
        evidence.append("No explicit step-by-step, checklist, or table structure found.")

    contradiction_markers = ["always", "never"]
    count_markers = sum(body.lower().count(m) for m in contradiction_markers)
    if count_markers <= 20:
        score += 4
        evidence.append("Instruction tone appears controlled and non-contradictory.")
    else:
        evidence.append(
            f"Potential over-constraint: 'always'/'never' used {count_markers} times."
        )

    return CriterionResult(
        score=min(score, max_score),
        max_score=max_score,
        status=status_for(score, max_score),
        evidence=evidence,
    )


# Fix 1: Broader imperative verb list; tables and code blocks count as templates
def score_actionability(body: str, max_score: int) -> CriterionResult:
    score = 0
    evidence = []

    imperative_pattern = re.compile(
        r"\b(use|run|create|read|write|check|validate|generate|save|add|define|apply|"
        r"execute|output|perform|ensure|install|configure|return|extract|analyze|report|"
        r"identify|select|build|deploy|load|parse|scan|send|list|call|open|close)\b",
        re.IGNORECASE,
    )
    imperative_hits = len(imperative_pattern.findall(body))

    code_blocks = body.count("```") // 2
    table_lines = len(re.findall(r"^\|.+\|", body, flags=re.MULTILINE))
    has_templates = "example" in body.lower() or code_blocks > 0 or table_lines >= 2

    if imperative_hits >= 15:
        score += 8
        evidence.append(f"Instructions are operational and action-oriented ({imperative_hits} imperative hits).")
    elif imperative_hits >= 6:
        score += 5
        evidence.append(f"Instructions have moderate actionability ({imperative_hits} imperative hits).")
    else:
        evidence.append(f"Instructions are not sufficiently operational ({imperative_hits} imperative hits).")

    if has_templates:
        score += 7
        parts = []
        if code_blocks:
            parts.append(f"{code_blocks} code block(s)")
        if table_lines >= 2:
            parts.append(f"{table_lines} table rows")
        if "example" in body.lower():
            parts.append("examples section")
        evidence.append(f"Reusable templates/examples present: {', '.join(parts)}.")
    else:
        evidence.append("No clear reusable examples, code blocks, or tables found.")

    return CriterionResult(
        score=min(score, max_score),
        max_score=max_score,
        status=status_for(score, max_score),
        evidence=evidence,
    )


def score_resource_consistency(skill_dir: Path, body: str, max_score: int) -> CriterionResult:
    score = 0
    evidence = []

    resource_refs = re.findall(r"(?:`)?(scripts|references|assets|docs|evals)/([^`\s)\"']+)(?:`)?", body)
    if not resource_refs:
        score = max_score
        evidence.append("No resource references detected; no broken references found.")
        return CriterionResult(
            score=score, max_score=max_score, status=status_for(score, max_score), evidence=evidence
        )

    missing = []
    for folder, rel_path in resource_refs:
        path = skill_dir / folder / rel_path
        if not path.exists():
            missing.append(str(path.relative_to(skill_dir)))

    if not missing:
        score = max_score
        evidence.append(f"All {len(resource_refs)} referenced resource(s) exist.")
    else:
        score = max(0, max_score - min(max_score, len(missing) * 2))
        evidence.append(f"Missing resource references: {', '.join(missing[:8])}")

    return CriterionResult(
        score=score, max_score=max_score, status=status_for(score, max_score), evidence=evidence
    )


def score_safety(body: str, max_score: int) -> CriterionResult:
    score = 0
    evidence = []

    risky_terms = ["exfiltrate", "malware", "bypass", "steal", "unauthorized access"]
    risky_hits = [term for term in risky_terms if term in body.lower()]

    if risky_hits:
        evidence.append(f"Potentially unsafe terms detected: {', '.join(risky_hits)}")
        score = 0
    else:
        score += 7
        evidence.append("No obvious malicious/risky behavior guidance detected.")

    if any(
        token in body.lower()
        for token in ["approval", "guardrail", "safety", "policy", "do not", "anti-pattern", "never do", "avoid"]
    ):
        score += 3
        evidence.append("Includes safety boundaries or anti-pattern constraints.")
    else:
        evidence.append("No explicit safety boundaries or anti-pattern section detected.")

    return CriterionResult(
        score=min(score, max_score), max_score=max_score, status=status_for(score, max_score), evidence=evidence
    )


def score_verifiability(body: str, skill_dir: Path, max_score: int) -> CriterionResult:
    score = 0
    evidence = []

    has_verification_terms = any(
        token in body.lower()
        for token in ["verify", "validation", "test", "assert", "expected output", "check that", "confirm"]
    )
    evals_dir = skill_dir / "evals"
    has_evals_dir = evals_dir.exists()

    if has_verification_terms:
        score += 6
        evidence.append("Mentions verification/testing criteria.")
    else:
        evidence.append("No clear verification/testing guidance found.")

    if has_evals_dir:
        eval_files = list(evals_dir.glob("*.json")) + list(evals_dir.glob("*.md"))
        if eval_files:
            score += 4
            evidence.append(f"Has `evals/` directory with {len(eval_files)} file(s).")
        else:
            score += 1
            evidence.append("Has `evals/` directory but it appears empty.")
    else:
        evidence.append("No `evals/` directory present.")

    return CriterionResult(
        score=min(score, max_score), max_score=max_score, status=status_for(score, max_score), evidence=evidence
    )


# Fix 4: Weighted recommendations — sorted by potential score delta, top 3 only
def generate_recommendations(criteria: Dict[str, CriterionResult]) -> List[str]:
    deltas: List[Tuple[int, str]] = []
    for name, result in criteria.items():
        delta = result.max_score - result.score
        if delta > 0 and name in RECOMMENDATION_TEMPLATES:
            deltas.append((delta, f"{RECOMMENDATION_TEMPLATES[name]} (+{delta} pts)"))
    deltas.sort(reverse=True)
    return [msg for _, msg in deltas[:3]]


def evaluate_skill(skill_dir: Path) -> SkillResult:
    skill_md = skill_dir / "SKILL.md"
    text = skill_md.read_text(encoding="utf-8", errors="ignore")

    # Fix 2: parse_frontmatter now returns warnings
    frontmatter, has_frontmatter, fm_warnings = parse_frontmatter(text)

    body = text
    if has_frontmatter:
        fm_end = text.find("\n---\n", 4)
        if fm_end != -1:
            body = text[fm_end + 5:]

    folder_name = skill_dir.name

    # Fix 5: select rubric based on tag
    skill_tag = frontmatter.get("tag", "domain-specific").strip()
    rubric = META_RUBRIC if skill_tag == "meta" else DEFAULT_RUBRIC

    criteria = {
        "metadata_frontmatter": score_metadata(
            folder_name, frontmatter, has_frontmatter, fm_warnings, rubric["metadata_frontmatter"]
        ),
        "trigger_description": score_trigger_description(frontmatter, rubric["trigger_description"]),
        "instruction_clarity": score_instruction_clarity(body, rubric["instruction_clarity"]),
        "actionability_reusability": score_actionability(body, rubric["actionability_reusability"]),
        "resource_consistency": score_resource_consistency(skill_dir, body, rubric["resource_consistency"]),
        "safety_non_surprise": score_safety(body, rubric["safety_non_surprise"]),
        "verifiability_evals": score_verifiability(body, skill_dir, rubric["verifiability_evals"]),
    }

    total_score = sum(item.score for item in criteria.values())
    max_score = sum(item.max_score for item in criteria.values())

    critical_issues = [name for name, result in criteria.items() if result.status == "critical"]

    # Fix 4: recommendations ordered by score delta impact
    recommendations = generate_recommendations(criteria)

    return SkillResult(
        skill_name=frontmatter.get("name", folder_name),
        skill_path=str(skill_dir),
        total_score=total_score,
        max_score=max_score,
        quality_band=quality_band(total_score),
        skill_tag=skill_tag,
        criteria=criteria,
        critical_issues=critical_issues,
        recommendations=recommendations,
    )


def to_serializable(result: SkillResult) -> Dict:
    return {
        "skill_name": result.skill_name,
        "skill_path": result.skill_path,
        "total_score": result.total_score,
        "max_score": result.max_score,
        "quality_band": result.quality_band,
        "skill_tag": result.skill_tag,
        "criteria": {
            key: {
                "score": value.score,
                "max_score": value.max_score,
                "status": value.status,
                "evidence": value.evidence,
            }
            for key, value in result.criteria.items()
        },
        "critical_issues": result.critical_issues,
        "recommendations": result.recommendations,
    }


def to_context_path(path: Path, base: Path) -> str:
    try:
        return os.path.relpath(path.resolve(), base.resolve())
    except Exception:
        return str(path)


def build_dashboard_html(report: Dict) -> str:
    data = json.dumps(report, ensure_ascii=False)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Skills Quality Dashboard</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 0; padding: 24px; background: #f5f7fb; color: #222; }}
    h1 {{ margin-top: 0; }}
    .cards {{ display: grid; grid-template-columns: repeat(auto-fit,minmax(220px,1fr)); gap: 12px; margin-bottom: 20px; }}
    .card {{ background: white; border-radius: 10px; padding: 14px; box-shadow: 0 1px 4px rgba(0,0,0,0.08); }}
    table {{ width: 100%; border-collapse: collapse; background: white; border-radius: 10px; overflow: hidden; }}
    th, td {{ text-align: left; padding: 10px; border-bottom: 1px solid #eee; font-size: 14px; }}
    th {{ background: #111827; color: white; }}
    .pill {{ display: inline-block; padding: 2px 8px; border-radius: 999px; font-size: 12px; color: #fff; }}
    .good {{ background: #16a34a; }}
    .fair {{ background: #ca8a04; }}
    .poor {{ background: #dc2626; }}
    .tag {{ display: inline-block; padding: 1px 6px; border-radius: 4px; font-size: 11px; background: #e5e7eb; color: #374151; margin-left: 4px; }}
    details {{ margin-top: 6px; }}
    ul {{ margin: 6px 0; padding-left: 18px; }}
  </style>
</head>
<body>
  <h1>Skills Quality Dashboard</h1>
  <div id="cards" class="cards"></div>
  <table>
    <thead>
      <tr>
        <th>Rank</th>
        <th>Skill</th>
        <th>Score</th>
        <th>Band</th>
        <th>Critical Issues</th>
        <th>Top Recommendations</th>
      </tr>
    </thead>
    <tbody id="rows"></tbody>
  </table>

  <script>
    const report = {data};

    const rowsEl = document.getElementById('rows');
    const cardsEl = document.getElementById('cards');

    const poorCount = report.summary.by_band.poor || 0;
    const fairCount = report.summary.by_band.fair || 0;
    const goodCount = report.summary.by_band.good || 0;

    cardsEl.innerHTML = `
      <div class="card"><strong>Total skills</strong><div>${{report.summary.total_skills}}</div></div>
      <div class="card"><strong>Average score</strong><div>${{report.summary.average_score}}</div></div>
      <div class="card"><strong>Good</strong><div style="color:#16a34a">${{goodCount}}</div></div>
      <div class="card"><strong>Fair</strong><div style="color:#ca8a04">${{fairCount}}</div></div>
      <div class="card"><strong>Poor</strong><div style="color:#dc2626">${{poorCount}}</div></div>
    `;

    report.skills.forEach((item, idx) => {{
      const crit = item.critical_issues.length ? item.critical_issues.join(', ') : '-';
      const rec = item.recommendations.length
        ? `<ul>${{item.recommendations.map(r => `<li>${{r}}</li>`).join('')}}</ul>`
        : '-';
      const tagBadge = item.skill_tag ? `<span class="tag">${{item.skill_tag}}</span>` : '';
      rowsEl.innerHTML += `
        <tr>
          <td>${{idx + 1}}</td>
          <td><strong>${{item.skill_name}}</strong>${{tagBadge}}<br/><small style="color:#888">${{item.skill_path}}</small></td>
          <td>${{item.total_score}} / ${{item.max_score}}</td>
          <td><span class="pill ${{item.quality_band}}">${{item.quality_band}}</span></td>
          <td style="font-size:12px">${{crit}}</td>
          <td>${{rec}}</td>
        </tr>
      `;
    }});
  </script>
</body>
</html>
"""


def run(skills_root: Path, output_json: Path, output_html: Path, exclude: List[str]) -> None:
    context_base = Path.cwd()
    candidates = []
    for child in sorted(skills_root.iterdir()):
        if not child.is_dir():
            continue
        if child.name in exclude:
            continue
        if (child / "SKILL.md").exists():
            candidates.append(child)

    results = [evaluate_skill(path) for path in candidates]
    results.sort(key=lambda item: item.total_score, reverse=True)

    total = len(results)
    avg = round(sum(item.total_score for item in results) / total, 2) if total else 0
    by_band: Dict[str, int] = {"good": 0, "fair": 0, "poor": 0}
    for item in results:
        by_band[item.quality_band] += 1

    report = {
        "meta": {
            "skills_root": to_context_path(skills_root, context_base),
            "rubric_version": "2.0.0",
            "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        },
        "summary": {
            "total_skills": total,
            "average_score": avg,
            "by_band": by_band,
        },
        "skills": [
            {
                **to_serializable(item),
                "skill_path": to_context_path(Path(item.skill_path), context_base),
            }
            for item in results
        ],
    }

    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_json.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    output_html.parent.mkdir(parents=True, exist_ok=True)
    output_html.write_text(build_dashboard_html(report), encoding="utf-8")

    print(f"Analyzed {total} skills")
    print(f"JSON report: {output_json}")
    print(f"HTML dashboard: {output_html}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit and score skill quality")
    parser.add_argument("--skills-root", required=True, help="Root directory containing skill folders")
    parser.add_argument("--output-json", required=True, help="Output JSON report path")
    parser.add_argument("--output-html", required=True, help="Output HTML dashboard path")
    parser.add_argument("--exclude", action="append", default=[], help="Skill folder name to exclude")
    args = parser.parse_args()

    run(
        skills_root=Path(args.skills_root),
        output_json=Path(args.output_json),
        output_html=Path(args.output_html),
        exclude=args.exclude,
    )


if __name__ == "__main__":
    main()
