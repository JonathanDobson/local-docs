# Stripe API 2023-10-16 — `connect_account_reference` object

Expandable fields (pass `expand[]=<field>`): `account`

| Field | Type | Required | Description |
|---|---|---|---|
| `account` | string or `account` |  | The connected account being referenced when `type` is `account`. |
| `type` | enum: `account`, `self` | yes | Type of the account referenced. |

