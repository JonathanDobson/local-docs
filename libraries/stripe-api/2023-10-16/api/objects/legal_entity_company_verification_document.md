# Stripe API 2023-10-16 — `legal_entity_company_verification_document` object

Expandable fields (pass `expand[]=<field>`): `back`, `front`

| Field | Type | Required | Description |
|---|---|---|---|
| `back` | string or `file` |  | The back of a document returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `additional_verification`. |
| `details` | string |  | A user-displayable string describing the verification state of this document. |
| `details_code` | string |  | One of `document_corrupt`, `document_expired`, `document_failed_copy`, `document_failed_greyscale`, `document_failed_other`, `document_failed_test_mode`, `document_fraudulent`, `document_incomplete`, `document_invalid`, `document_manipulated`, `document_not_readable`, `document_not_uploaded`, `document_type_not_supported`, or `document_too_large`. A machine-readable code specifying the verification state for this document. |
| `front` | string or `file` |  | The front of a document returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `additional_verification`. |

