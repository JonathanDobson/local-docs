# Stripe API 2023-10-16 — `automatic_tax` object

Expandable fields (pass `expand[]=<field>`): `liability`

| Field | Type | Required | Description |
|---|---|---|---|
| `enabled` | boolean | yes | Whether Stripe automatically computes tax on this invoice. Note that incompatible invoice items (invoice items with manually specified [tax rates](https://stripe.com/docs/api/tax_rates), negative amounts, or `tax_behavior=unspecified`) cannot be added to automatic tax invoices. |
| `liability` | `connect_account_reference` |  | The account that's liable for tax. If set, the business address and tax registrations required to perform the tax calculation are loaded from this account. The tax transaction is returned in the report of the connected account. |
| `status` | enum: `complete`, `failed`, `requires_location_inputs` |  | The status of the most recent automated tax calculation for this invoice. |

