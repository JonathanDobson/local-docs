# Stripe API 2023-10-16 — `payment_method_details_acss_debit` object

| Field | Type | Required | Description |
|---|---|---|---|
| `bank_name` | string |  | Name of the bank associated with the bank account. |
| `fingerprint` | string |  | Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same. |
| `institution_number` | string |  | Institution number of the bank account |
| `last4` | string |  | Last four digits of the bank account number. |
| `mandate` | string |  | ID of the mandate used to make this payment. |
| `transit_number` | string |  | Transit number of the bank account. |

