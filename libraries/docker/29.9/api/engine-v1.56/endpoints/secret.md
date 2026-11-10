# Docker Engine API 1.56 — Secret

## GET /v1.56/secrets

operationId: `SecretList`

List secrets

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `filters` | query | string |  | A JSON encoded value of the filters (a `map[string][]string`) to process on the secrets list. Available filters: - `id=<secret id>` - `label=<key> or label=<key>=value` - `name=<secret name>` matches all or part of a secret name (prefix match) - `names=<secret name>` matches a secret name (exact match) |

| Response | Description | Body |
|---|---|---|
| 200 | no error | array of `Secret` |
| 500 | server error | `ErrorResponse` |
| 503 | node is not part of a swarm | `ErrorResponse` |

## POST /v1.56/secrets/create

operationId: `SecretCreate`

Create a secret

Request body: allOf(`SecretSpec`, object)

| Response | Description | Body |
|---|---|---|
| 201 | no error | `IDResponse` |
| 409 | name conflicts with an existing object | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |
| 503 | node is not part of a swarm | `ErrorResponse` |

## GET /v1.56/secrets/{id}

operationId: `SecretInspect`

Inspect a secret

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | ID of the secret |

| Response | Description | Body |
|---|---|---|
| 200 | no error | `Secret` |
| 404 | secret not found | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |
| 503 | node is not part of a swarm | `ErrorResponse` |

## DELETE /v1.56/secrets/{id}

operationId: `SecretDelete`

Delete a secret

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | ID of the secret |

| Response | Description | Body |
|---|---|---|
| 204 | no error |  |
| 404 | secret not found | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |
| 503 | node is not part of a swarm | `ErrorResponse` |

## POST /v1.56/secrets/{id}/update

operationId: `SecretUpdate`

Update a Secret

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | The ID or name of the secret |
| `version` | query | integer (int64) | yes | The version number of the secret object being updated. This is required to avoid conflicting writes. |

Request body: `SecretSpec`

| Response | Description | Body |
|---|---|---|
| 200 | no error |  |
| 400 | bad parameter | `ErrorResponse` |
| 404 | no such secret | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |
| 503 | node is not part of a swarm | `ErrorResponse` |
