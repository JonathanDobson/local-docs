# Gitea API 28.3.0 — repository

## POST /api/v1/repos/migrate

operationId: `repoMigrate`

Migrate a remote git repository

Request body (application/json): `MigrateRepoOptions`

| Response | Description | Body |
|---|---|---|
| 201 | Repository (`Repository`) | `Repository` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 409 | The repository with the same name already exists. |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/repos/search

operationId: `repoSearch`

Search for repositories

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `q` | query | string |  | keyword |
| `topic` | query | boolean |  | Limit search to repositories with keyword as topic |
| `includeDesc` | query | boolean |  | include search of keyword within repository description |
| `uid` | query | integer (int64) |  | search only for repos that the user with the given id owns or contributes to |
| `priority_owner_id` | query | integer (int64) |  | repo owner to prioritize in the results |
| `team_id` | query | integer (int64) |  | search only for repos that belong to the given team id |
| `starredBy` | query | integer (int64) |  | search only for repos that the user with the given id has starred |
| `private` | query | boolean |  | include private repositories this user has access to (defaults to true) |
| `is_private` | query | boolean |  | show only pubic, private or all repositories (defaults to all) |
| `template` | query | boolean |  | include template repositories this user has access to (defaults to true) |
| `archived` | query | boolean |  | show only archived, non-archived or all repositories (defaults to all) |
| `mode` | query | string |  | type of repository to search for. Supported values are "fork", "source", "mirror" and "collaborative" |
| `exclusive` | query | boolean |  | if `uid` is given, search only for repos that the user owns |
| `sort` | query | string |  | sort repos by attribute. Supported values are "alpha", "created", "updated", "size", "git_size", "lfs_size", "stars", "forks" and "id". Default is "alpha" |
| `order` | query | string |  | sort order, either "asc" (ascending) or "desc" (descending). Default is "asc", ignored if "sort" is not specified. |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | SearchResults (`SearchResults`) | `SearchResults` |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/repos/{owner}/{repo}

operationId: `repoGet`

Get a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

| Response | Description | Body |
|---|---|---|
| 200 | Repository (`Repository`) | `Repository` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PATCH /api/v1/repos/{owner}/{repo}

operationId: `repoEdit`

Edit a repository's properties. Only fields that are set will be changed.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo to edit |
| `repo` | path | string | yes | name of the repo to edit |

Request body (application/json): `EditRepoOption`

| Response | Description | Body |
|---|---|---|
| 200 | Repository (`Repository`) | `Repository` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## DELETE /api/v1/repos/{owner}/{repo}

operationId: `repoDelete`

Delete a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo to delete |
| `repo` | path | string | yes | name of the repo to delete |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/actions/artifacts

operationId: `getArtifacts`

Lists all artifacts for a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repository |
| `name` | query | string |  | name of the artifact |

| Response | Description | Body |
|---|---|---|
| 200 | ArtifactsList (`ArtifactsList`) | `ActionArtifactsResponse` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/actions/artifacts/{artifact_id}

operationId: `getArtifact`

Gets a specific artifact for a workflow run

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repository |
| `artifact_id` | path | string | yes | id of the artifact |

| Response | Description | Body |
|---|---|---|
| 200 | Artifact (`Artifact`) | `ActionArtifact` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/actions/artifacts/{artifact_id}

operationId: `deleteArtifact`

Deletes a specific artifact for a workflow run

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repository |
| `artifact_id` | path | string | yes | id of the artifact |

| Response | Description | Body |
|---|---|---|
| 204 | No Content |  |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/actions/artifacts/{artifact_id}/zip

operationId: `downloadArtifact`

Downloads a specific artifact for a workflow run redirects to blob url

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repository |
| `artifact_id` | path | string | yes | id of the artifact |

| Response | Description | Body |
|---|---|---|
| 302 | redirect to the blob download |  |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/actions/jobs

operationId: `listWorkflowJobs`

Lists all jobs for a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repository |
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

## GET /api/v1/repos/{owner}/{repo}/actions/jobs/{job_id}

operationId: `getWorkflowJob`

Gets a specific workflow job for a workflow run

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repository |
| `job_id` | path | string | yes | id of the job |

| Response | Description | Body |
|---|---|---|
| 200 | WorkflowJob (`WorkflowJob`) | `ActionWorkflowJob` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/actions/jobs/{job_id}/logs

operationId: `downloadActionsRunJobLogs`

Downloads the job logs for a workflow run

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repository |
| `job_id` | path | integer | yes | id of the job |

| Response | Description | Body |
|---|---|---|
| 200 | output blob content |  |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/actions/runners

operationId: `getRepoRunners`

Get repo-level runners

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `disabled` | query | boolean |  | filter by disabled status (true or false) |

| Response | Description | Body |
|---|---|---|
| 200 | RunnerList (`RunnerList`) | `ActionRunnersResponse` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/actions/runners/registration-token

operationId: `repoCreateRunnerRegistrationToken`

Get a repository's actions runner registration token

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

| Response | Description | Body |
|---|---|---|
| 200 | RegistrationToken is response related to registration token (`RegistrationToken`) |  |

## GET /api/v1/repos/{owner}/{repo}/actions/runners/{runner_id}

operationId: `getRepoRunner`

Get a repo-level runner

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `runner_id` | path | string | yes | id of the runner |

| Response | Description | Body |
|---|---|---|
| 200 | Runner (`Runner`) | `ActionRunner` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PATCH /api/v1/repos/{owner}/{repo}/actions/runners/{runner_id}

operationId: `updateRepoRunner`

Update a repo-level runner

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `runner_id` | path | string | yes | id of the runner |

Request body (application/json): `EditActionRunnerOption`

| Response | Description | Body |
|---|---|---|
| 200 | Runner (`Runner`) | `ActionRunner` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/actions/runners/{runner_id}

operationId: `deleteRepoRunner`

Delete a repo-level runner

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `runner_id` | path | string | yes | id of the runner |

| Response | Description | Body |
|---|---|---|
| 204 | runner has been deleted |  |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/actions/runs

operationId: `getWorkflowRuns`

Lists all runs for a repository run

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repository |
| `event` | query | string |  | workflow event name |
| `branch` | query | string |  | workflow branch |
| `status` | query | string |  | workflow status (requested, pending, queued, in_progress, failure, success, skipped) |
| `actor` | query | string |  | triggered by user |
| `head_sha` | query | string |  | triggering sha of the workflow run |
| `exclude_pull_requests` | query | boolean |  | if true, the `pull_requests` field on each returned run is emptied |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | WorkflowRunsList (`WorkflowRunsList`) | `ActionWorkflowRunsResponse` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/actions/runs/{run}

operationId: `GetWorkflowRun`

Gets a specific workflow run

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repository |
| `run` | path | integer | yes | id of the run |

| Response | Description | Body |
|---|---|---|
| 200 | WorkflowRun (`WorkflowRun`) | `ActionWorkflowRun` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/actions/runs/{run}

operationId: `deleteActionRun`

Delete a workflow run

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repository |
| `run` | path | integer | yes | runid of the workflow run |

| Response | Description | Body |
|---|---|---|
| 204 | No Content |  |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/actions/runs/{run}/approve

operationId: `approveWorkflowRun`

Approve a workflow run that requires approval

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repository |
| `run` | path | integer | yes | run ID |

| Response | Description | Body |
|---|---|---|
| 200 | WorkflowRun (`WorkflowRun`) | `ActionWorkflowRun` |
| 400 | APIError is error format response (`error`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 409 | APIConflict is a conflict empty response (`conflict`) |  |

## GET /api/v1/repos/{owner}/{repo}/actions/runs/{run}/artifacts

operationId: `getArtifactsOfRun`

Lists all artifacts for a repository run

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repository |
| `run` | path | integer | yes | runid of the workflow run |
| `name` | query | string |  | name of the artifact |

| Response | Description | Body |
|---|---|---|
| 200 | ArtifactsList (`ArtifactsList`) | `ActionArtifactsResponse` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/actions/runs/{run}/attempts/{attempt}

operationId: `getWorkflowRunAttempt`

Gets a specific workflow run attempt

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repository |
| `run` | path | integer | yes | id of the run |
| `attempt` | path | integer | yes | logical attempt number of the run |

| Response | Description | Body |
|---|---|---|
| 200 | WorkflowRun (`WorkflowRun`) | `ActionWorkflowRun` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/actions/runs/{run}/attempts/{attempt}/jobs

operationId: `listWorkflowRunAttemptJobs`

Lists all jobs for a workflow run attempt

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repository |
| `run` | path | integer | yes | id of the workflow run |
| `attempt` | path | integer | yes | logical attempt number of the run |
| `status` | query | string |  | workflow status (requested, pending, queued, in_progress, failure, success, skipped) |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | WorkflowJobsList (`WorkflowJobsList`) | `ActionWorkflowJobsResponse` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/actions/runs/{run}/cancel

operationId: `cancelWorkflowRun`

Cancel a workflow run and its jobs

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repository |
| `run` | path | integer | yes | run ID |

| Response | Description | Body |
|---|---|---|
| 200 | WorkflowRun (`WorkflowRun`) | `ActionWorkflowRun` |
| 400 | APIError is error format response (`error`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 409 | APIConflict is a conflict empty response (`conflict`) |  |

## POST /api/v1/repos/{owner}/{repo}/actions/runs/{run}/force-cancel

operationId: `forceCancelWorkflowRun`

Force-cancel a workflow run

Cancels a workflow run without waiting for its runners to acknowledge the cancellation.
The jobs are marked cancelled at once and anything a runner reports for them afterwards is discarded.
Only use this endpoint when the workflow run does not respond to `POST /repos/{owner}/{repo}/actions/runs/{run}/cancel`.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repository |
| `run` | path | integer | yes | run ID |

| Response | Description | Body |
|---|---|---|
| 200 | WorkflowRun (`WorkflowRun`) | `ActionWorkflowRun` |
| 400 | APIError is error format response (`error`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 409 | APIConflict is a conflict empty response (`conflict`) |  |

## GET /api/v1/repos/{owner}/{repo}/actions/runs/{run}/jobs

operationId: `listWorkflowRunJobs`

Lists all jobs for a workflow run

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repository |
| `run` | path | integer | yes | runid of the workflow run |
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

## POST /api/v1/repos/{owner}/{repo}/actions/runs/{run}/jobs/{job_id}/rerun

operationId: `rerunWorkflowJob`

Reruns a specific workflow job in a run

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repository |
| `run` | path | integer | yes | id of the run |
| `job_id` | path | integer | yes | id of the job |

| Response | Description | Body |
|---|---|---|
| 201 | WorkflowJob (`WorkflowJob`) | `ActionWorkflowJob` |
| 400 | APIError is error format response (`error`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 409 | APIError is error format response (`error`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/repos/{owner}/{repo}/actions/runs/{run}/logs

operationId: `getWorkflowRunLogs`

Download workflow run logs as archive

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repository |
| `run` | path | integer | yes | run ID |

| Response | Description | Body |
|---|---|---|
| 200 | Logs archive |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/actions/runs/{run}/rerun

operationId: `rerunWorkflowRun`

Reruns an entire workflow run

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repository |
| `run` | path | integer | yes | id of the run |

| Response | Description | Body |
|---|---|---|
| 201 | WorkflowRun (`WorkflowRun`) | `ActionWorkflowRun` |
| 400 | APIError is error format response (`error`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 409 | APIError is error format response (`error`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## POST /api/v1/repos/{owner}/{repo}/actions/runs/{run}/rerun-failed-jobs

operationId: `rerunFailedWorkflowRun`

Reruns all failed jobs in a workflow run

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repository |
| `run` | path | integer | yes | id of the run |

| Response | Description | Body |
|---|---|---|
| 201 | APIEmpty is an empty response (`empty`) |  |
| 400 | APIError is error format response (`error`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 409 | APIError is error format response (`error`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/repos/{owner}/{repo}/actions/secrets

operationId: `repoListActionsSecrets`

List a repo's actions secrets

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repository |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | SecretList (`SecretList`) | array of `Secret` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PUT /api/v1/repos/{owner}/{repo}/actions/secrets/{secretname}

operationId: `updateRepoSecret`

Create or Update a secret value in a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repository |
| `repo` | path | string | yes | name of the repository |
| `secretname` | path | string | yes | name of the secret |

Request body (application/json): `CreateOrUpdateSecretOption`

| Response | Description | Body |
|---|---|---|
| 201 | response when creating a secret |  |
| 204 | response when updating a secret |  |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/actions/secrets/{secretname}

operationId: `deleteRepoSecret`

Delete a secret in a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repository |
| `repo` | path | string | yes | name of the repository |
| `secretname` | path | string | yes | name of the secret |

| Response | Description | Body |
|---|---|---|
| 204 | delete one secret of the repository |  |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/actions/tasks

operationId: `ListActionTasks`

List a repository's action tasks

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results, default maximum page size is 50 |

| Response | Description | Body |
|---|---|---|
| 200 | TasksList (`TasksList`) | `ActionTaskResponse` |
| 400 | APIError is error format response (`error`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 409 | APIConflict is a conflict empty response (`conflict`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/repos/{owner}/{repo}/actions/variables

operationId: `getRepoVariablesList`

Get repo-level variables list

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repository |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | VariableList (`VariableList`) | array of `ActionVariable` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/actions/variables/{variablename}

operationId: `getRepoVariable`

Get a repo-level variable

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repository |
| `variablename` | path | string | yes | name of the variable |

| Response | Description | Body |
|---|---|---|
| 200 | ActionVariable (`ActionVariable`) | `ActionVariable` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/actions/variables/{variablename}

operationId: `createRepoVariable`

Create a repo-level variable

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repository |
| `variablename` | path | string | yes | name of the variable |

Request body (application/json): `CreateVariableOption`

| Response | Description | Body |
|---|---|---|
| 201 | response when creating a repo-level variable |  |
| 400 | APIError is error format response (`error`) |  |
| 409 | variable name already exists. |  |
| 500 | APIError is error format response (`error`) |  |

## PUT /api/v1/repos/{owner}/{repo}/actions/variables/{variablename}

operationId: `updateRepoVariable`

Update a repo-level variable

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repository |
| `variablename` | path | string | yes | name of the variable |

Request body (application/json): `UpdateVariableOption`

| Response | Description | Body |
|---|---|---|
| 201 | response when updating a repo-level variable |  |
| 204 | response when updating a repo-level variable |  |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/actions/variables/{variablename}

operationId: `deleteRepoVariable`

Delete a repo-level variable

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repository |
| `variablename` | path | string | yes | name of the variable |

| Response | Description | Body |
|---|---|---|
| 200 | ActionVariable (`ActionVariable`) | `ActionVariable` |
| 201 | response when deleting a variable |  |
| 204 | response when deleting a variable |  |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/actions/workflows

operationId: `ActionsListRepositoryWorkflows`

List repository workflows

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

| Response | Description | Body |
|---|---|---|
| 200 | ActionWorkflowList (`ActionWorkflowList`) | `ActionWorkflowResponse` |
| 400 | APIError is error format response (`error`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |
| 500 | APIError is error format response (`error`) |  |

## GET /api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id}

operationId: `ActionsGetWorkflow`

Get a workflow

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `workflow_id` | path | string | yes | id of the workflow |

| Response | Description | Body |
|---|---|---|
| 200 | ActionWorkflow (`ActionWorkflow`) | `ActionWorkflow` |
| 400 | APIError is error format response (`error`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |
| 500 | APIError is error format response (`error`) |  |

## PUT /api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable

operationId: `ActionsDisableWorkflow`

Disable a workflow

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `workflow_id` | path | string | yes | id of the workflow |

| Response | Description | Body |
|---|---|---|
| 204 | No Content |  |
| 400 | APIError is error format response (`error`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## POST /api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches

operationId: `ActionsDispatchWorkflow`

Create a workflow dispatch event

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `workflow_id` | path | string | yes | id of the workflow |
| `return_run_details` | query | boolean |  | Whether the response should include the workflow run ID and URLs. |
| `scoped_workflow_source_repo_id` | query | integer (int64) |  | For a scoped workflow, the ID of the source repository providing it; omit or 0 for a repo-level workflow. |

Request body (application/json): `CreateActionWorkflowDispatch`

| Response | Description | Body |
|---|---|---|
| 200 | RunDetails (`RunDetails`) | `RunDetails` |
| 204 | No Content, if return_run_details is missing or false |  |
| 400 | APIError is error format response (`error`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## PUT /api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable

operationId: `ActionsEnableWorkflow`

Enable a workflow

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `workflow_id` | path | string | yes | id of the workflow |

| Response | Description | Body |
|---|---|---|
| 204 | No Content |  |
| 400 | APIError is error format response (`error`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 409 | APIConflict is a conflict empty response (`conflict`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs

operationId: `ActionsListWorkflowRuns`

List runs for a workflow

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `workflow_id` | path | string | yes | id of the workflow, must be the workflow file name (e.g. `build.yml`) |
| `event` | query | string |  | workflow event name |
| `branch` | query | string |  | workflow branch |
| `status` | query | string |  | workflow status (requested, pending, queued, in_progress, failure, success, skipped) |
| `actor` | query | string |  | triggered by user |
| `head_sha` | query | string |  | triggering sha of the workflow run |
| `exclude_pull_requests` | query | boolean |  | if true, the `pull_requests` field on each returned run is emptied |
| `scoped_workflow_source_repo_id` | query | integer (int64) |  | For a scoped workflow, the ID of the source repository providing it; omit or 0 for a repo-level workflow. |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | WorkflowRunsList (`WorkflowRunsList`) | `ActionWorkflowRunsResponse` |
| 400 | APIError is error format response (`error`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/activities/feeds

operationId: `repoListActivityFeeds`

List a repository's activity feeds

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `date` | query | string (date) |  | the date of the activities to be found |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | ActivityFeedsList (`ActivityFeedsList`) | array of `Activity` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/archive/{archive}

operationId: `repoGetArchive`

Get an archive of a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `archive` | path | string | yes | the git reference for download with attached archive format (e.g. master.zip) |
| `path` | query | array of string |  | subpath of the repository to download |

| Response | Description | Body |
|---|---|---|
| 200 | success |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/assignees

operationId: `repoGetAssignees`

Return all users that have write access and can be assigned to issues

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

| Response | Description | Body |
|---|---|---|
| 200 | UserList (`UserList`) | array of `User` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/assignees/{assignee}

operationId: `repoCheckAssignee`

Check if a user can be assigned to issues in a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `assignee` | path | string | yes | username of the user to check for being an assignee |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/avatar

operationId: `repoUpdateAvatar`

Update avatar

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

Request body (application/json): `UpdateRepoAvatarOption`

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/avatar

operationId: `repoDeleteAvatar`

Delete avatar

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/branch_protections

operationId: `repoListBranchProtection`

List branch protections for a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

| Response | Description | Body |
|---|---|---|
| 200 | BranchProtectionList (`BranchProtectionList`) | array of `BranchProtection` |

## POST /api/v1/repos/{owner}/{repo}/branch_protections

operationId: `repoCreateBranchProtection`

Create a branch protections for a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

Request body (application/json): `CreateBranchProtectionOption`

| Response | Description | Body |
|---|---|---|
| 201 | BranchProtection (`BranchProtection`) | `BranchProtection` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## POST /api/v1/repos/{owner}/{repo}/branch_protections/priority

operationId: `repoUpdateBranchProtectionPriories`

Update the priorities of branch protections for a repository.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

Request body (application/json): `UpdateBranchProtectionPriories`

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## GET /api/v1/repos/{owner}/{repo}/branch_protections/{name}

operationId: `repoGetBranchProtection`

Get a specific branch protection for the repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `name` | path | string | yes | name of protected branch |

| Response | Description | Body |
|---|---|---|
| 200 | BranchProtection (`BranchProtection`) | `BranchProtection` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PATCH /api/v1/repos/{owner}/{repo}/branch_protections/{name}

operationId: `repoEditBranchProtection`

Edit a branch protections for a repository. Only fields that are set will be changed

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `name` | path | string | yes | name of protected branch |

Request body (application/json): `EditBranchProtectionOption`

| Response | Description | Body |
|---|---|---|
| 200 | BranchProtection (`BranchProtection`) | `BranchProtection` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/branch_protections/{name}

operationId: `repoDeleteBranchProtection`

Delete a specific branch protection for the repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `name` | path | string | yes | name of protected branch |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/branches

operationId: `repoListBranches`

List a repository's branches

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |
| `q` | query | string |  | branch name substring to filter by |

| Response | Description | Body |
|---|---|---|
| 200 | BranchList (`BranchList`) | array of `Branch` |

## POST /api/v1/repos/{owner}/{repo}/branches

operationId: `repoCreateBranch`

Create a branch

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

Request body (application/json): `CreateBranchRepoOption`

| Response | Description | Body |
|---|---|---|
| 201 | Branch (`Branch`) | `Branch` |
| 403 | The branch is archived or a mirror. |  |
| 404 | The old branch does not exist. |  |
| 409 | The branch with the same name already exists. |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## GET /api/v1/repos/{owner}/{repo}/branches/{branch}

operationId: `repoGetBranch`

Retrieve a specific branch from a repository, including its effective branch protection

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `branch` | path | string | yes | branch to get |

| Response | Description | Body |
|---|---|---|
| 200 | Branch (`Branch`) | `Branch` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PUT /api/v1/repos/{owner}/{repo}/branches/{branch}

operationId: `repoUpdateBranch`

Update a branch reference to a new commit

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `branch` | path | string | yes | name of the branch |

Request body (application/json): `UpdateBranchRepoOption`

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 409 | APIConflict is a conflict empty response (`conflict`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## PATCH /api/v1/repos/{owner}/{repo}/branches/{branch}

operationId: `repoRenameBranch`

Rename a branch

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `branch` | path | string | yes | name of the branch |

Request body (application/json): `RenameBranchRepoOption`

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/branches/{branch}

operationId: `repoDeleteBranch`

Delete a specific branch from a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `branch` | path | string | yes | branch to delete |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## GET /api/v1/repos/{owner}/{repo}/collaborators

operationId: `repoListCollaborators`

List a repository's collaborators

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | UserList (`UserList`) | array of `User` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/collaborators/{collaborator}

operationId: `repoCheckCollaborator`

Check if a user is a collaborator of a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `collaborator` | path | string | yes | username of the user to check for being a collaborator |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## PUT /api/v1/repos/{owner}/{repo}/collaborators/{collaborator}

operationId: `repoAddCollaborator`

Add or Update a collaborator to a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `collaborator` | path | string | yes | username of the user to add or update as a collaborator |

Request body (application/json): `AddCollaboratorOption`

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/collaborators/{collaborator}

operationId: `repoDeleteCollaborator`

Delete a collaborator from a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `collaborator` | path | string | yes | username of the collaborator to delete |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/repos/{owner}/{repo}/collaborators/{collaborator}/permission

operationId: `repoGetRepoPermissions`

Get repository permissions for a user

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `collaborator` | path | string | yes | username of the collaborator whose permissions are to be obtained |

| Response | Description | Body |
|---|---|---|
| 200 | RepoCollaboratorPermission (`RepoCollaboratorPermission`) | `RepoCollaboratorPermission` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/commits

operationId: `repoGetAllCommits`

Get a list of all commits from a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `sha` | query | string |  | SHA or branch to start listing commits from (usually 'master') |
| `path` | query | string |  | filepath of a file/dir |
| `since` | query | string (date-time) |  | Only commits after this date will be returned (ISO 8601 format) |
| `until` | query | string (date-time) |  | Only commits before this date will be returned (ISO 8601 format) |
| `stat` | query | boolean |  | include diff stats for every commit (disable for speedup, default 'true') |
| `verification` | query | boolean |  | include verification for every commit (disable for speedup, default 'true') |
| `files` | query | boolean |  | include a list of affected files for every commit (disable for speedup, default 'true') |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results (ignored if used with 'path') |
| `not` | query | string |  | commits that match the given specifier will not be listed. |

| Response | Description | Body |
|---|---|---|
| 200 | CommitList (`CommitList`) | array of `Commit` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 409 | EmptyRepository (`EmptyRepository`) | `APIError` |

## GET /api/v1/repos/{owner}/{repo}/commits/{ref}/status

operationId: `repoGetCombinedStatusByRef`

Get a commit's combined status, by branch/tag/commit reference

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `ref` | path | string | yes | name of branch/tag/commit |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | CombinedStatus (`CombinedStatus`) | `CombinedStatus` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/commits/{ref}/statuses

operationId: `repoListStatusesByRef`

Get a commit's statuses, by branch/tag/commit reference

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `ref` | path | string | yes | name of branch/tag/commit |
| `sort` | query | string enum: oldest, recentupdate, leastupdate, leastindex, highestindex |  | type of sort |
| `state` | query | string enum: pending, success, error, failure, warning |  | type of state |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | CommitStatusList (`CommitStatusList`) | array of `CommitStatus` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/commits/{sha}/pull

operationId: `repoGetCommitPullRequest`

Get the merged pull request of the commit

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `sha` | path | string | yes | SHA of the commit to get |

| Response | Description | Body |
|---|---|---|
| 200 | PullRequest (`PullRequest`) | `PullRequest` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/compare/{basehead}

operationId: `repoCompareDiff`

Get commit comparison information

By default returns JSON commit comparison information. The raw diff or patch can be
requested with the `output` query parameter set to `diff` or `patch` respectively.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `basehead` | path | string | yes | compare two refs as `base...head` (or `base..head`); refs may be branches, tags, full or short SHAs (including branch names that contain slashes), optionally with a `^` or `~N` revision suffix. |
| `output` | query | string enum: diff, patch |  | return the raw comparison as `diff` or `patch` instead of JSON |
| `verification` | query | boolean |  | include verification for every commit (disable for speedup, default 'true') |
| `files` | query | boolean |  | include a list of affected files for every commit (disable for speedup, default 'true') |

| Response | Description | Body |
|---|---|---|
| 200 |  (`Compare`) | `Compare` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/contents

operationId: `repoGetContentsList`

Gets the metadata of all the entries of the root dir.

This API follows GitHub's design, and it is not easy to use. Recommend users to use our "contents-ext" API instead.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `ref` | query | string |  | The name of the commit/branch/tag. Default to the repository’s default branch. |

| Response | Description | Body |
|---|---|---|
| 200 | ContentsListResponse (`ContentsListResponse`) | array of `ContentsResponse` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/contents

operationId: `repoChangeFiles`

Modify multiple files in a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

Request body (application/json): `ChangeFilesOptions`

| Response | Description | Body |
|---|---|---|
| 201 | FilesResponse (`FilesResponse`) | `FilesResponse` |
| 403 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIError is error format response (`error`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## GET /api/v1/repos/{owner}/{repo}/contents-ext/{filepath}

operationId: `repoGetContentsExt`

The extended "contents" API, to get file metadata and/or content, or list a directory.

It guarantees that only one of the response fields is set if the request succeeds. Users can pass "includes=file_content" or "includes=lfs_metadata" to retrieve more fields. "includes=file_content" only works for single file, if you need to retrieve file contents in batch, use "file-contents" API after listing the directory.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `filepath` | path | string | yes | path of the dir, file, symlink or submodule in the repo. Swagger requires path parameter to be "required", you can leave it empty or pass a single dot (".") to get the root directory. |
| `ref` | query | string |  | the name of the commit/branch/tag, default to the repository’s default branch. |
| `includes` | query | string |  | By default this API's response only contains file's metadata. Use comma-separated "includes" options to retrieve more fields. Option "file_content" will try to retrieve the file content, "lfs_metadata" will try to retrieve LFS metadata, "commit_metadata" will try to retrieve commit metadata, and "commit_message" will try to retrieve commit message. |

| Response | Description | Body |
|---|---|---|
| 200 |  (`ContentsExtResponse`) | `ContentsExtResponse` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/contents/{filepath}

operationId: `repoGetContents`

Gets the metadata and contents (if a file) of an entry in a repository, or a list of entries if a dir.

This API follows GitHub's design, and it is not easy to use. Recommend users to use the "contents-ext" API instead.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `filepath` | path | string | yes | path of the dir, file, symlink or submodule in the repo |
| `ref` | query | string |  | The name of the commit/branch/tag. Default to the repository’s default branch. |

| Response | Description | Body |
|---|---|---|
| 200 | ContentsResponse (`ContentsResponse`) | `ContentsResponse` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/contents/{filepath}

operationId: `repoCreateFile`

Create a file in a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `filepath` | path | string | yes | path of the file to create |

Request body (application/json): `CreateFileOptions`

| Response | Description | Body |
|---|---|---|
| 201 | FileResponse (`FileResponse`) | `FileResponse` |
| 403 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIError is error format response (`error`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## PUT /api/v1/repos/{owner}/{repo}/contents/{filepath}

operationId: `repoUpdateFile`

Update a file in a repository if SHA is set, or create the file if SHA is not set

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `filepath` | path | string | yes | path of the file to update |

Request body (application/json): `UpdateFileOptions`

| Response | Description | Body |
|---|---|---|
| 200 | FileResponse (`FileResponse`) | `FileResponse` |
| 201 | FileResponse (`FileResponse`) | `FileResponse` |
| 403 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIError is error format response (`error`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/contents/{filepath}

operationId: `repoDeleteFile`

Delete a file in a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `filepath` | path | string | yes | path of the file to delete |

Request body (application/json): `DeleteFileOptions`

| Response | Description | Body |
|---|---|---|
| 200 | FileDeleteResponse (`FileDeleteResponse`) | `FileDeleteResponse` |
| 400 | APIError is error format response (`error`) |  |
| 403 | APIError is error format response (`error`) |  |
| 404 | APIError is error format response (`error`) |  |
| 422 | APIError is error format response (`error`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## POST /api/v1/repos/{owner}/{repo}/diffpatch

operationId: `repoApplyDiffPatch`

Apply diff patch to repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

Request body (application/json): `ApplyDiffPatchFileOptions`

| Response | Description | Body |
|---|---|---|
| 200 | FileResponse (`FileResponse`) | `FileResponse` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## GET /api/v1/repos/{owner}/{repo}/editorconfig/{filepath}

operationId: `repoGetEditorConfig`

Get the EditorConfig definitions of a file in a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `filepath` | path | string | yes | filepath of file to get |
| `ref` | query | string |  | The name of the commit/branch/tag. Default to the repository’s default branch. |

| Response | Description | Body |
|---|---|---|
| 200 | success |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/file-contents

operationId: `repoGetFileContents`

Get the metadata and contents of requested files

See the POST method. This GET method supports using JSON encoded request body in query parameter.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `ref` | query | string |  | The name of the commit/branch/tag. Default to the repository’s default branch. |
| `body` | query | string | yes | The JSON encoded body (see the POST request): {"files": ["filename1", "filename2"]} |

| Response | Description | Body |
|---|---|---|
| 200 | ContentsListResponse (`ContentsListResponse`) | array of `ContentsResponse` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/file-contents

operationId: `repoGetFileContentsPost`

Get the metadata and contents of requested files

Uses automatic pagination based on default page size and max response size and returns the maximum allowed number of files. Files which could not be retrieved are null. Files which are too large are being returned with `encoding == null`, `content == null` and `size > 0`, they can be requested separately by using the `download_url`.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `ref` | query | string |  | The name of the commit/branch/tag. Default to the repository’s default branch. |

Request body (application/json): `GetFilesOptions`

| Response | Description | Body |
|---|---|---|
| 200 | ContentsListResponse (`ContentsListResponse`) | array of `ContentsResponse` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/forks

operationId: `listForks`

List a repository's forks

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | RepositoryList (`RepositoryList`) | array of `Repository` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/forks

operationId: `createFork`

Fork a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo to fork |
| `repo` | path | string | yes | name of the repo to fork |

Request body (application/json): `CreateForkOption`

| Response | Description | Body |
|---|---|---|
| 202 | Repository (`Repository`) | `Repository` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 409 | The repository with the same name already exists. |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/repos/{owner}/{repo}/git/blobs/{sha}

operationId: `GetBlob`

Gets the blob of a repository.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `sha` | path | string | yes | sha of the commit |

| Response | Description | Body |
|---|---|---|
| 200 | GitBlobResponse (`GitBlobResponse`) | `GitBlobResponse` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/git/commits/{sha}

operationId: `repoGetSingleCommit`

Get a single commit from a repository, it has a GitHub-compatible alias "/repos/{owner}/{repo}/commits/{ref}"

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `sha` | path | string | yes | a git ref or commit sha |
| `stat` | query | boolean |  | include diff stats for every commit (disable for speedup, default 'true') |
| `verification` | query | boolean |  | include verification for every commit (disable for speedup, default 'true') |
| `files` | query | boolean |  | include a list of affected files for every commit (disable for speedup, default 'true') |

| Response | Description | Body |
|---|---|---|
| 200 | Commit (`Commit`) | `Commit` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/repos/{owner}/{repo}/git/commits/{sha}.{diffType}

operationId: `repoDownloadCommitDiffOrPatch`

Get a commit's diff or patch

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `sha` | path | string | yes | SHA of the commit to get |
| `diffType` | path | string enum: diff, patch | yes | whether the output is diff or patch |

| Response | Description | Body |
|---|---|---|
| 200 | APIString is a string response (`string`) | string |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/git/notes/{sha}

operationId: `repoGetNote`

Get a note corresponding to a single commit from a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `sha` | path | string | yes | a git ref or commit sha |
| `verification` | query | boolean |  | include verification for every commit (disable for speedup, default 'true') |
| `files` | query | boolean |  | include a list of affected files for every commit (disable for speedup, default 'true') |

| Response | Description | Body |
|---|---|---|
| 200 | Note (`Note`) | `Note` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/repos/{owner}/{repo}/git/refs

operationId: `repoListAllGitRefs`

Get specified ref or filtered repository's refs

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

| Response | Description | Body |
|---|---|---|
| 200 | ReferenceList (`ReferenceList`) | array of `Reference` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/git/refs/{ref}

operationId: `repoListGitRefs`

Get specified ref or filtered repository's refs

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `ref` | path | string | yes | part or full name of the ref |

| Response | Description | Body |
|---|---|---|
| 200 | ReferenceList (`ReferenceList`) | array of `Reference` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/git/tags/{sha}

operationId: `GetAnnotatedTag`

Gets the tag object of an annotated tag (not lightweight tags)

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `sha` | path | string | yes | sha of the tag. The Git tags API only supports annotated tag objects, not lightweight tags. |

| Response | Description | Body |
|---|---|---|
| 200 | AnnotatedTag (`AnnotatedTag`) | `AnnotatedTag` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/git/trees/{sha}

operationId: `GetTree`

Gets the tree of a repository.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `sha` | path | string | yes | sha of the commit |
| `recursive` | query | boolean |  | show all directories and files |
| `page` | query | integer |  | page number; the 'truncated' field in the response will be true if there are still more items after this page, false if the last page |
| `per_page` | query | integer |  | number of items per page |

| Response | Description | Body |
|---|---|---|
| 200 | GitTreeResponse (`GitTreeResponse`) | `GitTreeResponse` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/hooks

operationId: `repoListHooks`

List the hooks in a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | HookList (`HookList`) | array of `Hook` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/hooks

operationId: `repoCreateHook`

Create a hook

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

Request body (application/json): `CreateHookOption`

| Response | Description | Body |
|---|---|---|
| 201 | Hook (`Hook`) | `Hook` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/hooks/git

operationId: `repoListGitHooks`

List the Git hooks in a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

| Response | Description | Body |
|---|---|---|
| 200 | GitHookList (`GitHookList`) | array of `GitHook` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/hooks/git/{id}

operationId: `repoGetGitHook`

Get a Git hook

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | string | yes | id of the hook to get |

| Response | Description | Body |
|---|---|---|
| 200 | GitHook (`GitHook`) | `GitHook` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PATCH /api/v1/repos/{owner}/{repo}/hooks/git/{id}

operationId: `repoEditGitHook`

Edit a Git hook in a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | string | yes | id of the hook to get |

Request body (application/json): `EditGitHookOption`

| Response | Description | Body |
|---|---|---|
| 200 | GitHook (`GitHook`) | `GitHook` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/hooks/git/{id}

operationId: `repoDeleteGitHook`

Delete a Git hook in a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | string | yes | id of the hook to get |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/hooks/{id}

operationId: `repoGetHook`

Get a hook

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the hook to get |

| Response | Description | Body |
|---|---|---|
| 200 | Hook (`Hook`) | `Hook` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PATCH /api/v1/repos/{owner}/{repo}/hooks/{id}

operationId: `repoEditHook`

Edit a hook in a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | index of the hook |

Request body (application/json): `EditHookOption`

| Response | Description | Body |
|---|---|---|
| 200 | Hook (`Hook`) | `Hook` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/hooks/{id}

operationId: `repoDeleteHook`

Delete a hook in a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the hook to delete |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/hooks/{id}/tests

operationId: `repoTestHook`

Test a push webhook

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the hook to test |
| `ref` | query | string |  | The name of the commit/branch/tag, indicates which commit will be loaded to the webhook payload. |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/issue_config

operationId: `repoGetIssueConfig`

Returns the issue config for a repo

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

| Response | Description | Body |
|---|---|---|
| 200 | RepoIssueConfig (`RepoIssueConfig`) | `IssueConfig` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/issue_config/validate

operationId: `repoValidateIssueConfig`

Returns the validation information for a issue config

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

| Response | Description | Body |
|---|---|---|
| 200 | RepoIssueConfigValidation (`RepoIssueConfigValidation`) | `IssueConfigValidation` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/issue_templates

operationId: `repoGetIssueTemplates`

Get available issue templates for a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

| Response | Description | Body |
|---|---|---|
| 200 | IssueTemplates (`IssueTemplates`) | array of `IssueTemplate` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/issues/pinned

operationId: `repoListPinnedIssues`

List a repo's pinned issues

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

| Response | Description | Body |
|---|---|---|
| 200 | IssueList (`IssueList`) | array of `Issue` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/keys

operationId: `repoListKeys`

List a repository's keys

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `key_id` | query | integer |  | the key_id to search for |
| `fingerprint` | query | string |  | fingerprint of the key |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | DeployKeyList (`DeployKeyList`) | array of `DeployKey` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/keys

operationId: `repoCreateKey`

Add a key to a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

Request body (application/json): `CreateKeyOption`

| Response | Description | Body |
|---|---|---|
| 201 | DeployKey (`DeployKey`) | `DeployKey` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## POST /api/v1/repos/{owner}/{repo}/keys/tokens

operationId: `repoCreateDeployToken`

Add a deploy token to a repository, it authenticates git over HTTPS

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

Request body (application/json): `CreateDeployKeyTokenOption`

| Response | Description | Body |
|---|---|---|
| 201 | DeployKey (`DeployKey`) | `DeployKey` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/repos/{owner}/{repo}/keys/{id}

operationId: `repoGetKey`

Get a repository's key by id

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the key to get |

| Response | Description | Body |
|---|---|---|
| 200 | DeployKey (`DeployKey`) | `DeployKey` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/keys/{id}

operationId: `repoDeleteKey`

Delete a key from a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the key to delete |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/languages

operationId: `repoGetLanguages`

Get languages and number of bytes of code written

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

| Response | Description | Body |
|---|---|---|
| 200 | LanguageStatistics (`LanguageStatistics`) | object |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/licenses

operationId: `repoGetLicenses`

Get repo licenses

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

| Response | Description | Body |
|---|---|---|
| 200 | LicensesList (`LicensesList`) | array of string |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/media/{filepath}

operationId: `repoGetRawFileOrLFS`

Get a file or it's LFS object from a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `filepath` | path | string | yes | path of the file to get, it should be "{ref}/{filepath}". If there is no ref could be inferred, it will be treated as the default branch |
| `ref` | query | string |  | The name of the commit/branch/tag. Default to the repository’s default branch |

| Response | Description | Body |
|---|---|---|
| 200 | Returns raw file content. | string (binary) |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/merge-upstream

operationId: `repoMergeUpstream`

Merge a branch from upstream

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

Request body (application/json): `MergeUpstreamRequest`

| Response | Description | Body |
|---|---|---|
| 200 |  (`MergeUpstreamResponse`) | `MergeUpstreamResponse` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 409 | APIError is error format response (`error`) |  |

## POST /api/v1/repos/{owner}/{repo}/mirror-sync

operationId: `repoMirrorSync`

Sync a mirrored repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo to sync |
| `repo` | path | string | yes | name of the repo to sync |

| Response | Description | Body |
|---|---|---|
| 200 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/new_pin_allowed

operationId: `repoNewPinAllowed`

Returns if new Issue Pins are allowed

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

| Response | Description | Body |
|---|---|---|
| 200 | RepoNewIssuePinsAllowed (`RepoNewIssuePinsAllowed`) | `NewIssuePinsAllowed` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/projects

operationId: `repoListProjects`

List a repository's projects

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `state` | query | string enum: open, closed, all |  | State of the project (open, closed, all) |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | ProjectList (`ProjectList`) | array of `Project` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/projects

operationId: `repoCreateProject`

Create a project owned by a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

Request body (application/json): `CreateProjectOption`

| Response | Description | Body |
|---|---|---|
| 201 | Project (`Project`) | `Project` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## GET /api/v1/repos/{owner}/{repo}/projects/{id}

operationId: `repoGetProject`

Get a project

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the project |

| Response | Description | Body |
|---|---|---|
| 200 | Project (`Project`) | `Project` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PATCH /api/v1/repos/{owner}/{repo}/projects/{id}

operationId: `repoEditProject`

Edit a project

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the project |

Request body (application/json): `EditProjectOption`

| Response | Description | Body |
|---|---|---|
| 200 | Project (`Project`) | `Project` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/projects/{id}

operationId: `repoDeleteProject`

Delete a project

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the project |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## GET /api/v1/repos/{owner}/{repo}/projects/{id}/columns

operationId: `repoListProjectColumns`

List a project's columns

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the project |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | ProjectColumnList (`ProjectColumnList`) | array of `ProjectColumn` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/projects/{id}/columns

operationId: `repoCreateProjectColumn`

Create a column in a project

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the project |

Request body (application/json): `CreateProjectColumnOption`

| Response | Description | Body |
|---|---|---|
| 201 | ProjectColumn (`ProjectColumn`) | `ProjectColumn` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## POST /api/v1/repos/{owner}/{repo}/projects/{id}/columns/move

operationId: `repoMoveProjectColumns`

Reorder a project's columns

Reorders every column of the project at once. The body lists all column IDs in their new order.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the project |

Request body (application/json): `MoveProjectColumnsOption`

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## GET /api/v1/repos/{owner}/{repo}/projects/{id}/columns/{column_id}

operationId: `repoGetProjectColumn`

Get a project column

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the project |
| `column_id` | path | integer (int64) | yes | id of the column |

| Response | Description | Body |
|---|---|---|
| 200 | ProjectColumn (`ProjectColumn`) | `ProjectColumn` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PATCH /api/v1/repos/{owner}/{repo}/projects/{id}/columns/{column_id}

operationId: `repoEditProjectColumn`

Edit a project column

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the project |
| `column_id` | path | integer (int64) | yes | id of the column |

Request body (application/json): `EditProjectColumnOption`

| Response | Description | Body |
|---|---|---|
| 200 | ProjectColumn (`ProjectColumn`) | `ProjectColumn` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/projects/{id}/columns/{column_id}

operationId: `repoDeleteProjectColumn`

Delete a project column

The default column cannot be deleted while it is still the column new issues land in.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the project |
| `column_id` | path | integer (int64) | yes | id of the column |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## POST /api/v1/repos/{owner}/{repo}/projects/{id}/columns/{column_id}/default

operationId: `repoSetDefaultProjectColumn`

Set a project's default column

The default column is where newly assigned issues land.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the project |
| `column_id` | path | integer (int64) | yes | id of the column |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## GET /api/v1/repos/{owner}/{repo}/projects/{id}/columns/{column_id}/issues

operationId: `repoListProjectColumnIssues`

List the issues in a project column

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the project |
| `column_id` | path | integer (int64) | yes | id of the column |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | IssueList (`IssueList`) | array of `Issue` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/projects/{id}/columns/{column_id}/issues/{issue_id}

operationId: `repoAddIssueToProjectColumn`

Add an issue to a project column

Assigns the issue to the project if it is not a member yet, then places it in the column.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
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

## DELETE /api/v1/repos/{owner}/{repo}/projects/{id}/columns/{column_id}/issues/{issue_id}

operationId: `repoRemoveIssueFromProjectColumn`

Remove an issue from a project column

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the project |
| `column_id` | path | integer (int64) | yes | id of the column |
| `issue_id` | path | integer (int64) | yes | global id of the issue, not the repository-local index |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## POST /api/v1/repos/{owner}/{repo}/projects/{id}/issues/{issue_id}/move

operationId: `repoMoveProjectIssue`

Move an issue between a project's columns

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
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

## GET /api/v1/repos/{owner}/{repo}/pulls

operationId: `repoListPullRequests`

List a repo's pull requests

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | Name of the repo |
| `base_branch` | query | string |  | Filter by target base branch of the pull request |
| `state` | query | string enum: open, closed, all |  | State of pull request |
| `sort` | query | string enum: oldest, recentupdate, recentclose, leastupdate, mostcomment, leastcomment, priority |  | Type of sort |
| `milestone` | query | integer (int64) |  | ID of the milestone |
| `labels` | query | array of integer (int64) |  | Label IDs |
| `poster` | query | string |  | Filter by pull request author |
| `page` | query | integer |  | Page number of results to return (1-based) |
| `limit` | query | integer |  | Page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | PullRequestList (`PullRequestList`) | array of `PullRequest` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 500 | APIError is error format response (`error`) |  |

## POST /api/v1/repos/{owner}/{repo}/pulls

operationId: `repoCreatePullRequest`

Create a pull request

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

Request body (application/json): `CreatePullRequestOption`

| Response | Description | Body |
|---|---|---|
| 201 | PullRequest (`PullRequest`) | `PullRequest` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 409 | APIError is error format response (`error`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## POST /api/v1/repos/{owner}/{repo}/pulls/comments/{id}/resolve

operationId: `repoResolvePullReviewComment`

Resolve a pull request review comment

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the review comment |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 400 | APIValidationError is error format response related to input validation (`validationError`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/pulls/comments/{id}/unresolve

operationId: `repoUnresolvePullReviewComment`

Unresolve a pull request review comment

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the review comment |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 400 | APIValidationError is error format response related to input validation (`validationError`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/pulls/pinned

operationId: `repoListPinnedPullRequests`

List a repo's pinned pull requests

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

| Response | Description | Body |
|---|---|---|
| 200 | PullRequestList (`PullRequestList`) | array of `PullRequest` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/pulls/{base}/{head}

operationId: `repoGetPullRequestByBaseHead`

Get a pull request by base and head

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `base` | path | string | yes | base of the pull request to get |
| `head` | path | string | yes | head of the pull request to get |

| Response | Description | Body |
|---|---|---|
| 200 | PullRequest (`PullRequest`) | `PullRequest` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/pulls/{index}

operationId: `repoGetPullRequest`

Get a pull request

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the pull request to get |

| Response | Description | Body |
|---|---|---|
| 200 | PullRequest (`PullRequest`) | `PullRequest` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PATCH /api/v1/repos/{owner}/{repo}/pulls/{index}

operationId: `repoEditPullRequest`

Update a pull request. If using deadline only the date will be taken into account, and time of day ignored.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the pull request to edit |

Request body (application/json): `EditPullRequestOption`

| Response | Description | Body |
|---|---|---|
| 201 | PullRequest (`PullRequest`) | `PullRequest` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 409 | APIError is error format response (`error`) |  |
| 412 | APIError is error format response (`error`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/repos/{owner}/{repo}/pulls/{index}.{diffType}

operationId: `repoDownloadPullDiffOrPatch`

Get a pull request diff or patch

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the pull request to get |
| `diffType` | path | string enum: diff, patch | yes | whether the output is diff or patch |
| `binary` | query | boolean |  | whether to include binary file changes. if true, the diff is applicable with `git apply` |

| Response | Description | Body |
|---|---|---|
| 200 | APIString is a string response (`string`) | string |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/pulls/{index}/comments/{id}/replies

operationId: `repoCreatePullReviewCommentReply`

Reply to a pull request review comment

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the pull request |
| `id` | path | integer (int64) | yes | id of the review comment to reply to |

Request body (application/json): `CreatePullReviewCommentReplyOptions`

| Response | Description | Body |
|---|---|---|
| 201 | PullComment (`PullReviewComment`) | `PullReviewComment` |
| 400 | APIValidationError is error format response related to input validation (`validationError`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/repos/{owner}/{repo}/pulls/{index}/commits

operationId: `repoGetPullRequestCommits`

Get commits for a pull request

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the pull request to get |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |
| `verification` | query | boolean |  | include verification for every commit (disable for speedup, default 'true') |
| `files` | query | boolean |  | include a list of affected files for every commit (disable for speedup, default 'true') |

| Response | Description | Body |
|---|---|---|
| 200 | CommitList (`CommitList`) | array of `Commit` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/pulls/{index}/files

operationId: `repoGetPullRequestFiles`

Get changed files for a pull request

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the pull request to get |
| `skip-to` | query | string |  | skip to given file |
| `whitespace` | query | string enum: ignore-all, ignore-change, ignore-eol, show-all |  | whitespace behavior |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | ChangedFileList (`ChangedFileList`) | array of `ChangedFile` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/pulls/{index}/merge

operationId: `repoPullRequestIsMerged`

Check if a pull request has been merged

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the pull request |

| Response | Description | Body |
|---|---|---|
| 204 | pull request has been merged |  |
| 404 | pull request has not been merged |  |

## POST /api/v1/repos/{owner}/{repo}/pulls/{index}/merge

operationId: `repoMergePullRequest`

Merge a pull request

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the pull request to merge |

Request body (application/json): `MergePullRequestOption`

| Response | Description | Body |
|---|---|---|
| 200 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 405 | APIEmpty is an empty response (`empty`) |  |
| 409 | APIError is error format response (`error`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/pulls/{index}/merge

operationId: `repoCancelScheduledAutoMerge`

Cancel the scheduled auto merge for the given pull request

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the pull request to merge |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## POST /api/v1/repos/{owner}/{repo}/pulls/{index}/requested_reviewers

operationId: `repoCreatePullReviewRequests`

create review requests for a pull request

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the pull request |

Request body (application/json): `PullReviewRequestOptions`

| Response | Description | Body |
|---|---|---|
| 201 | PullReviewList (`PullReviewList`) | array of `PullReview` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/pulls/{index}/requested_reviewers

operationId: `repoDeletePullReviewRequests`

cancel review requests for a pull request

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the pull request |

Request body (application/json): `PullReviewRequestOptions`

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/repos/{owner}/{repo}/pulls/{index}/reviews

operationId: `repoListPullReviews`

List all reviews for a pull request

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the pull request |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | PullReviewList (`PullReviewList`) | array of `PullReview` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/pulls/{index}/reviews

operationId: `repoCreatePullReview`

Create a review to a pull request

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the pull request |

Request body (application/json): `CreatePullReviewOptions`

| Response | Description | Body |
|---|---|---|
| 200 | PullReview (`PullReview`) | `PullReview` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/repos/{owner}/{repo}/pulls/{index}/reviews/{id}

operationId: `repoGetPullReview`

Get a specific review for a pull request

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the pull request |
| `id` | path | integer (int64) | yes | id of the review |

| Response | Description | Body |
|---|---|---|
| 200 | PullReview (`PullReview`) | `PullReview` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/pulls/{index}/reviews/{id}

operationId: `repoSubmitPullReview`

Submit a pending review to a pull request

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the pull request |
| `id` | path | integer (int64) | yes | id of the review |

Request body (application/json): `SubmitPullReviewOptions`

| Response | Description | Body |
|---|---|---|
| 200 | PullReview (`PullReview`) | `PullReview` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/pulls/{index}/reviews/{id}

operationId: `repoDeletePullReview`

Delete a specific review from a pull request

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the pull request |
| `id` | path | integer (int64) | yes | id of the review |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/comments

operationId: `repoGetPullReviewComments`

Get a specific review for a pull request

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the pull request |
| `id` | path | integer (int64) | yes | id of the review |

| Response | Description | Body |
|---|---|---|
| 200 | PullCommentList (`PullReviewCommentList`) | array of `PullReviewComment` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/dismissals

operationId: `repoDismissPullReview`

Dismiss a review for a pull request

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the pull request |
| `id` | path | integer (int64) | yes | id of the review |

Request body (application/json): `DismissPullReviewOptions`

| Response | Description | Body |
|---|---|---|
| 200 | PullReview (`PullReview`) | `PullReview` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## POST /api/v1/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/undismissals

operationId: `repoUnDismissPullReview`

Cancel to dismiss a review for a pull request

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the pull request |
| `id` | path | integer (int64) | yes | id of the review |

| Response | Description | Body |
|---|---|---|
| 200 | PullReview (`PullReview`) | `PullReview` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## POST /api/v1/repos/{owner}/{repo}/pulls/{index}/update

operationId: `repoUpdatePullRequest`

Merge PR's baseBranch into headBranch

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the pull request to get |
| `style` | query | string enum: merge, rebase |  | how to update pull request |

| Response | Description | Body |
|---|---|---|
| 200 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 409 | APIError is error format response (`error`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/repos/{owner}/{repo}/push_mirrors

operationId: `repoListPushMirrors`

Get all push mirrors of the repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | PushMirrorList (`PushMirrorList`) | array of `PushMirror` |
| 400 | APIError is error format response (`error`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/push_mirrors

operationId: `repoAddPushMirror`

add a push mirror to the repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

Request body (application/json): `CreatePushMirrorOption`

| Response | Description | Body |
|---|---|---|
| 200 | PushMirror (`PushMirror`) | `PushMirror` |
| 400 | APIError is error format response (`error`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/push_mirrors-sync

operationId: `repoPushMirrorSync`

Sync all push mirrored repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo to sync |
| `repo` | path | string | yes | name of the repo to sync |

| Response | Description | Body |
|---|---|---|
| 200 | APIEmpty is an empty response (`empty`) |  |
| 400 | APIError is error format response (`error`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/repos/{owner}/{repo}/push_mirrors/{name}

operationId: `repoGetPushMirrorByRemoteName`

Get push mirror of the repository by remoteName

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `name` | path | string | yes | remote name of push mirror |

| Response | Description | Body |
|---|---|---|
| 200 | PushMirror (`PushMirror`) | `PushMirror` |
| 400 | APIError is error format response (`error`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/push_mirrors/{name}

operationId: `repoDeletePushMirror`

deletes a push mirror from a repository by remoteName

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `name` | path | string | yes | remote name of the pushMirror |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/raw/{filepath}

operationId: `repoGetRawFile`

Get a file from a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `filepath` | path | string | yes | path of the file to get, it should be "{ref}/{filepath}". If there is no ref could be inferred, it will be treated as the default branch |
| `ref` | query | string |  | The name of the commit/branch/tag. Default to the repository’s default branch |

| Response | Description | Body |
|---|---|---|
| 200 | Returns raw file content. | string (binary) |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/releases

operationId: `repoListReleases`

List a repo's releases

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `draft` | query | boolean |  | filter (exclude / include) drafts, if you don't have repo write access none will show |
| `pre-release` | query | boolean |  | filter (exclude / include) pre-releases |
| `tag_filter` | query | string |  | filter releases by tag. supports "*" as a wildcard (for example: v1*, *beta, *rc*). |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | ReleaseList (`ReleaseList`) | array of `Release` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/releases

operationId: `repoCreateRelease`

Create a release

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

Request body (application/json): `CreateReleaseOption`

| Response | Description | Body |
|---|---|---|
| 201 | Release (`Release`) | `Release` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 409 | APIError is error format response (`error`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/repos/{owner}/{repo}/releases/latest

operationId: `repoGetLatestRelease`

Gets the most recent non-prerelease, non-draft release of a repository, sorted by created_at

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

| Response | Description | Body |
|---|---|---|
| 200 | Release (`Release`) | `Release` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/releases/tags/{tag}

operationId: `repoGetReleaseByTag`

Get a release by tag name

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `tag` | path | string | yes | tag name of the release to get |

| Response | Description | Body |
|---|---|---|
| 200 | Release (`Release`) | `Release` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/releases/tags/{tag}

operationId: `repoDeleteReleaseByTag`

Delete a release by tag name

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `tag` | path | string | yes | tag name of the release to delete |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/repos/{owner}/{repo}/releases/{id}

operationId: `repoGetRelease`

Get a release

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the release to get |

| Response | Description | Body |
|---|---|---|
| 200 | Release (`Release`) | `Release` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PATCH /api/v1/repos/{owner}/{repo}/releases/{id}

operationId: `repoEditRelease`

Update a release

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the release to edit |

Request body (application/json): `EditReleaseOption`

| Response | Description | Body |
|---|---|---|
| 200 | Release (`Release`) | `Release` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/releases/{id}

operationId: `repoDeleteRelease`

Delete a release

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the release to delete |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/repos/{owner}/{repo}/releases/{id}/assets

operationId: `repoListReleaseAttachments`

List release's attachments

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the release |

| Response | Description | Body |
|---|---|---|
| 200 | AttachmentList (`AttachmentList`) | array of `Attachment` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/releases/{id}/assets

operationId: `repoCreateReleaseAttachment`

Create a release attachment

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the release |
| `name` | query | string |  | name of the attachment |

Request body (application/octet-stream): object

Request body (multipart/form-data): object

| Response | Description | Body |
|---|---|---|
| 201 | Attachment (`Attachment`) | `Attachment` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 413 | APIError is error format response (`error`) |  |

## GET /api/v1/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}

operationId: `repoGetReleaseAttachment`

Get a release attachment

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the release |
| `attachment_id` | path | integer (int64) | yes | id of the attachment to get |

| Response | Description | Body |
|---|---|---|
| 200 | Attachment (`Attachment`) | `Attachment` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PATCH /api/v1/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}

operationId: `repoEditReleaseAttachment`

Edit a release attachment

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the release |
| `attachment_id` | path | integer (int64) | yes | id of the attachment to edit |

Request body (application/json): `EditAttachmentOptions`

| Response | Description | Body |
|---|---|---|
| 201 | Attachment (`Attachment`) | `Attachment` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}

operationId: `repoDeleteReleaseAttachment`

Delete a release attachment

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the release |
| `attachment_id` | path | integer (int64) | yes | id of the attachment to delete |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/reviewers

operationId: `repoGetReviewers`

Return all users that can be requested to review in this repo

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

| Response | Description | Body |
|---|---|---|
| 200 | UserList (`UserList`) | array of `User` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/signing-key.gpg

operationId: `repoSigningKey`

Get signing-key.gpg for given repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

| Response | Description | Body |
|---|---|---|
| 200 | GPG armored public key | string |

## GET /api/v1/repos/{owner}/{repo}/signing-key.pub

operationId: `repoSigningKeySSH`

Get signing-key.pub for given repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

| Response | Description | Body |
|---|---|---|
| 200 | ssh public key | string |

## GET /api/v1/repos/{owner}/{repo}/stargazers

operationId: `repoListStargazers`

List a repo's stargazers

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | UserList (`UserList`) | array of `User` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/statuses/{sha}

operationId: `repoListStatuses`

Get a commit's statuses

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `sha` | path | string | yes | sha of the commit |
| `sort` | query | string enum: oldest, recentupdate, leastupdate, leastindex, highestindex |  | type of sort |
| `state` | query | string enum: pending, success, error, failure, warning |  | type of state |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | CommitStatusList (`CommitStatusList`) | array of `CommitStatus` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/statuses/{sha}

operationId: `repoCreateStatus`

Create a commit status

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `sha` | path | string | yes | sha of the commit |

Request body (application/json): `CreateStatusOption`

| Response | Description | Body |
|---|---|---|
| 201 | CommitStatus (`CommitStatus`) | `CommitStatus` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/subscribers

operationId: `repoListSubscribers`

List a repo's watchers

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | UserList (`UserList`) | array of `User` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/subscription

operationId: `userCurrentCheckSubscription`

Check if the current user is watching a repo

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

| Response | Description | Body |
|---|---|---|
| 200 | WatchInfo (`WatchInfo`) | `WatchInfo` |
| 404 | User is not watching this repo or repo do not exist |  |

## PUT /api/v1/repos/{owner}/{repo}/subscription

operationId: `userCurrentPutSubscription`

Watch a repo

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

| Response | Description | Body |
|---|---|---|
| 200 | WatchInfo (`WatchInfo`) | `WatchInfo` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/subscription

operationId: `userCurrentDeleteSubscription`

Unwatch a repo

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/tag_protections

operationId: `repoListTagProtection`

List tag protections for a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

| Response | Description | Body |
|---|---|---|
| 200 | TagProtectionList (`TagProtectionList`) | array of `TagProtection` |

## POST /api/v1/repos/{owner}/{repo}/tag_protections

operationId: `repoCreateTagProtection`

Create a tag protections for a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

Request body (application/json): `CreateTagProtectionOption`

| Response | Description | Body |
|---|---|---|
| 201 | TagProtection (`TagProtection`) | `TagProtection` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## GET /api/v1/repos/{owner}/{repo}/tag_protections/{id}

operationId: `repoGetTagProtection`

Get a specific tag protection for the repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer | yes | id of the tag protect to get |

| Response | Description | Body |
|---|---|---|
| 200 | TagProtection (`TagProtection`) | `TagProtection` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PATCH /api/v1/repos/{owner}/{repo}/tag_protections/{id}

operationId: `repoEditTagProtection`

Edit a tag protections for a repository. Only fields that are set will be changed

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer | yes | id of protected tag |

Request body (application/json): `EditTagProtectionOption`

| Response | Description | Body |
|---|---|---|
| 200 | TagProtection (`TagProtection`) | `TagProtection` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/tag_protections/{id}

operationId: `repoDeleteTagProtection`

Delete a specific tag protection for the repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer | yes | id of protected tag |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/tags

operationId: `repoListTags`

List a repository's tags

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results, default maximum page size is 50 |

| Response | Description | Body |
|---|---|---|
| 200 | TagList (`TagList`) | array of `Tag` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/tags

operationId: `repoCreateTag`

Create a new git tag in a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

Request body (application/json): `CreateTagOption`

| Response | Description | Body |
|---|---|---|
| 200 | Tag (`Tag`) | `Tag` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 405 | APIEmpty is an empty response (`empty`) |  |
| 409 | APIConflict is a conflict empty response (`conflict`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## GET /api/v1/repos/{owner}/{repo}/tags/{tag}

operationId: `repoGetTag`

Get the tag of a repository by tag name

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `tag` | path | string | yes | name of tag |

| Response | Description | Body |
|---|---|---|
| 200 | Tag (`Tag`) | `Tag` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/tags/{tag}

operationId: `repoDeleteTag`

Delete a repository's tag by name

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `tag` | path | string | yes | name of tag to delete |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 405 | APIEmpty is an empty response (`empty`) |  |
| 409 | APIConflict is a conflict empty response (`conflict`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## GET /api/v1/repos/{owner}/{repo}/teams

operationId: `repoListTeams`

List a repository's teams

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

| Response | Description | Body |
|---|---|---|
| 200 | TeamList (`TeamList`) | array of `Team` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/teams/{team}

operationId: `repoCheckTeam`

Check if a team is assigned to a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `team` | path | string | yes | team name |

| Response | Description | Body |
|---|---|---|
| 200 | Team (`Team`) | `Team` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 405 | APIError is error format response (`error`) |  |

## PUT /api/v1/repos/{owner}/{repo}/teams/{team}

operationId: `repoAddTeam`

Add a team to a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `team` | path | string | yes | team name |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 405 | APIError is error format response (`error`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/teams/{team}

operationId: `repoDeleteTeam`

Delete a team from a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `team` | path | string | yes | team name |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 405 | APIError is error format response (`error`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/repos/{owner}/{repo}/times

operationId: `repoTrackedTimes`

List a repo's tracked times

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `user` | query | string |  | optional filter by user (available for issue managers) |
| `since` | query | string (date-time) |  | Only show times updated after the given time. This is a timestamp in RFC 3339 format |
| `before` | query | string (date-time) |  | Only show times updated before the given time. This is a timestamp in RFC 3339 format |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | TrackedTimeList (`TrackedTimeList`) | array of `TrackedTime` |
| 400 | APIError is error format response (`error`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/times/{user}

operationId: `userTrackedTimes`
**DEPRECATED**

List a user's tracked times in a repo

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `user` | path | string | yes | username of the user whose tracked times are to be listed |

| Response | Description | Body |
|---|---|---|
| 200 | TrackedTimeList (`TrackedTimeList`) | array of `TrackedTime` |
| 400 | APIError is error format response (`error`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/topics

operationId: `repoListTopics`

Get list of topics that a repository has

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | TopicNames (`TopicNames`) | `TopicName` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PUT /api/v1/repos/{owner}/{repo}/topics

operationId: `repoUpdateTopics`

Replace list of topics for a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

Request body (application/json): `RepoTopicOptions`

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIInvalidTopicsError is error format response to invalid topics (`invalidTopicsError`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## PUT /api/v1/repos/{owner}/{repo}/topics/{topic}

operationId: `repoAddTopic`

Add a topic to a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `topic` | path | string | yes | name of the topic to add |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIInvalidTopicsError is error format response to invalid topics (`invalidTopicsError`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/topics/{topic}

operationId: `repoDeleteTopic`

Delete a topic from a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `topic` | path | string | yes | name of the topic to delete |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIInvalidTopicsError is error format response to invalid topics (`invalidTopicsError`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## POST /api/v1/repos/{owner}/{repo}/transfer

operationId: `repoTransfer`

Transfer a repo ownership

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo to transfer |
| `repo` | path | string | yes | name of the repo to transfer |

Request body (application/json): `TransferRepoOption`

| Response | Description | Body |
|---|---|---|
| 202 | Repository (`Repository`) | `Repository` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## POST /api/v1/repos/{owner}/{repo}/transfer/accept

operationId: `acceptRepoTransfer`

Accept a repo transfer

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo to transfer |
| `repo` | path | string | yes | name of the repo to transfer |

| Response | Description | Body |
|---|---|---|
| 202 | Repository (`Repository`) | `Repository` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/transfer/reject

operationId: `rejectRepoTransfer`

Reject a repo transfer

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo to transfer |
| `repo` | path | string | yes | name of the repo to transfer |

| Response | Description | Body |
|---|---|---|
| 200 | Repository (`Repository`) | `Repository` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/wiki/new

operationId: `repoCreateWikiPage`

Create a wiki page

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

Request body (application/json): `CreateWikiPageOptions`

| Response | Description | Body |
|---|---|---|
| 201 | WikiPage (`WikiPage`) | `WikiPage` |
| 400 | APIError is error format response (`error`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## GET /api/v1/repos/{owner}/{repo}/wiki/page/{pageName}

operationId: `repoGetWikiPage`

Get a wiki page

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `pageName` | path | string | yes | name of the page |

| Response | Description | Body |
|---|---|---|
| 200 | WikiPage (`WikiPage`) | `WikiPage` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PATCH /api/v1/repos/{owner}/{repo}/wiki/page/{pageName}

operationId: `repoEditWikiPage`

Edit a wiki page

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `pageName` | path | string | yes | name of the page |

Request body (application/json): `CreateWikiPageOptions`

| Response | Description | Body |
|---|---|---|
| 200 | WikiPage (`WikiPage`) | `WikiPage` |
| 400 | APIError is error format response (`error`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/wiki/page/{pageName}

operationId: `repoDeleteWikiPage`

Delete a wiki page

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `pageName` | path | string | yes | name of the page |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## GET /api/v1/repos/{owner}/{repo}/wiki/pages

operationId: `repoGetWikiPages`

Get all wiki pages

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | WikiPageList (`WikiPageList`) | array of `WikiPageMetaData` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/wiki/revisions/{pageName}

operationId: `repoGetWikiPageRevisions`

Get revisions of a wiki page

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `pageName` | path | string | yes | name of the page |
| `page` | query | integer |  | page number of results to return (1-based) |

| Response | Description | Body |
|---|---|---|
| 200 | WikiCommitList (`WikiCommitList`) | `WikiCommitList` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{template_owner}/{template_repo}/generate

operationId: `generateRepo`

Create a repository using a template

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `template_owner` | path | string | yes | owner of the template repository |
| `template_repo` | path | string | yes | name of the template repository |

Request body (application/json): `GenerateRepoOption`

| Response | Description | Body |
|---|---|---|
| 201 | Repository (`Repository`) | `Repository` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 409 | The repository with the same name already exists. |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/repositories/{id}

operationId: `repoGetByID`

Get a repository by id

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer (int64) | yes | id of the repo to get |

| Response | Description | Body |
|---|---|---|
| 200 | Repository (`Repository`) | `Repository` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/topics/search

operationId: `topicSearch`

search topics via keyword

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `q` | query | string | yes | keywords to search |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | TopicListResponse (`TopicListResponse`) | `TopicListResponse` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
