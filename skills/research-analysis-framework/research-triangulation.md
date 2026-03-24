# Research Triangulation - Validation Methods

## Purpose

Validate key findings using multiple independent approaches. When different methods produce the same conclusion, confidence dramatically increases.

---

## What is Triangulation?

**Definition**: Using multiple independent methods/sources to arrive at the same conclusion.

**Why It Matters**:
- Single-source findings can be wrong or biased
- Multiple methods reaching same conclusion = high confidence
- If methods diverge, signals investigation needed

**Mathematical Effect**:
```
Single Source Evidence:  confidence = 🟡 MEDIUM (70%)
Two Sources Confirming: confidence = 🟡 MEDIUM-HIGH (80%)
Three Methods Aligned:  confidence = 🟢 HIGH (90%+)
```

---

## Four Types of Triangulation

### 1. SOURCE TRIANGULATION

**Method**: Multiple different sources confirm same finding

**Process**:
```
Question: "What is typical construction labor cost?"

Source 1: CREA Labor Report 2024
  └─ Finding: R$ 150-180/day for skilled labor

Source 2: Three Contractor Quotes
  └─ Finding: R$ 160, R$ 165, R$ 155/day

Source 3: Industry Benchmark Report
  └─ Finding: R$ 155-185/day in this region

Conclusion: All three sources align → R$ 155-180/day is strongly supported
Confidence: 🟢 HIGH (90%+)
```

**Application**:
- Compare TIER 1 sources with TIER 2 sources
- Get multiple expert estimates
- Review similar project data
- Look for pattern across sources

**Strengths**:
- Most straightforward validation
- Easy to explain to stakeholders
- Multiple sources = lower bias risk

**Limitations**:
- All sources may be wrong the same way
- Availability of multiple sources varies
- Sources may copy each other (not independent)

---

### 2. METHODOLOGICAL TRIANGULATION

**Method**: Different analytical approaches reach same conclusion

**Process**:
```
Question: "What will this house cost?"

Method 1: Top-Down Estimation (Cost per m²)
  Calculation: 500 m² × R$ 1100/m² = R$ 550,000

Method 2: Bottom-Up Estimation (Sum of Components)
  Foundation:      R$ 80,000
  Structure:       R$ 200,000
  MEP (Mech/Elec): R$ 120,000
  Finishes:        R$ 130,000
  Total:           R$ 530,000

Method 3: Historical Comparison (Similar Project)
  Similar project cost: R$ 520,000
  This project is +5% complexity = R$ 546,000

Convergence: Three methods yield R$ 530-550k range
Conclusion: Estimate of R$ 550k is reasonable
Confidence: 🟢 HIGH (90%+)
```

**Application**:
- Top-down vs. bottom-up budgeting
- Multiple estimation techniques for timeline
- Different analytical frameworks yielding same result
- Monte Carlo + deterministic both suggest similar outcome

**Strengths**:
- Validates methodology
- If both approaches wrong in same direction = unlikely
- Reveals estimation bias

**Limitations**:
- Can be time-consuming
- Requires expertise in multiple methods
- Not all questions support multiple methods

---

### 3. DATA TRIANGULATION

**Method**: Different data types/time periods confirm pattern

**Process**:
```
Question: "Is labor shortage emerging in construction?"

Data Point 1: Contractor Hiring Difficulty Survey
  Finding: 65% of contractors report difficulty hiring
  
Data Point 2: Wage Trends (Last 12 Months)
  Finding: Labor wages up 12% year-over-year (vs. 3% inflation)

Data Point 3: Project Timeline Extensions
  Finding: 40% of completed projects extended due to labor
  
Data Point 4: Historical Comparison (5 years ago)
  Finding: At that time, 5% reported hiring difficulty, 2% wage growth

Convergence: Multiple independent data points all point to labor shortage
Conclusion: Labor shortage is real and accelerating
Confidence: 🟢 HIGH (95%+)
```

**Application**:
- Current data + historical data both show pattern
- Quantitative metrics + qualitative feedback both confirm
- Different geographic/demographic slices show same trend
- Different time periods show consistency

**Strengths**:
- Pattern validation increases confidence significantly
- Hard to fake pattern across multiple data dimensions
- Historical comparison adds time-depth validation

**Limitations**:
- Requires robust data collection
- Time-consuming to gather multiple data points
- Some dimensions may not have available data

---

### 4. EXPERT TRIANGULATION

**Method**: Independent experts reach same conclusion

**Process**:
```
Question: "Is this building design technically sound?"

Expert 1: Structural Engineer (5+ years, certified)
  Review: Design is sound and meets ABNT standards

Expert 2: Building Inspector (20+ years, government)
  Review: No code violations identified

Expert 3: Geotechnical Engineer (15+ years, university)
  Review: Foundation design appropriate for soil conditions

Consensus: All three independent experts endorse design
Confidence: 🟢 HIGH (98%+)
```

**Application**:
- Get multiple independent professional reviews
- Experts with different specialties reach same conclusion
- Reviews based on different criteria all align
- Red-team review + standard review both agree

**Strengths**:
- Expert agreement is powerful validation
- Different expertise areas confirm from multiple angles
- Hard for experts to be biased in same direction

**Limitations**:
- May be expensive to get multiple expert reviews
- Experts may defer to consensus (groupthink risk)
- Need to ensure independence (not discussing findings)

---

## Triangulation Matrix: How to Apply

### Step 1: Identify Key Finding Requiring Validation

```
Major Finding: "Timeline should be 12 months"
Critical? YES (decision depends on this)
Current Confidence: 🟡 MEDIUM (75%)
Action: Triangulate to raise confidence
```

### Step 2: Select Triangulation Methods

| Finding Type | Best Validation Methods |
|---|---|
| **Cost** | Source (benchmarks) + Methodology (top/bottom-up) + Data (historical) |
| **Timeline** | Source (project history) + Methodology (activity-based) + Expert (contractor) |
| **Risk** | Source (similar projects) + Expert (specialized) + Data (trends) |
| **Viability** | Methodology (multiple frameworks) + Data (scenarios) + Expert (domain) |
| **Technical** | Expert (engineer review) + Data (testing) + Source (standards) |

### Step 3: Gather Evidence for Each Method

```
Timeline Finding Triangulation:

[SOURCE] Get 5 similar completed projects
  → Extract actual timelines
  → Identify variables (soil, weather, complexity)

[METHODOLOGY] Build activity-based timeline
  → Break into phases with dependencies
  → Estimate each phase
  → Check against ABNT standards

[EXPERT] Contractor detailed estimate
  → Based on scope & conditions
  → Include contingency
  → Note assumptions

[DATA] Check historical trend
  → Projects in this region taking longer?
  → Market conditions changed?
  → Supply chain impacts?
```

### Step 4: Compare Results

```
Source Method:        11-13 months (5 projects)
Methodology Method:   12 months (activity-based calc)
Expert Method:       12 months (contractor estimate)
Data Trend:          12 months (historical average)

RESULT: High convergence → Confidence = 🟢 HIGH (90%+)
```

### Step 5: Document Triangulation

In report:
```
FINDING: Project timeline is 12 months

Triangulation Evidence:
  ├─ [SOURCE] Similar projects: 11-13 months (5 completed projects, local market)
  ├─ [METHODOLOGY] Activity-based: 12 months (detailed WBS + timings)
  ├─ [EXPERT] Contractor estimate: 12 months (with standard contingency)
  └─ [DATA] Historical trend: 12 months (5-year average, this region)

Convergence: All four methods align in 12-month range
Confidence: 🟢 HIGH (90%+)

Mitigations:
  - Experienced contractor critical (unknown contractor = risk)
  - Standard weather conditions assumed (extreme weather could extend)
  - No major permit delays anticipated (regulatory delays could extend)

Contingency: Add 1 month buffer for realistic timeline of 13 months
```

---

## Dealing with Triangulation Conflicts

### When Methods Disagree

```
CONFLICT SCENARIO:

Methodology Says: 12 months
Expert Says:     14 months
Source Data:     10-12 months

Analysis:
├─ Why methodology low? (Didn't include setbacks?)
├─ Why expert high? (Conservative estimate?)
└─ Why source favors methodology? (Selection bias? Simpler projects?)

Resolution:
Case 1: Expert is more experienced → Weight expert opinion higher  
Case 2: Methodology has flaw → Fix methodology & recalculate
Case 3: All valid but different assumptions → Document range & assumptions
```

**Do NOT**:
- Average conflicting estimates (hides real uncertainty)
- Pick the one you like (cherry-picking)
- Ignore conflicts (transparency demanded)

**DO**:
- Investigate why differences exist
- Assess which method is more reliable
- Document the range + driver of disagreement
- Set contingencies accordingly

---

## Triangulation Checklist

For each major finding:

- [ ] Can this finding be triangulated? (Is it important enough?)
- [ ] What triangulation methods are feasible? (Sources, Methodology, Data, Expert?)
- [ ] Have I gathered evidence for each method?
- [ ] Do methods converge or conflict?
- [ ] If conflict, have I investigated cause?
- [ ] Have I documented findings of each method?
- [ ] Is confidence level justified by triangulation?
- [ ] Are contingencies appropriate for remaining uncertainty?

---

## Practical Example: Contractor Selection Decision

**Question**: "Should we hire this contractor?"

**Finding**: "Contractor is reliable and competent"

**Triangulation Plan**:

```
1. SOURCE TRIANGULATION
   └─ Gather references from past clients
      5 companies confirm: "Reliable, good quality, on-time"

2. METHODOLOGY TRIANGULATION
   └─ Assess capability using two frameworks
      A) Credential check (licenses, insurance, certifications) → ✓ PASS
      B) Interview + sample project review → ✓ PASS

3. DATA TRIANGULATION
   └─ Analyze historical project performance
      Last 5 projects: On-time 100%, Budget variance avg 5%, Quality score 9.2/10

4. EXPERT TRIANGULATION
   └─ Get opinion from two independent experts
      Building inspector: "Contractor is thorough and compliant"
      Project manager (independent): "Would hire again"

CONVERGENCE: All four methods strongly support contractor selection
CONFIDENCE: 🟢 HIGH (95%+)
RECOMMENDATION: Hire this contractor with confidence
```

---

## When Triangulation Isn't Possible

Some findings can't be triangulated (e.g., future conditions):

```
Finding: "Interest rates will remain stable"
├─ Can't triangulate (prediction, not current fact)
├─ Confidence: 🔴 UNVERIFIED
├─ Classification: Assumption, not validated finding
└─ Response: Include in contingency planning
```

In this case:
- Document it as assumption
- Note what would change if assumption breaks
- Include financial stress test
- Design decision trigger ("if rates rise >2%, revisit plan")

---

## Summary: Triangulation Workflow

```
FINDING
   ↓
Is it critical? YES
   ↓
Can it be triangulated? YES
   ↓
[Gather evidence for 2-4 methods]
   ↓
Do methods converge? YES → Confidence UP (🟡→🟢)
                     NO  → Investigate differences
   ↓
Document triangulation
   ↓
Adjust confidence level accordingly
```
