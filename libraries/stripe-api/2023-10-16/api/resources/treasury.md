# Stripe API 2023-10-16 — treasury

Operations under `/v1/treasury` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/treasury/credit_reversals

operationId: `GetTreasuryCreditReversals`

Returns a list of CreditReversals.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `financial_account` | string | yes | Returns objects associated with this FinancialAccount. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `received_credit` | string |  | Only return CreditReversals for the ReceivedCredit ID. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `status` | enum: `canceled`, `posted`, `processing` |  | Only return CreditReversals for a given status. |

Returns: object

## POST /v1/treasury/credit_reversals

operationId: `PostTreasuryCreditReversals`

Reverses a ReceivedCredit and creates a CreditReversal object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `received_credit` | string | yes | The ReceivedCredit to reverse. |

Returns: `treasury.credit_reversal`

## GET /v1/treasury/credit_reversals/{credit_reversal}

operationId: `GetTreasuryCreditReversalsCreditReversal`

Retrieves the details of an existing CreditReversal by passing the unique CreditReversal ID from either the CreditReversal creation request or CreditReversal list

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `credit_reversal (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `treasury.credit_reversal`

## GET /v1/treasury/debit_reversals

operationId: `GetTreasuryDebitReversals`

Returns a list of DebitReversals.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `financial_account` | string | yes | Returns objects associated with this FinancialAccount. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `received_debit` | string |  | Only return DebitReversals for the ReceivedDebit ID. |
| `resolution` | enum: `lost`, `won` |  | Only return DebitReversals for a given resolution. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `status` | enum: `canceled`, `completed`, `processing` |  | Only return DebitReversals for a given status. |

Returns: object

## POST /v1/treasury/debit_reversals

operationId: `PostTreasuryDebitReversals`

Reverses a ReceivedDebit and creates a DebitReversal object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `received_debit` | string | yes | The ReceivedDebit to reverse. |

Returns: `treasury.debit_reversal`

## GET /v1/treasury/debit_reversals/{debit_reversal}

operationId: `GetTreasuryDebitReversalsDebitReversal`

Retrieves a DebitReversal object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `debit_reversal (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `treasury.debit_reversal`

## GET /v1/treasury/financial_accounts

operationId: `GetTreasuryFinancialAccounts`

Returns a list of FinancialAccounts.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | object or integer |  | Only return FinancialAccounts that were created during the given date interval. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `ending_before` | string |  | An object ID cursor for use in pagination. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit ranging from 1 to 100 (defaults to 10). |
| `starting_after` | string |  | An object ID cursor for use in pagination. |

Returns: object

## POST /v1/treasury/financial_accounts

operationId: `PostTreasuryFinancialAccounts`

Creates a new FinancialAccount. For now, each connected account can only have one FinancialAccount.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `features` | object |  | Encodes whether a FinancialAccount has access to a particular feature. Stripe or the platform can control features via the requested field. |
| `features.card_issuing` | object |  |  |
| `features.card_issuing.requested` | boolean | yes |  |
| `features.deposit_insurance` | object |  |  |
| `features.deposit_insurance.requested` | boolean | yes |  |
| `features.financial_addresses` | object |  |  |
| `features.financial_addresses.aba` | object |  |  |
| `features.financial_addresses.aba.requested` | boolean | yes |  |
| `features.inbound_transfers` | object |  |  |
| `features.inbound_transfers.ach` | object |  |  |
| `features.inbound_transfers.ach.requested` | boolean | yes |  |
| `features.intra_stripe_flows` | object |  |  |
| `features.intra_stripe_flows.requested` | boolean | yes |  |
| `features.outbound_payments` | object |  |  |
| `features.outbound_payments.ach` | object |  |  |
| `features.outbound_payments.ach.requested` | boolean | yes |  |
| `features.outbound_payments.us_domestic_wire` | object |  |  |
| `features.outbound_payments.us_domestic_wire.requested` | boolean | yes |  |
| `features.outbound_transfers` | object |  |  |
| `features.outbound_transfers.ach` | object |  |  |
| `features.outbound_transfers.ach.requested` | boolean | yes |  |
| `features.outbound_transfers.us_domestic_wire` | object |  |  |
| `features.outbound_transfers.us_domestic_wire.requested` | boolean | yes |  |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `platform_restrictions` | object |  | The set of functionalities that the platform can restrict on the FinancialAccount. |
| `platform_restrictions.inbound_flows` | enum: `restricted`, `unrestricted` |  |  |
| `platform_restrictions.outbound_flows` | enum: `restricted`, `unrestricted` |  |  |
| `supported_currencies` | array of string | yes | The currencies the FinancialAccount can hold a balance in. |

Returns: `treasury.financial_account`

## GET /v1/treasury/financial_accounts/{financial_account}

operationId: `GetTreasuryFinancialAccountsFinancialAccount`

Retrieves the details of a FinancialAccount.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `financial_account (path)` | string | yes |  |

Returns: `treasury.financial_account`

## POST /v1/treasury/financial_accounts/{financial_account}

operationId: `PostTreasuryFinancialAccountsFinancialAccount`

Updates the details of a FinancialAccount.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `financial_account (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `features` | object |  | Encodes whether a FinancialAccount has access to a particular feature, with a status enum and associated `status_details`. Stripe or the platform may control features via the requested field. |
| `features.card_issuing` | object |  |  |
| `features.card_issuing.requested` | boolean | yes |  |
| `features.deposit_insurance` | object |  |  |
| `features.deposit_insurance.requested` | boolean | yes |  |
| `features.financial_addresses` | object |  |  |
| `features.financial_addresses.aba` | object |  |  |
| `features.financial_addresses.aba.requested` | boolean | yes |  |
| `features.inbound_transfers` | object |  |  |
| `features.inbound_transfers.ach` | object |  |  |
| `features.inbound_transfers.ach.requested` | boolean | yes |  |
| `features.intra_stripe_flows` | object |  |  |
| `features.intra_stripe_flows.requested` | boolean | yes |  |
| `features.outbound_payments` | object |  |  |
| `features.outbound_payments.ach` | object |  |  |
| `features.outbound_payments.ach.requested` | boolean | yes |  |
| `features.outbound_payments.us_domestic_wire` | object |  |  |
| `features.outbound_payments.us_domestic_wire.requested` | boolean | yes |  |
| `features.outbound_transfers` | object |  |  |
| `features.outbound_transfers.ach` | object |  |  |
| `features.outbound_transfers.ach.requested` | boolean | yes |  |
| `features.outbound_transfers.us_domestic_wire` | object |  |  |
| `features.outbound_transfers.us_domestic_wire.requested` | boolean | yes |  |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `platform_restrictions` | object |  | The set of functionalities that the platform can restrict on the FinancialAccount. |
| `platform_restrictions.inbound_flows` | enum: `restricted`, `unrestricted` |  |  |
| `platform_restrictions.outbound_flows` | enum: `restricted`, `unrestricted` |  |  |

Returns: `treasury.financial_account`

## GET /v1/treasury/financial_accounts/{financial_account}/features

operationId: `GetTreasuryFinancialAccountsFinancialAccountFeatures`

Retrieves Features information associated with the FinancialAccount.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `financial_account (path)` | string | yes |  |

Returns: `treasury.financial_account_features`

## POST /v1/treasury/financial_accounts/{financial_account}/features

operationId: `PostTreasuryFinancialAccountsFinancialAccountFeatures`

Updates the Features associated with a FinancialAccount.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `financial_account (path)` | string | yes |  |
| `card_issuing` | object |  | Encodes the FinancialAccount's ability to be used with the Issuing product, including attaching cards to and drawing funds from the FinancialAccount. |
| `card_issuing.requested` | boolean | yes |  |
| `deposit_insurance` | object |  | Represents whether this FinancialAccount is eligible for deposit insurance. Various factors determine the insurance amount. |
| `deposit_insurance.requested` | boolean | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `financial_addresses` | object |  | Contains Features that add FinancialAddresses to the FinancialAccount. |
| `financial_addresses.aba` | object |  |  |
| `financial_addresses.aba.requested` | boolean | yes |  |
| `inbound_transfers` | object |  | Contains settings related to adding funds to a FinancialAccount from another Account with the same owner. |
| `inbound_transfers.ach` | object |  |  |
| `inbound_transfers.ach.requested` | boolean | yes |  |
| `intra_stripe_flows` | object |  | Represents the ability for the FinancialAccount to send money to, or receive money from other FinancialAccounts (for example, via OutboundPayment). |
| `intra_stripe_flows.requested` | boolean | yes |  |
| `outbound_payments` | object |  | Includes Features related to initiating money movement out of the FinancialAccount to someone else's bucket of money. |
| `outbound_payments.ach` | object |  |  |
| `outbound_payments.ach.requested` | boolean | yes |  |
| `outbound_payments.us_domestic_wire` | object |  |  |
| `outbound_payments.us_domestic_wire.requested` | boolean | yes |  |
| `outbound_transfers` | object |  | Contains a Feature and settings related to moving money out of the FinancialAccount into another Account with the same owner. |
| `outbound_transfers.ach` | object |  |  |
| `outbound_transfers.ach.requested` | boolean | yes |  |
| `outbound_transfers.us_domestic_wire` | object |  |  |
| `outbound_transfers.us_domestic_wire.requested` | boolean | yes |  |

Returns: `treasury.financial_account_features`

## GET /v1/treasury/inbound_transfers

operationId: `GetTreasuryInboundTransfers`

Returns a list of InboundTransfers sent from the specified FinancialAccount.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `financial_account` | string | yes | Returns objects associated with this FinancialAccount. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `status` | enum: `canceled`, `failed`, `processing`, `succeeded` |  | Only return InboundTransfers that have the given status: `processing`, `succeeded`, `failed` or `canceled`. |

Returns: object

## POST /v1/treasury/inbound_transfers

operationId: `PostTreasuryInboundTransfers`

Creates an InboundTransfer.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | Amount (in cents) to be transferred. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `financial_account` | string | yes | The FinancialAccount to send funds to. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `origin_payment_method` | string | yes | The origin payment method to be debited for the InboundTransfer. |
| `statement_descriptor` | string |  | The complete description that appears on your customers' statements. Maximum 10 characters. |

Returns: `treasury.inbound_transfer`

## GET /v1/treasury/inbound_transfers/{id}

operationId: `GetTreasuryInboundTransfersId`

Retrieves the details of an existing InboundTransfer.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `id (path)` | string | yes |  |

Returns: `treasury.inbound_transfer`

## POST /v1/treasury/inbound_transfers/{inbound_transfer}/cancel

operationId: `PostTreasuryInboundTransfersInboundTransferCancel`

Cancels an InboundTransfer.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `inbound_transfer (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `treasury.inbound_transfer`

## GET /v1/treasury/outbound_payments

operationId: `GetTreasuryOutboundPayments`

Returns a list of OutboundPayments sent from the specified FinancialAccount.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | object or integer |  | Only return OutboundPayments that were created during the given date interval. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `customer` | string |  | Only return OutboundPayments sent to this customer. |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `financial_account` | string | yes | Returns objects associated with this FinancialAccount. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `status` | enum: `canceled`, `failed`, `posted`, `processing`, `returned` |  | Only return OutboundPayments that have the given status: `processing`, `failed`, `posted`, `returned`, or `canceled`. |

Returns: object

## POST /v1/treasury/outbound_payments

operationId: `PostTreasuryOutboundPayments`

Creates an OutboundPayment.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | Amount (in cents) to be transferred. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `customer` | string |  | ID of the customer to whom the OutboundPayment is sent. Must match the Customer attached to the `destination_payment_method` passed in. |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. |
| `destination_payment_method` | string |  | The PaymentMethod to use as the payment instrument for the OutboundPayment. Exclusive with `destination_payment_method_data`. |
| `destination_payment_method_data` | object |  | Hash used to generate the PaymentMethod to be used for this OutboundPayment. Exclusive with `destination_payment_method`. |
| `destination_payment_method_data.billing_details` | object |  |  |
| `destination_payment_method_data.billing_details.address` | object or "" (to unset) |  |  |
| `destination_payment_method_data.billing_details.address.city` | string |  |  |
| `destination_payment_method_data.billing_details.address.country` | string |  |  |
| `destination_payment_method_data.billing_details.address.line1` | string |  |  |
| `destination_payment_method_data.billing_details.address.line2` | string |  |  |
| `destination_payment_method_data.billing_details.address.postal_code` | string |  |  |
| `destination_payment_method_data.billing_details.address.state` | string |  |  |
| `destination_payment_method_data.billing_details.email` | string or "" (to unset) |  |  |
| `destination_payment_method_data.billing_details.name` | string or "" (to unset) |  |  |
| `destination_payment_method_data.billing_details.phone` | string or "" (to unset) |  |  |
| `destination_payment_method_data.financial_account` | string |  |  |
| `destination_payment_method_data.metadata` | map (key → value) |  |  |
| `destination_payment_method_data.type` | enum: `financial_account`, `us_bank_account` | yes |  |
| `destination_payment_method_data.us_bank_account` | object |  |  |
| `destination_payment_method_data.us_bank_account.account_holder_type` | enum: `company`, `individual` |  |  |
| `destination_payment_method_data.us_bank_account.account_number` | string |  |  |
| `destination_payment_method_data.us_bank_account.account_type` | enum: `checking`, `savings` |  |  |
| `destination_payment_method_data.us_bank_account.financial_connections_account` | string |  |  |
| `destination_payment_method_data.us_bank_account.routing_number` | string |  |  |
| `destination_payment_method_options` | object |  | Payment method-specific configuration for this OutboundPayment. |
| `destination_payment_method_options.us_bank_account` | object or "" (to unset) |  |  |
| `destination_payment_method_options.us_bank_account.network` | enum: `ach`, `us_domestic_wire` |  |  |
| `end_user_details` | object |  | End user details. |
| `end_user_details.ip_address` | string |  |  |
| `end_user_details.present` | boolean | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `financial_account` | string | yes | The FinancialAccount to pull funds from. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `statement_descriptor` | string |  | The description that appears on the receiving end for this OutboundPayment (for example, bank statement for external bank transfer). Maximum 10 characters for `ach` payments, 140 characters for `us_domestic_wire` payments, or 500 characters for `stripe` network transfers. The default value is "payment". |

Returns: `treasury.outbound_payment`

## GET /v1/treasury/outbound_payments/{id}

operationId: `GetTreasuryOutboundPaymentsId`

Retrieves the details of an existing OutboundPayment by passing the unique OutboundPayment ID from either the OutboundPayment creation request or OutboundPayment list.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `id (path)` | string | yes |  |

Returns: `treasury.outbound_payment`

## POST /v1/treasury/outbound_payments/{id}/cancel

operationId: `PostTreasuryOutboundPaymentsIdCancel`

Cancel an OutboundPayment.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `treasury.outbound_payment`

## GET /v1/treasury/outbound_transfers

operationId: `GetTreasuryOutboundTransfers`

Returns a list of OutboundTransfers sent from the specified FinancialAccount.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `financial_account` | string | yes | Returns objects associated with this FinancialAccount. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `status` | enum: `canceled`, `failed`, `posted`, `processing`, `returned` |  | Only return OutboundTransfers that have the given status: `processing`, `canceled`, `failed`, `posted`, or `returned`. |

Returns: object

## POST /v1/treasury/outbound_transfers

operationId: `PostTreasuryOutboundTransfers`

Creates an OutboundTransfer.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | Amount (in cents) to be transferred. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. |
| `destination_payment_method` | string |  | The PaymentMethod to use as the payment instrument for the OutboundTransfer. |
| `destination_payment_method_options` | object |  | Hash describing payment method configuration details. |
| `destination_payment_method_options.us_bank_account` | object or "" (to unset) |  |  |
| `destination_payment_method_options.us_bank_account.network` | enum: `ach`, `us_domestic_wire` |  |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `financial_account` | string | yes | The FinancialAccount to pull funds from. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `statement_descriptor` | string |  | Statement descriptor to be shown on the receiving end of an OutboundTransfer. Maximum 10 characters for `ach` transfers or 140 characters for `us_domestic_wire` transfers. The default value is "transfer". |

Returns: `treasury.outbound_transfer`

## GET /v1/treasury/outbound_transfers/{outbound_transfer}

operationId: `GetTreasuryOutboundTransfersOutboundTransfer`

Retrieves the details of an existing OutboundTransfer by passing the unique OutboundTransfer ID from either the OutboundTransfer creation request or OutboundTransfer list.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `outbound_transfer (path)` | string | yes |  |

Returns: `treasury.outbound_transfer`

## POST /v1/treasury/outbound_transfers/{outbound_transfer}/cancel

operationId: `PostTreasuryOutboundTransfersOutboundTransferCancel`

An OutboundTransfer can be canceled if the funds have not yet been paid out.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `outbound_transfer (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `treasury.outbound_transfer`

## GET /v1/treasury/received_credits

operationId: `GetTreasuryReceivedCredits`

Returns a list of ReceivedCredits.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `financial_account` | string | yes | The FinancialAccount that received the funds. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `linked_flows` | object |  | Only return ReceivedCredits described by the flow. |
| `linked_flows.source_flow_type` | enum: `credit_reversal`, `other`, `outbound_payment`, `payout` | yes |  |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `status` | enum: `failed`, `succeeded` |  | Only return ReceivedCredits that have the given status: `succeeded` or `failed`. |

Returns: object

## GET /v1/treasury/received_credits/{id}

operationId: `GetTreasuryReceivedCreditsId`

Retrieves the details of an existing ReceivedCredit by passing the unique ReceivedCredit ID from the ReceivedCredit list.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `id (path)` | string | yes |  |

Returns: `treasury.received_credit`

## GET /v1/treasury/received_debits

operationId: `GetTreasuryReceivedDebits`

Returns a list of ReceivedDebits.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `financial_account` | string | yes | The FinancialAccount that funds were pulled from. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `status` | enum: `failed`, `succeeded` |  | Only return ReceivedDebits that have the given status: `succeeded` or `failed`. |

Returns: object

## GET /v1/treasury/received_debits/{id}

operationId: `GetTreasuryReceivedDebitsId`

Retrieves the details of an existing ReceivedDebit by passing the unique ReceivedDebit ID from the ReceivedDebit list

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `id (path)` | string | yes |  |

Returns: `treasury.received_debit`

## GET /v1/treasury/transaction_entries

operationId: `GetTreasuryTransactionEntries`

Retrieves a list of TransactionEntry objects.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | object or integer |  | Only return TransactionEntries that were created during the given date interval. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `effective_at` | object or integer |  |  |
| `effective_at.gt` | integer |  |  |
| `effective_at.gte` | integer |  |  |
| `effective_at.lt` | integer |  |  |
| `effective_at.lte` | integer |  |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `financial_account` | string | yes | Returns objects associated with this FinancialAccount. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `order_by` | enum: `created`, `effective_at` |  | The results are in reverse chronological order by `created` or `effective_at`. The default is `created`. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `transaction` | string |  | Only return TransactionEntries associated with this Transaction. |

Returns: object

## GET /v1/treasury/transaction_entries/{id}

operationId: `GetTreasuryTransactionEntriesId`

Retrieves a TransactionEntry object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `id (path)` | string | yes |  |

Returns: `treasury.transaction_entry`

## GET /v1/treasury/transactions

operationId: `GetTreasuryTransactions`

Retrieves a list of Transaction objects.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | object or integer |  | Only return Transactions that were created during the given date interval. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `financial_account` | string | yes | Returns objects associated with this FinancialAccount. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `order_by` | enum: `created`, `posted_at` |  | The results are in reverse chronological order by `created` or `posted_at`. The default is `created`. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `status` | enum: `open`, `posted`, `void` |  | Only return Transactions that have the given status: `open`, `posted`, or `void`. |
| `status_transitions` | object |  | A filter for the `status_transitions.posted_at` timestamp. When using this filter, `status=posted` and `order_by=posted_at` must also be specified. |
| `status_transitions.posted_at` | object or integer |  |  |
| `status_transitions.posted_at.gt` | integer |  |  |
| `status_transitions.posted_at.gte` | integer |  |  |
| `status_transitions.posted_at.lt` | integer |  |  |
| `status_transitions.posted_at.lte` | integer |  |  |

Returns: object

## GET /v1/treasury/transactions/{id}

operationId: `GetTreasuryTransactionsId`

Retrieves the details of an existing Transaction.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `id (path)` | string | yes |  |

Returns: `treasury.transaction`

# Objects returned

## The `treasury.credit_reversal` object

You can reverse some [ReceivedCredits](https://stripe.com/docs/api#received_credits) depending on their network and source flow. Reversing a ReceivedCredit leads to the creation of a new object known as a CreditReversal.

Expandable fields (pass `expand[]=<field>`): `status_transitions`, `transaction`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | Amount (in cents) transferred. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `financial_account` | string | yes | The FinancialAccount to reverse funds from. |
| `hosted_regulatory_receipt_url` | string |  | A [hosted transaction receipt](https://stripe.com/docs/treasury/moving-money/regulatory-receipts) URL that is provided when money movement is considered regulated under Stripe's money transmission licenses. |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) | yes | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `network` | enum: `ach`, `stripe` | yes | The rails used to reverse the funds. |
| `object` | enum: `treasury.credit_reversal` | yes | String representing the object's type. Objects of the same type share the same value. |
| `received_credit` | string | yes | The ReceivedCredit being reversed. |
| `status` | enum: `canceled`, `posted`, `processing` | yes | Status of the CreditReversal |
| `status_transitions` | `treasury_received_credits_resource_status_transitions` | yes |  |
| `transaction` | string or `treasury.transaction` |  | The Transaction associated with this object. |

## The `treasury.debit_reversal` object

You can reverse some [ReceivedDebits](https://stripe.com/docs/api#received_debits) depending on their network and source flow. Reversing a ReceivedDebit leads to the creation of a new object known as a DebitReversal.

Expandable fields (pass `expand[]=<field>`): `linked_flows`, `status_transitions`, `transaction`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | Amount (in cents) transferred. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `financial_account` | string |  | The FinancialAccount to reverse funds from. |
| `hosted_regulatory_receipt_url` | string |  | A [hosted transaction receipt](https://stripe.com/docs/treasury/moving-money/regulatory-receipts) URL that is provided when money movement is considered regulated under Stripe's money transmission licenses. |
| `id` | string | yes | Unique identifier for the object. |
| `linked_flows` | `treasury_received_debits_resource_debit_reversal_linked_flows` |  | Other flows linked to a DebitReversal. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) | yes | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `network` | enum: `ach`, `card` | yes | The rails used to reverse the funds. |
| `object` | enum: `treasury.debit_reversal` | yes | String representing the object's type. Objects of the same type share the same value. |
| `received_debit` | string | yes | The ReceivedDebit being reversed. |
| `status` | enum: `failed`, `processing`, `succeeded` | yes | Status of the DebitReversal |
| `status_transitions` | `treasury_received_debits_resource_status_transitions` | yes |  |
| `transaction` | string or `treasury.transaction` |  | The Transaction associated with this object. |

## The `treasury.financial_account` object

Stripe Treasury provides users with a container for money called a FinancialAccount that is separate from their Payments balance.
FinancialAccounts serve as the source and destination of Treasury’s money movement APIs.

Expandable fields (pass `expand[]=<field>`): `balance`, `features`, `financial_addresses`, `platform_restrictions`, `status_details`

| Field | Type | Required | Description |
|---|---|---|---|
| `active_features` | array of enum: `card_issuing`, `deposit_insurance`, `financial_addresses.aba`, `inbound_transfers.ach`, `intra_stripe_flows`, `outbound_payments.ach`, `outbound_payments.us_domestic_wire`, `outbound_transfers.ach`, `outbound_transfers.us_domestic_wire`, `remote_deposit_capture` |  | The array of paths to active Features in the Features hash. |
| `balance` | `treasury_financial_accounts_resource_balance` | yes |  |
| `country` | string | yes | Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)). |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `features` | `treasury.financial_account_features` |  |  |
| `financial_addresses` | array of `treasury_financial_accounts_resource_financial_address` | yes | The set of credentials that resolve to a FinancialAccount. |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `object` | enum: `treasury.financial_account` | yes | String representing the object's type. Objects of the same type share the same value. |
| `pending_features` | array of enum: `card_issuing`, `deposit_insurance`, `financial_addresses.aba`, `inbound_transfers.ach`, `intra_stripe_flows`, `outbound_payments.ach`, `outbound_payments.us_domestic_wire`, `outbound_transfers.ach`, `outbound_transfers.us_domestic_wire`, `remote_deposit_capture` |  | The array of paths to pending Features in the Features hash. |
| `platform_restrictions` | `treasury_financial_accounts_resource_platform_restrictions` |  | The set of functionalities that the platform can restrict on the FinancialAccount. |
| `restricted_features` | array of enum: `card_issuing`, `deposit_insurance`, `financial_addresses.aba`, `inbound_transfers.ach`, `intra_stripe_flows`, `outbound_payments.ach`, `outbound_payments.us_domestic_wire`, `outbound_transfers.ach`, `outbound_transfers.us_domestic_wire`, `remote_deposit_capture` |  | The array of paths to restricted Features in the Features hash. |
| `status` | enum: `closed`, `open` | yes | The enum specifying what state the account is in. |
| `status_details` | `treasury_financial_accounts_resource_status_details` | yes |  |
| `supported_currencies` | array of string | yes | The currencies the FinancialAccount can hold a balance in. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. |

## The `treasury.financial_account_features` object

Encodes whether a FinancialAccount has access to a particular Feature, with a `status` enum and associated `status_details`.
Stripe or the platform can control Features via the requested field.

Expandable fields (pass `expand[]=<field>`): `card_issuing`, `deposit_insurance`, `financial_addresses`, `inbound_transfers`, `intra_stripe_flows`, `outbound_payments`, `outbound_transfers`

| Field | Type | Required | Description |
|---|---|---|---|
| `card_issuing` | `treasury_financial_accounts_resource_toggle_settings` |  |  |
| `deposit_insurance` | `treasury_financial_accounts_resource_toggle_settings` |  |  |
| `financial_addresses` | `treasury_financial_accounts_resource_financial_addresses_features` |  |  |
| `inbound_transfers` | `treasury_financial_accounts_resource_inbound_transfers` |  |  |
| `intra_stripe_flows` | `treasury_financial_accounts_resource_toggle_settings` |  |  |
| `object` | enum: `treasury.financial_account_features` | yes | String representing the object's type. Objects of the same type share the same value. |
| `outbound_payments` | `treasury_financial_accounts_resource_outbound_payments` |  |  |
| `outbound_transfers` | `treasury_financial_accounts_resource_outbound_transfers` |  |  |

## The `treasury.inbound_transfer` object

Use [InboundTransfers](https://stripe.com/docs/treasury/moving-money/financial-accounts/into/inbound-transfers) to add funds to your [FinancialAccount](https://stripe.com/docs/api#financial_accounts) via a PaymentMethod that is owned by you. The funds will be transferred via an ACH debit.

Expandable fields (pass `expand[]=<field>`): `failure_details`, `linked_flows`, `origin_payment_method_details`, `status_transitions`, `transaction`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | Amount (in cents) transferred. |
| `cancelable` | boolean | yes | Returns `true` if the InboundTransfer is able to be canceled. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. |
| `failure_details` | `treasury_inbound_transfers_resource_failure_details` |  | Details about this InboundTransfer's failure. Only set when status is `failed`. |
| `financial_account` | string | yes | The FinancialAccount that received the funds. |
| `hosted_regulatory_receipt_url` | string |  | A [hosted transaction receipt](https://stripe.com/docs/treasury/moving-money/regulatory-receipts) URL that is provided when money movement is considered regulated under Stripe's money transmission licenses. |
| `id` | string | yes | Unique identifier for the object. |
| `linked_flows` | `treasury_inbound_transfers_resource_inbound_transfer_resource_linked_flows` | yes |  |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) | yes | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `object` | enum: `treasury.inbound_transfer` | yes | String representing the object's type. Objects of the same type share the same value. |
| `origin_payment_method` | string | yes | The origin payment method to be debited for an InboundTransfer. |
| `origin_payment_method_details` | `inbound_transfers` |  | Details about the PaymentMethod for an InboundTransfer. |
| `returned` | boolean |  | Returns `true` if the funds for an InboundTransfer were returned after the InboundTransfer went to the `succeeded` state. |
| `statement_descriptor` | string | yes | Statement descriptor shown when funds are debited from the source. Not all payment networks support `statement_descriptor`. |
| `status` | enum: `canceled`, `failed`, `processing`, `succeeded` | yes | Status of the InboundTransfer: `processing`, `succeeded`, `failed`, and `canceled`. An InboundTransfer is `processing` if it is created and pending. The status changes to `succeeded` once the funds have been "confirmed" and a `transaction` is created and posted. The status changes to `failed` if the transfer fails. |
| `status_transitions` | `treasury_inbound_transfers_resource_inbound_transfer_resource_status_transitions` | yes |  |
| `transaction` | string or `treasury.transaction` |  | The Transaction associated with this object. |

## The `treasury.outbound_payment` object

Use OutboundPayments to send funds to another party's external bank account or [FinancialAccount](https://stripe.com/docs/api#financial_accounts). To send money to an account belonging to the same user, use an [OutboundTransfer](https://stripe.com/docs/api#outbound_transfers).

Simulate OutboundPayment state changes with the `/v1/test_helpers/treasury/outbound_payments` endpoints. These methods can only be called on test mode objects.

Expandable fields (pass `expand[]=<field>`): `destination_payment_method_details`, `end_user_details`, `returned_details`, `status_transitions`, `transaction`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | Amount (in cents) transferred. |
| `cancelable` | boolean | yes | Returns `true` if the object can be canceled, and `false` otherwise. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `customer` | string |  | ID of the [customer](https://stripe.com/docs/api/customers) to whom an OutboundPayment is sent. |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. |
| `destination_payment_method` | string |  | The PaymentMethod via which an OutboundPayment is sent. This field can be empty if the OutboundPayment was created using `destination_payment_method_data`. |
| `destination_payment_method_details` | `outbound_payments_payment_method_details` |  | Details about the PaymentMethod for an OutboundPayment. |
| `end_user_details` | `treasury_outbound_payments_resource_outbound_payment_resource_end_user_details` |  | Details about the end user. |
| `expected_arrival_date` | timestamp (Unix seconds) | yes | The date when funds are expected to arrive in the destination account. |
| `financial_account` | string | yes | The FinancialAccount that funds were pulled from. |
| `hosted_regulatory_receipt_url` | string |  | A [hosted transaction receipt](https://stripe.com/docs/treasury/moving-money/regulatory-receipts) URL that is provided when money movement is considered regulated under Stripe's money transmission licenses. |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) | yes | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `object` | enum: `treasury.outbound_payment` | yes | String representing the object's type. Objects of the same type share the same value. |
| `returned_details` | `treasury_outbound_payments_resource_returned_status` |  | Details about a returned OutboundPayment. Only set when the status is `returned`. |
| `statement_descriptor` | string | yes | The description that appears on the receiving end for an OutboundPayment (for example, bank statement for external bank transfer). |
| `status` | enum: `canceled`, `failed`, `posted`, `processing`, `returned` | yes | Current status of the OutboundPayment: `processing`, `failed`, `posted`, `returned`, `canceled`. An OutboundPayment is `processing` if it has been created and is pending. The status changes to `posted` once the OutboundPayment has been "confirmed" and funds have left the account, or to `failed` or `canceled`. If an OutboundPayment fails to arrive at its destination, its status will change to `returned`. |
| `status_transitions` | `treasury_outbound_payments_resource_outbound_payment_resource_status_transitions` | yes |  |
| `transaction` | string or `treasury.transaction` | yes | The Transaction associated with this object. |

## The `treasury.outbound_transfer` object

Use OutboundTransfers to transfer funds from a [FinancialAccount](https://stripe.com/docs/api#financial_accounts) to a PaymentMethod belonging to the same entity. To send funds to a different party, use [OutboundPayments](https://stripe.com/docs/api#outbound_payments) instead. You can send funds over ACH rails or through a domestic wire transfer to a user's own external bank account.

Simulate OutboundTransfer state changes with the `/v1/test_helpers/treasury/outbound_transfers` endpoints. These methods can only be called on test mode objects.

Expandable fields (pass `expand[]=<field>`): `destination_payment_method_details`, `returned_details`, `status_transitions`, `transaction`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | Amount (in cents) transferred. |
| `cancelable` | boolean | yes | Returns `true` if the object can be canceled, and `false` otherwise. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. |
| `destination_payment_method` | string |  | The PaymentMethod used as the payment instrument for an OutboundTransfer. |
| `destination_payment_method_details` | `outbound_transfers_payment_method_details` | yes |  |
| `expected_arrival_date` | timestamp (Unix seconds) | yes | The date when funds are expected to arrive in the destination account. |
| `financial_account` | string | yes | The FinancialAccount that funds were pulled from. |
| `hosted_regulatory_receipt_url` | string |  | A [hosted transaction receipt](https://stripe.com/docs/treasury/moving-money/regulatory-receipts) URL that is provided when money movement is considered regulated under Stripe's money transmission licenses. |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) | yes | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `object` | enum: `treasury.outbound_transfer` | yes | String representing the object's type. Objects of the same type share the same value. |
| `returned_details` | `treasury_outbound_transfers_resource_returned_details` |  | Details about a returned OutboundTransfer. Only set when the status is `returned`. |
| `statement_descriptor` | string | yes | Information about the OutboundTransfer to be sent to the recipient account. |
| `status` | enum: `canceled`, `failed`, `posted`, `processing`, `returned` | yes | Current status of the OutboundTransfer: `processing`, `failed`, `canceled`, `posted`, `returned`. An OutboundTransfer is `processing` if it has been created and is pending. The status changes to `posted` once the OutboundTransfer has been "confirmed" and funds have left the account, or to `failed` or `canceled`. If an OutboundTransfer fails to arrive at its destination, its status will change to `returned`. |
| `status_transitions` | `treasury_outbound_transfers_resource_status_transitions` | yes |  |
| `transaction` | string or `treasury.transaction` | yes | The Transaction associated with this object. |

## The `treasury.received_credit` object

ReceivedCredits represent funds sent to a [FinancialAccount](https://stripe.com/docs/api#financial_accounts) (for example, via ACH or wire). These money movements are not initiated from the FinancialAccount.

Expandable fields (pass `expand[]=<field>`): `initiating_payment_method_details`, `linked_flows`, `reversal_details`, `transaction`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | Amount (in cents) transferred. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `description` | string | yes | An arbitrary string attached to the object. Often useful for displaying to users. |
| `failure_code` | enum: `account_closed`, `account_frozen`, `other` |  | Reason for the failure. A ReceivedCredit might fail because the receiving FinancialAccount is closed or frozen. |
| `financial_account` | string |  | The FinancialAccount that received the funds. |
| `hosted_regulatory_receipt_url` | string |  | A [hosted transaction receipt](https://stripe.com/docs/treasury/moving-money/regulatory-receipts) URL that is provided when money movement is considered regulated under Stripe's money transmission licenses. |
| `id` | string | yes | Unique identifier for the object. |
| `initiating_payment_method_details` | `treasury_shared_resource_initiating_payment_method_details_initiating_payment_method_details` | yes |  |
| `linked_flows` | `treasury_received_credits_resource_linked_flows` | yes |  |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `network` | enum: `ach`, `card`, `stripe`, `us_domestic_wire` | yes | The rails used to send the funds. |
| `object` | enum: `treasury.received_credit` | yes | String representing the object's type. Objects of the same type share the same value. |
| `reversal_details` | `treasury_received_credits_resource_reversal_details` |  | Details describing when a ReceivedCredit may be reversed. |
| `status` | enum: `failed`, `succeeded` | yes | Status of the ReceivedCredit. ReceivedCredits are created either `succeeded` (approved) or `failed` (declined). If a ReceivedCredit is declined, the failure reason can be found in the `failure_code` field. |
| `transaction` | string or `treasury.transaction` |  | The Transaction associated with this object. |

## The `treasury.received_debit` object

ReceivedDebits represent funds pulled from a [FinancialAccount](https://stripe.com/docs/api#financial_accounts). These are not initiated from the FinancialAccount.

Expandable fields (pass `expand[]=<field>`): `initiating_payment_method_details`, `linked_flows`, `reversal_details`, `transaction`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | Amount (in cents) transferred. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `description` | string | yes | An arbitrary string attached to the object. Often useful for displaying to users. |
| `failure_code` | enum: `account_closed`, `account_frozen`, `insufficient_funds`, `other` |  | Reason for the failure. A ReceivedDebit might fail because the FinancialAccount doesn't have sufficient funds, is closed, or is frozen. |
| `financial_account` | string |  | The FinancialAccount that funds were pulled from. |
| `hosted_regulatory_receipt_url` | string |  | A [hosted transaction receipt](https://stripe.com/docs/treasury/moving-money/regulatory-receipts) URL that is provided when money movement is considered regulated under Stripe's money transmission licenses. |
| `id` | string | yes | Unique identifier for the object. |
| `initiating_payment_method_details` | `treasury_shared_resource_initiating_payment_method_details_initiating_payment_method_details` |  |  |
| `linked_flows` | `treasury_received_debits_resource_linked_flows` | yes |  |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `network` | enum: `ach`, `card`, `stripe` | yes | The network used for the ReceivedDebit. |
| `object` | enum: `treasury.received_debit` | yes | String representing the object's type. Objects of the same type share the same value. |
| `reversal_details` | `treasury_received_debits_resource_reversal_details` |  | Details describing when a ReceivedDebit might be reversed. |
| `status` | enum: `failed`, `succeeded` | yes | Status of the ReceivedDebit. ReceivedDebits are created with a status of either `succeeded` (approved) or `failed` (declined). The failure reason can be found under the `failure_code`. |
| `transaction` | string or `treasury.transaction` |  | The Transaction associated with this object. |

## The `treasury.transaction_entry` object

TransactionEntries represent individual units of money movements within a single [Transaction](https://stripe.com/docs/api#transactions).

Expandable fields (pass `expand[]=<field>`): `balance_impact`, `flow_details`, `transaction`

| Field | Type | Required | Description |
|---|---|---|---|
| `balance_impact` | `treasury_transactions_resource_balance_impact` | yes |  |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `effective_at` | timestamp (Unix seconds) | yes | When the TransactionEntry will impact the FinancialAccount's balance. |
| `financial_account` | string | yes | The FinancialAccount associated with this object. |
| `flow` | string |  | Token of the flow associated with the TransactionEntry. |
| `flow_details` | `treasury_transactions_resource_flow_details` |  | Details of the flow associated with the TransactionEntry. |
| `flow_type` | enum: `credit_reversal`, `debit_reversal`, `inbound_transfer`, `issuing_authorization`, `other`, `outbound_payment`, `outbound_transfer`, `received_credit`, `received_debit` | yes | Type of the flow associated with the TransactionEntry. |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `object` | enum: `treasury.transaction_entry` | yes | String representing the object's type. Objects of the same type share the same value. |
| `transaction` | string or `treasury.transaction` | yes | The Transaction associated with this object. |
| `type` | enum: `credit_reversal`, `credit_reversal_posting`, `debit_reversal`, `inbound_transfer`, `inbound_transfer_return`, `issuing_authorization_hold`, `issuing_authorization_release`, `other`, `outbound_payment`, `outbound_payment_cancellation`, `outbound_payment_failure`, `outbound_payment_posting`, `outbound_payment_return`, `outbound_transfer`, `outbound_transfer_cancellation`, `outbound_transfer_failure`, `outbound_transfer_posting`, `outbound_transfer_return`, `received_credit`, `received_debit` | yes | The specific money movement that generated the TransactionEntry. |

## The `treasury.transaction` object

Transactions represent changes to a [FinancialAccount's](https://stripe.com/docs/api#financial_accounts) balance.

Expandable fields (pass `expand[]=<field>`): `balance_impact`, `entries`, `flow_details`, `status_transitions`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | Amount (in cents) transferred. |
| `balance_impact` | `treasury_transactions_resource_balance_impact` | yes |  |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `description` | string | yes | An arbitrary string attached to the object. Often useful for displaying to users. |
| `entries` | object |  | A list of TransactionEntries that are part of this Transaction. This cannot be expanded in any list endpoints. |
| `financial_account` | string | yes | The FinancialAccount associated with this object. |
| `flow` | string |  | ID of the flow that created the Transaction. |
| `flow_details` | `treasury_transactions_resource_flow_details` |  | Details of the flow that created the Transaction. |
| `flow_type` | enum: `credit_reversal`, `debit_reversal`, `inbound_transfer`, `issuing_authorization`, `other`, `outbound_payment`, `outbound_transfer`, `received_credit`, `received_debit` | yes | Type of the flow that created the Transaction. |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `object` | enum: `treasury.transaction` | yes | String representing the object's type. Objects of the same type share the same value. |
| `status` | enum: `open`, `posted`, `void` | yes | Status of the Transaction. |
| `status_transitions` | `treasury_transactions_resource_abstract_transaction_resource_status_transitions` | yes |  |

