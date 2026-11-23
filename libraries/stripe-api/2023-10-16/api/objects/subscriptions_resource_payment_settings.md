# Stripe API 2023-10-16 — `subscriptions_resource_payment_settings` object

Expandable fields (pass `expand[]=<field>`): `payment_method_options`

| Field | Type | Required | Description |
|---|---|---|---|
| `payment_method_options` | `subscriptions_resource_payment_method_options` |  | Payment-method-specific configuration to provide to invoices created by the subscription. |
| `payment_method_types` | array of enum: `ach_credit_transfer`, `ach_debit`, `acss_debit`, `au_becs_debit`, `bacs_debit`, `bancontact`, `boleto`, `card`, `cashapp`, `customer_balance`, `eps`, `fpx`, `giropay`, `grabpay`, `ideal`, `konbini`, `link`, `p24`, `paynow`, `paypal`, `promptpay`, `sepa_debit`, `sofort`, `us_bank_account`, `wechat_pay` |  | The list of payment method types to provide to every invoice created by the subscription. If not set, Stripe attempts to automatically determine the types to use by looking at the invoice’s default payment method, the subscription’s default payment method, the customer’s default payment method, and your [invoice template settings](https://dashboard.stripe.com/settings/billing/invoice). |
| `save_default_payment_method` | enum: `off`, `on_subscription` |  | Either `off`, or `on_subscription`. With `on_subscription` Stripe updates `subscription.default_payment_method` when a subscription payment succeeds. |

