# Docker HUB API 2-beta — invites

## GET /v2/orgs/{org_name}/invites

operationId: `getV2OrgsByOrgNameInvites`

List org invites

Return all pending invites for a given org, only team owners can call this endpoint

This operation accepts bearer tokens issued from organization access tokens (OATs). The token must have the required resource access and scopes.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org_name` | path | string | yes | Name of the organization (namespace). |

| Response | Description | Body |
|---|---|---|
| 200 |  | object |
| 401 | Unauthorized (`unauthorized`) | `error` |
| 403 | Forbidden (`forbidden`) | `error` |
| 404 | Not Found (`not_found`) | `error` |

## DELETE /v2/invites/{id}

operationId: `deleteV2InvitesById`

Cancel an invite

Mark the invite as cancelled so it doesn't show up on the list of pending invites

This operation accepts bearer tokens issued from organization access tokens (OATs). The token must have the required resource access and scopes.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | ID of the invitation. |

| Response | Description | Body |
|---|---|---|
| 204 |  |  |
| 401 | Unauthorized (`unauthorized`) | `error` |
| 403 | Forbidden (`forbidden`) | `error` |
| 404 | Not Found (`not_found`) | `error` |

## PATCH /v2/invites/{id}/resend

operationId: `patchV2InvitesByIdResend`

Resend an invite

Resend a pending invite to the user, any org owner can resend an invite

This operation accepts bearer tokens issued from organization access tokens (OATs). The token must have the required resource access and scopes.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | ID of the invitation. |

| Response | Description | Body |
|---|---|---|
| 204 |  |  |
| 401 | Unauthorized (`unauthorized`) | `error` |
| 403 | Forbidden (`forbidden`) | `error` |
| 404 | Not Found (`not_found`) | `error` |

## POST /v2/invites/bulk

operationId: `postV2InvitesBulk`

Bulk create invites

Create multiple invites by emails or DockerIDs. Only a team owner can create invites.

This operation accepts bearer tokens issued from organization access tokens (OATs). The token must have the required resource access and scopes.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `X-Analytics-Client-Feature` | header | string |  | Optional string that indicates the feature used to submit the bulk invites (e.g.'file', 'web') |

| Response | Description | Body |
|---|---|---|
| 202 | Accepted | `bulk_invite` |
| 400 | Bad Request (`bad_request`) | `error` |
| 409 | Conflict (`conflict`) | `error` |
