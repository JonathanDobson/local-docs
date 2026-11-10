# Docker HUB API 2-beta — access-tokens

## GET /v2/access-tokens

operationId: `getV2AccessTokens`

List personal access tokens

Returns a paginated list of personal access tokens.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer |  | Page number (starts on 1). |
| `page_size` | query | integer |  | Number of items (rows) per page. |

| Response | Description | Body |
|---|---|---|
| 200 | OK | `getAccessTokensResponse` |
| 400 | Bad Request (`BadRequest`) | `error` |
| 401 | Unauthorized (`Unauthorized`) | `error` |

## POST /v2/access-tokens

operationId: `postV2AccessTokens`

Create personal access token

Creates and returns a personal access token.

Request body (application/json): `createAccessTokenRequest`

| Response | Description | Body |
|---|---|---|
| 201 | Created | `createAccessTokensResponse` |
| 400 | Bad Request (`BadRequest`) | `error` |
| 401 | Unauthorized (`Unauthorized`) | `error` |

## GET /v2/access-tokens/{uuid}

operationId: `getV2AccessTokensByUuid`

Get personal access token

Returns a personal access token by UUID.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `uuid` | path | string | yes | UUID of the personal access token. |

| Response | Description | Body |
|---|---|---|
| 200 | OK | allOf(`accessToken`, object) |
| 401 | Unauthorized (`Unauthorized`) | `error` |
| 404 | Not Found (`NotFound`) | `error` |

## PATCH /v2/access-tokens/{uuid}

operationId: `patchV2AccessTokensByUuid`

Update personal access token

Updates a personal access token partially. You can either update the token's label or enable/disable it.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `uuid` | path | string | yes | UUID of the personal access token. |

Request body (application/json): `patchAccessTokenRequest`

| Response | Description | Body |
|---|---|---|
| 200 | OK | `patchAccessTokenResponse` |
| 400 | Bad Request (`BadRequest`) | `error` |
| 401 | Unauthorized (`Unauthorized`) | `error` |

## DELETE /v2/access-tokens/{uuid}

operationId: `deleteV2AccessTokensByUuid`

Delete personal access token

Deletes a personal access token permanently. This cannot be undone.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `uuid` | path | string | yes | UUID of the personal access token. |

| Response | Description | Body |
|---|---|---|
| 204 | A successful response. |  |
| 401 | Unauthorized (`Unauthorized`) | `error` |
| 404 | Not Found (`NotFound`) | `error` |
