# Stripe API 2023-10-16 — `account_settings` object

Expandable fields (pass `expand[]=<field>`): `bacs_debit_payments`, `branding`, `card_issuing`, `card_payments`, `dashboard`, `invoices`, `payments`, `payouts`, `sepa_debit_payments`, `treasury`

| Field | Type | Required | Description |
|---|---|---|---|
| `bacs_debit_payments` | `account_bacs_debit_payments_settings` |  |  |
| `branding` | `account_branding_settings` | yes |  |
| `card_issuing` | `account_card_issuing_settings` |  |  |
| `card_payments` | `account_card_payments_settings` | yes |  |
| `dashboard` | `account_dashboard_settings` | yes |  |
| `invoices` | `account_invoices_settings` |  |  |
| `payments` | `account_payments_settings` | yes |  |
| `payouts` | `account_payout_settings` |  |  |
| `sepa_debit_payments` | `account_sepa_debit_payments_settings` |  |  |
| `treasury` | `account_treasury_settings` |  |  |

