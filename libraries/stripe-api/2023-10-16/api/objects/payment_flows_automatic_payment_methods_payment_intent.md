# Stripe API 2023-10-16 — `payment_flows_automatic_payment_methods_payment_intent` object

| Field | Type | Required | Description |
|---|---|---|---|
| `allow_redirects` | enum: `always`, `never` |  | Controls whether this PaymentIntent will accept redirect-based payment methods.<br>Redirect-based payment methods may require your customer to be redirected to a payment method's app or site for authentication or additional steps. To [confirm](https://stripe.com/docs/api/payment_intents/confirm) this PaymentIntent, you may be required to provide a `return_url` to redirect customers back to your site after they authenticate or complete the payment. |
| `enabled` | boolean | yes | Automatically calculates compatible payment methods |

