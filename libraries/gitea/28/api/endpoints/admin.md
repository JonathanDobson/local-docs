# Gitea API 28.3.0 — admin

## GET /api/v1/admin/actions/jobs

operationId: `listAdminWorkflowJobs`

Lists all jobs

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

## GET /api/v1/admin/actions/runners

operationId: `getAdminRunners`

Get all runners

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `disabled` | query | boolean |  | filter by disabled status (true or false) |

| Response | Description | Body |
|---|---|---|
| 200 | RunnerList (`RunnerList`) | `ActionRunnersResponse` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/admin/actions/runners/registration-token

operationId: `adminCreateRunnerRegistrationToken`

Get a global actions runner registration token

| Response | Description | Body |
|---|---|---|
| 200 | RegistrationToken is response related to registration token (`RegistrationToken`) |  |

## GET /api/v1/admin/actions/runners/{runner_id}

operationId: `getAdminRunner`

Get a global runner

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `runner_id` | path | string | yes | id of the runner |

| Response | Description | Body |
|---|---|---|
| 200 | Runner (`Runner`) | `ActionRunner` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PATCH /api/v1/admin/actions/runners/{runner_id}

operationId: `updateAdminRunner`

Update a global runner

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

## DELETE /api/v1/admin/actions/runners/{runner_id}

operationId: `deleteAdminRunner`

Delete a global runner

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `runner_id` | path | string | yes | id of the runner |

| Response | Description | Body |
|---|---|---|
| 204 | runner has been deleted |  |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/admin/actions/runs

operationId: `listAdminWorkflowRuns`

Lists all runs

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

## GET /api/v1/admin/cron

operationId: `adminCronList`

List cron tasks

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | CronList (`CronList`) | array of `Cron` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |

## POST /api/v1/admin/cron/{task}

operationId: `adminCronRun`

Run cron task

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `task` | path | string | yes | task to run |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/admin/emails

operationId: `adminGetAllEmails`

List all emails

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | EmailList (`EmailList`) | array of `Email` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |

## GET /api/v1/admin/emails/search

operationId: `adminSearchEmails`

Search all emails

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `q` | query | string |  | keyword |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | EmailList (`EmailList`) | array of `Email` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |

## GET /api/v1/admin/hooks

operationId: `adminListHooks`

List system's webhooks

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |
| `type` | query | string enum: system, default, all |  | system, default or both kinds of webhooks |

| Response | Description | Body |
|---|---|---|
| 200 | HookList (`HookList`) | array of `Hook` |

## POST /api/v1/admin/hooks

operationId: `adminCreateHook`

Create a hook

Request body (application/json): `CreateHookOption`

| Response | Description | Body |
|---|---|---|
| 201 | Hook (`Hook`) | `Hook` |

## GET /api/v1/admin/hooks/{id}

operationId: `adminGetHook`

Get a hook

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | id of the hook to get |

| Response | Description | Body |
|---|---|---|
| 200 | Hook (`Hook`) | `Hook` |

## PATCH /api/v1/admin/hooks/{id}

operationId: `adminEditHook`

Update a hook

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | id of the hook to update |

Request body (application/json): `EditHookOption`

| Response | Description | Body |
|---|---|---|
| 200 | Hook (`Hook`) | `Hook` |

## DELETE /api/v1/admin/hooks/{id}

operationId: `adminDeleteHook`

Delete a hook

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | id of the hook to delete |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |

## GET /api/v1/admin/orgs

operationId: `adminGetAllOrgs`

List all organizations

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | OrganizationList (`OrganizationList`) | array of `Organization` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |

## GET /api/v1/admin/packages

operationId: `adminListPackages`

List all packages

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |
| `type` | query | string enum: alpine, cargo, chef, composer, conan, conda, container, cran, debian, generic, go, helm |  | package type filter |
| `q` | query | string |  | name filter |

| Response | Description | Body |
|---|---|---|
| 200 | PackageList (`PackageList`) | array of `Package` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |

## GET /api/v1/admin/unadopted

operationId: `adminUnadoptedList`

List unadopted repositories

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |
| `query` | query | string |  | glob pattern of repositories to search for, in the form owner or owner/repo |

| Response | Description | Body |
|---|---|---|
| 200 | StringSlice (`StringSlice`) | array of string |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |

## POST /api/v1/admin/unadopted/{owner}/{repo}

operationId: `adminAdoptRepository`

Adopt unadopted files as a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/admin/unadopted/{owner}/{repo}

operationId: `adminDeleteUnadoptedRepository`

Delete unadopted files

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |

## GET /api/v1/admin/users

operationId: `adminSearchUsers`

Search users according filter conditions

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `source_id` | query | integer (int64) |  | ID of the user's login source to search for |
| `login_name` | query | string |  | identifier of the user, provided by the external authenticator |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |
| `sort` | query | string |  | sort users by attribute. Supported values are "name", "created", "updated" and "id". Default is "name" |
| `order` | query | string |  | sort order, either "asc" (ascending) or "desc" (descending). Default is "asc", ignored if "sort" is not specified. |
| `q` | query | string |  | search term (username, full name, email) |
| `visibility` | query | string |  | visibility filter. Supported values are "public", "limited" and "private". |
| `is_active` | query | boolean |  | filter active users |
| `is_admin` | query | boolean |  | filter admin users |
| `is_restricted` | query | boolean |  | filter restricted users |
| `is_2fa_enabled` | query | boolean |  | filter 2FA enabled users |
| `is_prohibit_login` | query | boolean |  | filter login prohibited users |

| Response | Description | Body |
|---|---|---|
| 200 | UserList (`UserList`) | array of `User` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## POST /api/v1/admin/users

operationId: `adminCreateUser`

Create a user

Request body (application/json): `CreateUserOption`

| Response | Description | Body |
|---|---|---|
| 201 | User (`User`) | `User` |
| 400 | APIError is error format response (`error`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 409 | APIError is error format response (`error`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## PATCH /api/v1/admin/users/{username}

operationId: `adminEditUser`

Edit an existing user

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | yes | username of the user whose data is to be edited |

Request body (application/json): `EditUserOption`

| Response | Description | Body |
|---|---|---|
| 200 | User (`User`) | `User` |
| 400 | APIError is error format response (`error`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 409 | APIError is error format response (`error`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## DELETE /api/v1/admin/users/{username}

operationId: `adminDeleteUser`

Delete a user

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | yes | username of the user to delete |
| `purge` | query | boolean |  | purge the user from the system completely |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/admin/users/{username}/badges

operationId: `adminListUserBadges`

List a user's badges

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | yes | username of the user whose badges are to be listed |

| Response | Description | Body |
|---|---|---|
| 200 | BadgeList (`BadgeList`) | array of `Badge` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/admin/users/{username}/badges

operationId: `adminAddUserBadges`

Add a badge to a user

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | yes | username of the user to whom a badge is to be added |

Request body (application/json): `UserBadgeOption`

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |

## DELETE /api/v1/admin/users/{username}/badges

operationId: `adminDeleteUserBadges`

Remove a badge from a user

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | yes | username of the user whose badge is to be deleted |

Request body (application/json): `UserBadgeOption`

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## POST /api/v1/admin/users/{username}/keys

operationId: `adminCreatePublicKey`

Add a public key on behalf of a user

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | yes | username of the user who is to receive a public key |

Request body (application/json): `CreateKeyOption`

| Response | Description | Body |
|---|---|---|
| 201 | PublicKey (`PublicKey`) | `PublicKey` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## DELETE /api/v1/admin/users/{username}/keys/{id}

operationId: `adminDeleteUserPublicKey`

Delete a user's public key

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | yes | username of the user whose public key is to be deleted |
| `id` | path | integer (int64) | yes | id of the key to delete |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/admin/users/{username}/orgs

operationId: `adminCreateOrg`

Create an organization

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | yes | username of the user who will own the created organization |

Request body (application/json): `CreateOrgOption`

| Response | Description | Body |
|---|---|---|
| 201 | Organization (`Organization`) | `Organization` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## POST /api/v1/admin/users/{username}/rename

operationId: `adminRenameUser`

Rename a user

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | yes | current username of the user |

Request body (application/json): `RenameUserOption`

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## POST /api/v1/admin/users/{username}/repos

operationId: `adminCreateRepo`

Create a repository on behalf of a user

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | yes | username of the user who will own the created repository |

Request body (application/json): `CreateRepoOption`

| Response | Description | Body |
|---|---|---|
| 201 | Repository (`Repository`) | `Repository` |
| 400 | APIError is error format response (`error`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 409 | APIError is error format response (`error`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |
