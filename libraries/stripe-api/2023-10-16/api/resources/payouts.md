# Stripe API 2023-10-16 — payouts

Operations under `/v1/payouts` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/payouts

operationId: `GetPayouts`

Returns a list of existing payouts sent to third-party bank accounts or payouts that Stripe sent to you. The payouts return in sorted order, with the most recently created payouts appearing first.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `arrival_date` | object or integer |  | Only return payouts that are expected to arrive during the given date interval. |
| `arrival_date.gt` | integer |  |  |
| `arrival_date.gte` | integer |  |  |
| `arrival_date.lt` | integer |  |  |
| `arrival_date.lte` | integer |  |  |
| `created` | object or integer |  | Only return payouts that were created during the given date interval. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `destination` | string |  | The ID of an external account - only return payouts sent to this external account. |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `status` | string |  | Only return payouts that have the given status: `pending`, `paid`, `failed`, or `canceled`. |

Returns: object

## POST /v1/payouts

operationId: `PostPayouts`

To send funds to your own bank account, create a new payout object. Your [Stripe balance](#balance) must cover the payout amount. If it doesn’t, you receive an “Insufficient Funds” error.

If your API key is in test mode, money won’t actually be sent, though every other action occurs as if you’re in live mode.

If you create a manual payout on a Stripe account that uses multiple payment source types, you need to specify the source type balance that the payout draws from. The [balance object](#balance_object) details available and pending amounts by source type.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | A positive integer in cents representing how much to payout. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. |
| `destination` | string |  | The ID of a bank account or a card to send the payout to. If you don't provide a destination, we use the default external account for the specified currency. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `method` | enum: `instant`, `standard` |  | The method used to send this payout, which is `standard` or `instant`. We support `instant` for payouts to debit cards and bank accounts in certain countries. Learn more about [bank support for Instant Payouts](https://stripe.com/docs/payouts/instant-payouts-banks). |
| `source_type` | enum: `bank_account`, `card`, `fpx` |  | The balance type of your Stripe balance to draw this payout from. Balances for different payment sources are kept separately. You can find the amounts with the Balances API. One of `bank_account`, `card`, or `fpx`. |
| `statement_descriptor` | string (open enum) |  | A string that displays on the recipient's bank or card statement (up to 22 characters). A `statement_descriptor` that's longer than 22 characters return an error. Most banks truncate this information and display it inconsistently. Some banks might not display it at all. |

Returns: `payout`

## GET /v1/payouts/{payout}

operationId: `GetPayoutsPayout`

Retrieves the details of an existing payout. Supply the unique payout ID from either a payout creation request or the payout list. Stripe returns the corresponding payout information.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `payout (path)` | string | yes |  |

Returns: `payout`

## POST /v1/payouts/{payout}

operationId: `PostPayoutsPayout`

Updates the specified payout by setting the values of the parameters you pass. We don’t change parameters that you don’t provide. This request only accepts the metadata as arguments.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `payout (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |

Returns: `payout`

## POST /v1/payouts/{payout}/cancel

operationId: `PostPayoutsPayoutCancel`

You can cancel a previously created payout if its status is `pending`. Stripe refunds the funds to your available balance. You can’t cancel automatic Stripe payouts.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `payout (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `payout`

## POST /v1/payouts/{payout}/reverse

operationId: `PostPayoutsPayoutReverse`

Reverses a payout by debiting the destination bank account. At this time, you can only reverse payouts for connected accounts to US bank accounts. If the payout is manual and in the `pending` status, use `/v1/payouts/:id/cancel` instead.

By requesting a reversal through `/v1/payouts/:id/reverse`, you confirm that the authorized signatory of the selected bank account authorizes the debit on the bank account and that no other authorization is required.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `payout (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |

Returns: `payout`

# Objects returned

## The `payout` object

A `Payout` object is created when you receive funds from Stripe, or when you
initiate a payout to either a bank account or debit card of a [connected
Stripe account](https://stripe.com/docs/connect/bank-debit-card-payouts). You can retrieve individual payouts,
and list all payouts. Payouts are made on [varying
schedules](https://stripe.com/docs/connect/manage-payout-schedule), depending on your country and
industry.

Related guide: [Receiving payouts](https://stripe.com/docs/payouts)

Expandable fields (pass `expand[]=<field>`): `balance_transaction`, `destination`, `failure_balance_transaction`, `original_payout`, `reversed_by`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | The amount (in cents (or local equivalent)) that transfers to your bank account or debit card. |
| `arrival_date` | timestamp (Unix seconds) | yes | Date that you can expect the payout to arrive in the bank. This factors in delays to account for weekends or bank holidays. |
| `automatic` | boolean | yes | Returns `true` if the payout is created by an [automated payout schedule](https://stripe.com/docs/payouts#payout-schedule) and `false` if it's [requested manually](https://stripe.com/docs/payouts#manual-payouts). |
| `balance_transaction` | string or `balance_transaction` |  | ID of the balance transaction that describes the impact of this payout on your account balance. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. |
| `destination` | string or `bank_account` or `card` or `deleted_bank_account` or `deleted_card` |  | ID of the bank account or card the payout is sent to. |
| `failure_balance_transaction` | string or `balance_transaction` |  | If the payout fails or cancels, this is the ID of the balance transaction that reverses the initial balance transaction and returns the funds from the failed payout back in your balance. |
| `failure_code` | string |  | Error code that provides a reason for a payout failure, if available. View our [list of failure codes](https://stripe.com/docs/api#payout_failures). |
| `failure_message` | string |  | Message that provides the reason for a payout failure, if available. |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `method` | string | yes | The method used to send this payout, which can be `standard` or `instant`. `instant` is supported for payouts to debit cards and bank accounts in certain countries. Learn more about [bank support for Instant Payouts](https://stripe.com/docs/payouts/instant-payouts-banks). |
| `object` | enum: `payout` | yes | String representing the object's type. Objects of the same type share the same value. |
| `original_payout` | string or `payout` |  | If the payout reverses another, this is the ID of the original payout. |
| `reconciliation_status` | enum: `completed`, `in_progress`, `not_applicable` | yes | If `completed`, you can use the [Balance Transactions API](https://stripe.com/docs/api/balance_transactions/list#balance_transaction_list-payout) to list all balance transactions that are paid out in this payout. |
| `reversed_by` | string or `payout` |  | If the payout reverses, this is the ID of the payout that reverses this payout. |
| `source_type` | string | yes | The source balance this payout came from, which can be one of the following: `card`, `fpx`, or `bank_account`. |
| `statement_descriptor` | string |  | Extra information about a payout that displays on the user's bank statement. |
| `status` | string | yes | Current status of the payout: `paid`, `pending`, `in_transit`, `canceled` or `failed`. A payout is `pending` until it's submitted to the bank, when it becomes `in_transit`. The status changes to `paid` if the transaction succeeds, or to `failed` or `canceled` (within 5 business days). Some payouts that fail might initially show as `paid`, then change to `failed`. |
| `type` | enum: `bank_account`, `card` | yes | Can be `bank_account` or `card`. |

