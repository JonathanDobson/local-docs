# Stripe API 2023-10-16 — `payment_links_resource_invoice_settings` object

Expandable fields (pass `expand[]=<field>`): `account_tax_ids`, `custom_fields`, `issuer`, `rendering_options`

| Field | Type | Required | Description |
|---|---|---|---|
| `account_tax_ids` | array of string or `tax_id` or `deleted_tax_id` |  | The account tax IDs associated with the invoice. |
| `custom_fields` | array of `invoice_setting_custom_field` |  | A list of up to 4 custom fields to be displayed on the invoice. |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. |
| `footer` | string |  | Footer to be displayed on the invoice. |
| `issuer` | `connect_account_reference` |  | The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `rendering_options` | `invoice_setting_rendering_options` |  | Options for invoice PDF rendering. |

