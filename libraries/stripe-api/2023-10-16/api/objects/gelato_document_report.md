# Stripe API 2023-10-16 — `gelato_document_report` object

Result from a document check

Expandable fields (pass `expand[]=<field>`): `address`, `dob`, `error`, `expiration_date`, `issued_date`

| Field | Type | Required | Description |
|---|---|---|---|
| `address` | `address` |  | Address as it appears in the document. |
| `dob` | `gelato_data_document_report_date_of_birth` |  | Date of birth as it appears in the document. |
| `error` | `gelato_document_report_error` |  | Details on the verification error. Present when status is `unverified`. |
| `expiration_date` | `gelato_data_document_report_expiration_date` |  | Expiration date of the document. |
| `files` | array of string |  | Array of [File](https://stripe.com/docs/api/files) ids containing images for this document. |
| `first_name` | string |  | First name as it appears in the document. |
| `issued_date` | `gelato_data_document_report_issued_date` |  | Issued date of the document. |
| `issuing_country` | string |  | Issuing country of the document. |
| `last_name` | string |  | Last name as it appears in the document. |
| `number` | string |  | Document ID number. |
| `status` | enum: `unverified`, `verified` | yes | Status of this `document` check. |
| `type` | enum: `driving_license`, `id_card`, `passport` |  | Type of the document. |

