# Stripe API 2023-10-16 — link account sessions

Operations under `/v1/link_account_sessions` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## POST /v1/link_account_sessions

operationId: `PostLinkAccountSessions`

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

## GET /v1/link_account_sessions/{session}

operationId: `GetLinkAccountSessionsSession`

Retrieves the details of a Financial Connections `Session`

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `session (path)` | string | yes |  |

Returns: `financial_connections.session`

# Objects returned

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

