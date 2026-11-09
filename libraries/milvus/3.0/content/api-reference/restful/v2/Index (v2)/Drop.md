---
title: "Drop Index"
---

# Drop Index

`POST /v2/vectordb/indexes/drop`

This operation deletes index from a specified collection.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database that to which the collection belongs . Setting this to a non-existing database results in an error.
- `collectionName` (string) **required** — The name of the target collection. Setting this to a non-existing collection results in an error.
- `indexName` (string) **required** — The name of the target index.
- `timestamp` (integer) — A timestamp for the drop request, given as an integer.

## Response 200

None

- **oneOf – success**: A success response
  - `code` (integer) — Response code. · example: `0`
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
