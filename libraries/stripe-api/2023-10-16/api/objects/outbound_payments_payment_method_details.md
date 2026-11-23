# Stripe API 2023-10-16 — `outbound_payments_payment_method_details` object

Expandable fields (pass `expand[]=<field>`): `billing_details`, `financial_account`, `us_bank_account`

| Field | Type | Required | Description |
|---|---|---|---|
| `billing_details` | `treasury_shared_resource_billing_details` | yes |  |
| `financial_account` | `outbound_payments_payment_method_details_financial_account` |  |  |
| `type` | enum: `financial_account`, `us_bank_account` | yes | The type of the payment method used in the OutboundPayment. |
| `us_bank_account` | `outbound_payments_payment_method_details_us_bank_account` |  |  |

