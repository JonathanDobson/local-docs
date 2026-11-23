# Stripe API 2023-10-16 — `customer_balance_resource_cash_balance_transaction_resource_funded_transaction_resource_bank_transfer` object

Expandable fields (pass `expand[]=<field>`): `eu_bank_transfer`, `gb_bank_transfer`, `jp_bank_transfer`, `us_bank_transfer`

| Field | Type | Required | Description |
|---|---|---|---|
| `eu_bank_transfer` | `customer_balance_resource_cash_balance_transaction_resource_funded_transaction_resource_bank_transfer_resource_eu_bank_transfer` |  |  |
| `gb_bank_transfer` | `customer_balance_resource_cash_balance_transaction_resource_funded_transaction_resource_bank_transfer_resource_gb_bank_transfer` |  |  |
| `jp_bank_transfer` | `customer_balance_resource_cash_balance_transaction_resource_funded_transaction_resource_bank_transfer_resource_jp_bank_transfer` |  |  |
| `reference` | string |  | The user-supplied reference field on the bank transfer. |
| `type` | enum: `eu_bank_transfer`, `gb_bank_transfer`, `jp_bank_transfer`, `mx_bank_transfer`, `us_bank_transfer` | yes | The funding method type used to fund the customer balance. Permitted values include: `eu_bank_transfer`, `gb_bank_transfer`, `jp_bank_transfer`, `mx_bank_transfer`, or `us_bank_transfer`. |
| `us_bank_transfer` | `customer_balance_resource_cash_balance_transaction_resource_funded_transaction_resource_bank_transfer_resource_us_bank_transfer` |  |  |

