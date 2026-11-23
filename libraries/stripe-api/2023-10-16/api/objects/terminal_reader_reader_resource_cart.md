# Stripe API 2023-10-16 — `terminal_reader_reader_resource_cart` object

Represents a cart to be displayed on the reader

Expandable fields (pass `expand[]=<field>`): `line_items`

| Field | Type | Required | Description |
|---|---|---|---|
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `line_items` | array of `terminal_reader_reader_resource_line_item` | yes | List of line items in the cart. |
| `tax` | integer |  | Tax amount for the entire cart. A positive integer in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). |
| `total` | integer | yes | Total amount for the entire cart, including tax. A positive integer in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). |

