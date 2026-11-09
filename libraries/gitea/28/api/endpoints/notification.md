# Gitea API 28.3.0 — notification

## GET /api/v1/notifications

operationId: `notifyGetList`

List users's notification threads

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `all` | query | boolean |  | If true, show notifications marked as read. Default value is false |
| `status-types` | query | array of string |  | Show notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread & pinned. |
| `subject-type` | query | array of string enum: issue, pull, commit, repository |  | filter notifications by subject type |
| `since` | query | string (date-time) |  | Only show notifications updated after the given time. This is a timestamp in RFC 3339 format |
| `before` | query | string (date-time) |  | Only show notifications updated before the given time. This is a timestamp in RFC 3339 format |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | NotificationThreadList (`NotificationThreadList`) | array of `NotificationThread` |

## PUT /api/v1/notifications

operationId: `notifyReadList`

Mark notification threads as read, pinned or unread

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `last_read_at` | query | string (date-time) |  | Describes the last point that notifications were checked. Anything updated since this time will not be updated. |
| `all` | query | string |  | If true, mark all notifications on this repo. Default value is false |
| `status-types` | query | array of string |  | Mark notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread. |
| `to-status` | query | string |  | Status to mark notifications as, Defaults to read. |

| Response | Description | Body |
|---|---|---|
| 205 | NotificationThreadList (`NotificationThreadList`) | array of `NotificationThread` |

## GET /api/v1/notifications/new

operationId: `notifyNewAvailable`

Check if unread notifications exist

| Response | Description | Body |
|---|---|---|
| 200 | Number of unread notifications (`NotificationCount`) | `NotificationCount` |

## GET /api/v1/notifications/threads/{id}

operationId: `notifyGetThread`

Get notification thread by ID

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | id of notification thread |

| Response | Description | Body |
|---|---|---|
| 200 | NotificationThread (`NotificationThread`) | `NotificationThread` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## PATCH /api/v1/notifications/threads/{id}

operationId: `notifyReadThread`

Mark notification thread as read by ID

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | id of notification thread |
| `to-status` | query | string |  | Status to mark notifications as |

| Response | Description | Body |
|---|---|---|
| 205 | NotificationThread (`NotificationThread`) | `NotificationThread` |
| 403 | APIForbiddenError is a forbidden error response (`forbidden`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/repos/{owner}/{repo}/notifications

operationId: `notifyGetRepoList`

List users's notification threads on a specific repo

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `all` | query | boolean |  | If true, show notifications marked as read. Default value is false |
| `status-types` | query | array of string |  | Show notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread & pinned |
| `subject-type` | query | array of string enum: issue, pull, commit, repository |  | filter notifications by subject type |
| `since` | query | string (date-time) |  | Only show notifications updated after the given time. This is a timestamp in RFC 3339 format |
| `before` | query | string (date-time) |  | Only show notifications updated before the given time. This is a timestamp in RFC 3339 format |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | NotificationThreadList (`NotificationThreadList`) | array of `NotificationThread` |

## PUT /api/v1/repos/{owner}/{repo}/notifications

operationId: `notifyReadRepoList`

Mark notification threads as read, pinned or unread on a specific repo

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the repo |
| `repo` | path | string | yes | name of the repo |
| `all` | query | string |  | If true, mark all notifications on this repo. Default value is false |
| `status-types` | query | array of string |  | Mark notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread. |
| `to-status` | query | string |  | Status to mark notifications as. Defaults to read. |
| `last_read_at` | query | string (date-time) |  | Describes the last point that notifications were checked. Anything updated since this time will not be updated. |

| Response | Description | Body |
|---|---|---|
| 205 | NotificationThreadList (`NotificationThreadList`) | array of `NotificationThread` |
