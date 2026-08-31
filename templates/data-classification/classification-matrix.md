# Data Classification Matrix

A four-tier classification scheme. Classification is the backbone of governance: it drives access, storage, retention, and the controls in every other template here. Classify the data **once**, and the ROPA, DPIA, and handling rules all inherit the answer.

> Replace the `[bracketed]` examples with your organisation's own. Keep the tier definitions stable - they should rarely change. **Not legal advice** - validate the tiers against the regulations that apply to you.

## The four tiers

| Tier | Definition | Typical examples | Who can access | Breach impact |
|---|---|---|---|---|
| **Public** | Approved for release to anyone; no harm if disclosed. | Marketing pages, published reports, open datasets. | Anyone. | None / negligible. |
| **Internal** | Not for public release; low harm if disclosed. Default tier for ordinary business data. | Internal memos, org charts, non-sensitive project docs. | All employees / contractors under NDA. | Low. |
| **Confidential** | Sensitive business or personal data; meaningful harm if disclosed. | Personal data (names, emails, phone), contracts, financials, non-special-category customer records. | Named teams / roles on a need-to-know basis. | Moderate to high (incl. regulatory exposure under PDPL/GDPR). |
| **Restricted** | Highest sensitivity; severe harm, legal, or regulatory consequences if disclosed. | Special-category / sensitive personal data, authentication secrets, **Emirates ID numbers, IBANs, full payment-card data, health data, biometrics**. | Strictly limited, explicitly authorised individuals; access logged. | Severe - regulatory penalties, fraud, individual harm. |

## Controls by tier

| Control | Public | Internal | Confidential | Restricted |
|---|---|---|---|---|
| **Encryption at rest** | Optional | Recommended | Required | Required (strong) |
| **Encryption in transit** | Recommended | Required | Required | Required |
| **Access model** | Open | Authenticated | Role-based, need-to-know | Explicit allow-list + approval |
| **Access logging** | No | Optional | Yes | Yes (immutable / audited) |
| **External sharing** | Allowed | Approval required | Contract + safeguard required | Prohibited unless explicitly authorised |
| **Cross-border transfer** | Allowed | Allowed | Allowed with safeguard (e.g. SCCs / adequacy) | Restricted; assess PDPL/GDPR transfer rules first |
| **Retention default** | As needed | `[e.g. 3 years]` | `[e.g. per purpose; see ROPA]` | `[minimum necessary; documented]` |
| **Disposal** | Standard | Standard | Secure deletion | Verified secure destruction |

## How special / sensitive data maps

Under **UAE PDPL** and **GDPR**, certain categories carry heightened obligations and should default to **Restricted** (or at least Confidential where a lower control set is justified and documented):

- **Special-category personal data** - health, biometric, genetic, racial/ethnic origin, religious belief, political opinion, criminal data → **Restricted**.
- **National / government identifiers** - Emirates ID, passport numbers → **Restricted**.
- **Financial credentials** - IBAN, full card numbers (PAN), CVV → **Restricted**.
- **Authentication secrets** - passwords, API keys, tokens → **Restricted** (and never store in plaintext).
- **Ordinary personal data** - name, email, phone, address → **Confidential** by default.

> See [`handling-rules.md`](handling-rules.md) for what each tier means in practice (email, analytics, storage locations), and the [field guide](classification-guide.md) for how to run a classification.
