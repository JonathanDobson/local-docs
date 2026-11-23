# Stripe API 2023-10-16 — `invoice_transfer_data` object

Expandable fields (pass `expand[]=<field>`): `destination`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer |  | The amount in cents (or local equivalent) that will be transferred to the destination account when the invoice is paid. By default, the entire amount is transferred to the destination. |
| `destination` | string or `account` | yes | The account where funds from the payment will be transferred to upon payment success. |

