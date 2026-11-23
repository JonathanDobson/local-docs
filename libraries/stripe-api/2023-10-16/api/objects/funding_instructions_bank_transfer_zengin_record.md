# Stripe API 2023-10-16 — `funding_instructions_bank_transfer_zengin_record` object

Zengin Records contain Japan bank account details per the Zengin format.

| Field | Type | Required | Description |
|---|---|---|---|
| `account_holder_name` | string |  | The account holder name |
| `account_number` | string |  | The account number |
| `account_type` | string |  | The bank account type. In Japan, this can only be `futsu` or `toza`. |
| `bank_code` | string |  | The bank code of the account |
| `bank_name` | string |  | The bank name of the account |
| `branch_code` | string |  | The branch code of the account |
| `branch_name` | string |  | The branch name of the account |

