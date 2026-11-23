# Stripe API 2023-10-16 — `gelato_selfie_report_error` object

| Field | Type | Required | Description |
|---|---|---|---|
| `code` | enum: `selfie_document_missing_photo`, `selfie_face_mismatch`, `selfie_manipulated`, `selfie_unverified_other` |  | A short machine-readable string giving the reason for the verification failure. |
| `reason` | string |  | A human-readable message giving the reason for the failure. These messages can be shown to your users. |

