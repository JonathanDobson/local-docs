# Stripe API 2023-10-16 — `gelato_session_document_options` object

| Field | Type | Required | Description |
|---|---|---|---|
| `allowed_types` | array of enum: `driving_license`, `id_card`, `passport` |  | Array of strings of allowed identity document types. If the provided identity document isn’t one of the allowed types, the verification check will fail with a document_type_not_allowed error code. |
| `require_id_number` | boolean |  | Collect an ID number and perform an [ID number check](https://stripe.com/docs/identity/verification-checks?type=id-number) with the document’s extracted name and date of birth. |
| `require_live_capture` | boolean |  | Disable image uploads, identity document images have to be captured using the device’s camera. |
| `require_matching_selfie` | boolean |  | Capture a face image and perform a [selfie check](https://stripe.com/docs/identity/verification-checks?type=selfie) comparing a photo ID and a picture of your user’s face. [Learn more](https://stripe.com/docs/identity/selfie). |

