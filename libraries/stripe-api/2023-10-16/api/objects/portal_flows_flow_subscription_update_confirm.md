# Stripe API 2023-10-16 — `portal_flows_flow_subscription_update_confirm` object

Expandable fields (pass `expand[]=<field>`): `discounts`, `items`

| Field | Type | Required | Description |
|---|---|---|---|
| `discounts` | array of `portal_flows_subscription_update_confirm_discount` |  | The coupon or promotion code to apply to this subscription update. Currently, only up to one may be specified. |
| `items` | array of `portal_flows_subscription_update_confirm_item` | yes | The [subscription item](https://stripe.com/docs/api/subscription_items) to be updated through this flow. Currently, only up to one may be specified and subscriptions with multiple items are not updatable. |
| `subscription` | string | yes | The ID of the subscription to be updated. |

