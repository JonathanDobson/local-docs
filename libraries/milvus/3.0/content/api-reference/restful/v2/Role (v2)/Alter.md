---
title: "Alter Role"
---

# Alter Role

`POST /v2/vectordb/roles/alter`

This operation updates the description of a specified role.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `roleName` (string) **required** — The name of the role.
- `description` (string) — The description of the role.
- `dbName` (string) — Name of the database. If not specified, the default database is used.

Example – example:

```json
{
  "roleName": "my_role",
  "description": "Grants read-only access to analytics collections."
}
```

## Response 200

Returns an empty object or an error message.

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
