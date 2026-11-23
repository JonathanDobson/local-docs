# Stripe API 2023-10-16 — `credit_note_line_item` object

The credit note line item object

Expandable fields (pass `expand[]=<field>`): `discount_amounts`, `tax_amounts`, `tax_rates`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | The integer amount in cents (or local equivalent) representing the gross amount being credited for this line item, excluding (exclusive) tax and discounts. |
| `amount_excluding_tax` | integer |  | The integer amount in cents (or local equivalent) representing the amount being credited for this line item, excluding all tax and discounts. |
| `description` | string |  | Description of the item being credited. |
| `discount_amount` | integer | yes | The integer amount in cents (or local equivalent) representing the discount being credited for this line item. |
| `discount_amounts` | array of `discounts_resource_discount_amount` | yes | The amount of discount calculated per discount for this line item |
| `id` | string | yes | Unique identifier for the object. |
| `invoice_line_item` | string |  | ID of the invoice line item being credited |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `object` | enum: `credit_note_line_item` | yes | String representing the object's type. Objects of the same type share the same value. |
| `quantity` | integer |  | The number of units of product being credited. |
| `tax_amounts` | array of `credit_note_tax_amount` | yes | The amount of tax calculated per tax rate for this line item |
| `tax_rates` | array of `tax_rate` | yes | The tax rates which apply to the line item. |
| `type` | enum: `custom_line_item`, `invoice_line_item` | yes | The type of the credit note line item, one of `invoice_line_item` or `custom_line_item`. When the type is `invoice_line_item` there is an additional `invoice_line_item` property on the resource the value of which is the id of the credited line item on the invoice. |
| `unit_amount` | integer |  | The cost of each unit of product being credited. |
| `unit_amount_decimal` | string |  | Same as `unit_amount`, but contains a decimal value with at most 12 decimal places. |
| `unit_amount_excluding_tax` | string |  | The amount in cents (or local equivalent) representing the unit amount being credited for this line item, excluding all tax and discounts. |

