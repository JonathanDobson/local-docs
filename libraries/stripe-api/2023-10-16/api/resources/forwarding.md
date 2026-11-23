# Stripe API 2023-10-16 — forwarding

Operations under `/v1/forwarding` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/forwarding/requests

operationId: `GetForwardingRequests`

Lists all ForwardingRequest objects.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | object |  | Similar to other List endpoints, filters results based on created timestamp. You can pass gt, gte, lt, and lte timestamp values. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `ending_before` | string |  | A pagination cursor to fetch the previous page of the list. The value must be a ForwardingRequest ID. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A pagination cursor to fetch the next page of the list. The value must be a ForwardingRequest ID. |

Returns: object

## POST /v1/forwarding/requests

operationId: `PostForwardingRequests`

Creates a ForwardingRequest object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `config` | string | yes | The Forwarding Config used when making the forwarded request. The config specifes the HTTP method, merchant credentials, connection settings, and supported destination URLs. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `payment_method` | string | yes | The PaymentMethod to insert into the forwarded request. Forwarding previously consumed PaymentMethods is allowed. |
| `replacements` | array of enum: `card_cvc`, `card_expiry`, `card_number`, `cardholder_name` | yes | The field kinds to be replaced in the forwarded request. |
| `request` | object |  | The request body and headers to be sent to the destination endpoint. |
| `request.body` | string |  |  |
| `request.headers` | array of object |  |  |
| `request.headers[].name` | string | yes |  |
| `request.headers[].value` | string | yes |  |
| `url` | string | yes | The destination URL for the forwarded request. Must be supported by the config. |

Returns: `forwarding.request`

## GET /v1/forwarding/requests/{id}

operationId: `GetForwardingRequestsId`

Retrieves a ForwardingRequest object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `id (path)` | string | yes |  |

Returns: `forwarding.request`

# Objects returned

## The `forwarding.request` object

Instructs Stripe to make a request on your behalf using the destination URL and HTTP method in the config.
A config is set up for each destination URL by Stripe at the time of onboarding. Stripe verifies requests with
your credentials in the config, and injects card details from the payment_method into the request.

Stripe redacts all sensitive fields and headers, including authentication credentials and card numbers,
before storing the request and response data in the forwarding Request object, which are subject to a
30-day retention period.

You can provide a Stripe idempotency key to make sure that requests with the same key result in only one
outbound request. The Stripe idempotency key provided should be unique and different from any idempotency
keys provided on the underlying third-party request.

Forwarding Requests are synchronous requests that return a response or time out according to
Stripe’s limits.

Related guide: [Forward card details to third-party API endpoints](https://docs.stripe.com/payments/forwarding).

Expandable fields (pass `expand[]=<field>`): `request_context`, `request_details`, `response_details`

| Field | Type | Required | Description |
|---|---|---|---|
| `config` | string | yes | The Forwarding Config used when making the forwarded request. The config specifes the HTTP method, merchant credentials, connection settings, and supported destination URLs. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `object` | enum: `forwarding.request` | yes | String representing the object's type. Objects of the same type share the same value. |
| `payment_method` | string | yes | The PaymentMethod to insert into the forwarded request. Forwarding previously consumed PaymentMethods is allowed. |
| `replacements` | array of enum: `card_cvc`, `card_expiry`, `card_number`, `cardholder_name` | yes | The field kinds to be replaced in the forwarded request. |
| `request_context` | `forwarded_request_context` |  | Context about the request from Stripe's servers to the destination endpoint. |
| `request_details` | `forwarded_request_details` |  | The request that was sent to the destination endpoint. We redact any sensitive fields. |
| `response_details` | `forwarded_response_details` |  | The response that the destination endpoint returned to us. We redact any sensitive fields. |
| `url` | string |  | The destination URL for the forwarded request. Must be supported by the config. |

