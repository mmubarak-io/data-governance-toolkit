# DPIA — Data Protection Impact Assessment

A DPIA assesses and mitigates the privacy risk of a processing activity *before* you build it. It is required under **GDPR Article 35** when processing is "likely to result in a high risk" to individuals, and the **UAE PDPL** requires an equivalent assessment for high-risk processing. A DPIA is also the natural place to assess an AI system that touches personal data.

> A `.docx` fillable version ships alongside this file. Complete the `[bracketed]` sections. Start with the trigger test in the [guide](DPIA-guide.md) — if no DPIA is required, record *that* decision and stop.

---

## 1. Project summary

| Field | Detail |
|---|---|
| Project / system name | `[ ]` |
| Owner & DPO | `[name, role]` / `[DPO name]` |
| Date / version | `[YYYY-MM-DD]` / `[v]` |
| Linked ROPA activity | `[reference]` |
| Description | `[what the project does, in 3–4 sentences]` |

## 2. Data flows

Describe the data lifecycle: what is collected, from whom, how it moves, where it is stored, who can access it, and when it is deleted.

```
Collected   : [data elements + source]
Stored      : [where, classification tier]
Used by     : [systems / teams]
Shared with : [recipients, processors, transfers]
Retained    : [period + deletion trigger]
```

## 3. Necessity & proportionality

- **Purpose:** `[why this processing is needed]`
- **Lawful basis:** `[GDPR Art. 6 / PDPL basis; Art. 9 condition if special-category]`
- **Could the purpose be met with less data or less intrusion?** `[data minimisation analysis]`
- **Data-subject rights:** how individuals are informed and can exercise access, rectification, erasure, objection. `[ ]`

## 4. Stakeholder consultation

| Stakeholder | Input / concern | Date |
|---|---|---|
| `[DPO]` | `[ ]` | `[ ]` |
| `[Security]` | `[ ]` | `[ ]` |
| `[Affected individuals / reps, if applicable]` | `[ ]` | `[ ]` |

## 5. Risk assessment

Score each risk: **Likelihood** (Low/Med/High) × **Severity** (Low/Med/High) → **Risk rating**.

| # | Risk to individuals | Likelihood | Severity | Rating | Mitigation | Residual rating |
|---|---|---|---|---|---|---|
| 1 | `[e.g. unauthorised access to sensitive data]` | `[ ]` | `[ ]` | `[ ]` | `[control]` | `[ ]` |
| 2 | `[e.g. data used beyond stated purpose]` | `[ ]` | `[ ]` | `[ ]` | `[control]` | `[ ]` |
| 3 | `[e.g. excessive retention]` | `[ ]` | `[ ]` | `[ ]` | `[control]` | `[ ]` |
| 4 | `[e.g. unlawful cross-border transfer]` | `[ ]` | `[ ]` | `[ ]` | `[control]` | `[ ]` |

## 6. Outcome & sign-off

| Field | Detail |
|---|---|
| Residual risk acceptable? | `[Yes / No — if high residual risk remains, prior consultation with the regulator may be required]` |
| Conditions / actions before go-live | `[ ]` |
| DPO recommendation | `[ ]` |
| Decision & owner | `[approved/rejected, by whom, date]` |
| Next review date | `[YYYY-MM-DD]` |

> If any residual risk remains **High** after mitigation, GDPR Art. 36 may require consulting the supervisory authority before proceeding. Record that step here.
