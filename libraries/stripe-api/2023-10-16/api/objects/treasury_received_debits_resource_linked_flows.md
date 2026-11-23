# Stripe API 2023-10-16 — `treasury_received_debits_resource_linked_flows` object

| Field | Type | Required | Description |
|---|---|---|---|
| `debit_reversal` | string |  | The DebitReversal created as a result of this ReceivedDebit being reversed. |
| `inbound_transfer` | string |  | Set if the ReceivedDebit is associated with an InboundTransfer's return of funds. |
| `issuing_authorization` | string |  | Set if the ReceivedDebit was created due to an [Issuing Authorization](https://stripe.com/docs/api#issuing_authorizations) object. |
| `issuing_transaction` | string |  | Set if the ReceivedDebit is also viewable as an [Issuing Dispute](https://stripe.com/docs/api#issuing_disputes) object. |
| `payout` | string |  | Set if the ReceivedDebit was created due to a [Payout](https://stripe.com/docs/api#payouts) object. |

