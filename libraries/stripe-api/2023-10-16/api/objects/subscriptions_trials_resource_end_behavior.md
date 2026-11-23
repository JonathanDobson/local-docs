# Stripe API 2023-10-16 — `subscriptions_trials_resource_end_behavior` object

Defines how a subscription behaves when a free trial ends.

| Field | Type | Required | Description |
|---|---|---|---|
| `missing_payment_method` | enum: `cancel`, `create_invoice`, `pause` | yes | Indicates how the subscription should change when the trial ends if the user did not provide a payment method. |

