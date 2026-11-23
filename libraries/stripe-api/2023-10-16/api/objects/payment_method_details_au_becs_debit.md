# Stripe API 2023-10-16 — `payment_method_details_au_becs_debit` object

| Field | Type | Required | Description |
|---|---|---|---|
| `bsb_number` | string |  | Bank-State-Branch number of the bank account. |
| `fingerprint` | string |  | Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same. |
| `last4` | string |  | Last four digits of the bank account number. |
| `mandate` | string |  | ID of the mandate used to make this payment. |

