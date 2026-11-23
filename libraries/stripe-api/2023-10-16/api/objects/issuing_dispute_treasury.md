# Stripe API 2023-10-16 — `issuing_dispute_treasury` object

| Field | Type | Required | Description |
|---|---|---|---|
| `debit_reversal` | string |  | The Treasury [DebitReversal](https://stripe.com/docs/api/treasury/debit_reversals) representing this Issuing dispute |
| `received_debit` | string | yes | The Treasury [ReceivedDebit](https://stripe.com/docs/api/treasury/received_debits) that is being disputed. |

