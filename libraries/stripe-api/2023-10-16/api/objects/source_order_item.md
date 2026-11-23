# Stripe API 2023-10-16 — `source_order_item` object

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer |  | The amount (price) for this order item. |
| `currency` | string |  | This currency of this order item. Required when `amount` is present. |
| `description` | string |  | Human-readable description for this order item. |
| `parent` | string |  | The ID of the associated object for this line item. Expandable if not null (e.g., expandable to a SKU). |
| `quantity` | integer |  | The quantity of this order item. When type is `sku`, this is the number of instances of the SKU to be ordered. |
| `type` | string |  | The type of this order item. Must be `sku`, `tax`, or `shipping`. |

