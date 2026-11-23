# Stripe API 2023-10-16 — `gelato_id_number_report` object

Result from an id_number check

Expandable fields (pass `expand[]=<field>`): `dob`, `error`

| Field | Type | Required | Description |
|---|---|---|---|
| `dob` | `gelato_data_id_number_report_date` |  | Date of birth. |
| `error` | `gelato_id_number_report_error` |  | Details on the verification error. Present when status is `unverified`. |
| `first_name` | string |  | First name. |
| `id_number` | string |  | ID number. When `id_number_type` is `us_ssn`, only the last 4 digits are present. |
| `id_number_type` | enum: `br_cpf`, `sg_nric`, `us_ssn` |  | Type of ID number. |
| `last_name` | string |  | Last name. |
| `status` | enum: `unverified`, `verified` | yes | Status of this `id_number` check. |

