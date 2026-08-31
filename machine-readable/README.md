# Machine-readable governance

The templates in this repo are for people. These YAML files are the same policies for **machines** - so tooling can consume the classification tiers and the policy register instead of re-typing them.

## Files
- **`classification.yaml`** - the 4-tier classification scheme + the sensitive-data patterns (Emirates ID, IBAN, etc.) that force a minimum tier. The YAML twin of `templates/data-classification/classification-matrix.md`.
- **`policy-register.yaml`** - every policy mapped to the regulation it implements, the toolkit artefact that **documents** it, and the executable check that could **enforce** it.

## Why this exists (the one-two)
This repo is **policy as documents**. The companion repo [`ai-compliance-gates`](https://github.com/mmubarak-io/ai-compliance-gates) is **the same policy as executable code** - CI gates that block a pipeline when a rule is broken. The `policy_id`s here (POL-PRIV-001, POL-GOV-002, …) are shared with that repo on purpose: the register you read on paper and the gate that enforces it in CI use the same vocabulary.

Read the templates to understand a control; consume these YAML files to enforce it.

> Illustrative and synthetic. Not legal advice. Validate against the current regulations for your jurisdiction.
