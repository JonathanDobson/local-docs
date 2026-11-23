# Stripe API 2023-10-16 — `tax_product_resource_tax_settings_defaults` object

| Field | Type | Required | Description |
|---|---|---|---|
| `tax_behavior` | enum: `exclusive`, `inclusive`, `inferred_by_currency` |  | Default [tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#tax-behavior) used to specify whether the price is considered inclusive of taxes or exclusive of taxes. If the item's price has a tax behavior set, it will take precedence over the default tax behavior. |
| `tax_code` | string |  | Default [tax code](https://stripe.com/docs/tax/tax-categories) used to classify your products and prices. |

