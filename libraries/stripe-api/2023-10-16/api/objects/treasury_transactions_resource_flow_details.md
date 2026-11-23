# Stripe API 2023-10-16 — `treasury_transactions_resource_flow_details` object

Expandable fields (pass `expand[]=<field>`): `credit_reversal`, `debit_reversal`, `inbound_transfer`, `issuing_authorization`, `outbound_payment`, `outbound_transfer`, `received_credit`, `received_debit`

| Field | Type | Required | Description |
|---|---|---|---|
| `credit_reversal` | `treasury.credit_reversal` |  |  |
| `debit_reversal` | `treasury.debit_reversal` |  |  |
| `inbound_transfer` | `treasury.inbound_transfer` |  |  |
| `issuing_authorization` | `issuing.authorization` |  |  |
| `outbound_payment` | `treasury.outbound_payment` |  |  |
| `outbound_transfer` | `treasury.outbound_transfer` |  |  |
| `received_credit` | `treasury.received_credit` |  |  |
| `received_debit` | `treasury.received_debit` |  |  |
| `type` | enum: `credit_reversal`, `debit_reversal`, `inbound_transfer`, `issuing_authorization`, `other`, `outbound_payment`, `outbound_transfer`, `received_credit`, `received_debit` | yes | Type of the flow that created the Transaction. Set to the same value as `flow_type`. |

