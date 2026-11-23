# Stripe API 2023-10-16 — financial connections

Operations under `/v1/financial_connections` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/financial_connections/accounts

operationId: `GetFinancialConnectionsAccounts`

Returns a list of Financial Connections `Account` objects.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account_holder` | object |  | If present, only return accounts that belong to the specified account holder. `account_holder[customer]` and `account_holder[account]` are mutually exclusive. |
| `account_holder.account` | string |  |  |
| `account_holder.customer` | string |  |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `session` | string |  | If present, only return accounts that were collected as part of the given session. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## GET /v1/financial_connections/accounts/{account}

operationId: `GetFinancialConnectionsAccountsAccount`

Retrieves the details of an Financial Connections `Account`.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `financial_connections.account`

## POST /v1/financial_connections/accounts/{account}/disconnect

operationId: `PostFinancialConnectionsAccountsAccountDisconnect`

Disables your access to a Financial Connections `Account`. You will no longer be able to access data associated with the account (e.g. balances, transactions).

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `financial_connections.account`

## GET /v1/financial_connections/accounts/{account}/owners

operationId: `GetFinancialConnectionsAccountsAccountOwners`

Lists all owners for a given `Account`

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account (path)` | string | yes |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `ownership` | string | yes | The ID of the ownership object to fetch owners from. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/financial_connections/accounts/{account}/refresh

operationId: `PostFinancialConnectionsAccountsAccountRefresh`

Refreshes the data associated with a Financial Connections `Account`.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `features` | array of enum: `balance`, `ownership`, `transactions` | yes | The list of account features that you would like to refresh. |

Returns: `financial_connections.account`

## POST /v1/financial_connections/accounts/{account}/subscribe

operationId: `PostFinancialConnectionsAccountsAccountSubscribe`

Subscribes to periodic refreshes of data associated with a Financial Connections `Account`.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `features` | array of enum: `transactions` | yes | The list of account features to which you would like to subscribe. |

Returns: `financial_connections.account`

## POST /v1/financial_connections/accounts/{account}/unsubscribe

operationId: `PostFinancialConnectionsAccountsAccountUnsubscribe`

Unsubscribes from periodic refreshes of data associated with a Financial Connections `Account`.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `features` | array of enum: `transactions` | yes | The list of account features from which you would like to unsubscribe. |

Returns: `financial_connections.account`

## POST /v1/financial_connections/sessions

operationId: `PostFinancialConnectionsSessions`

To launch the Financial Connections authorization flow, create a `Session`. The session’s `client_secret` can be used to launch the flow using Stripe.js.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account_holder` | object | yes | The account holder to link accounts for. |
| `account_holder.account` | string |  |  |
| `account_holder.customer` | string |  |  |
| `account_holder.type` | enum: `account`, `customer` | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `filters` | object |  | Filters to restrict the kinds of accounts to collect. |
| `filters.countries` | array of string | yes |  |
| `permissions` | array of enum: `balances`, `ownership`, `payment_method`, `transactions` | yes | List of data features that you would like to request access to.<br>Possible values are `balances`, `transactions`, `ownership`, and `payment_method`. |
| `prefetch` | array of enum: `balances`, `ownership`, `transactions` |  | List of data features that you would like to retrieve upon account creation. |
| `return_url` | string |  | For webview integrations only. Upon completing OAuth login in the native browser, the user will be redirected to this URL to return to your app. |

Returns: `financial_connections.session`

## GET /v1/financial_connections/sessions/{session}

operationId: `GetFinancialConnectionsSessionsSession`

Retrieves the details of a Financial Connections `Session`

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `session (path)` | string | yes |  |

Returns: `financial_connections.session`

## GET /v1/financial_connections/transactions

operationId: `GetFinancialConnectionsTransactions`

Returns a list of Financial Connections `Transaction` objects.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account` | string | yes | The ID of the Stripe account whose transactions will be retrieved. |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `transacted_at` | object or integer |  | A filter on the list based on the object `transacted_at` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with the following options: |
| `transacted_at.gt` | integer |  |  |
| `transacted_at.gte` | integer |  |  |
| `transacted_at.lt` | integer |  |  |
| `transacted_at.lte` | integer |  |  |
| `transaction_refresh` | object |  | A filter on the list based on the object `transaction_refresh` field. The value can be a dictionary with the following options: |
| `transaction_refresh.after` | string | yes |  |

Returns: object

## GET /v1/financial_connections/transactions/{transaction}

operationId: `GetFinancialConnectionsTransactionsTransaction`

Retrieves the details of a Financial Connections `Transaction`

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `transaction (path)` | string | yes |  |

Returns: `financial_connections.transaction`

# Objects returned

## The `financial_connections.account` object

A Financial Connections Account represents an account that exists outside of Stripe, to which you have been granted some degree of access.

Expandable fields (pass `expand[]=<field>`): `account_holder`, `balance`, `balance_refresh`, `ownership`, `ownership_refresh`, `transaction_refresh`

| Field | Type | Required | Description |
|---|---|---|---|
| `account_holder` | `bank_connections_resource_accountholder` |  | The account holder that this account belongs to. |
| `balance` | `bank_connections_resource_balance` |  | The most recent information about the account's balance. |
| `balance_refresh` | `bank_connections_resource_balance_refresh` |  | The state of the most recent attempt to refresh the account balance. |
| `category` | enum: `cash`, `credit`, `investment`, `other` | yes | The type of the account. Account category is further divided in `subcategory`. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `display_name` | string |  | A human-readable name that has been assigned to this account, either by the account holder or by the institution. |
| `id` | string | yes | Unique identifier for the object. |
| `institution_name` | string | yes | The name of the institution that holds this account. |
| `last4` | string |  | The last 4 digits of the account number. If present, this will be 4 numeric characters. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `object` | enum: `financial_connections.account` | yes | String representing the object's type. Objects of the same type share the same value. |
| `ownership` | string or `financial_connections.account_ownership` |  | The most recent information about the account's owners. |
| `ownership_refresh` | `bank_connections_resource_ownership_refresh` |  | The state of the most recent attempt to refresh the account owners. |
| `permissions` | array of enum: `balances`, `ownership`, `payment_method`, `transactions` |  | The list of permissions granted by this account. |
| `status` | enum: `active`, `disconnected`, `inactive` | yes | The status of the link to the account. |
| `subcategory` | enum: `checking`, `credit_card`, `line_of_credit`, `mortgage`, `other`, `savings` | yes | If `category` is `cash`, one of:<br> - `checking`  - `savings`  - `other`<br>If `category` is `credit`, one of:<br> - `mortgage`  - `line_of_credit`  - `credit_card`  - `other`<br>If `category` is `investment` or `other`, this will be `other`. |
| `subscriptions` | array of enum: `transactions` |  | The list of data refresh subscriptions requested on this account. |
| `supported_payment_method_types` | array of enum: `link`, `us_bank_account` | yes | The [PaymentMethod type](https://stripe.com/docs/api/payment_methods/object#payment_method_object-type)(s) that can be created from this account. |
| `transaction_refresh` | `bank_connections_resource_transaction_refresh` |  | The state of the most recent attempt to refresh the account transactions. |

## The `financial_connections.session` object

A Financial Connections Session is the secure way to programmatically launch the client-side Stripe.js modal that lets your users link their accounts.

Expandable fields (pass `expand[]=<field>`): `account_holder`, `accounts`, `filters`

| Field | Type | Required | Description |
|---|---|---|---|
| `account_holder` | `bank_connections_resource_accountholder` |  | The account holder for whom accounts are collected in this session. |
| `accounts` | object | yes | The accounts that were collected as part of this Session. |
| `client_secret` | string | yes | A value that will be passed to the client to launch the authentication flow. |
| `filters` | `bank_connections_resource_link_account_session_filters` |  |  |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `object` | enum: `financial_connections.session` | yes | String representing the object's type. Objects of the same type share the same value. |
| `permissions` | array of enum: `balances`, `ownership`, `payment_method`, `transactions` | yes | Permissions requested for accounts collected during this session. |
| `prefetch` | array of enum: `balances`, `ownership`, `transactions` |  | Data features requested to be retrieved upon account creation. |
| `return_url` | string |  | For webview integrations only. Upon completing OAuth login in the native browser, the user will be redirected to this URL to return to your app. |

## The `financial_connections.transaction` object

A Transaction represents a real transaction that affects a Financial Connections Account balance.

Expandable fields (pass `expand[]=<field>`): `status_transitions`

| Field | Type | Required | Description |
|---|---|---|---|
| `account` | string | yes | The ID of the Financial Connections Account this transaction belongs to. |
| `amount` | integer | yes | The amount of this transaction, in cents (or local equivalent). |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `description` | string | yes | The description of this transaction. |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `object` | enum: `financial_connections.transaction` | yes | String representing the object's type. Objects of the same type share the same value. |
| `status` | enum: `pending`, `posted`, `void` | yes | The status of the transaction. |
| `status_transitions` | `bank_connections_resource_transaction_resource_status_transitions` | yes |  |
| `transacted_at` | timestamp (Unix seconds) | yes | Time at which the transaction was transacted. Measured in seconds since the Unix epoch. |
| `transaction_refresh` | string | yes | The token of the transaction refresh that last updated or created this transaction. |
| `updated` | timestamp (Unix seconds) | yes | Time at which the object was last updated. Measured in seconds since the Unix epoch. |

