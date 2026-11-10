# Docker HUB API 2-beta — orgs

## GET /v2/orgs/{org_name}/members

operationId: `getV2OrgsByOrgNameMembers`

List org members

Returns a list of members for an organization.

_The following fields are only visible to orgs with insights enabled._

- `last_logged_in_at`
- `last_seen_at`
- `last_desktop_version`

To make visible, please see [View Insights for organization users](https://docs.docker.com/accounts/organization/insights/#view-insights-for-organization-users).

This operation accepts bearer tokens issued from organization access tokens (OATs). The token must have the required resource access and scopes.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org_name` | path | string | yes | Name of the organization (namespace). |
| `search` | query | string |  | Search members by username, full_name or email |
| `page` | query | integer |  | Page number (starts on 1). |
| `page_size` | query | integer |  | Number of items (rows) per page. |
| `invites` | query | boolean |  | Include invites in the response. |
| `type` | query | string enum: all, invitee, member |  | Filter members by membership type. |
| `role` | query | string enum: owner, editor, member |  | Filter members by their organization role. |

| Response | Description | Body |
|---|---|---|
| 200 | List of members | `org_member_paginated` |
| 400 | Bad Request (`bad_request`) | `error` |
| 401 | Unauthorized (`unauthorized`) | `error` |
| 403 | Forbidden (`forbidden`) | `error` |
| 404 | Not Found (`not_found`) | `error` |

## GET /v2/orgs/{org_name}/members/export

operationId: `getV2OrgsByOrgNameMembersExport`

Export org members CSV

Export members of an organization as a CSV

This operation accepts bearer tokens issued from organization access tokens (OATs). The token must have the required resource access and scopes.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org_name` | path | string | yes | Name of the organization (namespace). |

| Response | Description | Body |
|---|---|---|
| 200 | Exported members | string |
| 400 | Bad Request (`bad_request`) | `error` |
| 401 | Unauthorized (`unauthorized`) | `error` |
| 403 | Forbidden (`forbidden`) | `error` |
| 404 | Not Found (`not_found`) | `error` |

## PUT /v2/orgs/{org_name}/members/{username}

operationId: `putV2OrgsByOrgNameMembersByUsername`

Update org member (role)

Updates the role of a member in the organization.
***Only users in the "owners" group of the organization can use this endpoint.***

This operation accepts bearer tokens issued from organization access tokens (OATs). The token must have the required resource access and scopes.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org_name` | path | string | yes | Name of the organization (namespace). |
| `username` | path | string | yes | Username, identifier for the user (namespace, DockerID). |

Request body (application/json): object

| Response | Description | Body |
|---|---|---|
| 200 | Member role updated | `org_member` |
| 400 | Bad Request (`bad_request`) | `error` |
| 401 | Unauthorized (`unauthorized`) | `error` |
| 403 | Forbidden (`forbidden`) | `error` |
| 404 | Not Found (`not_found`) | `error` |

## DELETE /v2/orgs/{org_name}/members/{username}

operationId: `deleteV2OrgsByOrgNameMembersByUsername`

Remove member from org

Removes the member from the org, ie. all groups in the org, unless they're the last owner

This operation accepts bearer tokens issued from organization access tokens (OATs). The token must have the required resource access and scopes.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org_name` | path | string | yes | Name of the organization (namespace). |
| `username` | path | string | yes | Username, identifier for the user (namespace, DockerID). |

| Response | Description | Body |
|---|---|---|
| 204 | Member removed successfully |  |
| 400 | Bad Request (`bad_request`) | `error` |
| 401 | Unauthorized (`unauthorized`) | `error` |
| 403 | Forbidden (`forbidden`) | `error` |
| 404 | Not Found (`not_found`) | `error` |
