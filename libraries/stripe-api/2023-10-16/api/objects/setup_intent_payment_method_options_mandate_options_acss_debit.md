# Stripe API 2023-10-16 — `setup_intent_payment_method_options_mandate_options_acss_debit` object

| Field | Type | Required | Description |
|---|---|---|---|
| `custom_mandate_url` | string |  | A URL for custom mandate text |
| `default_for` | array of enum: `invoice`, `subscription` |  | List of Stripe products where this mandate can be selected automatically. |
| `interval_description` | string |  | Description of the interval. Only required if the 'payment_schedule' parameter is 'interval' or 'combined'. |
| `payment_schedule` | enum: `combined`, `interval`, `sporadic` |  | Payment schedule for the mandate. |
| `transaction_type` | enum: `business`, `personal` |  | Transaction type of the mandate. |

