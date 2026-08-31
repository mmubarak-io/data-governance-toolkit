# Worked Example - Breach Response for "SoukNova"

> ⚠️ **Entirely fictional.** SoukNova is an invented e-commerce/fintech marketplace. The incident, people, timings, and identifiers below are synthetic and written to illustrate the decision path. Never use real breach records in a demo.

**Scenario:** a seller-support engineer at SoukNova exports a KYC reconciliation file to a cloud bucket to debug a payout mismatch, and the bucket is left readable to anyone with the link for four days. The file covers seller KYC data - Emirates ID and IBAN - which the [classification example](filled-classification-souknova.md) puts in the **Restricted** tier, and which [ROPA Activity 2](filled-ropa-souknova.md) records. Completed using the [breach response template](../templates/breach-response/breach-response-template.md); the notification calls follow the [guide](../templates/breach-response/breach-response-guide.md).

---

## Part A - Response playbook

### 1. Detect & log
| Field | Value |
|---|---|
| Incident ID | BR-2026-004 |
| Detected by / how | External researcher emailed `security@souknova.example`; confirmed by the platform team |
| Detected at | 2026-07-03 09:12 GST |
| Reported to incident lead at | 2026-07-03 09:40 GST |
| Short description | A KYC reconciliation export was written to a storage bucket with public-link read access enabled. Exposed from 2026-06-29 14:05 until containment. |

### 2. Triage & assess
| Field | Value |
|---|---|
| Data affected | Seller KYC records: legal name, Emirates ID number, IBAN, trade-licence number |
| Classification tier | **Restricted** |
| Special / sensitive data? | Yes - national identifier + financial credentials |
| Approx. number of individuals | 1,842 sellers |
| Cause | Misconfigured access on a debug export (public link read enabled; not a system compromise) |
| Still ongoing? | No - access revoked 2026-07-03 10:25 GST |
| **Risk to individuals** | **High** - the Emirates ID + IBAN combination is directly usable for identity fraud and payment redirection |

### 3. Contain & recover
| Action | Owner | Done? |
|---|---|---|
| Stop the leak (revoke access, isolate system, rotate keys) | Platform on-call (R. Haddad) | Yes - public access removed 10:25, bucket set private, signing keys rotated |
| Preserve evidence / logs | Security (T. Okonkwo) | Yes - access logs for the full exposure window exported to the case file |
| Assess scope (what else is exposed) | Platform + Data | Yes - one object; no other bucket had public access. 11 distinct external IPs read the object |
| Recover / restore | Data (L. Q., Head of Data) | Yes - export deleted; the debug workflow now runs against masked data only |

### 4. Notify
| Question | Answer |
|---|---|
| Notify the supervisory authority / Data Office? | **Yes** - Restricted-tier personal data was exposed to unidentified third parties, so a risk to individuals cannot be ruled out |
| Deadline | Without undue delay, and per GDPR within 72h of becoming aware - clock started 2026-07-03 09:12, so 2026-07-06 09:12 |
| Notified at | 2026-07-04 15:30 GST (UAE Data Office). Filed on partial information, with a follow-up on 2026-07-09 once the read-access analysis was complete |
| Notify affected individuals? (high risk to them) | **Yes** - Art. 34 high-risk threshold is met; the data was not encrypted or tokenised in the export, so no exemption applies |
| Individuals notified at | 2026-07-05, email to all 1,842 sellers plus an in-app notice: what happened, what was exposed, and to watch for payout-change requests and to verify any bank-detail change by calling support |
| Notify processors / partners / cyber-insurer? | Payments processor informed 2026-07-04 (payout-fraud watch on affected seller accounts); cyber-insurer notified 2026-07-04 |

### 5. Close & learn
| Field | Value |
|---|---|
| Root cause | Debug exports were permitted to write to a bucket where public-link access could be set by hand. No preventive control blocked Restricted data leaving the KYC store in the clear. |
| Corrective actions | 1. Public access blocked at the account level (Platform, done 2026-07-06). 2. KYC debug workflows read masked values only - Emirates ID and IBAN truncated to last 4 (Data, done 2026-07-14). 3. Alert on any bucket becoming publicly readable (Security, done 2026-07-10). 4. Restricted-tier handling refresher for the seller-support team (DPO, 2026-07-31). |
| Linked DPIA / ROPA updated? | ROPA Activity 2 security-measures field updated 2026-07-15. No DPIA was on file for seller KYC; one was opened as DPIA-2026-014. |
| Post-incident review date | 2026-07-17 (held; actions above signed off by the DPO) |

---

## Part B - Breach register

Kept for every breach, reportable or not - the register is itself the accountability record (GDPR Art. 33(5)).

| ID | Date | Data + tier | # people | Cause | Risk | Authority notified? | Individuals notified? | Status |
|---|---|---|---|---|---|---|---|---|
| BR-2026-002 | 2026-04-11 | Buyer delivery address, Confidential | 1 | Mis-sent email to wrong recipient | Low | N - recorded, risk judged low | N | Closed |
| BR-2026-003 | 2026-05-22 | Marketing contact list, Confidential | 240 | Vendor sub-processor incident | Low | N - vendor notified its own authority; risk to our subjects judged low | N | Closed |
| BR-2026-004 | 2026-07-03 | Seller KYC (Emirates ID, IBAN), **Restricted** | 1,842 | Misconfigured public access on a debug export | **High** | Y - 2026-07-04 | Y - 2026-07-05 | Closed 2026-07-17 |

Note the two low-risk rows. They were **not** reported, and recording the reasoning is exactly what makes the decision defensible later.

---

## Roles
| Role | Who | Contact |
|---|---|---|
| Incident lead | R. Haddad, Platform Engineering Lead | `platform-oncall@souknova.example` |
| DPO | Omar T. | `dpo@souknova.example` |
| Security | T. Okonkwo | `security@souknova.example` |
| Comms / legal | Nadia F., General Counsel | `legal@souknova.example` |

---

### What this example is meant to show

The classification tier did the heavy lifting. "Restricted" answered the severity question in seconds, which is what let the team file inside the 72-hour window on partial information rather than waiting for a complete forensic picture. The two unreported rows in the register matter just as much as the reported one: the record of *why you did not notify* is the part an auditor asks for.
