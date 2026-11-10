# Docker Sandboxes API v1 — Network policies

## GET /sandboxes/v1/network-policies

operationId: `getNetworkPoliciesInOwnerScope`

GetNetworkPolicies returns effective and exact views of the same installed generation.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `acceptedSelectorVersions` | query | array of string |  | Omitted versions accept only destination.v1; an unsupported representation fails closed. |

| Response | Description | Body |
|---|---|---|
| 200 | Success | `GetNetworkPoliciesResponse` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## GET /sandboxes/v1/policy-logs

operationId: `listPolicyLogEntriesInOwnerScope`

ListPolicyLogEntries lists observed policy decisions.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `pageSize` | query | integer |  | page_size is an optional page size. Omitted or zero uses the backend default. Unless the operation states otherwise, page-size limits and handling of larger requests are backend-specific; use the backend support guide. Continue with nextPageToken until it is empty. |
| `pageToken` | query | string |  | page_token is an opaque continuation token. |
| `filter` | query | string |  | filter is comma-separated exact-match field=value terms; the portable field is domain. |
| `since` | query | string (date-time) |  | An RFC 3339 timestamp, for example 2026-01-01T12:00:00Z. Fractional seconds may contain up to nine digits. The supported range is 0001-01-01T00:00:00Z through 9999-12-31T23:59:59.999999999Z. |
| `until` | query | string (date-time) |  | An RFC 3339 timestamp, for example 2026-01-01T12:00:00Z. Fractional seconds may contain up to nine digits. The supported range is 0001-01-01T00:00:00Z through 9999-12-31T23:59:59.999999999Z. |

| Response | Description | Body |
|---|---|---|
| 200 | Success | `ListPolicyLogEntriesResponse` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## GET /sandboxes/v1/sandboxes/{sandbox}/network-policies

operationId: `getNetworkPolicies`

GetNetworkPolicies returns effective and exact views of the same installed generation.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `sandbox` | path | string | yes | The sandbox id. |
| `acceptedSelectorVersions` | query | array of string |  | Omitted versions accept only destination.v1; an unsupported representation fails closed. |

| Response | Description | Body |
|---|---|---|
| 200 | Success | `GetNetworkPoliciesResponse` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |

## GET /sandboxes/v1/sandboxes/{sandbox}/policy-logs

operationId: `listPolicyLogEntries`

ListPolicyLogEntries lists observed policy decisions.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `sandbox` | path | string | yes | The sandbox id. |
| `pageSize` | query | integer |  | page_size is an optional page size. Omitted or zero uses the backend default. Unless the operation states otherwise, page-size limits and handling of larger requests are backend-specific; use the backend support guide. Continue with nextPageToken until it is empty. |
| `pageToken` | query | string |  | page_token is an opaque continuation token. |
| `filter` | query | string |  | filter is comma-separated exact-match field=value terms; the portable field is domain. |
| `since` | query | string (date-time) |  | An RFC 3339 timestamp, for example 2026-01-01T12:00:00Z. Fractional seconds may contain up to nine digits. The supported range is 0001-01-01T00:00:00Z through 9999-12-31T23:59:59.999999999Z. |
| `until` | query | string (date-time) |  | An RFC 3339 timestamp, for example 2026-01-01T12:00:00Z. Fractional seconds may contain up to nine digits. The supported range is 0001-01-01T00:00:00Z through 9999-12-31T23:59:59.999999999Z. |

| Response | Description | Body |
|---|---|---|
| 200 | Success | `ListPolicyLogEntriesResponse` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |
