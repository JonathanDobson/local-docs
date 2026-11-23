# Stripe API 2023-10-16 — `treasury_financial_accounts_resource_balance` object

Balance information for the FinancialAccount

| Field | Type | Required | Description |
|---|---|---|---|
| `cash` | map (key → value) | yes | Funds the user can spend right now. |
| `inbound_pending` | map (key → value) | yes | Funds not spendable yet, but will become available at a later time. |
| `outbound_pending` | map (key → value) | yes | Funds in the account, but not spendable because they are being held for pending outbound flows. |

