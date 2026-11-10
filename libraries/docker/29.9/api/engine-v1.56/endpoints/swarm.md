# Docker Engine API 1.56 — Swarm

## GET /v1.56/swarm

operationId: `SwarmInspect`

Inspect swarm

| Response | Description | Body |
|---|---|---|
| 200 | no error | `Swarm` |
| 404 | no such swarm | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |
| 503 | node is not part of a swarm | `ErrorResponse` |

## POST /v1.56/swarm/init

operationId: `SwarmInit`

Initialize a new swarm

Request body: object

| Response | Description | Body |
|---|---|---|
| 200 | no error | string |
| 400 | bad parameter | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |
| 503 | node is already part of a swarm | `ErrorResponse` |

## POST /v1.56/swarm/join

operationId: `SwarmJoin`

Join an existing swarm

Request body: object

| Response | Description | Body |
|---|---|---|
| 200 | no error |  |
| 400 | bad parameter | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |
| 503 | node is already part of a swarm | `ErrorResponse` |

## POST /v1.56/swarm/leave

operationId: `SwarmLeave`

Leave a swarm

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `force` | query | boolean |  | Force leave swarm, even if this is the last manager or that it will break the cluster. |

| Response | Description | Body |
|---|---|---|
| 200 | no error |  |
| 500 | server error | `ErrorResponse` |
| 503 | node is not part of a swarm | `ErrorResponse` |

## POST /v1.56/swarm/update

operationId: `SwarmUpdate`

Update a swarm

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `version` | query | integer (int64) | yes | The version number of the swarm object being updated. This is required to avoid conflicting writes. |
| `rotateWorkerToken` | query | boolean |  | Rotate the worker join token. |
| `rotateManagerToken` | query | boolean |  | Rotate the manager join token. |
| `rotateManagerUnlockKey` | query | boolean |  | Rotate the manager unlock key. |

Request body: `SwarmSpec`

| Response | Description | Body |
|---|---|---|
| 200 | no error |  |
| 400 | bad parameter | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |
| 503 | node is not part of a swarm | `ErrorResponse` |

## GET /v1.56/swarm/unlockkey

operationId: `SwarmUnlockkey`

Get the unlock key

| Response | Description | Body |
|---|---|---|
| 200 | no error | object |
| 500 | server error | `ErrorResponse` |
| 503 | node is not part of a swarm | `ErrorResponse` |

## POST /v1.56/swarm/unlock

operationId: `SwarmUnlock`

Unlock a locked manager

Request body: object

| Response | Description | Body |
|---|---|---|
| 200 | no error |  |
| 500 | server error | `ErrorResponse` |
| 503 | node is not part of a swarm | `ErrorResponse` |
