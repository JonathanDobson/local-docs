# Stripe API 2023-10-16 — `payment_links_resource_subscription_data` object

Expandable fields (pass `expand[]=<field>`): `invoice_settings`, `trial_settings`

| Field | Type | Required | Description |
|---|---|---|---|
| `description` | string |  | The subscription's description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs. |
| `invoice_settings` | `payment_links_resource_subscription_data_invoice_settings` | yes |  |
| `metadata` | map (key → value) | yes | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that will set metadata on [Subscriptions](https://stripe.com/docs/api/subscriptions) generated from this payment link. |
| `trial_period_days` | integer |  | Integer representing the number of trial period days before the customer is charged for the first time. |
| `trial_settings` | `subscriptions_trials_resource_trial_settings` |  | Settings related to subscription trials. |

