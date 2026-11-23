# Stripe API 2023-10-16 — `shipping_rate_delivery_estimate` object

Expandable fields (pass `expand[]=<field>`): `maximum`, `minimum`

| Field | Type | Required | Description |
|---|---|---|---|
| `maximum` | `shipping_rate_delivery_estimate_bound` |  | The upper bound of the estimated range. If empty, represents no upper bound i.e., infinite. |
| `minimum` | `shipping_rate_delivery_estimate_bound` |  | The lower bound of the estimated range. If empty, represents no lower bound. |

