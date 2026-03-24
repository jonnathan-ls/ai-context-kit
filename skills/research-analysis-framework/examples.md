# Examples - Real Analysis Workflows

## Purpose

Show how the framework works in practice. Real-world examples demonstrating the complete workflow from question through deliverable.

---

## Example 1: Housing Investment Decision (Detailed Walkthrough)

### SCENARIO

Parents in São Paulo considering investing R$ 500k in building a residential house. They want to know: Should we proceed? What are the risks?

### STEP 1: INTAKE (5-10 minutes)

**Question Clarification**:
```
Raw question: "Should we build a house?"

Clarified question:
├─ Are we asking: Financial viability? Technical feasibility? Timeline?
├─ Decision timeline: When do we need to decide?
├─ Constraints: Budget, timeline, location fixed?
├─ Success criteria: What does "good" look like?
└─ Stakeholders: Who's deciding? Who's affected?

Refined Question for Analysis:
"Should we proceed with R$ +/- 550k residential construction investment
in specified São Paulo location, on specified timeline,
given current market, regulatory, and technical conditions?
What are key risks and mitigations?"

Decision Timeline: 30 days (want to start Q1 2024)
```

### STEP 2: RESEARCH (30-60 minutes)

**Source Repository Preparation**:
```
Created: /workspace/casa-sao-paulo/sources/

Organized by Category:
├─ regulatory/ (Building codes, ABNT standards, permit requirements)
├─ technical/ (Construction standards, materials specs, soil data)
├─ financial/ (Cost benchmarks, market values, labor rates)
├─ market/ (Real estate trends in region, demand indicators)
├─ contractor/ (Contractor profiles, quotes, references)
└─ index.md [Master registry of all sources with tiers]
```

**Source Gathering**:

| Source | Tier | Category | Topic |
|--------|------|----------|-------|
| ABNT NBR 6118:2014 | 1 | technical | Structural design standards |
| ABNT NBR 8953:2015 | 1 | technical | Material specifications |
| São Paulo Building Code | 1 | regulatory | Local construction requirements |
| Municipal Permit Procedures | 1 | regulatory | Permit timeline & requirements |
| CREA Labor Report 2024 | 2 | financial | Labor rates & availability |
| 5 Completed Projects (local) | 2 | financial | Cost actuals & timeline |
| Contractor Quotes (3 firms) | 2 | financial | Project-specific estimates |
| Real Estate Market Report | 2 | market | Property values & trends |
| Regional Cost Benchmarks | 2 | financial | Industry $/m² data |
| Supervisor interviews (2) | 3 | contractor | Contractor comparisons |

### STEP 3: ANALYSIS (60 minutes)

**Viability Assessment**:

```
┌─ TECHNICAL FEASIBILITY ──────────────────┐
│ What We Evaluated                        │
│ ├─ Building codes compliance            │
│ ├─ Soil conditions & foundation design  │
│ ├─ Structural specifications            │
│ ├─ Material availability & standards    │
│ └─ Construction methodology             │
│                                         │
│ Findings                                │
│ ├─ Codes fully defined (ABNT standards) │
│ ├─ Sandy soil (medium bearing capacity) │
│ ├─ Standard residential design suitable │
│ ├─ All materials readily available      │
│ └─ Proven construction methods          │
│                                         │
│ Score: 8/10 ✓ SOLID                    │
│ Confidence: 🟢 HIGH (95%)              │
│ Risk: Soil conditions require testing  │
│ Mitigation: Geotechnical study pending │
└─────────────────────────────────────────┘

┌─ FINANCIAL VIABILITY ────────────────────┐
│ What We Evaluated                        │
│ ├─ Total project cost estimate          │
│ ├─ Budget vs. actual market rates       │
│ ├─ Contingency adequacy                 │
│ ├─ Cash flow & timing                   │
│ └─ ROI/asset value                      │
│                                         │
│ Findings                                │
│ ├─ Estimate R$ 550k based on:           │
│ │  ├─ Benchmark R$ 1100/m² cost         │
│ │  ├─ 500 m² × 1100 = R$ 550           │
│ │  └─ Verified by 3 contractor quotes   │
│ ├─ Budget provided: R$ 500k (gap!)      │
│ ├─ Contingency: ZERO (high risk!)       │
│ ├─ Market value: R$ 750k (positive)     │
│ └─ Funding: Equity (confirmed)          │
│                                         │
│ Score: 5/10 ⚠ TIGHT                    │
│ Confidence: 🟡 MEDIUM (80%)            │
│ Risk: Insufficient financial buffer    │
│ Mitigation: Increase budget to R$ 575k │
└─────────────────────────────────────────┘

┌─ REGULATORY COMPLIANCE ──────────────────┐
│ What We Evaluated                        │
│ ├─ Required permits & approvals         │
│ ├─ Zoning compliance                    │
│ ├─ Code compliance                      │
│ └─ Timeline for permits                 │
│                                         │
│ Findings                                │
│ ├─ Building permit required: Standard   │
│ ├─ Zoning: Residential (matches use)    │
│ ├─ Compliant with all codes             │
│ ├─ Permit timeline: 3-4 weeks           │
│ └─ Electrical/Plumbing: Licensed req.   │
│                                         │
│ Score: 9/10 ✓ EXCELLENT                │
│ Confidence: 🟢 HIGH (98%)              │
│ Risk: Minimal                           │
│ Mitigation: None needed                 │
└─────────────────────────────────────────┘

[MARKET + OPERATIONAL + RISK scores similar]

COMPOSITE VIABILITY: 7.3/10 (GOOD)
```

**Triangulation** (for critical finding: timeline = 12 months):

```
SOURCE METHOD: Similar projects
├─ Project A (2022): 12 months elapsed
├─ Project B (2023): 11 months elapsed  
├─ Project C (2023): 13 months elapsed
└─ Range: 11-13 months (consensus 12 months)

METHODOLOGY: Activity-based estimation
├─ Foundation: 2 months
├─ Structure: 4 months
├─ MEP: 4 months
├─ Finishes: 3 months
├─ Contingency: 1 month
└─ Total: 14 months (conservative)

EXPERT: Contractor estimate
├─ Reviewed plans & scope
├─ Considered crew capability
├─ Included weather buffer
└─ Estimated: 12 months (with standard crew)

DATA: Historical trend (5-year average)
└─ Average completion: 12 months (this region)

CONVERGENCE: All methods suggest 12-13 months
CONFIDENCE: 🟢 HIGH (90%+)
```

### STEP 4: PRESENTATION

**Executive Brief**:
```
HOUSING INVESTMENT DECISION

Recommendation: PROCEED IF budget increased to R$ 575k

Viability Score: 7.3/10 (GOOD - manage risks)

Top Risks:
1. Financial: Budget zero contingency → Add 15%
2. Market: Cost inflation possible → Lock quotes early
3. Execution: Contractor quality critical → Verify references

Next Steps:
1. Approve R$ 575k budget (THIS WEEK)
2. Soil testing + permit submission (This month)
3. Lock supplier quotes (Before breaking ground)

Timeline: Construction 12-14 months, completion Q1/Q2 2025

Full analysis shows project is viable with proper risk management.
```

**Financial Analysis**:
```
COST ESTIMATE
├─ Foundation:       R$ 80,000
├─ Structure:        R$ 200,000
├─ MEP:              R$ 120,000
├─ Finishes:         R$ 130,000
├─ Subtotal:         R$ 530,000
├─ Contingency(5%):  R$ 26,500
├─ TOTAL ESTIMATE:   R$ 556,500 (vs R$ 550k budget)
└─ RECOMMENDATION:   Approve R$ 575k (includes full 15% buffer)

SCENARIOS
├─ BEST CASE:    R$ 520k (cost underruns + efficiency)
├─ BASE CASE:    R$ 555k (as estimated)
├─ ROUGH CASE:   R$ 620k (15% inflation + issues)
└─ ASSET VALUE:  R$ 750k (market comparable)

FINANCIAL HEALTH
├─ Equity created: R$ 195k (R$ 750k value - R$ 555k cost)
├─ ROI: 35% cumulative (7-year horizon)
├─ Break-even: Year 5-6 (through appreciation)
└─ Risk if costs exceed R$ 575k: Would eliminate contingency
```

### STEP 5: DECISION SUPPORT

**Quality Checklist**:
- ✅ All claims source-traceable
- ✅ Viability scored across 6 dimensions
- ✅ Confidence levels assigned to findings
- ✅ Contradictions surfaced & resolved
- ✅ Assumptions documented
- ✅ Limitations acknowledged
- ✅ No unqualified certainty claims
- ✅ Recommendations justified by findings

**Bias Audit**:
- ✅ Red-team reviewed (found optimism risk in timeline, now conservative)
- ✅ Confirmation bias managed (actively sought contradictory evidence)
- ✅ Multiple estimation methods (top-down, bottom-up, benchmarks aligned)
- ✅ Contingency appropriate (15% is conservative for residential construction)

**Go/No-Go Criteria**:
```
PROCEED IF:
✓ Budget approved at R$ 575k (or scope reduced to R$ 500k)
✓ Geotechnical testing shows no major issues
✓ Permits on track for Q1 approval
✓ Contractor confirms timeline & crew

CAUTION IF:
⚠ Geotechnical testing reveals poor soil (redesign needed)
⚠ Permit delays indicated (>4 weeks)
⚠ Contractor expresses timeline concerns
⚠ Material inflation exceeds 8%

STOP IF:
🔴 Budget cannot be increased; funding unavailable
🔴 Zoning restriction emerges
🔴 Contractor unavailable or unreliable
🔴 Major geological issue found
```

---

## Example 2: Contractor Hiring Decision (Accelerated)

### SCENARIO

Need to hire contractor for construction. Have 3 candidates. Which one?

### ANALYSIS (Compressed)

**Question**: "Which contractor should we hire?"

**Sources Gathered**:
```
Contractor A:
├─ References: 5 past clients interviewed → All positive (9.2/10 avg)
├─ Credentials: CREA, insurance, licenses → All current
├─ Financial: Stable firm (10+ years) → No risk signals
├─ Track record: Last 5 projects → On-time 100%, budget +5% avg
└─ Interview: Professional, knowledgeable, understood scope

Contractor B:
├─ References: 1 contact available (others wouldn't respond) → Neutral
├─ Credentials: Licensed but insurance lapsed (⚠️)
├─ Financial: Smaller firm (3 years) → Limited track record
├─ Track record: Mixed (some on-time, some delayed)
└─ Interview: Enthusiastic but vague on methodology

Contractor C:
├─ References: Declined to provide → Red flag
├─ Credentials: Licensed but no insurance → Missing coverage
├─ Financial: Startup (1 year) → Unproven
├─ Track record: No visible track record → Unknown
└─ Interview: Aggressive price pitch, limited substance
```

**Scoring**:
```
CRITERIA        A ✓        B ⚠          C 🔴
──────────────────────────────────────────────
References      9/10       6/10         2/10
Credentials     10/10      6/10         4/10
Experience      9/10       5/10         2/10
Track record    9/10       6/10         0/10
Interview       8/10       6/10         5/10
Financial       9/10       5/10         3/10
Price quote     R$ 80k     R$ 65k       R$ 55k
──────────────────────────────────────────────
OVERALL SCORE   8.9/10     5.7/10       2.7/10

RECOMMENDATION:  HIRE A
```

**Risk Assessment**:
```
With Contractor A:
├─ Risk: Project execution at risk (low) 
├─ Risk: Budget overrun risk (low - track record shows +5% max)
├─ Risk: Timeline at risk (low - 100% on-time)
├─ Risk: Quality at risk (low - references confirm quality)
└─ Overall: LOW RISK ✓

With Contractor B:
├─ Risk: Insurance gap (HIGH - need coverage confirmed)
├─ Risk: Experience limited (MEDIUM - small firm, shorter track record)
├─ Risk: Mixed performance history (MEDIUM - some delays)
└─ Overall: MEDIUM-HIGH RISK ⚠

With Contractor C:
├─ Risk: Unproven (CRITICAL - zero track record)
├─ Risk: No insurance (CRITICAL - unmitigated exposure)
├─ Risk: Won't provide references (RED FLAG - integrity concern)
└─ Overall: VERY HIGH RISK 🔴
```

**Recommendation**: 
```
HIRE CONTRACTOR A

Contractor B could be backup if A becomes unavailable

DO NOT hire Contractor C (unproven, missing critical insurance, integrity concerns)
```

---

## Example 3: Market Entry Decision (Strategic)

### SCENARIO

Should we enter São Paulo residential construction market? Long-term strategic question.

### ANALYSIS (Strategic Level)

**Question**: "Is São Paulo residential construction market attractive for entry?"

**Six-Dimension Viability**:

```
1. MARKET VIABILITY: 9/10
   └─ High demand, growing population, supply shortage, pricing power
   └─ Confidence: 🟢 HIGH (official demographic data, market reports)

2. TECHNICAL FEASIBILITY: 8/10
   └─ Standard construction; proven methods; skilled labor available
   └─ Confidence: 🟢 HIGH (ABNT standards clearly defined)

3. FINANCIAL VIABILITY: 7/10
   └─ Attractive margins; proven ROI; healthy cash flow
   └─ Confidence: 🟡 MEDIUM-HIGH (benchmarks robust; actual project validation needed)

4. REGULATORY ENVIRONMENT: 7/10
   └─ Clear regulations; permitting works; some bureaucracy but manageable
   └─ Confidence: 🟡 MEDIUM (municipal procedures vary; some unpredictability)

5. COMPETITIVE POSITION: 6/10
   └─ Crowded market; many competitors; differentiation opportunity
   └─ Confidence: 🟡 MEDIUM (market share limited but growing)

6. OPERATIONAL CAPACITY: 6/10
   └─ Need to build team, capability, reputation in new market
   └─ Confidence: 🟠 LOW (depends on execution, hiring, partnership)

OVERALL SCORE: 7.2/10 (GOOD - enter with strategy)
```

**Risk Profile**:
```
HIGH RISKS:
├─ Market downturned (interest rates up, affordability down)
├─ Regulatory changes (permitting becomes harder)
└─ Competition intensifies (smaller margins)

MEDIUM RISKS:
├─ Finding experienced contractor partners
├─ Building reputation in new market
├─ Supply chain bottlenecks
└─ Labor shortage (skill availability)

LOW RISKS:
├─ Technical execution (proven methodology)
├─ Customer demand (market fundamentals strong)
└─ Regulatory compliance (clear framework)
```

**Mitigations**:
```
For market downturn risk:
├─ Start with modest portfolio (2-3 projects)
├─ Build financial reserves before scaling
├─ Design for different price points (flexibility)

For contractor partnerships:
├─ Develop relationships now (before scaling)
├─ Partner with established local builders
├─ Build backup suppliers/contractors

For competitive pressure:
├─ Target underserved segments (e.g., mid-market)
├─ Build reputation for quality/reliability
├─ Focus on customer experience
```

**Recommendation**:
```
ENTER MARKET with staged approach:

PHASE 1 (Year 1): Validation
├─ Build partnerships with 2-3 quality contractors
├─ Complete 2-3 pilot projects in different segments
├─ Validate unit economics and processes
├─ Establish brand/reputation

PHASE 2 (Year 2): Scale
├─ Expand to 5-8 concurrent projects
├─ Build internal capabilities (project management, sales)
├─ Refine processes based on pilot learnings
├─ Target 15-20% market share in segment

PHASE 3 (Year 3+): Consolidate
├─ Scale to industry player status
├─ Build brand recognition
├─ Develop residential construction platform
```

---

## Example 4: Technical Feasibility Review (Fast-Track)

### SCENARIO

New building design submitted. Engineering team wants quick validation: Is this feasible to build?

### ANALYSIS (Quick Format)

**Question**: "Is proposed design technically feasible?"

**Assessment**:
```
SPECIFICATION COMPLIANCE
├─ Building codes: ✓ Reviewed against ABNT NBR 6118
├─ Result: FULLY COMPLIANT (no violations detected)
└─ Confidence: 🟢 HIGH (official standards, engineer certified)

STRUCTURAL DESIGN  
├─ Load calculations: ✓ For sandy soil conditions
├─ Result: ADEQUATE (appropriate safety factors)
└─ Confidence: 🟢 HIGH (structural engineer certified)

MATERIAL SPECIFICATIONS
├─ Concrete, steel, finishes: ✓ All standard & available
├─ Result: SPECIFIED (current market supply confirmed)
└─ Confidence: 🟢 HIGH (supplier quotes available)

CONSTRUCTION METHODOLOGY
├─ Known techniques: ✓ Proven in this region
├─ Result: STANDARD (no novel/experimental methods)
└─ Confidence: 🟢 HIGH (5+ completed similar projects)

TIMELINE REALISM
├─ Activity estimation: ✓ Based on scope
├─ Result: 12 months FEASIBLE (with experienced contractor)
└─ Confidence: 🟡 HIGH (assumes quality contractor)

RISKS
├─ Soil conditions: Geotechnical study pending (LOW risk, testable)
├─ Supply availability: Currently confirmed (LOW risk)
├─ Contractor quality: Critical factor (MEDIUM risk, mitigable)
└─ No show-stoppers identified

VERDICT: TECHNICALLY SOUND ✓

Design is feasible to build. No technical barriers.
Standard construction using proven methods.
Proceed to next phase (permitting, contractor selection).
```

---

## How These Examples Show the Framework

**Pattern across all examples**:

1. **Question Clarified** → Specific decision framed
2. **Sources Gathered** → Tier-assigned evidence collected
3. **Analysis Done** → 6 dimensions assessed (or relevant subset)
4. **Confidence Assigned** → 🟢🟡🟠🔴 on key findings
5. **Triangulation Applied** → Multiple methods converge
6. **Bias Checked** → Known biases actively managed
7. **Recommendation Made** → Justified by evidence
8. **Risks Documented** → Mitigations clear
9. **Decision Enabled** → Reader can decide based on analysis

**All use the same framework, adapted to context**.

---

## Key Takeaways from Examples

✅ **What Worked Well**:
- Clear source tiers determined evidence weight
- Multiple estimation methods increased confidence
- Triangulation converged on similar answers (high confidence)
- Risk explicitly surfaced (not hidden)
- Contingencies matched risk profile

⚠ **Tension Points**:
- Budget too tight forced difficult trade-offs (reduce scope OR increase budget)
- Contractor quality critical but subjective (mitigated with references + scoring)
- Market uncertainty inherent (mitigated with contingency + scenario planning)
- Regulatory timeline unknowable (mitigated with early permit application)

🎯 **Decision Enablement**:
- Clear recommendation + conditions (not wishy-washy)
- Risk acknowledged but manageable (not hiding downsides)
- Next steps specific + actionable (not vague)
- Timeline realistic (not overly optimistic)
- Reader can confidently decide (whether to proceed or pivot)
