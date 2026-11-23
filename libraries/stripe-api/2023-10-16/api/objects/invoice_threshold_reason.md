# Stripe API 2023-10-16 — `invoice_threshold_reason` object

Expandable fields (pass `expand[]=<field>`): `item_reasons`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount_gte` | integer |  | The total invoice amount threshold boundary if it triggered the threshold invoice. |
| `item_reasons` | array of `invoice_item_threshold_reason` | yes | Indicates which line items triggered a threshold invoice. |

