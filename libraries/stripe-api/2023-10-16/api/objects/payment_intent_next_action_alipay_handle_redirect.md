# Stripe API 2023-10-16 — `payment_intent_next_action_alipay_handle_redirect` object

| Field | Type | Required | Description |
|---|---|---|---|
| `native_data` | string |  | The native data to be used with Alipay SDK you must redirect your customer to in order to authenticate the payment in an Android App. |
| `native_url` | string |  | The native URL you must redirect your customer to in order to authenticate the payment in an iOS App. |
| `return_url` | string |  | If the customer does not exit their browser while authenticating, they will be redirected to this specified URL after completion. |
| `url` | string |  | The URL you must redirect your customer to in order to authenticate the payment. |

