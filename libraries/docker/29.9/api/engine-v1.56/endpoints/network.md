# Docker Engine API 1.56 — Network

## GET /v1.56/networks

operationId: `NetworkList`

List networks

Returns a list of networks. For details on the format, see the
[network inspect endpoint](#operation/NetworkInspect).

Note that it uses a different, smaller representation of a network than
inspecting a single network. For example, the list of containers attached
to the network is not propagated in API versions 1.28 and up.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `filters` | query | string |  | JSON encoded value of the filters (a `map[string][]string`) to process on the networks list. Available filters: - `dangling=<boolean>` When set to `true` (or `1`), returns all networks that are not in use by a container. When set to `false` (or `0`), only networks that are in use by one or more containers are returned. - `driver=<driver-name>` Matches a network's driver. - `id=<network-id>` Matches all or part of a network ID. - `label=<key>` or `label=<key>=<value>` of a network label. - `name=<network-name>` Matches all or part of a network name. - `scope=["swarm"\|"global"\|"local"]` Filters networks by scope (`swarm`, `global`, or `local`). - `type=["custom"\|"builtin"]` Filters networks by type. The `custom` keyword returns all user-defined networks. |

| Response | Description | Body |
|---|---|---|
| 200 | No error | array of `NetworkSummary` |
| 500 | Server error | `ErrorResponse` |

## GET /v1.56/networks/{id}

operationId: `NetworkInspect`

Inspect a network

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | Network ID or name |
| `verbose` | query | boolean |  | Detailed inspect output for troubleshooting |
| `scope` | query | string |  | Filter the network by scope (swarm, global, or local) |

| Response | Description | Body |
|---|---|---|
| 200 | No error | `NetworkInspect` |
| 404 | Network not found | `ErrorResponse` |
| 500 | Server error | `ErrorResponse` |

## DELETE /v1.56/networks/{id}

operationId: `NetworkDelete`

Remove a network

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | Network ID or name |

| Response | Description | Body |
|---|---|---|
| 204 | No error |  |
| 403 | operation not supported for pre-defined networks | `ErrorResponse` |
| 404 | no such network | `ErrorResponse` |
| 500 | Server error | `ErrorResponse` |

## POST /v1.56/networks/create

operationId: `NetworkCreate`

Create a network

Request body: object

| Response | Description | Body |
|---|---|---|
| 201 | Network created successfully | `NetworkCreateResponse` |
| 400 | bad parameter | `ErrorResponse` |
| 403 | Forbidden operation. This happens when trying to create a network named after a pre-defined network, or when trying to create an overlay network on a daemon which is not part of a Swarm cluster. | `ErrorResponse` |
| 404 | plugin not found | `ErrorResponse` |
| 500 | Server error | `ErrorResponse` |

## POST /v1.56/networks/{id}/connect

operationId: `NetworkConnect`

Connect a container to a network

The network must be either a local-scoped network or a swarm-scoped network with the `attachable` option set. A network cannot be re-attached to a running container

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | Network ID or name |

Request body: `NetworkConnectRequest`

| Response | Description | Body |
|---|---|---|
| 200 | No error |  |
| 400 | bad parameter | `ErrorResponse` |
| 403 | Operation forbidden | `ErrorResponse` |
| 404 | Network or container not found | `ErrorResponse` |
| 500 | Server error | `ErrorResponse` |

## POST /v1.56/networks/{id}/disconnect

operationId: `NetworkDisconnect`

Disconnect a container from a network

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | Network ID or name |

Request body: `NetworkDisconnectRequest`

| Response | Description | Body |
|---|---|---|
| 200 | No error |  |
| 403 | Operation not supported for swarm scoped networks | `ErrorResponse` |
| 404 | Network or container not found | `ErrorResponse` |
| 500 | Server error | `ErrorResponse` |

## POST /v1.56/networks/prune

operationId: `NetworkPrune`

Delete unused networks

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `filters` | query | string |  | Filters to process on the prune list, encoded as JSON (a `map[string][]string`). Available filters: - `until=<timestamp>` Prune networks created before this timestamp. The `<timestamp>` can be Unix timestamps, date formatted timestamps, or Go duration strings (e.g. `10m`, `1h30m`) computed relative to the daemon machine’s time. - `label` (`label=<key>`, `label=<key>=<value>`, `label!=<key>`, or `label!=<key>=<value>`) Prune networks with (or without, in case `label!=...` is used) the specified labels. |

| Response | Description | Body |
|---|---|---|
| 200 | No error | object |
| 500 | Server error | `ErrorResponse` |
