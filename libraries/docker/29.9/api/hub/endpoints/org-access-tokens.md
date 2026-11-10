# Docker HUB API 2-beta — org-access-tokens

## GET /v2/orgs/{org_name}/access-tokens

operationId: `getV2OrgsByNameAccessTokens`

List access tokens

List access tokens for an organization.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org_name` | path | string | yes | Name of the organization (namespace). |
| `page` | query | integer |  | Page number (starts on 1). |
| `page_size` | query | integer |  | Number of items (rows) per page. |

| Response | Description | Body |
|---|---|---|
| 200 | OK | `getOrgAccessTokensResponse` |
| 401 | Unauthorized (`Unauthorized`) | `error` |
| 403 | Forbidden (`Forbidden`) | `error` |
| 404 | Not Found (`NotFound`) | `error` |

## POST /v2/orgs/{org_name}/access-tokens

operationId: `postV2OrgsByNameAccessTokens`

Create access token

Create an access token for an organization.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org_name` | path | string | yes | Name of the organization (namespace). |

Request body (application/json): `createOrgAccessTokenRequest`

| Response | Description | Body |
|---|---|---|
| 201 | Created | `createOrgAccessTokenResponse` |
| 400 | Bad Request (`BadRequest`) | `error` |
| 401 | Unauthorized (`Unauthorized`) | `error` |
| 403 | Forbidden (`Forbidden`) | `error` |
| 404 | Not Found (`NotFound`) | `error` |

## GET /v2/orgs/{org_name}/access-tokens/{access_token_id}

operationId: `getV2OrgsByOrgNameAccessTokensByAccessTokenId`

Get access token

Get details of a specific access token for an organization.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org_name` | path | string | yes | Name of the organization (namespace). |
| `access_token_id` | path | string | yes | The ID of the access token to retrieve |

| Response | Description | Body |
|---|---|---|
| 200 | OK | `getOrgAccessTokenResponse` |
| 401 | Unauthorized (`Unauthorized`) | `error` |
| 403 | Forbidden (`Forbidden`) | `error` |
| 404 | Not Found (`NotFound`) | `error` |

## PATCH /v2/orgs/{org_name}/access-tokens/{access_token_id}

operationId: `patchV2OrgsByOrgNameAccessTokensByAccessTokenId`

Update access token

Update a specific access token for an organization.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org_name` | path | string | yes | Name of the organization (namespace). |
| `access_token_id` | path | string | yes | The ID of the access token to retrieve |

Request body (application/json): `updateOrgAccessTokenRequest`

| Response | Description | Body |
|---|---|---|
| 200 | OK | `updateOrgAccessTokenResponse` |
| 401 | Unauthorized (`Unauthorized`) | `error` |
| 403 | Forbidden (`Forbidden`) | `error` |
| 404 | Not Found (`NotFound`) | `error` |

## DELETE /v2/orgs/{org_name}/access-tokens/{access_token_id}

operationId: `deleteV2OrgsByOrgNameAccessTokensByAccessTokenId`

Delete access token

Delete a specific access token for an organization. This action cannot be undone.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org_name` | path | string | yes | Name of the organization (namespace). |
| `access_token_id` | path | string | yes | The ID of the access token to retrieve |

| Response | Description | Body |
|---|---|---|
| 204 | Access token deleted successfully |  |
| 401 | Unauthorized (`Unauthorized`) | `error` |
| 403 | Forbidden (`Forbidden`) | `error` |
| 404 | Not Found (`NotFound`) | `error` |
