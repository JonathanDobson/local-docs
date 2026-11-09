---
title: "Has Collection"
---

# Has Collection

`POST /v2/vectordb/collections/has`

This operation checks whether a collection exists.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database which the collection belongs to. Setting this to a non-existing database results in an error. If not specified, the default database applies.
- `collectionName` (string) **required** — The name of the target collection. Setting this to a non-existing collection results in an error.
- `partitionNames` (array<string>) — Names of the partitions to which this operation applies. When specified, the operation scope is limited to these partitions; otherwise the entire Collection is used.

## Response 200

A boolean value indicates whether the specified collection exists.

- **anyOf – success**: The response body indicating whether a specified Collection exists.
  - `code` (integer) — Response code. · example: `0`
  - `data` (object) — Response payload which carries a boolean value.
    - `has` (boolean) — A boolean value indicates whether the specified collection exists.
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
