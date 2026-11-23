# Stripe API 2023-10-16 — `deleted_card` object

| Field | Type | Required | Description |
|---|---|---|---|
| `currency` | string |  | Three-letter [ISO code for the currency](https://stripe.com/docs/payouts) paid out to the bank account. |
| `deleted` | enum: `True` | yes | Always true for a deleted object |
| `id` | string | yes | Unique identifier for the object. |
| `object` | enum: `card` | yes | String representing the object's type. Objects of the same type share the same value. |

