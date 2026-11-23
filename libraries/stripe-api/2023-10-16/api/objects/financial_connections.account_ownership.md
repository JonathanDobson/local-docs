# Stripe API 2023-10-16 — `financial_connections.account_ownership` object

Describes a snapshot of the owners of an account at a particular point in time.

Expandable fields (pass `expand[]=<field>`): `owners`

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `id` | string | yes | Unique identifier for the object. |
| `object` | enum: `financial_connections.account_ownership` | yes | String representing the object's type. Objects of the same type share the same value. |
| `owners` | object | yes | A paginated list of owners for this account. |

