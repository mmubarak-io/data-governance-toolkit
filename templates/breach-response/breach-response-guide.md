# Guide - When and how to notify a breach

The hard decisions in a breach are two: **must you notify the regulator?** and **must you tell the affected people?** This guide walks both. It is orientation, **not legal advice** - confirm the exact triggers and deadlines that apply to you.

## First: is it a personal-data breach at all?
A personal-data breach is a breach of security leading to the accidental or unlawful **destruction, loss, alteration, unauthorised disclosure of, or access to** personal data. That includes a lost laptop, a mis-sent email, ransomware, or a vendor being breached - not only "hackers stole the database."

## Decision 1 - Notify the supervisory authority / UAE Data Office?
Under **GDPR Art. 33**, notify the supervisory authority **without undue delay and, where feasible, within 72 hours** of becoming aware, **unless** the breach is unlikely to result in a risk to individuals. The **UAE PDPL** requires notifying the **UAE Data Office** of a breach that would prejudice the privacy, confidentiality, or security of the data subject's data.

Rule of thumb: if there's any realistic risk to individuals, notify. "We weren't sure" is not a defence, and the register should record the decision either way.

The notification should describe: the nature of the breach, categories and approximate numbers affected, likely consequences, and the measures taken or proposed. If you don't have everything within the window, notify with what you have and follow up.

## Decision 2 - Notify the affected individuals?
Under **GDPR Art. 34**, tell the individuals **without undue delay** when the breach is likely to result in a **high risk** to their rights and freedoms - for example, exposure of Emirates ID, IBAN, passwords, or health data, where the practical risk is fraud or identity theft. You may be exempt if the data was, e.g., strongly encrypted/tokenised so it's unintelligible, or if you've since taken steps that remove the high risk.

Tell people in **plain language**: what happened, likely consequences, what you're doing, and what they can do to protect themselves.

## The clock starts at "aware"
The 72-hour GDPR clock runs from when you become **reasonably certain** a breach has occurred, not when you've finished investigating. So triage fast, and notify on partial information rather than missing the window.

## Why keep a register even for non-reportable breaches
GDPR Art. 33(5) requires documenting **all** breaches - facts, effects, and remedial action - regardless of whether they were reported. The register in the [template](breach-response-template.md) is that record, and it's exactly what an auditor asks to see.

## How this connects
- The **classification tier** of the affected data (from the [classification matrix](../data-classification/classification-matrix.md)) is the fastest signal of severity: a Restricted-tier breach (Emirates ID, IBAN) points toward "high risk → notify individuals."
- AI systems: the [AI-System Risk Checklist](../ai-system-risk-checklist/ai-risk-checklist.md) asks for an AI-specific incident path (harmful output, data leakage) that should feed into this same runbook.
