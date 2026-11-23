# Stripe API 2023-10-16 — `account_unification_account_controller` object

| Field | Type | Required | Description |
|---|---|---|---|
| `is_controller` | boolean |  | `true` if the Connect application retrieving the resource controls the account and can therefore exercise [platform controls](https://stripe.com/docs/connect/platform-controls-for-standard-accounts). Otherwise, this field is null. |
| `type` | enum: `account`, `application` | yes | The controller type. Can be `application`, if a Connect application controls the account, or `account`, if the account controls itself. |

