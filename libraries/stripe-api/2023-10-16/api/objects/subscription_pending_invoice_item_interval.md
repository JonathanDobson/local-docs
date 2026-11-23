# Stripe API 2023-10-16 — `subscription_pending_invoice_item_interval` object

| Field | Type | Required | Description |
|---|---|---|---|
| `interval` | enum: `day`, `month`, `week`, `year` | yes | Specifies invoicing frequency. Either `day`, `week`, `month` or `year`. |
| `interval_count` | integer | yes | The number of intervals between invoices. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of one year interval allowed (1 year, 12 months, or 52 weeks). |

