# Stripe API 2023-10-16 — `payment_method_options_customer_balance_bank_transfer` object

Expandable fields (pass `expand[]=<field>`): `eu_bank_transfer`

| Field | Type | Required | Description |
|---|---|---|---|
| `eu_bank_transfer` | `payment_method_options_customer_balance_eu_bank_account` |  |  |
| `requested_address_types` | array of enum: `aba`, `iban`, `sepa`, `sort_code`, `spei`, `swift`, `zengin` |  | List of address types that should be returned in the financial_addresses response. If not specified, all valid types will be returned.<br>Permitted values include: `sort_code`, `zengin`, `iban`, or `spei`. |
| `type` | enum: `eu_bank_transfer`, `gb_bank_transfer`, `jp_bank_transfer`, `mx_bank_transfer`, `us_bank_transfer` |  | The bank transfer type that this PaymentIntent is allowed to use for funding Permitted values include: `eu_bank_transfer`, `gb_bank_transfer`, `jp_bank_transfer`, `mx_bank_transfer`, or `us_bank_transfer`. |

