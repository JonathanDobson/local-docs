# Stripe API 2023-10-16 — `setup_intent_next_action` object

Expandable fields (pass `expand[]=<field>`): `cashapp_handle_redirect_or_display_qr_code`, `redirect_to_url`, `verify_with_microdeposits`

| Field | Type | Required | Description |
|---|---|---|---|
| `cashapp_handle_redirect_or_display_qr_code` | `payment_intent_next_action_cashapp_handle_redirect_or_display_qr_code` |  |  |
| `redirect_to_url` | `setup_intent_next_action_redirect_to_url` |  |  |
| `type` | string | yes | Type of the next action to perform, one of `redirect_to_url`, `use_stripe_sdk`, `alipay_handle_redirect`, `oxxo_display_details`, or `verify_with_microdeposits`. |
| `use_stripe_sdk` | object |  | When confirming a SetupIntent with Stripe.js, Stripe.js depends on the contents of this dictionary to invoke authentication flows. The shape of the contents is subject to change and is only intended to be used by Stripe.js. |
| `verify_with_microdeposits` | `setup_intent_next_action_verify_with_microdeposits` |  |  |

