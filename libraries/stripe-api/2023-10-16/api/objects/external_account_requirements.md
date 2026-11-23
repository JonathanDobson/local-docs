# Stripe API 2023-10-16 — `external_account_requirements` object

Expandable fields (pass `expand[]=<field>`): `errors`

| Field | Type | Required | Description |
|---|---|---|---|
| `currently_due` | array of string |  | Fields that need to be collected to keep the external account enabled. If not collected by `current_deadline`, these fields appear in `past_due` as well, and the account is disabled. |
| `errors` | array of `account_requirements_error` |  | Fields that are `currently_due` and need to be collected again because validation or verification failed. |
| `past_due` | array of string |  | Fields that weren't collected by `current_deadline`. These fields need to be collected to enable the external account. |
| `pending_verification` | array of string |  | Fields that may become required depending on the results of verification or review. Will be an empty array unless an asynchronous verification is pending. If verification fails, these fields move to `eventually_due`, `currently_due`, or `past_due`. |

