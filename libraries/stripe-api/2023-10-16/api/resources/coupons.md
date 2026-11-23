# Stripe API 2023-10-16 — coupons

Operations under `/v1/coupons` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/coupons

operationId: `GetCoupons`

Returns a list of your coupons.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | object or integer |  | A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/coupons

operationId: `PostCoupons`

You can create coupons easily via the [coupon management](https://dashboard.stripe.com/coupons) page of the Stripe dashboard. Coupon creation is also accessible via the API if you need to create coupons on the fly.

A coupon has either a `percent_off` or an `amount_off` and `currency`. If you set an `amount_off`, that amount will be subtracted from any invoice’s subtotal. For example, an invoice with a subtotal of <currency>100</currency> will have a final total of <currency>0</currency> if a coupon with an `amount_off` of <amount>200</amount> is applied to it and an invoice with a subtotal of <currency>300</currency> will have a final total of <currency>100</currency> if a coupon with an `amount_off` of <amount>200</amount> is applied to it.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `amount_off` | integer |  | A positive integer representing the amount to subtract from an invoice total (required if `percent_off` is not passed). |
| `applies_to` | object |  | A hash containing directions for what this Coupon will apply discounts to. |
| `applies_to.products` | array of string |  |  |
| `currency` | string |  | Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) of the `amount_off` parameter (required if `amount_off` is passed). |
| `currency_options` | map (key → value) |  | Coupons defined in each available currency option (only supported if `amount_off` is passed). Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies). |
| `duration` | enum: `forever`, `once`, `repeating` |  | Specifies how long the discount will be in effect if used on a subscription. Defaults to `once`. |
| `duration_in_months` | integer |  | Required only if `duration` is `repeating`, in which case it must be a positive integer that specifies the number of months the discount will be in effect. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `id` | string |  | Unique string of your choice that will be used to identify this coupon when applying it to a customer. If you don't want to specify a particular code, you can leave the ID blank and we'll generate a random code for you. |
| `max_redemptions` | integer |  | A positive integer specifying the number of times the coupon can be redeemed before it's no longer valid. For example, you might have a 50% off coupon that the first 20 readers of your blog can use. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `name` | string |  | Name of the coupon displayed to customers on, for instance invoices, or receipts. By default the `id` is shown if `name` is not set. |
| `percent_off` | number |  | A positive float larger than 0, and smaller or equal to 100, that represents the discount the coupon will apply (required if `amount_off` is not passed). |
| `redeem_by` | timestamp (Unix seconds) |  | Unix timestamp specifying the last time at which the coupon can be redeemed. After the redeem_by date, the coupon can no longer be applied to new customers. |

Returns: `coupon`

## GET /v1/coupons/{coupon}

operationId: `GetCouponsCoupon`

Retrieves the coupon with the given ID.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `coupon (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `coupon`

## POST /v1/coupons/{coupon}

operationId: `PostCouponsCoupon`

Updates the metadata of a coupon. Other coupon details (currency, duration, amount_off) are, by design, not editable.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `coupon (path)` | string | yes |  |
| `currency_options` | map (key → value) |  | Coupons defined in each available currency option (only supported if the coupon is amount-based). Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies). |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `name` | string |  | Name of the coupon displayed to customers on, for instance invoices, or receipts. By default the `id` is shown if `name` is not set. |

Returns: `coupon`

## DELETE /v1/coupons/{coupon}

operationId: `DeleteCouponsCoupon`

You can delete coupons via the [coupon management](https://dashboard.stripe.com/coupons) page of the Stripe dashboard. However, deleting a coupon does not affect any customers who have already applied the coupon; it means that new customers can’t redeem the coupon. You can also delete coupons via the API.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `coupon (path)` | string | yes |  |

Returns: `deleted_coupon`

# Objects returned

## The `coupon` object

A coupon contains information about a percent-off or amount-off discount you
might want to apply to a customer. Coupons may be applied to [subscriptions](https://stripe.com/docs/api#subscriptions), [invoices](https://stripe.com/docs/api#invoices),
[checkout sessions](https://stripe.com/docs/api/checkout/sessions), [quotes](https://stripe.com/docs/api#quotes), and more. Coupons do not work with conventional one-off [charges](https://stripe.com/docs/api#create_charge) or [payment intents](https://stripe.com/docs/api/payment_intents).

Expandable fields (pass `expand[]=<field>`): `applies_to`, `currency_options`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount_off` | integer |  | Amount (in the `currency` specified) that will be taken off the subtotal of any invoices for this customer. |
| `applies_to` | `coupon_applies_to` |  |  |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string |  | If `amount_off` has been set, the three-letter [ISO code for the currency](https://stripe.com/docs/currencies) of the amount to take off. |
| `currency_options` | map (key → value) |  | Coupons defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies). |
| `duration` | enum: `forever`, `once`, `repeating` | yes | One of `forever`, `once`, and `repeating`. Describes how long a customer who applies this coupon will get the discount. |
| `duration_in_months` | integer |  | If `duration` is `repeating`, the number of months the coupon applies. Null if coupon `duration` is `forever` or `once`. |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `max_redemptions` | integer |  | Maximum number of times this coupon can be redeemed, in total, across all customers, before it is no longer valid. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `name` | string |  | Name of the coupon displayed to customers on for instance invoices or receipts. |
| `object` | enum: `coupon` | yes | String representing the object's type. Objects of the same type share the same value. |
| `percent_off` | number |  | Percent that will be taken off the subtotal of any invoices for this customer for the duration of the coupon. For example, a coupon with percent_off of 50 will make a $ (or local equivalent)100 invoice $ (or local equivalent)50 instead. |
| `redeem_by` | timestamp (Unix seconds) |  | Date after which the coupon can no longer be redeemed. |
| `times_redeemed` | integer | yes | Number of times this coupon has been applied to a customer. |
| `valid` | boolean | yes | Taking account of the above properties, whether this coupon can still be applied to a customer. |

## The `deleted_coupon` object

| Field | Type | Required | Description |
|---|---|---|---|
| `deleted` | enum: `True` | yes | Always true for a deleted object |
| `id` | string | yes | Unique identifier for the object. |
| `object` | enum: `coupon` | yes | String representing the object's type. Objects of the same type share the same value. |

