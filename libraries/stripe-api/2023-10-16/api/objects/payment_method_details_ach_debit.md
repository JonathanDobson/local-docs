# Stripe API 2023-10-16 — `payment_method_details_ach_debit` object

| Field | Type | Required | Description |
|---|---|---|---|
| `account_holder_type` | enum: `company`, `individual` |  | Type of entity that holds the account. This can be either `individual` or `company`. |
| `bank_name` | string |  | Name of the bank associated with the bank account. |
| `country` | string |  | Two-letter ISO code representing the country the bank account is located in. |
| `fingerprint` | string |  | Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same. |
| `last4` | string |  | Last four digits of the bank account number. |
| `routing_number` | string |  | Routing transit number of the bank account. |

