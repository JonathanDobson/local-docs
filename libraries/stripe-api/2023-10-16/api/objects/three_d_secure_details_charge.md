# Stripe API 2023-10-16 — `three_d_secure_details_charge` object

| Field | Type | Required | Description |
|---|---|---|---|
| `authentication_flow` | enum: `challenge`, `frictionless` |  | For authenticated transactions: how the customer was authenticated by the issuing bank. |
| `electronic_commerce_indicator` | enum: `01`, `02`, `05`, `06`, `07` |  | The Electronic Commerce Indicator (ECI). A protocol-level field indicating what degree of authentication was performed. |
| `exemption_indicator` | enum: `low_risk`, `none` |  | The exemption requested via 3DS and accepted by the issuer at authentication time. |
| `exemption_indicator_applied` | boolean |  | Whether Stripe requested the value of `exemption_indicator` in the transaction. This will depend on the outcome of Stripe's internal risk assessment. |
| `result` | enum: `attempt_acknowledged`, `authenticated`, `exempted`, `failed`, `not_supported`, `processing_error` |  | Indicates the outcome of 3D Secure authentication. |
| `result_reason` | enum: `abandoned`, `bypassed`, `canceled`, `card_not_enrolled`, `network_not_supported`, `protocol_error`, `rejected` |  | Additional information about why 3D Secure succeeded or failed based on the `result`. |
| `transaction_id` | string |  | The 3D Secure 1 XID or 3D Secure 2 Directory Server Transaction ID (dsTransId) for this payment. |
| `version` | enum: `1.0.2`, `2.1.0`, `2.2.0` |  | The version of 3D Secure that was used. |

