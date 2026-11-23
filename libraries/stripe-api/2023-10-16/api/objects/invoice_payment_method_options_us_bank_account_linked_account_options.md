# Stripe API 2023-10-16 — `invoice_payment_method_options_us_bank_account_linked_account_options` object

| Field | Type | Required | Description |
|---|---|---|---|
| `permissions` | array of enum: `balances`, `payment_method`, `transactions` |  | The list of permissions to request. The `payment_method` permission must be included. |
| `prefetch` | array of enum: `balances`, `transactions` |  | Data features requested to be retrieved upon account creation. |

