# Stripe API 2023-10-16 — subscription items

Operations under `/v1/subscription_items` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/subscription_items

operationId: `GetSubscriptionItems`

Returns a list of your subscription items for a given subscription.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `subscription` | string | yes | The ID of the subscription whose items will be retrieved. |

Returns: object

## POST /v1/subscription_items

operationId: `PostSubscriptionItems`

Adds a new item to an existing subscription. No existing items will be changed or replaced.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `billing_thresholds` | object or "" (to unset) |  | Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. When updating, pass an empty string to remove previously-defined thresholds. |
| `billing_thresholds.usage_gte` | integer | yes |  |
| `discounts` | array of object or "" (to unset) |  | The coupons to redeem into discounts for the subscription item. |
| `discounts[].coupon` | string |  |  |
| `discounts[].discount` | string |  |  |
| `discounts[].promotion_code` | string |  |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `payment_behavior` | enum: `allow_incomplete`, `default_incomplete`, `error_if_incomplete`, `pending_if_incomplete` |  | Use `allow_incomplete` to transition the subscription to `status=past_due` if a payment is required but cannot be paid. This allows you to manage scenarios where additional user actions are needed to pay a subscription's invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the [SCA Migration Guide](https://stripe.com/docs/billing/migration/strong-customer-authentication) for Billing to learn more. This is the default behavior.<br>Use `default_incomplete` to transition the subscription to `status=past_due` when payment is required and await explicit confirmation of the invoice's payment intent. This allows simpler management of scenarios where additional user actions are needed to pay a subscription’s invoice. Such as failed payments, [SCA regulation](https://stripe.com/docs/billing/migration/strong-customer-authentication), or collecting a mandate for a bank debit payment method.<br>Use `pending_if_incomplete` to update the subscription using [pending updates](https://stripe.com/docs/billing/subscriptions/pending-updates). When you use `pending_if_incomplete` you can only pass the parameters [supported by pending updates](https://stripe.com/docs/billing/pending-updates-reference#supported-attributes).<br>Use `error_if_incomplete` if you want Stripe to return an HTTP 402 status code if a subscription's invoice cannot be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further user action is needed, this parameter does not update the subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the [changelog](https://stripe.com/docs/upgrades#2019-03-14) to learn more. |
| `price` | string |  | The ID of the price object. |
| `price_data` | object |  | Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline. |
| `price_data.currency` | string | yes |  |
| `price_data.product` | string | yes |  |
| `price_data.recurring` | object | yes |  |
| `price_data.recurring.interval` | enum: `day`, `month`, `week`, `year` | yes |  |
| `price_data.recurring.interval_count` | integer |  |  |
| `price_data.tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  |  |
| `price_data.unit_amount` | integer |  |  |
| `price_data.unit_amount_decimal` | string |  |  |
| `proration_behavior` | enum: `always_invoice`, `create_prorations`, `none` |  | Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) when the billing cycle changes (e.g., when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial), or if an item's `quantity` changes. The default value is `create_prorations`. |
| `proration_date` | timestamp (Unix seconds) |  | If set, the proration will be calculated as though the subscription was updated at the given time. This can be used to apply the same proration that was previewed with the [upcoming invoice](https://stripe.com/docs/api#retrieve_customer_invoice) endpoint. |
| `quantity` | integer |  | The quantity you'd like to apply to the subscription item you're creating. |
| `subscription` | string | yes | The identifier of the subscription to modify. |
| `tax_rates` | array of string or "" (to unset) |  | A list of [Tax Rate](https://stripe.com/docs/api/tax_rates) ids. These Tax Rates will override the [`default_tax_rates`](https://stripe.com/docs/api/subscriptions/create#create_subscription-default_tax_rates) on the Subscription. When updating, pass an empty string to remove previously-defined tax rates. |

Returns: `subscription_item`

## GET /v1/subscription_items/{item}

operationId: `GetSubscriptionItemsItem`

Retrieves the subscription item with the given ID.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `item (path)` | string | yes |  |

Returns: `subscription_item`

## POST /v1/subscription_items/{item}

operationId: `PostSubscriptionItemsItem`

Updates the plan or quantity of an item on a current subscription.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `item (path)` | string | yes |  |
| `billing_thresholds` | object or "" (to unset) |  | Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. When updating, pass an empty string to remove previously-defined thresholds. |
| `billing_thresholds.usage_gte` | integer | yes |  |
| `discounts` | array of object or "" (to unset) |  | The coupons to redeem into discounts for the subscription item. |
| `discounts[].coupon` | string |  |  |
| `discounts[].discount` | string |  |  |
| `discounts[].promotion_code` | string |  |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `off_session` | boolean |  | Indicates if a customer is on or off-session while an invoice payment is attempted. |
| `payment_behavior` | enum: `allow_incomplete`, `default_incomplete`, `error_if_incomplete`, `pending_if_incomplete` |  | Use `allow_incomplete` to transition the subscription to `status=past_due` if a payment is required but cannot be paid. This allows you to manage scenarios where additional user actions are needed to pay a subscription's invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the [SCA Migration Guide](https://stripe.com/docs/billing/migration/strong-customer-authentication) for Billing to learn more. This is the default behavior.<br>Use `default_incomplete` to transition the subscription to `status=past_due` when payment is required and await explicit confirmation of the invoice's payment intent. This allows simpler management of scenarios where additional user actions are needed to pay a subscription’s invoice. Such as failed payments, [SCA regulation](https://stripe.com/docs/billing/migration/strong-customer-authentication), or collecting a mandate for a bank debit payment method.<br>Use `pending_if_incomplete` to update the subscription using [pending updates](https://stripe.com/docs/billing/subscriptions/pending-updates). When you use `pending_if_incomplete` you can only pass the parameters [supported by pending updates](https://stripe.com/docs/billing/pending-updates-reference#supported-attributes).<br>Use `error_if_incomplete` if you want Stripe to return an HTTP 402 status code if a subscription's invoice cannot be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further user action is needed, this parameter does not update the subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the [changelog](https://stripe.com/docs/upgrades#2019-03-14) to learn more. |
| `price` | string |  | The ID of the price object. When changing a subscription item's price, `quantity` is set to 1 unless a `quantity` parameter is provided. |
| `price_data` | object |  | Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline. |
| `price_data.currency` | string | yes |  |
| `price_data.product` | string | yes |  |
| `price_data.recurring` | object | yes |  |
| `price_data.recurring.interval` | enum: `day`, `month`, `week`, `year` | yes |  |
| `price_data.recurring.interval_count` | integer |  |  |
| `price_data.tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  |  |
| `price_data.unit_amount` | integer |  |  |
| `price_data.unit_amount_decimal` | string |  |  |
| `proration_behavior` | enum: `always_invoice`, `create_prorations`, `none` |  | Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) when the billing cycle changes (e.g., when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial), or if an item's `quantity` changes. The default value is `create_prorations`. |
| `proration_date` | timestamp (Unix seconds) |  | If set, the proration will be calculated as though the subscription was updated at the given time. This can be used to apply the same proration that was previewed with the [upcoming invoice](https://stripe.com/docs/api#retrieve_customer_invoice) endpoint. |
| `quantity` | integer |  | The quantity you'd like to apply to the subscription item you're creating. |
| `tax_rates` | array of string or "" (to unset) |  | A list of [Tax Rate](https://stripe.com/docs/api/tax_rates) ids. These Tax Rates will override the [`default_tax_rates`](https://stripe.com/docs/api/subscriptions/create#create_subscription-default_tax_rates) on the Subscription. When updating, pass an empty string to remove previously-defined tax rates. |

Returns: `subscription_item`

## DELETE /v1/subscription_items/{item}

operationId: `DeleteSubscriptionItemsItem`

Deletes an item from the subscription. Removing a subscription item from a subscription will not cancel the subscription.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `item (path)` | string | yes |  |
| `clear_usage` | boolean |  | Delete all usage for the given subscription item. Allowed only when the current plan's `usage_type` is `metered`. |
| `proration_behavior` | enum: `always_invoice`, `create_prorations`, `none` |  | Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) when the billing cycle changes (e.g., when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial), or if an item's `quantity` changes. The default value is `create_prorations`. |
| `proration_date` | timestamp (Unix seconds) |  | If set, the proration will be calculated as though the subscription was updated at the given time. This can be used to apply the same proration that was previewed with the [upcoming invoice](https://stripe.com/docs/api#retrieve_customer_invoice) endpoint. |

Returns: `deleted_subscription_item`

## GET /v1/subscription_items/{subscription_item}/usage_record_summaries

operationId: `GetSubscriptionItemsSubscriptionItemUsageRecordSummaries`

For the specified subscription item, returns a list of summary objects. Each object in the list provides usage information that’s been summarized from multiple usage records and over a subscription billing period (e.g., 15 usage records in the month of September).

The list is sorted in reverse-chronological order (newest first). The first list item represents the most current usage period that hasn’t ended yet. Since new usage records can still be added, the returned summary information for the subscription item’s ID should be seen as unstable until the subscription billing period ends.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `subscription_item (path)` | string | yes |  |

Returns: object

## POST /v1/subscription_items/{subscription_item}/usage_records

operationId: `PostSubscriptionItemsSubscriptionItemUsageRecords`

Creates a usage record for a specified subscription item and date, and fills it with a quantity.

Usage records provide `quantity` information that Stripe uses to track how much a customer is using your service. With usage information and the pricing model set up by the [metered billing](https://stripe.com/docs/billing/subscriptions/metered-billing) plan, Stripe helps you send accurate invoices to your customers.

The default calculation for usage is to add up all the `quantity` values of the usage records within a billing period. You can change this default behavior with the billing plan’s `aggregate_usage` [parameter](https://stripe.com/docs/api/plans/create#create_plan-aggregate_usage). When there is more than one usage record with the same timestamp, Stripe adds the `quantity` values together. In most cases, this is the desired resolution, however, you can change this behavior with the `action` parameter.

The default pricing model for metered billing is [per-unit pricing](https://stripe.com/docs/api/plans/object#plan_object-billing_scheme). For finer granularity, you can configure metered billing to have a [tiered pricing](https://stripe.com/docs/billing/subscriptions/tiers) model.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `subscription_item (path)` | string | yes |  |
| `action` | enum: `increment`, `set` |  | Valid values are `increment` (default) or `set`. When using `increment` the specified `quantity` will be added to the usage at the specified timestamp. The `set` action will overwrite the usage quantity at that timestamp. If the subscription has [billing thresholds](https://stripe.com/docs/api/subscriptions/object#subscription_object-billing_thresholds), `increment` is the only allowed value. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `quantity` | integer | yes | The usage quantity for the specified timestamp. |
| `timestamp` | enum: `now` or timestamp (Unix seconds) |  | The timestamp for the usage event. This timestamp must be within the current billing period of the subscription of the provided `subscription_item`, and must not be in the future. When passing `"now"`, Stripe records usage for the current time. Default is `"now"` if a value is not provided. |

Returns: `usage_record`

# Objects returned

## The `subscription_item` object

Subscription items allow you to create customer subscriptions with more than
one plan, making it easy to represent complex billing relationships.

Expandable fields (pass `expand[]=<field>`): `billing_thresholds`, `discounts`, `price`, `tax_rates`

| Field | Type | Required | Description |
|---|---|---|---|
| `billing_thresholds` | `subscription_item_billing_thresholds` |  | Define thresholds at which an invoice will be sent, and the related subscription advanced to a new billing period |
| `created` | integer | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `discounts` | array of string or `discount` | yes | The discounts applied to the subscription item. Subscription item discounts are applied before subscription discounts. Use `expand[]=discounts` to expand each discount. |
| `id` | string | yes | Unique identifier for the object. |
| `metadata` | map (key → value) | yes | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `object` | enum: `subscription_item` | yes | String representing the object's type. Objects of the same type share the same value. |
| `price` | `price` | yes |  |
| `quantity` | integer |  | The [quantity](https://stripe.com/docs/subscriptions/quantities) of the plan to which the customer should be subscribed. |
| `subscription` | string | yes | The `subscription` this `subscription_item` belongs to. |
| `tax_rates` | array of `tax_rate` |  | The tax rates which apply to this `subscription_item`. When set, the `default_tax_rates` on the subscription do not apply to this `subscription_item`. |

## The `deleted_subscription_item` object

| Field | Type | Required | Description |
|---|---|---|---|
| `deleted` | enum: `True` | yes | Always true for a deleted object |
| `id` | string | yes | Unique identifier for the object. |
| `object` | enum: `subscription_item` | yes | String representing the object's type. Objects of the same type share the same value. |

## The `usage_record` object

Usage records allow you to report customer usage and metrics to Stripe for
metered billing of subscription prices.

Related guide: [Metered billing](https://stripe.com/docs/billing/subscriptions/metered-billing)

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `object` | enum: `usage_record` | yes | String representing the object's type. Objects of the same type share the same value. |
| `quantity` | integer | yes | The usage quantity for the specified date. |
| `subscription_item` | string | yes | The ID of the subscription item this usage record contains data for. |
| `timestamp` | timestamp (Unix seconds) | yes | The timestamp when this usage occurred. |

