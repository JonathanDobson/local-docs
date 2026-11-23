# Stripe API 2023-10-16 — `payment_links_resource_automatic_tax` object

Expandable fields (pass `expand[]=<field>`): `liability`

| Field | Type | Required | Description |
|---|---|---|---|
| `enabled` | boolean | yes | If `true`, tax will be calculated automatically using the customer's location. |
| `liability` | `connect_account_reference` |  | The account that's liable for tax. If set, the business address and tax registrations required to perform the tax calculation are loaded from this account. The tax transaction is returned in the report of the connected account. |

