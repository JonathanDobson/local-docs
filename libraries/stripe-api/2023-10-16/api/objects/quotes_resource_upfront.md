# Stripe API 2023-10-16 — `quotes_resource_upfront` object

Expandable fields (pass `expand[]=<field>`): `line_items`, `total_details`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount_subtotal` | integer | yes | Total before any discounts or taxes are applied. |
| `amount_total` | integer | yes | Total after discounts and taxes are applied. |
| `line_items` | object |  | The line items that will appear on the next invoice after this quote is accepted. This does not include pending invoice items that exist on the customer but may still be included in the next invoice. |
| `total_details` | `quotes_resource_total_details` | yes |  |

