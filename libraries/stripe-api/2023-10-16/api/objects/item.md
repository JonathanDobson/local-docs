# Stripe API 2023-10-16 — `item` object

A line item.

Expandable fields (pass `expand[]=<field>`): `discounts`, `price`, `taxes`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount_discount` | integer | yes | Total discount amount applied. If no discounts were applied, defaults to 0. |
| `amount_subtotal` | integer | yes | Total before any discounts or taxes are applied. |
| `amount_tax` | integer | yes | Total tax amount applied. If no tax was applied, defaults to 0. |
| `amount_total` | integer | yes | Total after discounts and taxes. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `description` | string | yes | An arbitrary string attached to the object. Often useful for displaying to users. Defaults to product name. |
| `discounts` | array of `line_items_discount_amount` |  | The discounts applied to the line item. |
| `id` | string | yes | Unique identifier for the object. |
| `object` | enum: `item` | yes | String representing the object's type. Objects of the same type share the same value. |
| `price` | `price` |  | The price used to generate the line item. |
| `quantity` | integer |  | The quantity of products being purchased. |
| `taxes` | array of `line_items_tax_amount` |  | The taxes applied to the line item. |

