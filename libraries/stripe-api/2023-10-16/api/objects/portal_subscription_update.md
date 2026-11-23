# Stripe API 2023-10-16 — `portal_subscription_update` object

Expandable fields (pass `expand[]=<field>`): `products`

| Field | Type | Required | Description |
|---|---|---|---|
| `default_allowed_updates` | array of enum: `price`, `promotion_code`, `quantity` | yes | The types of subscription updates that are supported for items listed in the `products` attribute. When empty, subscriptions are not updateable. |
| `enabled` | boolean | yes | Whether the feature is enabled. |
| `products` | array of `portal_subscription_update_product` |  | The list of up to 10 products that support subscription updates. |
| `proration_behavior` | enum: `always_invoice`, `create_prorations`, `none` | yes | Determines how to handle prorations resulting from subscription updates. Valid values are `none`, `create_prorations`, and `always_invoice`. Defaults to a value of `none` if you don't set it during creation. |

