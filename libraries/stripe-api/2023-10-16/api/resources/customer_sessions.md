# Stripe API 2023-10-16 — customer sessions

Operations under `/v1/customer_sessions` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## POST /v1/customer_sessions

operationId: `PostCustomerSessions`

Creates a customer session object that includes a single-use client secret that you can use on your front-end to grant client-side API access for certain customer resources.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `components` | object | yes | Configuration for each component. Exactly 1 component must be enabled. |
| `components.buy_button` | object |  |  |
| `components.buy_button.enabled` | boolean | yes |  |
| `components.pricing_table` | object |  |  |
| `components.pricing_table.enabled` | boolean | yes |  |
| `customer` | string | yes | The ID of an existing customer for which to create the customer session. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `customer_session`

# Objects returned

## The `customer_session` object

A customer session allows you to grant client access to Stripe's frontend SDKs (like StripeJs)
control over a customer.

Expandable fields (pass `expand[]=<field>`): `components`, `customer`

| Field | Type | Required | Description |
|---|---|---|---|
| `client_secret` | string | yes | The client secret of this customer session. Used on the client to set up secure access to the given `customer`.<br>The client secret can be used to provide access to `customer` from your frontend. It should not be stored, logged, or exposed to anyone other than the relevant customer. Make sure that you have TLS enabled on any page that includes the client secret. |
| `components` | `customer_session_resource_components` |  |  |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `customer` | string or `customer` | yes | The customer the customer session was created for. |
| `expires_at` | timestamp (Unix seconds) | yes | The timestamp at which this customer session will expire. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `object` | enum: `customer_session` | yes | String representing the object's type. Objects of the same type share the same value. |

