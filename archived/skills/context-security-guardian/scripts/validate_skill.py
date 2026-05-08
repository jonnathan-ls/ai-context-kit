#!/usr/bin/env python3
"""
Skill Security Validator - Pre-Loading Gate
Validates a skill BEFORE it is processed or loaded.
Returns a blocking decision before any skill code executes.

Usage: python3 validate_skill.py <skill-name>
Output: JSON with {blocked: bool, reason: str, report: {...}}
"""

import sys
import json
import subprocess
from pathlib import Path
from typing import Dict, Any, Tuple

def validate_skill(skill_name: str, context_root: Path) -> Dict[str, Any]:
    """
    Validate a skill BEFORE loading.
    
    Args:
        skill_name: Name of skill (e.g., "always-process")
        context_root: Path to .ai-context directory
        
    Returns:
        Dict with {blocked, reason, report, severity}
    """
    skill_dir = context_root / "skills" / skill_name
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        skill_file = skill_dir / "skill.md"
    if not skill_file.exists():
        return {
            "blocked": False,
            "reason": "Skill not found (may be remote/external)",
            "severity": "info"
        }
    
    # Run scanner on JUST this skill
    scanner = context_root / "skills" / "context-security-guardian" / "scripts" / "scan_aicontext_security.py"
    
    if not scanner.exists():
        return {
            "blocked": False,
            "reason": "Security scanner not found",
            "severity": "warning"
        }
    
    reports_dir = context_root / "skills" / "context-security-guardian" / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    
    report_json = reports_dir / "skill-validation.json"
    
    try:
        cmd = [
            "python3",
            str(scanner),
            "--context-root", str(context_root),
            "--output-json", str(report_json),
            "--output-md", "/dev/null",  # Suppress markdown for speed
            "--analyze-files", str(skill_file.relative_to(context_root))
        ]
        
        result = subprocess.run(cmd, capture_output=True, timeout=10)
        
        if not report_json.exists():
            return {
                "blocked": False,
                "reason": "Validation failed to generate report",
                "severity": "warning"
            }
        
        report = json.loads(report_json.read_text())
        
        flagged = [a for a in report["artifacts"] if a["status"] == "flagged"]
        
        if not flagged:
            return {
                "blocked": False,
                "reason": "Skill validation passed",
                "severity": "none",
                "report": report
            }
        
        # Evaluate severity
        artifact = flagged[0]
        findings = artifact["findings"]
        critical = [f for f in findings if f["severity"] == "critical"]
        high = [f for f in findings if f["severity"] == "high"]
        
        # Blocking decision
        if critical:
            return {
                "blocked": True,
                "reason": f"CRITICAL vulnerability detected in skill: {skill_name}",
                "severity": "critical",
                "findings": findings,
                "report": report
            }
        
        if len(high) >= 2:
            return {
                "blocked": True,
                "reason": f"Multiple HIGH vulnerabilities detected in skill: {skill_name}",
                "severity": "high",
                "findings": findings,
                "report": report
            }
        
        # High but not blocking - just warn
        return {
            "blocked": False,
            "reason": f"HIGH vulnerability detected (educational context allowed): {skill_name}",
            "severity": "high",
            "findings": findings,
            "report": report
        }
    
    except subprocess.TimeoutExpired:
        return {
            "blocked": True,
            "reason": f"Validation timeout (possible DoS attack): {skill_name}",
            "severity": "critical"
        }
    except Exception as e:
        return {
            "blocked": True,
            "reason": f"Validation error: {str(e)}",
            "severity": "critical"
        }


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Usage: validate_skill.py <skill-name>"}))
        sys.exit(1)
    
    skill_name = sys.argv[1]
    context_root = Path.cwd() / ".ai-context"
    
    result = validate_skill(skill_name, context_root)
    print(json.dumps(result, indent=2))
    
    # Exit code signals blocking status
    sys.exit(1 if result.get("blocked", False) else 0)


if __name__ == "__main__":
    main()
