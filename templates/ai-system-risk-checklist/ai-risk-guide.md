# Guide — The AI-System Risk Checklist and the EU AI Act

How to read the [checklist](ai-risk-checklist.md) against the EU AI Act's risk tiers, and why this matters for regulated teams.

## The EU AI Act in one screen

The Act regulates AI by **risk tier**, with heavier obligations as risk rises:

| Tier | What it covers | What's required | Status |
|---|---|---|---|
| **Unacceptable / prohibited** | Social scoring, manipulative techniques, untargeted facial scraping, certain biometric categorisation. | Banned outright. | In effect since **Feb 2025**. |
| **High-risk** | Systems in sensitive domains (Annex III) — e.g. credit/creditworthiness, employment, essential services, biometrics. | Risk management, data governance, technical documentation, logging, human oversight, accuracy/robustness, conformity assessment, registration. | Main Annex III obligations phase toward **2 Dec 2027** (per the May 2026 Digital Omnibus); product-embedded systems toward **Aug 2028**. |
| **Limited risk (transparency)** | Chatbots, AI-generated content, deepfakes. | Disclose that users are dealing with AI; label synthetic content. | Applying. |
| **Minimal risk** | Most other AI. | No mandatory obligations. | n/a |
| **General-purpose AI (GPAI)** | Foundation models. | Provider transparency/documentation duties. | Applying since **Aug 2025**. |

> Dates move. The Digital Omnibus (provisional agreement, May 2026) pushed the main high-risk deadline back; always confirm the current timeline before relying on a date.

## Why a regulated-grade AI needs this

For a regulated organisation, the relevant question is rarely "is this minimal risk?" — it's "what do we have to prove if a regulator asks?" The high-risk obligations (data governance, logging, human oversight, accuracy, documentation) are good engineering practice regardless of whether your specific system is formally in-scope. Treating them as the default bar is what "data & AI that survives an audit" means in practice.

## How the checklist sections map to the tiers

- **§1 Prohibited screen** → the unacceptable tier. A one-time gate; if you trip it, stop.
- **§2 Data sourcing, §5 Accuracy/bias, §6 Logging, §8 Monitoring** → the core **high-risk** obligations (data governance, accuracy/robustness, record-keeping, post-market monitoring).
- **§3 Transparency, §4 oversight/AI-literacy** → the **transparency** duties (and the human-oversight high-risk requirement).
- **§7 Vendor/transfer** → overlaps the AI Act and PDPL/GDPR transfer rules — the intersection most teams miss.

## How this connects to the rest of the toolkit

An AI system processing personal data typically needs **all three**: a ROPA entry, a DPIA, *and* this checklist. The DPIA covers privacy risk to individuals; this checklist covers AI-specific risk (bias, oversight, model/vendor exposure) the DPIA won't prompt for. The classification matrix tells you the sensitivity of the data feeding the model.
