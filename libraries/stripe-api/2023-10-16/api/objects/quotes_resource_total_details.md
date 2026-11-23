# Stripe API 2023-10-16 — `quotes_resource_total_details` object

Expandable fields (pass `expand[]=<field>`): `breakdown`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount_discount` | integer | yes | This is the sum of all the discounts. |
| `amount_shipping` | integer |  | This is the sum of all the shipping amounts. |
| `amount_tax` | integer | yes | This is the sum of all the tax amounts. |
| `breakdown` | `quotes_resource_total_details_resource_breakdown` |  |  |

