# Stripe API 2023-10-16 — `payment_intent_payment_method_options_mandate_options_acss_debit` object

| Field | Type | Required | Description |
|---|---|---|---|
| `custom_mandate_url` | string |  | A URL for custom mandate text |
| `interval_description` | string |  | Description of the interval. Only required if the 'payment_schedule' parameter is 'interval' or 'combined'. |
| `payment_schedule` | enum: `combined`, `interval`, `sporadic` |  | Payment schedule for the mandate. |
| `transaction_type` | enum: `business`, `personal` |  | Transaction type of the mandate. |

