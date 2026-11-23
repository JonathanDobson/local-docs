# Stripe API 2023-10-16 — `account_future_requirements` object

Expandable fields (pass `expand[]=<field>`): `alternatives`, `errors`

| Field | Type | Required | Description |
|---|---|---|---|
| `alternatives` | array of `account_requirements_alternative` |  | Fields that are due and can be satisfied by providing the corresponding alternative fields instead. |
| `current_deadline` | timestamp (Unix seconds) |  | Date on which `future_requirements` merges with the main `requirements` hash and `future_requirements` becomes empty. After the transition, `currently_due` requirements may immediately become `past_due`, but the account may also be given a grace period depending on its enablement state prior to transitioning. |
| `currently_due` | array of string |  | Fields that need to be collected to keep the account enabled. If not collected by `future_requirements[current_deadline]`, these fields will transition to the main `requirements` hash. |
| `disabled_reason` | string |  | This is typed as a string for consistency with `requirements.disabled_reason`. |
| `errors` | array of `account_requirements_error` |  | Fields that are `currently_due` and need to be collected again because validation or verification failed. |
| `eventually_due` | array of string |  | Fields that need to be collected assuming all volume thresholds are reached. As they become required, they appear in `currently_due` as well. |
| `past_due` | array of string |  | Fields that weren't collected by `requirements.current_deadline`. These fields need to be collected to enable the capability on the account. New fields will never appear here; `future_requirements.past_due` will always be a subset of `requirements.past_due`. |
| `pending_verification` | array of string |  | Fields that may become required depending on the results of verification or review. Will be an empty array unless an asynchronous verification is pending. If verification fails, these fields move to `eventually_due` or `currently_due`. |

