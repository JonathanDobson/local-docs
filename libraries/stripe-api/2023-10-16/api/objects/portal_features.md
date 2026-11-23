# Stripe API 2023-10-16 — `portal_features` object

Expandable fields (pass `expand[]=<field>`): `customer_update`, `invoice_history`, `payment_method_update`, `subscription_cancel`, `subscription_update`

| Field | Type | Required | Description |
|---|---|---|---|
| `customer_update` | `portal_customer_update` | yes |  |
| `invoice_history` | `portal_invoice_list` | yes |  |
| `payment_method_update` | `portal_payment_method_update` | yes |  |
| `subscription_cancel` | `portal_subscription_cancel` | yes |  |
| `subscription_update` | `portal_subscription_update` | yes |  |

