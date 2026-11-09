---
title: "Grant Role To User"
---

# Grant Role To User

`POST /v2/vectordb/users/grant_role`

This operation grants a specified role to the current user. Once granted the role, the user gets permissions allowed for the current role and can perform certain operations.To complete this operation, you need to enable authentication on your Milvus instance. For details, refer to [Authenticate User Access](https://milvus.io/docs/authenticate.md).

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
