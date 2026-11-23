# Stripe API 2023-10-16 — `funding_instructions_bank_transfer_financial_address` object

FinancialAddresses contain identifying information that resolves to a FinancialAccount.

Expandable fields (pass `expand[]=<field>`): `aba`, `iban`, `sort_code`, `spei`, `swift`, `zengin`

| Field | Type | Required | Description |
|---|---|---|---|
| `aba` | `funding_instructions_bank_transfer_aba_record` |  |  |
| `iban` | `funding_instructions_bank_transfer_iban_record` |  |  |
| `sort_code` | `funding_instructions_bank_transfer_sort_code_record` |  |  |
| `spei` | `funding_instructions_bank_transfer_spei_record` |  |  |
| `supported_networks` | array of enum: `ach`, `bacs`, `domestic_wire_us`, `fps`, `sepa`, `spei`, `swift`, `zengin` |  | The payment networks supported by this FinancialAddress |
| `swift` | `funding_instructions_bank_transfer_swift_record` |  |  |
| `type` | enum: `aba`, `iban`, `sort_code`, `spei`, `swift`, `zengin` | yes | The type of financial address |
| `zengin` | `funding_instructions_bank_transfer_zengin_record` |  |  |

