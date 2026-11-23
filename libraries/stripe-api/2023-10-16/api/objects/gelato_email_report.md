# Stripe API 2023-10-16 — `gelato_email_report` object

Result from a email check

Expandable fields (pass `expand[]=<field>`): `error`

| Field | Type | Required | Description |
|---|---|---|---|
| `email` | string |  | Email to be verified. |
| `error` | `gelato_email_report_error` |  | Details on the verification error. Present when status is `unverified`. |
| `status` | enum: `unverified`, `verified` | yes | Status of this `email` check. |

