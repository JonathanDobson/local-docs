---
title: "List Roles"
---

# List Roles

`POST /v2/vectordb/roles/list`

This operation lists the information about all existing roles.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `dbName` (string) — Name of the database. If not specified, the default database is used.

## Response 200

A RoleInfo object that contains a list of RoleItem objects.

- **oneOf – success**: One possible result of the role listing request, representing a single response variant returned by the operation.
  - `code` (integer) — Response code. · example: `0`
  - `data` (array<string>) — Response payload which is a list of item objects.
- **oneOf – failure**: A failure response.
  - `code` (integer) — Response code.
  - `message` (string) — Error message.

Example – success:

```json
{
  "code": 0,
  "data": [
    "admin",
    "public"
  ]
}
```

Example – failure:

```json
{
  "code": 1800,
  "message": "User hasn't authenticated"
}
```
