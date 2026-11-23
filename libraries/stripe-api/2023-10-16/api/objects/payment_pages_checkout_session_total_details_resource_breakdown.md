# Stripe API 2023-10-16 — `payment_pages_checkout_session_total_details_resource_breakdown` object

Expandable fields (pass `expand[]=<field>`): `discounts`, `taxes`

| Field | Type | Required | Description |
|---|---|---|---|
| `discounts` | array of `line_items_discount_amount` | yes | The aggregated discounts. |
| `taxes` | array of `line_items_tax_amount` | yes | The aggregated tax amounts by rate. |

