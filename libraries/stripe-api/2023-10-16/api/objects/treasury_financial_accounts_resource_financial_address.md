# Stripe API 2023-10-16 — `treasury_financial_accounts_resource_financial_address` object

FinancialAddresses contain identifying information that resolves to a FinancialAccount.

Expandable fields (pass `expand[]=<field>`): `aba`

| Field | Type | Required | Description |
|---|---|---|---|
| `aba` | `treasury_financial_accounts_resource_aba_record` |  |  |
| `supported_networks` | array of enum: `ach`, `us_domestic_wire` |  | The list of networks that the address supports |
| `type` | enum: `aba` | yes | The type of financial address |

