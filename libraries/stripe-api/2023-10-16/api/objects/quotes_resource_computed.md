# Stripe API 2023-10-16 — `quotes_resource_computed` object

Expandable fields (pass `expand[]=<field>`): `recurring`, `upfront`

| Field | Type | Required | Description |
|---|---|---|---|
| `recurring` | `quotes_resource_recurring` |  | The definitive totals and line items the customer will be charged on a recurring basis. Takes into account the line items with recurring prices and discounts with `duration=forever` coupons only. Defaults to `null` if no inputted line items with recurring prices. |
| `upfront` | `quotes_resource_upfront` | yes |  |

