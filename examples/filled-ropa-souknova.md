# Worked Example - ROPA for "SoukNova"

> ⚠️ **Entirely fictional.** SoukNova is an invented e-commerce/fintech marketplace used to illustrate a completed ROPA. All names, data, and details are synthetic. Generate fake data (e.g. with [Faker](https://faker.readthedocs.io/)) for any demo - never use real records.

**Scenario:** SoukNova is a UAE-based marketplace app. Buyers create accounts and pay; sellers onboard with KYC and receive payouts. Below are three representative processing activities, completed using the [ROPA template](../templates/ropa/ROPA-template.md).

## Register header

| Field | Value |
|---|---|
| Organisation (controller) | SoukNova Marketplace FZ-LLC (fictional) |
| Controller contact | Lana Q., Head of Data, data@souknova.example |
| Data Protection Officer | Omar T., dpo@souknova.example |
| Date of last review | 2026-06-15 |
| Review cadence | Annually, or on material change |

## Activity 1 - Buyer account & order processing

| Field | Value |
|---|---|
| Activity name | Buyer account & order processing |
| Business owner | Consumer Product team |
| Purpose | Create/maintain buyer accounts; process orders and deliveries |
| Lawful basis | Contract (GDPR Art. 6(1)(b)); PDPL: necessary for performance of a contract |
| Data-subject categories | Buyers (adults) |
| Personal-data categories | Name, email, phone, delivery address, order history |
| Special / sensitive flag | No |
| Classification tier | Confidential |
| Source of data | Collected from the individual |
| Recipients / third parties | Delivery partner (processor); cloud hosting (processor) |
| Cross-border transfers | Cloud region outside UAE - covered by DPA + SCCs |
| Retention | Account life + 24 months after closure, then deleted |
| Security measures | TLS in transit, AES-256 at rest, role-based access, access logging |
| Linked DPIA? | N/A (not high-risk) |
| Last reviewed | 2026-06-15 |

## Activity 2 - Seller KYC & payouts

| Field | Value |
|---|---|
| Activity name | Seller KYC & payouts |
| Business owner | Payments & Compliance team |
| Purpose | Verify seller identity (KYC/AML); pay seller earnings |
| Lawful basis | Legal obligation (AML) + contract; PDPL: legal obligation + contract |
| Data-subject categories | Sellers (individuals & sole traders) |
| Personal-data categories | Name, **Emirates ID number**, **IBAN**, trade licence, contact details |
| Special / sensitive flag | **Yes** - national identifier + financial credentials |
| Classification tier | **Restricted** |
| Source of data | Collected from the individual; verified via KYC provider |
| Recipients / third parties | KYC verification provider (processor); payments processor |
| Cross-border transfers | KYC provider in adequate jurisdiction; transfer condition documented |
| Retention | Per AML retention rules (e.g. 5 years after relationship ends) |
| Security measures | Emirates ID & IBAN tokenised; encryption; allow-listed access; immutable access log |
| Linked DPIA? | **DPIA-2026-007** (large-scale processing of identifiers) |
| Last reviewed | 2026-06-15 |

## Activity 3 - AI support assistant (RAG over help-centre + tickets)

| Field | Value |
|---|---|
| Activity name | AI customer-support assistant |
| Business owner | Customer Experience team |
| Purpose | Answer buyer/seller queries using an LLM grounded in help articles and the user's own ticket history |
| Lawful basis | Legitimate interests (efficient support), balancing test recorded; PDPL basis documented |
| Data-subject categories | Buyers, sellers |
| Personal-data categories | Name, email, ticket content (may reference order/payment details) |
| Special / sensitive flag | Possible - tickets can contain financial details |
| Classification tier | Confidential (Restricted if payment data appears) |
| Source of data | Existing support tickets + help-centre content |
| Recipients / third parties | External LLM provider (processor) - **PII redacted before prompts** |
| Cross-border transfers | LLM provider region - DPA + transfer safeguard; provider-training opt-out enabled |
| Retention | Query/response logs retained 12 months for audit |
| Security measures | PII redaction pre-prompt; full query/response audit log; source-citation tracking; human escalation path |
| Linked DPIA? | **DPIA-2026-011** (new technology / AI) + **AI Risk Checklist** completed |
| Last reviewed | 2026-06-15 |

---

Notice how Activity 3 pulls in all three artefacts - a ROPA row, a DPIA, *and* the AI-System Risk Checklist - and how its safeguards (redaction before prompts, audit logging, citation tracking) are exactly what a guardrailed RAG implementation must provide.
