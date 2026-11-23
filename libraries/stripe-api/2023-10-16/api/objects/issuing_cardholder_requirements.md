# Stripe API 2023-10-16 — `issuing_cardholder_requirements` object

| Field | Type | Required | Description |
|---|---|---|---|
| `disabled_reason` | enum: `listed`, `rejected.listed`, `requirements.past_due`, `under_review` |  | If `disabled_reason` is present, all cards will decline authorizations with `cardholder_verification_required` reason. |
| `past_due` | array of enum: `company.tax_id`, `individual.card_issuing.user_terms_acceptance.date`, `individual.card_issuing.user_terms_acceptance.ip`, `individual.dob.day`, `individual.dob.month`, `individual.dob.year`, `individual.first_name`, `individual.last_name`, `individual.verification.document` |  | Array of fields that need to be collected in order to verify and re-enable the cardholder. |

