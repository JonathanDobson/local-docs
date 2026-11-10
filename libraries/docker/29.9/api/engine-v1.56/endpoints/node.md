# Docker Engine API 1.56 — Node

## GET /v1.56/nodes

operationId: `NodeList`

List nodes

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `filters` | query | string |  | Filters to process on the nodes list, encoded as JSON (a `map[string][]string`). Available filters: - `id=<node id>` - `label=<engine label>` - `membership=`(`accepted`\|`pending`)` - `name=<node name>` - `node.label=<node label>` - `role=`(`manager`\|`worker`)` |

| Response | Description | Body |
|---|---|---|
| 200 | no error | array of `Node` |
| 500 | server error | `ErrorResponse` |
| 503 | node is not part of a swarm | `ErrorResponse` |

## GET /v1.56/nodes/{id}

operationId: `NodeInspect`

Inspect a node

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | The ID or name of the node |

| Response | Description | Body |
|---|---|---|
| 200 | no error | `Node` |
| 404 | no such node | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |
| 503 | node is not part of a swarm | `ErrorResponse` |

## DELETE /v1.56/nodes/{id}

operationId: `NodeDelete`

Delete a node

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | The ID or name of the node |
| `force` | query | boolean |  | Force remove a node from the swarm |

| Response | Description | Body |
|---|---|---|
| 200 | no error |  |
| 404 | no such node | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |
| 503 | node is not part of a swarm | `ErrorResponse` |

## POST /v1.56/nodes/{id}/update

operationId: `NodeUpdate`

Update a node

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | The ID of the node |
| `version` | query | integer (int64) | yes | The version number of the node object being updated. This is required to avoid conflicting writes. |

Request body: `NodeSpec`

| Response | Description | Body |
|---|---|---|
| 200 | no error |  |
| 400 | bad parameter | `ErrorResponse` |
| 404 | no such node | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |
| 503 | node is not part of a swarm | `ErrorResponse` |
