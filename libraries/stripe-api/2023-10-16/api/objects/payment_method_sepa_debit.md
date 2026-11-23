# Stripe API 2023-10-16 — `payment_method_sepa_debit` object

Expandable fields (pass `expand[]=<field>`): `generated_from`

| Field | Type | Required | Description |
|---|---|---|---|
| `bank_code` | string |  | Bank code of bank associated with the bank account. |
| `branch_code` | string |  | Branch code of bank associated with the bank account. |
| `country` | string |  | Two-letter ISO code representing the country the bank account is located in. |
| `fingerprint` | string |  | Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same. |
| `generated_from` | `sepa_debit_generated_from` |  | Information about the object that generated this PaymentMethod. |
| `last4` | string |  | Last four characters of the IBAN. |

