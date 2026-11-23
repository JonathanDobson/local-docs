# Stripe API 2023-10-16 — `payment_method_details_sepa_debit` object

| Field | Type | Required | Description |
|---|---|---|---|
| `bank_code` | string |  | Bank code of bank associated with the bank account. |
| `branch_code` | string |  | Branch code of bank associated with the bank account. |
| `country` | string |  | Two-letter ISO code representing the country the bank account is located in. |
| `fingerprint` | string |  | Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same. |
| `last4` | string |  | Last four characters of the IBAN. |
| `mandate` | string |  | Find the ID of the mandate used for this payment under the [payment_method_details.sepa_debit.mandate](https://stripe.com/docs/api/charges/object#charge_object-payment_method_details-sepa_debit-mandate) property on the Charge. Use this mandate ID to [retrieve the Mandate](https://stripe.com/docs/api/mandates/retrieve). |

