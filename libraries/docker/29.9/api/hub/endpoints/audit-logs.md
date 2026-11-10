# Docker HUB API 2-beta — audit-logs

## GET /v2/auditlogs/{account}/actions

operationId: `AuditLogs_ListAuditActions`

List audit log actions

List audit log actions for a namespace to be used as a filter for querying audit log events.

This operation accepts bearer tokens issued from organization access tokens (OATs). The token must have the required resource access and scopes.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `account` | path | string | yes | Namespace to query audit log actions for. |

| Response | Description | Body |
|---|---|---|
| 200 | A successful response. | `GetAuditActionsResponse` |
| 429 |  |  |
| 500 |  | `error` |
| default | An unexpected error response. | `error` |

## GET /v2/auditlogs/{account}

operationId: `AuditLogs_ListAuditLogs`

List audit log events

List audit log events for a given namespace.

This operation accepts bearer tokens issued from organization access tokens (OATs). The token must have the required resource access and scopes.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `account` | path | string | yes | Namespace to query audit logs for. |
| `action` | query | string |  | action name one of ["repo.tag.push", ...]. Optional parameter to filter specific audit log actions. |
| `name` | query | string |  | name. Optional parameter to filter audit log events to a specific name. For repository events, this is the name of the repository. For organization events, this is the name of the organization. For team member events, this is the username of the team member. |
| `actor` | query | string |  | actor name. Optional parameter to filter audit log events to the specific user who triggered the event. |
| `from` | query | string (date-time) |  | Start of the time window you wish to query audit events for. |
| `to` | query | string (date-time) |  | End of the time window you wish to query audit events for. |
| `page` | query | integer |  | Page number (starts on 1). |
| `page_size` | query | integer |  | Number of items (rows) per page. |

| Response | Description | Body |
|---|---|---|
| 200 | A successful response. | `GetAuditLogsResponse` |
| 429 |  |  |
| 500 |  | `error` |
| default | An unexpected error response. | `error` |
