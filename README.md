# Data Governance Toolkit

**Practical, ready-to-use data-governance templates for regulated teams - one artefact, mapped to GDPR, UAE PDPL, and the EU AI Act at once.**

> Built for the compliance reality you're actually facing. The **UAE PDPL** is in force, but its Executive Regulations have not yet been published - and once they are, organisations get six months to comply. The artefacts below are what you build in the meantime. Meanwhile the **EU AI Act**'s high-risk obligations are phasing in. This toolkit gives data leads, DPOs, and engineers the operational artefacts those regimes ask for - ROPA, DPIA, data classification, and an AI-system risk checklist - as fill-in-the-blanks documents you can use on Monday.

This is the operational side of governance: not the law, but the paperwork the law expects you to have.

---

## Who this is for

- **Data & analytics leads** standing up governance in a regulated or GCC organisation.
- **DPOs / privacy officers** who need a register and an assessment template that map to GDPR, UAE PDPL, and the EU AI Act.
- **Engineers** building data and AI systems - the AI-system risk checklist and the machine-readable classification + policy register say what "compliant by design" means in practice, and share policy IDs with the [`ai-compliance-gates`](https://github.com/mmubarak-io/ai-compliance-gates) CI checks.

## What's inside

| Template | Use it when… | Files |
|---|---|---|
| **Data Classification Matrix** | You need a shared definition of Public / Internal / Confidential / Restricted and the handling rules for each. | [`templates/data-classification/`](templates/data-classification/) |
| **ROPA - Record of Processing Activities** | You need a GDPR Art. 30 / PDPL processing register. | [`templates/ropa/`](templates/ropa/) |
| **DPIA - Data Protection Impact Assessment** | A project involves high-risk, large-scale, or new-technology processing. | [`templates/dpia/`](templates/dpia/) |
| **AI-System Risk Checklist** | You're putting an AI/LLM system anywhere near personal or regulated data. | [`templates/ai-system-risk-checklist/`](templates/ai-system-risk-checklist/) |
| **Breach Response** | You need a notification playbook + register for when a personal-data breach happens (GDPR Art. 33/34, PDPL). | [`templates/breach-response/`](templates/breach-response/) |

Plus a [frameworks crosswalk](docs/frameworks-crosswalk.md) (GDPR ↔ UAE PDPL ↔ EU AI Act), a [glossary](docs/glossary.md), fully-worked **synthetic examples** for every artefact ([`examples/`](examples/)), and a **machine-readable** layer ([`machine-readable/`](machine-readable/)) - the classification tiers and policy register as YAML, sharing policy IDs with the companion [`ai-compliance-gates`](https://github.com/mmubarak-io/ai-compliance-gates) repo so the *policy as documents* here lines up with *policy as code* there.

## Architecture / how the pieces fit

The toolkit models a small governance operating model: classification underpins everything, the ROPA records what you process, the DPIA assesses high-risk processing, and the AI risk checklist gates AI systems before they touch data.

![Toolkit operating model (ArchiMate)](assets/architecture/toolkit-overview.png)

## Preview

The data classification matrix (`.xlsx`), colour-coded by sensitivity:

![Data classification matrix](assets/screenshots/classification-matrix.png)

The ROPA register with the synthetic **SoukNova** example filled in - note how a single Restricted activity (seller KYC: Emirates ID + IBAN) links to a DPIA:

![ROPA register example](assets/screenshots/ropa-register.png)

## Quickstart

1. **Pick** the template you need from the table above.
2. **Copy** it and fill the `[bracketed]` fields - every template ships with a field-by-field guide.
3. **Review** the completed artefact with your DPO / legal function before relying on it.

## Frameworks covered

`GDPR (EU 2016/679)` · `UAE PDPL (Federal Decree-Law No. 45 of 2021)` · `EU AI Act (Regulation 2024/1689)`

See the [crosswalk](docs/frameworks-crosswalk.md) for how a single artefact satisfies obligations across regimes, and [`STATUS.md`](STATUS.md) for what is settled law versus a provisional reading - dated, and reviewed as regulations move.

## Roadmap

Dated, so you can see what's moving:

| Next | What | Status |
|---|---|---|
| **v1.1** | **Arabic (العربية)** - a parallel `-ar` file beside every English file, using the PDPL's own Arabic terms | In progress |
| v1.2 | **Saudi PDPL** mapping column - fully in force, and the Arabic work carries straight over | Planned |
| v1.2 | **DIFC / ADGM** mapping column - the free-zone regimes most GCC financial entities actually sit under | Planned |
| Later | ISO 42001 / NIST AI RMF cross-references on the AI risk checklist | Considering |

⭐ the repo to follow the Arabic release. Corrections against the regulations are the most useful contribution - see [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Contributing

Corrections against the regulations are the most useful contribution here - open an issue with the source. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the ground rules, and [`SECURITY.md`](SECURITY.md) for what to report privately instead (anything that looks like real personal data).

Repository consistency is checked in CI by [`scripts/check-repo.py`](scripts/check-repo.py): internal links, YAML validity, disclaimer coverage, an example per artefact, and that the policy IDs here still line up with the gates in `ai-compliance-gates`.

## Disclaimer

This toolkit is **not legal advice**. It is a set of starting-point templates. Always validate completed artefacts against the regulations that apply to you and with qualified counsel. See [`DISCLAIMER.md`](DISCLAIMER.md).

## License

[MIT](LICENSE) - use, adapt, and redistribute freely.

---

*Maintained by [Mohamed](https://github.com/mmubarak-io). Building data & AI that survives an audit, in regulated industries.*
