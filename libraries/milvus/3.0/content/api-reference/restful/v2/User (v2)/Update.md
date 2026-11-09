---
title: "Update User"
---

# Update User

`POST /v2/vectordb/users/update_password`

This operation updates the password or description of a specified user.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `userName` (string) **required** — The name of the target user. The value should start with a letter and can only contain underline, letters and numbers.
- `password` (string) — The current password of the user. Provide this field together with `newPassword` when changing the password. · format: `"password"`
- `newPassword` (string) — The new password for the user. Provide this field together with `password` when changing the password. · format: `"password"`
- `description` (string) — The new description of the user. The value can be an empty string.

Example – Update password:

```json
{
  "userName": "myUser",
  "password": "P@ssw0rd*",
  "newPassword": "P@ssw0rd!"
}
```

Example – Update description:

```json
{
  "userName": "myUser",
  "description": "Read-only analyst account."
}
```

## Response 200

Return an empty object or an error message

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
