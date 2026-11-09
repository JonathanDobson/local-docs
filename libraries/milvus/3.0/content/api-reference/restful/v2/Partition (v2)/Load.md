---
title: "Load Partitions"
---

# Load Partitions

`POST /v2/vectordb/partitions/load`

This operation loads the data of the current partition into memory.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database that to which the collection belongs . Setting this to a non-existing database results in an error.
- `collectionName` (string) **required** — The name of the target collection. Setting this to a non-existing collection results in an error.
- `partitionNames` (array<string>) **required** — The list of names of the target partitions.

## Response 200

Return an empty object or an error message.

- **anyOf – success**: A success response
  - `code` (integer) — Response code. · example: `0`
  - `data` (object) — Response payload which is an empty object.
- **anyOf – failure**: Returns an error message.
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
