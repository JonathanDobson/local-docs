# Gitea API 28.3.0 — user

## GET /api/v1/user

operationId: `userGetCurrent`

Get the authenticated user

| Response | Description | Body |
|---|---|---|
| 200 | User (`User`) | `User` |

## GET /api/v1/user/actions/jobs

operationId: `getUserWorkflowJobs`

Get workflow jobs

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `status` | query | string |  | workflow status (requested, pending, queued, in_progress, failure, success, skipped) |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |
| `sort` | query | string |  | sort jobs by attribute. Supported values are "id". Default is "id" |
| `order` | query | string |  | sort order, either "asc" (ascending) or "desc" (descending). Default is "asc" |

| Response | Description | Body |
|---|---|---|
| 200 | WorkflowJobsList (`WorkflowJobsList`) | `ActionWorkflowJobsResponse` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/user/actions/runners

operationId: `getUserRunners`

Get user-level runners

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `disabled` | query | boolean |  | filter by disabled status (true or false) |

| Response | Description | Body |
|---|---|---|
| 200 | RunnerList (`RunnerList`) | `ActionRunnersResponse` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/user/actions/runners/registration-token

operationId: `userCreateRunnerRegistrationToken`

Get a user's actions runner registration token

| Response | Description | Body |
|---|---|---|
| 200 | RegistrationToken is response related to registration token (`RegistrationToken`) |  |

## GET /api/v1/user/actions/runners/{runner_id}

operationId: `getUserRunner`

Get a user-level runner

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `runner_id` | path | string | yes | id of the runner |

| Response | Description | Body |
|---|---|---|
| 200 | Runner (`Runner`) | `ActionRunner` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PATCH /api/v1/user/actions/runners/{runner_id}

operationId: `updateUserRunner`

Update a user-level runner

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `runner_id` | path | string | yes | id of the runner |

Request body (application/json): `EditActionRunnerOption`

| Response | Description | Body |
|---|---|---|
| 200 | Runner (`Runner`) | `ActionRunner` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## DELETE /api/v1/user/actions/runners/{runner_id}

operationId: `deleteUserRunner`

Delete a user-level runner

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `runner_id` | path | string | yes | id of the runner |

| Response | Description | Body |
|---|---|---|
| 204 | runner has been deleted |  |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/user/actions/runs

operationId: `getUserWorkflowRuns`

Get workflow runs

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `event` | query | string |  | workflow event name |
| `branch` | query | string |  | workflow branch |
| `status` | query | string |  | workflow status (requested, pending, queued, in_progress, failure, success, skipped) |
| `actor` | query | string |  | triggered by user |
| `head_sha` | query | string |  | triggering sha of the workflow run |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | WorkflowRunsList (`WorkflowRunsList`) | `ActionWorkflowRunsResponse` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PUT /api/v1/user/actions/secrets/{secretname}

operationId: `updateUserSecret`

Create or Update a secret value in a user scope

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `secretname` | path | string | yes | name of the secret |

Request body (application/json): `CreateOrUpdateSecretOption`

| Response | Description | Body |
|---|---|---|
| 201 | response when creating a secret |  |
| 204 | response when updating a secret |  |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/user/actions/secrets/{secretname}

operationId: `deleteUserSecret`

Delete a secret in a user scope

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `secretname` | path | string | yes | name of the secret |

| Response | Description | Body |
|---|---|---|
| 204 | delete one secret of the user |  |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/user/actions/variables

operationId: `getUserVariablesList`

Get the user-level list of variables which is created by current doer

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | VariableList (`VariableList`) | array of `ActionVariable` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/user/actions/variables/{variablename}

operationId: `getUserVariable`

Get a user-level variable which is created by current doer

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `variablename` | path | string | yes | name of the variable |

| Response | Description | Body |
|---|---|---|
| 200 | ActionVariable (`ActionVariable`) | `ActionVariable` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/user/actions/variables/{variablename}

operationId: `createUserVariable`

Create a user-level variable

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `variablename` | path | string | yes | name of the variable |

Request body (application/json): `CreateVariableOption`

| Response | Description | Body |
|---|---|---|
| 201 | successfully created the user-level variable |  |
| 400 | APIError is error format response (`error`) |  |
| 409 | variable name already exists. |  |

## PUT /api/v1/user/actions/variables/{variablename}

operationId: `updateUserVariable`

Update a user-level variable which is created by current doer

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `variablename` | path | string | yes | name of the variable |

Request body (application/json): `UpdateVariableOption`

| Response | Description | Body |
|---|---|---|
| 201 | response when updating a variable |  |
| 204 | response when updating a variable |  |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/user/actions/variables/{variablename}

operationId: `deleteUserVariable`

Delete a user-level variable which is created by current doer

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `variablename` | path | string | yes | name of the variable |

| Response | Description | Body |
|---|---|---|
| 201 | response when deleting a variable |  |
| 204 | response when deleting a variable |  |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/user/applications/oauth2

operationId: `userGetOauth2Application`

List the authenticated user's oauth2 applications

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | OAuth2ApplicationList represents a list of OAuth2 applications. (`OAuth2ApplicationList`) | array of `OAuth2Application` |

## POST /api/v1/user/applications/oauth2

operationId: `userCreateOAuth2Application`

creates a new OAuth2 application

Request body (application/json): `CreateOAuth2ApplicationOptions`

| Response | Description | Body |
|---|---|---|
| 201 | OAuth2Application (`OAuth2Application`) | `OAuth2Application` |
| 400 | APIError is error format response (`error`) |  |

## GET /api/v1/user/applications/oauth2/{id}

operationId: `userGetOAuth2Application`

get an OAuth2 Application

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | Application ID to be found |

| Response | Description | Body |
|---|---|---|
| 200 | OAuth2Application (`OAuth2Application`) | `OAuth2Application` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PATCH /api/v1/user/applications/oauth2/{id}

operationId: `userUpdateOAuth2Application`

update an OAuth2 Application, this includes regenerating the client secret

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | application to be updated |

Request body (application/json): `CreateOAuth2ApplicationOptions`

| Response | Description | Body |
|---|---|---|
| 200 | OAuth2Application (`OAuth2Application`) | `OAuth2Application` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/user/applications/oauth2/{id}

operationId: `userDeleteOAuth2Application`

delete an OAuth2 Application

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | token to be deleted |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/user/avatar

operationId: `userUpdateAvatar`

Update Avatar

Request body (application/json): `UpdateUserAvatarOption`

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |

## DELETE /api/v1/user/avatar

operationId: `userDeleteAvatar`

Delete Avatar

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |

## GET /api/v1/user/blocks

operationId: `userListBlocks`

List users blocked by the authenticated user

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | UserList (`UserList`) | array of `User` |

## GET /api/v1/user/blocks/{username}

operationId: `userCheckUserBlock`

Check if a user is blocked by the authenticated user

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | yes | username of the user to check |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PUT /api/v1/user/blocks/{username}

operationId: `userBlockUser`

Block a user

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | yes | username of the user to block |
| `note` | query | string |  | optional note for the block |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## DELETE /api/v1/user/blocks/{username}

operationId: `userUnblockUser`

Unblock a user

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | yes | username of the user to unblock |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/user/emails

operationId: `userListEmails`

List the authenticated user's email addresses

| Response | Description | Body |
|---|---|---|
| 200 | EmailList (`EmailList`) | array of `Email` |

## POST /api/v1/user/emails

operationId: `userAddEmail`

Add email addresses

Request body (application/json): `CreateEmailOption`

| Response | Description | Body |
|---|---|---|
| 201 | EmailList (`EmailList`) | array of `Email` |
| 400 | APIError is error format response (`error`) |  |
| 409 | APIError is error format response (`error`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## DELETE /api/v1/user/emails

operationId: `userDeleteEmail`

Delete email addresses

Request body (application/json): `DeleteEmailOption`

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/user/followers

operationId: `userCurrentListFollowers`

List the authenticated user's followers

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | UserList (`UserList`) | array of `User` |

## GET /api/v1/user/following

operationId: `userCurrentListFollowing`

List the users that the authenticated user is following

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | UserList (`UserList`) | array of `User` |

## GET /api/v1/user/following/{username}

operationId: `userCurrentCheckFollowing`

Check whether a user is followed by the authenticated user

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | yes | username of the user to check for authenticated followers |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PUT /api/v1/user/following/{username}

operationId: `userCurrentPutFollow`

Follow a user

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | yes | username of the user to follow |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/user/following/{username}

operationId: `userCurrentDeleteFollow`

Unfollow a user

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | yes | username of the user to unfollow |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/user/gpg_key_token

operationId: `getVerificationToken`

Get a Token to verify

| Response | Description | Body |
|---|---|---|
| 200 | APIString is a string response (`string`) | string |
| 401 | APIUnauthorizedError is an unauthorized error response (`unauthorized`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/user/gpg_key_verify

operationId: `userVerifyGPGKey`

Verify a GPG key

| Response | Description | Body |
|---|---|---|
| 201 | GPGKey (`GPGKey`) | `GPGKey` |
| 401 | APIUnauthorizedError is an unauthorized error response (`unauthorized`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/user/gpg_keys

operationId: `userCurrentListGPGKeys`

List the authenticated user's GPG keys

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | GPGKeyList (`GPGKeyList`) | array of `GPGKey` |
| 401 | APIUnauthorizedError is an unauthorized error response (`unauthorized`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |

## POST /api/v1/user/gpg_keys

operationId: `userCurrentPostGPGKey`

Create a GPG key

Request body (application/json): `CreateGPGKeyOption`

| Response | Description | Body |
|---|---|---|
| 201 | GPGKey (`GPGKey`) | `GPGKey` |
| 401 | APIUnauthorizedError is an unauthorized error response (`unauthorized`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/user/gpg_keys/{id}

operationId: `userCurrentGetGPGKey`

Get a GPG key

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | id of key to get |

| Response | Description | Body |
|---|---|---|
| 200 | GPGKey (`GPGKey`) | `GPGKey` |
| 401 | APIUnauthorizedError is an unauthorized error response (`unauthorized`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/user/gpg_keys/{id}

operationId: `userCurrentDeleteGPGKey`

Remove a GPG key

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | id of key to delete |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 401 | APIUnauthorizedError is an unauthorized error response (`unauthorized`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/user/hooks

operationId: `userListHooks`

List the authenticated user's webhooks

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | HookList (`HookList`) | array of `Hook` |

## POST /api/v1/user/hooks

operationId: `userCreateHook`

Create a hook

Request body (application/json): `CreateHookOption`

| Response | Description | Body |
|---|---|---|
| 201 | Hook (`Hook`) | `Hook` |

## GET /api/v1/user/hooks/{id}

operationId: `userGetHook`

Get a hook

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | id of the hook to get |

| Response | Description | Body |
|---|---|---|
| 200 | Hook (`Hook`) | `Hook` |

## PATCH /api/v1/user/hooks/{id}

operationId: `userEditHook`

Update a hook

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | id of the hook to update |

Request body (application/json): `EditHookOption`

| Response | Description | Body |
|---|---|---|
| 200 | Hook (`Hook`) | `Hook` |

## DELETE /api/v1/user/hooks/{id}

operationId: `userDeleteHook`

Delete a hook

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | id of the hook to delete |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |

## GET /api/v1/user/keys

operationId: `userCurrentListKeys`

List the authenticated user's public keys

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `fingerprint` | query | string |  | fingerprint of the key |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | PublicKeyList (`PublicKeyList`) | array of `PublicKey` |
| 401 | APIUnauthorizedError is an unauthorized error response (`unauthorized`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |

## POST /api/v1/user/keys

operationId: `userCurrentPostKey`

Create a public key

Request body (application/json): `CreateKeyOption`

| Response | Description | Body |
|---|---|---|
| 201 | PublicKey (`PublicKey`) | `PublicKey` |
| 401 | APIUnauthorizedError is an unauthorized error response (`unauthorized`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/user/keys/{id}

operationId: `userCurrentGetKey`

Get a public key

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | id of key to get |

| Response | Description | Body |
|---|---|---|
| 200 | PublicKey (`PublicKey`) | `PublicKey` |
| 401 | APIUnauthorizedError is an unauthorized error response (`unauthorized`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/user/keys/{id}

operationId: `userCurrentDeleteKey`

Delete a public key

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | id of key to delete |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 401 | APIUnauthorizedError is an unauthorized error response (`unauthorized`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/user/projects

operationId: `userCurrentListProjects`

List your projects

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `state` | query | string enum: open, closed, all |  | State of the project (open, closed, all) |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | ProjectList (`ProjectList`) | array of `Project` |

## POST /api/v1/user/projects

operationId: `userCurrentCreateProject`

Create a project owned by the authenticated user

Request body (application/json): `CreateProjectOption`

| Response | Description | Body |
|---|---|---|
| 201 | Project (`Project`) | `Project` |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/user/projects/{id}

operationId: `userCurrentGetProject`

Get a project

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | id of the project |

| Response | Description | Body |
|---|---|---|
| 200 | Project (`Project`) | `Project` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PATCH /api/v1/user/projects/{id}

operationId: `userCurrentEditProject`

Edit a project

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | id of the project |

Request body (application/json): `EditProjectOption`

| Response | Description | Body |
|---|---|---|
| 200 | Project (`Project`) | `Project` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## DELETE /api/v1/user/projects/{id}

operationId: `userCurrentDeleteProject`

Delete a project

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | id of the project |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/user/projects/{id}/columns

operationId: `userCurrentListProjectColumns`

List a project's columns

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | id of the project |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | ProjectColumnList (`ProjectColumnList`) | array of `ProjectColumn` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/user/projects/{id}/columns

operationId: `userCurrentCreateProjectColumn`

Create a column in a project

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | id of the project |

Request body (application/json): `CreateProjectColumnOption`

| Response | Description | Body |
|---|---|---|
| 201 | ProjectColumn (`ProjectColumn`) | `ProjectColumn` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## POST /api/v1/user/projects/{id}/columns/move

operationId: `userCurrentMoveProjectColumns`

Reorder a project's columns

Reorders every column of the project at once. The body lists all column IDs in their new order.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | id of the project |

Request body (application/json): `MoveProjectColumnsOption`

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/user/projects/{id}/columns/{column_id}

operationId: `userCurrentGetProjectColumn`

Get a project column

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | id of the project |
| `column_id` | path | integer (int64) | yes | id of the column |

| Response | Description | Body |
|---|---|---|
| 200 | ProjectColumn (`ProjectColumn`) | `ProjectColumn` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PATCH /api/v1/user/projects/{id}/columns/{column_id}

operationId: `userCurrentEditProjectColumn`

Edit a project column

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | id of the project |
| `column_id` | path | integer (int64) | yes | id of the column |

Request body (application/json): `EditProjectColumnOption`

| Response | Description | Body |
|---|---|---|
| 200 | ProjectColumn (`ProjectColumn`) | `ProjectColumn` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## DELETE /api/v1/user/projects/{id}/columns/{column_id}

operationId: `userCurrentDeleteProjectColumn`

Delete a project column

The default column cannot be deleted while it is still the column new issues land in.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | id of the project |
| `column_id` | path | integer (int64) | yes | id of the column |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## POST /api/v1/user/projects/{id}/columns/{column_id}/default

operationId: `userCurrentSetDefaultProjectColumn`

Set a project's default column

The default column is where newly assigned issues land.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | id of the project |
| `column_id` | path | integer (int64) | yes | id of the column |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/user/projects/{id}/columns/{column_id}/issues

operationId: `userCurrentListProjectColumnIssues`

List the issues in a project column

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | id of the project |
| `column_id` | path | integer (int64) | yes | id of the column |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | IssueList (`IssueList`) | array of `Issue` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/user/projects/{id}/columns/{column_id}/issues/{issue_id}

operationId: `userCurrentAddIssueToProjectColumn`

Add an issue to a project column

Assigns the issue to the project if it is not a member yet, then places it in the column.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | id of the project |
| `column_id` | path | integer (int64) | yes | id of the column |
| `issue_id` | path | integer (int64) | yes | global id of the issue, not the repository-local index |

| Response | Description | Body |
|---|---|---|
| 201 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## DELETE /api/v1/user/projects/{id}/columns/{column_id}/issues/{issue_id}

operationId: `userCurrentRemoveIssueFromProjectColumn`

Remove an issue from a project column

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | id of the project |
| `column_id` | path | integer (int64) | yes | id of the column |
| `issue_id` | path | integer (int64) | yes | global id of the issue, not the repository-local index |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## POST /api/v1/user/projects/{id}/issues/{issue_id}/move

operationId: `userCurrentMoveProjectIssue`

Move an issue between a project's columns

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | id of the project |
| `issue_id` | path | integer (int64) | yes | global id of the issue, not the repository-local index |

Request body (application/json): `MoveProjectIssueOption`

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## GET /api/v1/user/repos

operationId: `userCurrentListRepos`

List the repos that the authenticated user owns

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | RepositoryList (`RepositoryList`) | array of `Repository` |

## POST /api/v1/user/repos

operationId: `createCurrentUserRepo`

Create a repository

Request body (application/json): `CreateRepoOption`

| Response | Description | Body |
|---|---|---|
| 201 | Repository (`Repository`) | `Repository` |
| 400 | APIError is error format response (`error`) |  |
| 409 | The repository with the same name already exists. |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/user/settings

operationId: `getUserSettings`

Get user settings

| Response | Description | Body |
|---|---|---|
| 200 | UserSettings (`UserSettings`) | `UserSettings` |

## PATCH /api/v1/user/settings

operationId: `updateUserSettings`

Update user settings

Request body (application/json): `UserSettingsOptions`

| Response | Description | Body |
|---|---|---|
| 200 | UserSettings (`UserSettings`) | `UserSettings` |

## GET /api/v1/user/starred

operationId: `userCurrentListStarred`

The repos that the authenticated user has starred

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | RepositoryList (`RepositoryList`) | array of `Repository` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |

## GET /api/v1/user/starred/{owner}/{repo}

operationId: `userCurrentCheckStarring`

Whether the authenticated is starring the repo

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PUT /api/v1/user/starred/{owner}/{repo}

operationId: `userCurrentPutStar`

Star the given repo

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo to star |
| `repo` | path | string | yes | name of the repo to star |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/user/starred/{owner}/{repo}

operationId: `userCurrentDeleteStar`

Unstar the given repo

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo to unstar |
| `repo` | path | string | yes | name of the repo to unstar |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/user/stopwatches

operationId: `userGetStopWatches`

Get list of all existing stopwatches

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | StopWatchList (`StopWatchList`) | array of `StopWatch` |

## GET /api/v1/user/subscriptions

operationId: `userCurrentListSubscriptions`

List repositories watched by the authenticated user

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | RepositoryList (`RepositoryList`) | array of `Repository` |

## GET /api/v1/user/teams

operationId: `userListTeams`

List all the teams a user belongs to

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | TeamList (`TeamList`) | array of `Team` |

## GET /api/v1/user/times

operationId: `userCurrentTrackedTimes`

List the current user's tracked times

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |
| `since` | query | string (date-time) |  | Only show times updated after the given time. This is a timestamp in RFC 3339 format |
| `before` | query | string (date-time) |  | Only show times updated before the given time. This is a timestamp in RFC 3339 format |

| Response | Description | Body |
|---|---|---|
| 200 | TrackedTimeList (`TrackedTimeList`) | array of `TrackedTime` |

## GET /api/v1/users/search

operationId: `userSearch`

Search for users

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `q` | query | string |  | keyword |
| `uid` | query | integer (int64) |  | ID of the user to search for |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | SearchResults of a successful search | object |

## GET /api/v1/users/{username}

operationId: `userGet`

Get a user

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | yes | username of the user whose data is to be listed |

| Response | Description | Body |
|---|---|---|
| 200 | User (`User`) | `User` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/users/{username}/activities/feeds

operationId: `userListActivityFeeds`

List a user's activity feeds

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | yes | username of the user whose activity feeds are to be listed |
| `only-performed-by` | query | boolean |  | if true, only show actions performed by the requested user |
| `date` | query | string (date) |  | the date of the activities to be found |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | ActivityFeedsList (`ActivityFeedsList`) | array of `Activity` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/users/{username}/followers

operationId: `userListFollowers`

List the given user's followers

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | yes | username of the user whose followers are to be listed |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | UserList (`UserList`) | array of `User` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/users/{username}/following

operationId: `userListFollowing`

List the users that the given user is following

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | yes | username of the user whose followed users are to be listed |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | UserList (`UserList`) | array of `User` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/users/{username}/following/{target}

operationId: `userCheckFollowing`

Check if one user is following another user

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | yes | username of the following user |
| `target` | path | string | yes | username of the followed user |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/users/{username}/gpg_keys

operationId: `userListGPGKeys`

List the given user's GPG keys

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | yes | username of the user whose GPG key list is to be obtained |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | GPGKeyList (`GPGKeyList`) | array of `GPGKey` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/users/{username}/heatmap

operationId: `userGetHeatmapData`

Get a user's heatmap

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | yes | username of the user whose heatmap is to be obtained |

| Response | Description | Body |
|---|---|---|
| 200 | UserHeatmapData (`UserHeatmapData`) | array of `UserHeatmapData` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/users/{username}/keys

operationId: `userListKeys`

List the given user's public keys

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | yes | username of the user whose public keys are to be listed |
| `fingerprint` | query | string |  | fingerprint of the key |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | PublicKeyList (`PublicKeyList`) | array of `PublicKey` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/users/{username}/projects

operationId: `userListProjects`

List a user's projects

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | yes | username of the user |
| `state` | query | string enum: open, closed, all |  | State of the project (open, closed, all) |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | ProjectList (`ProjectList`) | array of `Project` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/users/{username}/repos

operationId: `userListRepos`

List the repos owned by the given user

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | yes | username of the user whose owned repos are to be listed |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | RepositoryList (`RepositoryList`) | array of `Repository` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/users/{username}/starred

operationId: `userListStarred`

The repos that the given user has starred

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | yes | username of the user whose starred repos are to be listed |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | RepositoryList (`RepositoryList`) | array of `Repository` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/users/{username}/subscriptions

operationId: `userListSubscriptions`

List the repositories watched by a user

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | yes | username of the user whose watched repos are to be listed |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | RepositoryList (`RepositoryList`) | array of `Repository` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/users/{username}/tokens

operationId: `userGetTokens`

List the authenticated user's access tokens

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | yes | username of to user whose access tokens are to be listed |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | AccessTokenList represents a list of API access token. (`AccessTokenList`) | array of `AccessToken` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |

## POST /api/v1/users/{username}/tokens

operationId: `userCreateToken`

Create an access token

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | yes | username of the user whose token is to be created |

Request body (application/json): `CreateAccessTokenOption`

| Response | Description | Body |
|---|---|---|
| 201 | AccessToken represents an API access token. (`AccessToken`) | `AccessToken` |
| 400 | APIError is error format response (`error`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |

## DELETE /api/v1/users/{username}/tokens/{token}

operationId: `userDeleteAccessToken`

delete an access token

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | yes | username of the user whose token is to be deleted |
| `token` | path | string | yes | token to be deleted, identified by ID and if not available by name |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIError is error format response (`error`) |  |
