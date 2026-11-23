# Stripe API 2023-10-16 — `quotes_resource_recurring` object

Expandable fields (pass `expand[]=<field>`): `total_details`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount_subtotal` | integer | yes | Total before any discounts or taxes are applied. |
| `amount_total` | integer | yes | Total after discounts and taxes are applied. |
| `interval` | enum: `day`, `month`, `week`, `year` | yes | The frequency at which a subscription is billed. One of `day`, `week`, `month` or `year`. |
| `interval_count` | integer | yes | The number of intervals (specified in the `interval` attribute) between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months. |
| `total_details` | `quotes_resource_total_details` | yes |  |

