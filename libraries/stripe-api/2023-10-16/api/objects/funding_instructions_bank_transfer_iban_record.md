# Stripe API 2023-10-16 — `funding_instructions_bank_transfer_iban_record` object

Iban Records contain E.U. bank account details per the SEPA format.

| Field | Type | Required | Description |
|---|---|---|---|
| `account_holder_name` | string | yes | The name of the person or business that owns the bank account |
| `bic` | string | yes | The BIC/SWIFT code of the account. |
| `country` | string | yes | Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)). |
| `iban` | string | yes | The IBAN of the account. |

