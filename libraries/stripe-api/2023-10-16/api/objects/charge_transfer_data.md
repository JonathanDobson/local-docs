# Stripe API 2023-10-16 — `charge_transfer_data` object

Expandable fields (pass `expand[]=<field>`): `destination`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer |  | The amount transferred to the destination account, if specified. By default, the entire charge amount is transferred to the destination account. |
| `destination` | string or `account` | yes | ID of an existing, connected Stripe account to transfer funds to if `transfer_data` was specified in the charge request. |

