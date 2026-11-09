---
title: "Get"
---

# Get

`POST /v2/vectordb/entities/get`

This operation gets specific entities by their IDs.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database.
- `collectionName` (string) **required** — The name of the collection to which this operation applies.
- `id` (object) **required** — A specific entity ID or a list of entity IDs.
- `outputFields` (array<string>) — An array of fields to return along with the query results.
- `partitionNames` (array<string>) — The name of the partitions to which this operation applies.
- `consistencyLevel` (string) — The consistency level for this operation. The default value is `Bounded`. · default: `"Bounded"` · enum: `["Strong", "Eventually", "Session", "Bounded"]`
- `partitionName` (string) — Name of the partition to get entities from.

## Response 200

Returns the query results.

- **anyOf – success**: A response object returned by the get operation, carrying the outcome of the request.
  - `code` (integer) — Response code.
  - `cost` (integer) — Cost of this operation.
  - `data` (array<object>) — Query results.
    - `id` (integer | string) — The primary key value of the returned entity. Milvus primary keys are Int64 or VarChar depending on the collection schema, so the value may arrive as a number or a string.
      - *oneOf – option 1*
      - *oneOf – option 2*
  - `scanned_remote_bytes` (integer) — Returned when the deployment uses tiered storage with usage tracking enabled and the operation reads from remote/disk storage. Omitted when all data is served from local cache.
  - `scanned_total_bytes` (integer) — Returned when the deployment uses tiered storage with usage tracking enabled and the operation reads from remote/disk storage. Omitted when all data is served from local cache.
  - `cache_hit_ratio` (number) — Returned when the deployment uses tiered storage with usage tracking enabled and the operation reads from remote/disk storage. Omitted when all data is served from local cache.
- **anyOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 0,
  "data": [
    {
      "color": "red_7025",
      "id": 1
    },
    {
      "color": "pink_9298",
      "id": 3
    },
    {
      "color": "yellow_4222",
      "id": 5
    }
  ]
}
```

Example – failure:

```json
{
  "code": 1800,
  "message": "User hasn't authenticated"
}
```
