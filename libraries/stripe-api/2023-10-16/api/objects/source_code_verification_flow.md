# Stripe API 2023-10-16 — `source_code_verification_flow` object

| Field | Type | Required | Description |
|---|---|---|---|
| `attempts_remaining` | integer | yes | The number of attempts remaining to authenticate the source object with a verification code. |
| `status` | string | yes | The status of the code verification, either `pending` (awaiting verification, `attempts_remaining` should be greater than 0), `succeeded` (successful verification) or `failed` (failed verification, cannot be verified anymore as `attempts_remaining` should be 0). |

