# Stripe API 2023-10-16 — `subscription_details_data` object

| Field | Type | Required | Description |
|---|---|---|---|
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) defined as subscription metadata when an invoice is created. Becomes an immutable snapshot of the subscription metadata at the time of invoice finalization.  *Note: This attribute is populated only for invoices created on or after June 29, 2023.* |

