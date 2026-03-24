# Examples - Practical Contract Analyses

## Example 1: Service Agreement (Consulting)

### Contract Snippet
```
SERVICE CONSULTING AGREEMENT

PARTIES: XYZ Consulting and ABC Company

2. OBJECT
Consulting services on process management as needed by contractor.

3. TERM
Indefinite term, auto-renewable.

4. COMPENSATION
R$ 500 per hour, as needed. Payment within 30 days of invoice.

6. LIABILITY
Consultant is liable for all direct, indirect and consequential damages, 
without limit.

7. TERMINATION
Contractor can terminate anytime without notice.
```

---

### Analysis by Our Framework

#### 1️⃣ EXECUTIVE SUMMARY
Consulting contract with multiple critical risks. Undefined scope and 
unlimited hours, unlimited liability, unilateral termination. **CRITICAL RISK** - 
Reject or fundamentally renegotiate.

#### 2️⃣ PROBLEMS IDENTIFIED

| # | Problem | Text | Risk | Impact | Action |
|---|---------|------|------|--------|--------|
| 1 | Vague Scope | "as needed" | 🔴 CRITICAL | Contractor can demand unlimited; permanent conflict | Specify hours/month; list exclusions |
| 2 | Indefinite Term | "indefinite, auto-renewable" | 🔴 CRITICAL | No guaranteed exit; permanent revenue uncertainty | Minimum 12 months; 60-day notice before renewal |
| 3 | Unlimited Liability | "all damages... without limit" | 🔴 CRITICAL | Undefined financial exposure; covers third-party damages | Cap indemnity: 12-month contract value; exclude indirect |
| 4 | Unilateral Termination | "anytime without notice" | 🟠 HIGH | No guaranteed revenue; no transition time | Minimum 60 days; 3-month indemnity if termination for convenience |
| 5 | No Clear Deliverables | No scope/schedule annexes | 🟡 MEDIUM | Ambiguity about what was "delivered" | Attach: detailed scope, schedule, acceptance criteria |

#### 3️⃣ POSITIVE POINTS

| Aspect | Clause | Importance |
|--------|--------|-----------|
| Hourly Rate | "R$ 500 per hour" | ✅ Clear value (better than "as needed") |
| Payment Deadline | "within 30 days of invoice" | ✅ Clear payment deadline |
| Simplicity | Short, direct contract | ✅ Easy to understand general terms |

**Recognition:** Contract isn't malicious, just heavily favors 
the contractor (client).

#### 4️⃣ RECOMMENDATIONS

**[CRITICAL - Reject this contract as-is]**

**Proposed Reformulation:**

```
2. OBJECT
Consulting services on process management - [insert specific processes] - 
consisting of monthly analysis, written recommendations, and quarterly 
presentation. Excludes: implementation, staff training, IT systems 
analysis (out of scope).

3. TERM
Initial term of 12 months (DD/MM/YYYY to DD/MM/YYYY).
Renews for 12 additional months, unless one party notifies 
termination with 60 days advance notice.

4. COMPENSATION
R$ 500 per hour, maximum 20 hours per month = R$ 10,000/month.
Monthly invoice, due by 10th of following month.
Annual adjustment: accumulated IPCA of prior year.

6. LIABILITY
6.1 Consultant liable for: direct damages from negligence.
6.2 Excluded liability:
    - Indirect, consequential, lost profits damages
    - Damages from client implementation failure
    - Damages from client decisions against consultant recommendation

6.3 Total indemnity limit: 12 months contract value = R$ 120,000

7. TERMINATION
7.1 For convenience: 60 days notice, indemnity of 3 months (R$ 30,000)
7.2 For breach: 15 days to remedy; then terminate at no cost
```

**Negotiation Language:**

```
Email to Client:

"We reviewed the contract and see mutual value in partnership, 
but some terms need adjustment for sustainability:

1. Scope needs limits (maximum hours) so both can budget
2. Unlimited liability exposes me to disproportionate risk
3. Indefinite term with immediate termination creates uncertainty

I've proposed reformulation that protects you (clear quality, 
defined scope) and me (predictable revenue, identified exposure).

Let's schedule a call to detail?"
```

#### 5️⃣ VERIFICATION CHECKLIST

- [ ] Scope defined with specific deliverables
- [ ] Hours/month or maximum specified
- [ ] Acceptance criteria/project end clear
- [ ] Term has explicit end date
- [ ] Termination deadline (minimum 30 days)
- [ ] Liability capped (not infinite)
- [ ] Indirect damages excluded
- [ ] Termination indemnity (if significant value)
- [ ] Confidentiality with deadline (ex: 3 years)
- [ ] IP allocated (consultant's prior work vs. new)

---

## Example 2: Rental Agreement (Lease)

### Contract Snippet
```
LEASE AGREEMENT - Residential House

PARTIES: Owner [Name] and Tenant [Name]

OBJECT: Property at [Address]

DURATION: [Indefinite] / [Until renovation completion]

MONTHLY VALUE: R$ 2,500

DEPOSIT: 1 month rent (release "per owner evaluation")

MAINTENANCE: Tenant responsible for most maintenance
  - Exterior painting
  - Structural repairs
  - Infiltration fixes

TERMINATION: Owner can evict tenant with 30 days notice, 
without cause. Tenant must renovate before leaving.
```

---

### Analysis

#### 🔴 CRITICAL ISSUES

| Problem | Risk | Fix |
|---------|------|-----|
| Disproportionate Obligations | Tenant responsible for everything; owner nothing | Law requires: owner responsible for structure; tenant for use/cleaning |
| Deposit "Per Evaluation" | Owner never returns (vague criteria) | Law requires return within 30d; justify deductions in writing |
| Indefinite/"Until Renovation" | Tenant never knows when term ends | Defined term (ex: 24 months) |
| Immediate Eviction | No notice/hearing right | Law requires: 30d notice + legal cause or agreement |
| Forced Renovation | New unexpected cost | Law: return to normal hygiene state; renovation is owner responsibility |

#### 🟡 RECOMMENDATIONS

**Standard Corrected Clause:**

```
CONTRACT LEASE - ADJUSTED

3. TERM
12-month term, starting DD/MM/YYYY, ending DD/MM/YYYY.
Renewal: 12 additional months if both parties agree in writing 
60 days before end.

4. VALUE AND PAYMENT
Rent: R$ 2,500/month
Due: 10th of each month via transfer to [owner account]
Annual adjustment: accumulated IPCA

5. SECURITY DEPOSIT
One (1) month rent = R$ 2,500
Return within 30 days after termination, deducted for:
  - Damages from tenant negligence
  - Unpaid rent/fees
Owner must provide detailed deduction justification.

6. RESPONSIBILITIES
6.1 OWNER:
    - Structural maintenance (foundations, walls, roof)
    - Systems (electrical, plumbing, heating)
    - Repairs from normal wear

6.2 TENANT:
    - Regular cleaning and hygiene maintenance
    - Care of included furniture/equipment
    - Repair of negligence-caused damages
    - State normal cleanliness upon vacating

6.3 PROHIBITED:
    - Structural renovation without written consent
    - Tenant responsible for renovation: NO

7. TERMINATION
7.1 For convenience: 30 days written notice
7.2 For breach: 
    - Notify arrears
    - 15 days to pay
    - If not paid, evict via legal process

8. PROPERTY RETURN
Tenant returns in normal hygiene state, without damage beyond 
normal wear. Renovation is owner responsibility.
```

---

## Example 3: Service Contract (E-commerce Setup)

### Red Flags Found

```
PROBLEM #1 - Inadequate IP Ownership
Text: "All work product belongs to Client"
Risk: 🔴 CRITICAL - Vendor can't use methodology in future projects

PROBLEM #2 - Unlimited Revisions
Text: "Unlimited revisions during project"
Risk: 🟠 HIGH - Project never ends; infinite scope

PROBLEM #3 - Payment Only on Completion
Text: "100% payment upon project delivery"
Risk: 🟠 HIGH - Vendor finances entire project; client can reject everything

PROBLEM #4 - No SLA or Performance Metrics
Risk: 🟡 MEDIUM - "Site must work well" is vague; no baseline/targets
```

### Recommendations

```
✅ SOLUTION: Structured Payment Milestones

Milestone 1 (30%): Design mockups approved → R$ 30,000
Milestone 2 (40%): Development complete → R$ 40,000
Milestone 3 (30%): Testing & launch → R$ 30,000

Revisions included: 2 rounds per milestone
Additional revisions: R$ 1,500/hour

✅ SOLUTION: Balanced IP Ownership

Pre-existing tools/components → Vendor retains
Custom code/design → Client exclusive ownership
Vendor retains → Right to use methods/processes in future projects

✅ SOLUTION: Performance Baseline

Site SLA: 99.5% uptime during business hours
Load time: < 3 seconds on standard connection
SEO audit: Score ≥ 90 on Lighthouse
```

---

## Key Takeaways from Examples

| Contract Type | Common Red Flag | Protection |
|---------------|-----------------|-----------|
| **Services** | Undefined scope + unlimited liability | Hours/month + liability cap |
| **Lease** | Disproportionate tenant obligations | Law-mandated division (structure vs. use) |
| **Project** | No milestones, infinite revisions | Payment by phase + capped revisions |
| **Partnership** | No clear exit/dissolution | Explicit term (12-24m) + termination notice |
| **Supply** | "Best efforts" with no metrics | Specify: deadline, quantity, quality |

---

## Negotiation Outcomes from Examples

### Example 1 Outcome
✅ **Consulting:** Accepted revision. Changed to 20h/month, 12-month cap, 
60-day termination with compensation. Result: Both comfortable with terms.

### Example 2 Outcome
⚠️ **Lease:** Owner accepted structure/responsibilities but resisted 
"automatic" deposit. Agreement: Deposit retained; return per law 
with written details.

### Example 3 Outcome
✅ **E-commerce:** Client preferred milestone payments (both happy). 
Agreed 2 revisions per milestone. IP: Client gets website, vendor retains 
right to reuse framework in future projects.
