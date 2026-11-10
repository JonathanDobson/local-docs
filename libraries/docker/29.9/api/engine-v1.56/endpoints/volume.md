# Docker Engine API 1.56 — Volume

## GET /v1.56/volumes

operationId: `VolumeList`

List volumes

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `filters` | query | string (json) |  | JSON encoded value of the filters (a `map[string][]string`) to process on the volumes list. Available filters: - `dangling=<boolean>` When set to `true` (or `1`), returns all volumes that are not in use by a container. When set to `false` (or `0`), only volumes that are in use by one or more containers are returned. - `driver=<volume-driver-name>` Matches volumes based on their driver. - `label=<key>` or `label=<key>:<value>` Matches volumes based on the presence of a `label` alone or a `label` and a value. - `name=<volume-name>` Matches all or part of a volume name. |

| Response | Description | Body |
|---|---|---|
| 200 | Summary volume data that matches the query | `VolumeListResponse` |
| 500 | Server error | `ErrorResponse` |

## POST /v1.56/volumes/create

operationId: `VolumeCreate`

Create a volume

Request body: `VolumeCreateRequest`

| Response | Description | Body |
|---|---|---|
| 201 | The volume was created successfully | `Volume` |
| 500 | Server error | `ErrorResponse` |

## GET /v1.56/volumes/{name}

operationId: `VolumeInspect`

Inspect a volume

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `name` | path | string | yes | Volume name or ID |

| Response | Description | Body |
|---|---|---|
| 200 | No error | `Volume` |
| 404 | No such volume | `ErrorResponse` |
| 500 | Server error | `ErrorResponse` |

## PUT /v1.56/volumes/{name}

operationId: `VolumeUpdate`

"Update a volume. Valid only for Swarm cluster volumes"


| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `name` | path | string | yes | The name or ID of the volume |
| `version` | query | integer (int64) | yes | The version number of the volume being updated. This is required to avoid conflicting writes. Found in the volume's `ClusterVolume` field. |

Request body: object

| Response | Description | Body |
|---|---|---|
| 200 | no error |  |
| 400 | bad parameter | `ErrorResponse` |
| 404 | no such volume | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |
| 503 | node is not part of a swarm | `ErrorResponse` |

## DELETE /v1.56/volumes/{name}

operationId: `VolumeDelete`

Remove a volume

Instruct the driver to remove the volume.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `name` | path | string | yes | Volume name or ID |
| `force` | query | boolean |  | Force the removal of the volume |

| Response | Description | Body |
|---|---|---|
| 204 | The volume was removed |  |
| 404 | No such volume or volume driver | `ErrorResponse` |
| 409 | Volume is in use and cannot be removed | `ErrorResponse` |
| 500 | Server error | `ErrorResponse` |

## POST /v1.56/volumes/prune

operationId: `VolumePrune`

Delete unused volumes

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `filters` | query | string |  | Filters to process on the prune list, encoded as JSON (a `map[string][]string`). Available filters: - `label` (`label=<key>`, `label=<key>=<value>`, `label!=<key>`, or `label!=<key>=<value>`) Prune volumes with (or without, in case `label!=...` is used) the specified labels. - `all` (`all=true`) - Consider all (local) volumes for pruning and not just anonymous volumes. |

| Response | Description | Body |
|---|---|---|
| 200 | No error | object |
| 500 | Server error | `ErrorResponse` |
