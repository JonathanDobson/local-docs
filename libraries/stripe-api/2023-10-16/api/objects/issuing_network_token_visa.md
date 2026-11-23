# Stripe API 2023-10-16 — `issuing_network_token_visa` object

| Field | Type | Required | Description |
|---|---|---|---|
| `card_reference_id` | string | yes | A unique reference ID from Visa to represent the card account number. |
| `token_reference_id` | string | yes | The network-unique identifier for the token. |
| `token_requestor_id` | string | yes | The ID of the entity requesting tokenization, specific to Visa. |
| `token_risk_score` | string |  | Degree of risk associated with the token between `01` and `99`, with higher number indicating higher risk. A `00` value indicates the token was not scored by Visa. |

