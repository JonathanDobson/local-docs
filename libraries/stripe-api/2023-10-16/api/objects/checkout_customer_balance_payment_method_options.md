# Stripe API 2023-10-16 — `checkout_customer_balance_payment_method_options` object

Expandable fields (pass `expand[]=<field>`): `bank_transfer`

| Field | Type | Required | Description |
|---|---|---|---|
| `bank_transfer` | `checkout_customer_balance_bank_transfer_payment_method_options` |  |  |
| `funding_type` | enum: `bank_transfer` |  | The funding method type to be used when there are not enough funds in the customer balance. Permitted values include: `bank_transfer`. |
| `setup_future_usage` | enum: `none` |  | Indicates that you intend to make future payments with this PaymentIntent's payment method.<br>Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.<br>When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication). |

