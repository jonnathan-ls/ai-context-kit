---
name: good-example
description: Data analysis and report generation specialist. Use this skill whenever the user asks to analyze data, generate reports, summarize datasets, or visualize metrics. Triggers on "analyze this data", "generate a report", "summarize results", "create a dashboard".
allowed-tools: Read, Write, Bash
version: 1.0.0
tag: domain-specific
---

# Good Example Skill

An expert data analysis assistant that transforms raw datasets into structured, actionable reports.

## When to Use

- User has a dataset and wants insights or summaries
- User needs a formatted report from raw data
- User wants to identify trends, outliers, or anomalies

## Execution Flow

```
Step 1 → INGEST    : Read and validate the input data
Step 2 → ANALYZE   : Apply statistical summaries and trend detection
Step 3 → REPORT    : Generate structured Markdown output with findings
Step 4 → VERIFY    : Confirm output matches user expectations
```

## Step 1 — Ingest

1. Read the data source provided by the user.
2. Validate the format (CSV, JSON, plain text).
3. Report any missing fields or parsing errors before proceeding.

## Step 2 — Analyze

Apply the following checks:
- [ ] Compute descriptive statistics (mean, median, range)
- [ ] Identify top-N values by key metric
- [ ] Detect outliers beyond 2 standard deviations
- [ ] Check for missing or null values

## Step 3 — Report

Generate a Markdown report with:

| Section | Content |
|---------|---------|
| Summary | Dataset dimensions, completeness |
| Key Metrics | Top values, averages, totals |
| Anomalies | Outliers and missing data |
| Recommendations | Suggested next steps |

Example output structure:

```markdown
## Data Report — {dataset_name}
- Rows: 1,240 | Columns: 8 | Missing: 3%
- Top value: Region A (42%)
- Anomaly: 12 rows with null `revenue` field
```

## Step 4 — Verify

Confirm with the user:
- Does the report cover the requested metrics?
- Are the anomalies actionable?

## Anti-Patterns

- Do not fabricate data points when values are missing — flag them explicitly.
- Do not skip the validation step even if the user says data is "clean".
- Never present statistical claims without noting sample size.

## Verification Criteria

- Output includes all 4 report sections
- Anomaly detection runs on every numeric column
- Expected output matches format shown in Step 3 example
