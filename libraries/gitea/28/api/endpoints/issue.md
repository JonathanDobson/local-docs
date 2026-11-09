# Gitea API 28.3.0 — issue

## GET /api/v1/repos/issues/search

operationId: `issueSearchIssues`

Search for issues across the repositories that the user has access to

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `state` | query | string enum: open, closed, all |  | State of the issue |
| `labels` | query | string |  | Comma-separated list of label names. Fetch only issues that have any of these labels. Non existent labels are discarded. |
| `milestones` | query | string |  | Comma-separated list of milestone names. Fetch only issues that have any of these milestones. Non existent milestones are discarded. |
| `q` | query | string |  | Search string |
| `type` | query | string enum: issues, pulls |  | Filter by issue type |
| `since` | query | string (date-time) |  | Only show issues updated after the given time (RFC 3339 format) |
| `before` | query | string (date-time) |  | Only show issues updated before the given time (RFC 3339 format) |
| `assigned` | query | boolean |  | Filter issues or pulls assigned to the authenticated user |
| `created` | query | boolean |  | Filter issues or pulls created by the authenticated user |
| `mentioned` | query | boolean |  | Filter issues or pulls mentioning the authenticated user |
| `review_requested` | query | boolean |  | Filter pull requests where the authenticated user's review was requested |
| `reviewed` | query | boolean |  | Filter pull requests reviewed by the authenticated user |
| `owner` | query | string |  | Filter by repository owner |
| `created_by` | query | string |  | Only show items which were created by the given user |
| `team` | query | string |  | Filter by team (requires organization owner parameter) |
| `page` | query | integer |  | Page number of results to return (1-based) |
| `limit` | query | integer |  | Number of items per page |

| Response | Description | Body |
|---|---|---|
| 200 | IssueList (`IssueList`) | array of `Issue` |
| 400 | APIError is error format response (`error`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/repos/{owner}/{repo}/issues

operationId: `issueListIssues`

List a repository's issues

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `state` | query | string enum: closed, open, all |  | whether issue is open or closed |
| `labels` | query | string |  | comma separated list of label names. Fetch only issues that have any of this label names. Non existent labels are discarded. |
| `q` | query | string |  | search string |
| `type` | query | string enum: issues, pulls |  | filter by type (issues / pulls) if set |
| `milestones` | query | string |  | comma separated list of milestone names or ids. It uses names and fall back to ids. Fetch only issues that have any of this milestones. Non existent milestones are discarded |
| `since` | query | string (date-time) |  | Only show items updated after the given time. This is a timestamp in RFC 3339 format |
| `before` | query | string (date-time) |  | Only show items updated before the given time. This is a timestamp in RFC 3339 format |
| `created_by` | query | string |  | Only show items which were created by the given user |
| `assigned_by` | query | string |  | Only show items for which the given user is assigned |
| `mentioned_by` | query | string |  | Only show items in which the given user was mentioned |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | IssueList (`IssueList`) | array of `Issue` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/issues

operationId: `issueCreateIssue`

Create an issue. If using deadline only the date will be taken into account, and time of day ignored.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

Request body (application/json): `CreateIssueOption`

| Response | Description | Body |
|---|---|---|
| 201 | Issue (`Issue`) | `Issue` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 412 | APIError is error format response (`error`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## GET /api/v1/repos/{owner}/{repo}/issues/comments

operationId: `issueGetRepoComments`

List all comments in a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `since` | query | string (date-time) |  | if provided, only comments updated since the provided time are returned. |
| `before` | query | string (date-time) |  | if provided, only comments updated before the provided time are returned. |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | CommentList (`CommentList`) | array of `Comment` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/issues/comments/{id}

operationId: `issueGetComment`

Get a comment

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the comment |

| Response | Description | Body |
|---|---|---|
| 200 | Comment (`Comment`) | `Comment` |
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PATCH /api/v1/repos/{owner}/{repo}/issues/comments/{id}

operationId: `issueEditComment`

Edit a comment

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the comment to edit |

Request body (application/json): `EditIssueCommentOption`

| Response | Description | Body |
|---|---|---|
| 200 | Comment (`Comment`) | `Comment` |
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/issues/comments/{id}

operationId: `issueDeleteComment`

Delete a comment

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of comment to delete |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/issues/comments/{id}/assets

operationId: `issueListIssueCommentAttachments`

List comment's attachments

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the comment |

| Response | Description | Body |
|---|---|---|
| 200 | AttachmentList (`AttachmentList`) | array of `Attachment` |
| 404 | APIError is error format response (`error`) |  |

## POST /api/v1/repos/{owner}/{repo}/issues/comments/{id}/assets

operationId: `issueCreateIssueCommentAttachment`

Create a comment attachment

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the comment |
| `name` | query | string |  | name of the attachment |

Request body (multipart/form-data): object

| Response | Description | Body |
|---|---|---|
| 201 | Attachment (`Attachment`) | `Attachment` |
| 400 | APIError is error format response (`error`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APIError is error format response (`error`) |  |
| 413 | APIError is error format response (`error`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## GET /api/v1/repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id}

operationId: `issueGetIssueCommentAttachment`

Get a comment attachment

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the comment |
| `attachment_id` | path | integer (int64) | yes | id of the attachment to get |

| Response | Description | Body |
|---|---|---|
| 200 | Attachment (`Attachment`) | `Attachment` |
| 404 | APIError is error format response (`error`) |  |

## PATCH /api/v1/repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id}

operationId: `issueEditIssueCommentAttachment`

Edit a comment attachment

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the comment |
| `attachment_id` | path | integer (int64) | yes | id of the attachment to edit |

Request body (application/json): `EditAttachmentOptions`

| Response | Description | Body |
|---|---|---|
| 201 | Attachment (`Attachment`) | `Attachment` |
| 404 | APIError is error format response (`error`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id}

operationId: `issueDeleteIssueCommentAttachment`

Delete a comment attachment

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the comment |
| `attachment_id` | path | integer (int64) | yes | id of the attachment to delete |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APIError is error format response (`error`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## GET /api/v1/repos/{owner}/{repo}/issues/comments/{id}/reactions

operationId: `issueGetCommentReactions`

Get a list of reactions from a comment of an issue

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the comment to edit |

| Response | Description | Body |
|---|---|---|
| 200 | ReactionList (`ReactionList`) | array of `Reaction` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/issues/comments/{id}/reactions

operationId: `issuePostCommentReaction`

Add a reaction to a comment of an issue

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the comment to edit |

Request body (application/json): `EditReactionOption`

| Response | Description | Body |
|---|---|---|
| 200 | Reaction (`Reaction`) | `Reaction` |
| 201 | Reaction (`Reaction`) | `Reaction` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/issues/comments/{id}/reactions

operationId: `issueDeleteCommentReaction`

Remove a reaction from a comment of an issue

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the comment to edit |

Request body (application/json): `EditReactionOption`

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/issues/{index}

operationId: `issueGetIssue`

Get an issue

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the issue to get |

| Response | Description | Body |
|---|---|---|
| 200 | Issue (`Issue`) | `Issue` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PATCH /api/v1/repos/{owner}/{repo}/issues/{index}

operationId: `issueEditIssue`

Edit an issue. If using deadline only the date will be taken into account, and time of day ignored.

Pass `content_version` to enable optimistic locking on body edits.
If the version doesn't match the current value, the request fails with 409 Conflict.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the issue to edit |

Request body (application/json): `EditIssueOption`

| Response | Description | Body |
|---|---|---|
| 201 | Issue (`Issue`) | `Issue` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 412 | APIError is error format response (`error`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/issues/{index}

operationId: `issueDelete`

Delete an issue

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of issue to delete |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## GET /api/v1/repos/{owner}/{repo}/issues/{index}/assets

operationId: `issueListIssueAttachments`

List issue's attachments

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the issue |

| Response | Description | Body |
|---|---|---|
| 200 | AttachmentList (`AttachmentList`) | array of `Attachment` |
| 404 | APIError is error format response (`error`) |  |

## POST /api/v1/repos/{owner}/{repo}/issues/{index}/assets

operationId: `issueCreateIssueAttachment`

Create an issue attachment

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the issue |
| `name` | query | string |  | name of the attachment |

Request body (multipart/form-data): object

| Response | Description | Body |
|---|---|---|
| 201 | Attachment (`Attachment`) | `Attachment` |
| 400 | APIError is error format response (`error`) |  |
| 404 | APIError is error format response (`error`) |  |
| 413 | APIError is error format response (`error`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## GET /api/v1/repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}

operationId: `issueGetIssueAttachment`

Get an issue attachment

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the issue |
| `attachment_id` | path | integer (int64) | yes | id of the attachment to get |

| Response | Description | Body |
|---|---|---|
| 200 | Attachment (`Attachment`) | `Attachment` |
| 404 | APIError is error format response (`error`) |  |

## PATCH /api/v1/repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}

operationId: `issueEditIssueAttachment`

Edit an issue attachment

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the issue |
| `attachment_id` | path | integer (int64) | yes | id of the attachment to edit |

Request body (application/json): `EditAttachmentOptions`

| Response | Description | Body |
|---|---|---|
| 201 | Attachment (`Attachment`) | `Attachment` |
| 404 | APIError is error format response (`error`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}

operationId: `issueDeleteIssueAttachment`

Delete an issue attachment

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the issue |
| `attachment_id` | path | integer (int64) | yes | id of the attachment to delete |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APIError is error format response (`error`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## POST /api/v1/repos/{owner}/{repo}/issues/{index}/assignees

operationId: `issueAddAssignees`

Add assignees to an issue

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the issue |

Request body (application/json): `IssueAssigneesOption`

| Response | Description | Body |
|---|---|---|
| 201 | Issue (`Issue`) | `Issue` |
| 400 | APIError is error format response (`error`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/assignees

operationId: `issueRemoveAssignees`

Remove assignees from an issue

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the issue |

Request body (application/json): `IssueAssigneesOption`

| Response | Description | Body |
|---|---|---|
| 200 | Issue (`Issue`) | `Issue` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/repos/{owner}/{repo}/issues/{index}/assignees/{assignee}

operationId: `issueCheckAssignee`

Check if a user can be assigned to an issue

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the issue |
| `assignee` | path | string | yes | username of the user to check for being an assignee |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 400 | APIError is error format response (`error`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/issues/{index}/blocks

operationId: `issueListBlocks`

List issues that are blocked by this issue

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | string | yes | index of the issue |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | IssueList (`IssueList`) | array of `Issue` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/issues/{index}/blocks

operationId: `issueCreateIssueBlocking`

Block the issue given in the body by the issue in path

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | string | yes | index of the issue |

Request body (application/json): `IssueMeta`

| Response | Description | Body |
|---|---|---|
| 201 | Issue (`Issue`) | `Issue` |
| 404 | the issue does not exist |  |

## DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/blocks

operationId: `issueRemoveIssueBlocking`

Unblock the issue given in the body by the issue in path

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | string | yes | index of the issue |

Request body (application/json): `IssueMeta`

| Response | Description | Body |
|---|---|---|
| 200 | Issue (`Issue`) | `Issue` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/issues/{index}/comments

operationId: `issueGetComments`

List all comments on an issue

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the issue |
| `since` | query | string (date-time) |  | if provided, only comments updated since the specified time are returned. |
| `before` | query | string (date-time) |  | if provided, only comments updated before the provided time are returned. |

| Response | Description | Body |
|---|---|---|
| 200 | CommentList (`CommentList`) | array of `Comment` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/issues/{index}/comments

operationId: `issueCreateComment`

Add a comment to an issue

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the issue |

Request body (application/json): `CreateIssueCommentOption`

| Response | Description | Body |
|---|---|---|
| 201 | Comment (`Comment`) | `Comment` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## PATCH /api/v1/repos/{owner}/{repo}/issues/{index}/comments/{id}

operationId: `issueEditCommentDeprecated`
**DEPRECATED**

Edit a comment

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer | yes | this parameter is ignored |
| `id` | path | integer (int64) | yes | id of the comment to edit |

Request body (application/json): `EditIssueCommentOption`

| Response | Description | Body |
|---|---|---|
| 200 | Comment (`Comment`) | `Comment` |
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/comments/{id}

operationId: `issueDeleteCommentDeprecated`
**DEPRECATED**

Delete a comment

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer | yes | this parameter is ignored |
| `id` | path | integer (int64) | yes | id of comment to delete |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/issues/{index}/deadline

operationId: `issueEditIssueDeadline`

Set an issue deadline. If set to null, the deadline is deleted. If using deadline only the date will be taken into account, and time of day ignored.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the issue to create or update a deadline on |

Request body (application/json): `EditDeadlineOption`

| Response | Description | Body |
|---|---|---|
| 201 | IssueDeadline (`IssueDeadline`) | `IssueDeadline` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/issues/{index}/dependencies

operationId: `issueListIssueDependencies`

List an issue's dependencies, i.e all issues that block this issue.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | string | yes | index of the issue |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | IssueList (`IssueList`) | array of `Issue` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/issues/{index}/dependencies

operationId: `issueCreateIssueDependencies`

Make the issue in the url depend on the issue in the form.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | string | yes | index of the issue |

Request body (application/json): `IssueMeta`

| Response | Description | Body |
|---|---|---|
| 201 | Issue (`Issue`) | `Issue` |
| 404 | the issue does not exist |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/dependencies

operationId: `issueRemoveIssueDependencies`

Remove an issue dependency

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | string | yes | index of the issue |

Request body (application/json): `IssueMeta`

| Response | Description | Body |
|---|---|---|
| 200 | Issue (`Issue`) | `Issue` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## GET /api/v1/repos/{owner}/{repo}/issues/{index}/labels

operationId: `issueGetLabels`

Get an issue's labels

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the issue |

| Response | Description | Body |
|---|---|---|
| 200 | LabelList (`LabelList`) | array of `Label` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/issues/{index}/labels

operationId: `issueAddLabel`

Add a label to an issue

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the issue |

Request body (application/json): `IssueLabelsOption`

| Response | Description | Body |
|---|---|---|
| 200 | LabelList (`LabelList`) | array of `Label` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## PUT /api/v1/repos/{owner}/{repo}/issues/{index}/labels

operationId: `issueReplaceLabels`

Replace an issue's labels

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the issue |

Request body (application/json): `IssueLabelsOption`

| Response | Description | Body |
|---|---|---|
| 200 | LabelList (`LabelList`) | array of `Label` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/labels

operationId: `issueClearLabels`

Remove all labels from an issue

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the issue |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/labels/{id}

operationId: `issueRemoveLabel`

Remove a label from an issue

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the issue |
| `id` | path | integer (int64) | yes | id of the label to remove |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |
| 423 | APIRepoArchivedError is an error that is raised when an archived repo should be modified (`repoArchivedError`) |  |

## PUT /api/v1/repos/{owner}/{repo}/issues/{index}/lock

operationId: `issueLockIssue`

Lock an issue

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the issue |

Request body (application/json): `LockIssueOption`

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/lock

operationId: `issueUnlockIssue`

Unlock an issue

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the issue |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/issues/{index}/pin

operationId: `pinIssue`

Pin an Issue

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of issue to pin |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/pin

operationId: `unpinIssue`

Unpin an Issue

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of issue to unpin |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PATCH /api/v1/repos/{owner}/{repo}/issues/{index}/pin/{position}

operationId: `moveIssuePin`

Moves the Pin to the given Position

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of issue |
| `position` | path | integer (int64) | yes | the new position |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/issues/{index}/reactions

operationId: `issueGetIssueReactions`

Get a list reactions of an issue

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the issue |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | ReactionList (`ReactionList`) | array of `Reaction` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/issues/{index}/reactions

operationId: `issuePostIssueReaction`

Add a reaction to an issue

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the issue |

Request body (application/json): `EditReactionOption`

| Response | Description | Body |
|---|---|---|
| 200 | Reaction (`Reaction`) | `Reaction` |
| 201 | Reaction (`Reaction`) | `Reaction` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/reactions

operationId: `issueDeleteIssueReaction`

Remove a reaction from an issue

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the issue |

Request body (application/json): `EditReactionOption`

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/stopwatch/delete

operationId: `issueDeleteStopWatch`

Delete an issue's existing stopwatch.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the issue to stop the stopwatch on |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 403 | Not repo writer, user does not have rights to toggle stopwatch |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 409 | Cannot cancel a non-existent stopwatch |  |

## POST /api/v1/repos/{owner}/{repo}/issues/{index}/stopwatch/start

operationId: `issueStartStopWatch`

Start stopwatch on an issue.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the issue to create the stopwatch on |

| Response | Description | Body |
|---|---|---|
| 201 | APIEmpty is an empty response (`empty`) |  |
| 403 | Not repo writer, user does not have rights to toggle stopwatch |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 409 | Cannot start a stopwatch again if it already exists |  |

## POST /api/v1/repos/{owner}/{repo}/issues/{index}/stopwatch/stop

operationId: `issueStopStopWatch`

Stop an issue's existing stopwatch.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the issue to stop the stopwatch on |

| Response | Description | Body |
|---|---|---|
| 201 | APIEmpty is an empty response (`empty`) |  |
| 403 | Not repo writer, user does not have rights to toggle stopwatch |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 409 | Cannot stop a non-existent stopwatch |  |

## GET /api/v1/repos/{owner}/{repo}/issues/{index}/subscriptions

operationId: `issueSubscriptions`

Get users who subscribed on an issue.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the issue |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | UserList (`UserList`) | array of `User` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/issues/{index}/subscriptions/check

operationId: `issueCheckSubscription`

Check if user is subscribed to an issue

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the issue |

| Response | Description | Body |
|---|---|---|
| 200 | WatchInfo (`WatchInfo`) | `WatchInfo` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PUT /api/v1/repos/{owner}/{repo}/issues/{index}/subscriptions/{user}

operationId: `issueAddSubscription`

Subscribe user to issue

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the issue |
| `user` | path | string | yes | username of the user to subscribe the issue to |

| Response | Description | Body |
|---|---|---|
| 200 | Already subscribed |  |
| 201 | Successfully Subscribed |  |
| 304 | User can only subscribe itself if he is no admin |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/subscriptions/{user}

operationId: `issueDeleteSubscription`

Unsubscribe user from issue

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the issue |
| `user` | path | string | yes | username of the user to unsubscribe from an issue |

| Response | Description | Body |
|---|---|---|
| 200 | Already unsubscribed |  |
| 201 | Successfully Unsubscribed |  |
| 304 | User can only subscribe itself if he is no admin |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/issues/{index}/timeline

operationId: `issueGetCommentsAndTimeline`

List all comments and events on an issue

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the issue |
| `since` | query | string (date-time) |  | if provided, only comments updated since the specified time are returned. |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |
| `before` | query | string (date-time) |  | if provided, only comments updated before the provided time are returned. |

| Response | Description | Body |
|---|---|---|
| 200 | TimelineList (`TimelineList`) | array of `TimelineComment` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/issues/{index}/times

operationId: `issueTrackedTimes`

List an issue's tracked times

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the issue |
| `user` | query | string |  | optional filter by user (available for issue managers) |
| `since` | query | string (date-time) |  | Only show times updated after the given time. This is a timestamp in RFC 3339 format |
| `before` | query | string (date-time) |  | Only show times updated before the given time. This is a timestamp in RFC 3339 format |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | TrackedTimeList (`TrackedTimeList`) | array of `TrackedTime` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/issues/{index}/times

operationId: `issueAddTime`

Add tracked time to a issue

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the issue |

Request body (application/json): `AddTimeOption`

| Response | Description | Body |
|---|---|---|
| 200 | TrackedTime (`TrackedTime`) | `TrackedTime` |
| 400 | APIError is error format response (`error`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/times

operationId: `issueResetTime`

Reset a tracked time of an issue

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the issue to add tracked time to |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 400 | APIError is error format response (`error`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/times/{id}

operationId: `issueDeleteTime`

Delete specific tracked time

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `index` | path | integer (int64) | yes | index of the issue |
| `id` | path | integer (int64) | yes | id of time to delete |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 400 | APIError is error format response (`error`) |  |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/labels

operationId: `issueListLabels`

Get all of a repository's labels

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | LabelList (`LabelList`) | array of `Label` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/labels

operationId: `issueCreateLabel`

Create a label

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

Request body (application/json): `CreateLabelOption`

| Response | Description | Body |
|---|---|---|
| 201 | Label (`Label`) | `Label` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/repos/{owner}/{repo}/labels/{id}

operationId: `issueGetLabel`

Get a single label

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the label to get |

| Response | Description | Body |
|---|---|---|
| 200 | Label (`Label`) | `Label` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PATCH /api/v1/repos/{owner}/{repo}/labels/{id}

operationId: `issueEditLabel`

Update a label

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the label to edit |

Request body (application/json): `EditLabelOption`

| Response | Description | Body |
|---|---|---|
| 200 | Label (`Label`) | `Label` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/labels/{id}

operationId: `issueDeleteLabel`

Delete a label

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | integer (int64) | yes | id of the label to delete |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/milestones

operationId: `issueGetMilestonesList`

Get all of a repository's opened milestones

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `state` | query | string |  | Milestone state, Recognized values are open, closed and all. Defaults to "open" |
| `name` | query | string |  | filter by milestone name |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | MilestoneList (`MilestoneList`) | array of `Milestone` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/repos/{owner}/{repo}/milestones

operationId: `issueCreateMilestone`

Create a milestone

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |

Request body (application/json): `CreateMilestoneOption`

| Response | Description | Body |
|---|---|---|
| 201 | Milestone (`Milestone`) | `Milestone` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/milestones/{id}

operationId: `issueGetMilestone`

Get a milestone

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | string | yes | the milestone to get, identified by ID and if not available by name |

| Response | Description | Body |
|---|---|---|
| 200 | Milestone (`Milestone`) | `Milestone` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PATCH /api/v1/repos/{owner}/{repo}/milestones/{id}

operationId: `issueEditMilestone`

Update a milestone

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | string | yes | the milestone to edit, identified by ID and if not available by name |

Request body (application/json): `EditMilestoneOption`

| Response | Description | Body |
|---|---|---|
| 200 | Milestone (`Milestone`) | `Milestone` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/repos/{owner}/{repo}/milestones/{id}

operationId: `issueDeleteMilestone`

Delete a milestone

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `id` | path | string | yes | the milestone to delete, identified by ID and if not available by name |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
