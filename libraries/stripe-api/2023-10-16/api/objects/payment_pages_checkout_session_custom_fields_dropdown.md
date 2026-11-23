# Stripe API 2023-10-16 — `payment_pages_checkout_session_custom_fields_dropdown` object

Expandable fields (pass `expand[]=<field>`): `options`

| Field | Type | Required | Description |
|---|---|---|---|
| `options` | array of `payment_pages_checkout_session_custom_fields_option` | yes | The options available for the customer to select. Up to 200 options allowed. |
| `value` | string |  | The option selected by the customer. This will be the `value` for the option. |

