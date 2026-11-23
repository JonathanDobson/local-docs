# Stripe API 2023-10-16 — `treasury_financial_accounts_resource_aba_record` object

ABA Records contain U.S. bank account details per the ABA format.

| Field | Type | Required | Description |
|---|---|---|---|
| `account_holder_name` | string | yes | The name of the person or business that owns the bank account. |
| `account_number` | string |  | The account number. |
| `account_number_last4` | string | yes | The last four characters of the account number. |
| `bank_name` | string | yes | Name of the bank. |
| `routing_number` | string | yes | Routing number for the account. |

