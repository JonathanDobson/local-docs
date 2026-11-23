# Stripe API 2023-10-16 — `issuing_dispute_evidence` object

Expandable fields (pass `expand[]=<field>`): `canceled`, `duplicate`, `fraudulent`, `merchandise_not_as_described`, `not_received`, `other`, `service_not_as_described`

| Field | Type | Required | Description |
|---|---|---|---|
| `canceled` | `issuing_dispute_canceled_evidence` |  |  |
| `duplicate` | `issuing_dispute_duplicate_evidence` |  |  |
| `fraudulent` | `issuing_dispute_fraudulent_evidence` |  |  |
| `merchandise_not_as_described` | `issuing_dispute_merchandise_not_as_described_evidence` |  |  |
| `not_received` | `issuing_dispute_not_received_evidence` |  |  |
| `other` | `issuing_dispute_other_evidence` |  |  |
| `reason` | enum: `canceled`, `duplicate`, `fraudulent`, `merchandise_not_as_described`, `not_received`, `other`, `service_not_as_described` | yes | The reason for filing the dispute. Its value will match the field containing the evidence. |
| `service_not_as_described` | `issuing_dispute_service_not_as_described_evidence` |  |  |

