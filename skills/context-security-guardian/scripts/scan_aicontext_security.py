#!/usr/bin/env python3
import argparse
import datetime
import json
import os
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

SCANNER_VERSION = "2.0.0"

HARM_CATEGORY_PATTERNS: Dict[str, str] = {
    "exfiltration": r"\b(exfiltrat|steal data|dump credentials?|upload secrets?|send data out|token theft|secret leak|get secret|extract credential)\b",
    "code-injection": r"\b(eval|code injection|exec|execute arbitrary|run arbitrary code|shell injection)\b",
    "destructive-command": r"\b(rm\s+-rf|wipe|destroy files?|mkfs\.|dd\s+if=)\b",
    "policy-bypass": r"\b(bypass (?:policy|guardrail|safety)|disable safety|ignore policy|skip checks?)\b",
    "malicious-behavior": r"\b(malicious|malware|virus|trojan|backdoor|attack|exploit|unauthorized access|privilege escalation|unauthorized-access)\b",
    "obfuscation-or-stealth": r"\b(obfuscat|hide traces|disable logging|covert|stealth|evade detection)\b",
}

ACTION_PATTERNS = [
    r"\b(run|execute|use|launch|deploy|send|extract|collect|dump|delete|disable|bypass|modify|eval|get|obtain)\b",
]

IMPERATIVE_PATTERNS = [
    r"(^|\n)\s*(\d+\.|-|\*)\s*(run|execute|use|bypass|disable|delete|steal|exfiltrat|dump|upload|eval|inject)\b",
    r"(^|\n)\s*(first|then|next|finally),?\s+(run|execute|use|bypass|disable|eval|inject)\b",
    r"\b(run|execute)\s+\w*eval\b",
]

MALICIOUS_INTENT_PATTERNS = [
    r"\b(without permission|without consent|without authorization|covertly|secretly)\b",
    r"\b(gain unauthorized|evade detection|hide evidence|steal|exfiltrat|malicious|unauthorized)\b",
    r"\b(get secret|extract credential|obtain password|get token|steal)\b",
]

DEFENSIVE_CONTEXT_PATTERNS = [
    r"\b(defensive|for defense|for detection|for audit|for hardening|mitigat|prevent|protect|secure)\b",
    r"\b(authorized testing|with permission|within scope|ethical|checklist|training|education)\b",
    r"\b(do not use maliciously|do not abuse|never use for unauthorized|apenas simulacao|apenas simu|simulation only|this is a test)\b",
]

GUARDRAIL_PATTERNS = [
    r"\b(only with permission|only in lab|authorized scope|require approval|consent required)\b",
]

CRITICAL_COMMAND_PATTERNS = [
    r"\brm\s+-rf\s+(/|\$HOME|~|\.\.|\*)",
    r"\b(curl|wget)\b[^\n]*(http|https)[^\n]*(token|secret|credential|key|passwd|password)",
    r"\b(eval|exec)\s*\(",
]

EXECUTION_SINK_PATTERN = r"\b(os\.system|subprocess\.(run|Popen|call)|eval\(|exec\()"

TEXT_EXTS = {
    ".md", ".txt", ".json", ".yaml", ".yml", ".py", ".sh", ".js", ".ts", ".toml", ".cfg", ".ini", ".xml"
}


@dataclass
class Finding:
    severity: str
    category: str
    file: str
    line: int
    match: str
    evidence: str


@dataclass
class ArtifactScan:
    artifact_id: str
    artifact_type: str
    artifact_path: str
    status: str
    risk_score: int
    findings: List[Finding]
    quarantine_action: Dict[str, object]


@dataclass
class Artifact:
    artifact_id: str
    artifact_type: str
    source_path: Path
    member_files: List[Path]


@dataclass
class TextBlock:
    start_line: int
    content: str


def rel(path: Path, base: Path) -> str:
    try:
        return os.path.relpath(path.resolve(), base.resolve())
    except Exception:
        return str(path)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""


def is_excluded(path: Path, excluded: List[Path]) -> bool:
    resolved = path.resolve()
    for ex in excluded:
        ex_res = ex.resolve()
        if resolved == ex_res:
            return True
        if ex_res in resolved.parents:
            return True
    return False


def should_scan_file(path: Path) -> bool:
    if not path.is_file():
        return False
    if path.name.startswith("."):
        return False
    if path.suffix.lower() in TEXT_EXTS:
        return True
    if path.name in {"SKILL.md", "skill.md", "CLAUDE.md", "README"}:
        return True
    return False


def count_matches(text: str, patterns: List[str]) -> int:
    total = 0
    for pattern in patterns:
        total += len(re.findall(pattern, text, flags=re.IGNORECASE | re.MULTILINE))
    return total


def split_text_blocks(text: str) -> List[TextBlock]:
    lines = text.splitlines()
    blocks: List[TextBlock] = []
    start_line = 1
    bucket: List[str] = []

    for idx, line in enumerate(lines, start=1):
        if line.strip() == "":
            if bucket:
                blocks.append(TextBlock(start_line=start_line, content="\n".join(bucket)))
                bucket = []
            start_line = idx + 1
            continue

        if not bucket:
            start_line = idx
        bucket.append(line)

    if bucket:
        blocks.append(TextBlock(start_line=start_line, content="\n".join(bucket)))

    return blocks


def is_markdown_table(content: str) -> bool:
    """
    Detect if content block is a markdown table.
    Tables are informational, not instructional.
    """
    lines = content.strip().splitlines()
    if not lines or len(lines) < 2:
        return False
    # Check for pipe characters (markdown table markers)
    table_lines = [ln for ln in lines if "|" in ln]
    if len(table_lines) < 2:
        return False
    # At least 2 consecutive lines with pipes
    for i in range(len(lines) - 1):
        if "|" in lines[i] and "|" in lines[i + 1]:
            return True
    return False


def detect_category_hits(text: str) -> List[str]:
    hits = []
    for category, pattern in HARM_CATEGORY_PATTERNS.items():
        if re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE):
            hits.append(category)
    return hits


def evaluate_text_block(block: TextBlock, rel_file: str) -> List[Finding]:
    content = block.content
    lower = content.lower()

    categories = detect_category_hits(content)
    if not categories:
        return []

    # Check if this is a markdown table (informational, not instructional)
    if is_markdown_table(content):
        return []

    action_score = count_matches(content, ACTION_PATTERNS)
    imperative_score = count_matches(content, IMPERATIVE_PATTERNS)
    malicious_intent_score = count_matches(content, MALICIOUS_INTENT_PATTERNS)
    defensive_score = count_matches(content, DEFENSIVE_CONTEXT_PATTERNS)
    guardrail_score = count_matches(content, GUARDRAIL_PATTERNS)
    critical_command_score = count_matches(content, CRITICAL_COMMAND_PATTERNS)

    # Semantic rule: ANY dangerous executable + ANY malicious indicator = suspicious
    # This catches combinations we haven't explicitly codified
    dangerous_executables = bool(re.search(
        r"\b(eval|exec|system|popen|subprocess|spawn|fork|sh|bash|curl|wget|powershell|cmd\.exe)\b",
        content,
        re.IGNORECASE
    ))
    any_malicious_marker = bool(re.search(
        r"\b(malicious|steal|unauthorized|unauthorized|bypass|exploit|backdoor|attack|harmful|dangerous|attack|exfiltrat)\b",
        content,
        re.IGNORECASE
    ))
    
    # If we have dangerous code + ANY malicious marker, it's suspicious
    semantic_threat = dangerous_executables and any_malicious_marker

    instructionality = imperative_score > 0 or action_score >= 2 or semantic_threat
    clearly_defensive = defensive_score > 0 and malicious_intent_score == 0

    if clearly_defensive and critical_command_score == 0:
        return []

    if not instructionality and critical_command_score == 0:
        return []

    findings: List[Finding] = []
    for category in categories:
        severity = None

        if critical_command_score > 0 and instructionality and guardrail_score == 0:
            severity = "critical"
        elif instructionality and malicious_intent_score > 0 and defensive_score == 0:
            severity = "high"
        elif instructionality and defensive_score == 0 and guardrail_score == 0 and category in {"exfiltration", "destructive-command"}:
            severity = "high"
        elif instructionality and defensive_score == 0:
            severity = "medium"

        if severity is None:
            continue

        snippet = content.splitlines()[0].strip()[:220]
        findings.append(
            Finding(
                severity=severity,
                category=category,
                file=rel_file,
                line=block.start_line,
                match=snippet,
                evidence=(
                    f"Context-aware detection: category={category}, actions={action_score}, imperatives={imperative_score}, "
                    f"intent={malicious_intent_score}, defensive={defensive_score}, guardrails={guardrail_score}."
                ),
            )
        )

    return findings


def evaluate_executable_lines(path: Path, text: str, context_root: Path) -> List[Finding]:
    findings: List[Finding] = []
    rel_file = rel(path, context_root)

    lines = text.splitlines()
    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#") or stripped.startswith("//"):
            continue

        if re.search(EXECUTION_SINK_PATTERN, line, flags=re.IGNORECASE):
            if re.search(r"shell\s*=\s*True", line, flags=re.IGNORECASE):
                findings.append(
                    Finding(
                        severity="high",
                        category="obfuscation-or-stealth",
                        file=rel_file,
                        line=idx,
                        match=stripped[:220],
                        evidence="Executable sink with shell=True increases command execution risk.",
                    )
                )

        for pattern in CRITICAL_COMMAND_PATTERNS:
            if re.search(pattern, line, flags=re.IGNORECASE):
                findings.append(
                    Finding(
                        severity="critical",
                        category="destructive-command" if "rm\\s+-rf" in pattern else "exfiltration",
                        file=rel_file,
                        line=idx,
                        match=stripped[:220],
                        evidence="Critical command pattern detected in executable context.",
                    )
                )

    return findings


def scan_text_for_findings(path: Path, context_root: Path) -> List[Finding]:
    text = read_text(path)
    if not text:
        return []

    rel_file = rel(path, context_root)
    findings: List[Finding] = []

    blocks = split_text_blocks(text)
    for block in blocks:
        findings.extend(evaluate_text_block(block, rel_file))

    if path.suffix.lower() in {".py", ".sh", ".js", ".ts"}:
        findings.extend(evaluate_executable_lines(path, text, context_root))

    dedup: Dict[Tuple[str, str, str, int], Finding] = {}
    for item in findings:
        key = (item.severity, item.category, item.file, item.line)
        dedup[key] = item
    return list(dedup.values())


def risk_score(findings: List[Finding]) -> int:
    total = 0
    for finding in findings:
        if finding.severity == "critical":
            total += 35
        elif finding.severity == "high":
            total += 20
        elif finding.severity == "medium":
            total += 10
        elif finding.severity == "low":
            total += 5
    return min(total, 100)


def should_quarantine(findings: List[Finding]) -> bool:
    critical = sum(1 for f in findings if f.severity == "critical")
    high = sum(1 for f in findings if f.severity == "high")
    return critical >= 1 or high >= 2


def collect_artifacts(context_root: Path, excluded: List[Path], filter_files: List[str] = None) -> List[Artifact]:
    """Collect artifacts, optionally filtering to specific files (for meta-skill mode).
    
    If filter_files provided: only include artifacts that CONTAIN any of those files.
    If filter_files empty: scan all artifacts (full scan).
    """
    artifacts: List[Artifact] = []
    filter_paths: set = set()
    if filter_files:
        for fpath in filter_files:
            resolved = (context_root / fpath).resolve()
            filter_paths.add(resolved)

    def artifact_has_filtered_files(member_files: List[Path]) -> bool:
        """Check if any member file is in the filter list."""
        if not filter_paths:
            return True  # No filter = include all
        for mfile in member_files:
            if mfile.resolve() in filter_paths:
                return True
        return False

    skills_dir = context_root / "skills"
    reserved_skill_dirs = {"context-security-guardian"}

    # 1) Skill artifacts as folder-level entities
    if skills_dir.exists():
        for skill_dir in sorted(skills_dir.iterdir()):
            if not skill_dir.is_dir():
                continue
            if skill_dir.name in reserved_skill_dirs:
                continue
            if is_excluded(skill_dir, excluded):
                continue
            has_skill_manifest = (skill_dir / "SKILL.md").exists() or (skill_dir / "skill.md").exists()
            if not has_skill_manifest:
                continue

            members = [p for p in skill_dir.rglob("*") if should_scan_file(p) and not is_excluded(p, excluded)]
            
            # Check if this skill contains any filtered files
            if not artifact_has_filtered_files(members):
                continue
                
            artifacts.append(
                Artifact(
                    artifact_id=f"skill:{skill_dir.name}",
                    artifact_type="skill",
                    source_path=skill_dir,
                    member_files=members,
                )
            )

    # 2) Rule/Agent/Workflow single-file artifacts
    typed_roots = {
        "rule": context_root / "rules",
        "agent": context_root / "agents",
        "workflow": context_root / "workflows",
    }

    seen_files: set = set()
    for artifact_type, root in typed_roots.items():
        if not root.exists():
            continue
        for file_path in sorted(root.rglob("*.md")):
            if is_excluded(file_path, excluded):
                continue
            if not should_scan_file(file_path):
                continue
            if not artifact_has_filtered_files([file_path]):
                continue
            seen_files.add(file_path.resolve())
            artifacts.append(
                Artifact(
                    artifact_id=f"{artifact_type}:{file_path.stem}",
                    artifact_type=artifact_type,
                    source_path=file_path,
                    member_files=[file_path],
                )
            )

    # 3) Other files from any current/future folder
    skip_roots = {
        (context_root / "skills").resolve(),
        (context_root / "rules").resolve(),
        (context_root / "agents").resolve(),
        (context_root / "workflows").resolve(),
        (context_root / "quarantine").resolve(),
    }

    for file_path in sorted(context_root.rglob("*")):
        if not should_scan_file(file_path):
            continue
        if is_excluded(file_path, excluded):
            continue
        if not artifact_has_filtered_files([file_path]):
            continue
        if file_path.resolve() in seen_files:
            continue
        if any(parent == skip for parent in [file_path.resolve()] + list(file_path.resolve().parents) for skip in skip_roots):
            continue
        artifacts.append(
            Artifact(
                artifact_id=f"other:{rel(file_path, context_root)}",
                artifact_type="other",
                source_path=file_path,
                member_files=[file_path],
            )
        )

    return artifacts


def scan_artifact(artifact: Artifact, context_root: Path) -> ArtifactScan:
    findings: List[Finding] = []
    for file_path in artifact.member_files:
        findings.extend(scan_text_for_findings(file_path, context_root))

    return ArtifactScan(
        artifact_id=artifact.artifact_id,
        artifact_type=artifact.artifact_type,
        artifact_path=rel(artifact.source_path, context_root),
        status="clean" if not findings else "flagged",
        risk_score=risk_score(findings),
        findings=findings,
        quarantine_action={"executed": False, "target": None},
    )


def ensure_json(path: Path, default_data: Dict) -> Dict:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(json.dumps(default_data, indent=2), encoding="utf-8")
        return default_data
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default_data


def unique_target(path: Path) -> Path:
    if not path.exists():
        return path
    suffix = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%d%H%M%S")
    return path.with_name(f"{path.name}-{suffix}")


def quarantine_artifact(
    scan: ArtifactScan,
    context_root: Path,
    quarantine_root: Path,
    blocked_registry: Path,
) -> Optional[Dict[str, object]]:
    src = (context_root / scan.artifact_path).resolve()
    if not src.exists():
        return None

    # Never self-quarantine the guardian skill itself
    if scan.artifact_id == "skill:context-security-guardian":
        return None

    rel_src = rel(src, context_root)
    target = unique_target((quarantine_root / rel_src).resolve())
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(src), str(target))

    scan.status = "quarantined"
    scan.quarantine_action = {"executed": True, "target": rel(target, context_root)}

    registry = ensure_json(blocked_registry, {"blocked_artifacts": []})
    entries = registry.get("blocked_artifacts", [])
    entries.append(
        {
            "artifact_id": scan.artifact_id,
            "artifact_type": scan.artifact_type,
            "artifact_path": scan.artifact_path,
            "blocked_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "reason": "Security findings exceeded quarantine threshold.",
            "risk_score": scan.risk_score,
            "finding_count": len(scan.findings),
            "quarantine_path": scan.quarantine_action["target"],
        }
    )
    registry["blocked_artifacts"] = entries
    blocked_registry.write_text(json.dumps(registry, indent=2, ensure_ascii=False), encoding="utf-8")

    return scan.quarantine_action


def severity_counts(scans: List[ArtifactScan]) -> Dict[str, int]:
    counts = {"critical": 0, "high": 0, "medium": 0, "low": 0}
    for scan in scans:
        for finding in scan.findings:
            counts[finding.severity] = counts.get(finding.severity, 0) + 1
    return counts


def type_counts(scans: List[ArtifactScan]) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for scan in scans:
        counts[scan.artifact_type] = counts.get(scan.artifact_type, 0) + 1
    return counts


def build_report(scans: List[ArtifactScan], context_root: Path) -> Dict:
    flagged = [s for s in scans if s.findings]
    return {
        "meta": {
            "context_root": rel(context_root, Path.cwd()),
            "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "scanner_version": SCANNER_VERSION,
        },
        "summary": {
            "artifacts_scanned": len(scans),
            "artifacts_flagged": len(flagged),
            "total_findings": sum(len(s.findings) for s in scans),
            "by_severity": severity_counts(scans),
            "by_artifact_type": type_counts(scans),
        },
        "artifacts": [
            {
                "artifact_id": s.artifact_id,
                "artifact_type": s.artifact_type,
                "artifact_path": s.artifact_path,
                "status": s.status,
                "risk_score": s.risk_score,
                "findings": [
                    {
                        "severity": f.severity,
                        "category": f.category,
                        "file": f.file,
                        "line": f.line,
                        "match": f.match,
                        "evidence": f.evidence,
                    }
                    for f in s.findings
                ],
                "quarantine_action": s.quarantine_action,
            }
            for s in sorted(scans, key=lambda x: x.risk_score, reverse=True)
        ],
    }


def build_markdown(report: Dict) -> str:
    lines = [
        "# AI Context Security Report",
        "",
        f"- Generated at: {report['meta']['generated_at']}",
        f"- Context root: {report['meta']['context_root']}",
        f"- Artifacts scanned: {report['summary']['artifacts_scanned']}",
        f"- Artifacts flagged: {report['summary']['artifacts_flagged']}",
        f"- Total findings: {report['summary']['total_findings']}",
        "",
        "## Severity Breakdown",
        "",
    ]

    for sev, count in report["summary"]["by_severity"].items():
        lines.append(f"- {sev}: {count}")

    lines.extend(["", "## Artifact Type Coverage", ""])
    for kind, count in report["summary"]["by_artifact_type"].items():
        lines.append(f"- {kind}: {count}")

    lines.extend(["", "## Artifacts", ""])

    for item in report["artifacts"]:
        lines.append(f"### {item['artifact_id']} ({item['status']})")
        lines.append(f"- Type: {item['artifact_type']}")
        lines.append(f"- Path: {item['artifact_path']}")
        lines.append(f"- Risk score: {item['risk_score']}")
        if item["quarantine_action"]["executed"]:
            lines.append(f"- Quarantined to: {item['quarantine_action']['target']}")

        if not item["findings"]:
            lines.append("- Findings: none")
            lines.append("")
            continue

        lines.append("- Findings:")
        for finding in item["findings"]:
            lines.append(
                f"  - [{finding['severity']}] {finding['category']} at {finding['file']}:{finding['line']}"
            )
            lines.append(f"    - Evidence: {finding['evidence']}")
        lines.append("")

    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Scan all AI context files for malicious or risky instructions")
    parser.add_argument("--context-root", required=True)
    parser.add_argument("--output-json", required=True)
    parser.add_argument("--output-md", required=True)
    parser.add_argument("--exclude-path", action="append", default=[])
    parser.add_argument("--enforce-quarantine", action="store_true")
    parser.add_argument("--analyze-files", action="append", default=[], help="Limit analysis to specific files (relative paths)")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    context_root = Path(args.context_root)
    output_json = Path(args.output_json)
    output_md = Path(args.output_md)

    excluded = [Path(p) for p in args.exclude_path]
    excluded.extend([
        context_root / "quarantine",
        context_root / "security",
        context_root / "skills" / "context-security-guardian" / "reports",
    ])

    artifacts = collect_artifacts(context_root=context_root, excluded=excluded, filter_files=args.analyze_files)
    scans = [scan_artifact(artifact, context_root) for artifact in artifacts]

    if args.enforce_quarantine:
        quarantine_root = context_root / "quarantine"
        blocked_registry = context_root / "security" / "blocked-artifacts.json"
        for scan in scans:
            if should_quarantine(scan.findings):
                quarantine_artifact(
                    scan=scan,
                    context_root=context_root,
                    quarantine_root=quarantine_root,
                    blocked_registry=blocked_registry,
                )

    report = build_report(scans, context_root)

    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_json.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    output_md.parent.mkdir(parents=True, exist_ok=True)
    output_md.write_text(build_markdown(report), encoding="utf-8")

    print(f"Artifacts scanned: {report['summary']['artifacts_scanned']}")
    print(f"Artifacts flagged: {report['summary']['artifacts_flagged']}")
    print(f"JSON report: {output_json}")
    print(f"Markdown report: {output_md}")


if __name__ == "__main__":
    main()
