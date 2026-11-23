# Stripe API 2023-10-16 — `account_requirements` object

Expandable fields (pass `expand[]=<field>`): `alternatives`, `errors`

| Field | Type | Required | Description |
|---|---|---|---|
| `alternatives` | array of `account_requirements_alternative` |  | Fields that are due and can be satisfied by providing the corresponding alternative fields instead. |
| `current_deadline` | timestamp (Unix seconds) |  | Date by which the fields in `currently_due` must be collected to keep the account enabled. These fields may disable the account sooner if the next threshold is reached before they are collected. |
| `currently_due` | array of string |  | Fields that need to be collected to keep the account enabled. If not collected by `current_deadline`, these fields appear in `past_due` as well, and the account is disabled. |
| `disabled_reason` | string |  | If the account is disabled, this string describes why. [Learn more about handling verification issues](https://stripe.com/docs/connect/handling-api-verification). Can be `action_required.requested_capabilities`, `requirements.past_due`, `requirements.pending_verification`, `listed`, `platform_paused`, `rejected.fraud`, `rejected.incomplete_verification`, `rejected.listed`, `rejected.other`, `rejected.terms_of_service`, `under_review`, or `other`. |
| `errors` | array of `account_requirements_error` |  | Fields that are `currently_due` and need to be collected again because validation or verification failed. |
| `eventually_due` | array of string |  | Fields that need to be collected assuming all volume thresholds are reached. As they become required, they appear in `currently_due` as well, and `current_deadline` becomes set. |
| `past_due` | array of string |  | Fields that weren't collected by `current_deadline`. These fields need to be collected to enable the account. |
| `pending_verification` | array of string |  | Fields that may become required depending on the results of verification or review. Will be an empty array unless an asynchronous verification is pending. If verification fails, these fields move to `eventually_due`, `currently_due`, or `past_due`. |

