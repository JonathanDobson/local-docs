# Stripe API 2023-10-16 — `payment_links_resource_transfer_data` object

Expandable fields (pass `expand[]=<field>`): `destination`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer |  | The amount in cents (or local equivalent) that will be transferred to the destination account. By default, the entire amount is transferred to the destination. |
| `destination` | string or `account` | yes | The connected account receiving the transfer. |

