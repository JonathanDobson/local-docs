# Stripe API 2023-10-16 — `tax_id_verification` object

| Field | Type | Required | Description |
|---|---|---|---|
| `status` | enum: `pending`, `unavailable`, `unverified`, `verified` | yes | Verification status, one of `pending`, `verified`, `unverified`, or `unavailable`. |
| `verified_address` | string |  | Verified address. |
| `verified_name` | string |  | Verified name. |

