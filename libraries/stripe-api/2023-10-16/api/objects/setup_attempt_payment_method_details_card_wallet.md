# Stripe API 2023-10-16 — `setup_attempt_payment_method_details_card_wallet` object

Expandable fields (pass `expand[]=<field>`): `apple_pay`, `google_pay`

| Field | Type | Required | Description |
|---|---|---|---|
| `apple_pay` | `payment_method_details_card_wallet_apple_pay` |  |  |
| `google_pay` | `payment_method_details_card_wallet_google_pay` |  |  |
| `type` | enum: `apple_pay`, `google_pay`, `link` | yes | The type of the card wallet, one of `apple_pay`, `google_pay`, or `link`. An additional hash is included on the Wallet subhash with a name matching this value. It contains additional information specific to the card wallet type. |

