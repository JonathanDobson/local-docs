# Stripe API 2023-10-16 — `treasury_outbound_payments_resource_returned_status` object

Expandable fields (pass `expand[]=<field>`): `transaction`

| Field | Type | Required | Description |
|---|---|---|---|
| `code` | enum: `account_closed`, `account_frozen`, `bank_account_restricted`, `bank_ownership_changed`, `declined`, `incorrect_account_holder_name`, `invalid_account_number`, `invalid_currency`, `no_account`, `other` | yes | Reason for the return. |
| `transaction` | string or `treasury.transaction` | yes | The Transaction associated with this object. |

