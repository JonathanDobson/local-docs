---
title: "Drop Index Properties"
---

# Drop Index Properties

`POST /v2/vectordb/indexes/drop_properties`

This operation drops the properties of an index.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database that to which the collection belongs . Setting this to a non-existing database results in an error.
- `collectionName` (string) **required** — The name of the target collection. Setting this to a non-existing collection results in an error.
- `indexName` (string) **required** — The name of the target index.
- `propertyKeys` (array<string>) **required** — The names of the properties to drop.

## Response 200

Returns an empty response.

- **oneOf – success**: A response body variant returned for the drop index properties request.
  - `code` (integer) — Response code.
  - `data` (object) — The payload returned after the index properties are dropped.
- **oneOf – failure**: Returns an error message.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 0,
  "cost": 0,
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
