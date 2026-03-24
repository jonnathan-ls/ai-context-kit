#!/usr/bin/env python3
import argparse
import datetime
import json
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

RUBRIC = {
    "metadata_frontmatter": 20,
    "trigger_description": 15,
    "instruction_clarity": 20,
    "actionability_reusability": 15,
    "resource_consistency": 10,
    "safety_non_surprise": 10,
    "verifiability_evals": 10,
}


def parse_frontmatter(text: str) -> Tuple[Dict[str, str], bool]:
    if not text.startswith("---\n"):
        return {}, False
    end_idx = text.find("\n---\n", 4)
    if end_idx == -1:
        return {}, False

    fm_block = text[4:end_idx].strip()
    data: Dict[str, str] = {}
    for line in fm_block.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data, True


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
    criteria: Dict[str, CriterionResult]
    critical_issues: List[str]
    recommendations: List[str]


def score_metadata(folder_name: str, frontmatter: Dict[str, str], has_frontmatter: bool) -> CriterionResult:
    max_score = RUBRIC["metadata_frontmatter"]
    score = 0
    evidence = []

    if has_frontmatter:
        score += 6
        evidence.append("Frontmatter block is present.")
    else:
        evidence.append("Missing or invalid frontmatter block.")

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

    return CriterionResult(score=min(score, max_score), max_score=max_score, status=status_for(score, max_score), evidence=evidence)


def score_trigger_description(frontmatter: Dict[str, str]) -> CriterionResult:
    max_score = RUBRIC["trigger_description"]
    score = 0
    evidence = []

    description = frontmatter.get("description", "")
    desc_low = description.lower()

    if description:
        score += 5
        evidence.append("Description is present.")
    else:
        evidence.append("Description is missing.")

    if any(token in desc_low for token in ["use when", "whenever", "when the user", "when to use"]):
        score += 5
        evidence.append("Description includes trigger context.")
    else:
        evidence.append("Description lacks explicit trigger context.")

    if len(description.split()) >= 10:
        score += 5
        evidence.append("Description has enough detail for reliable triggering.")
    elif description:
        evidence.append("Description may be too short for reliable triggering.")

    return CriterionResult(score=min(score, max_score), max_score=max_score, status=status_for(score, max_score), evidence=evidence)


def score_instruction_clarity(body: str) -> CriterionResult:
    max_score = RUBRIC["instruction_clarity"]
    score = 0
    evidence = []

    headings = len(re.findall(r"^##+\s+", body, flags=re.MULTILINE))
    numbered_steps = len(re.findall(r"^\d+\.\s+", body, flags=re.MULTILINE))

    if headings >= 3:
        score += 8
        evidence.append(f"Structured headings found ({headings}).")
    elif headings > 0:
        score += 4
        evidence.append(f"Some headings found ({headings}), but structure is shallow.")
    else:
        evidence.append("No section headings found.")

    if numbered_steps >= 3:
        score += 8
        evidence.append(f"Step-by-step sequence present ({numbered_steps} steps).")
    elif numbered_steps > 0:
        score += 4
        evidence.append("Partial step sequence found.")
    else:
        evidence.append("No explicit step-by-step instructions found.")

    contradiction_markers = ["always", "never"]
    count_markers = sum(body.lower().count(m) for m in contradiction_markers)
    if count_markers <= 20:
        score += 4
        evidence.append("Instruction tone appears controlled and mostly non-contradictory.")
    else:
        evidence.append("Potential over-constraint detected from repeated rigid directives.")

    return CriterionResult(score=min(score, max_score), max_score=max_score, status=status_for(score, max_score), evidence=evidence)


def score_actionability(body: str) -> CriterionResult:
    max_score = RUBRIC["actionability_reusability"]
    score = 0
    evidence = []

    imperative_hits = len(re.findall(r"\b(use|run|create|read|write|check|validate|generate|save)\b", body.lower()))
    has_examples = "example" in body.lower() or "```" in body

    if imperative_hits >= 15:
        score += 8
        evidence.append("Instructions are operational and action-oriented.")
    elif imperative_hits >= 6:
        score += 5
        evidence.append("Instructions have moderate actionability.")
    else:
        evidence.append("Instructions are not sufficiently operational.")

    if has_examples:
        score += 7
        evidence.append("Examples/templates are present for reuse.")
    else:
        evidence.append("No clear reusable examples/templates found.")

    return CriterionResult(score=min(score, max_score), max_score=max_score, status=status_for(score, max_score), evidence=evidence)


def score_resource_consistency(skill_dir: Path, body: str) -> CriterionResult:
    max_score = RUBRIC["resource_consistency"]
    score = 0
    evidence = []

    resource_refs = re.findall(r"(?:`)?(scripts|references|assets)/([^`\s)]+)(?:`)?", body)
    if not resource_refs:
        score = max_score
        evidence.append("No resource references detected; no broken references found.")
        return CriterionResult(score=score, max_score=max_score, status=status_for(score, max_score), evidence=evidence)

    missing = []
    for folder, rel_path in resource_refs:
        path = skill_dir / folder / rel_path
        if not path.exists():
            missing.append(str(path.relative_to(skill_dir)))

    if not missing:
        score = max_score
        evidence.append("All referenced resources exist.")
    else:
        score = max(0, max_score - min(10, len(missing) * 2))
        evidence.append(f"Missing resource references: {', '.join(missing[:8])}")

    return CriterionResult(score=score, max_score=max_score, status=status_for(score, max_score), evidence=evidence)


def score_safety(body: str) -> CriterionResult:
    max_score = RUBRIC["safety_non_surprise"]
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

    if any(token in body.lower() for token in ["approval", "guardrail", "safety", "policy", "do not"]):
        score += 3
        evidence.append("Includes some safety boundaries or constraints.")
    else:
        evidence.append("No explicit safety boundaries detected.")

    return CriterionResult(score=min(score, max_score), max_score=max_score, status=status_for(score, max_score), evidence=evidence)


def score_verifiability(body: str, skill_dir: Path) -> CriterionResult:
    max_score = RUBRIC["verifiability_evals"]
    score = 0
    evidence = []

    has_verification_terms = any(token in body.lower() for token in ["verify", "validation", "test", "assert", "expected output"])
    has_evals_dir = (skill_dir / "evals").exists()

    if has_verification_terms:
        score += 6
        evidence.append("Mentions verification/testing criteria.")
    else:
        evidence.append("No clear verification/testing guidance found.")

    if has_evals_dir:
        score += 4
        evidence.append("Skill has an `evals/` directory.")
    else:
        evidence.append("No `evals/` directory present.")

    return CriterionResult(score=min(score, max_score), max_score=max_score, status=status_for(score, max_score), evidence=evidence)


def evaluate_skill(skill_dir: Path) -> SkillResult:
    skill_md = skill_dir / "SKILL.md"
    text = skill_md.read_text(encoding="utf-8", errors="ignore")
    frontmatter, has_frontmatter = parse_frontmatter(text)

    body = text
    if has_frontmatter:
        fm_end = text.find("\n---\n", 4)
        if fm_end != -1:
            body = text[fm_end + 5 :]

    folder_name = skill_dir.name

    criteria = {
        "metadata_frontmatter": score_metadata(folder_name, frontmatter, has_frontmatter),
        "trigger_description": score_trigger_description(frontmatter),
        "instruction_clarity": score_instruction_clarity(body),
        "actionability_reusability": score_actionability(body),
        "resource_consistency": score_resource_consistency(skill_dir, body),
        "safety_non_surprise": score_safety(body),
        "verifiability_evals": score_verifiability(body, skill_dir),
    }

    total_score = sum(item.score for item in criteria.values())
    max_score = sum(item.max_score for item in criteria.values())

    critical_issues: List[str] = []
    recommendations: List[str] = []

    for name, result in criteria.items():
        if result.status == "critical":
            critical_issues.append(name)

    if criteria["metadata_frontmatter"].score < 15:
        recommendations.append("Fix frontmatter completeness and naming consistency.")
    if criteria["trigger_description"].score < 10:
        recommendations.append("Improve description with explicit when-to-use trigger context.")
    if criteria["instruction_clarity"].score < 12:
        recommendations.append("Refactor SKILL.md into clearer sections and ordered steps.")
    if criteria["resource_consistency"].score < 8:
        recommendations.append("Remove or fix broken references to scripts/references/assets.")
    if criteria["verifiability_evals"].score < 6:
        recommendations.append("Add verification guidance and objective eval criteria.")

    return SkillResult(
        skill_name=frontmatter.get("name", folder_name),
        skill_path=str(skill_dir),
        total_score=total_score,
        max_score=max_score,
        quality_band=quality_band(total_score),
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
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
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
    details {{ margin-top: 6px; }}
    ul {{ margin: 6px 0; padding-left: 18px; }}
  </style>
</head>
<body>
  <h1>Skills Quality Dashboard</h1>
  <div id=\"cards\" class=\"cards\"></div>
  <table>
    <thead>
      <tr>
        <th>Rank</th>
        <th>Skill</th>
        <th>Score</th>
        <th>Band</th>
        <th>Critical Issues</th>
        <th>Recommendations</th>
      </tr>
    </thead>
    <tbody id=\"rows\"></tbody>
  </table>

  <script>
    const report = {data};

    const rowsEl = document.getElementById('rows');
    const cardsEl = document.getElementById('cards');

    const poorCount = report.summary.by_band.poor || 0;
    const fairCount = report.summary.by_band.fair || 0;
    const goodCount = report.summary.by_band.good || 0;

    cardsEl.innerHTML = `
      <div class=\"card\"><strong>Total skills</strong><div>${{report.summary.total_skills}}</div></div>
      <div class=\"card\"><strong>Average score</strong><div>${{report.summary.average_score}}</div></div>
      <div class=\"card\"><strong>Good</strong><div>${{goodCount}}</div></div>
      <div class=\"card\"><strong>Fair</strong><div>${{fairCount}}</div></div>
      <div class=\"card\"><strong>Poor</strong><div>${{poorCount}}</div></div>
    `;

    report.skills.forEach((item, idx) => {{
      const crit = item.critical_issues.length ? item.critical_issues.join(', ') : '-';
      const rec = item.recommendations.length ? `<ul>${{item.recommendations.map(r => `<li>${{r}}</li>`).join('')}}</ul>` : '-';
      rowsEl.innerHTML += `
        <tr>
          <td>${{idx + 1}}</td>
          <td><strong>${{item.skill_name}}</strong><br/><small>${{item.skill_path}}</small></td>
          <td>${{item.total_score}} / ${{item.max_score}}</td>
          <td><span class=\"pill ${{item.quality_band}}\">${{item.quality_band}}</span></td>
          <td>${{crit}}</td>
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
    by_band = {"good": 0, "fair": 0, "poor": 0}
    for item in results:
        by_band[item.quality_band] += 1

    report = {
        "meta": {
            "skills_root": to_context_path(skills_root, context_base),
            "rubric_version": "1.0.0",
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
