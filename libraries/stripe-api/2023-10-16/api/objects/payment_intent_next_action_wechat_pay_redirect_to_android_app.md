# Stripe API 2023-10-16 — `payment_intent_next_action_wechat_pay_redirect_to_android_app` object

| Field | Type | Required | Description |
|---|---|---|---|
| `app_id` | string | yes | app_id is the APP ID registered on WeChat open platform |
| `nonce_str` | string | yes | nonce_str is a random string |
| `package` | string | yes | package is static value |
| `partner_id` | string | yes | an unique merchant ID assigned by WeChat Pay |
| `prepay_id` | string | yes | an unique trading ID assigned by WeChat Pay |
| `sign` | string | yes | A signature |
| `timestamp` | string | yes | Specifies the current time in epoch format |

