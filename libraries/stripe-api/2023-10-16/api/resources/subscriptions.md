# Stripe API 2023-10-16 — subscriptions

Operations under `/v1/subscriptions` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/subscriptions

operationId: `GetSubscriptions`

By default, returns a list of subscriptions that have not been canceled. In order to list canceled subscriptions, specify `status=canceled`.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `automatic_tax` | object |  | Filter subscriptions by their automatic tax settings. |
| `automatic_tax.enabled` | boolean | yes |  |
| `collection_method` | enum: `charge_automatically`, `send_invoice` |  | The collection method of the subscriptions to retrieve. Either `charge_automatically` or `send_invoice`. |
| `created` | object or integer |  | Only return subscriptions that were created during the given date interval. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `current_period_end` | object or integer |  |  |
| `current_period_end.gt` | integer |  |  |
| `current_period_end.gte` | integer |  |  |
| `current_period_end.lt` | integer |  |  |
| `current_period_end.lte` | integer |  |  |
| `current_period_start` | object or integer |  |  |
| `current_period_start.gt` | integer |  |  |
| `current_period_start.gte` | integer |  |  |
| `current_period_start.lt` | integer |  |  |
| `current_period_start.lte` | integer |  |  |
| `customer` | string |  | The ID of the customer whose subscriptions will be retrieved. |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `price` | string |  | Filter for subscriptions that contain this recurring price ID. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `status` | enum: `active`, `all`, `canceled`, `ended`, `incomplete`, `incomplete_expired`, `past_due`, `paused`, `trialing`, `unpaid` |  | The status of the subscriptions to retrieve. Passing in a value of `canceled` will return all canceled subscriptions, including those belonging to deleted customers. Pass `ended` to find subscriptions that are canceled and subscriptions that are expired due to [incomplete payment](https://stripe.com/docs/billing/subscriptions/overview#subscription-statuses). Passing in a value of `all` will return subscriptions of all statuses. If no value is supplied, all subscriptions that have not been canceled are returned. |
| `test_clock` | string |  | Filter for subscriptions that are associated with the specified test clock. The response will not include subscriptions with test clocks if this and the customer parameter is not set. |

Returns: object

## POST /v1/subscriptions

operationId: `PostSubscriptions`

Creates a new subscription on an existing customer. Each customer can have up to 500 active or scheduled subscriptions.

When you create a subscription with `collection_method=charge_automatically`, the first invoice is finalized as part of the request.
The `payment_behavior` parameter determines the exact behavior of the initial payment.

To start subscriptions where the first invoice always begins in a `draft` status, use [subscription schedules](https://stripe.com/docs/billing/subscriptions/subscription-schedules#managing) instead.
Schedules provide the flexibility to model more complex billing configurations that change over time.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `add_invoice_items` | array of object |  | A list of prices and quantities that will generate invoice items appended to the next invoice for this subscription. You may pass up to 20 items. |
| `add_invoice_items[].discounts` | array of object |  |  |
| `add_invoice_items[].discounts[].coupon` | string |  |  |
| `add_invoice_items[].discounts[].discount` | string |  |  |
| `add_invoice_items[].discounts[].promotion_code` | string |  |  |
| `add_invoice_items[].price` | string |  |  |
| `add_invoice_items[].price_data` | object |  |  |
| `add_invoice_items[].price_data.currency` | string | yes |  |
| `add_invoice_items[].price_data.product` | string | yes |  |
| `add_invoice_items[].price_data.tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  |  |
| `add_invoice_items[].price_data.unit_amount` | integer |  |  |
| `add_invoice_items[].price_data.unit_amount_decimal` | string |  |  |
| `add_invoice_items[].quantity` | integer |  |  |
| `add_invoice_items[].tax_rates` | array of string or "" (to unset) |  |  |
| `application_fee_percent` | number or "" (to unset) |  | A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. The request must be made by a platform account on a connected account in order to set an application fee percentage. For more information, see the application fees [documentation](https://stripe.com/docs/connect/subscriptions#collecting-fees-on-subscriptions). |
| `automatic_tax` | object |  | Automatic tax settings for this subscription. We recommend you only include this parameter when the existing value is being changed. |
| `automatic_tax.enabled` | boolean | yes |  |
| `automatic_tax.liability` | object |  |  |
| `automatic_tax.liability.account` | string |  |  |
| `automatic_tax.liability.type` | enum: `account`, `self` | yes |  |
| `backdate_start_date` | timestamp (Unix seconds) |  | For new subscriptions, a past timestamp to backdate the subscription's start date to. If set, the first invoice will contain a proration for the timespan between the start date and the current time. Can be combined with trials and the billing cycle anchor. |
| `billing_cycle_anchor` | timestamp (Unix seconds) |  | A future timestamp in UTC format to anchor the subscription's [billing cycle](https://stripe.com/docs/subscriptions/billing-cycle). The anchor is the reference point that aligns future billing cycle dates. It sets the day of week for `week` intervals, the day of month for `month` and `year` intervals, and the month of year for `year` intervals. |
| `billing_cycle_anchor_config` | object |  | Mutually exclusive with billing_cycle_anchor and only valid with monthly and yearly price intervals. When provided, the billing_cycle_anchor is set to the next occurence of the day_of_month at the hour, minute, and second UTC. |
| `billing_cycle_anchor_config.day_of_month` | integer | yes |  |
| `billing_cycle_anchor_config.hour` | integer |  |  |
| `billing_cycle_anchor_config.minute` | integer |  |  |
| `billing_cycle_anchor_config.month` | integer |  |  |
| `billing_cycle_anchor_config.second` | integer |  |  |
| `billing_thresholds` | object or "" (to unset) |  | Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. Pass an empty string to remove previously-defined thresholds. |
| `billing_thresholds.amount_gte` | integer |  |  |
| `billing_thresholds.reset_billing_cycle_anchor` | boolean |  |  |
| `cancel_at` | timestamp (Unix seconds) |  | A timestamp at which the subscription should cancel. If set to a date before the current period ends, this will cause a proration if prorations have been enabled using `proration_behavior`. If set during a future period, this will always cause a proration for that period. |
| `cancel_at_period_end` | boolean |  | Boolean indicating whether this subscription should cancel at the end of the current period. |
| `collection_method` | enum: `charge_automatically`, `send_invoice` |  | Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this subscription at the end of the cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`. |
| `coupon` | string |  | The ID of the coupon to apply to this subscription. A coupon applied to a subscription will only affect invoices created for that particular subscription. This field has been deprecated and will be removed in a future API version. Use `discounts` instead. |
| `currency` | string |  | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `customer` | string | yes | The identifier of the customer to subscribe. |
| `days_until_due` | integer |  | Number of days a customer has to pay invoices generated by this subscription. Valid only for subscriptions where `collection_method` is set to `send_invoice`. |
| `default_payment_method` | string |  | ID of the default payment method for the subscription. It must belong to the customer associated with the subscription. This takes precedence over `default_source`. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source). |
| `default_source` | string |  | ID of the default payment source for the subscription. It must belong to the customer associated with the subscription and be in a chargeable state. If `default_payment_method` is also set, `default_payment_method` will take precedence. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source). |
| `default_tax_rates` | array of string or "" (to unset) |  | The tax rates that will apply to any subscription item that does not have `tax_rates` set. Invoices created will have their `default_tax_rates` populated from the subscription. |
| `description` | string |  | The subscription's description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs. |
| `discounts` | array of object or "" (to unset) |  | The coupons to redeem into discounts for the subscription. If not specified or empty, inherits the discount from the subscription's customer. |
| `discounts[].coupon` | string |  |  |
| `discounts[].discount` | string |  |  |
| `discounts[].promotion_code` | string |  |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `invoice_settings` | object |  | All invoices will be billed using the specified settings. |
| `invoice_settings.account_tax_ids` | array of string or "" (to unset) |  |  |
| `invoice_settings.issuer` | object |  |  |
| `invoice_settings.issuer.account` | string |  |  |
| `invoice_settings.issuer.type` | enum: `account`, `self` | yes |  |
| `items` | array of object |  | A list of up to 20 subscription items, each with an attached price. |
| `items[].billing_thresholds` | object or "" (to unset) |  |  |
| `items[].billing_thresholds.usage_gte` | integer | yes |  |
| `items[].discounts` | array of object or "" (to unset) |  |  |
| `items[].discounts[].coupon` | string |  |  |
| `items[].discounts[].discount` | string |  |  |
| `items[].discounts[].promotion_code` | string |  |  |
| `items[].metadata` | map (key → value) |  |  |
| `items[].price` | string |  |  |
| `items[].price_data` | object |  |  |
| `items[].price_data.currency` | string | yes |  |
| `items[].price_data.product` | string | yes |  |
| `items[].price_data.recurring` | object | yes |  |
| `items[].price_data.recurring.interval` | enum: `day`, `month`, `week`, `year` | yes |  |
| `items[].price_data.recurring.interval_count` | integer |  |  |
| `items[].price_data.tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  |  |
| `items[].price_data.unit_amount` | integer |  |  |
| `items[].price_data.unit_amount_decimal` | string |  |  |
| `items[].quantity` | integer |  |  |
| `items[].tax_rates` | array of string or "" (to unset) |  |  |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `off_session` | boolean |  | Indicates if a customer is on or off-session while an invoice payment is attempted. |
| `on_behalf_of` | string or "" (to unset) |  | The account on behalf of which to charge, for each of the subscription's invoices. |
| `payment_behavior` | enum: `allow_incomplete`, `default_incomplete`, `error_if_incomplete`, `pending_if_incomplete` |  | Only applies to subscriptions with `collection_method=charge_automatically`.<br>Use `allow_incomplete` to create Subscriptions with `status=incomplete` if the first invoice can't be paid. Creating Subscriptions with this status allows you to manage scenarios where additional customer actions are needed to pay a subscription's invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the [SCA Migration Guide](https://stripe.com/docs/billing/migration/strong-customer-authentication) for Billing to learn more. This is the default behavior.<br>Use `default_incomplete` to create Subscriptions with `status=incomplete` when the first invoice requires payment, otherwise start as active. Subscriptions transition to `status=active` when successfully confirming the PaymentIntent on the first invoice. This allows simpler management of scenarios where additional customer actions are needed to pay a subscription’s invoice, such as failed payments, [SCA regulation](https://stripe.com/docs/billing/migration/strong-customer-authentication), or collecting a mandate for a bank debit payment method. If the PaymentIntent is not confirmed within 23 hours Subscriptions transition to `status=incomplete_expired`, which is a terminal state.<br>Use `error_if_incomplete` if you want Stripe to return an HTTP 402 status code if a subscription's first invoice can't be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further customer action is needed, this parameter doesn't create a Subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the [changelog](https://stripe.com/docs/upgrades#2019-03-14) to learn more.<br>`pending_if_incomplete` is only used with updates and cannot be passed when creating a Subscription.<br>Subscriptions with `collection_method=send_invoice` are automatically activated regardless of the first Invoice status. |
| `payment_settings` | object |  | Payment settings to pass to invoices created by the subscription. |
| `payment_settings.payment_method_options` | object |  |  |
| `payment_settings.payment_method_options.acss_debit` | object or "" (to unset) |  |  |
| `payment_settings.payment_method_options.acss_debit.mandate_options` | object |  |  |
| `payment_settings.payment_method_options.acss_debit.mandate_options.transaction_type` | enum: `business`, `personal` |  |  |
| `payment_settings.payment_method_options.acss_debit.verification_method` | enum: `automatic`, `instant`, `microdeposits` |  |  |
| `payment_settings.payment_method_options.bancontact` | object or "" (to unset) |  |  |
| `payment_settings.payment_method_options.bancontact.preferred_language` | enum: `de`, `en`, `fr`, `nl` |  |  |
| `payment_settings.payment_method_options.card` | object or "" (to unset) |  |  |
| `payment_settings.payment_method_options.card.mandate_options` | object |  |  |
| `payment_settings.payment_method_options.card.mandate_options.amount` | integer |  |  |
| `payment_settings.payment_method_options.card.mandate_options.amount_type` | enum: `fixed`, `maximum` |  |  |
| `payment_settings.payment_method_options.card.mandate_options.description` | string |  |  |
| `payment_settings.payment_method_options.card.network` | enum: `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `interac`, `jcb`, `mastercard`, `unionpay`, `unknown`, `visa` |  |  |
| `payment_settings.payment_method_options.card.request_three_d_secure` | enum: `any`, `automatic`, `challenge` |  |  |
| `payment_settings.payment_method_options.customer_balance` | object or "" (to unset) |  |  |
| `payment_settings.payment_method_options.customer_balance.bank_transfer` | object |  |  |
| `payment_settings.payment_method_options.customer_balance.bank_transfer.eu_bank_transfer` | object |  |  |
| `payment_settings.payment_method_options.customer_balance.bank_transfer.eu_bank_transfer.country` | string | yes |  |
| `payment_settings.payment_method_options.customer_balance.bank_transfer.type` | string |  |  |
| `payment_settings.payment_method_options.customer_balance.funding_type` | string |  |  |
| `payment_settings.payment_method_options.konbini` | object or "" (to unset) |  |  |
| `payment_settings.payment_method_options.sepa_debit` | object or "" (to unset) |  |  |
| `payment_settings.payment_method_options.us_bank_account` | object or "" (to unset) |  |  |
| `payment_settings.payment_method_options.us_bank_account.financial_connections` | object |  |  |
| `payment_settings.payment_method_options.us_bank_account.financial_connections.permissions` | array of enum: `balances`, `ownership`, `payment_method`, `transactions` |  |  |
| `payment_settings.payment_method_options.us_bank_account.financial_connections.prefetch` | array of enum: `balances`, `transactions` |  |  |
| `payment_settings.payment_method_options.us_bank_account.verification_method` | enum: `automatic`, `instant`, `microdeposits` |  |  |
| `payment_settings.payment_method_types` | array of enum: `ach_credit_transfer`, `ach_debit`, `acss_debit`, `au_becs_debit`, `bacs_debit`, `bancontact`, `boleto`, `card`, `cashapp`, `customer_balance`, `eps`, `fpx`, `giropay`, `grabpay`, `ideal`, `konbini`, `link`, `p24`, `paynow`, `paypal`, `promptpay`, `sepa_debit`, `sofort`, `us_bank_account`, `wechat_pay` or "" (to unset) |  |  |
| `payment_settings.save_default_payment_method` | enum: `off`, `on_subscription` |  |  |
| `pending_invoice_item_interval` | object or "" (to unset) |  | Specifies an interval for how often to bill for any pending invoice items. It is analogous to calling [Create an invoice](https://stripe.com/docs/api#create_invoice) for the given subscription at the specified interval. |
| `pending_invoice_item_interval.interval` | enum: `day`, `month`, `week`, `year` | yes |  |
| `pending_invoice_item_interval.interval_count` | integer |  |  |
| `promotion_code` | string |  | The ID of a promotion code to apply to this subscription. A promotion code applied to a subscription will only affect invoices created for that particular subscription. This field has been deprecated and will be removed in a future API version. Use `discounts` instead. |
| `proration_behavior` | enum: `always_invoice`, `create_prorations`, `none` |  | Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) resulting from the `billing_cycle_anchor`. If no value is passed, the default is `create_prorations`. |
| `transfer_data` | object |  | If specified, the funds from the subscription's invoices will be transferred to the destination and the ID of the resulting transfers will be found on the resulting charges. |
| `transfer_data.amount_percent` | number |  |  |
| `transfer_data.destination` | string | yes |  |
| `trial_end` | enum: `now` or timestamp (Unix seconds) |  | Unix timestamp representing the end of the trial period the customer will get before being charged for the first time. If set, trial_end will override the default trial period of the plan the customer is being subscribed to. The special value `now` can be provided to end the customer's trial immediately. Can be at most two years from `billing_cycle_anchor`. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more. |
| `trial_from_plan` | boolean |  | Indicates if a plan's `trial_period_days` should be applied to the subscription. Setting `trial_end` per subscription is preferred, and this defaults to `false`. Setting this flag to `true` together with `trial_end` is not allowed. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more. |
| `trial_period_days` | integer |  | Integer representing the number of trial period days before the customer is charged for the first time. This will always overwrite any trials that might apply via a subscribed plan. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more. |
| `trial_settings` | object |  | Settings related to subscription trials. |
| `trial_settings.end_behavior` | object | yes |  |
| `trial_settings.end_behavior.missing_payment_method` | enum: `cancel`, `create_invoice`, `pause` | yes |  |

Returns: `subscription`

## GET /v1/subscriptions/search

operationId: `GetSubscriptionsSearch`

Search for subscriptions you’ve previously created using Stripe’s [Search Query Language](https://stripe.com/docs/search#search-query-language).
Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating
conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up
to an hour behind during outages. Search functionality is not available to merchants in India.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `page` | string |  | A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results. |
| `query` | string | yes | The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for subscriptions](https://stripe.com/docs/search#query-fields-for-subscriptions). |

Returns: object

## GET /v1/subscriptions/{subscription_exposed_id}

operationId: `GetSubscriptionsSubscriptionExposedId`

Retrieves the subscription with the given ID.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `subscription_exposed_id (path)` | string | yes |  |

Returns: `subscription`

## POST /v1/subscriptions/{subscription_exposed_id}

operationId: `PostSubscriptionsSubscriptionExposedId`

Updates an existing subscription to match the specified parameters.
When changing prices or quantities, we optionally prorate the price we charge next month to make up for any price changes.
To preview how the proration is calculated, use the [upcoming invoice](https://stripe.com/docs/api/invoices/upcoming) endpoint.

By default, we prorate subscription changes. For example, if a customer signs up on May 1 for a <currency>100</currency> price, they’ll be billed <currency>100</currency> immediately. If on May 15 they switch to a <currency>200</currency> price, then on June 1 they’ll be billed <currency>250</currency> (<currency>200</currency> for a renewal of her subscription, plus a <currency>50</currency> prorating adjustment for half of the previous month’s <currency>100</currency> difference). Similarly, a downgrade generates a credit that is applied to the next invoice. We also prorate when you make quantity changes.

Switching prices does not normally change the billing date or generate an immediate charge unless:

- The billing interval is changed (for example, from monthly to yearly).

- The subscription moves from free to paid, or paid to free.

- A trial starts or ends.

In these cases, we apply a credit for the unused time on the previous price, immediately charge the customer using the new price, and reset the billing date.

If you want to charge for an upgrade immediately, pass `proration_behavior` as `always_invoice` to create prorations, automatically invoice the customer for those proration adjustments, and attempt to collect payment. If you pass `create_prorations`, the prorations are created but not automatically invoiced. If you want to bill the customer for the prorations before the subscription’s renewal date, you need to manually [invoice the customer](https://stripe.com/docs/api/invoices/create).

If you don’t want to prorate, set the `proration_behavior` option to `none`. With this option, the customer is billed <currency>100</currency> on May 1 and <currency>200</currency> on June 1. Similarly, if you set `proration_behavior` to `none` when switching between different billing intervals (for example, from monthly to yearly), we don’t generate any credits for the old subscription’s unused time. We still reset the billing date and bill immediately for the new subscription.

Updating the quantity on a subscription many times in an hour may result in [rate limiting](https://stripe.com/docs/rate-limits). If you need to bill for a frequently changing quantity, consider integrating [usage-based billing](https://stripe.com/docs/billing/subscriptions/usage-based) instead.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `subscription_exposed_id (path)` | string | yes |  |
| `add_invoice_items` | array of object |  | A list of prices and quantities that will generate invoice items appended to the next invoice for this subscription. You may pass up to 20 items. |
| `add_invoice_items[].discounts` | array of object |  |  |
| `add_invoice_items[].discounts[].coupon` | string |  |  |
| `add_invoice_items[].discounts[].discount` | string |  |  |
| `add_invoice_items[].discounts[].promotion_code` | string |  |  |
| `add_invoice_items[].price` | string |  |  |
| `add_invoice_items[].price_data` | object |  |  |
| `add_invoice_items[].price_data.currency` | string | yes |  |
| `add_invoice_items[].price_data.product` | string | yes |  |
| `add_invoice_items[].price_data.tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  |  |
| `add_invoice_items[].price_data.unit_amount` | integer |  |  |
| `add_invoice_items[].price_data.unit_amount_decimal` | string |  |  |
| `add_invoice_items[].quantity` | integer |  |  |
| `add_invoice_items[].tax_rates` | array of string or "" (to unset) |  |  |
| `application_fee_percent` | number or "" (to unset) |  | A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. The request must be made by a platform account on a connected account in order to set an application fee percentage. For more information, see the application fees [documentation](https://stripe.com/docs/connect/subscriptions#collecting-fees-on-subscriptions). |
| `automatic_tax` | object |  | Automatic tax settings for this subscription. We recommend you only include this parameter when the existing value is being changed. |
| `automatic_tax.enabled` | boolean | yes |  |
| `automatic_tax.liability` | object |  |  |
| `automatic_tax.liability.account` | string |  |  |
| `automatic_tax.liability.type` | enum: `account`, `self` | yes |  |
| `billing_cycle_anchor` | enum: `now`, `unchanged` |  | Either `now` or `unchanged`. Setting the value to `now` resets the subscription's billing cycle anchor to the current time (in UTC). For more information, see the billing cycle [documentation](https://stripe.com/docs/billing/subscriptions/billing-cycle). |
| `billing_thresholds` | object or "" (to unset) |  | Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. Pass an empty string to remove previously-defined thresholds. |
| `billing_thresholds.amount_gte` | integer |  |  |
| `billing_thresholds.reset_billing_cycle_anchor` | boolean |  |  |
| `cancel_at` | timestamp (Unix seconds) or "" (to unset) |  | A timestamp at which the subscription should cancel. If set to a date before the current period ends, this will cause a proration if prorations have been enabled using `proration_behavior`. If set during a future period, this will always cause a proration for that period. |
| `cancel_at_period_end` | boolean |  | Boolean indicating whether this subscription should cancel at the end of the current period. |
| `cancellation_details` | object |  | Details about why this subscription was cancelled |
| `cancellation_details.comment` | string or "" (to unset) |  |  |
| `cancellation_details.feedback` | enum: ``, `customer_service`, `low_quality`, `missing_features`, `other`, `switched_service`, `too_complex`, `too_expensive`, `unused` |  |  |
| `collection_method` | enum: `charge_automatically`, `send_invoice` |  | Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this subscription at the end of the cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`. |
| `coupon` | string |  | The ID of the coupon to apply to this subscription. A coupon applied to a subscription will only affect invoices created for that particular subscription. This field has been deprecated and will be removed in a future API version. Use `discounts` instead. |
| `days_until_due` | integer |  | Number of days a customer has to pay invoices generated by this subscription. Valid only for subscriptions where `collection_method` is set to `send_invoice`. |
| `default_payment_method` | string |  | ID of the default payment method for the subscription. It must belong to the customer associated with the subscription. This takes precedence over `default_source`. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source). |
| `default_source` | string or "" (to unset) |  | ID of the default payment source for the subscription. It must belong to the customer associated with the subscription and be in a chargeable state. If `default_payment_method` is also set, `default_payment_method` will take precedence. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source). |
| `default_tax_rates` | array of string or "" (to unset) |  | The tax rates that will apply to any subscription item that does not have `tax_rates` set. Invoices created will have their `default_tax_rates` populated from the subscription. Pass an empty string to remove previously-defined tax rates. |
| `description` | string or "" (to unset) |  | The subscription's description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs. |
| `discounts` | array of object or "" (to unset) |  | The coupons to redeem into discounts for the subscription. If not specified or empty, inherits the discount from the subscription's customer. |
| `discounts[].coupon` | string |  |  |
| `discounts[].discount` | string |  |  |
| `discounts[].promotion_code` | string |  |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `invoice_settings` | object |  | All invoices will be billed using the specified settings. |
| `invoice_settings.account_tax_ids` | array of string or "" (to unset) |  |  |
| `invoice_settings.issuer` | object |  |  |
| `invoice_settings.issuer.account` | string |  |  |
| `invoice_settings.issuer.type` | enum: `account`, `self` | yes |  |
| `items` | array of object |  | A list of up to 20 subscription items, each with an attached price. |
| `items[].billing_thresholds` | object or "" (to unset) |  |  |
| `items[].billing_thresholds.usage_gte` | integer | yes |  |
| `items[].clear_usage` | boolean |  |  |
| `items[].deleted` | boolean |  |  |
| `items[].discounts` | array of object or "" (to unset) |  |  |
| `items[].discounts[].coupon` | string |  |  |
| `items[].discounts[].discount` | string |  |  |
| `items[].discounts[].promotion_code` | string |  |  |
| `items[].id` | string |  |  |
| `items[].metadata` | map (key → value) or "" (to unset) |  |  |
| `items[].price` | string |  |  |
| `items[].price_data` | object |  |  |
| `items[].price_data.currency` | string | yes |  |
| `items[].price_data.product` | string | yes |  |
| `items[].price_data.recurring` | object | yes |  |
| `items[].price_data.recurring.interval` | enum: `day`, `month`, `week`, `year` | yes |  |
| `items[].price_data.recurring.interval_count` | integer |  |  |
| `items[].price_data.tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  |  |
| `items[].price_data.unit_amount` | integer |  |  |
| `items[].price_data.unit_amount_decimal` | string |  |  |
| `items[].quantity` | integer |  |  |
| `items[].tax_rates` | array of string or "" (to unset) |  |  |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `off_session` | boolean |  | Indicates if a customer is on or off-session while an invoice payment is attempted. |
| `on_behalf_of` | string or "" (to unset) |  | The account on behalf of which to charge, for each of the subscription's invoices. |
| `pause_collection` | object or "" (to unset) |  | If specified, payment collection for this subscription will be paused. Note that the subscription status will be unchanged and will not be updated to `paused`. Learn more about [pausing collection](/billing/subscriptions/pause-payment). |
| `pause_collection.behavior` | enum: `keep_as_draft`, `mark_uncollectible`, `void` | yes |  |
| `pause_collection.resumes_at` | timestamp (Unix seconds) |  |  |
| `payment_behavior` | enum: `allow_incomplete`, `default_incomplete`, `error_if_incomplete`, `pending_if_incomplete` |  | Use `allow_incomplete` to transition the subscription to `status=past_due` if a payment is required but cannot be paid. This allows you to manage scenarios where additional user actions are needed to pay a subscription's invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the [SCA Migration Guide](https://stripe.com/docs/billing/migration/strong-customer-authentication) for Billing to learn more. This is the default behavior.<br>Use `default_incomplete` to transition the subscription to `status=past_due` when payment is required and await explicit confirmation of the invoice's payment intent. This allows simpler management of scenarios where additional user actions are needed to pay a subscription’s invoice. Such as failed payments, [SCA regulation](https://stripe.com/docs/billing/migration/strong-customer-authentication), or collecting a mandate for a bank debit payment method.<br>Use `pending_if_incomplete` to update the subscription using [pending updates](https://stripe.com/docs/billing/subscriptions/pending-updates). When you use `pending_if_incomplete` you can only pass the parameters [supported by pending updates](https://stripe.com/docs/billing/pending-updates-reference#supported-attributes).<br>Use `error_if_incomplete` if you want Stripe to return an HTTP 402 status code if a subscription's invoice cannot be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further user action is needed, this parameter does not update the subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the [changelog](https://stripe.com/docs/upgrades#2019-03-14) to learn more. |
| `payment_settings` | object |  | Payment settings to pass to invoices created by the subscription. |
| `payment_settings.payment_method_options` | object |  |  |
| `payment_settings.payment_method_options.acss_debit` | object or "" (to unset) |  |  |
| `payment_settings.payment_method_options.acss_debit.mandate_options` | object |  |  |
| `payment_settings.payment_method_options.acss_debit.mandate_options.transaction_type` | enum: `business`, `personal` |  |  |
| `payment_settings.payment_method_options.acss_debit.verification_method` | enum: `automatic`, `instant`, `microdeposits` |  |  |
| `payment_settings.payment_method_options.bancontact` | object or "" (to unset) |  |  |
| `payment_settings.payment_method_options.bancontact.preferred_language` | enum: `de`, `en`, `fr`, `nl` |  |  |
| `payment_settings.payment_method_options.card` | object or "" (to unset) |  |  |
| `payment_settings.payment_method_options.card.mandate_options` | object |  |  |
| `payment_settings.payment_method_options.card.mandate_options.amount` | integer |  |  |
| `payment_settings.payment_method_options.card.mandate_options.amount_type` | enum: `fixed`, `maximum` |  |  |
| `payment_settings.payment_method_options.card.mandate_options.description` | string |  |  |
| `payment_settings.payment_method_options.card.network` | enum: `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `interac`, `jcb`, `mastercard`, `unionpay`, `unknown`, `visa` |  |  |
| `payment_settings.payment_method_options.card.request_three_d_secure` | enum: `any`, `automatic`, `challenge` |  |  |
| `payment_settings.payment_method_options.customer_balance` | object or "" (to unset) |  |  |
| `payment_settings.payment_method_options.customer_balance.bank_transfer` | object |  |  |
| `payment_settings.payment_method_options.customer_balance.bank_transfer.eu_bank_transfer` | object |  |  |
| `payment_settings.payment_method_options.customer_balance.bank_transfer.eu_bank_transfer.country` | string | yes |  |
| `payment_settings.payment_method_options.customer_balance.bank_transfer.type` | string |  |  |
| `payment_settings.payment_method_options.customer_balance.funding_type` | string |  |  |
| `payment_settings.payment_method_options.konbini` | object or "" (to unset) |  |  |
| `payment_settings.payment_method_options.sepa_debit` | object or "" (to unset) |  |  |
| `payment_settings.payment_method_options.us_bank_account` | object or "" (to unset) |  |  |
| `payment_settings.payment_method_options.us_bank_account.financial_connections` | object |  |  |
| `payment_settings.payment_method_options.us_bank_account.financial_connections.permissions` | array of enum: `balances`, `ownership`, `payment_method`, `transactions` |  |  |
| `payment_settings.payment_method_options.us_bank_account.financial_connections.prefetch` | array of enum: `balances`, `transactions` |  |  |
| `payment_settings.payment_method_options.us_bank_account.verification_method` | enum: `automatic`, `instant`, `microdeposits` |  |  |
| `payment_settings.payment_method_types` | array of enum: `ach_credit_transfer`, `ach_debit`, `acss_debit`, `au_becs_debit`, `bacs_debit`, `bancontact`, `boleto`, `card`, `cashapp`, `customer_balance`, `eps`, `fpx`, `giropay`, `grabpay`, `ideal`, `konbini`, `link`, `p24`, `paynow`, `paypal`, `promptpay`, `sepa_debit`, `sofort`, `us_bank_account`, `wechat_pay` or "" (to unset) |  |  |
| `payment_settings.save_default_payment_method` | enum: `off`, `on_subscription` |  |  |
| `pending_invoice_item_interval` | object or "" (to unset) |  | Specifies an interval for how often to bill for any pending invoice items. It is analogous to calling [Create an invoice](https://stripe.com/docs/api#create_invoice) for the given subscription at the specified interval. |
| `pending_invoice_item_interval.interval` | enum: `day`, `month`, `week`, `year` | yes |  |
| `pending_invoice_item_interval.interval_count` | integer |  |  |
| `promotion_code` | string |  | The promotion code to apply to this subscription. A promotion code applied to a subscription will only affect invoices created for that particular subscription. |
| `proration_behavior` | enum: `always_invoice`, `create_prorations`, `none` |  | Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) when the billing cycle changes (e.g., when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial), or if an item's `quantity` changes. The default value is `create_prorations`. |
| `proration_date` | timestamp (Unix seconds) |  | If set, the proration will be calculated as though the subscription was updated at the given time. This can be used to apply exactly the same proration that was previewed with [upcoming invoice](https://stripe.com/docs/api#upcoming_invoice) endpoint. It can also be used to implement custom proration logic, such as prorating by day instead of by second, by providing the time that you wish to use for proration calculations. |
| `transfer_data` | object or "" (to unset) |  | If specified, the funds from the subscription's invoices will be transferred to the destination and the ID of the resulting transfers will be found on the resulting charges. This will be unset if you POST an empty value. |
| `transfer_data.amount_percent` | number |  |  |
| `transfer_data.destination` | string | yes |  |
| `trial_end` | enum: `now` or timestamp (Unix seconds) |  | Unix timestamp representing the end of the trial period the customer will get before being charged for the first time. This will always overwrite any trials that might apply via a subscribed plan. If set, trial_end will override the default trial period of the plan the customer is being subscribed to. The special value `now` can be provided to end the customer's trial immediately. Can be at most two years from `billing_cycle_anchor`. |
| `trial_from_plan` | boolean |  | Indicates if a plan's `trial_period_days` should be applied to the subscription. Setting `trial_end` per subscription is preferred, and this defaults to `false`. Setting this flag to `true` together with `trial_end` is not allowed. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more. |
| `trial_settings` | object |  | Settings related to subscription trials. |
| `trial_settings.end_behavior` | object | yes |  |
| `trial_settings.end_behavior.missing_payment_method` | enum: `cancel`, `create_invoice`, `pause` | yes |  |

Returns: `subscription`

## DELETE /v1/subscriptions/{subscription_exposed_id}

operationId: `DeleteSubscriptionsSubscriptionExposedId`

Cancels a customer’s subscription immediately. The customer will not be charged again for the subscription.

Note, however, that any pending invoice items that you’ve created will still be charged for at the end of the period, unless manually [deleted](#delete_invoiceitem). If you’ve set the subscription to cancel at the end of the period, any pending prorations will also be left in place and collected at the end of the period. But if the subscription is set to cancel immediately, pending prorations will be removed.

By default, upon subscription cancellation, Stripe will stop automatic collection of all finalized invoices for the customer. This is intended to prevent unexpected payment attempts after the customer has canceled a subscription. However, you can resume automatic collection of the invoices manually after subscription cancellation to have us proceed. Or, you could check for unpaid invoices before allowing the customer to cancel the subscription at all.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `subscription_exposed_id (path)` | string | yes |  |
| `cancellation_details` | object |  | Details about why this subscription was cancelled |
| `cancellation_details.comment` | string or "" (to unset) |  |  |
| `cancellation_details.feedback` | enum: ``, `customer_service`, `low_quality`, `missing_features`, `other`, `switched_service`, `too_complex`, `too_expensive`, `unused` |  |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `invoice_now` | boolean |  | Will generate a final invoice that invoices for any un-invoiced metered usage and new/pending proration invoice items. |
| `prorate` | boolean |  | Will generate a proration invoice item that credits remaining unused time until the subscription period end. |

Returns: `subscription`

## DELETE /v1/subscriptions/{subscription_exposed_id}/discount

operationId: `DeleteSubscriptionsSubscriptionExposedIdDiscount`

Removes the currently applied discount on a subscription.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `subscription_exposed_id (path)` | string | yes |  |

Returns: `deleted_discount`

## POST /v1/subscriptions/{subscription}/resume

operationId: `PostSubscriptionsSubscriptionResume`

Initiates resumption of a paused subscription, optionally resetting the billing cycle anchor and creating prorations. If a resumption invoice is generated, it must be paid or marked uncollectible before the subscription will be unpaused. If payment succeeds the subscription will become `active`, and if payment fails the subscription will be `past_due`. The resumption invoice will void automatically if not paid by the expiration date.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `subscription (path)` | string | yes |  |
| `billing_cycle_anchor` | enum: `now`, `unchanged` |  | Either `now` or `unchanged`. Setting the value to `now` resets the subscription's billing cycle anchor to the current time (in UTC). Setting the value to `unchanged` advances the subscription's billing cycle anchor to the period that surrounds the current time. For more information, see the billing cycle [documentation](https://stripe.com/docs/billing/subscriptions/billing-cycle). |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `proration_behavior` | enum: `always_invoice`, `create_prorations`, `none` |  | Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) when the billing cycle changes (e.g., when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial), or if an item's `quantity` changes. The default value is `create_prorations`. |
| `proration_date` | timestamp (Unix seconds) |  | If set, the proration will be calculated as though the subscription was resumed at the given time. This can be used to apply exactly the same proration that was previewed with [upcoming invoice](https://stripe.com/docs/api#retrieve_customer_invoice) endpoint. |

Returns: `subscription`

# Objects returned

## The `subscription` object

Subscriptions allow you to charge a customer on a recurring basis.

Related guide: [Creating subscriptions](https://stripe.com/docs/billing/subscriptions/creating)

Expandable fields (pass `expand[]=<field>`): `application`, `automatic_tax`, `billing_cycle_anchor_config`, `billing_thresholds`, `cancellation_details`, `customer`, `default_payment_method`, `default_source`, `default_tax_rates`, `discount`, `discounts`, `items`, `latest_invoice`, `on_behalf_of`, `pause_collection`, `payment_settings`, `pending_invoice_item_interval`, `pending_setup_intent`, `pending_update`, `schedule`, `test_clock`, `transfer_data`, `trial_settings`

| Field | Type | Required | Description |
|---|---|---|---|
| `application` | string or `application` or `deleted_application` |  | ID of the Connect Application that created the subscription. |
| `application_fee_percent` | number |  | A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. |
| `automatic_tax` | `subscription_automatic_tax` | yes |  |
| `billing_cycle_anchor` | timestamp (Unix seconds) | yes | The reference point that aligns future [billing cycle](https://stripe.com/docs/subscriptions/billing-cycle) dates. It sets the day of week for `week` intervals, the day of month for `month` and `year` intervals, and the month of year for `year` intervals. The timestamp is in UTC format. |
| `billing_cycle_anchor_config` | `subscriptions_resource_billing_cycle_anchor_config` |  | The fixed values used to calculate the `billing_cycle_anchor`. |
| `billing_thresholds` | `subscription_billing_thresholds` |  | Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period |
| `cancel_at` | timestamp (Unix seconds) |  | A date in the future at which the subscription will automatically get canceled |
| `cancel_at_period_end` | boolean | yes | If the subscription has been canceled with the `at_period_end` flag set to `true`, `cancel_at_period_end` on the subscription will be true. You can use this attribute to determine whether a subscription that has a status of active is scheduled to be canceled at the end of the current period. |
| `canceled_at` | timestamp (Unix seconds) |  | If the subscription has been canceled, the date of that cancellation. If the subscription was canceled with `cancel_at_period_end`, `canceled_at` will reflect the time of the most recent update request, not the end of the subscription period when the subscription is automatically moved to a canceled state. |
| `cancellation_details` | `cancellation_details` |  | Details about why this subscription was cancelled |
| `collection_method` | enum: `charge_automatically`, `send_invoice` | yes | Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this subscription at the end of the cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `current_period_end` | timestamp (Unix seconds) | yes | End of the current period that the subscription has been invoiced for. At the end of this period, a new invoice will be created. |
| `current_period_start` | timestamp (Unix seconds) | yes | Start of the current period that the subscription has been invoiced for. |
| `customer` | string or `customer` or `deleted_customer` | yes | ID of the customer who owns the subscription. |
| `days_until_due` | integer |  | Number of days a customer has to pay invoices generated by this subscription. This value will be `null` for subscriptions where `collection_method=charge_automatically`. |
| `default_payment_method` | string or `payment_method` |  | ID of the default payment method for the subscription. It must belong to the customer associated with the subscription. This takes precedence over `default_source`. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source). |
| `default_source` | string or `bank_account` or `card` or `source` |  | ID of the default payment source for the subscription. It must belong to the customer associated with the subscription and be in a chargeable state. If `default_payment_method` is also set, `default_payment_method` will take precedence. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source). |
| `default_tax_rates` | array of `tax_rate` |  | The tax rates that will apply to any subscription item that does not have `tax_rates` set. Invoices created will have their `default_tax_rates` populated from the subscription. |
| `description` | string |  | The subscription's description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs. |
| `discount` | `discount` |  | Describes the current discount applied to this subscription, if there is one. When billing, a discount applied to a subscription overrides a discount applied on a customer-wide basis. This field has been deprecated and will be removed in a future API version. Use `discounts` instead. |
| `discounts` | array of string or `discount` | yes | The discounts applied to the subscription. Subscription item discounts are applied before subscription discounts. Use `expand[]=discounts` to expand each discount. |
| `ended_at` | timestamp (Unix seconds) |  | If the subscription has ended, the date the subscription ended. |
| `id` | string | yes | Unique identifier for the object. |
| `items` | object | yes | List of subscription items, each with an attached price. |
| `latest_invoice` | string or `invoice` |  | The most recent invoice this subscription has generated. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) | yes | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `next_pending_invoice_item_invoice` | timestamp (Unix seconds) |  | Specifies the approximate timestamp on which any pending invoice items will be billed according to the schedule provided at `pending_invoice_item_interval`. |
| `object` | enum: `subscription` | yes | String representing the object's type. Objects of the same type share the same value. |
| `on_behalf_of` | string or `account` |  | The account (if any) the charge was made on behalf of for charges associated with this subscription. See the Connect documentation for details. |
| `pause_collection` | `subscriptions_resource_pause_collection` |  | If specified, payment collection for this subscription will be paused. Note that the subscription status will be unchanged and will not be updated to `paused`. Learn more about [pausing collection](/billing/subscriptions/pause-payment). |
| `payment_settings` | `subscriptions_resource_payment_settings` |  | Payment settings passed on to invoices created by the subscription. |
| `pending_invoice_item_interval` | `subscription_pending_invoice_item_interval` |  | Specifies an interval for how often to bill for any pending invoice items. It is analogous to calling [Create an invoice](https://stripe.com/docs/api#create_invoice) for the given subscription at the specified interval. |
| `pending_setup_intent` | string or `setup_intent` |  | You can use this [SetupIntent](https://stripe.com/docs/api/setup_intents) to collect user authentication when creating a subscription without immediate payment or updating a subscription's payment method, allowing you to optimize for off-session payments. Learn more in the [SCA Migration Guide](https://stripe.com/docs/billing/migration/strong-customer-authentication#scenario-2). |
| `pending_update` | `subscriptions_resource_pending_update` |  | If specified, [pending updates](https://stripe.com/docs/billing/subscriptions/pending-updates) that will be applied to the subscription once the `latest_invoice` has been paid. |
| `schedule` | string or `subscription_schedule` |  | The schedule attached to the subscription |
| `start_date` | timestamp (Unix seconds) | yes | Date when the subscription was first created. The date might differ from the `created` date due to backdating. |
| `status` | enum: `active`, `canceled`, `incomplete`, `incomplete_expired`, `past_due`, `paused`, `trialing`, `unpaid` | yes | Possible values are `incomplete`, `incomplete_expired`, `trialing`, `active`, `past_due`, `canceled`, `unpaid`, or `paused`. <br>For `collection_method=charge_automatically` a subscription moves into `incomplete` if the initial payment attempt fails. A subscription in this status can only have metadata and default_source updated. Once the first invoice is paid, the subscription moves into an `active` status. If the first invoice is not paid within 23 hours, the subscription transitions to `incomplete_expired`. This is a terminal status, the open invoice will be voided and no further invoices will be generated. <br>A subscription that is currently in a trial period is `trialing` and moves to `active` when the trial period is over. <br>A subscription can only enter a `paused` status [when a trial ends without a payment method](/billing/subscriptions/trials#create-free-trials-without-payment). A `paused` subscription doesn't generate invoices and can be resumed after your customer adds their payment method. The `paused` status is different from [pausing collection](/billing/subscriptions/pause-payment), which still generates invoices and leaves the subscription's status unchanged. <br>If subscription `collection_method=charge_automatically`, it becomes `past_due` when payment is required but cannot be paid (due to failed payment or awaiting additional user actions). Once Stripe has exhausted all payment retry attempts, the subscription will become `canceled` or `unpaid` (depending on your subscriptions settings). <br>If subscription `collection_method=send_invoice` it becomes `past_due` when its invoice is not paid by the due date, and `canceled` or `unpaid` if it is still not paid by an additional deadline after that. Note that when a subscription has a status of `unpaid`, no subsequent invoices will be attempted (invoices will be created, but then immediately automatically closed). After receiving updated payment information from a customer, you may choose to reopen and pay their closed invoices. |
| `test_clock` | string or `test_helpers.test_clock` |  | ID of the test clock this subscription belongs to. |
| `transfer_data` | `subscription_transfer_data` |  | The account (if any) the subscription's payments will be attributed to for tax reporting, and where funds from each payment will be transferred to for each of the subscription's invoices. |
| `trial_end` | timestamp (Unix seconds) |  | If the subscription has a trial, the end of that trial. |
| `trial_settings` | `subscriptions_trials_resource_trial_settings` |  | Settings related to subscription trials. |
| `trial_start` | timestamp (Unix seconds) |  | If the subscription has a trial, the beginning of that trial. |

## The `deleted_discount` object

Expandable fields (pass `expand[]=<field>`): `coupon`, `customer`, `promotion_code`

| Field | Type | Required | Description |
|---|---|---|---|
| `checkout_session` | string |  | The Checkout session that this coupon is applied to, if it is applied to a particular session in payment mode. Will not be present for subscription mode. |
| `coupon` | `coupon` | yes |  |
| `customer` | string or `customer` or `deleted_customer` |  | The ID of the customer associated with this discount. |
| `deleted` | enum: `True` | yes | Always true for a deleted object |
| `id` | string | yes | The ID of the discount object. Discounts cannot be fetched by ID. Use `expand[]=discounts` in API calls to expand discount IDs in an array. |
| `invoice` | string |  | The invoice that the discount's coupon was applied to, if it was applied directly to a particular invoice. |
| `invoice_item` | string |  | The invoice item `id` (or invoice line item `id` for invoice line items of type='subscription') that the discount's coupon was applied to, if it was applied directly to a particular invoice item or invoice line item. |
| `object` | enum: `discount` | yes | String representing the object's type. Objects of the same type share the same value. |
| `promotion_code` | string or `promotion_code` |  | The promotion code applied to create this discount. |
| `start` | timestamp (Unix seconds) | yes | Date that the coupon was applied. |
| `subscription` | string |  | The subscription that this coupon is applied to, if it is applied to a particular subscription. |
| `subscription_item` | string |  | The subscription item that this coupon is applied to, if it is applied to a particular subscription item. |

