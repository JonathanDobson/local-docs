---
title: "Revoke Object Privilege From Role"
---

# Revoke Object Privilege From Role

`POST /v2/vectordb/roles/revoke_privilege`

This operation revokes a privilege granted to the current role.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `roleName` (string) **required** — The name of the role.
- `objectType` (string) **required** — The type of the object to which the specified privilege belongs.
- `objectName` (string) **required** — The name of the object to which the specified privilege belongs.
- `privilege` (string) **required** — The privilege that is revoked from the role.
- `dbName` (string) — Name of the database. If not specified, the default database is used.

## Response 200

Return an empty object or an error message.

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
