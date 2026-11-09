---
title: "Drop Collection"
---

# Drop Collection

`POST /v1/vector/collections/drop`

**Deprecated.**

Drops a collection. This operation erases your collection data. Exercise caution when performing this operation.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database.
- `collectionName` (string) **required** — The name of the collection to delete.

## Response 200

Returns an empty object or an error message.

- **anyOf – success**: An object returned when a Collection is dropped successfully.
  - `code` (integer) — Response code.
  - `data` (object) — Returns an empty object.
- **anyOf – failure**: Returns an error message.
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
