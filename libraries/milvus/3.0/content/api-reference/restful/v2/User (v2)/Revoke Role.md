---
title: "Revoke Role From User"
---

# Revoke Role From User

`POST /v2/vectordb/users/revoke_role`

This operation revokes a privilege granted to the current role.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `userName` (string) **required** — The name of the target user. The value should start with a letter and can only contain underline, letters and numbers.
- `roleName` (string) **required** — The name of the target role.

Example – example:

```json
{
  "roleName": "admin",
  "userName": "milvusAdmin"
}
```

## Response 200

None

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
