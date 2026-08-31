# Worked Example - Data Classification for "SoukNova"

> ⚠️ **Entirely fictional.** SoukNova is an invented e-commerce/fintech marketplace. All names, data, and details are synthetic.

**Scenario:** SoukNova classifies its main data assets once, then lets the [ROPA](filled-ropa-souknova.md), DPIA, and access controls inherit the tier. Completed using the [classification matrix](../templates/data-classification/classification-matrix.md) and [handling rules](../templates/data-classification/handling-rules.md).

## Classified data assets

| Data asset | Contains | Tier | Why |
|---|---|---|---|
| Public product catalogue | Listings, prices, seller shop names | **Public** | Meant for public release; no harm if disclosed. |
| Marketing site content | Blog posts, campaign pages | **Public** | Approved for release. |
| Internal runbooks & org charts | Ops docs, team structure | **Internal** | Not for public release; low harm. Default tier. |
| Buyer profile | Name, email, phone, delivery address, order history | **Confidential** | Ordinary personal data; meaningful harm if disclosed. |
| Support tickets | Message content (may reference orders/payments) | **Confidential** | Personal data; can contain financial detail (→ Restricted if it does). |
| **Seller KYC records** | Name, **Emirates ID**, trade licence | **Restricted** | National identifier; severe regulatory + fraud impact. |
| **Payout / payment credentials** | **IBAN**, full card data (PAN) | **Restricted** | Financial credentials; severe harm. |
| Authentication secrets | Passwords (hashed), API keys, tokens | **Restricted** | Never store in plaintext; severe impact if leaked. |
| Fraud/risk model features | Derived signals over buyers/sellers | **Confidential** | Derived personal data; re-classify outputs. |

## How the top tier is handled (Restricted)

Applying the [handling rules](../templates/data-classification/handling-rules.md) to SoukNova's Restricted assets:

- **Storage:** Emirates ID and IBAN are **tokenised** - the raw value is stored masked except the last digits; the token maps to the real value in a dedicated, access-logged vault.
- **Access:** an explicit allow-list (Payments & Compliance only); every read/write is written to an immutable log.
- **Email / chat:** raw Restricted values are never sent by email or Slack.
- **Analytics / BI:** dashboards show masked values only; the fraud model uses tokens, not raw IDs.
- **Cross-border:** any transfer of Restricted data is assessed against PDPL/GDPR transfer rules before it happens.

## The one decision that cascades

Because Seller KYC is classified **Restricted**, everything downstream inherits it automatically: the ROPA row for "Seller KYC & payouts" is Restricted, that row triggers **DPIA-2026-007**, and access is locked to the allow-list. Classify once; the rest follows.
