# Stripe API 2023-10-16 — sources

Operations under `/v1/sources` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## POST /v1/sources

operationId: `PostSources`

Creates a new source object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer |  | Amount associated with the source. This is the amount for which the source will be chargeable once ready. Required for `single_use` sources. Not supported for `receiver` type sources, where charge amount may not be specified until funds land. |
| `currency` | string |  | Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) associated with the source. This is the currency for which the source will be chargeable once ready. |
| `customer` | string |  | The `Customer` to whom the original source is attached to. Must be set when the original source is not a `Source` (e.g., `Card`). |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `flow` | enum: `code_verification`, `none`, `receiver`, `redirect` |  | The authentication `flow` of the source to create. `flow` is one of `redirect`, `receiver`, `code_verification`, `none`. It is generally inferred unless a type supports multiple flows. |
| `mandate` | object |  | Information about a mandate possibility attached to a source object (generally for bank debits) as well as its acceptance status. |
| `mandate.acceptance` | object |  |  |
| `mandate.acceptance.date` | timestamp (Unix seconds) |  |  |
| `mandate.acceptance.ip` | string |  |  |
| `mandate.acceptance.offline` | object |  |  |
| `mandate.acceptance.offline.contact_email` | string | yes |  |
| `mandate.acceptance.online` | object |  |  |
| `mandate.acceptance.online.date` | timestamp (Unix seconds) |  |  |
| `mandate.acceptance.online.ip` | string |  |  |
| `mandate.acceptance.online.user_agent` | string |  |  |
| `mandate.acceptance.status` | enum: `accepted`, `pending`, `refused`, `revoked` | yes |  |
| `mandate.acceptance.type` | enum: `offline`, `online` |  |  |
| `mandate.acceptance.user_agent` | string |  |  |
| `mandate.amount` | integer or "" (to unset) |  |  |
| `mandate.currency` | string |  |  |
| `mandate.interval` | enum: `one_time`, `scheduled`, `variable` |  |  |
| `mandate.notification_method` | enum: `deprecated_none`, `email`, `manual`, `none`, `stripe_email` |  |  |
| `metadata` | map (key → value) |  |  |
| `original_source` | string |  | The source to share. |
| `owner` | object |  | Information about the owner of the payment instrument that may be used or required by particular source types. |
| `owner.address` | object |  |  |
| `owner.address.city` | string |  |  |
| `owner.address.country` | string |  |  |
| `owner.address.line1` | string |  |  |
| `owner.address.line2` | string |  |  |
| `owner.address.postal_code` | string |  |  |
| `owner.address.state` | string |  |  |
| `owner.email` | string |  |  |
| `owner.name` | string |  |  |
| `owner.phone` | string |  |  |
| `receiver` | object |  | Optional parameters for the receiver flow. Can be set only if the source is a receiver (`flow` is `receiver`). |
| `receiver.refund_attributes_method` | enum: `email`, `manual`, `none` |  |  |
| `redirect` | object |  | Parameters required for the redirect flow. Required if the source is authenticated by a redirect (`flow` is `redirect`). |
| `redirect.return_url` | string | yes |  |
| `source_order` | object |  | Information about the items and shipping associated with the source. Required for transactional credit (for example Klarna) sources before you can charge it. |
| `source_order.items` | array of object |  |  |
| `source_order.items[].amount` | integer |  |  |
| `source_order.items[].currency` | string |  |  |
| `source_order.items[].description` | string |  |  |
| `source_order.items[].parent` | string |  |  |
| `source_order.items[].quantity` | integer |  |  |
| `source_order.items[].type` | enum: `discount`, `shipping`, `sku`, `tax` |  |  |
| `source_order.shipping` | object |  |  |
| `source_order.shipping.address` | object | yes |  |
| `source_order.shipping.address.city` | string |  |  |
| `source_order.shipping.address.country` | string |  |  |
| `source_order.shipping.address.line1` | string | yes |  |
| `source_order.shipping.address.line2` | string |  |  |
| `source_order.shipping.address.postal_code` | string |  |  |
| `source_order.shipping.address.state` | string |  |  |
| `source_order.shipping.carrier` | string |  |  |
| `source_order.shipping.name` | string |  |  |
| `source_order.shipping.phone` | string |  |  |
| `source_order.shipping.tracking_number` | string |  |  |
| `statement_descriptor` | string |  | An arbitrary string to be displayed on your customer's statement. As an example, if your website is `RunClub` and the item you're charging for is a race ticket, you may want to specify a `statement_descriptor` of `RunClub 5K race ticket.` While many payment types will display this information, some may not display it at all. |
| `token` | string |  | An optional token used to create the source. When passed, token properties will override source parameters. |
| `type` | string |  | The `type` of the source to create. Required unless `customer` and `original_source` are specified (see the [Cloning card Sources](https://stripe.com/docs/sources/connect#cloning-card-sources) guide) |
| `usage` | enum: `reusable`, `single_use` |  |  |

Returns: `source`

## GET /v1/sources/{source}

operationId: `GetSourcesSource`

Retrieves an existing source object. Supply the unique source ID from a source creation request and Stripe will return the corresponding up-to-date source object information.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `client_secret` | string |  | The client secret of the source. Required if a publishable key is used to retrieve the source. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `source (path)` | string | yes |  |

Returns: `source`

## POST /v1/sources/{source}

operationId: `PostSourcesSource`

Updates the specified source by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

This request accepts the `metadata` and `owner` as arguments. It is also possible to update type specific information for selected payment methods. Please refer to our [payment method guides](https://stripe.com/docs/sources) for more detail.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `source (path)` | string | yes |  |
| `amount` | integer |  | Amount associated with the source. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `mandate` | object |  | Information about a mandate possibility attached to a source object (generally for bank debits) as well as its acceptance status. |
| `mandate.acceptance` | object |  |  |
| `mandate.acceptance.date` | timestamp (Unix seconds) |  |  |
| `mandate.acceptance.ip` | string |  |  |
| `mandate.acceptance.offline` | object |  |  |
| `mandate.acceptance.offline.contact_email` | string | yes |  |
| `mandate.acceptance.online` | object |  |  |
| `mandate.acceptance.online.date` | timestamp (Unix seconds) |  |  |
| `mandate.acceptance.online.ip` | string |  |  |
| `mandate.acceptance.online.user_agent` | string |  |  |
| `mandate.acceptance.status` | enum: `accepted`, `pending`, `refused`, `revoked` | yes |  |
| `mandate.acceptance.type` | enum: `offline`, `online` |  |  |
| `mandate.acceptance.user_agent` | string |  |  |
| `mandate.amount` | integer or "" (to unset) |  |  |
| `mandate.currency` | string |  |  |
| `mandate.interval` | enum: `one_time`, `scheduled`, `variable` |  |  |
| `mandate.notification_method` | enum: `deprecated_none`, `email`, `manual`, `none`, `stripe_email` |  |  |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `owner` | object |  | Information about the owner of the payment instrument that may be used or required by particular source types. |
| `owner.address` | object |  |  |
| `owner.address.city` | string |  |  |
| `owner.address.country` | string |  |  |
| `owner.address.line1` | string |  |  |
| `owner.address.line2` | string |  |  |
| `owner.address.postal_code` | string |  |  |
| `owner.address.state` | string |  |  |
| `owner.email` | string |  |  |
| `owner.name` | string |  |  |
| `owner.phone` | string |  |  |
| `source_order` | object |  | Information about the items and shipping associated with the source. Required for transactional credit (for example Klarna) sources before you can charge it. |
| `source_order.items` | array of object |  |  |
| `source_order.items[].amount` | integer |  |  |
| `source_order.items[].currency` | string |  |  |
| `source_order.items[].description` | string |  |  |
| `source_order.items[].parent` | string |  |  |
| `source_order.items[].quantity` | integer |  |  |
| `source_order.items[].type` | enum: `discount`, `shipping`, `sku`, `tax` |  |  |
| `source_order.shipping` | object |  |  |
| `source_order.shipping.address` | object | yes |  |
| `source_order.shipping.address.city` | string |  |  |
| `source_order.shipping.address.country` | string |  |  |
| `source_order.shipping.address.line1` | string | yes |  |
| `source_order.shipping.address.line2` | string |  |  |
| `source_order.shipping.address.postal_code` | string |  |  |
| `source_order.shipping.address.state` | string |  |  |
| `source_order.shipping.carrier` | string |  |  |
| `source_order.shipping.name` | string |  |  |
| `source_order.shipping.phone` | string |  |  |
| `source_order.shipping.tracking_number` | string |  |  |

Returns: `source`

## GET /v1/sources/{source}/mandate_notifications/{mandate_notification}

operationId: `GetSourcesSourceMandateNotificationsMandateNotification`

Retrieves a new Source MandateNotification.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `mandate_notification (path)` | string | yes |  |
| `source (path)` | string | yes |  |

Returns: `source_mandate_notification`

## GET /v1/sources/{source}/source_transactions

operationId: `GetSourcesSourceSourceTransactions`

List source transactions for a given source.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `source (path)` | string | yes |  |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## GET /v1/sources/{source}/source_transactions/{source_transaction}

operationId: `GetSourcesSourceSourceTransactionsSourceTransaction`

Retrieve an existing source transaction object. Supply the unique source ID from a source creation request and the source transaction ID and Stripe will return the corresponding up-to-date source object information.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `source (path)` | string | yes |  |
| `source_transaction (path)` | string | yes |  |

Returns: `source_transaction`

## POST /v1/sources/{source}/verify

operationId: `PostSourcesSourceVerify`

Verify a given source.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `source (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `values` | array of string | yes | The values needed to verify the source. |

Returns: `source`

# Objects returned

## The `source` object

`Source` objects allow you to accept a variety of payment methods. They
represent a customer's payment instrument, and can be used with the Stripe API
just like a `Card` object: once chargeable, they can be charged, or can be
attached to customers.

Stripe doesn't recommend using the deprecated [Sources API](https://stripe.com/docs/api/sources).
We recommend that you adopt the [PaymentMethods API](https://stripe.com/docs/api/payment_methods).
This newer API provides access to our latest features and payment method types.

Related guides: [Sources API](https://stripe.com/docs/sources) and [Sources & Customers](https://stripe.com/docs/sources/customers).

Expandable fields (pass `expand[]=<field>`): `code_verification`, `owner`, `receiver`, `redirect`, `source_order`

| Field | Type | Required | Description |
|---|---|---|---|
| `ach_credit_transfer` | `source_type_ach_credit_transfer` |  |  |
| `ach_debit` | `source_type_ach_debit` |  |  |
| `acss_debit` | `source_type_acss_debit` |  |  |
| `alipay` | `source_type_alipay` |  |  |
| `amount` | integer |  | A positive integer in the smallest currency unit (that is, 100 cents for $1.00, or 1 for ¥1, Japanese Yen being a zero-decimal currency) representing the total amount associated with the source. This is the amount for which the source will be chargeable once ready. Required for `single_use` sources. |
| `au_becs_debit` | `source_type_au_becs_debit` |  |  |
| `bancontact` | `source_type_bancontact` |  |  |
| `card` | `source_type_card` |  |  |
| `card_present` | `source_type_card_present` |  |  |
| `client_secret` | string | yes | The client secret of the source. Used for client-side retrieval using a publishable key. |
| `code_verification` | `source_code_verification_flow` |  |  |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string |  | Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) associated with the source. This is the currency for which the source will be chargeable once ready. Required for `single_use` sources. |
| `customer` | string |  | The ID of the customer to which this source is attached. This will not be present when the source has not been attached to a customer. |
| `eps` | `source_type_eps` |  |  |
| `flow` | string | yes | The authentication `flow` of the source. `flow` is one of `redirect`, `receiver`, `code_verification`, `none`. |
| `giropay` | `source_type_giropay` |  |  |
| `id` | string | yes | Unique identifier for the object. |
| `ideal` | `source_type_ideal` |  |  |
| `klarna` | `source_type_klarna` |  |  |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `multibanco` | `source_type_multibanco` |  |  |
| `object` | enum: `source` | yes | String representing the object's type. Objects of the same type share the same value. |
| `owner` | `source_owner` |  | Information about the owner of the payment instrument that may be used or required by particular source types. |
| `p24` | `source_type_p24` |  |  |
| `receiver` | `source_receiver_flow` |  |  |
| `redirect` | `source_redirect_flow` |  |  |
| `sepa_debit` | `source_type_sepa_debit` |  |  |
| `sofort` | `source_type_sofort` |  |  |
| `source_order` | `source_order` |  |  |
| `statement_descriptor` | string |  | Extra information about a source. This will appear on your customer's statement every time you charge the source. |
| `status` | string | yes | The status of the source, one of `canceled`, `chargeable`, `consumed`, `failed`, or `pending`. Only `chargeable` sources can be used to create a charge. |
| `three_d_secure` | `source_type_three_d_secure` |  |  |
| `type` | enum: `ach_credit_transfer`, `ach_debit`, `acss_debit`, `alipay`, `au_becs_debit`, `bancontact`, `card`, `card_present`, `eps`, `giropay`, `ideal`, `klarna`, `multibanco`, `p24`, `sepa_debit`, `sofort`, `three_d_secure`, `wechat` | yes | The `type` of the source. The `type` is a payment method, one of `ach_credit_transfer`, `ach_debit`, `alipay`, `bancontact`, `card`, `card_present`, `eps`, `giropay`, `ideal`, `multibanco`, `klarna`, `p24`, `sepa_debit`, `sofort`, `three_d_secure`, or `wechat`. An additional hash is included on the source with a name matching this value. It contains additional information specific to the [payment method](https://stripe.com/docs/sources) used. |
| `usage` | string |  | Either `reusable` or `single_use`. Whether this source should be reusable or not. Some source types may or may not be reusable by construction, while others may leave the option at creation. If an incompatible value is passed, an error will be returned. |
| `wechat` | `source_type_wechat` |  |  |

## The `source_mandate_notification` object

Source mandate notifications should be created when a notification related to
a source mandate must be sent to the payer. They will trigger a webhook or
deliver an email to the customer.

Expandable fields (pass `expand[]=<field>`): `acss_debit`, `bacs_debit`, `sepa_debit`, `source`

| Field | Type | Required | Description |
|---|---|---|---|
| `acss_debit` | `source_mandate_notification_acss_debit_data` |  |  |
| `amount` | integer |  | A positive integer in the smallest currency unit (that is, 100 cents for $1.00, or 1 for ¥1, Japanese Yen being a zero-decimal currency) representing the amount associated with the mandate notification. The amount is expressed in the currency of the underlying source. Required if the notification type is `debit_initiated`. |
| `bacs_debit` | `source_mandate_notification_bacs_debit_data` |  |  |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `object` | enum: `source_mandate_notification` | yes | String representing the object's type. Objects of the same type share the same value. |
| `reason` | string | yes | The reason of the mandate notification. Valid reasons are `mandate_confirmed` or `debit_initiated`. |
| `sepa_debit` | `source_mandate_notification_sepa_debit_data` |  |  |
| `source` | `source` | yes |  |
| `status` | string | yes | The status of the mandate notification. Valid statuses are `pending` or `submitted`. |
| `type` | string | yes | The type of source this mandate notification is attached to. Should be the source type identifier code for the payment method, such as `three_d_secure`. |

## The `source_transaction` object

Some payment methods have no required amount that a customer must send.
Customers can be instructed to send any amount, and it can be made up of
multiple transactions. As such, sources can have multiple associated
transactions.

Expandable fields (pass `expand[]=<field>`): `ach_credit_transfer`, `chf_credit_transfer`, `gbp_credit_transfer`, `paper_check`, `sepa_credit_transfer`

| Field | Type | Required | Description |
|---|---|---|---|
| `ach_credit_transfer` | `source_transaction_ach_credit_transfer_data` |  |  |
| `amount` | integer | yes | A positive integer in the smallest currency unit (that is, 100 cents for $1.00, or 1 for ¥1, Japanese Yen being a zero-decimal currency) representing the amount your customer has pushed to the receiver. |
| `chf_credit_transfer` | `source_transaction_chf_credit_transfer_data` |  |  |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `gbp_credit_transfer` | `source_transaction_gbp_credit_transfer_data` |  |  |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `object` | enum: `source_transaction` | yes | String representing the object's type. Objects of the same type share the same value. |
| `paper_check` | `source_transaction_paper_check_data` |  |  |
| `sepa_credit_transfer` | `source_transaction_sepa_credit_transfer_data` |  |  |
| `source` | string | yes | The ID of the source this transaction is attached to. |
| `status` | string | yes | The status of the transaction, one of `succeeded`, `pending`, or `failed`. |
| `type` | enum: `ach_credit_transfer`, `ach_debit`, `alipay`, `bancontact`, `card`, `card_present`, `eps`, `giropay`, `ideal`, `klarna`, `multibanco`, `p24`, `sepa_debit`, `sofort`, `three_d_secure`, `wechat` | yes | The type of source this transaction is attached to. |

