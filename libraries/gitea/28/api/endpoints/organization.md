# Gitea API 28.3.0 — organization

## POST /api/v1/org/{org}/repos

operationId: `createOrgRepoDeprecated`
**DEPRECATED**

Create a repository in an organization

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of organization |

Request body (application/json): `CreateRepoOption`

| Response | Description | Body |
|---|---|---|
| 201 | Repository (`Repository`) | `Repository` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/orgs

operationId: `orgGetAll`

Get list of organizations

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | OrganizationList (`OrganizationList`) | array of `Organization` |

## POST /api/v1/orgs

operationId: `orgCreate`

Create an organization

Request body (application/json): `CreateOrgOption`

| Response | Description | Body |
|---|---|---|
| 201 | Organization (`Organization`) | `Organization` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/orgs/{org}

operationId: `orgGet`

Get an organization

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization to get |

| Response | Description | Body |
|---|---|---|
| 200 | Organization (`Organization`) | `Organization` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PATCH /api/v1/orgs/{org}

operationId: `orgEdit`

Edit an organization

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization to edit |

Request body (application/json): `EditOrgOption`

| Response | Description | Body |
|---|---|---|
| 200 | Organization (`Organization`) | `Organization` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/orgs/{org}

operationId: `orgDelete`

Delete an organization

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | organization that is to be deleted |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/orgs/{org}/actions/jobs

operationId: `getOrgWorkflowJobs`

Get org-level workflow jobs

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `status` | query | string |  | workflow status (requested, pending, queued, in_progress, failure, success, skipped) |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | WorkflowJobsList (`WorkflowJobsList`) | `ActionWorkflowJobsResponse` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/orgs/{org}/actions/runners

operationId: `getOrgRunners`

Get org-level runners

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `disabled` | query | boolean |  | filter by disabled status (true or false) |

| Response | Description | Body |
|---|---|---|
| 200 | RunnerList (`RunnerList`) | `ActionRunnersResponse` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/orgs/{org}/actions/runners/registration-token

operationId: `orgCreateRunnerRegistrationToken`

Get an organization's actions runner registration token

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |

| Response | Description | Body |
|---|---|---|
| 200 | RegistrationToken is response related to registration token (`RegistrationToken`) |  |

## GET /api/v1/orgs/{org}/actions/runners/{runner_id}

operationId: `getOrgRunner`

Get an org-level runner

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `runner_id` | path | string | yes | id of the runner |

| Response | Description | Body |
|---|---|---|
| 200 | Runner (`Runner`) | `ActionRunner` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PATCH /api/v1/orgs/{org}/actions/runners/{runner_id}

operationId: `updateOrgRunner`

Update an org-level runner

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `runner_id` | path | string | yes | id of the runner |

Request body (application/json): `EditActionRunnerOption`

| Response | Description | Body |
|---|---|---|
| 200 | Runner (`Runner`) | `ActionRunner` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## DELETE /api/v1/orgs/{org}/actions/runners/{runner_id}

operationId: `deleteOrgRunner`

Delete an org-level runner

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `runner_id` | path | string | yes | id of the runner |

| Response | Description | Body |
|---|---|---|
| 204 | runner has been deleted |  |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/orgs/{org}/actions/runs

operationId: `getOrgWorkflowRuns`

Get org-level workflow runs

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
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

## GET /api/v1/orgs/{org}/actions/secrets

operationId: `orgListActionsSecrets`

List an organization's actions secrets

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | SecretList (`SecretList`) | array of `Secret` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PUT /api/v1/orgs/{org}/actions/secrets/{secretname}

operationId: `updateOrgSecret`

Create or Update a secret value in an organization

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of organization |
| `secretname` | path | string | yes | name of the secret |

Request body (application/json): `CreateOrUpdateSecretOption`

| Response | Description | Body |
|---|---|---|
| 201 | response when creating a secret |  |
| 204 | response when updating a secret |  |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/orgs/{org}/actions/secrets/{secretname}

operationId: `deleteOrgSecret`

Delete a secret in an organization

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of organization |
| `secretname` | path | string | yes | name of the secret |

| Response | Description | Body |
|---|---|---|
| 204 | delete one secret of the organization |  |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/orgs/{org}/actions/variables

operationId: `getOrgVariablesList`

Get an org-level variables list

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | VariableList (`VariableList`) | array of `ActionVariable` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/orgs/{org}/actions/variables/{variablename}

operationId: `getOrgVariable`

Get an org-level variable

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `variablename` | path | string | yes | name of the variable |

| Response | Description | Body |
|---|---|---|
| 200 | ActionVariable (`ActionVariable`) | `ActionVariable` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/orgs/{org}/actions/variables/{variablename}

operationId: `createOrgVariable`

Create an org-level variable

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `variablename` | path | string | yes | name of the variable |

Request body (application/json): `CreateVariableOption`

| Response | Description | Body |
|---|---|---|
| 201 | successfully created the org-level variable |  |
| 400 | APIError is error format response (`error`) |  |
| 409 | variable name already exists. |  |
| 500 | APIError is error format response (`error`) |  |

## PUT /api/v1/orgs/{org}/actions/variables/{variablename}

operationId: `updateOrgVariable`

Update an org-level variable

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `variablename` | path | string | yes | name of the variable |

Request body (application/json): `UpdateVariableOption`

| Response | Description | Body |
|---|---|---|
| 201 | response when updating an org-level variable |  |
| 204 | response when updating an org-level variable |  |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/orgs/{org}/actions/variables/{variablename}

operationId: `deleteOrgVariable`

Delete an org-level variable

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `variablename` | path | string | yes | name of the variable |

| Response | Description | Body |
|---|---|---|
| 200 | ActionVariable (`ActionVariable`) | `ActionVariable` |
| 201 | response when deleting a variable |  |
| 204 | response when deleting a variable |  |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/orgs/{org}/activities/feeds

operationId: `orgListActivityFeeds`

List an organization's activity feeds

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the org |
| `date` | query | string (date) |  | the date of the activities to be found |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | ActivityFeedsList (`ActivityFeedsList`) | array of `Activity` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/orgs/{org}/avatar

operationId: `orgUpdateAvatar`

Update Avatar

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |

Request body (application/json): `UpdateUserAvatarOption`

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/orgs/{org}/avatar

operationId: `orgDeleteAvatar`

Delete Avatar

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/orgs/{org}/blocks

operationId: `organizationListBlocks`

List users blocked by the organization

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | UserList (`UserList`) | array of `User` |

## GET /api/v1/orgs/{org}/blocks/{username}

operationId: `organizationCheckUserBlock`

Check if a user is blocked by the organization

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `username` | path | string | yes | username of the user to check |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PUT /api/v1/orgs/{org}/blocks/{username}

operationId: `organizationBlockUser`

Block a user

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `username` | path | string | yes | username of the user to block |
| `note` | query | string |  | optional note for the block |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## DELETE /api/v1/orgs/{org}/blocks/{username}

operationId: `organizationUnblockUser`

Unblock a user

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `username` | path | string | yes | username of the user to unblock |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/orgs/{org}/hooks

operationId: `orgListHooks`

List an organization's webhooks

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | HookList (`HookList`) | array of `Hook` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/orgs/{org}/hooks

operationId: `orgCreateHook`

Create a hook

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |

Request body (application/json): `CreateHookOption`

| Response | Description | Body |
|---|---|---|
| 201 | Hook (`Hook`) | `Hook` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/orgs/{org}/hooks/{id}

operationId: `orgGetHook`

Get a hook

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `id` | path | integer (int64) | yes | id of the hook to get |

| Response | Description | Body |
|---|---|---|
| 200 | Hook (`Hook`) | `Hook` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PATCH /api/v1/orgs/{org}/hooks/{id}

operationId: `orgEditHook`

Update a hook

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `id` | path | integer (int64) | yes | id of the hook to update |

Request body (application/json): `EditHookOption`

| Response | Description | Body |
|---|---|---|
| 200 | Hook (`Hook`) | `Hook` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/orgs/{org}/hooks/{id}

operationId: `orgDeleteHook`

Delete a hook

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `id` | path | integer (int64) | yes | id of the hook to delete |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/orgs/{org}/labels

operationId: `orgListLabels`

List an organization's labels

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | LabelList (`LabelList`) | array of `Label` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/orgs/{org}/labels

operationId: `orgCreateLabel`

Create a label for an organization

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |

Request body (application/json): `CreateLabelOption`

| Response | Description | Body |
|---|---|---|
| 201 | Label (`Label`) | `Label` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/orgs/{org}/labels/{id}

operationId: `orgGetLabel`

Get a single label

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `id` | path | integer (int64) | yes | id of the label to get |

| Response | Description | Body |
|---|---|---|
| 200 | Label (`Label`) | `Label` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PATCH /api/v1/orgs/{org}/labels/{id}

operationId: `orgEditLabel`

Update a label

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `id` | path | integer (int64) | yes | id of the label to edit |

Request body (application/json): `EditLabelOption`

| Response | Description | Body |
|---|---|---|
| 200 | Label (`Label`) | `Label` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## DELETE /api/v1/orgs/{org}/labels/{id}

operationId: `orgDeleteLabel`

Delete a label

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `id` | path | integer (int64) | yes | id of the label to delete |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/orgs/{org}/members

operationId: `orgListMembers`

List an organization's members

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | UserList (`UserList`) | array of `User` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/orgs/{org}/members/{username}

operationId: `orgIsMember`

Check if a user is a member of an organization

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `username` | path | string | yes | username of the user to check for an organization membership |

| Response | Description | Body |
|---|---|---|
| 204 | user is a member |  |
| 303 | redirection to /orgs/{org}/public_members/{username} |  |
| 404 | user is not a member |  |

## DELETE /api/v1/orgs/{org}/members/{username}

operationId: `orgDeleteMember`

Remove a member from an organization

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `username` | path | string | yes | username of the user to remove from the organization |

| Response | Description | Body |
|---|---|---|
| 204 | member removed |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/orgs/{org}/projects

operationId: `orgListProjects`

List an organization's projects

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `state` | query | string enum: open, closed, all |  | State of the project (open, closed, all) |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | ProjectList (`ProjectList`) | array of `Project` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/orgs/{org}/projects

operationId: `orgCreateProject`

Create a project owned by an organization

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |

Request body (application/json): `CreateProjectOption`

| Response | Description | Body |
|---|---|---|
| 201 | Project (`Project`) | `Project` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/orgs/{org}/projects/{id}

operationId: `orgGetProject`

Get a project

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `id` | path | integer (int64) | yes | id of the project |

| Response | Description | Body |
|---|---|---|
| 200 | Project (`Project`) | `Project` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PATCH /api/v1/orgs/{org}/projects/{id}

operationId: `orgEditProject`

Edit a project

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `id` | path | integer (int64) | yes | id of the project |

Request body (application/json): `EditProjectOption`

| Response | Description | Body |
|---|---|---|
| 200 | Project (`Project`) | `Project` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## DELETE /api/v1/orgs/{org}/projects/{id}

operationId: `orgDeleteProject`

Delete a project

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `id` | path | integer (int64) | yes | id of the project |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/orgs/{org}/projects/{id}/columns

operationId: `orgListProjectColumns`

List a project's columns

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `id` | path | integer (int64) | yes | id of the project |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | ProjectColumnList (`ProjectColumnList`) | array of `ProjectColumn` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/orgs/{org}/projects/{id}/columns

operationId: `orgCreateProjectColumn`

Create a column in a project

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `id` | path | integer (int64) | yes | id of the project |

Request body (application/json): `CreateProjectColumnOption`

| Response | Description | Body |
|---|---|---|
| 201 | ProjectColumn (`ProjectColumn`) | `ProjectColumn` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## POST /api/v1/orgs/{org}/projects/{id}/columns/move

operationId: `orgMoveProjectColumns`

Reorder a project's columns

Reorders every column of the project at once. The body lists all column IDs in their new order.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `id` | path | integer (int64) | yes | id of the project |

Request body (application/json): `MoveProjectColumnsOption`

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/orgs/{org}/projects/{id}/columns/{column_id}

operationId: `orgGetProjectColumn`

Get a project column

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `id` | path | integer (int64) | yes | id of the project |
| `column_id` | path | integer (int64) | yes | id of the column |

| Response | Description | Body |
|---|---|---|
| 200 | ProjectColumn (`ProjectColumn`) | `ProjectColumn` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PATCH /api/v1/orgs/{org}/projects/{id}/columns/{column_id}

operationId: `orgEditProjectColumn`

Edit a project column

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `id` | path | integer (int64) | yes | id of the project |
| `column_id` | path | integer (int64) | yes | id of the column |

Request body (application/json): `EditProjectColumnOption`

| Response | Description | Body |
|---|---|---|
| 200 | ProjectColumn (`ProjectColumn`) | `ProjectColumn` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## DELETE /api/v1/orgs/{org}/projects/{id}/columns/{column_id}

operationId: `orgDeleteProjectColumn`

Delete a project column

The default column cannot be deleted while it is still the column new issues land in.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `id` | path | integer (int64) | yes | id of the project |
| `column_id` | path | integer (int64) | yes | id of the column |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## POST /api/v1/orgs/{org}/projects/{id}/columns/{column_id}/default

operationId: `orgSetDefaultProjectColumn`

Set a project's default column

The default column is where newly assigned issues land.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `id` | path | integer (int64) | yes | id of the project |
| `column_id` | path | integer (int64) | yes | id of the column |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/orgs/{org}/projects/{id}/columns/{column_id}/issues

operationId: `orgListProjectColumnIssues`

List the issues in a project column

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `id` | path | integer (int64) | yes | id of the project |
| `column_id` | path | integer (int64) | yes | id of the column |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | IssueList (`IssueList`) | array of `Issue` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/orgs/{org}/projects/{id}/columns/{column_id}/issues/{issue_id}

operationId: `orgAddIssueToProjectColumn`

Add an issue to a project column

Assigns the issue to the project if it is not a member yet, then places it in the column.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
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

## DELETE /api/v1/orgs/{org}/projects/{id}/columns/{column_id}/issues/{issue_id}

operationId: `orgRemoveIssueFromProjectColumn`

Remove an issue from a project column

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `id` | path | integer (int64) | yes | id of the project |
| `column_id` | path | integer (int64) | yes | id of the column |
| `issue_id` | path | integer (int64) | yes | global id of the issue, not the repository-local index |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## POST /api/v1/orgs/{org}/projects/{id}/issues/{issue_id}/move

operationId: `orgMoveProjectIssue`

Move an issue between a project's columns

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
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

## GET /api/v1/orgs/{org}/public_members

operationId: `orgListPublicMembers`

List an organization's public members

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | UserList (`UserList`) | array of `User` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/orgs/{org}/public_members/{username}

operationId: `orgIsPublicMember`

Check if a user is a public member of an organization

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `username` | path | string | yes | username of the user to check for a public organization membership |

| Response | Description | Body |
|---|---|---|
| 204 | user is a public member |  |
| 404 | user is not a public member |  |

## PUT /api/v1/orgs/{org}/public_members/{username}

operationId: `orgPublicizeMember`

Publicize a user's membership

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `username` | path | string | yes | username of the user whose membership is to be publicized |

| Response | Description | Body |
|---|---|---|
| 204 | membership publicized |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/orgs/{org}/public_members/{username}

operationId: `orgConcealMember`

Conceal a user's membership

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `username` | path | string | yes | username of the user whose membership is to be concealed |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/orgs/{org}/rename

operationId: `renameOrg`

Rename an organization

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | existing org name |

Request body (application/json): `RenameOrgOption`

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/orgs/{org}/repos

operationId: `orgListRepos`

List an organization's repos

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | RepositoryList (`RepositoryList`) | array of `Repository` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/orgs/{org}/repos

operationId: `createOrgRepo`

Create a repository in an organization

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of organization |

Request body (application/json): `CreateRepoOption`

| Response | Description | Body |
|---|---|---|
| 201 | Repository (`Repository`) | `Repository` |
| 400 | APIError is error format response (`error`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/orgs/{org}/repos

operationId: `orgDeleteRepos`

Delete all repositories in an organization

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |

| Response | Description | Body |
|---|---|---|
| 202 | APIEmpty is an empty response (`empty`) |  |
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/orgs/{org}/teams

operationId: `orgListTeams`

List an organization's teams

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | TeamList (`TeamList`) | array of `Team` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/orgs/{org}/teams

operationId: `orgCreateTeam`

Create a team

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |

Request body (application/json): `CreateTeamOption`

| Response | Description | Body |
|---|---|---|
| 201 | Team (`Team`) | `Team` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/orgs/{org}/teams/search

operationId: `teamSearch`

Search for teams within an organization

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org` | path | string | yes | name of the organization |
| `q` | query | string |  | keywords to search |
| `include_desc` | query | boolean |  | include search within team description (defaults to true) |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | SearchResults of a successful search | object |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/teams/{id}

operationId: `orgGetTeam`

Get a team

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | id of the team to get |

| Response | Description | Body |
|---|---|---|
| 200 | Team (`Team`) | `Team` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PATCH /api/v1/teams/{id}

operationId: `orgEditTeam`

Edit a team

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | yes | id of the team to edit |

Request body (application/json): `EditTeamOption`

| Response | Description | Body |
|---|---|---|
| 200 | Team (`Team`) | `Team` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/teams/{id}

operationId: `orgDeleteTeam`

Delete a team

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | id of the team to delete |

| Response | Description | Body |
|---|---|---|
| 204 | team deleted |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/teams/{id}/activities/feeds

operationId: `orgListTeamActivityFeeds`

List a team's activity feeds

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | id of the team |
| `date` | query | string (date) |  | the date of the activities to be found |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | ActivityFeedsList (`ActivityFeedsList`) | array of `Activity` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/teams/{id}/members

operationId: `orgListTeamMembers`

List a team's members

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | id of the team |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | UserList (`UserList`) | array of `User` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/teams/{id}/members/{username}

operationId: `orgListTeamMember`

List a particular member of team

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | id of the team |
| `username` | path | string | yes | username of the user whose data is to be listed |

| Response | Description | Body |
|---|---|---|
| 200 | User (`User`) | `User` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PUT /api/v1/teams/{id}/members/{username}

operationId: `orgAddTeamMember`

Add a team member

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | id of the team |
| `username` | path | string | yes | username of the user to add to a team |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/teams/{id}/members/{username}

operationId: `orgRemoveTeamMember`

Remove a team member

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | id of the team |
| `username` | path | string | yes | username of the user to remove from a team |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/teams/{id}/repos

operationId: `orgListTeamRepos`

List a team's repos

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | id of the team |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | RepositoryList (`RepositoryList`) | array of `Repository` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/teams/{id}/repos/{org}/{repo}

operationId: `orgListTeamRepo`

List a particular repo of team

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | id of the team |
| `org` | path | string | yes | organization that owns the repo to list |
| `repo` | path | string | yes | name of the repo to list |

| Response | Description | Body |
|---|---|---|
| 200 | Repository (`Repository`) | `Repository` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PUT /api/v1/teams/{id}/repos/{org}/{repo}

operationId: `orgAddTeamRepository`

Add a repository to a team

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | id of the team |
| `org` | path | string | yes | organization that owns the repo to add |
| `repo` | path | string | yes | name of the repo to add |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/teams/{id}/repos/{org}/{repo}

operationId: `orgRemoveTeamRepository`

Remove a repository from a team

This does not delete the repository, it only removes the repository from the team.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | id of the team |
| `org` | path | string | yes | organization that owns the repo to remove |
| `repo` | path | string | yes | name of the repo to remove |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/user/orgs

operationId: `orgListCurrentUserOrgs`

List the current user's organizations

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | OrganizationList (`OrganizationList`) | array of `Organization` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/users/{username}/orgs

operationId: `orgListUserOrgs`

List a user's organizations

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | yes | username of the user whose organizations are to be listed |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | OrganizationList (`OrganizationList`) | array of `Organization` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/users/{username}/orgs/{org}/permissions

operationId: `orgGetUserPermissions`

Get user permissions in organization

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `username` | path | string | yes | username of the user whose permissions are to be obtained |
| `org` | path | string | yes | name of the organization |

| Response | Description | Body |
|---|---|---|
| 200 | OrganizationPermissions (`OrganizationPermissions`) | `OrganizationPermissions` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
