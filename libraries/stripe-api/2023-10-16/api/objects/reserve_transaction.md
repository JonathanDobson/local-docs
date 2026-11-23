# Stripe API 2023-10-16 — `reserve_transaction` object

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes |  |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. |
| `id` | string | yes | Unique identifier for the object. |
| `object` | enum: `reserve_transaction` | yes | String representing the object's type. Objects of the same type share the same value. |

