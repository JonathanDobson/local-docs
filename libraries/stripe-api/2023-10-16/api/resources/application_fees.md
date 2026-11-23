# Stripe API 2023-10-16 — application fees

Operations under `/v1/application_fees` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/application_fees

operationId: `GetApplicationFees`

Returns a list of application fees you’ve previously collected. The application fees are returned in sorted order, with the most recent fees appearing first.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `charge` | string |  | Only return application fees for the charge specified by this charge ID. |
| `created` | object or integer |  | Only return applications fees that were created during the given date interval. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## GET /v1/application_fees/{fee}/refunds/{id}

operationId: `GetApplicationFeesFeeRefundsId`

By default, you can see the 10 most recent refunds stored directly on the application fee object, but you can also retrieve details about a specific refund stored on the application fee.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `fee (path)` | string | yes |  |
| `id (path)` | string | yes |  |

Returns: `fee_refund`

## POST /v1/application_fees/{fee}/refunds/{id}

operationId: `PostApplicationFeesFeeRefundsId`

Updates the specified application fee refund by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

This request only accepts metadata as an argument.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `fee (path)` | string | yes |  |
| `id (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |

Returns: `fee_refund`

## GET /v1/application_fees/{id}

operationId: `GetApplicationFeesId`

Retrieves the details of an application fee that your account has collected. The same information is returned when refunding the application fee.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `id (path)` | string | yes |  |

Returns: `application_fee`

## POST /v1/application_fees/{id}/refund

operationId: `PostApplicationFeesIdRefund`

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string | yes |  |
| `amount` | integer |  |  |
| `directive` | string |  |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `application_fee`

## GET /v1/application_fees/{id}/refunds

operationId: `GetApplicationFeesIdRefunds`

You can see a list of the refunds belonging to a specific application fee. Note that the 10 most recent refunds are always available by default on the application fee object. If you need more than those 10, you can use this API method and the `limit` and `starting_after` parameters to page through additional refunds.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `id (path)` | string | yes |  |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/application_fees/{id}/refunds

operationId: `PostApplicationFeesIdRefunds`

Refunds an application fee that has previously been collected but not yet refunded.
Funds will be refunded to the Stripe account from which the fee was originally collected.

You can optionally refund only part of an application fee.
You can do so multiple times, until the entire fee has been refunded.

Once entirely refunded, an application fee can’t be refunded again.
This method will raise an error when called on an already-refunded application fee,
or when trying to refund more money than is left on an application fee.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string | yes |  |
| `amount` | integer |  | A positive integer, in _cents (or local equivalent)_, representing how much of this fee to refund. Can refund only up to the remaining unrefunded amount of the fee. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |

Returns: `fee_refund`

# Objects returned

## The `fee_refund` object

`Application Fee Refund` objects allow you to refund an application fee that
has previously been created but not yet refunded. Funds will be refunded to
the Stripe account from which the fee was originally collected.

Related guide: [Refunding application fees](https://stripe.com/docs/connect/destination-charges#refunding-app-fee)

Expandable fields (pass `expand[]=<field>`): `balance_transaction`, `fee`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | Amount, in cents (or local equivalent). |
| `balance_transaction` | string or `balance_transaction` |  | Balance transaction that describes the impact on your account balance. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `fee` | string or `application_fee` | yes | ID of the application fee that was refunded. |
| `id` | string | yes | Unique identifier for the object. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `object` | enum: `fee_refund` | yes | String representing the object's type. Objects of the same type share the same value. |

## The `application_fee` object

Expandable fields (pass `expand[]=<field>`): `account`, `application`, `balance_transaction`, `charge`, `originating_transaction`, `refunds`

| Field | Type | Required | Description |
|---|---|---|---|
| `account` | string or `account` | yes | ID of the Stripe account this fee was taken from. |
| `amount` | integer | yes | Amount earned, in cents (or local equivalent). |
| `amount_refunded` | integer | yes | Amount in cents (or local equivalent) refunded (can be less than the amount attribute on the fee if a partial refund was issued) |
| `application` | string or `application` | yes | ID of the Connect application that earned the fee. |
| `balance_transaction` | string or `balance_transaction` |  | Balance transaction that describes the impact of this collected application fee on your account balance (not including refunds). |
| `charge` | string or `charge` | yes | ID of the charge that the application fee was taken from. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `object` | enum: `application_fee` | yes | String representing the object's type. Objects of the same type share the same value. |
| `originating_transaction` | string or `charge` |  | ID of the corresponding charge on the platform account, if this fee was the result of a charge using the `destination` parameter. |
| `refunded` | boolean | yes | Whether the fee has been fully refunded. If the fee is only partially refunded, this attribute will still be false. |
| `refunds` | object | yes | A list of refunds that have been applied to the fee. |

