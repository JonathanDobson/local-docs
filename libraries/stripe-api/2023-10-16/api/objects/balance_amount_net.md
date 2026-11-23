# Stripe API 2023-10-16 — `balance_amount_net` object

Expandable fields (pass `expand[]=<field>`): `source_types`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | Balance amount. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `source_types` | `balance_amount_by_source_type` |  |  |

