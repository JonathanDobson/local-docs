# Stripe API 2023-10-16 — `issuing_authorization_pending_request` object

Expandable fields (pass `expand[]=<field>`): `amount_details`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | The additional amount Stripe will hold if the authorization is approved, in the card's [currency](https://stripe.com/docs/api#issuing_authorization_object-pending-request-currency) and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). |
| `amount_details` | `issuing_authorization_amount_details` |  | Detailed breakdown of amount components. These amounts are denominated in `currency` and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `is_amount_controllable` | boolean | yes | If set `true`, you may provide [amount](https://stripe.com/docs/api/issuing/authorizations/approve#approve_issuing_authorization-amount) to control how much to hold for the authorization. |
| `merchant_amount` | integer | yes | The amount the merchant is requesting to be authorized in the `merchant_currency`. The amount is in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). |
| `merchant_currency` | string | yes | The local currency the merchant is requesting to authorize. |
| `network_risk_score` | integer |  | The card network's estimate of the likelihood that an authorization is fraudulent. Takes on values between 1 and 99. |

