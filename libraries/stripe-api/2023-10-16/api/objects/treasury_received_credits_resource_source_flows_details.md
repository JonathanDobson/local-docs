# Stripe API 2023-10-16 — `treasury_received_credits_resource_source_flows_details` object

Expandable fields (pass `expand[]=<field>`): `credit_reversal`, `outbound_payment`, `payout`

| Field | Type | Required | Description |
|---|---|---|---|
| `credit_reversal` | `treasury.credit_reversal` |  |  |
| `outbound_payment` | `treasury.outbound_payment` |  |  |
| `payout` | `payout` |  |  |
| `type` | enum: `credit_reversal`, `other`, `outbound_payment`, `payout` | yes | The type of the source flow that originated the ReceivedCredit. |

