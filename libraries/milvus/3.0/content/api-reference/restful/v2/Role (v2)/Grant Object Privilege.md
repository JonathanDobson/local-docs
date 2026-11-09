---
title: "Grant Object Privilege To Role"
---

# Grant Object Privilege To Role

`POST /v2/vectordb/roles/grant_privilege`

This operation grants a privilege to the current role.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `roleName` (string) **required** — The name of the role.
- `objectType` (string) **required** — The type of the object to which the privilege belongs.
- `objectName` (string) **required** — The name of the object to which the role is granted the specified privilege.
- `privilege` (string) **required** — The privilege that is granted to the role.
- `dbName` (string) — Name of the database. If not specified, the default database is used.

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
