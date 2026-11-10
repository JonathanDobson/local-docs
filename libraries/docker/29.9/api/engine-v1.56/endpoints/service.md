# Docker Engine API 1.56 — Service

## GET /v1.56/services

operationId: `ServiceList`

List services

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `filters` | query | string |  | A JSON encoded value of the filters (a `map[string][]string`) to process on the services list. Available filters: - `id=<service id>` - `label=<service label>` - `mode=["replicated"\|"global"]` - `name=<service name>` |
| `status` | query | boolean |  | Include service status, with count of running and desired tasks. |

| Response | Description | Body |
|---|---|---|
| 200 | no error | array of `Service` |
| 500 | server error | `ErrorResponse` |
| 503 | node is not part of a swarm | `ErrorResponse` |

## POST /v1.56/services/create

operationId: `ServiceCreate`

Create a service

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `X-Registry-Auth` | header | string |  | A base64url-encoded auth configuration for pulling from private registries. Refer to the [authentication section](#section/Authentication) for details. |

Request body: allOf(`ServiceSpec`, object)

| Response | Description | Body |
|---|---|---|
| 201 | no error | `ServiceCreateResponse` |
| 400 | bad parameter | `ErrorResponse` |
| 403 | network is not eligible for services | `ErrorResponse` |
| 409 | name conflicts with an existing service | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |
| 503 | node is not part of a swarm | `ErrorResponse` |

## GET /v1.56/services/{id}

operationId: `ServiceInspect`

Inspect a service

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | ID or name of service. |
| `insertDefaults` | query | boolean |  | Fill empty fields with default values. |

| Response | Description | Body |
|---|---|---|
| 200 | no error | `Service` |
| 404 | no such service | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |
| 503 | node is not part of a swarm | `ErrorResponse` |

## DELETE /v1.56/services/{id}

operationId: `ServiceDelete`

Delete a service

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | ID or name of service. |

| Response | Description | Body |
|---|---|---|
| 200 | no error |  |
| 404 | no such service | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |
| 503 | node is not part of a swarm | `ErrorResponse` |

## POST /v1.56/services/{id}/update

operationId: `ServiceUpdate`

Update a service

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | ID or name of service. |
| `version` | query | integer | yes | The version number of the service object being updated. This is required to avoid conflicting writes. This version number should be the value as currently set on the service *before* the update. You can find the current version by calling `GET /services/{id}` |
| `registryAuthFrom` | query | string enum: spec, previous-spec |  | If the `X-Registry-Auth` header is not specified, this parameter indicates where to find registry authorization credentials. |
| `rollback` | query | string |  | Set to this parameter to `previous` to cause a server-side rollback to the previous service spec. The supplied spec will be ignored in this case. |
| `X-Registry-Auth` | header | string |  | A base64url-encoded auth configuration for pulling from private registries. Refer to the [authentication section](#section/Authentication) for details. |

Request body: allOf(`ServiceSpec`, object)

| Response | Description | Body |
|---|---|---|
| 200 | no error | `ServiceUpdateResponse` |
| 400 | bad parameter | `ErrorResponse` |
| 404 | no such service | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |
| 503 | node is not part of a swarm | `ErrorResponse` |

## GET /v1.56/services/{id}/logs

operationId: `ServiceLogs`

Get service logs

Get `stdout` and `stderr` logs from a service. See also
[`/containers/{id}/logs`](#operation/ContainerLogs).

**Note**: This endpoint works only for services with the `local`,
`json-file` or `journald` logging drivers.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | ID or name of the service |
| `details` | query | boolean |  | Show service context and extra details provided to logs. |
| `follow` | query | boolean |  | Keep connection after returning logs. |
| `stdout` | query | boolean |  | Return logs from `stdout` |
| `stderr` | query | boolean |  | Return logs from `stderr` |
| `since` | query | integer |  | Only return logs since this time, as a UNIX timestamp |
| `timestamps` | query | boolean |  | Add timestamps to every log line |
| `tail` | query | string |  | Only return this number of log lines from the end of the logs. Specify as an integer or `all` to output all log lines. |

| Response | Description | Body |
|---|---|---|
| 200 | logs returned as a stream in response body | string (binary) |
| 404 | no such service | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |
| 503 | node is not part of a swarm | `ErrorResponse` |
