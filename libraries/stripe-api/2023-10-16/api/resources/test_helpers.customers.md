# Stripe API 2023-10-16 — test helpers / customers

Operations under `/v1/test_helpers/customers` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## POST /v1/test_helpers/customers/{customer}/fund_cash_balance

operationId: `PostTestHelpersCustomersCustomerFundCashBalance`

Create an incoming testmode bank transfer

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer (path)` | string | yes |  |
| `amount` | integer | yes | Amount to be used for this test cash balance transaction. A positive integer representing how much to fund in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (e.g., 100 cents to fund $1.00 or 100 to fund ¥100, a zero-decimal currency). |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `reference` | string |  | A description of the test funding. This simulates free-text references supplied by customers when making bank transfers to their cash balance. You can use this to test how Stripe's [reconciliation algorithm](https://stripe.com/docs/payments/customer-balance/reconciliation) applies to different user inputs. |

Returns: `customer_cash_balance_transaction`

# Objects returned

## The `customer_cash_balance_transaction` object

Customers with certain payments enabled have a cash balance, representing funds that were paid
by the customer to a merchant, but have not yet been allocated to a payment. Cash Balance Transactions
represent when funds are moved into or out of this balance. This includes funding by the customer, allocation
to payments, and refunds to the customer.

Expandable fields (pass `expand[]=<field>`): `adjusted_for_overdraft`, `applied_to_payment`, `customer`, `funded`, `refunded_from_payment`, `transferred_to_balance`, `unapplied_from_payment`

| Field | Type | Required | Description |
|---|---|---|---|
| `adjusted_for_overdraft` | `customer_balance_resource_cash_balance_transaction_resource_adjusted_for_overdraft` |  |  |
| `applied_to_payment` | `customer_balance_resource_cash_balance_transaction_resource_applied_to_payment_transaction` |  |  |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `customer` | string or `customer` | yes | The customer whose available cash balance changed as a result of this transaction. |
| `ending_balance` | integer | yes | The total available cash balance for the specified currency after this transaction was applied. Represented in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). |
| `funded` | `customer_balance_resource_cash_balance_transaction_resource_funded_transaction` |  |  |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `net_amount` | integer | yes | The amount by which the cash balance changed, represented in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). A positive value represents funds being added to the cash balance, a negative value represents funds being removed from the cash balance. |
| `object` | enum: `customer_cash_balance_transaction` | yes | String representing the object's type. Objects of the same type share the same value. |
| `refunded_from_payment` | `customer_balance_resource_cash_balance_transaction_resource_refunded_from_payment_transaction` |  |  |
| `transferred_to_balance` | `customer_balance_resource_cash_balance_transaction_resource_transferred_to_balance` |  |  |
| `type` | enum: `adjusted_for_overdraft`, `applied_to_payment`, `funded`, `funding_reversed`, `refunded_from_payment`, `return_canceled`, `return_initiated`, `transferred_to_balance`, `unapplied_from_payment` | yes | The type of the cash balance transaction. New types may be added in future. See [Customer Balance](https://stripe.com/docs/payments/customer-balance#types) to learn more about these types. |
| `unapplied_from_payment` | `customer_balance_resource_cash_balance_transaction_resource_unapplied_from_payment_transaction` |  |  |

