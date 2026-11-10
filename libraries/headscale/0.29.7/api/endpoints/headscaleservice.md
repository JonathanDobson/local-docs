# headscale/v1/headscale.proto 0.29.7 — HeadscaleService

## GET /api/v1/apikey

operationId: `HeadscaleService_ListApiKeys`

| Response | Description | Body |
|---|---|---|
| 200 | A successful response. | `v1ListApiKeysResponse` |
| default | An unexpected error response. | `rpcStatus` |

## POST /api/v1/apikey

operationId: `HeadscaleService_CreateApiKey`

--- ApiKeys start ---

Request body: `v1CreateApiKeyRequest`

| Response | Description | Body |
|---|---|---|
| 200 | A successful response. | `v1CreateApiKeyResponse` |
| default | An unexpected error response. | `rpcStatus` |

## POST /api/v1/apikey/expire

operationId: `HeadscaleService_ExpireApiKey`

Request body: `v1ExpireApiKeyRequest`

| Response | Description | Body |
|---|---|---|
| 200 | A successful response. | `v1ExpireApiKeyResponse` |
| default | An unexpected error response. | `rpcStatus` |

## DELETE /api/v1/apikey/{prefix}

operationId: `HeadscaleService_DeleteApiKey`

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `prefix` | path | string | yes |  |
| `id` | query | string (uint64) |  |  |

| Response | Description | Body |
|---|---|---|
| 200 | A successful response. | `v1DeleteApiKeyResponse` |
| default | An unexpected error response. | `rpcStatus` |

## POST /api/v1/auth/approve

operationId: `HeadscaleService_AuthApprove`

Request body: `v1AuthApproveRequest`

| Response | Description | Body |
|---|---|---|
| 200 | A successful response. | `v1AuthApproveResponse` |
| default | An unexpected error response. | `rpcStatus` |

## POST /api/v1/auth/register

operationId: `HeadscaleService_AuthRegister`

--- Auth start ---

Request body: `v1AuthRegisterRequest`

| Response | Description | Body |
|---|---|---|
| 200 | A successful response. | `v1AuthRegisterResponse` |
| default | An unexpected error response. | `rpcStatus` |

## POST /api/v1/auth/reject

operationId: `HeadscaleService_AuthReject`

Request body: `v1AuthRejectRequest`

| Response | Description | Body |
|---|---|---|
| 200 | A successful response. | `v1AuthRejectResponse` |
| default | An unexpected error response. | `rpcStatus` |

## POST /api/v1/debug/node

operationId: `HeadscaleService_DebugCreateNode`

--- Node start ---

Request body: `v1DebugCreateNodeRequest`

| Response | Description | Body |
|---|---|---|
| 200 | A successful response. | `v1DebugCreateNodeResponse` |
| default | An unexpected error response. | `rpcStatus` |

## GET /api/v1/health

operationId: `HeadscaleService_Health`

--- Health start ---

| Response | Description | Body |
|---|---|---|
| 200 | A successful response. | `v1HealthResponse` |
| default | An unexpected error response. | `rpcStatus` |

## GET /api/v1/node

operationId: `HeadscaleService_ListNodes`

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `user` | query | string |  |  |

| Response | Description | Body |
|---|---|---|
| 200 | A successful response. | `v1ListNodesResponse` |
| default | An unexpected error response. | `rpcStatus` |

## POST /api/v1/node/backfillips

operationId: `HeadscaleService_BackfillNodeIPs`

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `confirmed` | query | boolean |  |  |

| Response | Description | Body |
|---|---|---|
| 200 | A successful response. | `v1BackfillNodeIPsResponse` |
| default | An unexpected error response. | `rpcStatus` |

## POST /api/v1/node/register

operationId: `HeadscaleService_RegisterNode`

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `user` | query | string |  |  |
| `key` | query | string |  |  |

| Response | Description | Body |
|---|---|---|
| 200 | A successful response. | `v1RegisterNodeResponse` |
| default | An unexpected error response. | `rpcStatus` |

## GET /api/v1/node/{nodeId}

operationId: `HeadscaleService_GetNode`

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `nodeId` | path | string (uint64) | yes |  |

| Response | Description | Body |
|---|---|---|
| 200 | A successful response. | `v1GetNodeResponse` |
| default | An unexpected error response. | `rpcStatus` |

## DELETE /api/v1/node/{nodeId}

operationId: `HeadscaleService_DeleteNode`

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `nodeId` | path | string (uint64) | yes |  |

| Response | Description | Body |
|---|---|---|
| 200 | A successful response. | `v1DeleteNodeResponse` |
| default | An unexpected error response. | `rpcStatus` |

## POST /api/v1/node/{nodeId}/approve_routes

operationId: `HeadscaleService_SetApprovedRoutes`

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `nodeId` | path | string (uint64) | yes |  |

Request body: `HeadscaleServiceSetApprovedRoutesBody`

| Response | Description | Body |
|---|---|---|
| 200 | A successful response. | `v1SetApprovedRoutesResponse` |
| default | An unexpected error response. | `rpcStatus` |

## POST /api/v1/node/{nodeId}/expire

operationId: `HeadscaleService_ExpireNode`

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `nodeId` | path | string (uint64) | yes |  |
| `expiry` | query | string (date-time) |  |  |
| `disableExpiry` | query | boolean |  | When true, sets expiry to null (node will never expire). |

| Response | Description | Body |
|---|---|---|
| 200 | A successful response. | `v1ExpireNodeResponse` |
| default | An unexpected error response. | `rpcStatus` |

## POST /api/v1/node/{nodeId}/rename/{newName}

operationId: `HeadscaleService_RenameNode`

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `nodeId` | path | string (uint64) | yes |  |
| `newName` | path | string | yes |  |

| Response | Description | Body |
|---|---|---|
| 200 | A successful response. | `v1RenameNodeResponse` |
| default | An unexpected error response. | `rpcStatus` |

## POST /api/v1/node/{nodeId}/tags

operationId: `HeadscaleService_SetTags`

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `nodeId` | path | string (uint64) | yes |  |

Request body: `HeadscaleServiceSetTagsBody`

| Response | Description | Body |
|---|---|---|
| 200 | A successful response. | `v1SetTagsResponse` |
| default | An unexpected error response. | `rpcStatus` |

## GET /api/v1/policy

operationId: `HeadscaleService_GetPolicy`

--- Policy start ---

| Response | Description | Body |
|---|---|---|
| 200 | A successful response. | `v1GetPolicyResponse` |
| default | An unexpected error response. | `rpcStatus` |

## PUT /api/v1/policy

operationId: `HeadscaleService_SetPolicy`

Request body: `v1SetPolicyRequest`

| Response | Description | Body |
|---|---|---|
| 200 | A successful response. | `v1SetPolicyResponse` |
| default | An unexpected error response. | `rpcStatus` |

## POST /api/v1/policy/check

operationId: `HeadscaleService_CheckPolicy`

Request body: `v1CheckPolicyRequest`

| Response | Description | Body |
|---|---|---|
| 200 | A successful response. | `v1CheckPolicyResponse` |
| default | An unexpected error response. | `rpcStatus` |

## GET /api/v1/preauthkey

operationId: `HeadscaleService_ListPreAuthKeys`

| Response | Description | Body |
|---|---|---|
| 200 | A successful response. | `v1ListPreAuthKeysResponse` |
| default | An unexpected error response. | `rpcStatus` |

## POST /api/v1/preauthkey

operationId: `HeadscaleService_CreatePreAuthKey`

--- PreAuthKeys start ---

Request body: `v1CreatePreAuthKeyRequest`

| Response | Description | Body |
|---|---|---|
| 200 | A successful response. | `v1CreatePreAuthKeyResponse` |
| default | An unexpected error response. | `rpcStatus` |

## DELETE /api/v1/preauthkey

operationId: `HeadscaleService_DeletePreAuthKey`

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | query | string (uint64) |  |  |

| Response | Description | Body |
|---|---|---|
| 200 | A successful response. | `v1DeletePreAuthKeyResponse` |
| default | An unexpected error response. | `rpcStatus` |

## POST /api/v1/preauthkey/expire

operationId: `HeadscaleService_ExpirePreAuthKey`

Request body: `v1ExpirePreAuthKeyRequest`

| Response | Description | Body |
|---|---|---|
| 200 | A successful response. | `v1ExpirePreAuthKeyResponse` |
| default | An unexpected error response. | `rpcStatus` |

## GET /api/v1/user

operationId: `HeadscaleService_ListUsers`

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | query | string (uint64) |  |  |
| `name` | query | string |  |  |
| `email` | query | string |  |  |

| Response | Description | Body |
|---|---|---|
| 200 | A successful response. | `v1ListUsersResponse` |
| default | An unexpected error response. | `rpcStatus` |

## POST /api/v1/user

operationId: `HeadscaleService_CreateUser`

--- User start ---

Request body: `v1CreateUserRequest`

| Response | Description | Body |
|---|---|---|
| 200 | A successful response. | `v1CreateUserResponse` |
| default | An unexpected error response. | `rpcStatus` |

## DELETE /api/v1/user/{id}

operationId: `HeadscaleService_DeleteUser`

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string (uint64) | yes |  |

| Response | Description | Body |
|---|---|---|
| 200 | A successful response. | `v1DeleteUserResponse` |
| default | An unexpected error response. | `rpcStatus` |

## POST /api/v1/user/{oldId}/rename/{newName}

operationId: `HeadscaleService_RenameUser`

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `oldId` | path | string (uint64) | yes |  |
| `newName` | path | string | yes |  |

| Response | Description | Body |
|---|---|---|
| 200 | A successful response. | `v1RenameUserResponse` |
| default | An unexpected error response. | `rpcStatus` |
