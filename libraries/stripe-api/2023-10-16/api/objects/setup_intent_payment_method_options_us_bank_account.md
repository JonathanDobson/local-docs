# Stripe API 2023-10-16 — `setup_intent_payment_method_options_us_bank_account` object

Expandable fields (pass `expand[]=<field>`): `financial_connections`, `mandate_options`

| Field | Type | Required | Description |
|---|---|---|---|
| `financial_connections` | `linked_account_options_us_bank_account` |  |  |
| `mandate_options` | `payment_method_options_us_bank_account_mandate_options` |  |  |
| `verification_method` | enum: `automatic`, `instant`, `microdeposits` |  | Bank account verification method. |

