# Stripe API 2023-10-16 — topups

Operations under `/v1/topups` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/topups

operationId: `GetTopups`

Returns a list of top-ups.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | object or integer |  | A positive integer representing how much to transfer. |
| `amount.gt` | integer |  |  |
| `amount.gte` | integer |  |  |
| `amount.lt` | integer |  |  |
| `amount.lte` | integer |  |  |
| `created` | object or integer |  | A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `status` | enum: `canceled`, `failed`, `pending`, `succeeded` |  | Only return top-ups that have the given status. One of `canceled`, `failed`, `pending` or `succeeded`. |

Returns: object

## POST /v1/topups

operationId: `PostTopups`

Top up the balance of an account

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | A positive integer representing how much to transfer. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `source` | string |  | The ID of a source to transfer funds from. For most users, this should be left unspecified which will use the bank account that was set up in the dashboard for the specified currency. In test mode, this can be a test bank token (see [Testing Top-ups](https://stripe.com/docs/connect/testing#testing-top-ups)). |
| `statement_descriptor` | string |  | Extra information about a top-up for the source's bank statement. Limited to 15 ASCII characters. |
| `transfer_group` | string |  | A string that identifies this top-up as part of a group. |

Returns: `topup`

## GET /v1/topups/{topup}

operationId: `GetTopupsTopup`

Retrieves the details of a top-up that has previously been created. Supply the unique top-up ID that was returned from your previous request, and Stripe will return the corresponding top-up information.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `topup (path)` | string | yes |  |

Returns: `topup`

## POST /v1/topups/{topup}

operationId: `PostTopupsTopup`

Updates the metadata of a top-up. Other top-up details are not editable by design.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `topup (path)` | string | yes |  |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |

Returns: `topup`

## POST /v1/topups/{topup}/cancel

operationId: `PostTopupsTopupCancel`

Cancels a top-up. Only pending top-ups can be canceled.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `topup (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `topup`

# Objects returned

## The `topup` object

To top up your Stripe balance, you create a top-up object. You can retrieve
individual top-ups, as well as list all top-ups. Top-ups are identified by a
unique, random ID.

Related guide: [Topping up your platform account](https://stripe.com/docs/connect/top-ups)

Expandable fields (pass `expand[]=<field>`): `balance_transaction`, `source`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | Amount transferred. |
| `balance_transaction` | string or `balance_transaction` |  | ID of the balance transaction that describes the impact of this top-up on your account balance. May not be specified depending on status of top-up. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. |
| `expected_availability_date` | integer |  | Date the funds are expected to arrive in your Stripe account for payouts. This factors in delays like weekends or bank holidays. May not be specified depending on status of top-up. |
| `failure_code` | string |  | Error code explaining reason for top-up failure if available (see [the errors section](https://stripe.com/docs/api#errors) for a list of codes). |
| `failure_message` | string |  | Message to user further explaining reason for top-up failure if available. |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) | yes | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `object` | enum: `topup` | yes | String representing the object's type. Objects of the same type share the same value. |
| `source` | `source` |  | The source field is deprecated. It might not always be present in the API response. |
| `statement_descriptor` | string |  | Extra information about a top-up. This will appear on your source's bank statement. It must contain at least one letter. |
| `status` | enum: `canceled`, `failed`, `pending`, `reversed`, `succeeded` | yes | The status of the top-up is either `canceled`, `failed`, `pending`, `reversed`, or `succeeded`. |
| `transfer_group` | string |  | A string that identifies this top-up as part of a group. |

