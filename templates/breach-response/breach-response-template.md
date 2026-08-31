# Data Breach Response - Template & Register

A personal-data breach is discovered on your worst day, not your calendar's. This template is the playbook you fill in *before* one happens: how to triage, contain, decide whether you must notify, and record the whole thing. It maps to **GDPR Art. 33/34** (notification to the supervisory authority and to data subjects) and the **UAE PDPL** breach-notification duty to the UAE Data Office.

> Fill the `[bracketed]` fields when adopting this, and again per incident. Pull the **classification tier** of affected data from the [classification matrix](../data-classification/classification-matrix.md). See the [guide](breach-response-guide.md) for the notification decision and timelines. **Not legal advice** - confirm the exact triggers and deadlines that apply to you with counsel.

---

## Part A - Response playbook (per incident)

### 1. Detect & log
| Field | Value |
|---|---|
| Incident ID | `[BR-YYYY-NNN]` |
| Detected by / how | `[name / alert / report]` |
| Detected at | `[YYYY-MM-DD HH:MM TZ]` |
| Reported to incident lead at | `[time]` |
| Short description | `[what appears to have happened]` |

### 2. Triage & assess
| Field | Value |
|---|---|
| Data affected | `[categories, e.g. buyer profiles]` |
| Classification tier | `[Public / Internal / Confidential / Restricted]` |
| Special / sensitive data? | `[Yes/No - Emirates ID, IBAN, health, etc.]` |
| Approx. number of individuals | `[count or estimate]` |
| Cause | `[e.g. misconfigured access, lost device, phishing, vendor breach]` |
| Still ongoing? | `[Yes/No]` |
| **Risk to individuals** | `[Low / High - drives whether you must notify individuals]` |

### 3. Contain & recover
| Action | Owner | Done? |
|---|---|---|
| Stop the leak (revoke access, isolate system, rotate keys) | `[ ]` | `[ ]` |
| Preserve evidence / logs | `[ ]` | `[ ]` |
| Assess scope (what else is exposed) | `[ ]` | `[ ]` |
| Recover / restore | `[ ]` | `[ ]` |

### 4. Notify (see the guide for the decision + clock)
| Question | Answer |
|---|---|
| Notify the supervisory authority / Data Office? | `[Yes/No + why]` |
| Deadline | `[e.g. without undue delay, and per GDPR within 72h of becoming aware]` |
| Notified at | `[time]` |
| Notify affected individuals? (high risk to them) | `[Yes/No + why]` |
| Individuals notified at | `[time / method]` |
| Notify processors / partners / cyber-insurer? | `[ ]` |

### 5. Close & learn
| Field | Value |
|---|---|
| Root cause | `[ ]` |
| Corrective actions | `[control changes, with owners + dates]` |
| Linked DPIA / ROPA updated? | `[ref]` |
| Post-incident review date | `[YYYY-MM-DD]` |

---

## Part B - Breach register (one row per incident)

Keep this even for breaches you decide *not* to report - the register itself is evidence of accountability (GDPR Art. 33(5)).

| ID | Date | Data + tier | # people | Cause | Risk | Authority notified? | Individuals notified? | Status |
|---|---|---|---|---|---|---|---|---|
| `[BR-2026-001]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` | `[Low/High]` | `[Y/N + date]` | `[Y/N + date]` | `[Open/Closed]` |

---

## Roles (fill once)
| Role | Who | Contact |
|---|---|---|
| Incident lead | `[ ]` | `[ ]` |
| DPO | `[ ]` | `[ ]` |
| Security | `[ ]` | `[ ]` |
| Comms / legal | `[ ]` | `[ ]` |
