# Stripe API 2023-10-16 — `payment_intent_next_action_cashapp_handle_redirect_or_display_qr_code` object

Expandable fields (pass `expand[]=<field>`): `qr_code`

| Field | Type | Required | Description |
|---|---|---|---|
| `hosted_instructions_url` | string | yes | The URL to the hosted Cash App Pay instructions page, which allows customers to view the QR code, and supports QR code refreshing on expiration. |
| `mobile_auth_url` | string | yes | The url for mobile redirect based auth |
| `qr_code` | `payment_intent_next_action_cashapp_qr_code` | yes |  |

