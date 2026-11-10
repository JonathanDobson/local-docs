---
title: "AI Governance API 1"
source: https://docs.docker.com/reference/api/ai-governance/latest/
---

# AI Governance API 1


[API catalog](/reference/api/) · [AI Governance overview](/reference/api/ai-governance/latest/) · [Product manual](https://docs.docker.com/ai/governance/organization/policies/) · [OpenAPI specification](/reference/api/ai-governance/api.yaml)

API version: 1




## Overview

HTTP+JSON API for managing Docker governance policies and rules.

**Resource model.** An organization owns one or more policies. Each policy
contains a list of rules grouped into a single domain: either `network` or
`filesystem`. A policy's domain is derived from its rule actions; mixing
domains within a single policy is not permitted.

**Lifecycle.** Create a policy with CreatePolicy, then add rules with
CreateRule. Rules can be updated in place with UpdateRule or removed with
DeleteRule. Deleting all rules does not delete the policy itself.

**Rule evaluation.** All rules in a policy are tested against every request.
`deny` always wins: if any rule matches with `decision: deny`, the request
is denied regardless of any `allow` rules.

**Enforcement.** Organization policies take precedence over local sandbox
policies and cannot be overridden by individual users.

**Propagation.** Policy changes take up to five minutes to reach developer
machines after being written.

See the [AI Governance documentation](https://docs.docker.com/ai/sandboxes/governance/)
for product documentation.

## Connecting to the AI Governance API


### bearerAuth

Short-lived JWT obtained by exchanging Docker Hub credentials at
`POST https://hub.docker.com/v2/auth/token`. Pass the JWT in the
`Authorization: Bearer <token>` header. Tokens expire after a short
period; request a fresh one when you receive a `401`.

The `password` field of the token request accepts any of the following
credential types:

| Type | Format | Notes |
|------|--------|-------|
| Password | Plain text | Your Docker Hub account password. |
| Personal Access Token (PAT) | `dckr_pat_*` | Recommended over passwords. Create one under Account Settings → Security. |
| Organization Access Token (OAT) | `dckr_oat_*` | Scoped to an organization. Create one under Organization Settings → Access Tokens. |

PAT and OAT strings can't be used directly as a bearer token. They must
be exchanged at the token endpoint first.

See [Docker Hub authentication](https://docs.docker.com/reference/api/hub/latest/operations/AuthCreateAccessToken/)
for full details.



Server: `https://hub.docker.com/v2`





## Policies

Policy lifecycle management

## Rules

Rule management within an allowlist policy

## Operations

- [GET /orgs/{org_name}/governance/policies](/reference/api/ai-governance/latest/operations/listPolicies/): List policies

- [POST /orgs/{org_name}/governance/policies](/reference/api/ai-governance/latest/operations/createPolicy/): Create policy

- [GET /orgs/{org_name}/governance/policies/{policy_id}](/reference/api/ai-governance/latest/operations/getPolicy/): Get policy

- [DELETE /orgs/{org_name}/governance/policies/{policy_id}](/reference/api/ai-governance/latest/operations/deletePolicy/): Delete policy

- [PATCH /orgs/{org_name}/governance/policies/{policy_id}](/reference/api/ai-governance/latest/operations/updatePolicy/): Update policy

- [POST /orgs/{org_name}/governance/policies/{policy_id}/rules](/reference/api/ai-governance/latest/operations/createRule/): Create rule

- [DELETE /orgs/{org_name}/governance/policies/{policy_id}/rules/{rule_id}](/reference/api/ai-governance/latest/operations/deleteRule/): Delete rule

- [PATCH /orgs/{org_name}/governance/policies/{policy_id}/rules/{rule_id}](/reference/api/ai-governance/latest/operations/updateRule/): Update rule

## Schemas

- [AllowlistV0](/reference/api/ai-governance/latest/schemas/AllowlistV0/)

- [CedarV1Policy](/reference/api/ai-governance/latest/schemas/CedarV1Policy/)

- [CreatePolicyRequest](/reference/api/ai-governance/latest/schemas/CreatePolicyRequest/)

- [CreateRuleRequest](/reference/api/ai-governance/latest/schemas/CreateRuleRequest/)

- [DeletePolicyResponse](/reference/api/ai-governance/latest/schemas/DeletePolicyResponse/)

- [DeleteRuleResponse](/reference/api/ai-governance/latest/schemas/DeleteRuleResponse/)

- [Error](/reference/api/ai-governance/latest/schemas/Error/)

- [HTTPResource](/reference/api/ai-governance/latest/schemas/HTTPResource/)

- [HTTPResources](/reference/api/ai-governance/latest/schemas/HTTPResources/)

- [Policy](/reference/api/ai-governance/latest/schemas/Policy/)

- [PolicySummary](/reference/api/ai-governance/latest/schemas/PolicySummary/)

- [Rule](/reference/api/ai-governance/latest/schemas/Rule/)

- [RuleActions](/reference/api/ai-governance/latest/schemas/RuleActions/)

- [RuleDecision](/reference/api/ai-governance/latest/schemas/RuleDecision/)

- [RuleResources](/reference/api/ai-governance/latest/schemas/RuleResources/)

- [Scope](/reference/api/ai-governance/latest/schemas/Scope/)

- [ScopePatch](/reference/api/ai-governance/latest/schemas/ScopePatch/)

- [UpdatePolicyRequest](/reference/api/ai-governance/latest/schemas/UpdatePolicyRequest/)

- [UpdatePolicyResponse](/reference/api/ai-governance/latest/schemas/UpdatePolicyResponse/)

- [UpdateRuleRequest](/reference/api/ai-governance/latest/schemas/UpdateRuleRequest/)

- [UpdateRuleResponse](/reference/api/ai-governance/latest/schemas/UpdateRuleResponse/)
