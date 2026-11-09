---
title: "Grant Privilege To Role"
---

# Grant Privilege To Role

`POST /v2/vectordb/roles/grant_privilege_v2`

This operation grants a privilege to a role at the global, database, or collection level.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. If you are using a project endpoint, only a valid API key with sufficient permissions applies. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `roleName` (string) **required** — The name of the role.
- `privilege` (string) **required** — The privilege to grant or revoke.
- `dbName` (string) — The name of the database to which the privilege applies. Use `*` for all databases.
- `collectionName` (string) — The name of the collection to which the privilege applies. Use `*` for all collections.

## Response 200

None

- **anyOf – success**: A generic response envelope used by operations that return no substantial payload.
  - `code` (integer) — Response code.
  - `data` (object) — Payload object of the response envelope. It holds the result content of the operation.
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
