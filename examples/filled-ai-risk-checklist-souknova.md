# Worked Example - AI-System Risk Checklist for "SoukNova" support assistant

> ⚠️ **Entirely fictional.** SoukNova is an invented marketplace; all details are synthetic.

**Scenario:** SoukNova completes the [AI-System Risk Checklist](../templates/ai-system-risk-checklist/ai-risk-checklist.md) for its AI support assistant, alongside [DPIA-2026-011](filled-dpia-souknova.md). `[x]` = satisfied, with the note showing *how*. Any unchecked box records the accepted risk.

## 1. Prohibited-use screen
- [x] Not a prohibited practice - it answers support questions; no scoring, biometrics, or manipulation.

## 2. Data sourcing & PII
- [x] Sources and tiers known: help-centre content (Public), user's own tickets (Confidential). See the [classification example](filled-classification-souknova.md).
- [x] PII redacted **before** egress: names, emails, Emirates IDs, IBANs stripped/masked before any text reaches the LLM.
- [x] Lawful basis recorded in the ROPA (Activity 3: legitimate interests, balancing test on file).
- [x] Grounding data reviewed: help articles curated; ticket retrieval scoped to the requesting user only.

## 3. Transparency & disclosure
- [x] Users told it's AI: the chat opens with "You're chatting with SoukNova's AI assistant."
- [ ] Synthetic-media labelling - **N/A** (text-only assistant, no generated media). *Risk accepted: not applicable.*
- [x] Purpose, limits, intended use documented for the support team.

## 4. Human oversight & decisions
- [x] Human override: an agent can take over any conversation; no replies auto-send without agent review for sensitive cases.
- [x] No fully automated significant decisions - it drafts/answers support queries, it doesn't decide accounts or payments.
- [x] Agents trained on the assistant's limitations (AI-literacy note in onboarding).

## 5. Accuracy, robustness & bias
- [x] Accuracy measured against a benchmark set of 200 real-style questions; an **eval harness** re-runs on each prompt/model change.
- [x] Bias/fairness checked across languages (English/Arabic) and buyer vs seller queries.
- [x] Adversarial input considered: prompt-injection tests run; retrieval + system prompt hardened.

## 6. Logging & auditability
- [x] Every query and response logged with who/when/inputs/outputs/model version.
- [x] Source citations tracked - each answer records which help article / ticket it drew from.
- [x] Logs retained 12 months, stored at Confidential tier.

## 7. Security & third-party / LLM-vendor risk
- [x] LLM vendor covered by a DPA + transfer safeguard.
- [x] No Restricted data in prompts (redaction enforced); secrets and system prompt protected.
- [x] Vendor training opt-out enabled; vendor retention reviewed and minimised.

## 8. Lifecycle & monitoring
- [x] Named owner: Priya N. (Customer Experience Lead).
- [x] Post-deployment monitoring for drift, accuracy drop, and misuse.
- [x] AI-incident path defined and linked to the [breach-response runbook](../templates/breach-response/breach-response-template.md).
- [x] Review date set: 2026-09-12 (matches the DPIA review).

---

Every "how" note in sections 2, 6, and 7 - redaction before the model, citation tracking, full audit logging, the eval harness - is a concrete control, not a promise. That's the difference between a checklist that survives an audit and one that doesn't.
