# Stripe API 2023-10-16 — `issuing_authorization_authentication_exemption` object

| Field | Type | Required | Description |
|---|---|---|---|
| `claimed_by` | enum: `acquirer`, `issuer` | yes | The entity that requested the exemption, either the acquiring merchant or the Issuing user. |
| `type` | enum: `low_value_transaction`, `transaction_risk_analysis`, `unknown` | yes | The specific exemption claimed for this authorization. |

