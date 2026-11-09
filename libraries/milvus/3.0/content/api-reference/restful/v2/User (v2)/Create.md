---
title: "Create User"
---

# Create User

`POST /v2/vectordb/users/create`

This operation creates a new user with a corresponding password.

## Parameters

- `Authorization` (in header) **required** — The authentication token should be a pair of colon-joined username and password, like `username:password`. · example: `Bearer {{TOKEN}}`

## Request body (application/json)

- `userName` (string) **required** — The name of the target user. The value should start with a letter and can only contain underline, letters and numbers.
- `password` (string) **required** — The corresponding password to the user. The password must must include at least three of the following character types: uppercase letters, lowercase letters, numbers, and special characters. · format: `"password"`
- `description` (string) — The description of the user.

Example – example:

```json
{
  "userName": "myUser",
  "password": "P@ssw0rd",
  "description": "Read-only analyst account."
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
