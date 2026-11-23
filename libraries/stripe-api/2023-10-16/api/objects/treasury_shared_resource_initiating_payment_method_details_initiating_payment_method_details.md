# Stripe API 2023-10-16 — `treasury_shared_resource_initiating_payment_method_details_initiating_payment_method_details` object

Expandable fields (pass `expand[]=<field>`): `billing_details`, `financial_account`, `us_bank_account`

| Field | Type | Required | Description |
|---|---|---|---|
| `balance` | enum: `payments` |  | Set when `type` is `balance`. |
| `billing_details` | `treasury_shared_resource_billing_details` | yes |  |
| `financial_account` | `received_payment_method_details_financial_account` |  |  |
| `issuing_card` | string |  | Set when `type` is `issuing_card`. This is an [Issuing Card](https://stripe.com/docs/api#issuing_cards) ID. |
| `type` | enum: `balance`, `financial_account`, `issuing_card`, `stripe`, `us_bank_account` | yes | Polymorphic type matching the originating money movement's source. This can be an external account, a Stripe balance, or a FinancialAccount. |
| `us_bank_account` | `treasury_shared_resource_initiating_payment_method_details_us_bank_account` |  |  |

