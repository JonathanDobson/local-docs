# Stripe API 2023-10-16 — `account_monthly_estimated_revenue` object

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal). |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |

