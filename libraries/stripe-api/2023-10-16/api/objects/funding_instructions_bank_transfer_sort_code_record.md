# Stripe API 2023-10-16 — `funding_instructions_bank_transfer_sort_code_record` object

Sort Code Records contain U.K. bank account details per the sort code format.

| Field | Type | Required | Description |
|---|---|---|---|
| `account_holder_name` | string | yes | The name of the person or business that owns the bank account |
| `account_number` | string | yes | The account number |
| `sort_code` | string | yes | The six-digit sort code |

