# Stripe API 2023-10-16 — `financial_connections.account_owner` object

Describes an owner of an account.

| Field | Type | Required | Description |
|---|---|---|---|
| `email` | string |  | The email address of the owner. |
| `id` | string | yes | Unique identifier for the object. |
| `name` | string | yes | The full name of the owner. |
| `object` | enum: `financial_connections.account_owner` | yes | String representing the object's type. Objects of the same type share the same value. |
| `ownership` | string | yes | The ownership object that this owner belongs to. |
| `phone` | string |  | The raw phone number of the owner. |
| `raw_address` | string |  | The raw physical address of the owner. |
| `refreshed_at` | timestamp (Unix seconds) |  | The timestamp of the refresh that updated this owner. |

