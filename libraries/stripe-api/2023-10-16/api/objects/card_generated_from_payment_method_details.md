# Stripe API 2023-10-16 — `card_generated_from_payment_method_details` object

Expandable fields (pass `expand[]=<field>`): `card_present`

| Field | Type | Required | Description |
|---|---|---|---|
| `card_present` | `payment_method_details_card_present` |  |  |
| `type` | string | yes | The type of payment method transaction-specific details from the transaction that generated this `card` payment method. Always `card_present`. |

