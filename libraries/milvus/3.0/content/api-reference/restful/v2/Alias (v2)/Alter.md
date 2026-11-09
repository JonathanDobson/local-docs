---
title: "Alter Alias"
---

# Alter Alias

`POST /v2/vectordb/aliases/alter`

This operation reassigns the alias of one collection to another.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — The name of the database to which the collection belongs.
- `collectionName` (string) **required** — The name of the target collection to reassign an alias to.
- `aliasName` (string) **required** — The alias of the collection.

## Response 200

Returns an empty object or an error message.

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
