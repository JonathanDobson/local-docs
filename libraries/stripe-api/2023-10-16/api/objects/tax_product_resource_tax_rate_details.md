# Stripe API 2023-10-16 — `tax_product_resource_tax_rate_details` object

| Field | Type | Required | Description |
|---|---|---|---|
| `country` | string |  | Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)). |
| `percentage_decimal` | string | yes | The tax rate percentage as a string. For example, 8.5% is represented as `"8.5"`. |
| `state` | string |  | State, county, province, or region. |
| `tax_type` | enum: `amusement_tax`, `communications_tax`, `gst`, `hst`, `igst`, `jct`, `lease_tax`, `pst`, `qst`, `rst`, `sales_tax`, `vat` |  | The tax type, such as `vat` or `sales_tax`. |

