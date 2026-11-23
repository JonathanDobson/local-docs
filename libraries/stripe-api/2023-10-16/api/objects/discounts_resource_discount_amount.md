# Stripe API 2023-10-16 — `discounts_resource_discount_amount` object

Expandable fields (pass `expand[]=<field>`): `discount`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | The amount, in cents (or local equivalent), of the discount. |
| `discount` | string or `discount` or `deleted_discount` | yes | The discount that was applied to get this discount amount. |

