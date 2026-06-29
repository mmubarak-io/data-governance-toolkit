# Frameworks Crosswalk — GDPR ↔ UAE PDPL ↔ EU AI Act

A quick map of how the toolkit's artefacts satisfy obligations across the three regimes. The point: one well-built artefact usually serves several regulators at once. This is a practitioner's orientation, **not legal advice** — provisions are summarised, not quoted.

## The three regimes at a glance

| | **GDPR** | **UAE PDPL** | **EU AI Act** |
|---|---|---|---|
| Instrument | Regulation (EU) 2016/679 | Federal Decree-Law No. 45 of 2021 + Executive Regulations (2026) | Regulation (EU) 2024/1689 |
| Scope | Personal data of people in the EU | Personal data of UAE residents (federal; free zones like DIFC/ADGM have their own laws) | AI systems placed on the EU market |
| Key deadline | In force since 2018 | Compliance expected by **1 Jan 2027** | High-risk obligations phasing toward **Dec 2027** |
| Regulator | National DPAs | UAE Data Office | National market-surveillance + EU AI Office |

## Obligation → artefact map

| Obligation | GDPR | UAE PDPL | EU AI Act | Toolkit artefact |
|---|---|---|---|---|
| Maintain a processing register | Art. 30 | Accountability / records obligations | — | **ROPA** |
| Assess high-risk processing before it starts | Art. 35 (DPIA) | Impact-assessment obligation for high-risk processing | Risk management for high-risk systems | **DPIA** + **AI Risk Checklist** |
| Lawful basis for processing | Art. 6 (and Art. 9 for special data) | Consent + defined exceptions | — | ROPA (lawful-basis field) |
| Data minimisation & purpose limitation | Art. 5 | Core principles | Data governance (high-risk) | DPIA §3, Classification |
| Security of processing | Art. 32 | Security obligations | Accuracy/robustness/cybersecurity (high-risk) | Classification + handling rules |
| Restrict cross-border transfers | Ch. V (adequacy/SCCs) | Transfer conditions to adequate jurisdictions | — | ROPA (transfer field), handling rules |
| Data-subject / individual rights | Arts. 12–22 | Access, rectification, erasure, objection | — | DPIA §3 |
| Transparency about AI | — | — | Limited-risk transparency duties | AI Risk Checklist §3 |
| Human oversight of AI | Art. 22 (automated decisions) | — | High-risk requirement | AI Risk Checklist §4 |
| Logging / record-keeping for AI | — | — | High-risk requirement | AI Risk Checklist §6 |
| Appoint a DPO | Art. 37 (where required) | Required in defined cases | — | ROPA header |

## How to read it

- **If you operate in the UAE**, the PDPL is your anchor and the Jan 2027 deadline is the forcing function — but building to GDPR-level artefacts means you're ready for both, plus EU customers.
- **If you build AI**, the EU AI Act adds obligations *on top of* data-protection law; an AI system handling personal data needs the privacy artefacts (ROPA, DPIA) **and** the AI controls (checklist).
- **Free zones:** DIFC (DP Law 2020) and ADGM have their own data-protection regimes that broadly track GDPR; check which applies to your entity.

> Always validate against the current text of each instrument and qualified counsel. See the [glossary](glossary.md) for terms.
