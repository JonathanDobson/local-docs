# Stripe API 2023-10-16 — `subscriptions_resource_pending_update` object

Pending Updates store the changes pending from a previous update that will be applied
to the Subscription upon successful payment.

Expandable fields (pass `expand[]=<field>`): `subscription_items`

| Field | Type | Required | Description |
|---|---|---|---|
| `billing_cycle_anchor` | timestamp (Unix seconds) |  | If the update is applied, determines the date of the first full invoice, and, for plans with `month` or `year` intervals, the day of the month for subsequent invoices. The timestamp is in UTC format. |
| `expires_at` | timestamp (Unix seconds) | yes | The point after which the changes reflected by this update will be discarded and no longer applied. |
| `subscription_items` | array of `subscription_item` |  | List of subscription items, each with an attached plan, that will be set if the update is applied. |
| `trial_end` | timestamp (Unix seconds) |  | Unix timestamp representing the end of the trial period the customer will get before being charged for the first time, if the update is applied. |
| `trial_from_plan` | boolean |  | Indicates if a plan's `trial_period_days` should be applied to the subscription. Setting `trial_end` per subscription is preferred, and this defaults to `false`. Setting this flag to `true` together with `trial_end` is not allowed. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more. |

