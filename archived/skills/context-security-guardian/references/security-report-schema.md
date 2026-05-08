# AI Context Security Report Schema

## JSON Root

```json
{
  "meta": {
    "context_root": "string",
    "generated_at": "ISO-8601",
    "scanner_version": "1.0.0"
  },
  "summary": {
    "artifacts_scanned": 0,
    "artifacts_flagged": 0,
    "total_findings": 0,
    "by_severity": {
      "critical": 0,
      "high": 0,
      "medium": 0,
      "low": 0
    }
  },
  "artifacts": []
}
```

## Artifact Item

```json
{
  "artifact_id": "string",
  "artifact_type": "skill|agent|rule|workflow|other",
  "artifact_path": "string",
  "status": "clean|flagged|quarantined",
  "risk_score": 0,
  "findings": [
    {
      "severity": "critical|high|medium|low",
      "category": "exfiltration|destructive-command|policy-bypass|unauthorized-access|obfuscation-or-stealth",
      "file": "relative/path",
      "line": 0,
      "match": "text",
      "evidence": "short explanation"
    }
  ],
  "quarantine_action": {
    "executed": false,
    "target": "string|null"
  }
}
```

## Quarantine Rule

An artifact is quarantined when:
- it has at least one `critical` finding, OR
- it has at least two `high` findings.
