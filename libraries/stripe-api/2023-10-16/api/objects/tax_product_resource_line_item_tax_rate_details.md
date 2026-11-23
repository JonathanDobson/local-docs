# Stripe API 2023-10-16 — `tax_product_resource_line_item_tax_rate_details` object

| Field | Type | Required | Description |
|---|---|---|---|
| `display_name` | string | yes | A localized display name for tax type, intended to be human-readable. For example, "Local Sales and Use Tax", "Value-added tax (VAT)", or "Umsatzsteuer (USt.)". |
| `percentage_decimal` | string | yes | The tax rate percentage as a string. For example, 8.5% is represented as "8.5". |
| `tax_type` | enum: `amusement_tax`, `communications_tax`, `gst`, `hst`, `igst`, `jct`, `lease_tax`, `pst`, `qst`, `rst`, `sales_tax`, `vat` | yes | The tax type, such as `vat` or `sales_tax`. |

