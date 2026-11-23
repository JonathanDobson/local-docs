# Stripe API 2023-10-16 — `invoices_payment_settings` object

Expandable fields (pass `expand[]=<field>`): `payment_method_options`

| Field | Type | Required | Description |
|---|---|---|---|
| `default_mandate` | string |  | ID of the mandate to be used for this invoice. It must correspond to the payment method used to pay the invoice, including the invoice's default_payment_method or default_source, if set. |
| `payment_method_options` | `invoices_payment_method_options` |  | Payment-method-specific configuration to provide to the invoice’s PaymentIntent. |
| `payment_method_types` | array of enum: `ach_credit_transfer`, `ach_debit`, `acss_debit`, `au_becs_debit`, `bacs_debit`, `bancontact`, `boleto`, `card`, `cashapp`, `customer_balance`, `eps`, `fpx`, `giropay`, `grabpay`, `ideal`, `konbini`, `link`, `p24`, `paynow`, `paypal`, `promptpay`, `sepa_debit`, `sofort`, `us_bank_account`, `wechat_pay` |  | The list of payment method types (e.g. card) to provide to the invoice’s PaymentIntent. If not set, Stripe attempts to automatically determine the types to use by looking at the invoice’s default payment method, the subscription’s default payment method, the customer’s default payment method, and your [invoice template settings](https://dashboard.stripe.com/settings/billing/invoice). |

