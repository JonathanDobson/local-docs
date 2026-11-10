# Docker AI Governance Policy API 1 — schemas

## AllowlistV0

Network, HTTP, or filesystem allowlist containing a list of rules. Present on
Policy when `PolicySummary.type` is `allowlist_v0`; omitted when the
policy has no rules yet. All rules in an allowlist share the same domain.
All rules are evaluated on every request: `deny` always wins over `allow`.

| Field | Type | Required | Description |
|---|---|---|---|
| `domain` | string enum: network, filesystem |  | The access-control domain shared by all rules in this allowlist. Derived from rule actions: network actions (`connect:tcp`, `connect:udp`) produce `network`; filesystem actions (`read`, `write`) produce `filesystem`. Present when `rules` is non-empty; absent when the allowlist has no rules. |
| `rules` | array of `Rule` | yes |  |

## CedarV1Policy

Cedar:V1 policy body. Present on `Policy` when `PolicySummary.type` is `cedar_v1`. Cedar policies encode their rules directly in `text` rather than in the rules sub-resource; the rules endpoints are not available for Cedar policies.

| Field | Type | Required | Description |
|---|---|---|---|
| `text` | string | yes | One or more Cedar `permit` or `forbid` statements. Must be syntactically valid Cedar and must not carry an `@id` annotation (IDs are server-assigned). |
| `schema_url` | string | yes | URL of the Cedar schema this policy was authored against. The evaluator looks up the schema by this URL from its built-in registry. Use `https://schemas.docker.com/policy/cedar/v1/mcp/v0` for MCP policies. |

## CreatePolicyRequest

Fields required to create a new policy. Omitting `cedar_v1` creates an `allowlist_v0` policy with an empty rule set. Supplying `cedar_v1` creates a Cedar:V1 policy; rules are embedded in the Cedar text rather than managed via the rules sub-resource.

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | yes | Policy name, unique within the organization. |
| `scope` | `Scope` |  |  |
| `cedar_v1` | `CedarV1Policy` |  |  |

## CreateRuleRequest

Fields required to create a new rule within a policy's rule set.

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | yes | Human-readable label for the rule. |
| `actions` | `RuleActions` | yes |  |
| `resources` | `RuleResources` |  |  |
| `http_resources` | `HTTPResources` |  |  |
| `decision` | `RuleDecision` | yes |  |

## DeletePolicyResponse

The full deleted policy.

| Field | Type | Required | Description |
|---|---|---|---|
| `deleted` | `Policy` | yes |  |

## DeleteRuleResponse

The deleted rule.

| Field | Type | Required | Description |
|---|---|---|---|
| `deleted` | `Rule` | yes |  |

## Error

Error envelope returned on all non-2xx responses.

| Field | Type | Required | Description |
|---|---|---|---|
| `error` | object | yes | Error detail. |

## HTTPResource

| Field | Type | Required | Description |
|---|---|---|---|
| `host` | string | yes | Domain name or domain glob without a URL scheme or port. Use the separate `port` field to restrict the target to one port. |
| `port` | integer |  | Optional destination port. Omit it to match every port. |
| `path` | string | yes | Absolute HTTP path glob. `*` matches one segment and `**` matches any depth, including the bare path. |

## HTTPResources

HTTP request targets. Required for HTTP rules and forbidden for network and filesystem rules. A request matches when any target matches.

Type: array of `HTTPResource`

## Policy

Full policy representation. Exactly one of `allowlist_v0` or `cedar_v1` is present, depending on the policy type.

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | yes |  |
| `name` | string | yes | Human-readable label, unique within the organization. |
| `org` | string | yes |  |
| `scope` | `Scope` | yes |  |
| `created_at` | string (date-time) | yes |  |
| `updated_at` | string (date-time) | yes |  |
| `allowlist_v0` | `AllowlistV0` |  |  |
| `cedar_v1` | `CedarV1Policy` |  |  |

## PolicySummary

Shallow policy representation returned by ListPolicies. Excludes the rule set.

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | yes |  |
| `name` | string | yes | Human-readable label, unique within the organization. |
| `org` | string | yes |  |
| `scope` | `Scope` | yes |  |
| `created_at` | string (date-time) | yes |  |
| `updated_at` | string (date-time) | yes |  |
| `type` | string enum: allowlist_v0, cedar_v1 | yes | Identifies the policy type. `allowlist_v0` for network, HTTP, and filesystem allowlist policies; `cedar_v1` for Cedar language policies. |

## Rule

A single allow or deny rule within an allowlist policy.

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | yes |  |
| `name` | string | yes | Human-readable label for the rule. |
| `actions` | `RuleActions` | yes |  |
| `resources` | `RuleResources` |  |  |
| `http_resources` | `HTTPResources` |  |  |
| `decision` | `RuleDecision` | yes |  |

## RuleActions

Network actions: `connect:tcp`, `connect:udp`. Filesystem actions: `read`, `write`. HTTP actions: `request:get`, `request:post`, `request:put`, `request:delete`, `request:patch`, `request:head`, `request:options`, `request:connect`, `request:trace`. All actions in a rule must belong to the same layer; mixing HTTP, network, or filesystem actions in one rule is rejected.

Type: array of string enum: connect:tcp, connect:udp, read, write, request:get, request:post, request:put, request:delete, request:patch, request:head, request:options, request:connect

## RuleDecision

Outcome applied when this rule matches a request. `deny` always wins: if any rule in the policy matches with `decision: deny`, the request is denied even if other rules match with `decision: allow`.

Type: string enum: allow, deny

## RuleResources

Network domain: hostnames (for example, `example.com`), wildcard subdomains (`*.example.com` or `**.example.com`), hostnames with port (for example, `example.com:443`), or CIDRs in IPv4 or IPv6 notation (for example, `10.0.0.0/8` or `2001:db8::/32`). Filesystem domain: paths (for example, `/data`); `*` matches within one path segment, `**` matches recursively (for example, `/data/**`). Required for network and filesystem rules and forbidden for HTTP rules.

Type: array of string

## Scope

Restricts the policy to specific teams. An empty or absent list means the policy applies org-wide.

| Field | Type | Required | Description |
|---|---|---|---|
| `teams` | array of string |  | Team IDs the policy applies to. Each must be a valid team in the organization. |

## ScopePatch

Per-sub-field patch of a policy's scope. An omitted sub-field is left unchanged; a present list replaces that dimension, and an empty list clears it (making the policy org-wide for that dimension).

| Field | Type | Required | Description |
|---|---|---|---|
| `teams` | array of string |  |  |

## UpdatePolicyRequest

Partial update of a policy. Only fields present in the body are updated; absent fields are left unchanged. At least one field must be present. For `cedar_v1` policies, supply `cedar_v1` to replace the policy text; `name` and `scope` may be combined freely.

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  | Policy name, unique within the organization. |
| `scope` | `ScopePatch` |  |  |
| `cedar_v1` | `CedarV1Policy` |  |  |

## UpdatePolicyResponse

The full policy before and after the update.

| Field | Type | Required | Description |
|---|---|---|---|
| `old` | `Policy` | yes |  |
| `new` | `Policy` | yes |  |

## UpdateRuleRequest

Partial update. Only fields present in the body are updated; absent fields are left unchanged.

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  | Human-readable label for the rule. |
| `actions` | `RuleActions` |  |  |
| `resources` | `RuleResources` |  |  |
| `http_resources` | `HTTPResources` |  |  |
| `decision` | `RuleDecision` |  |  |

## UpdateRuleResponse

The rule state before and after the update.

| Field | Type | Required | Description |
|---|---|---|---|
| `old` | `Rule` | yes |  |
| `new` | `Rule` | yes |  |

