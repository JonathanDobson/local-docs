# Stripe API 2023-10-16 — `gelato_selfie_report` object

Result from a selfie check

Expandable fields (pass `expand[]=<field>`): `error`

| Field | Type | Required | Description |
|---|---|---|---|
| `document` | string |  | ID of the [File](https://stripe.com/docs/api/files) holding the image of the identity document used in this check. |
| `error` | `gelato_selfie_report_error` |  | Details on the verification error. Present when status is `unverified`. |
| `selfie` | string |  | ID of the [File](https://stripe.com/docs/api/files) holding the image of the selfie used in this check. |
| `status` | enum: `unverified`, `verified` | yes | Status of this `selfie` check. |

