# Stripe API 2023-10-16 — ephemeral keys

Operations under `/v1/ephemeral_keys` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## POST /v1/ephemeral_keys

operationId: `PostEphemeralKeys`

Creates a short-lived API key for a given resource.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer` | string |  | The ID of the Customer you'd like to modify using the resulting ephemeral key. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `issuing_card` | string |  | The ID of the Issuing Card you'd like to access using the resulting ephemeral key. |
| `nonce` | string |  | A single-use token, created by Stripe.js, used for creating ephemeral keys for Issuing Cards without exchanging sensitive information. |
| `verification_session` | string |  | The ID of the Identity VerificationSession you'd like to access using the resulting ephemeral key |

Returns: `ephemeral_key`

## DELETE /v1/ephemeral_keys/{key}

operationId: `DeleteEphemeralKeysKey`

Invalidates a short-lived API key for a given resource.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `key (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `ephemeral_key`

# Objects returned

## The `ephemeral_key` object

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `expires` | timestamp (Unix seconds) | yes | Time at which the key will expire. Measured in seconds since the Unix epoch. |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `object` | enum: `ephemeral_key` | yes | String representing the object's type. Objects of the same type share the same value. |
| `secret` | string |  | The key's secret. You can use this value to make authorized requests to the Stripe API. |

