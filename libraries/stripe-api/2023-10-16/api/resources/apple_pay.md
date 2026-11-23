# Stripe API 2023-10-16 — apple pay

Operations under `/v1/apple_pay` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/apple_pay/domains

operationId: `GetApplePayDomains`

List apple pay domains.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `domain_name` | string |  |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/apple_pay/domains

operationId: `PostApplePayDomains`

Create an apple pay domain.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `domain_name` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `apple_pay_domain`

## GET /v1/apple_pay/domains/{domain}

operationId: `GetApplePayDomainsDomain`

Retrieve an apple pay domain.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `domain (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `apple_pay_domain`

## DELETE /v1/apple_pay/domains/{domain}

operationId: `DeleteApplePayDomainsDomain`

Delete an apple pay domain.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `domain (path)` | string | yes |  |

Returns: `deleted_apple_pay_domain`

# Objects returned

## The `apple_pay_domain` object

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `domain_name` | string | yes |  |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `object` | enum: `apple_pay_domain` | yes | String representing the object's type. Objects of the same type share the same value. |

## The `deleted_apple_pay_domain` object

| Field | Type | Required | Description |
|---|---|---|---|
| `deleted` | enum: `True` | yes | Always true for a deleted object |
| `id` | string | yes | Unique identifier for the object. |
| `object` | enum: `apple_pay_domain` | yes | String representing the object's type. Objects of the same type share the same value. |

