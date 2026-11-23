# Stripe API 2023-10-16 — `payment_method_card_wallet_masterpass` object

Expandable fields (pass `expand[]=<field>`): `billing_address`, `shipping_address`

| Field | Type | Required | Description |
|---|---|---|---|
| `billing_address` | `address` |  | Owner's verified billing address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated. |
| `email` | string |  | Owner's verified email. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated. |
| `name` | string |  | Owner's verified full name. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated. |
| `shipping_address` | `address` |  | Owner's verified shipping address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated. |

