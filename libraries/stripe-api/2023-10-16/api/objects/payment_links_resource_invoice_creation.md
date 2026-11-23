# Stripe API 2023-10-16 — `payment_links_resource_invoice_creation` object

Expandable fields (pass `expand[]=<field>`): `invoice_data`

| Field | Type | Required | Description |
|---|---|---|---|
| `enabled` | boolean | yes | Enable creating an invoice on successful payment. |
| `invoice_data` | `payment_links_resource_invoice_settings` |  | Configuration for the invoice. Default invoice values will be used if unspecified. |

