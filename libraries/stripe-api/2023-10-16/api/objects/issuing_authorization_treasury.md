# Stripe API 2023-10-16 — `issuing_authorization_treasury` object

| Field | Type | Required | Description |
|---|---|---|---|
| `received_credits` | array of string | yes | The array of [ReceivedCredits](https://stripe.com/docs/api/treasury/received_credits) associated with this authorization |
| `received_debits` | array of string | yes | The array of [ReceivedDebits](https://stripe.com/docs/api/treasury/received_debits) associated with this authorization |
| `transaction` | string |  | The Treasury [Transaction](https://stripe.com/docs/api/treasury/transactions) associated with this authorization |

