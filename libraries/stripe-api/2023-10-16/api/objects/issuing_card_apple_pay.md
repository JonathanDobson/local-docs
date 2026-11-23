# Stripe API 2023-10-16 — `issuing_card_apple_pay` object

| Field | Type | Required | Description |
|---|---|---|---|
| `eligible` | boolean | yes | Apple Pay Eligibility |
| `ineligible_reason` | enum: `missing_agreement`, `missing_cardholder_contact`, `unsupported_region` |  | Reason the card is ineligible for Apple Pay |

