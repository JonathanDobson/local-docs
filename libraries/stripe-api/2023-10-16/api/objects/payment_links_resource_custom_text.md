# Stripe API 2023-10-16 — `payment_links_resource_custom_text` object

Expandable fields (pass `expand[]=<field>`): `after_submit`, `shipping_address`, `submit`, `terms_of_service_acceptance`

| Field | Type | Required | Description |
|---|---|---|---|
| `after_submit` | `payment_links_resource_custom_text_position` |  | Custom text that should be displayed after the payment confirmation button. |
| `shipping_address` | `payment_links_resource_custom_text_position` |  | Custom text that should be displayed alongside shipping address collection. |
| `submit` | `payment_links_resource_custom_text_position` |  | Custom text that should be displayed alongside the payment confirmation button. |
| `terms_of_service_acceptance` | `payment_links_resource_custom_text_position` |  | Custom text that should be displayed in place of the default terms of service agreement text. |

