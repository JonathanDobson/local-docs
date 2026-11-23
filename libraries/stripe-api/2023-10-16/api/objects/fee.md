# Stripe API 2023-10-16 — `fee` object

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | Amount of the fee, in cents. |
| `application` | string |  | ID of the Connect application that earned the fee. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. |
| `type` | string | yes | Type of the fee, one of: `application_fee`, `payment_method_passthrough_fee`, `stripe_fee` or `tax`. |

