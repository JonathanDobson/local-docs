# Stripe API 2023-10-16 — charges

Operations under `/v1/charges` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/charges

operationId: `GetCharges`

Returns a list of charges you’ve previously created. The charges are returned in sorted order, with the most recent charges appearing first.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | object or integer |  | Only return charges that were created during the given date interval. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `customer` | string |  | Only return charges for the customer specified by this customer ID. |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `payment_intent` | string |  | Only return charges that were created by the PaymentIntent specified by this PaymentIntent ID. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `transfer_group` | string |  | Only return charges for this transfer group. |

Returns: object

## POST /v1/charges

operationId: `PostCharges`

This method is no longer recommended—use the [Payment Intents API](https://stripe.com/docs/api/payment_intents)
to initiate a new payment instead. Confirmation of the PaymentIntent creates the `Charge`
object used to request payment.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer |  | Amount intended to be collected by this payment. A positive integer representing how much to charge in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or [equivalent in charge currency](https://stripe.com/docs/currencies#minimum-and-maximum-charge-amounts). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99). |
| `application_fee` | integer |  |  |
| `application_fee_amount` | integer |  | A fee in cents (or local equivalent) that will be applied to the charge and transferred to the application owner's Stripe account. The request must be made with an OAuth key or the `Stripe-Account` header in order to take an application fee. For more information, see the application fees [documentation](https://stripe.com/docs/connect/direct-charges#collecting-fees). |
| `capture` | boolean |  | Whether to immediately capture the charge. Defaults to `true`. When `false`, the charge issues an authorization (or pre-authorization), and will need to be [captured](https://stripe.com/docs/api#capture_charge) later. Uncaptured charges expire after a set number of days (7 by default). For more information, see the [authorizing charges and settling later](https://stripe.com/docs/charges/placing-a-hold) documentation. |
| `card` | object or string |  | A token, like the ones returned by [Stripe.js](https://stripe.com/docs/js). |
| `card.address_city` | string |  |  |
| `card.address_country` | string |  |  |
| `card.address_line1` | string |  |  |
| `card.address_line2` | string |  |  |
| `card.address_state` | string |  |  |
| `card.address_zip` | string |  |  |
| `card.cvc` | string |  |  |
| `card.exp_month` | integer | yes |  |
| `card.exp_year` | integer | yes |  |
| `card.metadata` | map (key → value) |  |  |
| `card.name` | string |  |  |
| `card.number` | string | yes |  |
| `card.object` | enum: `card` |  |  |
| `currency` | string |  | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `customer` | string |  | The ID of an existing customer that will be charged in this request. |
| `description` | string |  | An arbitrary string which you can attach to a `Charge` object. It is displayed when in the web interface alongside the charge. Note that if you use Stripe to send automatic email receipts to your customers, your receipt emails will include the `description` of the charge(s) that they are describing. |
| `destination` | object or string |  |  |
| `destination.account` | string | yes |  |
| `destination.amount` | integer |  |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `on_behalf_of` | string |  | The Stripe account ID for which these funds are intended. Automatically set if you use the `destination` parameter. For details, see [Creating Separate Charges and Transfers](https://stripe.com/docs/connect/separate-charges-and-transfers#on-behalf-of). |
| `radar_options` | object |  | Options to configure Radar. See [Radar Session](https://stripe.com/docs/radar/radar-session) for more information. |
| `radar_options.session` | string |  |  |
| `receipt_email` | string |  | The email address to which this charge's [receipt](https://stripe.com/docs/dashboard/receipts) will be sent. The receipt will not be sent until the charge is paid, and no receipts will be sent for test mode charges. If this charge is for a [Customer](https://stripe.com/docs/api/customers/object), the email address specified here will override the customer's email address. If `receipt_email` is specified for a charge in live mode, a receipt will be sent regardless of your [email settings](https://dashboard.stripe.com/account/emails). |
| `shipping` | object |  | Shipping information for the charge. Helps prevent fraud on charges for physical goods. |
| `shipping.address` | object | yes |  |
| `shipping.address.city` | string |  |  |
| `shipping.address.country` | string |  |  |
| `shipping.address.line1` | string |  |  |
| `shipping.address.line2` | string |  |  |
| `shipping.address.postal_code` | string |  |  |
| `shipping.address.state` | string |  |  |
| `shipping.carrier` | string |  |  |
| `shipping.name` | string | yes |  |
| `shipping.phone` | string |  |  |
| `shipping.tracking_number` | string |  |  |
| `source` | string (open enum) |  | A payment source to be charged. This can be the ID of a [card](https://stripe.com/docs/api#cards) (i.e., credit or debit card), a [bank account](https://stripe.com/docs/api#bank_accounts), a [source](https://stripe.com/docs/api#sources), a [token](https://stripe.com/docs/api#tokens), or a [connected account](https://stripe.com/docs/connect/account-debits#charging-a-connected-account). For certain sources---namely, [cards](https://stripe.com/docs/api#cards), [bank accounts](https://stripe.com/docs/api#bank_accounts), and attached [sources](https://stripe.com/docs/api#sources)---you must also pass the ID of the associated customer. |
| `statement_descriptor` | string |  | For card charges, use `statement_descriptor_suffix` instead. Otherwise, you can use this value as the complete description of a charge on your customers’ statements. Must contain at least one letter, maximum 22 characters. |
| `statement_descriptor_suffix` | string |  | Provides information about the charge that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that’s set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor. |
| `transfer_data` | object |  | An optional dictionary including the account to automatically transfer to as part of a destination charge. [See the Connect documentation](https://stripe.com/docs/connect/destination-charges) for details. |
| `transfer_data.amount` | integer |  |  |
| `transfer_data.destination` | string | yes |  |
| `transfer_group` | string |  | A string that identifies this transaction as part of a group. For details, see [Grouping transactions](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-options). |

Returns: `charge`

## GET /v1/charges/search

operationId: `GetChargesSearch`

Search for charges you’ve previously created using Stripe’s [Search Query Language](https://stripe.com/docs/search#search-query-language).
Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating
conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up
to an hour behind during outages. Search functionality is not available to merchants in India.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `page` | string |  | A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results. |
| `query` | string | yes | The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for charges](https://stripe.com/docs/search#query-fields-for-charges). |

Returns: object

## GET /v1/charges/{charge}

operationId: `GetChargesCharge`

Retrieves the details of a charge that has previously been created. Supply the unique charge ID that was returned from your previous request, and Stripe will return the corresponding charge information. The same information is returned when creating or refunding the charge.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `charge (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `charge`

## POST /v1/charges/{charge}

operationId: `PostChargesCharge`

Updates the specified charge by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `charge (path)` | string | yes |  |
| `customer` | string |  | The ID of an existing customer that will be associated with this request. This field may only be updated if there is no existing associated customer with this charge. |
| `description` | string |  | An arbitrary string which you can attach to a charge object. It is displayed when in the web interface alongside the charge. Note that if you use Stripe to send automatic email receipts to your customers, your receipt emails will include the `description` of the charge(s) that they are describing. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `fraud_details` | object |  | A set of key-value pairs you can attach to a charge giving information about its riskiness. If you believe a charge is fraudulent, include a `user_report` key with a value of `fraudulent`. If you believe a charge is safe, include a `user_report` key with a value of `safe`. Stripe will use the information you send to improve our fraud detection algorithms. |
| `fraud_details.user_report` | enum: ``, `fraudulent`, `safe` | yes |  |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `receipt_email` | string |  | This is the email address that the receipt for this charge will be sent to. If this field is updated, then a new email receipt will be sent to the updated address. |
| `shipping` | object |  | Shipping information for the charge. Helps prevent fraud on charges for physical goods. |
| `shipping.address` | object | yes |  |
| `shipping.address.city` | string |  |  |
| `shipping.address.country` | string |  |  |
| `shipping.address.line1` | string |  |  |
| `shipping.address.line2` | string |  |  |
| `shipping.address.postal_code` | string |  |  |
| `shipping.address.state` | string |  |  |
| `shipping.carrier` | string |  |  |
| `shipping.name` | string | yes |  |
| `shipping.phone` | string |  |  |
| `shipping.tracking_number` | string |  |  |
| `transfer_group` | string |  | A string that identifies this transaction as part of a group. `transfer_group` may only be provided if it has not been set. See the [Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-options) for details. |

Returns: `charge`

## POST /v1/charges/{charge}/capture

operationId: `PostChargesChargeCapture`

Capture the payment of an existing, uncaptured charge that was created with the `capture` option set to false.

Uncaptured payments expire a set number of days after they are created ([7 by default](https://stripe.com/docs/charges/placing-a-hold)), after which they are marked as refunded and capture attempts will fail.

Don’t use this method to capture a PaymentIntent-initiated charge. Use [Capture a PaymentIntent](https://stripe.com/docs/api/payment_intents/capture).

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `charge (path)` | string | yes |  |
| `amount` | integer |  | The amount to capture, which must be less than or equal to the original amount. Any additional amount will be automatically refunded. |
| `application_fee` | integer |  | An application fee to add on to this charge. |
| `application_fee_amount` | integer |  | An application fee amount to add on to this charge, which must be less than or equal to the original amount. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `receipt_email` | string |  | The email address to send this charge's receipt to. This will override the previously-specified email address for this charge, if one was set. Receipts will not be sent in test mode. |
| `statement_descriptor` | string |  | For card charges, use `statement_descriptor_suffix` instead. Otherwise, you can use this value as the complete description of a charge on your customers’ statements. Must contain at least one letter, maximum 22 characters. |
| `statement_descriptor_suffix` | string |  | Provides information about the charge that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that’s set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor. |
| `transfer_data` | object |  | An optional dictionary including the account to automatically transfer to as part of a destination charge. [See the Connect documentation](https://stripe.com/docs/connect/destination-charges) for details. |
| `transfer_data.amount` | integer |  |  |
| `transfer_group` | string |  | A string that identifies this transaction as part of a group. `transfer_group` may only be provided if it has not been set. See the [Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-options) for details. |

Returns: `charge`

## GET /v1/charges/{charge}/dispute

operationId: `GetChargesChargeDispute`

Retrieve a dispute for a specified charge.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `charge (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `dispute`

## POST /v1/charges/{charge}/dispute

operationId: `PostChargesChargeDispute`

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `charge (path)` | string | yes |  |
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

## POST /v1/charges/{charge}/dispute/close

operationId: `PostChargesChargeDisputeClose`

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `charge (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `dispute`

## POST /v1/charges/{charge}/refund

operationId: `PostChargesChargeRefund`

When you create a new refund, you must specify either a Charge or a PaymentIntent object.

This action refunds a previously created charge that’s not refunded yet.
Funds are refunded to the credit or debit card that’s originally charged.

You can optionally refund only part of a charge.
You can repeat this until the entire charge is refunded.

After you entirely refund a charge, you can’t refund it again.
This method raises an error when it’s called on an already-refunded charge,
or when you attempt to refund more money than is left on a charge.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `charge (path)` | string | yes | The identifier of the charge to refund. |
| `amount` | integer |  | A positive integer in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) representing how much of this charge to refund. Can refund only up to the remaining, unrefunded amount of the charge. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `instructions_email` | string |  | For payment methods without native refund support (e.g., Konbini, PromptPay), use this email from the customer to receive refund instructions. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `payment_intent` | string |  | The identifier of the PaymentIntent to refund. |
| `reason` | enum: `duplicate`, `fraudulent`, `requested_by_customer` |  | String indicating the reason for the refund. If set, possible values are `duplicate`, `fraudulent`, and `requested_by_customer`. If you believe the charge to be fraudulent, specifying `fraudulent` as the reason will add the associated card and email to your [block lists](https://stripe.com/docs/radar/lists), and will also help us improve our fraud detection algorithms. |
| `refund_application_fee` | boolean |  | Boolean indicating whether the application fee should be refunded when refunding this charge. If a full charge refund is given, the full application fee will be refunded. Otherwise, the application fee will be refunded in an amount proportional to the amount of the charge refunded. An application fee can be refunded only by the application that created the charge. |
| `reverse_transfer` | boolean |  | Boolean indicating whether the transfer should be reversed when refunding this charge. The transfer will be reversed proportionally to the amount being refunded (either the entire or partial amount).<br>A transfer can be reversed only by the application that created the charge. |

Returns: `charge`

## GET /v1/charges/{charge}/refunds

operationId: `GetChargesChargeRefunds`

You can see a list of the refunds belonging to a specific charge. Note that the 10 most recent refunds are always available by default on the charge object. If you need more than those 10, you can use this API method and the `limit` and `starting_after` parameters to page through additional refunds.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `charge (path)` | string | yes |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/charges/{charge}/refunds

operationId: `PostChargesChargeRefunds`

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
| `charge (path)` | string | yes | The identifier of the charge to refund. |
| `amount` | integer |  |  |
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

## GET /v1/charges/{charge}/refunds/{refund}

operationId: `GetChargesChargeRefundsRefund`

Retrieves the details of an existing refund.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `charge (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `refund (path)` | string | yes |  |

Returns: `refund`

## POST /v1/charges/{charge}/refunds/{refund}

operationId: `PostChargesChargeRefundsRefund`

Update a specified refund.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `charge (path)` | string | yes |  |
| `refund (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) or "" (to unset) |  |  |

Returns: `refund`

# Objects returned

## The `charge` object

The `Charge` object represents a single attempt to move money into your Stripe account.
PaymentIntent confirmation is the most common way to create Charges, but transferring
money to a different Stripe account through Connect also creates Charges.
Some legacy payment flows create Charges directly, which is not recommended for new integrations.

Expandable fields (pass `expand[]=<field>`): `application`, `application_fee`, `balance_transaction`, `billing_details`, `customer`, `failure_balance_transaction`, `fraud_details`, `invoice`, `on_behalf_of`, `outcome`, `payment_intent`, `payment_method_details`, `radar_options`, `refunds`, `review`, `shipping`, `source_transfer`, `transfer`, `transfer_data`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | Amount intended to be collected by this payment. A positive integer representing how much to charge in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or [equivalent in charge currency](https://stripe.com/docs/currencies#minimum-and-maximum-charge-amounts). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99). |
| `amount_captured` | integer | yes | Amount in cents (or local equivalent) captured (can be less than the amount attribute on the charge if a partial capture was made). |
| `amount_refunded` | integer | yes | Amount in cents (or local equivalent) refunded (can be less than the amount attribute on the charge if a partial refund was issued). |
| `application` | string or `application` |  | ID of the Connect application that created the charge. |
| `application_fee` | string or `application_fee` |  | The application fee (if any) for the charge. [See the Connect documentation](https://stripe.com/docs/connect/direct-charges#collecting-fees) for details. |
| `application_fee_amount` | integer |  | The amount of the application fee (if any) requested for the charge. [See the Connect documentation](https://stripe.com/docs/connect/direct-charges#collecting-fees) for details. |
| `balance_transaction` | string or `balance_transaction` |  | ID of the balance transaction that describes the impact of this charge on your account balance (not including refunds or disputes). |
| `billing_details` | `billing_details` | yes |  |
| `calculated_statement_descriptor` | string |  | The full statement descriptor that is passed to card networks, and that is displayed on your customers' credit card and bank statements. Allows you to see what the statement descriptor looks like after the static and dynamic portions are combined. |
| `captured` | boolean | yes | If the charge was created without capturing, this Boolean represents whether it is still uncaptured or has since been captured. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `customer` | string or `customer` or `deleted_customer` |  | ID of the customer this charge is for if one exists. |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. |
| `disputed` | boolean | yes | Whether the charge has been disputed. |
| `failure_balance_transaction` | string or `balance_transaction` |  | ID of the balance transaction that describes the reversal of the balance on your account due to payment failure. |
| `failure_code` | string |  | Error code explaining reason for charge failure if available (see [the errors section](https://stripe.com/docs/error-codes) for a list of codes). |
| `failure_message` | string |  | Message to user further explaining reason for charge failure if available. |
| `fraud_details` | `charge_fraud_details` |  | Information on fraud assessments for the charge. |
| `id` | string | yes | Unique identifier for the object. |
| `invoice` | string or `invoice` |  | ID of the invoice this charge is for if one exists. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) | yes | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `object` | enum: `charge` | yes | String representing the object's type. Objects of the same type share the same value. |
| `on_behalf_of` | string or `account` |  | The account (if any) the charge was made on behalf of without triggering an automatic transfer. See the [Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers) for details. |
| `outcome` | `charge_outcome` |  | Details about whether the payment was accepted, and why. See [understanding declines](https://stripe.com/docs/declines) for details. |
| `paid` | boolean | yes | `true` if the charge succeeded, or was successfully authorized for later capture. |
| `payment_intent` | string or `payment_intent` |  | ID of the PaymentIntent associated with this charge, if one exists. |
| `payment_method` | string |  | ID of the payment method used in this charge. |
| `payment_method_details` | `payment_method_details` |  | Details about the payment method at the time of the transaction. |
| `radar_options` | `radar_radar_options` |  |  |
| `receipt_email` | string |  | This is the email address that the receipt for this charge was sent to. |
| `receipt_number` | string |  | This is the transaction number that appears on email receipts sent for this charge. This attribute will be `null` until a receipt has been sent. |
| `receipt_url` | string |  | This is the URL to view the receipt for this charge. The receipt is kept up-to-date to the latest state of the charge, including any refunds. If the charge is for an Invoice, the receipt will be stylized as an Invoice receipt. |
| `refunded` | boolean | yes | Whether the charge has been fully refunded. If the charge is only partially refunded, this attribute will still be false. |
| `refunds` | object |  | A list of refunds that have been applied to the charge. |
| `review` | string or `review` |  | ID of the review associated with this charge if one exists. |
| `shipping` | `shipping` |  | Shipping information for the charge. |
| `source_transfer` | string or `transfer` |  | The transfer ID which created this charge. Only present if the charge came from another Stripe account. [See the Connect documentation](https://stripe.com/docs/connect/destination-charges) for details. |
| `statement_descriptor` | string |  | For card charges, use `statement_descriptor_suffix` instead. Otherwise, you can use this value as the complete description of a charge on your customers’ statements. Must contain at least one letter, maximum 22 characters. |
| `statement_descriptor_suffix` | string |  | Provides information about the charge that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that’s set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor. |
| `status` | enum: `failed`, `pending`, `succeeded` | yes | The status of the payment is either `succeeded`, `pending`, or `failed`. |
| `transfer` | string or `transfer` |  | ID of the transfer to the `destination` account (only applicable if the charge was created using the `destination` parameter). |
| `transfer_data` | `charge_transfer_data` |  | An optional dictionary including the account to automatically transfer to as part of a destination charge. [See the Connect documentation](https://stripe.com/docs/connect/destination-charges) for details. |
| `transfer_group` | string |  | A string that identifies this transaction as part of a group. See the [Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-options) for details. |

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

