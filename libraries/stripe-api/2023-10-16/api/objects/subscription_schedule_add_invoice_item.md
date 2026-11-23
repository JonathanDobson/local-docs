# Stripe API 2023-10-16 — `subscription_schedule_add_invoice_item` object

An Add Invoice Item describes the prices and quantities that will be added as pending invoice items when entering a phase.

Expandable fields (pass `expand[]=<field>`): `discounts`, `price`, `tax_rates`

| Field | Type | Required | Description |
|---|---|---|---|
| `discounts` | array of `discounts_resource_stackable_discount` | yes | The stackable discounts that will be applied to the item. |
| `price` | string or `price` or `deleted_price` | yes | ID of the price used to generate the invoice item. |
| `quantity` | integer |  | The quantity of the invoice item. |
| `tax_rates` | array of `tax_rate` |  | The tax rates which apply to the item. When set, the `default_tax_rates` do not apply to this item. |

