# Stripe API 2023-10-16 — `treasury_received_credits_resource_linked_flows` object

Expandable fields (pass `expand[]=<field>`): `source_flow_details`

| Field | Type | Required | Description |
|---|---|---|---|
| `credit_reversal` | string |  | The CreditReversal created as a result of this ReceivedCredit being reversed. |
| `issuing_authorization` | string |  | Set if the ReceivedCredit was created due to an [Issuing Authorization](https://stripe.com/docs/api#issuing_authorizations) object. |
| `issuing_transaction` | string |  | Set if the ReceivedCredit is also viewable as an [Issuing transaction](https://stripe.com/docs/api#issuing_transactions) object. |
| `source_flow` | string |  | ID of the source flow. Set if `network` is `stripe` and the source flow is visible to the user. Examples of source flows include OutboundPayments, payouts, or CreditReversals. |
| `source_flow_details` | `treasury_received_credits_resource_source_flows_details` |  | The expandable object of the source flow. |
| `source_flow_type` | string |  | The type of flow that originated the ReceivedCredit (for example, `outbound_payment`). |

