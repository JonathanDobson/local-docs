# Stripe API 2023-10-16 — `currency_option` object

Expandable fields (pass `expand[]=<field>`): `custom_unit_amount`, `tiers`

| Field | Type | Required | Description |
|---|---|---|---|
| `custom_unit_amount` | `custom_unit_amount` |  | When set, provides configuration for the amount to be adjusted by the customer during Checkout Sessions and Payment Links. |
| `tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  | Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed. |
| `tiers` | array of `price_tier` |  | Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`. |
| `unit_amount` | integer |  | The unit amount in cents (or local equivalent) to be charged, represented as a whole integer if possible. Only set if `billing_scheme=per_unit`. |
| `unit_amount_decimal` | string |  | The unit amount in cents (or local equivalent) to be charged, represented as a decimal string with at most 12 decimal places. Only set if `billing_scheme=per_unit`. |

