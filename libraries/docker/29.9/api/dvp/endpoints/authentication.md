# DVP Data API 1.0.0 — authentication

## POST /api/publisher/analytics/v1/v2/users/login

operationId: `PostUsersLogin`

Create an authentication token

Creates and returns a bearer token in JWT format that you can use to
authenticate with Docker Hub APIs.

The returned token is used in the HTTP Authorization header like `Authorization: Bearer {TOKEN}`.

Most Docker Hub APIs require this token either to consume or to get detailed information. For example, to list images in a private repository.

Request body (application/json): `UsersLoginRequest`

| Response | Description | Body |
|---|---|---|
| 200 | Authentication successful | `PostUsersLoginSuccessResponse` |
| 401 | Authentication failed or second factor required | `PostUsersLoginErrorResponse` |

## POST /api/publisher/analytics/v1/v2/users/2fa-login

operationId: `PostUsers2FALogin`

Second factor authentication

When a user has 2FA enabled, this is the second call to perform after
`/v2/users/login` call.

Creates and returns a bearer token in JWT format that you can use to authenticate with Docker Hub APIs.

The returned token is used in the HTTP Authorization header like `Authorization: Bearer {TOKEN}`.

Most Docker Hub APIs require this token either to consume or to get detailed information. For example, to list images in a private repository.

Request body (application/json): `Users2FALoginRequest`

| Response | Description | Body |
|---|---|---|
| 200 | Authentication successful | `PostUsersLoginSuccessResponse` |
| 401 | Authentication failed or second factor required | `PostUsers2FALoginErrorResponse` |
