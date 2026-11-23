# Stripe API 2023-10-16 — `mandate_acss_debit` object

| Field | Type | Required | Description |
|---|---|---|---|
| `default_for` | array of enum: `invoice`, `subscription` |  | List of Stripe products where this mandate can be selected automatically. |
| `interval_description` | string |  | Description of the interval. Only required if the 'payment_schedule' parameter is 'interval' or 'combined'. |
| `payment_schedule` | enum: `combined`, `interval`, `sporadic` | yes | Payment schedule for the mandate. |
| `transaction_type` | enum: `business`, `personal` | yes | Transaction type of the mandate. |

