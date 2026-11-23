# Stripe API 2023-10-16 — `issuing_network_token_network_data` object

Expandable fields (pass `expand[]=<field>`): `device`, `mastercard`, `visa`, `wallet_provider`

| Field | Type | Required | Description |
|---|---|---|---|
| `device` | `issuing_network_token_device` |  |  |
| `mastercard` | `issuing_network_token_mastercard` |  |  |
| `type` | enum: `mastercard`, `visa` | yes | The network that the token is associated with. An additional hash is included with a name matching this value, containing tokenization data specific to the card network. |
| `visa` | `issuing_network_token_visa` |  |  |
| `wallet_provider` | `issuing_network_token_wallet_provider` |  |  |

