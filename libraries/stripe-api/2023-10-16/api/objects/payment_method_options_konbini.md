# Stripe API 2023-10-16 — `payment_method_options_konbini` object

| Field | Type | Required | Description |
|---|---|---|---|
| `confirmation_number` | string |  | An optional 10 to 11 digit numeric-only string determining the confirmation code at applicable convenience stores. |
| `expires_after_days` | integer |  | The number of calendar days (between 1 and 60) after which Konbini payment instructions will expire. For example, if a PaymentIntent is confirmed with Konbini and `expires_after_days` set to 2 on Monday JST, the instructions will expire on Wednesday 23:59:59 JST. |
| `expires_at` | timestamp (Unix seconds) |  | The timestamp at which the Konbini payment instructions will expire. Only one of `expires_after_days` or `expires_at` may be set. |
| `product_description` | string |  | A product descriptor of up to 22 characters, which will appear to customers at the convenience store. |
| `setup_future_usage` | enum: `none` |  | Indicates that you intend to make future payments with this PaymentIntent's payment method.<br>Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.<br>When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication). |

