# Stripe API 2023-10-16 — `payment_method_us_bank_account` object

Expandable fields (pass `expand[]=<field>`): `networks`, `status_details`

| Field | Type | Required | Description |
|---|---|---|---|
| `account_holder_type` | enum: `company`, `individual` |  | Account holder type: individual or company. |
| `account_type` | enum: `checking`, `savings` |  | Account type: checkings or savings. Defaults to checking if omitted. |
| `bank_name` | string |  | The name of the bank. |
| `financial_connections_account` | string |  | The ID of the Financial Connections Account used to create the payment method. |
| `fingerprint` | string |  | Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same. |
| `last4` | string |  | Last four digits of the bank account number. |
| `networks` | `us_bank_account_networks` |  | Contains information about US bank account networks that can be used. |
| `routing_number` | string |  | Routing number of the bank account. |
| `status_details` | `payment_method_us_bank_account_status_details` |  | Contains information about the future reusability of this PaymentMethod. |

