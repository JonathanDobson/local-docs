# Stripe API 2023-10-16 — linked accounts

Operations under `/v1/linked_accounts` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/linked_accounts

operationId: `GetLinkedAccounts`

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

## GET /v1/linked_accounts/{account}

operationId: `GetLinkedAccountsAccount`

Retrieves the details of an Financial Connections `Account`.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `financial_connections.account`

## POST /v1/linked_accounts/{account}/disconnect

operationId: `PostLinkedAccountsAccountDisconnect`

Disables your access to a Financial Connections `Account`. You will no longer be able to access data associated with the account (e.g. balances, transactions).

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `financial_connections.account`

## GET /v1/linked_accounts/{account}/owners

operationId: `GetLinkedAccountsAccountOwners`

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

## POST /v1/linked_accounts/{account}/refresh

operationId: `PostLinkedAccountsAccountRefresh`

Refreshes the data associated with a Financial Connections `Account`.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `features` | array of enum: `balance`, `ownership`, `transactions` | yes | The list of account features that you would like to refresh. |

Returns: `financial_connections.account`

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

