---
title: "Create Alias"
---

# Create Alias

`POST /v2/vectordb/aliases/create`

This operation creates an alias for an existing collection. A collection can have multiple aliases, while an alias can be associated with only one collection.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database to which the collection belongs.
- `collectionName` (string) **required** — The name of the target collection to assign the created alias to.
- `aliasName` (string) **required** — The alias of the collection.

## Response 200

None

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
