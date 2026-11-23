# Stripe API 2023-10-16 — `payment_pages_checkout_session_custom_fields` object

Expandable fields (pass `expand[]=<field>`): `dropdown`, `label`, `numeric`, `text`

| Field | Type | Required | Description |
|---|---|---|---|
| `dropdown` | `payment_pages_checkout_session_custom_fields_dropdown` |  |  |
| `key` | string | yes | String of your choice that your integration can use to reconcile this field. Must be unique to this field, alphanumeric, and up to 200 characters. |
| `label` | `payment_pages_checkout_session_custom_fields_label` | yes |  |
| `numeric` | `payment_pages_checkout_session_custom_fields_numeric` |  |  |
| `optional` | boolean | yes | Whether the customer is required to complete the field before completing the Checkout Session. Defaults to `false`. |
| `text` | `payment_pages_checkout_session_custom_fields_text` |  |  |
| `type` | enum: `dropdown`, `numeric`, `text` | yes | The type of the field. |

