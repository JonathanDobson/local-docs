# Stripe API 2023-10-16 — `invoices_resource_shipping_cost` object

Expandable fields (pass `expand[]=<field>`): `shipping_rate`, `taxes`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount_subtotal` | integer | yes | Total shipping cost before any taxes are applied. |
| `amount_tax` | integer | yes | Total tax amount applied due to shipping costs. If no tax was applied, defaults to 0. |
| `amount_total` | integer | yes | Total shipping cost after taxes are applied. |
| `shipping_rate` | string or `shipping_rate` |  | The ID of the ShippingRate for this invoice. |
| `taxes` | array of `line_items_tax_amount` |  | The taxes applied to the shipping rate. |

