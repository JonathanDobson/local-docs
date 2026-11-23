# Stripe API 2023-10-16 — `shipping_rate_fixed_amount` object

Expandable fields (pass `expand[]=<field>`): `currency_options`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | A non-negative integer in cents representing how much to charge. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `currency_options` | map (key → value) |  | Shipping rates defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies). |

