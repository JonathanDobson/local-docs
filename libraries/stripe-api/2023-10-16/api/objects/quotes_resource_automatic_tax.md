# Stripe API 2023-10-16 — `quotes_resource_automatic_tax` object

Expandable fields (pass `expand[]=<field>`): `liability`

| Field | Type | Required | Description |
|---|---|---|---|
| `enabled` | boolean | yes | Automatically calculate taxes |
| `liability` | `connect_account_reference` |  | The account that's liable for tax. If set, the business address and tax registrations required to perform the tax calculation are loaded from this account. The tax transaction is returned in the report of the connected account. |
| `status` | enum: `complete`, `failed`, `requires_location_inputs` |  | The status of the most recent automated tax calculation for this quote. |

