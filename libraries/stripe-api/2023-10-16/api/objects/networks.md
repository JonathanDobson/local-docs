# Stripe API 2023-10-16 — `networks` object

| Field | Type | Required | Description |
|---|---|---|---|
| `available` | array of string | yes | All available networks for the card. |
| `preferred` | string |  | The preferred network for co-branded cards. Can be `cartes_bancaires`, `mastercard`, `visa` or `invalid_preference` if requested network is not valid for the card. |

