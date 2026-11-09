---
title: "Drop Collection Field"
---

# Drop Collection Field

`POST /v2/vectordb/collections/fields/drop`

This operation drops a field from an existing collection by field name or field ID.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- **anyOf – option 1**: The request body must specify `collectionName` together with either `fieldName` or `fieldId` to identify the field to drop.
  - `collectionName` (string) **required** — The name of the Collection from which the field is dropped.
  - `dbName` (string) — The name of the database that contains the target collection. Use it to scope the request to a specific database.
- **anyOf – option 2**: The request body must specify `collectionName` together with either `fieldName` or `fieldId` to identify the field to drop.
  - `collectionName` (string) **required** — The name of the Collection from which the field is dropped.
  - `dbName` (string) — The name of the database that contains the target collection. Use it to scope the request to a specific database.

## Response 200

Returns an empty object.

- **oneOf – success**: A generic response envelope returned by operations that carry no operation-specific result data. It still includes a `data` object.
  - `code` (integer) — Response code.
  - `data` (object) — The response payload object. Its contents depend on the operation that returns it.
- **oneOf – failure**: Returns an error message.
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
  "code": 1100,
  "message": "field not found"
}
```
