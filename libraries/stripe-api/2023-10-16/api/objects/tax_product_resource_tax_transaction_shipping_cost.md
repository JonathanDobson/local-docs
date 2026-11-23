# Stripe API 2023-10-16 — `tax_product_resource_tax_transaction_shipping_cost` object

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | The shipping amount in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). If `tax_behavior=inclusive`, then this amount includes taxes. Otherwise, taxes were calculated on top of this amount. |
| `amount_tax` | integer | yes | The amount of tax calculated for shipping, in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). |
| `shipping_rate` | string |  | The ID of an existing [ShippingRate](https://stripe.com/docs/api/shipping_rates/object). |
| `tax_behavior` | enum: `exclusive`, `inclusive` | yes | Specifies whether the `amount` includes taxes. If `tax_behavior=inclusive`, then the amount includes taxes. |
| `tax_code` | string | yes | The [tax code](https://stripe.com/docs/tax/tax-categories) ID used for shipping. |

