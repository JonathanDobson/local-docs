# Docker HUB API 2-beta — groups

## GET /v2/orgs/{org_name}/groups

operationId: `getV2OrgsByOrgNameGroups`

Get groups of an organization

Get groups of an organization.

This operation accepts bearer tokens issued from organization access tokens (OATs). The token must have the required resource access and scopes.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org_name` | path | string | yes | Name of the organization (namespace). |
| `page` | query | integer |  | Page number (starts on 1). |
| `page_size` | query | integer |  | Number of items (rows) per page. |
| `username` | query | string |  | Get groups for the specified username in the organization. |
| `search` | query | string |  | Get groups for the specified group in the organization. |

| Response | Description | Body |
|---|---|---|
| 200 |  | object |
| 401 | Unauthorized (`unauthorized`) | `error` |
| 403 | Forbidden (`forbidden`) | `error` |
| 404 | Not Found (`not_found`) | `error` |

## POST /v2/orgs/{org_name}/groups

operationId: `postV2OrgsByOrgNameGroups`

Create a new group

Create a new group within an organization.

This operation accepts bearer tokens issued from organization access tokens (OATs). The token must have the required resource access and scopes.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org_name` | path | string | yes | Name of the organization (namespace). |

Request body (application/json): object

| Response | Description | Body |
|---|---|---|
| 201 | Group created successfully | `org_group` |
| 400 | Bad Request (`bad_request`) | `error` |
| 401 | Unauthorized (`unauthorized`) | `error` |
| 403 | Forbidden (`forbidden`) | `error` |

## GET /v2/orgs/{org_name}/groups/{group_name}

operationId: `getV2OrgsByOrgNameGroupsByGroupName`

Get a group of an organization

Get a group of an organization.

This operation accepts bearer tokens issued from organization access tokens (OATs). The token must have the required resource access and scopes.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org_name` | path | string | yes | Name of the organization (namespace). |
| `group_name` | path | string | yes | Name of the group (team) in the organization. |

| Response | Description | Body |
|---|---|---|
| 200 |  | `org_group` |
| 401 | Unauthorized (`unauthorized`) | `error` |
| 403 | Forbidden (`forbidden`) | `error` |
| 404 | Not Found (`not_found`) | `error` |

## PUT /v2/orgs/{org_name}/groups/{group_name}

operationId: `putV2OrgsByOrgNameGroupsByGroupName`

Update the details for an organization group

Update the details for an organization group.

This operation accepts bearer tokens issued from organization access tokens (OATs). The token must have the required resource access and scopes.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org_name` | path | string | yes | Name of the organization (namespace). |
| `group_name` | path | string | yes | Name of the group (team) in the organization. |

Request body (application/json): object

| Response | Description | Body |
|---|---|---|
| 200 |  | `org_group` |
| 401 | Unauthorized (`unauthorized`) | `error` |
| 403 | Forbidden (`forbidden`) | `error` |
| 404 | Not Found (`not_found`) | `error` |

## PATCH /v2/orgs/{org_name}/groups/{group_name}

operationId: `patchV2OrgsByOrgNameGroupsByGroupName`

Update some details for an organization group

Update some details for an organization group.

This operation accepts bearer tokens issued from organization access tokens (OATs). The token must have the required resource access and scopes.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org_name` | path | string | yes | Name of the organization (namespace). |
| `group_name` | path | string | yes | Name of the group (team) in the organization. |

Request body (application/json): object

| Response | Description | Body |
|---|---|---|
| 200 |  | `org_group` |
| 401 | Unauthorized (`unauthorized`) | `error` |
| 403 | Forbidden (`forbidden`) | `error` |
| 404 | Not Found (`not_found`) | `error` |

## DELETE /v2/orgs/{org_name}/groups/{group_name}

operationId: `deleteV2OrgsByOrgNameGroupsByGroupName`

Delete an organization group

Delete an organization group.

This operation accepts bearer tokens issued from organization access tokens (OATs). The token must have the required resource access and scopes.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org_name` | path | string | yes | Name of the organization (namespace). |
| `group_name` | path | string | yes | Name of the group (team) in the organization. |

| Response | Description | Body |
|---|---|---|
| 204 | Group deleted successfully |  |
| 401 | Unauthorized (`unauthorized`) | `error` |
| 403 | Forbidden (`forbidden`) | `error` |
| 404 | Not Found (`not_found`) | `error` |

## GET /v2/orgs/{org_name}/groups/{group_name}/members

operationId: `getV2OrgsByOrgNameGroupsByGroupNameMembers`

List members of a group

List the members (users) that are in a group.
If user is owner of the org or has otherwise elevated permissions, they can search by email and the result will also contain emails.

This operation accepts bearer tokens issued from organization access tokens (OATs). The token must have the required resource access and scopes.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org_name` | path | string | yes | Name of the organization (namespace). |
| `group_name` | path | string | yes | Name of the group (team) in the organization. |
| `page` | query | integer |  | Page number (starts on 1). |
| `page_size` | query | integer |  | Number of items (rows) per page. |
| `search` | query | string |  | Search members by username, full_name or email |

| Response | Description | Body |
|---|---|---|
| 200 |  | object |
| 401 | Unauthorized (`unauthorized`) | `error` |
| 403 | Forbidden (`forbidden`) | `error` |
| 404 | Not Found (`not_found`) | `error` |

## POST /v2/orgs/{org_name}/groups/{group_name}/members

operationId: `postV2OrgsByOrgNameGroupsByGroupNameMembers`

Add a member to a group

Add a member to a group.

This operation accepts bearer tokens issued from organization access tokens (OATs). The token must have the required resource access and scopes.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org_name` | path | string | yes | Name of the organization (namespace). |
| `group_name` | path | string | yes | Name of the group (team) in the organization. |

| Response | Description | Body |
|---|---|---|
| 200 | OK |  |
| 401 | Unauthorized (`unauthorized`) | `error` |
| 403 | Forbidden (`forbidden`) | `error` |
| 404 | Not Found (`not_found`) | `error` |
| 500 | Internal (`internal_error`) | `error` |

## DELETE /v2/orgs/{org_name}/groups/{group_name}/members/{username}

operationId: `deleteV2OrgsByOrgNameGroupsByGroupNameMembersByUsername`

Remove a user from a group

Remove a user from a group.

This operation accepts bearer tokens issued from organization access tokens (OATs). The token must have the required resource access and scopes.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org_name` | path | string | yes | Name of the organization (namespace). |
| `group_name` | path | string | yes | Name of the group (team) in the organization. |
| `username` | path | string | yes | Username, identifier for the user (namespace, DockerID). |

| Response | Description | Body |
|---|---|---|
| 204 | User removed successfully |  |
| 401 | Unauthorized (`unauthorized`) | `error` |
| 403 | Forbidden (`forbidden`) | `error` |
| 404 | Not Found (`not_found`) | `error` |
