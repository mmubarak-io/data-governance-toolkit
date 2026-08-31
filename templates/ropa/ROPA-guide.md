# Field Guide - Filling the ROPA

How to complete the [ROPA template](ROPA-template.md) without it becoming shelfware.

## What a ROPA is for

It answers, on demand, "what personal data do you hold, why, and how is it protected?" Regulators ask for it first because it reveals whether you actually understand your own processing. A good ROPA is also the map you use for breach response, DPIA scoping, and data-subject requests.

## Controller vs processor

- A **controller** decides *why* and *how* personal data is processed. You maintain a full ROPA.
- A **processor** acts on a controller's instructions (e.g. a SaaS vendor). Processors keep a lighter record - categories of processing performed for each controller, transfers, and security measures - but still need one.

If you're unsure, ask: do we decide the purpose? If yes, you're a controller for that activity.

## Filling the trickier fields

- **Purpose (field 3):** specific verbs, not categories. "Send order-status notifications" beats "customer communications". Vague purposes fail audits.
- **Lawful basis (field 4):** pick exactly one Art. 6 basis per purpose. "Legitimate interests" requires a balancing test you can show. For special-category data, you *also* need an Art. 9 condition. Under PDPL, map to its lawful-basis equivalents (consent is the default; note the exceptions you rely on).
- **Special/sensitive flag (field 7):** if Yes, expect this activity to need a DPIA and a Restricted classification.
- **Cross-border transfers (field 11):** name the destination *and* the safeguard. "We use a US cloud provider" is a transfer - record the mechanism (SCCs, adequacy, or the relevant PDPL condition). PDPL restricts transfers to jurisdictions without adequate protection unless a condition is met.
- **Retention (field 12):** tie the period to the purpose and name the deletion trigger ("90 days after account closure"). "As long as needed" is not a retention period.

## Keeping it alive

- Review on the cadence you set in the header, and whenever a new system or purpose appears.
- One owner per row - accountability beats completeness.
- Link rows to DPIAs and to the classification register so the three reconcile.

## How this connects

- **Classification tier (field 8)** comes from the [classification matrix](../data-classification/classification-matrix.md).
- A **Yes** in the special/sensitive flag usually triggers the [DPIA](../dpia/DPIA-template.md).
- AI activities recorded here should also run the [AI-System Risk Checklist](../ai-system-risk-checklist/ai-risk-checklist.md).
