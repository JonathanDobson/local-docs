# Stripe API 2023-10-16 — `tax_i_ds_owner` object

Expandable fields (pass `expand[]=<field>`): `account`, `application`, `customer`

| Field | Type | Required | Description |
|---|---|---|---|
| `account` | string or `account` |  | The account being referenced when `type` is `account`. |
| `application` | string or `application` |  | The Connect Application being referenced when `type` is `application`. |
| `customer` | string or `customer` |  | The customer being referenced when `type` is `customer`. |
| `type` | enum: `account`, `application`, `customer`, `self` | yes | Type of owner referenced. |

