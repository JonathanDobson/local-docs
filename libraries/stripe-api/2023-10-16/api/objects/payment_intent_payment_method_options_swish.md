# Stripe API 2023-10-16 — `payment_intent_payment_method_options_swish` object

| Field | Type | Required | Description |
|---|---|---|---|
| `reference` | string |  | The order ID displayed in the Swish app after the payment is authorized. |
| `setup_future_usage` | enum: `none` |  | Indicates that you intend to make future payments with this PaymentIntent's payment method.<br>Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.<br>When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication). |

