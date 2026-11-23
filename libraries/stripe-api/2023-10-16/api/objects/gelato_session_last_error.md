# Stripe API 2023-10-16 — `gelato_session_last_error` object

Shows last VerificationSession error

| Field | Type | Required | Description |
|---|---|---|---|
| `code` | enum: `abandoned`, `consent_declined`, `country_not_supported`, `device_not_supported`, `document_expired`, `document_type_not_supported`, `document_unverified_other`, `email_unverified_other`, `email_verification_declined`, `id_number_insufficient_document_data`, `id_number_mismatch`, `id_number_unverified_other`, `phone_unverified_other`, `phone_verification_declined`, `selfie_document_missing_photo`, `selfie_face_mismatch`, `selfie_manipulated`, `selfie_unverified_other`, `under_supported_age` |  | A short machine-readable string giving the reason for the verification or user-session failure. |
| `reason` | string |  | A message that explains the reason for verification or user-session failure. |

