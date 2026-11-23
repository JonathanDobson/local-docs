# Stripe API 2023-10-16 — `payment_links_resource_completed_sessions` object

| Field | Type | Required | Description |
|---|---|---|---|
| `count` | integer | yes | The current number of checkout sessions that have been completed on the payment link which count towards the `completed_sessions` restriction to be met. |
| `limit` | integer | yes | The maximum number of checkout sessions that can be completed for the `completed_sessions` restriction to be met. |

