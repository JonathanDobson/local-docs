# Stripe API 2023-10-16 — `issuing_network_token_mastercard` object

| Field | Type | Required | Description |
|---|---|---|---|
| `card_reference_id` | string |  | A unique reference ID from MasterCard to represent the card account number. |
| `token_reference_id` | string | yes | The network-unique identifier for the token. |
| `token_requestor_id` | string | yes | The ID of the entity requesting tokenization, specific to MasterCard. |
| `token_requestor_name` | string |  | The name of the entity requesting tokenization, if known. This is directly provided from MasterCard. |

