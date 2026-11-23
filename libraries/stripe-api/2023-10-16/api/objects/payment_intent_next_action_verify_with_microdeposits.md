# Stripe API 2023-10-16 — `payment_intent_next_action_verify_with_microdeposits` object

| Field | Type | Required | Description |
|---|---|---|---|
| `arrival_date` | timestamp (Unix seconds) | yes | The timestamp when the microdeposits are expected to land. |
| `hosted_verification_url` | string | yes | The URL for the hosted verification page, which allows customers to verify their bank account. |
| `microdeposit_type` | enum: `amounts`, `descriptor_code` |  | The type of the microdeposit sent to the customer. Used to distinguish between different verification methods. |

