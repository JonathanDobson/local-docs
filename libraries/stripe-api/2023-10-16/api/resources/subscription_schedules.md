# Stripe API 2023-10-16 — subscription schedules

Operations under `/v1/subscription_schedules` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/subscription_schedules

operationId: `GetSubscriptionSchedules`

Retrieves the list of your subscription schedules.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `canceled_at` | object or integer |  | Only return subscription schedules that were created canceled the given date interval. |
| `canceled_at.gt` | integer |  |  |
| `canceled_at.gte` | integer |  |  |
| `canceled_at.lt` | integer |  |  |
| `canceled_at.lte` | integer |  |  |
| `completed_at` | object or integer |  | Only return subscription schedules that completed during the given date interval. |
| `completed_at.gt` | integer |  |  |
| `completed_at.gte` | integer |  |  |
| `completed_at.lt` | integer |  |  |
| `completed_at.lte` | integer |  |  |
| `created` | object or integer |  | Only return subscription schedules that were created during the given date interval. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `customer` | string |  | Only return subscription schedules for the given customer. |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `released_at` | object or integer |  | Only return subscription schedules that were released during the given date interval. |
| `released_at.gt` | integer |  |  |
| `released_at.gte` | integer |  |  |
| `released_at.lt` | integer |  |  |
| `released_at.lte` | integer |  |  |
| `scheduled` | boolean |  | Only return subscription schedules that have not started yet. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/subscription_schedules

operationId: `PostSubscriptionSchedules`

Creates a new subscription schedule object. Each customer can have up to 500 active or scheduled subscriptions.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer` | string |  | The identifier of the customer to create the subscription schedule for. |
| `default_settings` | object |  | Object representing the subscription schedule's default settings. |
| `default_settings.application_fee_percent` | number |  |  |
| `default_settings.automatic_tax` | object |  |  |
| `default_settings.automatic_tax.enabled` | boolean | yes |  |
| `default_settings.automatic_tax.liability` | object |  |  |
| `default_settings.automatic_tax.liability.account` | string |  |  |
| `default_settings.automatic_tax.liability.type` | enum: `account`, `self` | yes |  |
| `default_settings.billing_cycle_anchor` | enum: `automatic`, `phase_start` |  |  |
| `default_settings.billing_thresholds` | object or "" (to unset) |  |  |
| `default_settings.billing_thresholds.amount_gte` | integer |  |  |
| `default_settings.billing_thresholds.reset_billing_cycle_anchor` | boolean |  |  |
| `default_settings.collection_method` | enum: `charge_automatically`, `send_invoice` |  |  |
| `default_settings.default_payment_method` | string |  |  |
| `default_settings.description` | string or "" (to unset) |  |  |
| `default_settings.invoice_settings` | object |  |  |
| `default_settings.invoice_settings.account_tax_ids` | array of string or "" (to unset) |  |  |
| `default_settings.invoice_settings.days_until_due` | integer |  |  |
| `default_settings.invoice_settings.issuer` | object |  |  |
| `default_settings.invoice_settings.issuer.account` | string |  |  |
| `default_settings.invoice_settings.issuer.type` | enum: `account`, `self` | yes |  |
| `default_settings.on_behalf_of` | string or "" (to unset) |  |  |
| `default_settings.transfer_data` | object or "" (to unset) |  |  |
| `default_settings.transfer_data.amount_percent` | number |  |  |
| `default_settings.transfer_data.destination` | string | yes |  |
| `end_behavior` | enum: `cancel`, `none`, `release`, `renew` |  | Behavior of the subscription schedule and underlying subscription when it ends. Possible values are `release` or `cancel` with the default being `release`. `release` will end the subscription schedule and keep the underlying subscription running. `cancel` will end the subscription schedule and cancel the underlying subscription. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `from_subscription` | string |  | Migrate an existing subscription to be managed by a subscription schedule. If this parameter is set, a subscription schedule will be created using the subscription's item(s), set to auto-renew using the subscription's interval. When using this parameter, other parameters (such as phase values) cannot be set. To create a subscription schedule with other modifications, we recommend making two separate API calls. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `phases` | array of object |  | List representing phases of the subscription schedule. Each phase can be customized to have different durations, plans, and coupons. If there are multiple phases, the `end_date` of one phase will always equal the `start_date` of the next phase. |
| `phases[].add_invoice_items` | array of object |  |  |
| `phases[].add_invoice_items[].discounts` | array of object |  |  |
| `phases[].add_invoice_items[].discounts[].coupon` | string |  |  |
| `phases[].add_invoice_items[].discounts[].discount` | string |  |  |
| `phases[].add_invoice_items[].discounts[].promotion_code` | string |  |  |
| `phases[].add_invoice_items[].price` | string |  |  |
| `phases[].add_invoice_items[].price_data` | object |  |  |
| `phases[].add_invoice_items[].price_data.currency` | string | yes |  |
| `phases[].add_invoice_items[].price_data.product` | string | yes |  |
| `phases[].add_invoice_items[].price_data.tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  |  |
| `phases[].add_invoice_items[].price_data.unit_amount` | integer |  |  |
| `phases[].add_invoice_items[].price_data.unit_amount_decimal` | string |  |  |
| `phases[].add_invoice_items[].quantity` | integer |  |  |
| `phases[].add_invoice_items[].tax_rates` | array of string or "" (to unset) |  |  |
| `phases[].application_fee_percent` | number |  |  |
| `phases[].automatic_tax` | object |  |  |
| `phases[].automatic_tax.enabled` | boolean | yes |  |
| `phases[].automatic_tax.liability` | object |  |  |
| `phases[].automatic_tax.liability.account` | string |  |  |
| `phases[].automatic_tax.liability.type` | enum: `account`, `self` | yes |  |
| `phases[].billing_cycle_anchor` | enum: `automatic`, `phase_start` |  |  |
| `phases[].billing_thresholds` | object or "" (to unset) |  |  |
| `phases[].billing_thresholds.amount_gte` | integer |  |  |
| `phases[].billing_thresholds.reset_billing_cycle_anchor` | boolean |  |  |
| `phases[].collection_method` | enum: `charge_automatically`, `send_invoice` |  |  |
| `phases[].coupon` | string |  |  |
| `phases[].currency` | string |  |  |
| `phases[].default_payment_method` | string |  |  |
| `phases[].default_tax_rates` | array of string or "" (to unset) |  |  |
| `phases[].description` | string or "" (to unset) |  |  |
| `phases[].discounts` | array of object or "" (to unset) |  |  |
| `phases[].discounts[].coupon` | string |  |  |
| `phases[].discounts[].discount` | string |  |  |
| `phases[].discounts[].promotion_code` | string |  |  |
| `phases[].end_date` | timestamp (Unix seconds) |  |  |
| `phases[].invoice_settings` | object |  |  |
| `phases[].invoice_settings.account_tax_ids` | array of string or "" (to unset) |  |  |
| `phases[].invoice_settings.days_until_due` | integer |  |  |
| `phases[].invoice_settings.issuer` | object |  |  |
| `phases[].invoice_settings.issuer.account` | string |  |  |
| `phases[].invoice_settings.issuer.type` | enum: `account`, `self` | yes |  |
| `phases[].items` | array of object | yes |  |
| `phases[].items[].billing_thresholds` | object or "" (to unset) |  |  |
| `phases[].items[].billing_thresholds.usage_gte` | integer | yes |  |
| `phases[].items[].discounts` | array of object or "" (to unset) |  |  |
| `phases[].items[].discounts[].coupon` | string |  |  |
| `phases[].items[].discounts[].discount` | string |  |  |
| `phases[].items[].discounts[].promotion_code` | string |  |  |
| `phases[].items[].metadata` | map (key → value) |  |  |
| `phases[].items[].price` | string |  |  |
| `phases[].items[].price_data` | object |  |  |
| `phases[].items[].price_data.currency` | string | yes |  |
| `phases[].items[].price_data.product` | string | yes |  |
| `phases[].items[].price_data.recurring` | object | yes |  |
| `phases[].items[].price_data.recurring.interval` | enum: `day`, `month`, `week`, `year` | yes |  |
| `phases[].items[].price_data.recurring.interval_count` | integer |  |  |
| `phases[].items[].price_data.tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  |  |
| `phases[].items[].price_data.unit_amount` | integer |  |  |
| `phases[].items[].price_data.unit_amount_decimal` | string |  |  |
| `phases[].items[].quantity` | integer |  |  |
| `phases[].items[].tax_rates` | array of string or "" (to unset) |  |  |
| `phases[].iterations` | integer |  |  |
| `phases[].metadata` | map (key → value) |  |  |
| `phases[].on_behalf_of` | string |  |  |
| `phases[].proration_behavior` | enum: `always_invoice`, `create_prorations`, `none` |  |  |
| `phases[].transfer_data` | object |  |  |
| `phases[].transfer_data.amount_percent` | number |  |  |
| `phases[].transfer_data.destination` | string | yes |  |
| `phases[].trial` | boolean |  |  |
| `phases[].trial_end` | timestamp (Unix seconds) |  |  |
| `start_date` | timestamp (Unix seconds) or enum: `now` |  | When the subscription schedule starts. We recommend using `now` so that it starts the subscription immediately. You can also use a Unix timestamp to backdate the subscription so that it starts on a past date, or set a future date for the subscription to start on. |

Returns: `subscription_schedule`

## GET /v1/subscription_schedules/{schedule}

operationId: `GetSubscriptionSchedulesSchedule`

Retrieves the details of an existing subscription schedule. You only need to supply the unique subscription schedule identifier that was returned upon subscription schedule creation.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `schedule (path)` | string | yes |  |

Returns: `subscription_schedule`

## POST /v1/subscription_schedules/{schedule}

operationId: `PostSubscriptionSchedulesSchedule`

Updates an existing subscription schedule.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `schedule (path)` | string | yes |  |
| `default_settings` | object |  | Object representing the subscription schedule's default settings. |
| `default_settings.application_fee_percent` | number |  |  |
| `default_settings.automatic_tax` | object |  |  |
| `default_settings.automatic_tax.enabled` | boolean | yes |  |
| `default_settings.automatic_tax.liability` | object |  |  |
| `default_settings.automatic_tax.liability.account` | string |  |  |
| `default_settings.automatic_tax.liability.type` | enum: `account`, `self` | yes |  |
| `default_settings.billing_cycle_anchor` | enum: `automatic`, `phase_start` |  |  |
| `default_settings.billing_thresholds` | object or "" (to unset) |  |  |
| `default_settings.billing_thresholds.amount_gte` | integer |  |  |
| `default_settings.billing_thresholds.reset_billing_cycle_anchor` | boolean |  |  |
| `default_settings.collection_method` | enum: `charge_automatically`, `send_invoice` |  |  |
| `default_settings.default_payment_method` | string |  |  |
| `default_settings.description` | string or "" (to unset) |  |  |
| `default_settings.invoice_settings` | object |  |  |
| `default_settings.invoice_settings.account_tax_ids` | array of string or "" (to unset) |  |  |
| `default_settings.invoice_settings.days_until_due` | integer |  |  |
| `default_settings.invoice_settings.issuer` | object |  |  |
| `default_settings.invoice_settings.issuer.account` | string |  |  |
| `default_settings.invoice_settings.issuer.type` | enum: `account`, `self` | yes |  |
| `default_settings.on_behalf_of` | string or "" (to unset) |  |  |
| `default_settings.transfer_data` | object or "" (to unset) |  |  |
| `default_settings.transfer_data.amount_percent` | number |  |  |
| `default_settings.transfer_data.destination` | string | yes |  |
| `end_behavior` | enum: `cancel`, `none`, `release`, `renew` |  | Behavior of the subscription schedule and underlying subscription when it ends. Possible values are `release` or `cancel` with the default being `release`. `release` will end the subscription schedule and keep the underlying subscription running. `cancel` will end the subscription schedule and cancel the underlying subscription. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `phases` | array of object |  | List representing phases of the subscription schedule. Each phase can be customized to have different durations, plans, and coupons. If there are multiple phases, the `end_date` of one phase will always equal the `start_date` of the next phase. Note that past phases can be omitted. |
| `phases[].add_invoice_items` | array of object |  |  |
| `phases[].add_invoice_items[].discounts` | array of object |  |  |
| `phases[].add_invoice_items[].discounts[].coupon` | string |  |  |
| `phases[].add_invoice_items[].discounts[].discount` | string |  |  |
| `phases[].add_invoice_items[].discounts[].promotion_code` | string |  |  |
| `phases[].add_invoice_items[].price` | string |  |  |
| `phases[].add_invoice_items[].price_data` | object |  |  |
| `phases[].add_invoice_items[].price_data.currency` | string | yes |  |
| `phases[].add_invoice_items[].price_data.product` | string | yes |  |
| `phases[].add_invoice_items[].price_data.tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  |  |
| `phases[].add_invoice_items[].price_data.unit_amount` | integer |  |  |
| `phases[].add_invoice_items[].price_data.unit_amount_decimal` | string |  |  |
| `phases[].add_invoice_items[].quantity` | integer |  |  |
| `phases[].add_invoice_items[].tax_rates` | array of string or "" (to unset) |  |  |
| `phases[].application_fee_percent` | number |  |  |
| `phases[].automatic_tax` | object |  |  |
| `phases[].automatic_tax.enabled` | boolean | yes |  |
| `phases[].automatic_tax.liability` | object |  |  |
| `phases[].automatic_tax.liability.account` | string |  |  |
| `phases[].automatic_tax.liability.type` | enum: `account`, `self` | yes |  |
| `phases[].billing_cycle_anchor` | enum: `automatic`, `phase_start` |  |  |
| `phases[].billing_thresholds` | object or "" (to unset) |  |  |
| `phases[].billing_thresholds.amount_gte` | integer |  |  |
| `phases[].billing_thresholds.reset_billing_cycle_anchor` | boolean |  |  |
| `phases[].collection_method` | enum: `charge_automatically`, `send_invoice` |  |  |
| `phases[].coupon` | string |  |  |
| `phases[].default_payment_method` | string |  |  |
| `phases[].default_tax_rates` | array of string or "" (to unset) |  |  |
| `phases[].description` | string or "" (to unset) |  |  |
| `phases[].discounts` | array of object or "" (to unset) |  |  |
| `phases[].discounts[].coupon` | string |  |  |
| `phases[].discounts[].discount` | string |  |  |
| `phases[].discounts[].promotion_code` | string |  |  |
| `phases[].end_date` | timestamp (Unix seconds) or enum: `now` |  |  |
| `phases[].invoice_settings` | object |  |  |
| `phases[].invoice_settings.account_tax_ids` | array of string or "" (to unset) |  |  |
| `phases[].invoice_settings.days_until_due` | integer |  |  |
| `phases[].invoice_settings.issuer` | object |  |  |
| `phases[].invoice_settings.issuer.account` | string |  |  |
| `phases[].invoice_settings.issuer.type` | enum: `account`, `self` | yes |  |
| `phases[].items` | array of object | yes |  |
| `phases[].items[].billing_thresholds` | object or "" (to unset) |  |  |
| `phases[].items[].billing_thresholds.usage_gte` | integer | yes |  |
| `phases[].items[].discounts` | array of object or "" (to unset) |  |  |
| `phases[].items[].discounts[].coupon` | string |  |  |
| `phases[].items[].discounts[].discount` | string |  |  |
| `phases[].items[].discounts[].promotion_code` | string |  |  |
| `phases[].items[].metadata` | map (key → value) |  |  |
| `phases[].items[].price` | string |  |  |
| `phases[].items[].price_data` | object |  |  |
| `phases[].items[].price_data.currency` | string | yes |  |
| `phases[].items[].price_data.product` | string | yes |  |
| `phases[].items[].price_data.recurring` | object | yes |  |
| `phases[].items[].price_data.recurring.interval` | enum: `day`, `month`, `week`, `year` | yes |  |
| `phases[].items[].price_data.recurring.interval_count` | integer |  |  |
| `phases[].items[].price_data.tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  |  |
| `phases[].items[].price_data.unit_amount` | integer |  |  |
| `phases[].items[].price_data.unit_amount_decimal` | string |  |  |
| `phases[].items[].quantity` | integer |  |  |
| `phases[].items[].tax_rates` | array of string or "" (to unset) |  |  |
| `phases[].iterations` | integer |  |  |
| `phases[].metadata` | map (key → value) |  |  |
| `phases[].on_behalf_of` | string |  |  |
| `phases[].proration_behavior` | enum: `always_invoice`, `create_prorations`, `none` |  |  |
| `phases[].start_date` | timestamp (Unix seconds) or enum: `now` |  |  |
| `phases[].transfer_data` | object |  |  |
| `phases[].transfer_data.amount_percent` | number |  |  |
| `phases[].transfer_data.destination` | string | yes |  |
| `phases[].trial` | boolean |  |  |
| `phases[].trial_end` | timestamp (Unix seconds) or enum: `now` |  |  |
| `proration_behavior` | enum: `always_invoice`, `create_prorations`, `none` |  | If the update changes the current phase, indicates whether the changes should be prorated. The default value is `create_prorations`. |

Returns: `subscription_schedule`

## POST /v1/subscription_schedules/{schedule}/cancel

operationId: `PostSubscriptionSchedulesScheduleCancel`

Cancels a subscription schedule and its associated subscription immediately (if the subscription schedule has an active subscription). A subscription schedule can only be canceled if its status is `not_started` or `active`.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `schedule (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `invoice_now` | boolean |  | If the subscription schedule is `active`, indicates if a final invoice will be generated that contains any un-invoiced metered usage and new/pending proration invoice items. Defaults to `true`. |
| `prorate` | boolean |  | If the subscription schedule is `active`, indicates if the cancellation should be prorated. Defaults to `true`. |

Returns: `subscription_schedule`

## POST /v1/subscription_schedules/{schedule}/release

operationId: `PostSubscriptionSchedulesScheduleRelease`

Releases the subscription schedule immediately, which will stop scheduling of its phases, but leave any existing subscription in place. A schedule can only be released if its status is `not_started` or `active`. If the subscription schedule is currently associated with a subscription, releasing it will remove its `subscription` property and set the subscription’s ID to the `released_subscription` property.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `schedule (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `preserve_cancel_date` | boolean |  | Keep any cancellation on the subscription that the schedule has set |

Returns: `subscription_schedule`

# Objects returned

## The `subscription_schedule` object

A subscription schedule allows you to create and manage the lifecycle of a subscription by predefining expected changes.

Related guide: [Subscription schedules](https://stripe.com/docs/billing/subscriptions/subscription-schedules)

Expandable fields (pass `expand[]=<field>`): `application`, `current_phase`, `customer`, `default_settings`, `phases`, `subscription`, `test_clock`

| Field | Type | Required | Description |
|---|---|---|---|
| `application` | string or `application` or `deleted_application` |  | ID of the Connect Application that created the schedule. |
| `canceled_at` | timestamp (Unix seconds) |  | Time at which the subscription schedule was canceled. Measured in seconds since the Unix epoch. |
| `completed_at` | timestamp (Unix seconds) |  | Time at which the subscription schedule was completed. Measured in seconds since the Unix epoch. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `current_phase` | `subscription_schedule_current_phase` |  | Object representing the start and end dates for the current phase of the subscription schedule, if it is `active`. |
| `customer` | string or `customer` or `deleted_customer` | yes | ID of the customer who owns the subscription schedule. |
| `default_settings` | `subscription_schedules_resource_default_settings` | yes |  |
| `end_behavior` | enum: `cancel`, `none`, `release`, `renew` | yes | Behavior of the subscription schedule and underlying subscription when it ends. Possible values are `release` or `cancel` with the default being `release`. `release` will end the subscription schedule and keep the underlying subscription running. `cancel` will end the subscription schedule and cancel the underlying subscription. |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `object` | enum: `subscription_schedule` | yes | String representing the object's type. Objects of the same type share the same value. |
| `phases` | array of `subscription_schedule_phase_configuration` | yes | Configuration for the subscription schedule's phases. |
| `released_at` | timestamp (Unix seconds) |  | Time at which the subscription schedule was released. Measured in seconds since the Unix epoch. |
| `released_subscription` | string |  | ID of the subscription once managed by the subscription schedule (if it is released). |
| `status` | enum: `active`, `canceled`, `completed`, `not_started`, `released` | yes | The present status of the subscription schedule. Possible values are `not_started`, `active`, `completed`, `released`, and `canceled`. You can read more about the different states in our [behavior guide](https://stripe.com/docs/billing/subscriptions/subscription-schedules). |
| `subscription` | string or `subscription` |  | ID of the subscription managed by the subscription schedule. |
| `test_clock` | string or `test_helpers.test_clock` |  | ID of the test clock this subscription schedule belongs to. |

