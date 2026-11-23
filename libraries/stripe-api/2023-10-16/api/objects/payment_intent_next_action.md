# Stripe API 2023-10-16 — `payment_intent_next_action` object

Expandable fields (pass `expand[]=<field>`): `alipay_handle_redirect`, `boleto_display_details`, `card_await_notification`, `cashapp_handle_redirect_or_display_qr_code`, `display_bank_transfer_instructions`, `konbini_display_details`, `oxxo_display_details`, `paynow_display_qr_code`, `pix_display_qr_code`, `promptpay_display_qr_code`, `redirect_to_url`, `swish_handle_redirect_or_display_qr_code`, `verify_with_microdeposits`, `wechat_pay_display_qr_code`, `wechat_pay_redirect_to_android_app`, `wechat_pay_redirect_to_ios_app`

| Field | Type | Required | Description |
|---|---|---|---|
| `alipay_handle_redirect` | `payment_intent_next_action_alipay_handle_redirect` |  |  |
| `boleto_display_details` | `payment_intent_next_action_boleto` |  |  |
| `card_await_notification` | `payment_intent_next_action_card_await_notification` |  |  |
| `cashapp_handle_redirect_or_display_qr_code` | `payment_intent_next_action_cashapp_handle_redirect_or_display_qr_code` |  |  |
| `display_bank_transfer_instructions` | `payment_intent_next_action_display_bank_transfer_instructions` |  |  |
| `konbini_display_details` | `payment_intent_next_action_konbini` |  |  |
| `oxxo_display_details` | `payment_intent_next_action_display_oxxo_details` |  |  |
| `paynow_display_qr_code` | `payment_intent_next_action_paynow_display_qr_code` |  |  |
| `pix_display_qr_code` | `payment_intent_next_action_pix_display_qr_code` |  |  |
| `promptpay_display_qr_code` | `payment_intent_next_action_promptpay_display_qr_code` |  |  |
| `redirect_to_url` | `payment_intent_next_action_redirect_to_url` |  |  |
| `swish_handle_redirect_or_display_qr_code` | `payment_intent_next_action_swish_handle_redirect_or_display_qr_code` |  |  |
| `type` | string | yes | Type of the next action to perform, one of `redirect_to_url`, `use_stripe_sdk`, `alipay_handle_redirect`, `oxxo_display_details`, or `verify_with_microdeposits`. |
| `use_stripe_sdk` | object |  | When confirming a PaymentIntent with Stripe.js, Stripe.js depends on the contents of this dictionary to invoke authentication flows. The shape of the contents is subject to change and is only intended to be used by Stripe.js. |
| `verify_with_microdeposits` | `payment_intent_next_action_verify_with_microdeposits` |  |  |
| `wechat_pay_display_qr_code` | `payment_intent_next_action_wechat_pay_display_qr_code` |  |  |
| `wechat_pay_redirect_to_android_app` | `payment_intent_next_action_wechat_pay_redirect_to_android_app` |  |  |
| `wechat_pay_redirect_to_ios_app` | `payment_intent_next_action_wechat_pay_redirect_to_ios_app` |  |  |

