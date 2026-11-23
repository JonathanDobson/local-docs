# Stripe API 2023-10-16 — `issuing_card_wallets` object

Expandable fields (pass `expand[]=<field>`): `apple_pay`, `google_pay`

| Field | Type | Required | Description |
|---|---|---|---|
| `apple_pay` | `issuing_card_apple_pay` | yes |  |
| `google_pay` | `issuing_card_google_pay` | yes |  |
| `primary_account_identifier` | string |  | Unique identifier for a card used with digital wallets |

