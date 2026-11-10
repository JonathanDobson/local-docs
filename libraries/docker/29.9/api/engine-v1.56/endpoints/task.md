# Docker Engine API 1.56 — Task

## GET /v1.56/tasks

operationId: `TaskList`

List tasks

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `filters` | query | string |  | A JSON encoded value of the filters (a `map[string][]string`) to process on the tasks list. Available filters: - `desired-state=(running \| shutdown \| accepted)` - `id=<task id>` - `label=key` or `label="key=value"` - `name=<task name>` - `node=<node id or name>` - `service=<service name>` |

| Response | Description | Body |
|---|---|---|
| 200 | no error | array of `Task` |
| 500 | server error | `ErrorResponse` |
| 503 | node is not part of a swarm | `ErrorResponse` |

## GET /v1.56/tasks/{id}

operationId: `TaskInspect`

Inspect a task

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | ID of the task |

| Response | Description | Body |
|---|---|---|
| 200 | no error | `Task` |
| 404 | no such task | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |
| 503 | node is not part of a swarm | `ErrorResponse` |

## GET /v1.56/tasks/{id}/logs

operationId: `TaskLogs`

Get task logs

Get `stdout` and `stderr` logs from a task.
See also [`/containers/{id}/logs`](#operation/ContainerLogs).

**Note**: This endpoint works only for services with the `local`,
`json-file` or `journald` logging drivers.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | ID of the task |
| `details` | query | boolean |  | Show task context and extra details provided to logs. |
| `follow` | query | boolean |  | Keep connection after returning logs. |
| `stdout` | query | boolean |  | Return logs from `stdout` |
| `stderr` | query | boolean |  | Return logs from `stderr` |
| `since` | query | integer |  | Only return logs since this time, as a UNIX timestamp |
| `timestamps` | query | boolean |  | Add timestamps to every log line |
| `tail` | query | string |  | Only return this number of log lines from the end of the logs. Specify as an integer or `all` to output all log lines. |

| Response | Description | Body |
|---|---|---|
| 200 | logs returned as a stream in response body | string (binary) |
| 404 | no such task | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |
| 503 | node is not part of a swarm | `ErrorResponse` |
