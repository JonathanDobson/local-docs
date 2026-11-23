# Stripe API 2023-10-16 — `bank_connections_resource_balance` object

Expandable fields (pass `expand[]=<field>`): `cash`, `credit`

| Field | Type | Required | Description |
|---|---|---|---|
| `as_of` | timestamp (Unix seconds) | yes | The time that the external institution calculated this balance. Measured in seconds since the Unix epoch. |
| `cash` | `bank_connections_resource_balance_api_resource_cash_balance` |  |  |
| `credit` | `bank_connections_resource_balance_api_resource_credit_balance` |  |  |
| `current` | map (key → value) | yes | The balances owed to (or by) the account holder.<br>Each key is a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase.<br>Each value is a integer amount. A positive amount indicates money owed to the account holder. A negative amount indicates money owed by the account holder. |
| `type` | enum: `cash`, `credit` | yes | The `type` of the balance. An additional hash is included on the balance with a name matching this value. |

