# Stripe API 2023-10-16 — test helpers / treasury

Operations under `/v1/test_helpers/treasury` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## POST /v1/test_helpers/treasury/inbound_transfers/{id}/fail

operationId: `PostTestHelpersTreasuryInboundTransfersIdFail`

Transitions a test mode created InboundTransfer to the `failed` status. The InboundTransfer must already be in the `processing` state.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `failure_details` | object |  | Details about a failed InboundTransfer. |
| `failure_details.code` | enum: `account_closed`, `account_frozen`, `bank_account_restricted`, `bank_ownership_changed`, `debit_not_authorized`, `incorrect_account_holder_address`, `incorrect_account_holder_name`, `incorrect_account_holder_tax_id`, `insufficient_funds`, `invalid_account_number`, `invalid_currency`, `no_account`, `other` |  |  |

Returns: `treasury.inbound_transfer`

## POST /v1/test_helpers/treasury/inbound_transfers/{id}/return

operationId: `PostTestHelpersTreasuryInboundTransfersIdReturn`

Marks the test mode InboundTransfer object as returned and links the InboundTransfer to a ReceivedDebit. The InboundTransfer must already be in the `succeeded` state.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `treasury.inbound_transfer`

## POST /v1/test_helpers/treasury/inbound_transfers/{id}/succeed

operationId: `PostTestHelpersTreasuryInboundTransfersIdSucceed`

Transitions a test mode created InboundTransfer to the `succeeded` status. The InboundTransfer must already be in the `processing` state.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `treasury.inbound_transfer`

## POST /v1/test_helpers/treasury/outbound_payments/{id}/fail

operationId: `PostTestHelpersTreasuryOutboundPaymentsIdFail`

Transitions a test mode created OutboundPayment to the `failed` status. The OutboundPayment must already be in the `processing` state.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `treasury.outbound_payment`

## POST /v1/test_helpers/treasury/outbound_payments/{id}/post

operationId: `PostTestHelpersTreasuryOutboundPaymentsIdPost`

Transitions a test mode created OutboundPayment to the `posted` status. The OutboundPayment must already be in the `processing` state.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `treasury.outbound_payment`

## POST /v1/test_helpers/treasury/outbound_payments/{id}/return

operationId: `PostTestHelpersTreasuryOutboundPaymentsIdReturn`

Transitions a test mode created OutboundPayment to the `returned` status. The OutboundPayment must already be in the `processing` state.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `returned_details` | object |  | Optional hash to set the the return code. |
| `returned_details.code` | enum: `account_closed`, `account_frozen`, `bank_account_restricted`, `bank_ownership_changed`, `declined`, `incorrect_account_holder_name`, `invalid_account_number`, `invalid_currency`, `no_account`, `other` |  |  |

Returns: `treasury.outbound_payment`

## POST /v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/fail

operationId: `PostTestHelpersTreasuryOutboundTransfersOutboundTransferFail`

Transitions a test mode created OutboundTransfer to the `failed` status. The OutboundTransfer must already be in the `processing` state.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `outbound_transfer (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `treasury.outbound_transfer`

## POST /v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/post

operationId: `PostTestHelpersTreasuryOutboundTransfersOutboundTransferPost`

Transitions a test mode created OutboundTransfer to the `posted` status. The OutboundTransfer must already be in the `processing` state.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `outbound_transfer (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `treasury.outbound_transfer`

## POST /v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/return

operationId: `PostTestHelpersTreasuryOutboundTransfersOutboundTransferReturn`

Transitions a test mode created OutboundTransfer to the `returned` status. The OutboundTransfer must already be in the `processing` state.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `outbound_transfer (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `returned_details` | object |  | Details about a returned OutboundTransfer. |
| `returned_details.code` | enum: `account_closed`, `account_frozen`, `bank_account_restricted`, `bank_ownership_changed`, `declined`, `incorrect_account_holder_name`, `invalid_account_number`, `invalid_currency`, `no_account`, `other` |  |  |

Returns: `treasury.outbound_transfer`

## POST /v1/test_helpers/treasury/received_credits

operationId: `PostTestHelpersTreasuryReceivedCredits`

Use this endpoint to simulate a test mode ReceivedCredit initiated by a third party. In live mode, you can’t directly create ReceivedCredits initiated by third parties.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | Amount (in cents) to be transferred. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `financial_account` | string | yes | The FinancialAccount to send funds to. |
| `initiating_payment_method_details` | object |  | Initiating payment method details for the object. |
| `initiating_payment_method_details.type` | enum: `us_bank_account` | yes |  |
| `initiating_payment_method_details.us_bank_account` | object |  |  |
| `initiating_payment_method_details.us_bank_account.account_holder_name` | string |  |  |
| `initiating_payment_method_details.us_bank_account.account_number` | string |  |  |
| `initiating_payment_method_details.us_bank_account.routing_number` | string |  |  |
| `network` | enum: `ach`, `us_domestic_wire` | yes | Specifies the network rails to be used. If not set, will default to the PaymentMethod's preferred network. See the [docs](https://stripe.com/docs/treasury/money-movement/timelines) to learn more about money movement timelines for each network type. |

Returns: `treasury.received_credit`

## POST /v1/test_helpers/treasury/received_debits

operationId: `PostTestHelpersTreasuryReceivedDebits`

Use this endpoint to simulate a test mode ReceivedDebit initiated by a third party. In live mode, you can’t directly create ReceivedDebits initiated by third parties.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | Amount (in cents) to be transferred. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `financial_account` | string | yes | The FinancialAccount to pull funds from. |
| `initiating_payment_method_details` | object |  | Initiating payment method details for the object. |
| `initiating_payment_method_details.type` | enum: `us_bank_account` | yes |  |
| `initiating_payment_method_details.us_bank_account` | object |  |  |
| `initiating_payment_method_details.us_bank_account.account_holder_name` | string |  |  |
| `initiating_payment_method_details.us_bank_account.account_number` | string |  |  |
| `initiating_payment_method_details.us_bank_account.routing_number` | string |  |  |
| `network` | enum: `ach` | yes | Specifies the network rails to be used. If not set, will default to the PaymentMethod's preferred network. See the [docs](https://stripe.com/docs/treasury/money-movement/timelines) to learn more about money movement timelines for each network type. |

Returns: `treasury.received_debit`

# Objects returned

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

