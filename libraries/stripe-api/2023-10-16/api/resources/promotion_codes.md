# Stripe API 2023-10-16 — promotion codes

Operations under `/v1/promotion_codes` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/promotion_codes

operationId: `GetPromotionCodes`

Returns a list of your promotion codes.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `active` | boolean |  | Filter promotion codes by whether they are active. |
| `code` | string |  | Only return promotion codes that have this case-insensitive code. |
| `coupon` | string |  | Only return promotion codes for this coupon. |
| `created` | object or integer |  | A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `customer` | string |  | Only return promotion codes that are restricted to this customer. |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/promotion_codes

operationId: `PostPromotionCodes`

A promotion code points to a coupon. You can optionally restrict the code to a specific customer, redemption limit, and expiration date.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `active` | boolean |  | Whether the promotion code is currently active. |
| `code` | string |  | The customer-facing code. Regardless of case, this code must be unique across all active promotion codes for a specific customer. If left blank, we will generate one automatically. |
| `coupon` | string | yes | The coupon for this promotion code. |
| `customer` | string |  | The customer that this promotion code can be used by. If not set, the promotion code can be used by all customers. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `expires_at` | timestamp (Unix seconds) |  | The timestamp at which this promotion code will expire. If the coupon has specified a `redeems_by`, then this value cannot be after the coupon's `redeems_by`. |
| `max_redemptions` | integer |  | A positive integer specifying the number of times the promotion code can be redeemed. If the coupon has specified a `max_redemptions`, then this value cannot be greater than the coupon's `max_redemptions`. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `restrictions` | object |  | Settings that restrict the redemption of the promotion code. |
| `restrictions.currency_options` | map (key → value) |  |  |
| `restrictions.first_time_transaction` | boolean |  |  |
| `restrictions.minimum_amount` | integer |  |  |
| `restrictions.minimum_amount_currency` | string |  |  |

Returns: `promotion_code`

## GET /v1/promotion_codes/{promotion_code}

operationId: `GetPromotionCodesPromotionCode`

Retrieves the promotion code with the given ID. In order to retrieve a promotion code by the customer-facing `code` use [list](https://stripe.com/docs/api/promotion_codes/list) with the desired `code`.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `promotion_code (path)` | string | yes |  |

Returns: `promotion_code`

## POST /v1/promotion_codes/{promotion_code}

operationId: `PostPromotionCodesPromotionCode`

Updates the specified promotion code by setting the values of the parameters passed. Most fields are, by design, not editable.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `promotion_code (path)` | string | yes |  |
| `active` | boolean |  | Whether the promotion code is currently active. A promotion code can only be reactivated when the coupon is still valid and the promotion code is otherwise redeemable. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `restrictions` | object |  | Settings that restrict the redemption of the promotion code. |
| `restrictions.currency_options` | map (key → value) |  |  |

Returns: `promotion_code`

# Objects returned

## The `promotion_code` object

A Promotion Code represents a customer-redeemable code for a [coupon](https://stripe.com/docs/api#coupons). It can be used to
create multiple codes for a single coupon.

Expandable fields (pass `expand[]=<field>`): `coupon`, `customer`, `restrictions`

| Field | Type | Required | Description |
|---|---|---|---|
| `active` | boolean | yes | Whether the promotion code is currently active. A promotion code is only active if the coupon is also valid. |
| `code` | string | yes | The customer-facing code. Regardless of case, this code must be unique across all active promotion codes for each customer. |
| `coupon` | `coupon` | yes |  |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `customer` | string or `customer` or `deleted_customer` |  | The customer that this promotion code can be used by. |
| `expires_at` | timestamp (Unix seconds) |  | Date at which the promotion code can no longer be redeemed. |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `max_redemptions` | integer |  | Maximum number of times this promotion code can be redeemed. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `object` | enum: `promotion_code` | yes | String representing the object's type. Objects of the same type share the same value. |
| `restrictions` | `promotion_codes_resource_restrictions` | yes |  |
| `times_redeemed` | integer | yes | Number of times this promotion code has been used. |

