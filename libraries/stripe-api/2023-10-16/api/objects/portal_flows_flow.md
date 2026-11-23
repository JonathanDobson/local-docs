# Stripe API 2023-10-16 — `portal_flows_flow` object

Expandable fields (pass `expand[]=<field>`): `after_completion`, `subscription_cancel`, `subscription_update`, `subscription_update_confirm`

| Field | Type | Required | Description |
|---|---|---|---|
| `after_completion` | `portal_flows_flow_after_completion` | yes |  |
| `subscription_cancel` | `portal_flows_flow_subscription_cancel` |  | Configuration when `flow.type=subscription_cancel`. |
| `subscription_update` | `portal_flows_flow_subscription_update` |  | Configuration when `flow.type=subscription_update`. |
| `subscription_update_confirm` | `portal_flows_flow_subscription_update_confirm` |  | Configuration when `flow.type=subscription_update_confirm`. |
| `type` | enum: `payment_method_update`, `subscription_cancel`, `subscription_update`, `subscription_update_confirm` | yes | Type of flow that the customer will go through. |

