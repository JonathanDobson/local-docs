# Docker Engine API 1.56 — System

## POST /v1.56/auth

operationId: `SystemAuth`

Check auth configuration

Validate credentials for a registry and, if available, get an identity
token for accessing the registry without password.

Request body: `AuthConfig`

| Response | Description | Body |
|---|---|---|
| 200 | An identity token was generated successfully. | `AuthResponse` |
| 204 | No error |  |
| 401 | Auth error | `ErrorResponse` |
| 500 | Server error | `ErrorResponse` |

## GET /v1.56/info

operationId: `SystemInfo`

Get system information

| Response | Description | Body |
|---|---|---|
| 200 | No error | `SystemInfo` |
| 500 | Server error | `ErrorResponse` |

## GET /v1.56/version

operationId: `SystemVersion`

Get version

Returns the version of Docker that is running and various information about the system that Docker is running on.

| Response | Description | Body |
|---|---|---|
| 200 | no error | `SystemVersion` |
| 500 | server error | `ErrorResponse` |

## GET /v1.56/_ping

operationId: `SystemPing`

Ping

This is a dummy endpoint you can use to test if the server is accessible.

| Response | Description | Body |
|---|---|---|
| 200 | no error | string |
| 500 | server error | `ErrorResponse` |

## HEAD /v1.56/_ping

operationId: `SystemPingHead`

Ping

This is a dummy endpoint you can use to test if the server is accessible.

| Response | Description | Body |
|---|---|---|
| 200 | no error | string |
| 500 | server error | `ErrorResponse` |

## GET /v1.56/events

operationId: `SystemEvents`

Monitor events

Stream real-time events from the server.

Various objects within Docker report events when something happens to them.

Containers report these events: `attach`, `commit`, `copy`, `create`, `destroy`, `detach`, `die`, `exec_create`, `exec_detach`, `exec_start`, `exec_die`, `export`, `health_status`, `kill`, `oom`, `pause`, `rename`, `resize`, `restart`, `start`, `stop`, `top`, `unpause`, `update`, and `prune`

Images report these events: `create`, `delete`, `import`, `load`, `pull`, `push`, `save`, `tag`, `untag`, and `prune`

Volumes report these events: `create`, `mount`, `unmount`, `destroy`, and `prune`

Networks report these events: `create`, `connect`, `disconnect`, `destroy`, `update`, `remove`, and `prune`

The Docker daemon reports these events: `reload`

Services report these events: `create`, `update`, and `remove`

Nodes report these events: `create`, `update`, and `remove`

Secrets report these events: `create`, `update`, and `remove`

Configs report these events: `create`, `update`, and `remove`

The Builder reports `prune` events

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `since` | query | string |  | Show events created since this timestamp then stream new events. |
| `until` | query | string |  | Show events created until this timestamp then stop streaming. |
| `filters` | query | string |  | A JSON encoded value of filters (a `map[string][]string`) to process on the event list. Available filters: - `config=<string>` config name or ID - `container=<string>` container name or ID - `daemon=<string>` daemon name or ID - `event=<string>` event type - `image=<string>` image name or ID - `label=<string>` image or container label - `network=<string>` network name or ID - `node=<string>` node ID - `plugin`=<string> plugin name or ID - `scope`=<string> local or swarm - `secret=<string>` secret name or ID - `service=<string>` service name or ID - `type=<string>` object to filter by, one of `container`, `image`, `volume`, `network`, `daemon`, `plugin`, `node`, `service`, `secret` or `config` - `volume=<string>` volume name |

| Response | Description | Body |
|---|---|---|
| 200 | no error | `EventMessage` |
| 400 | bad parameter | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |

## GET /v1.56/system/df

operationId: `SystemDataUsage`

Get data usage information

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `type` | query | array of string enum: container, image, volume, build-cache |  | Object types, for which to compute and return data. |
| `verbose` | query | boolean |  | Show detailed information on space usage. |

| Response | Description | Body |
|---|---|---|
| 200 | no error | object |
| 500 | server error | `ErrorResponse` |
