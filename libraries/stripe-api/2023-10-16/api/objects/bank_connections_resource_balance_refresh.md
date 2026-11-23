# Stripe API 2023-10-16 — `bank_connections_resource_balance_refresh` object

| Field | Type | Required | Description |
|---|---|---|---|
| `last_attempted_at` | timestamp (Unix seconds) | yes | The time at which the last refresh attempt was initiated. Measured in seconds since the Unix epoch. |
| `next_refresh_available_at` | timestamp (Unix seconds) |  | Time at which the next balance refresh can be initiated. This value will be `null` when `status` is `pending`. Measured in seconds since the Unix epoch. |
| `status` | enum: `failed`, `pending`, `succeeded` | yes | The status of the last refresh attempt. |

