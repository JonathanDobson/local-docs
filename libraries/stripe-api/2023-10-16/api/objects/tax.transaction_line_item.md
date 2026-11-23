# Stripe API 2023-10-16 — `tax.transaction_line_item` object

Expandable fields (pass `expand[]=<field>`): `reversal`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | The line item amount in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). If `tax_behavior=inclusive`, then this amount includes taxes. Otherwise, taxes were calculated on top of this amount. |
| `amount_tax` | integer | yes | The amount of tax calculated for this line item, in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `object` | enum: `tax.transaction_line_item` | yes | String representing the object's type. Objects of the same type share the same value. |
| `product` | string |  | The ID of an existing [Product](https://stripe.com/docs/api/products/object). |
| `quantity` | integer | yes | The number of units of the item being purchased. For reversals, this is the quantity reversed. |
| `reference` | string | yes | A custom identifier for this line item in the transaction. |
| `reversal` | `tax_product_resource_tax_transaction_line_item_resource_reversal` |  | If `type=reversal`, contains information about what was reversed. |
| `tax_behavior` | enum: `exclusive`, `inclusive` | yes | Specifies whether the `amount` includes taxes. If `tax_behavior=inclusive`, then the amount includes taxes. |
| `tax_code` | string | yes | The [tax code](https://stripe.com/docs/tax/tax-categories) ID used for this resource. |
| `type` | enum: `reversal`, `transaction` | yes | If `reversal`, this line item reverses an earlier transaction. |

