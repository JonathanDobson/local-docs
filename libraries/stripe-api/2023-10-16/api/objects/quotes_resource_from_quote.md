# Stripe API 2023-10-16 — `quotes_resource_from_quote` object

Expandable fields (pass `expand[]=<field>`): `quote`

| Field | Type | Required | Description |
|---|---|---|---|
| `is_revision` | boolean | yes | Whether this quote is a revision of a different quote. |
| `quote` | string or `quote` | yes | The quote that was cloned. |

