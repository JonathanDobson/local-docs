# Stripe API 2023-10-16 — `payment_method_details_us_bank_account` object

Expandable fields (pass `expand[]=<field>`): `mandate`

| Field | Type | Required | Description |
|---|---|---|---|
| `account_holder_type` | enum: `company`, `individual` |  | Account holder type: individual or company. |
| `account_type` | enum: `checking`, `savings` |  | Account type: checkings or savings. Defaults to checking if omitted. |
| `bank_name` | string |  | Name of the bank associated with the bank account. |
| `fingerprint` | string |  | Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same. |
| `last4` | string |  | Last four digits of the bank account number. |
| `mandate` | string or `mandate` |  | ID of the mandate used to make this payment. |
| `payment_reference` | string |  | Reference number to locate ACH payments with customer's bank. |
| `routing_number` | string |  | Routing number of the bank account. |

