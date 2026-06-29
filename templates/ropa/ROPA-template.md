# ROPA — Record of Processing Activities

A Record of Processing Activities is the register of *what personal data you process, why, and under what safeguards*. It is required of controllers and processors under **GDPR Article 30** and is the central evidence artefact regulators ask for first. The UAE PDPL's accountability obligations expect an equivalent record.

Maintain one **row per processing activity** (e.g. "customer onboarding", "marketing emails", "payroll"). The register works best as a spreadsheet — an `.xlsx` version ships alongside this file — but the field definitions below are the source of truth.

> Fill the `[bracketed]` fields. Pull the **Classification tier** straight from the [Data Classification Matrix](../data-classification/classification-matrix.md).

## Register header (record once)

| Field | Value |
|---|---|
| Organisation (controller) | `[legal entity name]` |
| Controller contact / representative | `[name, role, email]` |
| Data Protection Officer (if appointed) | `[name, email]` |
| Date of last review | `[YYYY-MM-DD]` |
| Review cadence | `[e.g. annually or on material change]` |

## Processing-activity fields (one row each)

| # | Field | What goes here |
|---|---|---|
| 1 | **Activity name** | Short, recognisable name of the processing. |
| 2 | **Business owner** | Team/role accountable for this activity. |
| 3 | **Purpose** | Why the data is processed — be specific (not "business purposes"). |
| 4 | **Lawful basis** | GDPR Art. 6 basis (consent / contract / legal obligation / vital interests / public task / legitimate interests) and the PDPL equivalent. For special-category data, also the Art. 9 condition. |
| 5 | **Data-subject categories** | Whose data — customers, employees, prospects, minors, etc. |
| 6 | **Personal-data categories** | What data — name, email, IBAN, location, etc. |
| 7 | **Special / sensitive flag** | Yes/No — health, biometric, Emirates ID, financial credentials, etc. Drives classification and DPIA need. |
| 8 | **Classification tier** | Public / Internal / Confidential / Restricted — from the classification matrix. |
| 9 | **Source of data** | Collected from the individual, generated internally, or obtained from a third party (name it). |
| 10 | **Recipients / third parties** | Who receives the data — internal teams, processors, vendors. Name processors. |
| 11 | **Cross-border transfers** | Destination country + safeguard (adequacy / SCCs / explicit consent / PDPL transfer condition). "None" if data stays in-region. |
| 12 | **Retention period** | How long, and the trigger for deletion. Avoid "indefinite". |
| 13 | **Security measures** | Encryption, access control, pseudonymisation, logging — summarise. |
| 14 | **Linked DPIA?** | Reference to a DPIA if one was required for this activity. |
| 15 | **Last reviewed** | `[YYYY-MM-DD]` for this row. |

## Blank row template (copy per activity)

```
Activity name      :
Business owner     :
Purpose            :
Lawful basis       :
Data-subject cats  :
Personal-data cats :
Special/sensitive  : [Yes/No — which]
Classification tier: [Public/Internal/Confidential/Restricted]
Source of data     :
Recipients/3rd pty :
Cross-border       : [country + safeguard, or None]
Retention          :
Security measures  :
Linked DPIA?       : [ref or N/A]
Last reviewed      :
```

> See the [field guide](ROPA-guide.md) for how to fill each field and a worked, fully synthetic example in [`examples/filled-ropa-souknova.md`](../../examples/filled-ropa-souknova.md).
