# Stripe API 2023-10-16 — `customer_tax` object

Expandable fields (pass `expand[]=<field>`): `location`

| Field | Type | Required | Description |
|---|---|---|---|
| `automatic_tax` | enum: `failed`, `not_collecting`, `supported`, `unrecognized_location` | yes | Surfaces if automatic tax computation is possible given the current customer location information. |
| `ip_address` | string |  | A recent IP address of the customer used for tax reporting and tax location inference. |
| `location` | `customer_tax_location` |  | The customer's location as identified by Stripe Tax. |

