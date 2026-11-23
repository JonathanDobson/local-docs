# Stripe API 2023-10-16 — `customer_tax_location` object

| Field | Type | Required | Description |
|---|---|---|---|
| `country` | string | yes | The customer's country as identified by Stripe Tax. |
| `source` | enum: `billing_address`, `ip_address`, `payment_method`, `shipping_destination` | yes | The data source used to infer the customer's location. |
| `state` | string |  | The customer's state, county, province, or region as identified by Stripe Tax. |

