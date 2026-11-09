---
title: "Get Partition Statistics"
---

# Get Partition Statistics

`POST /v2/vectordb/partitions/get_stats`

This operations gets the number of entities in a partition.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of an existing database. · default: `"default"`
- `collectionName` (string) **required** — The name of an existing collection.
- `partitionName` (string) **required** — The name of the target partition of this operation.

## Response 200

Returns the number of entities in the specified collection.

- **anyOf – success**: A response payload form carrying the statistics of the requested Partition.
  - `code` (integer) — Response code. · example: `0`
  - `data` (object) — Statistics of the specified partition.
    - `rowCount` (integer) — The number of entities.
- **anyOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 0,
  "data": {
    "rowCount": 0
  }
}
```

Example – failure:

```json
{
  "code": 1800,
  "message": "User hasn't authenticated"
}
```
