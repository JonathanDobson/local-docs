# Stripe API 2023-10-16 — `invoices_payment_method_options` object

Expandable fields (pass `expand[]=<field>`): `acss_debit`, `bancontact`, `card`, `customer_balance`, `konbini`, `sepa_debit`, `us_bank_account`

| Field | Type | Required | Description |
|---|---|---|---|
| `acss_debit` | `invoice_payment_method_options_acss_debit` |  | If paying by `acss_debit`, this sub-hash contains details about the Canadian pre-authorized debit payment method options to pass to the invoice’s PaymentIntent. |
| `bancontact` | `invoice_payment_method_options_bancontact` |  | If paying by `bancontact`, this sub-hash contains details about the Bancontact payment method options to pass to the invoice’s PaymentIntent. |
| `card` | `invoice_payment_method_options_card` |  | If paying by `card`, this sub-hash contains details about the Card payment method options to pass to the invoice’s PaymentIntent. |
| `customer_balance` | `invoice_payment_method_options_customer_balance` |  | If paying by `customer_balance`, this sub-hash contains details about the Bank transfer payment method options to pass to the invoice’s PaymentIntent. |
| `konbini` | `invoice_payment_method_options_konbini` |  | If paying by `konbini`, this sub-hash contains details about the Konbini payment method options to pass to the invoice’s PaymentIntent. |
| `sepa_debit` | `invoice_payment_method_options_sepa_debit` |  | If paying by `sepa_debit`, this sub-hash contains details about the SEPA Direct Debit payment method options to pass to the invoice’s PaymentIntent. |
| `us_bank_account` | `invoice_payment_method_options_us_bank_account` |  | If paying by `us_bank_account`, this sub-hash contains details about the ACH direct debit payment method options to pass to the invoice’s PaymentIntent. |

