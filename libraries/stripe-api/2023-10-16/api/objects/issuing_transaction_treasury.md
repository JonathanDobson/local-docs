# Stripe API 2023-10-16 — `issuing_transaction_treasury` object

| Field | Type | Required | Description |
|---|---|---|---|
| `received_credit` | string |  | The Treasury [ReceivedCredit](https://stripe.com/docs/api/treasury/received_credits) representing this Issuing transaction if it is a refund |
| `received_debit` | string |  | The Treasury [ReceivedDebit](https://stripe.com/docs/api/treasury/received_debits) representing this Issuing transaction if it is a capture |

