# Changelog

All notable changes to this toolkit are documented here. Format loosely follows [Keep a Changelog](https://keepachangelog.com/).

Nothing is tagged yet. The `v0.1.0` tag gets cut when the launch gate below clears.

## [Unreleased]

> ⚠️ **Launch gate:** This repository stays private/local until the maintainer's pre-launch review (outside-activities / IP clearance) is complete. See the local launch checklist (not committed).

### Added
- **Breach Response** template + guide (`templates/breach-response/`) - notification playbook + register mapped to GDPR Art. 33/34 and PDPL.
- Fully-worked **synthetic examples** for every artefact (`examples/`): DPIA, classification, AI-risk checklist, and breach response for "SoukNova" (joining the existing ROPA example).
- **Machine-readable** layer (`machine-readable/`): `classification.yaml` + `policy-register.yaml`, sharing policy IDs with `ai-compliance-gates` (policy-as-documents ↔ policy-as-code).
- `POL-GOV-001` (compliance tagging) and `POL-PRIV-005` (breach notification) in the policy register; every policy now carries an `enforcement:` status so "documented here" and "enforced in CI" can be told apart.
- Breach-notification row in the frameworks crosswalk, and glossary entries for personal-data breach, supervisory authority, Executive Regulations, and DIFC/ADGM.
- Community health files: `SECURITY.md`, `CODE_OF_CONDUCT.md`, issue + PR templates, `CODEOWNERS`.
- `scripts/check-repo.py` + a GitHub Actions workflow: link resolution, YAML parse, disclaimer presence, example coverage, house style, and a cross-repo policy-ID sync against `ai-compliance-gates`.

### Changed
- Retention and disposal defaults added to `classification.yaml`, so it covers all eight control rows of the matrix rather than six.
- `documented_by` in the policy register is now repo-relative paths only; prose moved to `documented_by_note` so tooling can resolve the field.
- House style: em-dashes replaced with hyphens across the markdown and the fillable `.xlsx` / `.docx`.

### Fixed
- "Not legal advice" notice added to the six templates and guides that shipped without one.
- The EU AI Act high-risk date is now hedged consistently in the checklist as well as the guide.
- Stale references to the removed diagram `.svg` export.

## [0.1.0] - content complete, not yet tagged

### Added (English markdown)
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
- ArchiMate diagram exported to PNG (`toolkit-overview.png`) and embedded in README so it previews inline on GitHub; `.drawio` kept as editable source.
- README screenshots (classification matrix + filled ROPA register).
- `.gitignore` (excludes lock files, OS cruft, and local-only notes).
- Pre-launch verification audit passed: shipped wording reviewed, `rag-with-guardrails` references marked as *(planned)*, synthetic data only and regulatory accuracy confirmed.

### Still to do before the v0.1.0 tag
- Outside-activities / IP clearance (see local launch checklist).
- Optional: PDF exports of the fillable docs.

## Planned for v0.2.0 (Arabic)
- Parallel `-ar` versions of every template, with RTL handling for the doc/sheet formats.
