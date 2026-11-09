---
title: "Create Index"
---

# Create Index

`POST /v2/vectordb/indexes/create`

This creates a named index for a target field, which can either be a vector field or a scalar field.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database that to which the collection belongs . Setting this to a non-existing database results in an error.
- `collectionName` (string) **required** — The name of the target collection. Setting this to a non-existing collection results in an error.
- `indexParams` (array<object>) **required** — The parameters that apply to the index-building process.
  - `metricType` (string) **required** — The similarity metric type used to build the index. For more information, refer to [Similarity Metrics Explained](/docs/search-metrics-explained). · default: `"COSINE"` · enum: `["L2", "IP", "COSINE"]`
  - `fieldName` (string) **required** — The name of the target field on which an index is to be created.
  - `indexName` (string) **required** — The name of the index to create. The value defaults to the target field name.
  - `indexType` (string) **required** — The type of the index to create
  - `params` (object) — The index type and related settings. For details, refer to [Vector Indexes](https://milvus.io/docs/index.md).
    - `M` (integer) — The maximum degree of the node. This applies only when **index_type** is set to **HNSW**.
    - `efConstruction` (integer) — The search scope. This applies only when **index_type** is set to **HNSW**.
    - `nlist` (integer) — The number of cluster units. This applies only when **index_type** is set to **IVF**-related index types.

## Response 200

None

- **oneOf – success**: A success response
  - `code` (integer) — Response code.
  - `data` (object) — Response payload which is an empty object.
- **oneOf – failure**: A failure response.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 0,
  "data": {}
}
```

Example – failure:

```json
{
  "code": 1800,
  "message": "User hasn't authenticated"
}
```
