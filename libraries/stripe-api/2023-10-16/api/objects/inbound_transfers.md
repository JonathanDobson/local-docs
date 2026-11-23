# Stripe API 2023-10-16 — `inbound_transfers` object

Expandable fields (pass `expand[]=<field>`): `billing_details`, `us_bank_account`

| Field | Type | Required | Description |
|---|---|---|---|
| `billing_details` | `treasury_shared_resource_billing_details` | yes |  |
| `type` | enum: `us_bank_account` | yes | The type of the payment method used in the InboundTransfer. |
| `us_bank_account` | `inbound_transfers_payment_method_details_us_bank_account` |  |  |

