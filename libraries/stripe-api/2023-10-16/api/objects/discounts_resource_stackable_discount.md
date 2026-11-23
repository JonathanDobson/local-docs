# Stripe API 2023-10-16 — `discounts_resource_stackable_discount` object

Expandable fields (pass `expand[]=<field>`): `coupon`, `discount`, `promotion_code`

| Field | Type | Required | Description |
|---|---|---|---|
| `coupon` | string or `coupon` |  | ID of the coupon to create a new discount for. |
| `discount` | string or `discount` |  | ID of an existing discount on the object (or one of its ancestors) to reuse. |
| `promotion_code` | string or `promotion_code` |  | ID of the promotion code to create a new discount for. |

