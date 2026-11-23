# Stripe API 2023-10-16 — `setup_intent_payment_method_options_acss_debit` object

Expandable fields (pass `expand[]=<field>`): `mandate_options`

| Field | Type | Required | Description |
|---|---|---|---|
| `currency` | enum: `cad`, `usd` |  | Currency supported by the bank account |
| `mandate_options` | `setup_intent_payment_method_options_mandate_options_acss_debit` |  |  |
| `verification_method` | enum: `automatic`, `instant`, `microdeposits` |  | Bank account verification method. |

