# Docker AI Governance Policy API 1 — policies

## GET /v2/orgs/{org_name}/governance/policies

operationId: `listPolicies`

List policies

Returns a shallow summary of the organization's policies, one page at a time. The rule set is not included; use GetPolicy to fetch the full object.

Results are paginated with an opaque cursor. Pass `page_size` to bound the page; if more policies remain, the response includes a non-null `next_page_token` to pass as `page_token` on the next request. Iterate until `next_page_token` is `null`. Treat the token as opaque; do not parse or construct it.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org_name` | path | string | yes | Docker Hub organization name. |
| `page_size` | query | integer |  | Maximum number of policies to return. Defaults to 100 if omitted or zero. The server caps values above 100 at 100. |
| `page_token` | query | string |  | Opaque cursor from a previous response's `next_page_token`. Omit to fetch the first page. |

| Response | Description | Body |
|---|---|---|
| 200 | Object wrapping an array of policy summaries under `data` and a `next_page_token`, which is null on the last page. Rule sets are not included; use GetPolicy to fetch a full policy. | object |
| 400 | Bad request (`InvalidArgument`) | `Error` |
| 401 | Missing or invalid credentials (`Unauthenticated`) | `Error` |
| 403 | Caller lacks the required permission for this org, or the org is not entitled to use governance. (`PermissionDenied`) | `Error` |
| 404 | Not found (`NotFound`) | `Error` |
| 500 | Internal server error (`InternalError`) | `Error` |

## POST /v2/orgs/{org_name}/governance/policies

operationId: `createPolicy`

Create policy

Creates a new policy with an empty rule set. Rules are added separately via the rules sub-resource.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org_name` | path | string | yes | Docker Hub organization name. |

Request body (application/json): `CreatePolicyRequest`

| Response | Description | Body |
|---|---|---|
| 201 | Policy created. Returns the new policy without its rule set. | `Policy` |
| 400 | Bad request (`InvalidArgument`) | `Error` |
| 401 | Missing or invalid credentials (`Unauthenticated`) | `Error` |
| 403 | Caller lacks the required permission for this org, the org is not entitled to use governance (`permission_denied`), or a creation limit has been reached (`limit_exceeded`): the org already has the maximum number of policies, or the policy already has the maximum number of rules. (`Forbidden`) | `Error` |
| 404 | Not found (`NotFound`) | `Error` |
| 409 | Conflict (`Conflict`) | `Error` |
| 500 | Internal server error (`InternalError`) | `Error` |

## GET /v2/orgs/{org_name}/governance/policies/{policy_id}

operationId: `getPolicy`

Get policy

Returns the full policy including its `allowlist_v0` rule set.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org_name` | path | string | yes | Docker Hub organization name. |
| `policy_id` | path | string | yes | Unique policy identifier. |

| Response | Description | Body |
|---|---|---|
| 200 | Full policy including its `allowlist_v0` rule set. | `Policy` |
| 401 | Missing or invalid credentials (`Unauthenticated`) | `Error` |
| 403 | Caller lacks the required permission for this org, or the org is not entitled to use governance. (`PermissionDenied`) | `Error` |
| 404 | Not found (`NotFound`) | `Error` |
| 500 | Internal server error (`InternalError`) | `Error` |

## PATCH /v2/orgs/{org_name}/governance/policies/{policy_id}

operationId: `updatePolicy`

Update policy

Partially updates a policy's metadata. Only fields present in the
request body are updated; absent fields are left unchanged. The `scope`
object is patched per sub-field: sending `teams` replaces that list,
while an omitted sub-field is left untouched and an empty list clears
it (org-wide).

The rule set is not modified here. Use the rule endpoints for that.
At least one field must be present. Returns the policy in both its old
and new states. Changes may take up to five minutes to reach developer
machines.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org_name` | path | string | yes | Docker Hub organization name. |
| `policy_id` | path | string | yes | Unique policy identifier. |

Request body (application/json): `UpdatePolicyRequest`

| Response | Description | Body |
|---|---|---|
| 200 | Policy updated, returns old and new states. | `UpdatePolicyResponse` |
| 400 | Bad request (`InvalidArgument`) | `Error` |
| 401 | Missing or invalid credentials (`Unauthenticated`) | `Error` |
| 403 | Caller lacks the required permission for this org, the org is not entitled to use governance (`permission_denied`), or a creation limit has been reached (`limit_exceeded`): the org already has the maximum number of policies, or the policy already has the maximum number of rules. (`Forbidden`) | `Error` |
| 404 | Not found (`NotFound`) | `Error` |
| 409 | Conflict (`Conflict`) | `Error` |
| 500 | Internal server error (`InternalError`) | `Error` |

## DELETE /v2/orgs/{org_name}/governance/policies/{policy_id}

operationId: `deletePolicy`

Delete policy

Permanently deletes the policy and its rule set. Returns the deleted
policy as a courtesy; its `updated_at` is unchanged by the deletion.
Changes may take up to five minutes to reach developer machines.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org_name` | path | string | yes | Docker Hub organization name. |
| `policy_id` | path | string | yes | Unique policy identifier. |

| Response | Description | Body |
|---|---|---|
| 200 | Policy deleted, returns the deleted policy. | `DeletePolicyResponse` |
| 401 | Missing or invalid credentials (`Unauthenticated`) | `Error` |
| 403 | Caller lacks the required permission for this org, or the org is not entitled to use governance. (`PermissionDenied`) | `Error` |
| 404 | Not found (`NotFound`) | `Error` |
| 500 | Internal server error (`InternalError`) | `Error` |
