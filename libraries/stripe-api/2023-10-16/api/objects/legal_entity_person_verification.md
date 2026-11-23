# Stripe API 2023-10-16 — `legal_entity_person_verification` object

Expandable fields (pass `expand[]=<field>`): `additional_document`, `document`

| Field | Type | Required | Description |
|---|---|---|---|
| `additional_document` | `legal_entity_person_verification_document` |  | A document showing address, either a passport, local ID card, or utility bill from a well-known utility company. |
| `details` | string |  | A user-displayable string describing the verification state for the person. For example, this may say "Provided identity information could not be verified". |
| `details_code` | string |  | One of `document_address_mismatch`, `document_dob_mismatch`, `document_duplicate_type`, `document_id_number_mismatch`, `document_name_mismatch`, `document_nationality_mismatch`, `failed_keyed_identity`, or `failed_other`. A machine-readable code specifying the verification state for the person. |
| `document` | `legal_entity_person_verification_document` |  |  |
| `status` | string | yes | The state of verification for the person. Possible values are `unverified`, `pending`, or `verified`. |

