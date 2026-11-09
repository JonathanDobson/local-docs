---
title: "Has Partition"
---

# Has Partition

`POST /v2/vectordb/partitions/has`

This operation checks whether a partition exists.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of an existing database.
- `collectionName` (string) **required** — The name of an existing collection.
- `partitionName` (string) **required** — The name of the partition to test.

## Response 200

A boolean value indicating whether the specified partition exists.

- **anyOf – success**: A response payload form for the Partition existence check, reporting whether the requested Partition is present.
  - `code` (integer) — Response code. · example: `0`
  - `data` (object) — Response payload which carries a boolean value.
    - `has` (boolean) — A boolean value indicates whether the specified partition exists.
- **anyOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 0,
  "data": {
    "has": true
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
