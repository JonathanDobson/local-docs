# Stripe API 2023-10-16 — `treasury_transactions_resource_balance_impact` object

Change to a FinancialAccount's balance

| Field | Type | Required | Description |
|---|---|---|---|
| `cash` | integer | yes | The change made to funds the user can spend right now. |
| `inbound_pending` | integer | yes | The change made to funds that are not spendable yet, but will become available at a later time. |
| `outbound_pending` | integer | yes | The change made to funds in the account, but not spendable because they are being held for pending outbound flows. |

