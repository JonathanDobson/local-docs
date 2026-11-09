---
title: "Drop Function from Collection"
---

# Drop Function from Collection

`POST /v2/vectordb/collections/drop_function`

This operation drops a function from the schema of a collection.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database.
- `collectionName` (string) **required** — The name of the collection.
- `FunctionName` (string) **required** — The name of the function to drop.

## Response 200

None

- **anyOf – success**: A generic response envelope returned by operations that carry no operation-specific result data. It still includes a `data` object.
  - `code` (integer) — Response code.
  - `data` (object) — The response payload object. Its contents depend on the operation that returns it.
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
  "code": 800,
  "message": "not enough permission"
}
```
