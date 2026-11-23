# Stripe API 2023-10-16 — `tax_product_resource_line_item_tax_breakdown` object

Expandable fields (pass `expand[]=<field>`): `jurisdiction`, `tax_rate_details`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | The amount of tax, in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). |
| `jurisdiction` | `tax_product_resource_jurisdiction` | yes |  |
| `sourcing` | enum: `destination`, `origin` | yes | Indicates whether the jurisdiction was determined by the origin (merchant's address) or destination (customer's address). |
| `tax_rate_details` | `tax_product_resource_line_item_tax_rate_details` |  | Details regarding the rate for this tax. This field will be `null` when the tax is not imposed, for example if the product is exempt from tax. |
| `taxability_reason` | enum: `customer_exempt`, `not_collecting`, `not_subject_to_tax`, `not_supported`, `portion_product_exempt`, `portion_reduced_rated`, `portion_standard_rated`, `product_exempt`, `product_exempt_holiday`, `proportionally_rated`, `reduced_rated`, `reverse_charge`, `standard_rated`, `taxable_basis_reduced`, `zero_rated` | yes | The reasoning behind this tax, for example, if the product is tax exempt. The possible values for this field may be extended as new tax rules are supported. |
| `taxable_amount` | integer | yes | The amount on which tax is calculated, in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). |

