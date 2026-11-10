# Docker AI Governance Policy API 1 — rules

## POST /v2/orgs/{org_name}/governance/policies/{policy_id}/rules

operationId: `createRule`

Create rule

Adds a rule to the policy's rule set. All rules in a policy must share
the same domain (`network`, which includes HTTP, or `filesystem`);
mixing domains is rejected. A single rule cannot mix L4 network and L7
HTTP actions.

**Network** actions: `connect:tcp`, `connect:udp`. Resources are
hostnames (for example, `example.com`), wildcard subdomains (`*.example.com`
for one level, `**.example.com` for any depth), hostnames with an optional
port (for example, `example.com:443`), or CIDRs in IPv4 or IPv6 notation
(for example, `10.0.0.0/8` or `2001:db8::/32`).

**Filesystem** actions: `read`, `write`. Resources are paths (for example,
`/data`). Use `*` to match within a single path segment and `**` to match
recursively across segments (for example, `/data/**`).

**HTTP** actions identify request methods, such as `request:get` and
`request:post`. Use `http_resources` to identify the host, optional port,
and absolute path glob. HTTP rules must not supply `resources`.

Changes may take up to five minutes to reach developer machines.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org_name` | path | string | yes | Docker Hub organization name. |
| `policy_id` | path | string | yes | Unique policy identifier. |

Request body (application/json): `CreateRuleRequest`

| Response | Description | Body |
|---|---|---|
| 201 | Rule created and added to the policy's rule set. | `Rule` |
| 400 | Bad request (`InvalidArgument`) | `Error` |
| 401 | Missing or invalid credentials (`Unauthenticated`) | `Error` |
| 403 | Caller lacks the required permission for this org, the org is not entitled to use governance (`permission_denied`), or a creation limit has been reached (`limit_exceeded`): the org already has the maximum number of policies, or the policy already has the maximum number of rules. (`Forbidden`) | `Error` |
| 404 | Not found (`NotFound`) | `Error` |
| 409 | Conflict (`Conflict`) | `Error` |
| 500 | Internal server error (`InternalError`) | `Error` |

## PATCH /v2/orgs/{org_name}/governance/policies/{policy_id}/rules/{rule_id}

operationId: `updateRule`

Update rule

Partially updates a rule. Only fields present in the request body are
updated; absent fields are left unchanged. Returns the rule in both its
old and new states.

Changing `actions` across domains (for example, from network actions to
filesystem actions) is rejected while other rules remain in the policy.
When changing a rule between L4 network and L7 HTTP, supply the matching
`resources` or `http_resources` in the same request. Changes may take up
to five minutes to reach developer machines.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org_name` | path | string | yes | Docker Hub organization name. |
| `policy_id` | path | string | yes | Unique policy identifier. |
| `rule_id` | path | string | yes | Unique rule identifier within the policy. |

Request body (application/json): `UpdateRuleRequest`

| Response | Description | Body |
|---|---|---|
| 200 | Rule updated, returns old and new states. | `UpdateRuleResponse` |
| 400 | Bad request (`InvalidArgument`) | `Error` |
| 401 | Missing or invalid credentials (`Unauthenticated`) | `Error` |
| 403 | Caller lacks the required permission for this org, or the org is not entitled to use governance. (`PermissionDenied`) | `Error` |
| 404 | Not found (`NotFound`) | `Error` |
| 409 | Conflict (`Conflict`) | `Error` |
| 500 | Internal server error (`InternalError`) | `Error` |

## DELETE /v2/orgs/{org_name}/governance/policies/{policy_id}/rules/{rule_id}

operationId: `deleteRule`

Delete rule

Deletes a rule from the policy. Returns the deleted rule. Changes may
take up to five minutes to reach developer machines.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org_name` | path | string | yes | Docker Hub organization name. |
| `policy_id` | path | string | yes | Unique policy identifier. |
| `rule_id` | path | string | yes | Unique rule identifier within the policy. |

| Response | Description | Body |
|---|---|---|
| 200 | Rule deleted, returns the deleted rule. | `DeleteRuleResponse` |
| 401 | Missing or invalid credentials (`Unauthenticated`) | `Error` |
| 403 | Caller lacks the required permission for this org, or the org is not entitled to use governance. (`PermissionDenied`) | `Error` |
| 404 | Not found (`NotFound`) | `Error` |
| 500 | Internal server error (`InternalError`) | `Error` |
