# Stripe API 2023-10-16 — `subscriptions_resource_payment_method_options` object

Expandable fields (pass `expand[]=<field>`): `acss_debit`, `bancontact`, `card`, `customer_balance`, `konbini`, `sepa_debit`, `us_bank_account`

| Field | Type | Required | Description |
|---|---|---|---|
| `acss_debit` | `invoice_payment_method_options_acss_debit` |  | This sub-hash contains details about the Canadian pre-authorized debit payment method options to pass to invoices created by the subscription. |
| `bancontact` | `invoice_payment_method_options_bancontact` |  | This sub-hash contains details about the Bancontact payment method options to pass to invoices created by the subscription. |
| `card` | `subscription_payment_method_options_card` |  | This sub-hash contains details about the Card payment method options to pass to invoices created by the subscription. |
| `customer_balance` | `invoice_payment_method_options_customer_balance` |  | This sub-hash contains details about the Bank transfer payment method options to pass to invoices created by the subscription. |
| `konbini` | `invoice_payment_method_options_konbini` |  | This sub-hash contains details about the Konbini payment method options to pass to invoices created by the subscription. |
| `sepa_debit` | `invoice_payment_method_options_sepa_debit` |  | This sub-hash contains details about the SEPA Direct Debit payment method options to pass to invoices created by the subscription. |
| `us_bank_account` | `invoice_payment_method_options_us_bank_account` |  | This sub-hash contains details about the ACH direct debit payment method options to pass to invoices created by the subscription. |

