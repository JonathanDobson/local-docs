# Stripe API 2023-10-16 — disputes

Operations under `/v1/disputes` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/disputes

operationId: `GetDisputes`

Returns a list of your disputes.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `charge` | string |  | Only return disputes associated to the charge specified by this charge ID. |
| `created` | object or integer |  |  |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `payment_intent` | string |  | Only return disputes associated to the PaymentIntent specified by this PaymentIntent ID. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## GET /v1/disputes/{dispute}

operationId: `GetDisputesDispute`

Retrieves the dispute with the given ID.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `dispute (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `dispute`

## POST /v1/disputes/{dispute}

operationId: `PostDisputesDispute`

When you get a dispute, contacting your customer is always the best first step. If that doesn’t work, you can submit evidence to help us resolve the dispute in your favor. You can do this in your [dashboard](https://dashboard.stripe.com/disputes), but if you prefer, you can use the API to submit evidence programmatically.

Depending on your dispute type, different evidence fields will give you a better chance of winning your dispute. To figure out which evidence fields to provide, see our [guide to dispute types](https://stripe.com/docs/disputes/categories).

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `dispute (path)` | string | yes |  |
| `evidence` | object |  | Evidence to upload, to respond to a dispute. Updating any field in the hash will submit all fields in the hash for review. The combined character count of all fields is limited to 150,000. |
| `evidence.access_activity_log` | string |  |  |
| `evidence.billing_address` | string |  |  |
| `evidence.cancellation_policy` | string |  |  |
| `evidence.cancellation_policy_disclosure` | string |  |  |
| `evidence.cancellation_rebuttal` | string |  |  |
| `evidence.customer_communication` | string |  |  |
| `evidence.customer_email_address` | string |  |  |
| `evidence.customer_name` | string |  |  |
| `evidence.customer_purchase_ip` | string |  |  |
| `evidence.customer_signature` | string |  |  |
| `evidence.duplicate_charge_documentation` | string |  |  |
| `evidence.duplicate_charge_explanation` | string |  |  |
| `evidence.duplicate_charge_id` | string |  |  |
| `evidence.product_description` | string |  |  |
| `evidence.receipt` | string |  |  |
| `evidence.refund_policy` | string |  |  |
| `evidence.refund_policy_disclosure` | string |  |  |
| `evidence.refund_refusal_explanation` | string |  |  |
| `evidence.service_date` | string |  |  |
| `evidence.service_documentation` | string |  |  |
| `evidence.shipping_address` | string |  |  |
| `evidence.shipping_carrier` | string |  |  |
| `evidence.shipping_date` | string |  |  |
| `evidence.shipping_documentation` | string |  |  |
| `evidence.shipping_tracking_number` | string |  |  |
| `evidence.uncategorized_file` | string |  |  |
| `evidence.uncategorized_text` | string |  |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `submit` | boolean |  | Whether to immediately submit evidence to the bank. If `false`, evidence is staged on the dispute. Staged evidence is visible in the API and Dashboard, and can be submitted to the bank by making another request with this attribute set to `true` (the default). |

Returns: `dispute`

## POST /v1/disputes/{dispute}/close

operationId: `PostDisputesDisputeClose`

Closing the dispute for a charge indicates that you do not have any evidence to submit and are essentially dismissing the dispute, acknowledging it as lost.

The status of the dispute will change from `needs_response` to `lost`. *Closing a dispute is irreversible*.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `dispute (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `dispute`

# Objects returned

## The `dispute` object

A dispute occurs when a customer questions your charge with their card issuer.
When this happens, you have the opportunity to respond to the dispute with
evidence that shows that the charge is legitimate.

Related guide: [Disputes and fraud](https://stripe.com/docs/disputes)

Expandable fields (pass `expand[]=<field>`): `balance_transactions`, `charge`, `evidence`, `evidence_details`, `payment_intent`, `payment_method_details`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | Disputed amount. Usually the amount of the charge, but it can differ (usually because of currency fluctuation or because only part of the order is disputed). |
| `balance_transactions` | array of `balance_transaction` | yes | List of zero, one, or two balance transactions that show funds withdrawn and reinstated to your Stripe account as a result of this dispute. |
| `charge` | string or `charge` | yes | ID of the charge that's disputed. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `evidence` | `dispute_evidence` | yes |  |
| `evidence_details` | `dispute_evidence_details` | yes |  |
| `id` | string | yes | Unique identifier for the object. |
| `is_charge_refundable` | boolean | yes | If true, it's still possible to refund the disputed payment. After the payment has been fully refunded, no further funds are withdrawn from your Stripe account as a result of this dispute. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) | yes | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `object` | enum: `dispute` | yes | String representing the object's type. Objects of the same type share the same value. |
| `payment_intent` | string or `payment_intent` |  | ID of the PaymentIntent that's disputed. |
| `payment_method_details` | `dispute_payment_method_details` |  |  |
| `reason` | string | yes | Reason given by cardholder for dispute. Possible values are `bank_cannot_process`, `check_returned`, `credit_not_processed`, `customer_initiated`, `debit_not_authorized`, `duplicate`, `fraudulent`, `general`, `incorrect_account_details`, `insufficient_funds`, `product_not_received`, `product_unacceptable`, `subscription_canceled`, or `unrecognized`. Learn more about [dispute reasons](https://stripe.com/docs/disputes/categories). |
| `status` | enum: `lost`, `needs_response`, `under_review`, `warning_closed`, `warning_needs_response`, `warning_under_review`, `won` | yes | Current status of dispute. Possible values are `warning_needs_response`, `warning_under_review`, `warning_closed`, `needs_response`, `under_review`, `won`, or `lost`. |

