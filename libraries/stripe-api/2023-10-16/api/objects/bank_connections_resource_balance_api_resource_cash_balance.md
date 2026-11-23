# Stripe API 2023-10-16 — `bank_connections_resource_balance_api_resource_cash_balance` object

| Field | Type | Required | Description |
|---|---|---|---|
| `available` | map (key → value) |  | The funds available to the account holder. Typically this is the current balance less any holds.<br>Each key is a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase.<br>Each value is a integer amount. A positive amount indicates money owed to the account holder. A negative amount indicates money owed by the account holder. |

