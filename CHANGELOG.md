# Changelog

All notable changes to this toolkit are documented here. Format loosely follows [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

> ⚠️ **Launch gate:** This repository stays private/local until the maintainer's pre-launch review (outside-activities / IP clearance) is complete. See the local launch checklist (not committed).

### Added (enhancements)
- **Breach Response** template + guide (`templates/breach-response/`) - notification playbook + register mapped to GDPR Art. 33/34 and PDPL.
- Fully-worked **synthetic examples** for every artefact (`examples/`): DPIA, classification, and AI-risk checklist for "SoukNova" (joining the existing ROPA example).
- **Machine-readable** layer (`machine-readable/`): `classification.yaml` + `policy-register.yaml`, sharing policy IDs with `ai-compliance-gates` (policy-as-documents ↔ policy-as-code).

### Added (English markdown - v0.1.0 content complete)
- Repository skeleton: README, MIT LICENSE, DISCLAIMER, CONTRIBUTING.
- **Data Classification Matrix** + handling rules + field guide.
- **ROPA** template + field guide.
- **DPIA** template + field guide (incl. the "when is a DPIA required" trigger test).
- **AI-System Risk Checklist** + guide with EU AI Act risk-tier mapping.
- **Frameworks crosswalk** (GDPR ↔ UAE PDPL ↔ EU AI Act) + **glossary**.
- One fully synthetic worked example (fictional "SoukNova" ROPA).
- ArchiMate architecture overview diagram (`assets/architecture/toolkit-overview.drawio`).

### Added (fillable formats)
- `ROPA-template.xlsx` - register with dropdowns (tier, lawful basis, Yes/No), header sheet, reference sheet, frozen panes.
- `classification-matrix.xlsx` - colour-coded matrix + handling-rules sheet.
- `DPIA-template.docx` - fillable, branded, with header/footer and "not legal advice" notice.

### Added (polish)
- ArchiMate diagram exported to PNG + SVG (`toolkit-overview.png` / `.svg`) and embedded in README so it previews inline on GitHub; `.drawio` kept as editable source.
- README screenshots (classification matrix + filled ROPA register).
- `.gitignore` (excludes lock files, OS cruft, and local-only notes).
- Pre-launch verification audit passed: shipped wording reviewed, `rag-with-guardrails` references marked as *(planned)*, synthetic data only and regulatory accuracy confirmed.

### Still to do before v0.1.0 tag
- Outside-activities / IP clearance (see local launch checklist).
- Optional: PDF exports of the fillable docs.

### Planned for v0.2.0 (Arabic)
- Parallel `-ar` versions of every template, with RTL handling for the doc/sheet formats.
