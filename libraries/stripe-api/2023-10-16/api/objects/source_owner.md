# Stripe API 2023-10-16 — `source_owner` object

Expandable fields (pass `expand[]=<field>`): `address`, `verified_address`

| Field | Type | Required | Description |
|---|---|---|---|
| `address` | `address` |  | Owner's address. |
| `email` | string |  | Owner's email address. |
| `name` | string |  | Owner's full name. |
| `phone` | string |  | Owner's phone number (including extension). |
| `verified_address` | `address` |  | Verified owner's address. Verified values are verified or provided by the payment method directly (and if supported) at the time of authorization or settlement. They cannot be set or mutated. |
| `verified_email` | string |  | Verified owner's email address. Verified values are verified or provided by the payment method directly (and if supported) at the time of authorization or settlement. They cannot be set or mutated. |
| `verified_name` | string |  | Verified owner's full name. Verified values are verified or provided by the payment method directly (and if supported) at the time of authorization or settlement. They cannot be set or mutated. |
| `verified_phone` | string |  | Verified owner's phone number (including extension). Verified values are verified or provided by the payment method directly (and if supported) at the time of authorization or settlement. They cannot be set or mutated. |

