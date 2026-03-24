# Source Repository Structure

## Standard Format

Users prepare topic analysis by creating a directory structure:

```
/workspace/[topic-name]/
├── sources/
│   ├── index.md                  ← ESSENTIAL: Source registry
│   ├── [category-1]/
│   │   ├── source-file-1.md
│   │   ├── source-file-2.md
│   │   └── source-file-3.md
│   ├── [category-2]/
│   │   └── source-files...
│   └── [category-N]/
│       └── source-files...
├── analysis-requests/
│   └── Request notes & conversation history
└── deliverables/
    └── [timestamp]-analysis-report.pdf
```

---

## Essential: sources/index.md

This file **must exist** and document all available sources:

```markdown
# Source Repository Index - [Topic Name]

## Purpose
[Description of what this repository covers]

## Sources by Category

### Regulatory Documents
- `building-codes.md` - Official building standards (TIER 1)
- `permits-requirements.md` - Permit application process (TIER 1)
- `compliance-checklist.md` - Legal compliance requirements (TIER 1)

### Technical Documentation  
- `technical-specs.md` - Material/structural specifications (TIER 1)
- `standards-adopted.md` - Industry standards applied (TIER 2)

### Financial Data
- `cost-benchmarks-2024.md` - Current market cost data (TIER 2)
- `labor-rates.md` - Prevailing labor costs (TIER 2)
- `historical-pricing.md` - 5-year price trends (TIER 3)

### Vendor/Contractor Data
- `contractor-ratings.md` - Third-party contractor reviews (TIER 2)
- `insurance-requirements.md` - Contractor insurance standards (TIER 1)

### Market Intelligence
- `market-analysis-2024.md` - Industry market position (TIER 3)
- `competitive-landscape.md` - Competitor analysis (TIER 3)

### References & Research
- `case-studies.md` - Similar projects (case studies) (TIER 3)
- `expert-commentary.md` - Industry expert opinions (TIER 3)

## Source Credibility Assessment

| Source | Tier | Notes |
|--------|------|-------|
| building-codes.md | TIER 1 | Official government document |
| cost-benchmarks-2024.md | TIER 2 | Industry benchmark, published 2024 |
| contractor-ratings.md | TIER 2 | Aggregated data from verified reviews |
| market-analysis-2024.md | TIER 3 | Industry analyst commentary, annual |

## Known Gaps & Limitations

- No vendor-specific insurance data (must obtain)
- Market data is 12 months old (may be outdated)
- Regional variation not captured (São Paulo-specific needed)
- Labor rate estimates, not actual contracts

## Last Updated
[Date] by [Who]

## Version
1.0
```

---

## Category Examples

### For "House Construction" Project

```
/workspace/casa-construcao/sources/

├── regulatory/
│   ├── building-code-sp-2024.md
│   ├── environmental-compliance.md
│   ├── permit-process.md
│   └── zoning-restrictions.md

├── technical/
│   ├── foundation-standards.md
│   ├── structural-engineering.md
│   ├── material-specs.md
│   └── finishing-standards.md

├── financial/
│   ├── cost-benchmarks-march-2026.md
│   ├── labor-rates-construction.md
│   ├── material-costs.md
│   └── financing-options.md

├── contractor-data/
│   ├── contractor-directory.md
│   ├── ratings-complaints.md
│   ├── insurance-requirements.md
│   └── verified-references.md

├── market-analysis/
│   ├── housing-market-trends.md
│   ├── regional-construction-activity.md
│   └── timing-considerations.md

└── index.md
```

### For "Hire Contractor Decision"

```
/workspace/contractor-selection/sources/

├── regulatory/
│   ├── contractor-licensing.md
│   ├── legal-requirements.md
│   └── compliance-checklist.md

├── financial/
│   ├── contractor-pricing-benchmarks.md
│   ├── cost-estimation-methodology.md
│   └── payment-terms-standards.md

├── quality-standards/
│   ├── workmanship-standards.md
│   ├── quality-assurance-protocols.md
│   └── inspection-procedures.md

├── risk-management/
│   ├── contractor-liability-insurance.md
│   ├── bonding-requirements.md
│   └── dispute-resolution.md

├── case-studies/
│   ├── successful-projects.md
│   ├── problem-projects-lessons.md
│   └── industry-benchmarks.md

└── index.md
```

---

## Source File Format

Each source file should follow:

```markdown
# [Source Title]

## Source Information
- **Type**: [Regulatory / Technical / Financial / Case Study / Expert Opinion]
- **Credibility Tier**: [TIER 1 / TIER 2 / TIER 3 / TIER 4]
- **Authority**: [Who published/verified this?]
- **Date**: [Publication/update date]
- **Relevance**: [How does this apply to our analysis?]

## Key Content

[Main content from the source - structured and summarized]

### Section 1: [Topic Area]
[Details...]

### Section 2: [Topic Area]
[Details...]

## Critical Findings for Analysis

[Bullet list of key facts/metrics most relevant to the analysis]

## Known Limitations

[Caveats, regional variations, date considerations, etc.]

## Related Sources
[Cross-references to other sources in repository]

## Original Source Reference
[Citation, URL, document ID if applicable]
```

---

## Preparing Source Materials

### 1. Official/Regulatory Sources
- Save official documents (government sites, standards bodies)
- Extract key sections (don't store 100-page PDFs)
- Highlight provisions most relevant to the decision

### 2. Technical/Standard Documentation
- Compile from industry standards (ABNT, NBR, etc.)
- Include technical specs, material standards, performance requirements
- Note which standards are mandatory vs. recommended

### 3. Financial Data
- Gather cost benchmarks (2-3 industry sources)
- Document labor rates (current market data)
- Include historical pricing for trend analysis
- Note regional variations

### 4. Contractor/Vendor Data
- Compile ratings/reviews (aggregated, anonymized)
- Document insurance/licensing requirements
- Include reference projects
- Note verification methodology

### 5. Market Intelligence
- Industry reports (analyst firms, associations)
- Competitive landscape analysis
- Case studies (similar projects)
- Market trends & forecasts

---

## Quality Standards for Source Materials

✅ **DO:**
- Cite original source (URL, document ID, publication date)
- Note credibility tier in index.md
- Extract key facts with context
- Document limitations/caveats
- Keep format consistent across files
- Update materials when new info becomes available

❌ **DON'T:**
- Store raw, unorganized source files
- Include opinion without attribution
- Omit publication dates
- Forget to cite sources
- Assume agent knows what you meant
- Store outdated materials without noting version

---

## Repository Maintenance

### Initial Setup
1. Create `/workspace/[topic]/sources/` directory
2. Gather source materials
3. Organize into categories
4. Create `index.md` with inventory
5. Share with agent for analysis

### Ongoing
1. Add new sources as they become available
2. Update `index.md` when adding sources
3. Version reports as analysis evolves
4. Re-run analysis quarterly (or when major new source added)
5. Update cost data annually

### Re-Analysis Pattern
```
Initial Analysis (v1.0)
     ↓ [3 months later]
New sources added (permits updated, contractor data refreshed)
     ↓
Re-run analysis with updated sources
     ↓
Report v2.0 (highlights changes from v1.0)
```

---

## Example: Minimal Viable Repository

For a quick analysis, minimal structure:

```
/workspace/topic/
├── sources/
│   ├── index.md                    ← MUST HAVE
│   ├── technical-facts.md
│   ├── financial-data.md
│   └── regulatory-checklist.md
└── analysis-request.txt            ← User's question
```

**This is sufficient** to deliver valuable analysis. As the topic develops, add more detailed sources.
