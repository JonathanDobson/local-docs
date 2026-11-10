# Docker Sandboxes API v1 — MCP gateways

## GET /sandboxes/v1/mcp-servers/{mcpServer}/authorization

operationId: `getMcpAuthorization`

GetMcpAuthorization reads the owner-scoped flow, including its pending URL, under mcp.write.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `mcpServer` | path | string | yes | The mcpServer id. |
| `If-None-Match` | header | string |  | A quoted entity-tag or comma-separated list, compared weakly with the current resource etag. A match, including a weak form or wildcard *, answers 304 without a body after authorization. Malformed input is treated as no match. |

| Response | Description | Body |
|---|---|---|
| 200 | Success | `McpAuthorization` |
| 304 | The resource's etag equals the If-None-Match value, so this response carries no body. |  |
| 404 | The target is absent or not visible within the caller's scope. | `Error` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## POST /sandboxes/v1/mcp-servers/{mcpServer}/authorization/authorize

operationId: `authorizeMcpServer`

AuthorizeMcpServer authorizes credentials for one named upstream.

AuthorizeMcpServer authorizes credentials for one named upstream.
Action: authorization runs an interactive grant whose result is not the request body.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `mcpServer` | path | string | yes | The mcpServer id. |
| `If-Match` | header | string |  | Optional current authorization etag. A supplied stale value answers 412 with failedPrecondition; omission permits create or convergence, including forced reauthorization. |

Request body (application/json): object

| Response | Description | Body |
|---|---|---|
| 200 | Success | allOf(`McpAuthorization`, object) |
| 202 | Accepted. The resource is still progressing; read it or follow its events until completion. | allOf(`McpAuthorization`, object) |
| 412 | The precondition is not the resource's current etag. The body carries failedPrecondition naming etag_mismatch and an EtagMismatch detail with the current value. | `Error` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## GET /sandboxes/v1/sandboxes/{sandbox}/mcp-gateway

operationId: `getMcpGateway`

GetMcpGateway reads gateway state for the sandbox.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `sandbox` | path | string | yes | The sandbox id. |

| Response | Description | Body |
|---|---|---|
| 200 | Success | `McpGateway` |
| 404 | The target is absent or not visible within the caller's scope. | `Error` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## POST /sandboxes/v1/sandboxes/{sandbox}/mcp-gateway/servers

operationId: `addMcpGatewayServer`

AddMcpGatewayServer adds one server to an existing ready gateway.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `sandbox` | path | string | yes | The sandbox id. |

Request body (application/json): object

| Response | Description | Body |
|---|---|---|
| 200 | Success | `AddMcpGatewayServerResponse` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |
