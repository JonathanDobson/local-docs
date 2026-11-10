# Docker Engine API 1.56 — Config

## GET /v1.56/configs

operationId: `ConfigList`

List configs

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `filters` | query | string |  | A JSON encoded value of the filters (a `map[string][]string`) to process on the configs list. Available filters: - `id=<config id>` - `label=<key> or label=<key>=value` - `name=<config name>` matches all or part of a config name (prefix match) |

| Response | Description | Body |
|---|---|---|
| 200 | no error | array of `Config` |
| 500 | server error | `ErrorResponse` |
| 503 | node is not part of a swarm | `ErrorResponse` |

## POST /v1.56/configs/create

operationId: `ConfigCreate`

Create a config

Request body: allOf(`ConfigSpec`, object)

| Response | Description | Body |
|---|---|---|
| 201 | no error | `IDResponse` |
| 409 | name conflicts with an existing object | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |
| 503 | node is not part of a swarm | `ErrorResponse` |

## GET /v1.56/configs/{id}

operationId: `ConfigInspect`

Inspect a config

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | ID of the config |

| Response | Description | Body |
|---|---|---|
| 200 | no error | `Config` |
| 404 | config not found | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |
| 503 | node is not part of a swarm | `ErrorResponse` |

## DELETE /v1.56/configs/{id}

operationId: `ConfigDelete`

Delete a config

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | ID of the config |

| Response | Description | Body |
|---|---|---|
| 204 | no error |  |
| 404 | config not found | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |
| 503 | node is not part of a swarm | `ErrorResponse` |

## POST /v1.56/configs/{id}/update

operationId: `ConfigUpdate`

Update a Config

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | The ID or name of the config |
| `version` | query | integer (int64) | yes | The version number of the config object being updated. This is required to avoid conflicting writes. |

Request body: `ConfigSpec`

| Response | Description | Body |
|---|---|---|
| 200 | no error |  |
| 400 | bad parameter | `ErrorResponse` |
| 404 | no such config | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |
| 503 | node is not part of a swarm | `ErrorResponse` |
