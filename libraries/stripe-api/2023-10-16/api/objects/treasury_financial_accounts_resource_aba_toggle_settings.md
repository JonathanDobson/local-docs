# Stripe API 2023-10-16 — `treasury_financial_accounts_resource_aba_toggle_settings` object

Toggle settings for enabling/disabling the ABA address feature

Expandable fields (pass `expand[]=<field>`): `status_details`

| Field | Type | Required | Description |
|---|---|---|---|
| `requested` | boolean | yes | Whether the FinancialAccount should have the Feature. |
| `status` | enum: `active`, `pending`, `restricted` | yes | Whether the Feature is operational. |
| `status_details` | array of `treasury_financial_accounts_resource_toggles_setting_status_details` | yes | Additional details; includes at least one entry when the status is not `active`. |

