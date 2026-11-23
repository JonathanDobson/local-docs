# Stripe API 2023-10-16 — refunds

Operations under `/v1/refunds` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/refunds

operationId: `GetRefunds`

Returns a list of all refunds you created. We return the refunds in sorted order, with the most recent refunds appearing first The 10 most recent refunds are always available by default on the Charge object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `charge` | string |  | Only return refunds for the charge specified by this charge ID. |
| `created` | object or integer |  | Only return refunds that were created during the given date interval. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `payment_intent` | string |  | Only return refunds for the PaymentIntent specified by this ID. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/refunds

operationId: `PostRefunds`

When you create a new refund, you must specify a Charge or a PaymentIntent object on which to create it.

Creating a new refund will refund a charge that has previously been created but not yet refunded.
Funds will be refunded to the credit or debit card that was originally charged.

You can optionally refund only part of a charge.
You can do so multiple times, until the entire charge has been refunded.

Once entirely refunded, a charge can’t be refunded again.
This method will raise an error when called on an already-refunded charge,
or when trying to refund more money than is left on a charge.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer |  |  |
| `charge` | string |  | The identifier of the charge to refund. |
| `currency` | string |  | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `customer` | string |  | Customer whose customer balance to refund from. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `instructions_email` | string |  | For payment methods without native refund support (e.g., Konbini, PromptPay), use this email from the customer to receive refund instructions. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `origin` | enum: `customer_balance` |  | Origin of the refund |
| `payment_intent` | string |  | The identifier of the PaymentIntent to refund. |
| `reason` | enum: `duplicate`, `fraudulent`, `requested_by_customer` |  | String indicating the reason for the refund. If set, possible values are `duplicate`, `fraudulent`, and `requested_by_customer`. If you believe the charge to be fraudulent, specifying `fraudulent` as the reason will add the associated card and email to your [block lists](https://stripe.com/docs/radar/lists), and will also help us improve our fraud detection algorithms. |
| `refund_application_fee` | boolean |  | Boolean indicating whether the application fee should be refunded when refunding this charge. If a full charge refund is given, the full application fee will be refunded. Otherwise, the application fee will be refunded in an amount proportional to the amount of the charge refunded. An application fee can be refunded only by the application that created the charge. |
| `reverse_transfer` | boolean |  | Boolean indicating whether the transfer should be reversed when refunding this charge. The transfer will be reversed proportionally to the amount being refunded (either the entire or partial amount).<br>A transfer can be reversed only by the application that created the charge. |

Returns: `refund`

## GET /v1/refunds/{refund}

operationId: `GetRefundsRefund`

Retrieves the details of an existing refund.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `refund (path)` | string | yes |  |

Returns: `refund`

## POST /v1/refunds/{refund}

operationId: `PostRefundsRefund`

Updates the refund that you specify by setting the values of the passed parameters. Any parameters that you don’t provide remain unchanged.

This request only accepts `metadata` as an argument.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `refund (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |

Returns: `refund`

## POST /v1/refunds/{refund}/cancel

operationId: `PostRefundsRefundCancel`

Cancels a refund with a status of `requires_action`.

You can’t cancel refunds in other states. Only refunds for payment methods that require customer action can enter the `requires_action` state.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `refund (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `refund`

# Objects returned

## The `refund` object

Refund objects allow you to refund a previously created charge that isn't
refunded yet. Funds are refunded to the credit or debit card that's
initially charged.

Related guide: [Refunds](https://stripe.com/docs/refunds)

Expandable fields (pass `expand[]=<field>`): `balance_transaction`, `charge`, `destination_details`, `failure_balance_transaction`, `next_action`, `payment_intent`, `source_transfer_reversal`, `transfer_reversal`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | Amount, in cents (or local equivalent). |
| `balance_transaction` | string or `balance_transaction` |  | Balance transaction that describes the impact on your account balance. |
| `charge` | string or `charge` |  | ID of the charge that's refunded. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `description` | string |  | An arbitrary string attached to the object. You can use this for displaying to users (available on non-card refunds only). |
| `destination_details` | `refund_destination_details` |  |  |
| `failure_balance_transaction` | string or `balance_transaction` |  | After the refund fails, this balance transaction describes the adjustment made on your account balance that reverses the initial balance transaction. |
| `failure_reason` | string |  | Provides the reason for the refund failure. Possible values are: `lost_or_stolen_card`, `expired_or_canceled_card`, `charge_for_pending_refund_disputed`, `insufficient_funds`, `declined`, `merchant_request`, or `unknown`. |
| `id` | string | yes | Unique identifier for the object. |
| `instructions_email` | string |  | For payment methods without native refund support (for example, Konbini, PromptPay), provide an email address for the customer to receive refund instructions. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `next_action` | `refund_next_action` |  |  |
| `object` | enum: `refund` | yes | String representing the object's type. Objects of the same type share the same value. |
| `payment_intent` | string or `payment_intent` |  | ID of the PaymentIntent that's refunded. |
| `reason` | enum: `duplicate`, `expired_uncaptured_charge`, `fraudulent`, `requested_by_customer` |  | Reason for the refund, which is either user-provided (`duplicate`, `fraudulent`, or `requested_by_customer`) or generated by Stripe internally (`expired_uncaptured_charge`). |
| `receipt_number` | string |  | This is the transaction number that appears on email receipts sent for this refund. |
| `source_transfer_reversal` | string or `transfer_reversal` |  | The transfer reversal that's associated with the refund. Only present if the charge came from another Stripe account. |
| `status` | string |  | Status of the refund. This can be `pending`, `requires_action`, `succeeded`, `failed`, or `canceled`. Learn more about [failed refunds](https://stripe.com/docs/refunds#failed-refunds). |
| `transfer_reversal` | string or `transfer_reversal` |  | This refers to the transfer reversal object if the accompanying transfer reverses. This is only applicable if the charge was created using the destination parameter. |

