# Stripe API 2023-10-16 — `bank_connections_resource_accountholder` object

Expandable fields (pass `expand[]=<field>`): `account`, `customer`

| Field | Type | Required | Description |
|---|---|---|---|
| `account` | string or `account` |  | The ID of the Stripe account this account belongs to. Should only be present if `account_holder.type` is `account`. |
| `customer` | string or `customer` |  | ID of the Stripe customer this account belongs to. Present if and only if `account_holder.type` is `customer`. |
| `type` | enum: `account`, `customer` | yes | Type of account holder that this account belongs to. |

