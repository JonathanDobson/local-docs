# Stripe API 2023-10-16 — `gelato_phone_report` object

Result from a phone check

Expandable fields (pass `expand[]=<field>`): `error`

| Field | Type | Required | Description |
|---|---|---|---|
| `error` | `gelato_phone_report_error` |  | Details on the verification error. Present when status is `unverified`. |
| `phone` | string |  | Phone to be verified. |
| `status` | enum: `unverified`, `verified` | yes | Status of this `phone` check. |

