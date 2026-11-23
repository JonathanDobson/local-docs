# Stripe API 2023-10-16 — balance transactions

Operations under `/v1/balance_transactions` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/balance_transactions

operationId: `GetBalanceTransactions`

Returns a list of transactions that have contributed to the Stripe account balance (e.g., charges, transfers, and so forth). The transactions are returned in sorted order, with the most recent transactions appearing first.

Note that this endpoint was previously called “Balance history” and used the path `/v1/balance/history`.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | object or integer |  | Only return transactions that were created during the given date interval. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `currency` | string |  | Only return transactions in a certain currency. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `payout` | string |  | For automatic Stripe payouts only, only returns transactions that were paid out on the specified payout ID. |
| `source` | string |  | Only returns the original transaction. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `type` | string |  | Only returns transactions of the given type. One of: `adjustment`, `advance`, `advance_funding`, `anticipation_repayment`, `application_fee`, `application_fee_refund`, `charge`, `climate_order_purchase`, `climate_order_refund`, `connect_collection_transfer`, `contribution`, `issuing_authorization_hold`, `issuing_authorization_release`, `issuing_dispute`, `issuing_transaction`, `obligation_outbound`, `obligation_reversal_inbound`, `payment`, `payment_failure_refund`, `payment_network_reserve_hold`, `payment_network_reserve_release`, `payment_refund`, `payment_reversal`, `payment_unreconciled`, `payout`, `payout_cancel`, `payout_failure`, `refund`, `refund_failure`, `reserve_transaction`, `reserved_funds`, `stripe_fee`, `stripe_fx_fee`, `tax_fee`, `topup`, `topup_reversal`, `transfer`, `transfer_cancel`, `transfer_failure`, or `transfer_refund`. |

Returns: object

## GET /v1/balance_transactions/{id}

operationId: `GetBalanceTransactionsId`

Retrieves the balance transaction with the given ID.

Note that this endpoint previously used the path `/v1/balance/history/:id`.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `id (path)` | string | yes |  |

Returns: `balance_transaction`

# Objects returned

## The `balance_transaction` object

Balance transactions represent funds moving through your Stripe account.
Stripe creates them for every type of transaction that enters or leaves your Stripe account balance.

Related guide: [Balance transaction types](https://stripe.com/docs/reports/balance-transaction-types)

Expandable fields (pass `expand[]=<field>`): `fee_details`, `source`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | Gross amount of this transaction (in cents (or local equivalent)). A positive value represents funds charged to another party, and a negative value represents funds sent to another party. |
| `available_on` | timestamp (Unix seconds) | yes | The date that the transaction's net funds become available in the Stripe balance. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. |
| `exchange_rate` | number |  | If applicable, this transaction uses an exchange rate. If money converts from currency A to currency B, then the `amount` in currency A, multipled by the `exchange_rate`, equals the `amount` in currency B. For example, if you charge a customer 10.00 EUR, the PaymentIntent's `amount` is `1000` and `currency` is `eur`. If this converts to 12.34 USD in your Stripe account, the BalanceTransaction's `amount` is `1234`, its `currency` is `usd`, and the `exchange_rate` is `1.234`. |
| `fee` | integer | yes | Fees (in cents (or local equivalent)) paid for this transaction. Represented as a positive integer when assessed. |
| `fee_details` | array of `fee` | yes | Detailed breakdown of fees (in cents (or local equivalent)) paid for this transaction. |
| `id` | string | yes | Unique identifier for the object. |
| `net` | integer | yes | Net impact to a Stripe balance (in cents (or local equivalent)). A positive value represents incrementing a Stripe balance, and a negative value decrementing a Stripe balance. You can calculate the net impact of a transaction on a balance by `amount` - `fee` |
| `object` | enum: `balance_transaction` | yes | String representing the object's type. Objects of the same type share the same value. |
| `reporting_category` | string | yes | Learn more about how [reporting categories](https://stripe.com/docs/reports/reporting-categories) can help you understand balance transactions from an accounting perspective. |
| `source` | string or `application_fee` or `charge` or `connect_collection_transfer` or `customer_cash_balance_transaction` or `dispute` or `fee_refund` or `issuing.authorization` or `issuing.dispute` or `issuing.transaction` or `payout` or `platform_tax_fee` or `refund` or `reserve_transaction` or `tax_deducted_at_source` or `topup` or `transfer` or `transfer_reversal` |  | This transaction relates to the Stripe object. |
| `status` | string | yes | The transaction's net funds status in the Stripe balance, which are either `available` or `pending`. |
| `type` | enum: `adjustment`, `advance`, `advance_funding`, `anticipation_repayment`, `application_fee`, `application_fee_refund`, `charge`, `climate_order_purchase`, `climate_order_refund`, `connect_collection_transfer`, `contribution`, `issuing_authorization_hold`, `issuing_authorization_release`, `issuing_dispute`, `issuing_transaction`, `obligation_outbound`, `obligation_reversal_inbound`, `payment`, `payment_failure_refund`, `payment_network_reserve_hold`, `payment_network_reserve_release`, `payment_refund`, `payment_reversal`, `payment_unreconciled`, `payout`, `payout_cancel`, `payout_failure`, `refund`, `refund_failure`, `reserve_transaction`, `reserved_funds`, `stripe_fee`, `stripe_fx_fee`, `tax_fee`, `topup`, `topup_reversal`, `transfer`, `transfer_cancel`, `transfer_failure`, `transfer_refund` | yes | Transaction type: `adjustment`, `advance`, `advance_funding`, `anticipation_repayment`, `application_fee`, `application_fee_refund`, `charge`, `climate_order_purchase`, `climate_order_refund`, `connect_collection_transfer`, `contribution`, `issuing_authorization_hold`, `issuing_authorization_release`, `issuing_dispute`, `issuing_transaction`, `obligation_outbound`, `obligation_reversal_inbound`, `payment`, `payment_failure_refund`, `payment_network_reserve_hold`, `payment_network_reserve_release`, `payment_refund`, `payment_reversal`, `payment_unreconciled`, `payout`, `payout_cancel`, `payout_failure`, `refund`, `refund_failure`, `reserve_transaction`, `reserved_funds`, `stripe_fee`, `stripe_fx_fee`, `tax_fee`, `topup`, `topup_reversal`, `transfer`, `transfer_cancel`, `transfer_failure`, or `transfer_refund`. Learn more about [balance transaction types and what they represent](https://stripe.com/docs/reports/balance-transaction-types). To classify transactions for accounting purposes, consider `reporting_category` instead. |

