# Stripe API 2023-10-16 — `customer_balance_resource_cash_balance_transaction_resource_adjusted_for_overdraft` object

Expandable fields (pass `expand[]=<field>`): `balance_transaction`, `linked_transaction`

| Field | Type | Required | Description |
|---|---|---|---|
| `balance_transaction` | string or `balance_transaction` | yes | The [Balance Transaction](https://stripe.com/docs/api/balance_transactions/object) that corresponds to funds taken out of your Stripe balance. |
| `linked_transaction` | string or `customer_cash_balance_transaction` | yes | The [Cash Balance Transaction](https://stripe.com/docs/api/cash_balance_transactions/object) that brought the customer balance negative, triggering the clawback of funds. |

