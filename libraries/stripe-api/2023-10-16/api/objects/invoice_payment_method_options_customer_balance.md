# Stripe API 2023-10-16 — `invoice_payment_method_options_customer_balance` object

Expandable fields (pass `expand[]=<field>`): `bank_transfer`

| Field | Type | Required | Description |
|---|---|---|---|
| `bank_transfer` | `invoice_payment_method_options_customer_balance_bank_transfer` |  |  |
| `funding_type` | enum: `bank_transfer` |  | The funding method type to be used when there are not enough funds in the customer balance. Permitted values include: `bank_transfer`. |

