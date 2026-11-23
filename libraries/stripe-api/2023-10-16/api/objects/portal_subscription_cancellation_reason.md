# Stripe API 2023-10-16 — `portal_subscription_cancellation_reason` object

| Field | Type | Required | Description |
|---|---|---|---|
| `enabled` | boolean | yes | Whether the feature is enabled. |
| `options` | array of enum: `customer_service`, `low_quality`, `missing_features`, `other`, `switched_service`, `too_complex`, `too_expensive`, `unused` | yes | Which cancellation reasons will be given as options to the customer. |

