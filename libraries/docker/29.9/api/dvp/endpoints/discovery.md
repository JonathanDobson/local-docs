# DVP Data API 1.0.0 — discovery

## GET /api/publisher/analytics/v1/

operationId: `getNamespaces`

Get namespaces and repos

Gets a list of your namespaces and repos which have data available.

| Response | Description | Body |
|---|---|---|
| 200 | Success | `NamespaceData` |

## GET /api/publisher/analytics/v1/namespaces

operationId: `getUserNamespaces`

Get user's namespaces

Get metadata associated with the namespaces the user has access to, including extra repos associated with the namespaces.

| Response | Description | Body |
|---|---|---|
| 200 | Success | array of `NamespaceMetadata` |
| 401 | Authentication failed or second factor required |  |

## GET /api/publisher/analytics/v1/namespaces/{namespace}

operationId: `getNamespace`

Get namespace

Gets metadata associated with specified namespace, including extra repos associated with the namespace.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `namespace` | path | string | yes | Namespace to fetch data for |

| Response | Description | Body |
|---|---|---|
| 200 | Success | `NamespaceMetadata` |
