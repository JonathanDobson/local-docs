# Stripe API 2023-10-16 — `customer_acceptance` object

Expandable fields (pass `expand[]=<field>`): `offline`, `online`

| Field | Type | Required | Description |
|---|---|---|---|
| `accepted_at` | timestamp (Unix seconds) |  | The time that the customer accepts the mandate. |
| `offline` | `offline_acceptance` |  |  |
| `online` | `online_acceptance` |  |  |
| `type` | enum: `offline`, `online` | yes | The mandate includes the type of customer acceptance information, such as: `online` or `offline`. |

