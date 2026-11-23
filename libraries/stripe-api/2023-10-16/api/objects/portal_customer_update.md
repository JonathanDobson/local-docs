# Stripe API 2023-10-16 — `portal_customer_update` object

| Field | Type | Required | Description |
|---|---|---|---|
| `allowed_updates` | array of enum: `address`, `email`, `name`, `phone`, `shipping`, `tax_id` | yes | The types of customer updates that are supported. When empty, customers are not updateable. |
| `enabled` | boolean | yes | Whether the feature is enabled. |

