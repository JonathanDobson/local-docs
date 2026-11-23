# Stripe API 2023-10-16 — `mandate_payment_method_details` object

Expandable fields (pass `expand[]=<field>`): `acss_debit`, `au_becs_debit`, `bacs_debit`, `card`, `cashapp`, `link`, `paypal`, `sepa_debit`, `us_bank_account`

| Field | Type | Required | Description |
|---|---|---|---|
| `acss_debit` | `mandate_acss_debit` |  |  |
| `au_becs_debit` | `mandate_au_becs_debit` |  |  |
| `bacs_debit` | `mandate_bacs_debit` |  |  |
| `card` | `card_mandate_payment_method_details` |  |  |
| `cashapp` | `mandate_cashapp` |  |  |
| `link` | `mandate_link` |  |  |
| `paypal` | `mandate_paypal` |  |  |
| `sepa_debit` | `mandate_sepa_debit` |  |  |
| `type` | string | yes | This mandate corresponds with a specific payment method type. The `payment_method_details` includes an additional hash with the same name and contains mandate information that's specific to that payment method. |
| `us_bank_account` | `mandate_us_bank_account` |  |  |

