# Docker Engine API 1.56 — Distribution

## GET /v1.56/distribution/{name}/json

operationId: `DistributionInspect`

Get image information from the registry

Return image digest and platform information by contacting the registry.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `name` | path | string | yes | Image name or id |

| Response | Description | Body |
|---|---|---|
| 200 | descriptor and platform information | `DistributionInspect` |
| 401 | Failed authentication or no image found | `ErrorResponse` |
| 500 | Server error | `ErrorResponse` |
