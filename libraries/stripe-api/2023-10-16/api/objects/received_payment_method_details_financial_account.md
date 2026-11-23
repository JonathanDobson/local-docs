# Stripe API 2023-10-16 — `received_payment_method_details_financial_account` object

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | yes | The FinancialAccount ID. |
| `network` | enum: `stripe` | yes | The rails the ReceivedCredit was sent over. A FinancialAccount can only send funds over `stripe`. |

