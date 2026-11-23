# Stripe API 2023-10-16 — `gelato_verified_outputs` object

Expandable fields (pass `expand[]=<field>`): `address`, `dob`

| Field | Type | Required | Description |
|---|---|---|---|
| `address` | `address` |  | The user's verified address. |
| `dob` | `gelato_data_verified_outputs_date` |  | The user’s verified date of birth. |
| `email` | string |  | The user's verified email address |
| `first_name` | string |  | The user's verified first name. |
| `id_number` | string |  | The user's verified id number. |
| `id_number_type` | enum: `br_cpf`, `sg_nric`, `us_ssn` |  | The user's verified id number type. |
| `last_name` | string |  | The user's verified last name. |
| `phone` | string |  | The user's verified phone number |

