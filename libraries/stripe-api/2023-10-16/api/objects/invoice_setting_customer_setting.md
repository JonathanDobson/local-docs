# Stripe API 2023-10-16 — `invoice_setting_customer_setting` object

Expandable fields (pass `expand[]=<field>`): `custom_fields`, `default_payment_method`, `rendering_options`

| Field | Type | Required | Description |
|---|---|---|---|
| `custom_fields` | array of `invoice_setting_custom_field` |  | Default custom fields to be displayed on invoices for this customer. |
| `default_payment_method` | string or `payment_method` |  | ID of a payment method that's attached to the customer, to be used as the customer's default payment method for subscriptions and invoices. |
| `footer` | string |  | Default footer to be displayed on invoices for this customer. |
| `rendering_options` | `invoice_setting_rendering_options` |  | Default options for invoice PDF rendering for this customer. |

