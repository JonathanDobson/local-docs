# Stripe API 2023-10-16 — `treasury_received_credits_resource_reversal_details` object

| Field | Type | Required | Description |
|---|---|---|---|
| `deadline` | timestamp (Unix seconds) |  | Time before which a ReceivedCredit can be reversed. |
| `restricted_reason` | enum: `already_reversed`, `deadline_passed`, `network_restricted`, `other`, `source_flow_restricted` |  | Set if a ReceivedCredit cannot be reversed. |

