# Stripe API 2023-10-16 — `payment_pages_checkout_session_shipping_option` object

Expandable fields (pass `expand[]=<field>`): `shipping_rate`

| Field | Type | Required | Description |
|---|---|---|---|
| `shipping_amount` | integer | yes | A non-negative integer in cents representing how much to charge. |
| `shipping_rate` | string or `shipping_rate` | yes | The shipping rate. |

