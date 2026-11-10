# headscale/v1/headscale.proto 0.29.7 — schemas

## HeadscaleServiceSetApprovedRoutesBody

| Field | Type | Required | Description |
|---|---|---|---|
| `routes` | array of string |  |  |

## HeadscaleServiceSetTagsBody

| Field | Type | Required | Description |
|---|---|---|---|
| `tags` | array of string |  |  |

## protobufAny

| Field | Type | Required | Description |
|---|---|---|---|
| `@type` | string |  |  |

## rpcStatus

| Field | Type | Required | Description |
|---|---|---|---|
| `code` | integer (int32) |  |  |
| `message` | string |  |  |
| `details` | array of `protobufAny` |  |  |

## v1ApiKey

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string (uint64) |  |  |
| `prefix` | string |  |  |
| `expiration` | string (date-time) |  |  |
| `createdAt` | string (date-time) |  |  |
| `lastSeen` | string (date-time) |  |  |

## v1AuthApproveRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `authId` | string |  |  |

## v1AuthApproveResponse

Type: object

## v1AuthRegisterRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `user` | string |  |  |
| `authId` | string |  |  |

## v1AuthRegisterResponse

| Field | Type | Required | Description |
|---|---|---|---|
| `node` | `v1Node` |  |  |

## v1AuthRejectRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `authId` | string |  |  |

## v1AuthRejectResponse

Type: object

## v1BackfillNodeIPsResponse

| Field | Type | Required | Description |
|---|---|---|---|
| `changes` | array of string |  |  |

## v1CheckPolicyRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `policy` | string |  |  |

## v1CheckPolicyResponse

Type: object

## v1CreateApiKeyRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `expiration` | string (date-time) |  |  |

## v1CreateApiKeyResponse

| Field | Type | Required | Description |
|---|---|---|---|
| `apiKey` | string |  |  |

## v1CreatePreAuthKeyRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `user` | string (uint64) |  |  |
| `reusable` | boolean |  |  |
| `ephemeral` | boolean |  |  |
| `expiration` | string (date-time) |  |  |
| `aclTags` | array of string |  |  |

## v1CreatePreAuthKeyResponse

| Field | Type | Required | Description |
|---|---|---|---|
| `preAuthKey` | `v1PreAuthKey` |  |  |

## v1CreateUserRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  |  |
| `displayName` | string |  |  |
| `email` | string |  |  |
| `pictureUrl` | string |  |  |

## v1CreateUserResponse

| Field | Type | Required | Description |
|---|---|---|---|
| `user` | `v1User` |  |  |

## v1DebugCreateNodeRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `user` | string |  |  |
| `key` | string |  |  |
| `name` | string |  |  |
| `routes` | array of string |  |  |

## v1DebugCreateNodeResponse

| Field | Type | Required | Description |
|---|---|---|---|
| `node` | `v1Node` |  |  |

## v1DeleteApiKeyResponse

Type: object

## v1DeleteNodeResponse

Type: object

## v1DeletePreAuthKeyResponse

Type: object

## v1DeleteUserResponse

Type: object

## v1ExpireApiKeyRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `prefix` | string |  |  |
| `id` | string (uint64) |  |  |

## v1ExpireApiKeyResponse

Type: object

## v1ExpireNodeResponse

| Field | Type | Required | Description |
|---|---|---|---|
| `node` | `v1Node` |  |  |

## v1ExpirePreAuthKeyRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string (uint64) |  |  |

## v1ExpirePreAuthKeyResponse

Type: object

## v1GetNodeResponse

| Field | Type | Required | Description |
|---|---|---|---|
| `node` | `v1Node` |  |  |

## v1GetPolicyResponse

| Field | Type | Required | Description |
|---|---|---|---|
| `policy` | string |  |  |
| `updatedAt` | string (date-time) |  |  |

## v1HealthResponse

| Field | Type | Required | Description |
|---|---|---|---|
| `databaseConnectivity` | boolean |  |  |

## v1ListApiKeysResponse

| Field | Type | Required | Description |
|---|---|---|---|
| `apiKeys` | array of `v1ApiKey` |  |  |

## v1ListNodesResponse

| Field | Type | Required | Description |
|---|---|---|---|
| `nodes` | array of `v1Node` |  |  |

## v1ListPreAuthKeysResponse

| Field | Type | Required | Description |
|---|---|---|---|
| `preAuthKeys` | array of `v1PreAuthKey` |  |  |

## v1ListUsersResponse

| Field | Type | Required | Description |
|---|---|---|---|
| `users` | array of `v1User` |  |  |

## v1Node

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string (uint64) |  |  |
| `machineKey` | string |  |  |
| `nodeKey` | string |  |  |
| `discoKey` | string |  |  |
| `ipAddresses` | array of string |  |  |
| `name` | string |  |  |
| `user` | `v1User` |  |  |
| `lastSeen` | string (date-time) |  |  |
| `expiry` | string (date-time) |  |  |
| `preAuthKey` | `v1PreAuthKey` |  |  |
| `createdAt` | string (date-time) |  |  |
| `registerMethod` | `v1RegisterMethod` |  |  |
| `givenName` | string |  |  |
| `online` | boolean |  |  |
| `approvedRoutes` | array of string |  |  |
| `availableRoutes` | array of string |  |  |
| `subnetRoutes` | array of string |  |  |
| `tags` | array of string |  |  |

## v1PreAuthKey

| Field | Type | Required | Description |
|---|---|---|---|
| `user` | `v1User` |  |  |
| `id` | string (uint64) |  |  |
| `key` | string |  |  |
| `reusable` | boolean |  |  |
| `ephemeral` | boolean |  |  |
| `used` | boolean |  |  |
| `expiration` | string (date-time) |  |  |
| `createdAt` | string (date-time) |  |  |
| `aclTags` | array of string |  |  |

## v1RegisterMethod

Type: string enum: REGISTER_METHOD_UNSPECIFIED, REGISTER_METHOD_AUTH_KEY, REGISTER_METHOD_CLI, REGISTER_METHOD_OIDC

## v1RegisterNodeResponse

| Field | Type | Required | Description |
|---|---|---|---|
| `node` | `v1Node` |  |  |

## v1RenameNodeResponse

| Field | Type | Required | Description |
|---|---|---|---|
| `node` | `v1Node` |  |  |

## v1RenameUserResponse

| Field | Type | Required | Description |
|---|---|---|---|
| `user` | `v1User` |  |  |

## v1SetApprovedRoutesResponse

| Field | Type | Required | Description |
|---|---|---|---|
| `node` | `v1Node` |  |  |

## v1SetPolicyRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `policy` | string |  |  |

## v1SetPolicyResponse

| Field | Type | Required | Description |
|---|---|---|---|
| `policy` | string |  |  |
| `updatedAt` | string (date-time) |  |  |

## v1SetTagsResponse

| Field | Type | Required | Description |
|---|---|---|---|
| `node` | `v1Node` |  |  |

## v1User

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string (uint64) |  |  |
| `name` | string |  |  |
| `createdAt` | string (date-time) |  |  |
| `displayName` | string |  |  |
| `email` | string |  |  |
| `providerId` | string |  |  |
| `provider` | string |  |  |
| `profilePicUrl` | string |  |  |

