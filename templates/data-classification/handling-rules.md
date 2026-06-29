# Handling Rules by Tier

What each classification means in day-to-day practice. Adapt the `[bracketed]` specifics to your tooling and jurisdiction.

## Public

- **Storage:** any approved location.
- **Email / messaging:** no restriction.
- **Analytics / BI:** freely usable.
- **Sharing:** may be published externally.
- **Devices:** no restriction.

## Internal

- **Storage:** corporate systems only `[name your sanctioned platforms]`. No personal cloud drives.
- **Email / messaging:** internal recipients freely; external requires a business reason.
- **Analytics / BI:** usable across internal teams.
- **Sharing:** external sharing requires manager approval.
- **Devices:** managed devices preferred.

## Confidential

- **Storage:** access-controlled corporate systems only; encrypted at rest. No local copies on unmanaged devices.
- **Email / messaging:** encrypt or use a secure-share link, not attachments, where possible. Verify recipients.
- **Analytics / BI:** personal data should be minimised or pseudonymised before analysis. Restrict dashboards to authorised viewers.
- **Sharing:** external sharing requires a contract (e.g. DPA) and an appropriate transfer safeguard. Log the disclosure.
- **Devices:** managed, encrypted devices only.

## Restricted

- **Storage:** dedicated, access-logged systems with strong encryption. Tokenise or mask where the raw value isn't needed `[e.g. store IBAN/Emirates ID masked except last digits]`.
- **Email / messaging:** **do not** send raw Restricted data by email or chat. Use a controlled system with audit logging.
- **Analytics / BI:** never expose raw Restricted values in dashboards. Use masking, aggregation, or pseudonymisation. Access is allow-listed and logged.
- **Sharing:** prohibited unless explicitly authorised by `[role, e.g. DPO]`; assess PDPL/GDPR cross-border transfer rules before any export.
- **Devices:** hardened, managed devices only; no local persistence beyond what is strictly necessary.
- **Logging:** every access read/write is recorded in an immutable, reviewable log.

---

### Minimisation note

The strongest control is not collecting or retaining the data at all. Before applying a tier, ask whether the field is needed — the cheapest Restricted record to protect is the one you never stored. This links directly to the **necessity & proportionality** section of the DPIA template.
