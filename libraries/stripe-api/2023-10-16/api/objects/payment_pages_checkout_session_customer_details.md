# Stripe API 2023-10-16 — `payment_pages_checkout_session_customer_details` object

Expandable fields (pass `expand[]=<field>`): `address`, `tax_ids`

| Field | Type | Required | Description |
|---|---|---|---|
| `address` | `address` |  | The customer's address after a completed Checkout Session. Note: This property is populated only for sessions on or after March 30, 2022. |
| `email` | string |  | The email associated with the Customer, if one exists, on the Checkout Session after a completed Checkout Session or at time of session expiry. Otherwise, if the customer has consented to promotional content, this value is the most recent valid email provided by the customer on the Checkout form. |
| `name` | string |  | The customer's name after a completed Checkout Session. Note: This property is populated only for sessions on or after March 30, 2022. |
| `phone` | string |  | The customer's phone number after a completed Checkout Session. |
| `tax_exempt` | enum: `exempt`, `none`, `reverse` |  | The customer’s tax exempt status after a completed Checkout Session. |
| `tax_ids` | array of `payment_pages_checkout_session_tax_id` |  | The customer’s tax IDs after a completed Checkout Session. |

