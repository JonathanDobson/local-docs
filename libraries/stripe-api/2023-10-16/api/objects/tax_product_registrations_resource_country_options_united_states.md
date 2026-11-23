# Stripe API 2023-10-16 — `tax_product_registrations_resource_country_options_united_states` object

Expandable fields (pass `expand[]=<field>`): `local_amusement_tax`, `local_lease_tax`

| Field | Type | Required | Description |
|---|---|---|---|
| `local_amusement_tax` | `tax_product_registrations_resource_country_options_us_local_amusement_tax` |  |  |
| `local_lease_tax` | `tax_product_registrations_resource_country_options_us_local_lease_tax` |  |  |
| `state` | string | yes | Two-letter US state code ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)). |
| `type` | enum: `local_amusement_tax`, `local_lease_tax`, `state_communications_tax`, `state_sales_tax` | yes | Type of registration in the US. |

