# Stripe API 2023-10-16 — `payment_method_options_card_installments` object

Expandable fields (pass `expand[]=<field>`): `available_plans`, `plan`

| Field | Type | Required | Description |
|---|---|---|---|
| `available_plans` | array of `payment_method_details_card_installments_plan` |  | Installment plans that may be selected for this PaymentIntent. |
| `enabled` | boolean | yes | Whether Installments are enabled for this PaymentIntent. |
| `plan` | `payment_method_details_card_installments_plan` |  | Installment plan selected for this PaymentIntent. |

