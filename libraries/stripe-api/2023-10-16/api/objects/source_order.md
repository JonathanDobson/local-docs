# Stripe API 2023-10-16 — `source_order` object

Expandable fields (pass `expand[]=<field>`): `items`, `shipping`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | A positive integer in the smallest currency unit (that is, 100 cents for $1.00, or 1 for ¥1, Japanese Yen being a zero-decimal currency) representing the total amount for the order. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `email` | string |  | The email address of the customer placing the order. |
| `items` | array of `source_order_item` |  | List of items constituting the order. |
| `shipping` | `shipping` |  |  |

