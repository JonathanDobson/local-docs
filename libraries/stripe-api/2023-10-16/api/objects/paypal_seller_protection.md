# Stripe API 2023-10-16 — `paypal_seller_protection` object

| Field | Type | Required | Description |
|---|---|---|---|
| `dispute_categories` | array of enum: `fraudulent`, `product_not_received` |  | An array of conditions that are covered for the transaction, if applicable. |
| `status` | enum: `eligible`, `not_eligible`, `partially_eligible` | yes | Indicates whether the transaction is eligible for PayPal's seller protection. |

