# Stripe API 2023-10-16 — `payment_method_details_card_installments_plan` object

| Field | Type | Required | Description |
|---|---|---|---|
| `count` | integer |  | For `fixed_count` installment plans, this is the number of installment payments your customer will make to their credit card. |
| `interval` | enum: `month` |  | For `fixed_count` installment plans, this is the interval between installment payments your customer will make to their credit card. One of `month`. |
| `type` | enum: `fixed_count` | yes | Type of installment plan, one of `fixed_count`. |

