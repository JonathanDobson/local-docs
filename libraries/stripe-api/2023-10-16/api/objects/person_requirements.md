# Stripe API 2023-10-16 — `person_requirements` object

Expandable fields (pass `expand[]=<field>`): `alternatives`, `errors`

| Field | Type | Required | Description |
|---|---|---|---|
| `alternatives` | array of `account_requirements_alternative` |  | Fields that are due and can be satisfied by providing the corresponding alternative fields instead. |
| `currently_due` | array of string | yes | Fields that need to be collected to keep the person's account enabled. If not collected by the account's `current_deadline`, these fields appear in `past_due` as well, and the account is disabled. |
| `errors` | array of `account_requirements_error` | yes | Fields that are `currently_due` and need to be collected again because validation or verification failed. |
| `eventually_due` | array of string | yes | Fields that need to be collected assuming all volume thresholds are reached. As they become required, they appear in `currently_due` as well, and the account's `current_deadline` becomes set. |
| `past_due` | array of string | yes | Fields that weren't collected by the account's `current_deadline`. These fields need to be collected to enable the person's account. |
| `pending_verification` | array of string | yes | Fields that may become required depending on the results of verification or review. Will be an empty array unless an asynchronous verification is pending. If verification fails, these fields move to `eventually_due`, `currently_due`, or `past_due`. |

