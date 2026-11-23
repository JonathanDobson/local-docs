# Stripe API 2023-10-16 — `payment_method_card_wallet` object

Expandable fields (pass `expand[]=<field>`): `amex_express_checkout`, `apple_pay`, `google_pay`, `link`, `masterpass`, `samsung_pay`, `visa_checkout`

| Field | Type | Required | Description |
|---|---|---|---|
| `amex_express_checkout` | `payment_method_card_wallet_amex_express_checkout` |  |  |
| `apple_pay` | `payment_method_card_wallet_apple_pay` |  |  |
| `dynamic_last4` | string |  | (For tokenized numbers only.) The last four digits of the device account number. |
| `google_pay` | `payment_method_card_wallet_google_pay` |  |  |
| `link` | `payment_method_card_wallet_link` |  |  |
| `masterpass` | `payment_method_card_wallet_masterpass` |  |  |
| `samsung_pay` | `payment_method_card_wallet_samsung_pay` |  |  |
| `type` | enum: `amex_express_checkout`, `apple_pay`, `google_pay`, `link`, `masterpass`, `samsung_pay`, `visa_checkout` | yes | The type of the card wallet, one of `amex_express_checkout`, `apple_pay`, `google_pay`, `masterpass`, `samsung_pay`, `visa_checkout`, or `link`. An additional hash is included on the Wallet subhash with a name matching this value. It contains additional information specific to the card wallet type. |
| `visa_checkout` | `payment_method_card_wallet_visa_checkout` |  |  |

