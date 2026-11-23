# Stripe API 2023-10-16 — `payment_intent_next_action_boleto` object

| Field | Type | Required | Description |
|---|---|---|---|
| `expires_at` | timestamp (Unix seconds) |  | The timestamp after which the boleto expires. |
| `hosted_voucher_url` | string |  | The URL to the hosted boleto voucher page, which allows customers to view the boleto voucher. |
| `number` | string |  | The boleto number. |
| `pdf` | string |  | The URL to the downloadable boleto voucher PDF. |

