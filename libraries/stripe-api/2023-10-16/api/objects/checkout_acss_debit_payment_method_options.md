# Stripe API 2023-10-16 — `checkout_acss_debit_payment_method_options` object

Expandable fields (pass `expand[]=<field>`): `mandate_options`

| Field | Type | Required | Description |
|---|---|---|---|
| `currency` | enum: `cad`, `usd` |  | Currency supported by the bank account. Returned when the Session is in `setup` mode. |
| `mandate_options` | `checkout_acss_debit_mandate_options` |  |  |
| `setup_future_usage` | enum: `none`, `off_session`, `on_session` |  | Indicates that you intend to make future payments with this PaymentIntent's payment method.<br>Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.<br>When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication). |
| `verification_method` | enum: `automatic`, `instant`, `microdeposits` |  | Bank account verification method. |

