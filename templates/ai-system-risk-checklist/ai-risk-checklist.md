# AI-System Risk Checklist

A pre-deployment checklist for any AI/ML or LLM system that touches personal or regulated data. It exists because "you can't just point an LLM at customer data" - doing so safely in a regulated environment requires specific controls that a generic DPIA won't prompt for.

Each item is tagged with the **EU AI Act** risk dimension it speaks to. Items marked **[High-risk]** map to obligations that apply to high-risk systems (Annex III), whose main deadline now phases in toward **2 December 2027**. Items marked **[Transparency]** map to the limited-risk transparency duties already in effect.

> Work top to bottom. Any unchecked box is a risk you're accepting - record why. Run this **alongside** a [DPIA](../dpia/DPIA-template.md), not instead of one.

## 1. Prohibited-use screen (do this first)

- [ ] The system does **not** perform a prohibited practice (social scoring, untargeted facial-image scraping, manipulative or exploitative techniques, certain biometric categorisation). *If it might, stop and get legal review.*

## 2. Data sourcing & PII

- [ ] We know the **classification tier** of every data source feeding the model (link to [classification matrix](../data-classification/classification-matrix.md)). **[High-risk]**
- [ ] Personal/Restricted data is **redacted, masked, or pseudonymised before it reaches the model or any third-party LLM.**
- [ ] Lawful basis for using this data to train/prompt the model is recorded in the [ROPA](../ropa/ROPA-template.md).
- [ ] Training/grounding data is assessed for representativeness and quality. **[High-risk]**

## 3. Transparency & disclosure

- [ ] Users are told they are interacting with an AI system. **[Transparency]**
- [ ] AI-generated or manipulated content is labelled where required (e.g. synthetic media). **[Transparency]**
- [ ] The system's purpose, limitations, and intended use are documented for deployers. **[High-risk]**

## 4. Human oversight & decisions

- [ ] A human can review, override, or stop the system's outputs. **[High-risk]**
- [ ] No legal or similarly significant decision about a person is fully automated without a lawful basis and a route to human review.
- [ ] Operators are trained on the system's limitations (AI literacy). **[Transparency]**

## 5. Accuracy, robustness & bias

- [ ] The system has measured accuracy/performance against a defined benchmark, with an **eval harness** that can be re-run. **[High-risk]**
- [ ] Bias/fairness across relevant groups has been tested and documented. **[High-risk]**
- [ ] Behaviour under adversarial or out-of-distribution input has been considered (prompt injection, jailbreaks).

## 6. Logging & auditability

- [ ] Every query and response is **logged** with enough context to reconstruct a decision (who, when, inputs, outputs, model/version). **[High-risk]**
- [ ] For retrieval/RAG systems, **source citations are tracked** so any answer can be traced to its source documents.
- [ ] Logs are retained per policy and protected at the right classification tier.

## 7. Security & third-party/LLM-vendor risk

- [ ] Data sent to any external model provider is covered by a contract/DPA and an appropriate transfer safeguard (PDPL/GDPR). **[High-risk]**
- [ ] Secrets, prompts, and system instructions are protected; no Restricted data in prompts unless explicitly authorised.
- [ ] Vendor data-retention and training-on-your-data settings are reviewed and configured (e.g. opt-out of provider training).

## 8. Lifecycle & monitoring

- [ ] A named owner is accountable for the system in production. **[High-risk]**
- [ ] Post-deployment monitoring is in place for drift, degraded accuracy, and misuse. **[High-risk]**
- [ ] An incident path exists for AI-specific failures (harmful output, leakage), linked to breach response.
- [ ] A review/retirement date is set.

---

### From checklist to flagship

Sections 2, 6, and 7 - redaction before the model, citation tracking, full query/response audit logging, and an eval harness - are exactly the requirements a guardrailed RAG implementation must satisfy. This checklist is the spec; a companion reference implementation (`rag-with-guardrails`, *planned*) will be the working proof. See the [AI risk guide](ai-risk-guide.md) for the EU AI Act tier mapping in detail.
