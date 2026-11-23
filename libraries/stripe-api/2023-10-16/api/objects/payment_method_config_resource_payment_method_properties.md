# Stripe API 2023-10-16 — `payment_method_config_resource_payment_method_properties` object

Expandable fields (pass `expand[]=<field>`): `display_preference`

| Field | Type | Required | Description |
|---|---|---|---|
| `available` | boolean | yes | Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active. |
| `display_preference` | `payment_method_config_resource_display_preference` | yes |  |

