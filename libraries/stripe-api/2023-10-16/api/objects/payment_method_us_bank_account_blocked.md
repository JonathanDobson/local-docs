# Stripe API 2023-10-16 — `payment_method_us_bank_account_blocked` object

| Field | Type | Required | Description |
|---|---|---|---|
| `network_code` | enum: `R02`, `R03`, `R04`, `R05`, `R07`, `R08`, `R10`, `R11`, `R16`, `R20`, `R29`, `R31` |  | The ACH network code that resulted in this block. |
| `reason` | enum: `bank_account_closed`, `bank_account_frozen`, `bank_account_invalid_details`, `bank_account_restricted`, `bank_account_unusable`, `debit_not_authorized` |  | The reason why this PaymentMethod's fingerprint has been blocked |

