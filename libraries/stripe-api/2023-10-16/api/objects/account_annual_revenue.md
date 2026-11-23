# Stripe API 2023-10-16 — `account_annual_revenue` object

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer |  | A non-negative integer representing the amount in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal). |
| `currency` | string |  | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `fiscal_year_end` | string |  | The close-out date of the preceding fiscal year in ISO 8601 format. E.g. 2023-12-31 for the 31st of December, 2023. |

