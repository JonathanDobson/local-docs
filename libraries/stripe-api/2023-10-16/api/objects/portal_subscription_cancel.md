# Stripe API 2023-10-16 — `portal_subscription_cancel` object

Expandable fields (pass `expand[]=<field>`): `cancellation_reason`

| Field | Type | Required | Description |
|---|---|---|---|
| `cancellation_reason` | `portal_subscription_cancellation_reason` | yes |  |
| `enabled` | boolean | yes | Whether the feature is enabled. |
| `mode` | enum: `at_period_end`, `immediately` | yes | Whether to cancel subscriptions immediately or at the end of the billing period. |
| `proration_behavior` | enum: `always_invoice`, `create_prorations`, `none` | yes | Whether to create prorations when canceling subscriptions. Possible values are `none` and `create_prorations`. |

