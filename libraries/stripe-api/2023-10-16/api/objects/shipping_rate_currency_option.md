# Stripe API 2023-10-16 — `shipping_rate_currency_option` object

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | A non-negative integer in cents representing how much to charge. |
| `tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` | yes | Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. |

