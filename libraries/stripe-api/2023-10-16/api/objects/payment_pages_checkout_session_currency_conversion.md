# Stripe API 2023-10-16 — `payment_pages_checkout_session_currency_conversion` object

| Field | Type | Required | Description |
|---|---|---|---|
| `amount_subtotal` | integer | yes | Total of all items in source currency before discounts or taxes are applied. |
| `amount_total` | integer | yes | Total of all items in source currency after discounts and taxes are applied. |
| `fx_rate` | string | yes | Exchange rate used to convert source currency amounts to customer currency amounts |
| `source_currency` | string | yes | Creation currency of the CheckoutSession before localization |

