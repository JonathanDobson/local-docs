# Stripe API 2023-10-16 — `funding_instructions_bank_transfer` object

Expandable fields (pass `expand[]=<field>`): `financial_addresses`

| Field | Type | Required | Description |
|---|---|---|---|
| `country` | string | yes | The country of the bank account to fund |
| `financial_addresses` | array of `funding_instructions_bank_transfer_financial_address` | yes | A list of financial addresses that can be used to fund a particular balance |
| `type` | enum: `eu_bank_transfer`, `jp_bank_transfer` | yes | The bank_transfer type |

