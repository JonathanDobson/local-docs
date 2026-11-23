# Stripe API 2023-10-16 — `payment_method_card_generated_card` object

Expandable fields (pass `expand[]=<field>`): `payment_method_details`, `setup_attempt`

| Field | Type | Required | Description |
|---|---|---|---|
| `charge` | string |  | The charge that created this object. |
| `payment_method_details` | `card_generated_from_payment_method_details` |  | Transaction-specific details of the payment method used in the payment. |
| `setup_attempt` | string or `setup_attempt` |  | The ID of the SetupAttempt that generated this PaymentMethod, if any. |

