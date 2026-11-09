---
title: "List Indexes"
---

# List Indexes

`POST /v2/vectordb/indexes/list`

This operation lists all indexes of a specific collection.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database to which the collection belongs.
- `collectionName` (string) **required** — The name of an existing collection. Setting this to a non-existing collection leads to an error.
- `partitionNames` (array<string>) — The names of the partitions to which this operation applies. When specified, the operation is limited to those partitions; when omitted, the entire Collection is covered.

## Response 200

An object that contains the names of all built indexes.

- **oneOf – success**: A success response.
  - `code` (integer) — Response code. · example: `0`
  - `data` (array<string>) — Response payload which is a list of indexes.
- **oneOf – failure**: A failure response.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 0,
  "data": [
    "my_vector_index"
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
