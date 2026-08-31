# Field Guide - When and How to Run a DPIA

The most useful part of a DPIA is knowing *when* you need one. This guide gives you the trigger test, then how to complete the [template](DPIA-template.md).

> **Not legal advice** - the trigger test is orientation, not a legal determination. Confirm whether a DPIA is required with your DPO or counsel.

## Do you even need a DPIA? (the trigger test)

A DPIA is required when processing is **likely to result in a high risk** to individuals. Run one if **any** of these apply:

- **Large-scale processing of special-category or sensitive data** - health, biometric, financial credentials, Emirates ID, etc.
- **Systematic, extensive profiling or automated decision-making** with legal or similarly significant effects.
- **Systematic monitoring** of a publicly accessible area, or large-scale tracking of behaviour.
- **New technologies** whose privacy impact isn't well understood - including **AI/ML and LLM-based systems** processing personal data.
- **Combining or matching datasets** from different sources in ways individuals wouldn't expect.
- **Processing data about vulnerable individuals**, including children.
- **Preventing data subjects from exercising a right** or using a service.

Rule of thumb: meet **two or more** of the EU regulators' nine criteria and you almost certainly need one. **If in doubt, do it** - a short DPIA that concludes "low risk" is cheap insurance and itself a record of accountability.

> Always record the trigger decision, even when the answer is "no DPIA required". That negative record is itself evidence of accountability.

## Completing each section

- **Data flows (§2):** draw the lifecycle before scoring risk - most risks are obvious once the flow is on paper. Tag each store with its classification tier.
- **Necessity & proportionality (§3):** this is where DPIAs add value. Challenge every data element: is it needed for the stated purpose? Minimisation is the strongest mitigation.
- **Risk scoring (§5):** score risk *to the individual*, not to the business. Likelihood × severity. Then re-score after mitigation to get the residual rating.
- **Sign-off (§6):** a DPIA without a decision and an owner is unfinished. If High residual risk remains, note the Art. 36 prior-consultation step.

## How this connects

- A DPIA is usually triggered by a **Yes** in the ROPA special/sensitive flag; link the two by reference.
- For AI systems, run the [AI-System Risk Checklist](../ai-system-risk-checklist/ai-risk-checklist.md) **alongside** the DPIA - the checklist covers AI-specific risks (bias, oversight, LLM-vendor exposure) the DPIA's generic risk table won't prompt for.
