# Stripe API 2023-10-16 — `payment_method_paypal` object

| Field | Type | Required | Description |
|---|---|---|---|
| `payer_email` | string |  | Owner's email. Values are provided by PayPal directly (if supported) at the time of authorization or settlement. They cannot be set or mutated. |
| `payer_id` | string |  | PayPal account PayerID. This identifier uniquely identifies the PayPal customer. |

