# Stripe API 2023-10-16 — `invoice_item_threshold_reason` object

| Field | Type | Required | Description |
|---|---|---|---|
| `line_item_ids` | array of string | yes | The IDs of the line items that triggered the threshold invoice. |
| `usage_gte` | integer | yes | The quantity threshold boundary that applied to the given line item. |

