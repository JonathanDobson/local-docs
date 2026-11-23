# Stripe API 2023-10-16 — `payment_method_details_swish` object

| Field | Type | Required | Description |
|---|---|---|---|
| `fingerprint` | string |  | Uniquely identifies the payer's Swish account. You can use this attribute to check whether two Swish transactions were paid for by the same payer |
| `payment_reference` | string |  | Payer bank reference number for the payment |
| `verified_phone_last4` | string |  | The last four digits of the Swish account phone number |

