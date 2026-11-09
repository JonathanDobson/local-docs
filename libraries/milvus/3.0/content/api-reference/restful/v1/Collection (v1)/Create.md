---
title: "Create Collection"
---

# Create Collection

`POST /v1/vector/collections/create`

**Deprecated.**

Creates a collection in a cluster.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database.
- `collectionName` (string) **required** — The name of the collection to create.
- `dimension` (integer) **required** — The number of dimensions for the vector field of the collection. · minimum: `1` · maximum: `32768`
- `metricType` (string) — The distance metric used for the collection. · default: `"COSINE"` · enum: `["L2", "IP", "COSINE"]`
- `primaryField` (string) — The primary key field name. · default: `"id"`
- `vectorField` (string) — The vector field. · default: `"vector"`
- `description` (string) — The description of the collection

Example – Option 1:

```json
{
  "collectionName": "medium_articles",
  "dimension": 256,
  "metricType": "COSINE",
  "primaryField": "id",
  "vectorField": "vector"
}
```

## Response 200

Returns an empty object.

- **oneOf – success**: A single response payload returned by the Collection creation operation.
  - `code` (integer) — Response code.
  - `data` (object) — Response payload which is an empty object.
- **oneOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 200,
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
