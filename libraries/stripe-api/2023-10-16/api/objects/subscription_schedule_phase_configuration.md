# Stripe API 2023-10-16 — `subscription_schedule_phase_configuration` object

A phase describes the plans, coupon, and trialing status of a subscription for a predefined time period.

Expandable fields (pass `expand[]=<field>`): `add_invoice_items`, `automatic_tax`, `billing_thresholds`, `coupon`, `default_payment_method`, `default_tax_rates`, `discounts`, `invoice_settings`, `items`, `on_behalf_of`, `transfer_data`

| Field | Type | Required | Description |
|---|---|---|---|
| `add_invoice_items` | array of `subscription_schedule_add_invoice_item` | yes | A list of prices and quantities that will generate invoice items appended to the next invoice for this phase. |
| `application_fee_percent` | number |  | A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account during this phase of the schedule. |
| `automatic_tax` | `schedules_phase_automatic_tax` |  |  |
| `billing_cycle_anchor` | enum: `automatic`, `phase_start` |  | Possible values are `phase_start` or `automatic`. If `phase_start` then billing cycle anchor of the subscription is set to the start of the phase when entering the phase. If `automatic` then the billing cycle anchor is automatically modified as needed when entering the phase. For more information, see the billing cycle [documentation](https://stripe.com/docs/billing/subscriptions/billing-cycle). |
| `billing_thresholds` | `subscription_billing_thresholds` |  | Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period |
| `collection_method` | enum: `charge_automatically`, `send_invoice` |  | Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay the underlying subscription at the end of each billing cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. |
| `coupon` | string or `coupon` or `deleted_coupon` |  | ID of the coupon to use during this phase of the subscription schedule. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `default_payment_method` | string or `payment_method` |  | ID of the default payment method for the subscription schedule. It must belong to the customer associated with the subscription schedule. If not set, invoices will use the default payment method in the customer's invoice settings. |
| `default_tax_rates` | array of `tax_rate` |  | The default tax rates to apply to the subscription during this phase of the subscription schedule. |
| `description` | string |  | Subscription description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs. |
| `discounts` | array of `discounts_resource_stackable_discount` | yes | The stackable discounts that will be applied to the subscription on this phase. Subscription item discounts are applied before subscription discounts. |
| `end_date` | timestamp (Unix seconds) | yes | The end of this phase of the subscription schedule. |
| `invoice_settings` | `invoice_setting_subscription_schedule_phase_setting` |  | The invoice settings applicable during this phase. |
| `items` | array of `subscription_schedule_configuration_item` | yes | Subscription items to configure the subscription to during this phase of the subscription schedule. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to a phase. Metadata on a schedule's phase will update the underlying subscription's `metadata` when the phase is entered. Updating the underlying subscription's `metadata` directly will not affect the current phase's `metadata`. |
| `on_behalf_of` | string or `account` |  | The account (if any) the charge was made on behalf of for charges associated with the schedule's subscription. See the Connect documentation for details. |
| `proration_behavior` | enum: `always_invoice`, `create_prorations`, `none` | yes | If the subscription schedule will prorate when transitioning to this phase. Possible values are `create_prorations` and `none`. |
| `start_date` | timestamp (Unix seconds) | yes | The start of this phase of the subscription schedule. |
| `transfer_data` | `subscription_transfer_data` |  | The account (if any) the associated subscription's payments will be attributed to for tax reporting, and where funds from each payment will be transferred to for each of the subscription's invoices. |
| `trial_end` | timestamp (Unix seconds) |  | When the trial ends within the phase. |

