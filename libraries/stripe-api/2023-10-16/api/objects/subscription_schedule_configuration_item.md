# Stripe API 2023-10-16 — `subscription_schedule_configuration_item` object

A phase item describes the price and quantity of a phase.

Expandable fields (pass `expand[]=<field>`): `billing_thresholds`, `discounts`, `price`, `tax_rates`

| Field | Type | Required | Description |
|---|---|---|---|
| `billing_thresholds` | `subscription_item_billing_thresholds` |  | Define thresholds at which an invoice will be sent, and the related subscription advanced to a new billing period |
| `discounts` | array of `discounts_resource_stackable_discount` | yes | The discounts applied to the subscription item. Subscription item discounts are applied before subscription discounts. Use `expand[]=discounts` to expand each discount. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an item. Metadata on this item will update the underlying subscription item's `metadata` when the phase is entered. |
| `price` | string or `price` or `deleted_price` | yes | ID of the price to which the customer should be subscribed. |
| `quantity` | integer |  | Quantity of the plan to which the customer should be subscribed. |
| `tax_rates` | array of `tax_rate` |  | The tax rates which apply to this `phase_item`. When set, the `default_tax_rates` on the phase do not apply to this `phase_item`. |

