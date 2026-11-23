# Stripe API 2023-10-16 — `payment_method_options_card_present` object

| Field | Type | Required | Description |
|---|---|---|---|
| `request_extended_authorization` | boolean |  | Request ability to capture this payment beyond the standard [authorization validity window](https://stripe.com/docs/terminal/features/extended-authorizations#authorization-validity) |
| `request_incremental_authorization_support` | boolean |  | Request ability to [increment](https://stripe.com/docs/terminal/features/incremental-authorizations) this PaymentIntent if the combination of MCC and card brand is eligible. Check [incremental_authorization_supported](https://stripe.com/docs/api/charges/object#charge_object-payment_method_details-card_present-incremental_authorization_supported) in the [Confirm](https://stripe.com/docs/api/payment_intents/confirm) response to verify support. |

