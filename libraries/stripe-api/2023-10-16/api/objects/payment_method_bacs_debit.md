# Stripe API 2023-10-16 — `payment_method_bacs_debit` object

| Field | Type | Required | Description |
|---|---|---|---|
| `fingerprint` | string |  | Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same. |
| `last4` | string |  | Last four digits of the bank account number. |
| `sort_code` | string |  | Sort code of the bank account. (e.g., `10-20-30`) |

