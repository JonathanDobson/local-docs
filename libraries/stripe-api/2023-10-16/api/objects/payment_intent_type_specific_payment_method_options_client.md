# Stripe API 2023-10-16 — `payment_intent_type_specific_payment_method_options_client` object

Expandable fields (pass `expand[]=<field>`): `installments`

| Field | Type | Required | Description |
|---|---|---|---|
| `capture_method` | enum: `manual`, `manual_preferred` |  | Controls when the funds will be captured from the customer's account. |
| `installments` | `payment_flows_installment_options` |  |  |
| `require_cvc_recollection` | boolean |  | When enabled, using a card that is attached to a customer will require the CVC to be provided again (i.e. using the cvc_token parameter). |
| `setup_future_usage` | enum: `none`, `off_session`, `on_session` |  | Indicates that you intend to make future payments with this PaymentIntent's payment method.<br>Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.<br>When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication). |
| `verification_method` | enum: `automatic`, `instant`, `microdeposits` |  | Bank account verification method. |

