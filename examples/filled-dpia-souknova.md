# Worked Example - DPIA for "SoukNova" AI support assistant

> ⚠️ **Entirely fictional.** SoukNova is an invented e-commerce/fintech marketplace. All names, data, and details are synthetic. Never use real records in a DPIA demo.

**Scenario:** SoukNova wants to launch an AI customer-support assistant (an LLM grounded in help articles and the user's own ticket history). Because it's new technology processing personal data at scale, it triggers a DPIA. This is the completed **DPIA-2026-011** referenced in [the ROPA example](filled-ropa-souknova.md), filled using the [DPIA template](../templates/dpia/DPIA-template.md).

## 1. Project summary

| Field | Detail |
|---|---|
| Project / system name | AI customer-support assistant (RAG) |
| Owner & DPO | Priya N., Customer Experience Lead / Omar T. (DPO) |
| Date / version | 2026-06-12 / v1.0 |
| Linked ROPA activity | Activity 3 - AI customer-support assistant |
| Description | An LLM answers buyer/seller support questions. It retrieves relevant help-centre articles and the requesting user's own past tickets, then generates an answer. A human agent can take over at any point. |

## 2. Data flows

```
Collected   : support tickets (name, email, message body which may reference orders/payments), help-centre content
Stored      : ticket store (Confidential); vector index of embeddings (Confidential); query/response logs (Confidential)
Used by     : Customer Experience team; the retrieval service; an external LLM provider (processor)
Shared with : external LLM provider - PII redacted before any text is sent; no data used to train the vendor's models
Retained    : query/response logs 12 months (audit); embeddings refreshed on source change; deleted on account closure
```

## 3. Necessity & proportionality

- **Purpose:** faster, more consistent support without expanding headcount. The assistant deflects repetitive questions and drafts answers for agents.
- **Lawful basis:** legitimate interests (efficient support). A balancing test is recorded: the impact on users is low given redaction and human oversight, and users can always reach a human. PDPL basis documented.
- **Could the purpose be met with less data or less intrusion?** Yes, and we applied it: PII is **redacted before** anything reaches the model; retrieval is scoped to the **requesting user's own** tickets only (no cross-user retrieval); payment values are masked at ingestion.
- **Data-subject rights:** users are told in the chat that they are talking to an AI and how to reach a human. Access/erasure requests flow through the existing DSAR process; a user's tickets and logs are deleted on account closure.

## 4. Stakeholder consultation

| Stakeholder | Input / concern | Date |
|---|---|---|
| Omar T. (DPO) | Wanted retrieval restricted to the user's own data and prompts logged for audit. Both adopted. | 2026-05-28 |
| Security | Required PII redaction before egress to the LLM vendor and vendor training opt-out. Both configured. | 2026-06-02 |
| Support agents (reps) | Asked for a clear "hand to human" control and no auto-sent replies. Adopted. | 2026-06-05 |

## 5. Risk assessment

| # | Risk to individuals | Likelihood | Severity | Rating | Mitigation | Residual rating |
|---|---|---|---|---|---|---|
| 1 | Personal data leaks to the external LLM provider | Med | High | High | Redact PII before egress; DPA + transfer safeguard; vendor training opt-out | Low |
| 2 | Retrieval surfaces another user's ticket ("confused deputy") | Med | High | High | Retrieval scoped to the requesting user's own records; access checks at query time | Low |
| 3 | Model gives a wrong/harmful answer treated as authoritative | Med | Med | Med | Source-citation tracking; human escalation path; no fully automated decisions | Low |
| 4 | Query/response logs over-retained | Low | Med | Low | 12-month retention with automatic deletion; logs at Confidential tier | Low |

## 6. Outcome & sign-off

| Field | Detail |
|---|---|
| Residual risk acceptable? | Yes - all residual risks reduced to Low after mitigation. |
| Conditions / actions before go-live | Confirm redaction runs on 100% of egress; confirm retrieval scoping in a pen test; enable query/response audit logging. |
| DPO recommendation | Approve, subject to the three go-live conditions and a review after 3 months of production use. |
| Decision & owner | Approved by Omar T. (DPO) and Priya N. (owner), 2026-06-12. |
| Next review date | 2026-09-12 (or on material change to the model/vendor) |

---

Notice how the mitigations here - **redaction before the model, per-user retrieval scoping, citation tracking, and full query/response logging** - are exactly the controls in the [AI-System Risk Checklist](../templates/ai-system-risk-checklist/ai-risk-checklist.md) and the spec a guardrailed RAG implementation must satisfy.
