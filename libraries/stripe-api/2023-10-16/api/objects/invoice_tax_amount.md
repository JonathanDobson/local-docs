# Stripe API 2023-10-16 — `invoice_tax_amount` object

Expandable fields (pass `expand[]=<field>`): `tax_rate`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | The amount, in cents (or local equivalent), of the tax. |
| `inclusive` | boolean | yes | Whether this tax amount is inclusive or exclusive. |
| `tax_rate` | string or `tax_rate` | yes | The tax rate that was applied to get this tax amount. |
| `taxability_reason` | enum: `customer_exempt`, `not_collecting`, `not_subject_to_tax`, `not_supported`, `portion_product_exempt`, `portion_reduced_rated`, `portion_standard_rated`, `product_exempt`, `product_exempt_holiday`, `proportionally_rated`, `reduced_rated`, `reverse_charge`, `standard_rated`, `taxable_basis_reduced`, `zero_rated` |  | The reasoning behind this tax, for example, if the product is tax exempt. The possible values for this field may be extended as new tax rules are supported. |
| `taxable_amount` | integer |  | The amount on which tax is calculated, in cents (or local equivalent). |

