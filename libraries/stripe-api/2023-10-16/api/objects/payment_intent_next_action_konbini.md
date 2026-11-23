# Stripe API 2023-10-16 — `payment_intent_next_action_konbini` object

Expandable fields (pass `expand[]=<field>`): `stores`

| Field | Type | Required | Description |
|---|---|---|---|
| `expires_at` | timestamp (Unix seconds) | yes | The timestamp at which the pending Konbini payment expires. |
| `hosted_voucher_url` | string |  | The URL for the Konbini payment instructions page, which allows customers to view and print a Konbini voucher. |
| `stores` | `payment_intent_next_action_konbini_stores` | yes |  |

