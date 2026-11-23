# Stripe API 2023-10-16 — `subscription_schedules_resource_default_settings` object

Expandable fields (pass `expand[]=<field>`): `automatic_tax`, `billing_thresholds`, `default_payment_method`, `invoice_settings`, `on_behalf_of`, `transfer_data`

| Field | Type | Required | Description |
|---|---|---|---|
| `application_fee_percent` | number |  | A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account during this phase of the schedule. |
| `automatic_tax` | `subscription_schedules_resource_default_settings_automatic_tax` |  |  |
| `billing_cycle_anchor` | enum: `automatic`, `phase_start` | yes | Possible values are `phase_start` or `automatic`. If `phase_start` then billing cycle anchor of the subscription is set to the start of the phase when entering the phase. If `automatic` then the billing cycle anchor is automatically modified as needed when entering the phase. For more information, see the billing cycle [documentation](https://stripe.com/docs/billing/subscriptions/billing-cycle). |
| `billing_thresholds` | `subscription_billing_thresholds` |  | Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period |
| `collection_method` | enum: `charge_automatically`, `send_invoice` |  | Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay the underlying subscription at the end of each billing cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. |
| `default_payment_method` | string or `payment_method` |  | ID of the default payment method for the subscription schedule. If not set, invoices will use the default payment method in the customer's invoice settings. |
| `description` | string |  | Subscription description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs. |
| `invoice_settings` | `invoice_setting_subscription_schedule_setting` | yes |  |
| `on_behalf_of` | string or `account` |  | The account (if any) the charge was made on behalf of for charges associated with the schedule's subscription. See the Connect documentation for details. |
| `transfer_data` | `subscription_transfer_data` |  | The account (if any) the associated subscription's payments will be attributed to for tax reporting, and where funds from each payment will be transferred to for each of the subscription's invoices. |

