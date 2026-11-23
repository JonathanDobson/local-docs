# Stripe API 2023-10-16 — `invoices_resource_from_invoice` object

Expandable fields (pass `expand[]=<field>`): `invoice`

| Field | Type | Required | Description |
|---|---|---|---|
| `action` | string | yes | The relation between this invoice and the cloned invoice |
| `invoice` | string or `invoice` | yes | The invoice that was cloned. |

