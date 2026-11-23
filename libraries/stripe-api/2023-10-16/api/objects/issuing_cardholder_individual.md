# Stripe API 2023-10-16 — `issuing_cardholder_individual` object

Expandable fields (pass `expand[]=<field>`): `card_issuing`, `dob`, `verification`

| Field | Type | Required | Description |
|---|---|---|---|
| `card_issuing` | `issuing_cardholder_card_issuing` |  | Information related to the card_issuing program for this cardholder. |
| `dob` | `issuing_cardholder_individual_dob` |  | The date of birth of this cardholder. |
| `first_name` | string |  | The first name of this cardholder. Required before activating Cards. This field cannot contain any numbers, special characters (except periods, commas, hyphens, spaces and apostrophes) or non-latin letters. |
| `last_name` | string |  | The last name of this cardholder. Required before activating Cards. This field cannot contain any numbers, special characters (except periods, commas, hyphens, spaces and apostrophes) or non-latin letters. |
| `verification` | `issuing_cardholder_verification` |  | Government-issued ID document for this cardholder. |

