# Stripe API 2023-10-16 — `subscriptions_resource_pause_collection` object

The Pause Collection settings determine how we will pause collection for this subscription and for how long the subscription
should be paused.

| Field | Type | Required | Description |
|---|---|---|---|
| `behavior` | enum: `keep_as_draft`, `mark_uncollectible`, `void` | yes | The payment collection behavior for this subscription while paused. One of `keep_as_draft`, `mark_uncollectible`, or `void`. |
| `resumes_at` | timestamp (Unix seconds) |  | The time after which the subscription will resume collecting payments. |

