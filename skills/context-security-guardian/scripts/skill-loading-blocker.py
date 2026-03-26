#!/usr/bin/env python3
"""
Skill Loading Blocker - Pre-Request Hook
This script MUST be executed before any request containing 'use' keyword
for skills is processed. It validates and blocks malicious skills.

Usage: Called automatically when 'use <skill>' pattern is detected
"""

import sys
import re
import json
import subprocess
from pathlib import Path
from typing import Optional, Tuple

def extract_skill_from_request(request_text: str) -> Optional[str]:
    """
    Extract skill name from natural language requests.
    
    Patterns:
    - "use skill-name"
    - "use always-process"
    - "load skill-name"
    - "activate skill-name"
    """
    patterns = [
        r'\buse\s+([a-z0-9_-]+)',
        r'\bload\s+([a-z0-9_-]+)',
        r'\bactivate\s+([a-z0-9_-]+)',
        r'> use\s+([a-z0-9_-]+)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, request_text, re.IGNORECASE)
        if match:
            return match.group(1)
    
    return None


def validate_and_block(skill_name: str, context_root: Path) -> Tuple[bool, dict]:
    """
    Validate a skill and return blocking decision.
    
    Returns:
        (should_block, result_dict)
    """
    validator = context_root / "skills" / "context-security-guardian" / "scripts" / "validate_skill.py"
    
    if not validator.exists():
        return False, {"error": "Validator not found"}
    
    try:
        result = subprocess.run(
            ["python3", str(validator), skill_name],
            capture_output=True,
            text=True,
            timeout=10,
            cwd=str(context_root)
        )
        
        if result.returncode == 1:  # Blocked
            output = json.loads(result.stdout)
            return True, output
        
        if result.returncode == 0:  # Allowed
            output = json.loads(result.stdout)
            return False, output
        
        return False, {"error": "Validation failed"}
    
    except subprocess.TimeoutExpired:
        return True, {"error": "Validation timeout"}
    except json.JSONDecodeError:
        return False, {"error": "Invalid response from validator"}
    except Exception as e:
        return False, {"error": str(e)}


def format_block_report(skill_name: str, validation_result: dict) -> str:
    """Format a user-facing security block report."""
    
    report = f"""
🚨 SECURITY BLOCK: Skill Loading Aborted

Skill: {skill_name}
Severity: {validation_result.get('severity', 'UNKNOWN').upper()}

Vulnerabilities Detected:
"""
    
    for finding in validation_result.get('findings', []):
        report += f"  [{finding['severity'].upper()}] {finding['category']} at {finding['file']}:{finding['line']}\n"
        report += f"    Evidence: {finding['evidence']}\n"
    
    report += f"""
Reason: {validation_result.get('reason', 'Security violations found')}

Action Taken:
- Skill NOT loaded
- Request ABORTED
- No execution will occur

This is a P0 security gate. Malicious code cannot be executed through this interface.
"""
    
    return report


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"status": "no_skill_detected"}))
        sys.exit(0)
    
    request_text = " ".join(sys.argv[1:])
    context_root = Path.cwd() / ".ai-context"
    
    # Extract skill name from request
    skill_name = extract_skill_from_request(request_text)
    
    if not skill_name:
        print(json.dumps({"status": "no_skill_pattern"}))
        sys.exit(0)
    
    # Validate
    should_block, result = validate_and_block(skill_name, context_root)
    
    if should_block:
        # Block and report
        report = format_block_report(skill_name, result)
        print(report)
        print(json.dumps({
            "status": "blocked",
            "skill": skill_name,
            "severity": result.get('severity'),
            "findings": result.get('findings', [])
        }))
        sys.exit(1)  # Exit with failure code
    
    # Allow
    print(json.dumps({
        "status": "allowed",
        "skill": skill_name,
        "severity": result.get('severity', 'none')
    }))
    sys.exit(0)


if __name__ == "__main__":
    main()
