# Stripe API 2023-10-16 — `tax_product_resource_tax_breakdown` object

Expandable fields (pass `expand[]=<field>`): `tax_rate_details`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | The amount of tax, in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). |
| `inclusive` | boolean | yes | Specifies whether the tax amount is included in the line item amount. |
| `tax_rate_details` | `tax_product_resource_tax_rate_details` | yes |  |
| `taxability_reason` | enum: `customer_exempt`, `not_collecting`, `not_subject_to_tax`, `not_supported`, `portion_product_exempt`, `portion_reduced_rated`, `portion_standard_rated`, `product_exempt`, `product_exempt_holiday`, `proportionally_rated`, `reduced_rated`, `reverse_charge`, `standard_rated`, `taxable_basis_reduced`, `zero_rated` | yes | The reasoning behind this tax, for example, if the product is tax exempt. We might extend the possible values for this field to support new tax rules. |
| `taxable_amount` | integer | yes | The amount on which tax is calculated, in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). |

