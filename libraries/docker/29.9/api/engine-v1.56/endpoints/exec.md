# Docker Engine API 1.56 — Exec

## POST /v1.56/containers/{id}/exec

operationId: `ContainerExec`

Create an exec instance

Run a command inside a running container.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | ID or name of container |

Request body: object

| Response | Description | Body |
|---|---|---|
| 201 | no error | `IDResponse` |
| 404 | no such container | `ErrorResponse` |
| 409 | container is paused | `ErrorResponse` |
| 500 | Server error | `ErrorResponse` |

## POST /v1.56/exec/{id}/start

operationId: `ExecStart`

Start an exec instance

Starts a previously set up exec instance. If detach is true, this endpoint
returns immediately after starting the command. Otherwise, it sets up an
interactive session with the command.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | Exec instance ID |

Request body: object

| Response | Description | Body |
|---|---|---|
| 200 | No error |  |
| 404 | No such exec instance | `ErrorResponse` |
| 409 | Container is stopped or paused | `ErrorResponse` |

## POST /v1.56/exec/{id}/resize

operationId: `ExecResize`

Resize an exec instance

Resize the TTY session used by an exec instance. This endpoint only works
if `tty` was specified as part of creating and starting the exec instance.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | Exec instance ID |
| `h` | query | integer | yes | Height of the TTY session in characters |
| `w` | query | integer | yes | Width of the TTY session in characters |

| Response | Description | Body |
|---|---|---|
| 200 | No error |  |
| 400 | bad parameter | `ErrorResponse` |
| 404 | No such exec instance | `ErrorResponse` |
| 500 | Server error | `ErrorResponse` |

## GET /v1.56/exec/{id}/json

operationId: `ExecInspect`

Inspect an exec instance

Return low-level information about an exec instance.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | Exec instance ID |

| Response | Description | Body |
|---|---|---|
| 200 | No error | object |
| 404 | No such exec instance | `ErrorResponse` |
| 500 | Server error | `ErrorResponse` |
