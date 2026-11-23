# Stripe API 2023-10-16 — `payment_intent_processing` object

Expandable fields (pass `expand[]=<field>`): `card`

| Field | Type | Required | Description |
|---|---|---|---|
| `card` | `payment_intent_card_processing` |  |  |
| `type` | enum: `card` | yes | Type of the payment method for which payment is in `processing` state, one of `card`. |

