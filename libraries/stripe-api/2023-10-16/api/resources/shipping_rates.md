# Stripe API 2023-10-16 — shipping rates

Operations under `/v1/shipping_rates` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/shipping_rates

operationId: `GetShippingRates`

Returns a list of your shipping rates.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `active` | boolean |  | Only return shipping rates that are active or inactive. |
| `created` | object or integer |  | A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `currency` | string |  | Only return shipping rates for the given currency. |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/shipping_rates

operationId: `PostShippingRates`

Creates a new shipping rate object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `delivery_estimate` | object |  | The estimated range for how long shipping will take, meant to be displayable to the customer. This will appear on CheckoutSessions. |
| `delivery_estimate.maximum` | object |  |  |
| `delivery_estimate.maximum.unit` | enum: `business_day`, `day`, `hour`, `month`, `week` | yes |  |
| `delivery_estimate.maximum.value` | integer | yes |  |
| `delivery_estimate.minimum` | object |  |  |
| `delivery_estimate.minimum.unit` | enum: `business_day`, `day`, `hour`, `month`, `week` | yes |  |
| `delivery_estimate.minimum.value` | integer | yes |  |
| `display_name` | string | yes | The name of the shipping rate, meant to be displayable to the customer. This will appear on CheckoutSessions. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `fixed_amount` | object |  | Describes a fixed amount to charge for shipping. Must be present if type is `fixed_amount`. |
| `fixed_amount.amount` | integer | yes |  |
| `fixed_amount.currency` | string | yes |  |
| `fixed_amount.currency_options` | map (key → value) |  |  |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  | Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. |
| `tax_code` | string |  | A [tax code](https://stripe.com/docs/tax/tax-categories) ID. The Shipping tax code is `txcd_92010001`. |
| `type` | enum: `fixed_amount` |  | The type of calculation to use on the shipping rate. Can only be `fixed_amount` for now. |

Returns: `shipping_rate`

## GET /v1/shipping_rates/{shipping_rate_token}

operationId: `GetShippingRatesShippingRateToken`

Returns the shipping rate object with the given ID.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `shipping_rate_token (path)` | string | yes |  |

Returns: `shipping_rate`

## POST /v1/shipping_rates/{shipping_rate_token}

operationId: `PostShippingRatesShippingRateToken`

Updates an existing shipping rate object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `shipping_rate_token (path)` | string | yes |  |
| `active` | boolean |  | Whether the shipping rate can be used for new purchases. Defaults to `true`. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `fixed_amount` | object |  | Describes a fixed amount to charge for shipping. Must be present if type is `fixed_amount`. |
| `fixed_amount.currency_options` | map (key → value) |  |  |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  | Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. |

Returns: `shipping_rate`

# Objects returned

## The `shipping_rate` object

Shipping rates describe the price of shipping presented to your customers and
applied to a purchase. For more information, see [Charge for shipping](https://stripe.com/docs/payments/during-payment/charge-shipping).

Expandable fields (pass `expand[]=<field>`): `delivery_estimate`, `fixed_amount`, `tax_code`

| Field | Type | Required | Description |
|---|---|---|---|
| `active` | boolean | yes | Whether the shipping rate can be used for new purchases. Defaults to `true`. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `delivery_estimate` | `shipping_rate_delivery_estimate` |  | The estimated range for how long shipping will take, meant to be displayable to the customer. This will appear on CheckoutSessions. |
| `display_name` | string |  | The name of the shipping rate, meant to be displayable to the customer. This will appear on CheckoutSessions. |
| `fixed_amount` | `shipping_rate_fixed_amount` |  |  |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) | yes | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `object` | enum: `shipping_rate` | yes | String representing the object's type. Objects of the same type share the same value. |
| `tax_behavior` | enum: `exclusive`, `inclusive`, `unspecified` |  | Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. |
| `tax_code` | string or `tax_code` |  | A [tax code](https://stripe.com/docs/tax/tax-categories) ID. The Shipping tax code is `txcd_92010001`. |
| `type` | enum: `fixed_amount` | yes | The type of calculation to use on the shipping rate. Can only be `fixed_amount` for now. |

