# Stripe API 2023-10-16 — `cancellation_details` object

| Field | Type | Required | Description |
|---|---|---|---|
| `comment` | string |  | Additional comments about why the user canceled the subscription, if the subscription was canceled explicitly by the user. |
| `feedback` | enum: `customer_service`, `low_quality`, `missing_features`, `other`, `switched_service`, `too_complex`, `too_expensive`, `unused` |  | The customer submitted reason for why they canceled, if the subscription was canceled explicitly by the user. |
| `reason` | enum: `cancellation_requested`, `payment_disputed`, `payment_failed` |  | Why this subscription was canceled. |

