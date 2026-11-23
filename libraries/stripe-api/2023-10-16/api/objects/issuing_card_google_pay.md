# Stripe API 2023-10-16 — `issuing_card_google_pay` object

| Field | Type | Required | Description |
|---|---|---|---|
| `eligible` | boolean | yes | Google Pay Eligibility |
| `ineligible_reason` | enum: `missing_agreement`, `missing_cardholder_contact`, `unsupported_region` |  | Reason the card is ineligible for Google Pay |

