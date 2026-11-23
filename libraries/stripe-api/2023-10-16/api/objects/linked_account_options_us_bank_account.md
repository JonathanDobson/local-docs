# Stripe API 2023-10-16 — `linked_account_options_us_bank_account` object

| Field | Type | Required | Description |
|---|---|---|---|
| `permissions` | array of enum: `balances`, `ownership`, `payment_method`, `transactions` |  | The list of permissions to request. The `payment_method` permission must be included. |
| `prefetch` | array of enum: `balances`, `transactions` |  | Data features requested to be retrieved upon account creation. |
| `return_url` | string |  | For webview integrations only. Upon completing OAuth login in the native browser, the user will be redirected to this URL to return to your app. |

