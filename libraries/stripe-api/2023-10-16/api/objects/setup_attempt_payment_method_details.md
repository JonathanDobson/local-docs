# Stripe API 2023-10-16 — `setup_attempt_payment_method_details` object

Expandable fields (pass `expand[]=<field>`): `acss_debit`, `au_becs_debit`, `bacs_debit`, `bancontact`, `boleto`, `card`, `card_present`, `cashapp`, `ideal`, `klarna`, `link`, `paypal`, `sepa_debit`, `sofort`, `us_bank_account`

| Field | Type | Required | Description |
|---|---|---|---|
| `acss_debit` | `setup_attempt_payment_method_details_acss_debit` |  |  |
| `au_becs_debit` | `setup_attempt_payment_method_details_au_becs_debit` |  |  |
| `bacs_debit` | `setup_attempt_payment_method_details_bacs_debit` |  |  |
| `bancontact` | `setup_attempt_payment_method_details_bancontact` |  |  |
| `boleto` | `setup_attempt_payment_method_details_boleto` |  |  |
| `card` | `setup_attempt_payment_method_details_card` |  |  |
| `card_present` | `setup_attempt_payment_method_details_card_present` |  |  |
| `cashapp` | `setup_attempt_payment_method_details_cashapp` |  |  |
| `ideal` | `setup_attempt_payment_method_details_ideal` |  |  |
| `klarna` | `setup_attempt_payment_method_details_klarna` |  |  |
| `link` | `setup_attempt_payment_method_details_link` |  |  |
| `paypal` | `setup_attempt_payment_method_details_paypal` |  |  |
| `sepa_debit` | `setup_attempt_payment_method_details_sepa_debit` |  |  |
| `sofort` | `setup_attempt_payment_method_details_sofort` |  |  |
| `type` | string | yes | The type of the payment method used in the SetupIntent (e.g., `card`). An additional hash is included on `payment_method_details` with a name matching this value. It contains confirmation-specific information for the payment method. |
| `us_bank_account` | `setup_attempt_payment_method_details_us_bank_account` |  |  |

