# Docker HUB API 2-beta — org-settings

## GET /v2/orgs/{org_name}/settings

operationId: `getV2OrgsByNameSettings`

Get organization settings

Returns organization settings by name.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org_name` | path | string | yes | Name of the organization (namespace). |

| Response | Description | Body |
|---|---|---|
| 200 | OK | `orgSettings` |
| 401 | Unauthorized (`Unauthorized`) | `error` |
| 403 | Forbidden (`Forbidden`) | `error` |
| 404 | Not Found (`NotFound`) | `error` |

## PUT /v2/orgs/{org_name}/settings

operationId: `putV2OrgsByNameSettings`

Update organization settings

Updates an organization's settings. Some settings are only used when the organization is on a business subscription.

***Only users with administrative privileges for the organization (owner role) can modify these settings.***

The following settings are only used on a business subscription:
- `restricted_images`

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org_name` | path | string | yes | Name of the organization (namespace). |

Request body (application/json): object

| Response | Description | Body |
|---|---|---|
| 200 | OK | `orgSettings` |
| 401 | Unauthorized (`Unauthorized`) | `error` |
| 403 | Forbidden (`Forbidden`) | `error` |
| 404 | Not Found (`NotFound`) | `error` |
