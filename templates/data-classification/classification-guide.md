# Field Guide - Running a Data Classification

How to use the [classification matrix](classification-matrix.md) in practice.

## Why classify

Classification is the single decision that drives the rest of your governance. Once a dataset is tagged Confidential or Restricted, its access model, encryption, retention, transfer rules, and whether it needs a DPIA all follow. Skipping it means making those decisions ad hoc, inconsistently, forever.

## The five-minute method

1. **Identify the data element or dataset.** Classify at the most useful granularity - usually a dataset, table, or field group, not individual values.
2. **Find the most sensitive element it contains.** A dataset inherits the tier of its most sensitive field. One IBAN column makes the whole export Restricted.
3. **Check the special-category and identifier list** in the matrix. Health, biometric, Emirates ID, IBAN, card data, auth secrets → Restricted by default.
4. **Assign the tier** and record it (in your data catalogue, the ROPA, or a simple register).
5. **Apply the controls** for that tier from the matrix and [handling rules](handling-rules.md).

## Common pitfalls

- **Over-classifying everything as Confidential.** If everything is sensitive, nothing is. Keep Internal as the genuine default for ordinary business data.
- **Classifying the container, not the contents.** A "general" SharePoint folder can hold Restricted data. Classify by what's inside.
- **Forgetting derived data.** An aggregate or model trained on Restricted data may still leak it. Re-classify outputs.
- **Static classification.** Re-classify when purpose or content changes. Note the review cadence `[e.g. annually, or on change]`.

## How this connects to the rest of the toolkit

- The **ROPA** records a *Classification tier* per processing activity - pulled straight from this exercise.
- The **DPIA** is typically triggered when Restricted / special-category data is processed at scale.
- The **AI-System Risk Checklist** asks what tier of data feeds the model - the answer comes from here.
