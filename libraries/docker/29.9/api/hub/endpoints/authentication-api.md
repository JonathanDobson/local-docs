# Docker HUB API 2-beta — authentication-api

## POST /v2/users/login

operationId: `PostUsersLogin`
**DEPRECATED**

Create an authentication token

Creates and returns a bearer token in JWT format that you can use to authenticate with Docker Hub APIs.

The returned token is used in the HTTP Authorization header like `Authorization: Bearer {TOKEN}`.

_**As of September 16, 2024, this route requires a personal access token (PAT) instead of a password if your organization has SSO enforced.**_


  Deprecated: Use [Create access token](#tag/authentication-api/operation/AuthCreateAccessToken) instead.

Request body (application/json): `UsersLoginRequest`

| Response | Description | Body |
|---|---|---|
| 200 | Authentication successful | `PostUsersLoginSuccessResponse` |
| 401 | Authentication failed or second factor required | `PostUsersLoginErrorResponse` |

## POST /v2/users/2fa-login

operationId: `PostUsers2FALogin`

Second factor authentication

When a user has two-factor authentication (2FA) enabled, this is the second call to perform after `/v2/auth/token` call.

Creates and returns a bearer token in JWT format that you can use to authenticate with Docker Hub APIs.

The returned token is used in the HTTP Authorization header like `Authorization: Bearer {TOKEN}`.

Most Docker Hub APIs require this token either to consume or to get detailed information. For example, to list images in a private repository.

Request body (application/json): `Users2FALoginRequest`

| Response | Description | Body |
|---|---|---|
| 200 | Authentication successful | `PostUsersLoginSuccessResponse` |
| 401 | Authentication failed | `PostUsers2FALoginErrorResponse` |

## POST /v2/auth/token

operationId: `AuthCreateAccessToken`

Create access token

Creates and returns a short-lived access token in JWT format for use as a bearer when calling Docker APIs.

If successful, the access token returned should be used in the HTTP Authorization header like 
`Authorization: Bearer {access_token}`.

_**If your organization has SSO enforced, you must use a personal access token (PAT) instead of a password.**_

Request body (application/json): object

| Response | Description | Body |
|---|---|---|
| 200 | Token created | `AuthCreateTokenResponse` |
| 401 | Unauthorized (`unauthorized`) | `error` |
