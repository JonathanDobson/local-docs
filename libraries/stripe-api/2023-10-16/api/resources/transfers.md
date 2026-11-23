# Stripe API 2023-10-16 — transfers

Operations under `/v1/transfers` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/transfers

operationId: `GetTransfers`

Returns a list of existing transfers sent to connected accounts. The transfers are returned in sorted order, with the most recently created transfers appearing first.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | object or integer |  | Only return transfers that were created during the given date interval. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `destination` | string |  | Only return transfers for the destination specified by this account ID. |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `transfer_group` | string |  | Only return transfers with the specified transfer group. |

Returns: object

## POST /v1/transfers

operationId: `PostTransfers`

To send funds from your Stripe account to a connected account, you create a new transfer object. Your [Stripe balance](#balance) must be able to cover the transfer amount, or you’ll receive an “Insufficient Funds” error.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer |  | A positive integer in cents (or local equivalent) representing how much to transfer. |
| `currency` | string | yes | 3-letter [ISO code for currency](https://stripe.com/docs/payouts). |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. |
| `destination` | string | yes | The ID of a connected Stripe account. [See the Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers) for details. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `source_transaction` | string |  | You can use this parameter to transfer funds from a charge before they are added to your available balance. A pending balance will transfer immediately but the funds will not become available until the original charge becomes available. [See the Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-availability) for details. |
| `source_type` | enum: `bank_account`, `card`, `fpx` |  | The source balance to use for this transfer. One of `bank_account`, `card`, or `fpx`. For most users, this will default to `card`. |
| `transfer_group` | string |  | A string that identifies this transaction as part of a group. See the [Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-options) for details. |

Returns: `transfer`

## GET /v1/transfers/{id}/reversals

operationId: `GetTransfersIdReversals`

You can see a list of the reversals belonging to a specific transfer. Note that the 10 most recent reversals are always available by default on the transfer object. If you need more than those 10, you can use this API method and the `limit` and `starting_after` parameters to page through additional reversals.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `id (path)` | string | yes |  |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/transfers/{id}/reversals

operationId: `PostTransfersIdReversals`

When you create a new reversal, you must specify a transfer to create it on.

When reversing transfers, you can optionally reverse part of the transfer. You can do so as many times as you wish until the entire transfer has been reversed.

Once entirely reversed, a transfer can’t be reversed again. This method will return an error when called on an already-reversed transfer, or when trying to reverse more money than is left on a transfer.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string | yes |  |
| `amount` | integer |  | A positive integer in cents (or local equivalent) representing how much of this transfer to reverse. Can only reverse up to the unreversed amount remaining of the transfer. Partial transfer reversals are only allowed for transfers to Stripe Accounts. Defaults to the entire transfer amount. |
| `description` | string |  | An arbitrary string which you can attach to a reversal object. It is displayed alongside the reversal in the Dashboard. This will be unset if you POST an empty value. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `refund_application_fee` | boolean |  | Boolean indicating whether the application fee should be refunded when reversing this transfer. If a full transfer reversal is given, the full application fee will be refunded. Otherwise, the application fee will be refunded with an amount proportional to the amount of the transfer reversed. |

Returns: `transfer_reversal`

## GET /v1/transfers/{transfer}

operationId: `GetTransfersTransfer`

Retrieves the details of an existing transfer. Supply the unique transfer ID from either a transfer creation request or the transfer list, and Stripe will return the corresponding transfer information.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `transfer (path)` | string | yes |  |

Returns: `transfer`

## POST /v1/transfers/{transfer}

operationId: `PostTransfersTransfer`

Updates the specified transfer by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

This request accepts only metadata as an argument.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `transfer (path)` | string | yes |  |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |

Returns: `transfer`

## GET /v1/transfers/{transfer}/reversals/{id}

operationId: `GetTransfersTransferReversalsId`

By default, you can see the 10 most recent reversals stored directly on the transfer object, but you can also retrieve details about a specific reversal stored on the transfer.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `id (path)` | string | yes |  |
| `transfer (path)` | string | yes |  |

Returns: `transfer_reversal`

## POST /v1/transfers/{transfer}/reversals/{id}

operationId: `PostTransfersTransferReversalsId`

Updates the specified reversal by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

This request only accepts metadata and description as arguments.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string | yes |  |
| `transfer (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |

Returns: `transfer_reversal`

# Objects returned

## The `transfer` object

A `Transfer` object is created when you move funds between Stripe accounts as
part of Connect.

Before April 6, 2017, transfers also represented movement of funds from a
Stripe account to a card or bank account. This behavior has since been split
out into a [Payout](https://stripe.com/docs/api#payout_object) object, with corresponding payout endpoints. For more
information, read about the
[transfer/payout split](https://stripe.com/docs/transfer-payout-split).

Related guide: [Creating separate charges and transfers](https://stripe.com/docs/connect/separate-charges-and-transfers)

Expandable fields (pass `expand[]=<field>`): `balance_transaction`, `destination`, `destination_payment`, `reversals`, `source_transaction`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | Amount in cents (or local equivalent) to be transferred. |
| `amount_reversed` | integer | yes | Amount in cents (or local equivalent) reversed (can be less than the amount attribute on the transfer if a partial reversal was issued). |
| `balance_transaction` | string or `balance_transaction` |  | Balance transaction that describes the impact of this transfer on your account balance. |
| `created` | timestamp (Unix seconds) | yes | Time that this record of the transfer was first created. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. |
| `destination` | string or `account` |  | ID of the Stripe account the transfer was sent to. |
| `destination_payment` | string or `charge` |  | If the destination is a Stripe account, this will be the ID of the payment that the destination account received for the transfer. |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) | yes | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `object` | enum: `transfer` | yes | String representing the object's type. Objects of the same type share the same value. |
| `reversals` | object | yes | A list of reversals that have been applied to the transfer. |
| `reversed` | boolean | yes | Whether the transfer has been fully reversed. If the transfer is only partially reversed, this attribute will still be false. |
| `source_transaction` | string or `charge` |  | ID of the charge or payment that was used to fund the transfer. If null, the transfer was funded from the available balance. |
| `source_type` | string |  | The source balance this transfer came from. One of `card`, `fpx`, or `bank_account`. |
| `transfer_group` | string |  | A string that identifies this transaction as part of a group. See the [Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-options) for details. |

## The `transfer_reversal` object

[Stripe Connect](https://stripe.com/docs/connect) platforms can reverse transfers made to a
connected account, either entirely or partially, and can also specify whether
to refund any related application fees. Transfer reversals add to the
platform's balance and subtract from the destination account's balance.

Reversing a transfer that was made for a [destination
charge](https://stripe.com/docs/connect/destination-charges) is allowed only up to the amount of
the charge. It is possible to reverse a
[transfer_group](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-options)
transfer only if the destination account has enough balance to cover the
reversal.

Related guide: [Reversing transfers](https://stripe.com/docs/connect/separate-charges-and-transfers#reversing-transfers)

Expandable fields (pass `expand[]=<field>`): `balance_transaction`, `destination_payment_refund`, `source_refund`, `transfer`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | Amount, in cents (or local equivalent). |
| `balance_transaction` | string or `balance_transaction` |  | Balance transaction that describes the impact on your account balance. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `destination_payment_refund` | string or `refund` |  | Linked payment refund for the transfer reversal. |
| `id` | string | yes | Unique identifier for the object. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `object` | enum: `transfer_reversal` | yes | String representing the object's type. Objects of the same type share the same value. |
| `source_refund` | string or `refund` |  | ID of the refund responsible for the transfer reversal. |
| `transfer` | string or `transfer` | yes | ID of the transfer that was reversed. |

