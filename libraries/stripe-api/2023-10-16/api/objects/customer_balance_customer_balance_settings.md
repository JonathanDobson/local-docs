# Stripe API 2023-10-16 — `customer_balance_customer_balance_settings` object

| Field | Type | Required | Description |
|---|---|---|---|
| `reconciliation_mode` | enum: `automatic`, `manual` | yes | The configuration for how funds that land in the customer cash balance are reconciled. |
| `using_merchant_default` | boolean | yes | A flag to indicate if reconciliation mode returned is the user's default or is specific to this customer cash balance |

