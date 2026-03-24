# Accuracy & Confidence Levels

## Purpose

Explicitly communicate how certain we are about each finding. Not all evidence is equal. Professional analysis distinguishes between "this is certain" and "this is a working hypothesis."

---

## The Confidence System

### Four Levels

#### 🟢 HIGH CONFIDENCE (95%+)

**Definition**: Multiple authoritative sources confirm. Finding is directly applicable. Certainty is very high.

**Characteristics**:
- Source: TIER 1 (official, primary)
- Evidence: Multiple confirming sources OR direct data
- Applicability: Directly on point, not extrapolated
- Basis: Quantitative data, not qualitative interpretation
- Contradiction: No conflicting sources

**Examples**:
- "ABNT NBR 6118 specifies 25mm minimum rebar cover for concrete" (official standard)
- "Current market labor rate in São Paulo is R$ 150-200/day for skilled labor" (multiple contractor quotes, industry report agree)
- "Building permit is required before construction in municipality" (government regulation)

**How to Use in Report**:
```
Finding: Floor load capacity is 500 kg/m²

Source: Structural design (ABNT NBR 6118) calculated by licensed engineer
Confidence: 🟢 HIGH (95%+)
Basis: Official code, professional calculation, certified design

Use this as: Project baseline. Safe to proceed on this assumption.
```

**Action if Findings Based on This**:
- Can recommend proceeding
- Can make commitments based on this
- Risk is minimal around this factor

---

#### 🟡 MEDIUM CONFIDENCE (70-94%)

**Definition**: Primary source or pattern emerges from evidence. Finding is solid but has limitations. Some uncertainty acceptable.

**Characteristics**:
- Source: TIER 1 + supporting evidence OR TIER 2 + multiple confirmations
- Evidence: Clear pattern but with caveats
- Applicability: Mostly applicable; some extrapolation
- Basis: Mix of quantitative + qualitative
- Contradiction: Minor contradictions or scope limitations noted

**Examples**:
- "Typical foundation costs R$ 25-35/m² for sandy soil" (industry benchmark + multiple project examples)
- "Building permit typically takes 3-4 weeks" (municipal report + actual project history)
- "Concrete curing requires 28 days at minimum" (ABNT standard + project experience)

**How to Use in Report**:
```
Finding: Expected timeline is 12 months for residential construction

Source: ABNT standards + 5 comparable completed projects
Confidence: 🟡 MEDIUM (80%)
Basis: Industry standard + verified project history
Limitations: If soil issues emerge, could extend timeline; requires experienced contractor
Contingency: Add 1 month buffer to be safe

Use this as: Planning baseline. Validate further if timeline-critical for project.
```

**Action if Findings Based on This**:
- Can use for planning but monitor closely
- Recommend contingency/buffer
- Flag as area for validation
- Escalate if timeline becomes critical

---

#### 🟠 LOW CONFIDENCE (50-69%)

**Definition**: Limited direct evidence. Working hypothesis with significant uncertainty. Further validation recommended for critical decisions.

**Characteristics**:
- Source: TIER 3 OR TIER 2 with significant limitations
- Evidence: Single source OR contradictory evidence not fully resolved
- Applicability: Extrapolation required; may not be exact fit
- Basis: Qualitative context OR narrow data set
- Contradiction: Some conflicting evidence; resolution unclear

**Examples**:
- "Material costs might increase 5-8% this year based on market commentary" (analyst opinion, not official data)
- "Similar project in different city took longer due to permit delays" (contextual but different situation)
- "Some contractors report difficulty finding skilled workers" (anecdotal evidence, not survey data)

**How to Use in Report**:
```
Finding: Material costs could experience modest inflation

Source: Industry commentator + one completed project report
Confidence: 🟠 LOW (60%)
Basis: Market opinion, not official pricing data
Limitations: Cost inflation is uncertain and project-dependent
Risk: If inflation >5%, budget impact is significant ($X)
Mitigation: Monitor market; lock in supplier quotes early

Use this as: Risk flag, not decision basis. Validate before committing.
```

**Action if Findings Based on This**:
- Cannot recommend action without further validation
- Should be flagged as assumption/risk
- Recommend contingency planning
- Escalate if critical to decision
- Gather more evidence before commitment

---

#### 🔴 UNVERIFIED (<50%)

**Definition**: No substantive source support. Expert opinion only. Assumption we're testing, not established fact.

**Characteristics**:
- Source: No TIER 1/2 support OR speculation/extrapolation
- Evidence: Minimal or anecdotal only
- Applicability: Highly speculative
- Basis: "We think" or "common sense" (not evidence-based)
- Contradiction: Contradicted by available evidence OR no evidence either way

**Examples**:
- "The market might shift to different building materials in future" (speculation, no data)
- "We could reduce timeline if we hire more people" (assumption, no evidence of scaling benefit)
- "Future interest rates will be higher" (forecasting, cannot be known)
- "The contractor will finish on time" (untested assumption, no track record)

**How to Use in Report**:
```
Finding: Future cost inflation may exceed current projections

Source: No reliable source data available
Confidence: 🔴 UNVERIFIED
Basis: Assumption based on general economic trends
Risk: High uncertainty; could impact budget significantly
Mitigation: Build contingency buffer; frequent cost monitoring
Action: Monitor economic indicators; reassess in 6 months

Use this as: Risk assumption, NOT decision basis.
Cannot recommend decision solely based on this.
```

**Action if Findings Based on This**:
- DO NOT recommend action
- MUST be flagged as assumption
- MUST have mitigation plan
- SHOULD have decision trigger ("if X happens, we revisit")
- Cannot use for commitments or promises

---

## How Confidence Affects Recommendation Strength

```
RECOMMENDATION STRENGTH BY CONFIDENCE

🟢 HIGH Confidence Finding
└─→ Strong Recommendation possible
    "We recommend proceeding—the evidence is clear"

🟡 MEDIUM Confidence Finding
└─→ Moderate Recommendation
    "We recommend proceeding if [condition], and monitor closely"

🟠 LOW Confidence Finding
└─→ Conditional Recommendation
    "Proceeding is possible, but validate X first"

🔴 UNVERIFIED Finding
└─→ NO Recommendation on this basis
    "We cannot recommend until this is verified"
```

---

## Assigning Confidence: Practical Approach

### Step 1: Identify the Claim

```
"The project will take 12 months to complete"
```

### Step 2: Trace to Source Evidence

```
Source: ABNT standards (standard curing = 28 days)
        + Comparable projects (typically 12 months)
        + Contractor estimate (scope-specific = 11-13 months)
```

### Step 3: Evaluate Source Quality

```
ABNT Standards:     TIER 1 (authoritative) ✓
Project Examples:   TIER 2 (established pattern) ✓
Contractor Ques:    TIER 2 (professional estimate) ✓
```

### Step 4: Check for Contradictions

```
Do sources agree?   Yes—all point to 12 months
Are there gaps?     None major—adequate evidence
Are limitations noted? Yes—assumes experienced contractor, standard conditions
```

### Step 5: Assign Confidence

```
Assessment:
├─ Multiple TIER 1 + TIER 2 sources ✓
├─ All sources aligned ✓
├─ No contradictions ✓
├─ Direct applicability ✓
└─ Some conditions required (experienced contractor)

Confidence Level: 🟡 MEDIUM (80%)
Not 🟢 HIGH because contractor selection is important variable
Not 🟠 LOW because evidence is strong
```

---

## Confidence Matrix for Reports

Create table showing all major findings + confidence:

| Finding | Evidence | Source(s) | Confidence |
|---------|----------|-----------|------------|
| Building permit required | Government regulation | Municipal code (TIER 1) | 🟢 95% |
| Permit timeline 3-4 weeks | Actual project data | 5 completed projects (TIER 2) | 🟡 85% |
| Foundation cost R$ 25-35/m² | Benchmarks + quotes | Industry report + contractors (TIER 2/3) | 🟡 75% |
| Total timeline 12 months | Standards + projects | ABNT + case studies (TIER 1/2) | 🟡 80% |
| Labor shortage emerging | Anecdotal reports | Contractor comments (TIER 3) | 🟠 60% |
| Material costs stable | No recent data | Assumption (NO SOURCE) | 🔴 UNVERIFIED |

---

## Confidence Rules

### Rule 1: Every Confidence Level Requires Justification

❌ DON'T:
```
"Labor costs are R$ 150/day"
Confidence: 🟢
```

✅ DO:
```
"Labor costs are R$ 150-200/day for skilled workers in São Paulo"
Confidence: 🟡 MEDIUM (80%)
Source: CREA labor report + 3 contractor quotes
Caveat: Rates vary by skill level, project risk, and market conditions
```

### Rule 2: No 🟢 HIGH Confidence Without TIER 1 Source

```
TIER 3 or TIER 4 Source Alone
└─→ Maximum confidence: 🟠 LOW (60%)
    Even if well-researched, tertiary sources have limits
```

### Rule 3: 🔴 UNVERIFIED Must Have Mitigation

```
Finding: (unverified assumption)

Confidence: 🔴 UNVERIFIED
Mitigation: [describe how you'll validate]
Decision Trigger: [if X happens, we revisit]
```

### Rule 4: Confidence ≠ Importance

```
A TIER 1 source saying "roof must support 150 kg/m²"
│
├─ Confidence: 🟢 HIGH
├─ Importance: CRITICAL (code requirement)
└─ Result: Must comply; non-negotiable

A TIER 3 source saying "consider green materials"
│
├─ Confidence: 🟠 LOW
├─ Importance: NICE-TO-HAVE (optional improvement)
└─ Result: Consider but not required
```

---

## Communicating Confidence in Writing

### In Executive Summary

```
Overall Assessment: Project is VIABLE (7.3/10)

Key Findings (Confidence Summary):
├─ Technical requirements are clear and achievable (🟢 HIGH)
├─ Regulatory path is straightforward (🟢 HIGH)
├─ Financial viability depends on budget contingency (🟡 MEDIUM)
├─ Market demand is strong (🟢 HIGH)
└─ Timeline assumes experienced contractor (🟡 MEDIUM)

CAUTION: Financial assessment is MEDIUM confidence due to tight budget.
         Recommend adding 15% contingency before commitment.
```

### In Detailed Findings

```
FINDING: Foundation Design Compliance

Statement: Foundation design complies with ABNT NBR 6118 for this soil type.

Evidence:
  - Geotechnical report identifies sandy soil (medium bearing capacity)
  - Structural engineer designed foundation for measured soil conditions
  - Design calculations verified against ABNT standards
  - Independent certification pending

Confidence: 🟡 MEDIUM (85%)
  Basis: ABNT standards are TIER 1; design is professional (experienced engineer)
  Caveat: Certification pending; unforeseen soil conditions could require redesign

Risk: If certification is denied, foundation redesign could delay 4-6 weeks

Mitigation: Geotechnical testing confirms soil; certification on-track

Recommendation: Proceed with foundation work; monitor certification timeline
```

### In Risk Register

```
RISK: Material Cost Inflation

Description: If material costs increase >10%, budget could exceed approved amount

Probability: MEDIUM (market trends suggest 5-8% inflation possible)
Impact: HIGH (would exceed budget and delay project)
Confidence in Risk Assessment: 🟠 LOW (60%)
  - Based on analyst opinion, not official forecasts
  - Historical inflation varies; trend unclear

Mitigation:
  1. Lock in supplier quotes now for key materials
  2. Monitor commodity price indices monthly
  3. Build 12% contingency in budget

Trigger: If inflation exceeds 8%, escalate to project sponsor
```

---

## Common Mistakes to Avoid

❌ **Claiming 🟢 HIGH when evidence is mixed**
- Confidence inflation erodes credibility
- Be honest about limitations
- If uncertain, use 🟡 MEDIUM

❌ **Using 🔴 UNVERIFIED without mitigation plan**
- Unverified assumptions are risks
- If you're basing decisions on them, they need contingencies
- If they're truly unknown, flag for research

❌ **Not updating confidence as evidence accumulates**
- Confidence can improve with new sources
- Confidence can decline if contradictions emerge
- Update assessments regularly

❌ **Mixing confidence with importance**
- A 🟠 LOW confidence finding can be CRITICAL (must verify)
- A 🟢 HIGH confidence finding can be MINOR (background info)
- Treat separately

✅ **DO: Assign confidence to every major claim**
✅ **DO: Update as new evidence emerges**
✅ **DO: Explain basis for confidence level**
✅ **DO: Use confidence to guide decision-making**
