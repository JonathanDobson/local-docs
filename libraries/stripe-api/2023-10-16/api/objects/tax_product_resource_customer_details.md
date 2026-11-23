# Stripe API 2023-10-16 — `tax_product_resource_customer_details` object

Expandable fields (pass `expand[]=<field>`): `address`, `tax_ids`

| Field | Type | Required | Description |
|---|---|---|---|
| `address` | `tax_product_resource_postal_address` |  | The customer's postal address (for example, home or business location). |
| `address_source` | enum: `billing`, `shipping` |  | The type of customer address provided. |
| `ip_address` | string |  | The customer's IP address (IPv4 or IPv6). |
| `tax_ids` | array of `tax_product_resource_customer_details_resource_tax_id` | yes | The customer's tax IDs (for example, EU VAT numbers). |
| `taxability_override` | enum: `customer_exempt`, `none`, `reverse_charge` | yes | The taxability override used for taxation. |

