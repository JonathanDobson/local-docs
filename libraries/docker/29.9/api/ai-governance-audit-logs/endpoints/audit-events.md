# Docker AI Governance Audit Logs API 1 — audit-events

## GET /v2/auditlogs/governance/{org_name}

operationId: `listAuditEvents`

List audit events

Returns audit events for the organization in reverse chronological
order. Pass `next_page_token` from one response as `page_token` in the
next request to continue listing events.

Every request covers a time range of 30 days or less. If `to` is
omitted, it defaults to the request time. If `from` is omitted, it
defaults to 30 days before `to`. `from` must be earlier than `to`.
Text search uses the same defaults and requires at least three
bytes after trimming whitespace.

The page token preserves the resolved time range. Keep other filters
unchanged on later pages. Omit `from` and `to` or supply timestamps that
match the token's range.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `org_name` | path | string | yes | Organization name. The value must match the organization associated with the OAT. |
| `from` | query | string (date-time) |  | Include events created at or after this RFC 3339 timestamp. Defaults to 30 days before the effective `to` on the first page. Must be earlier than `to`, with a range of no more than 30 days. On later pages, omit this parameter or use the timestamp preserved in the page token. |
| `to` | query | string (date-time) |  | Include events created at or before this RFC 3339 timestamp. Defaults to the request time on the first page. On later pages, omit this parameter or use the timestamp preserved in the page token. |
| `audit_session_id` | query | string |  | Return events from this audit session. |
| `username` | query | string |  | Return events associated with this Docker username. |
| `decision` | query | string |  | Return events with this exact audit decision value. |
| `enforcement_mode` | query | string |  | Return events with this exact enforcement mode, such as `audit`, `warn`, or `enforce`. |
| `action_type` | query | string |  | Return events with this exact action type. |
| `query` | query | string |  | Case-insensitive text search across username, action type, decision, and event type. Uses the same default time range as other list requests. The trimmed value must be between 3 and 256 bytes. |
| `resource_id` | query | string |  | Case-insensitive prefix match against the resource ID in the event payload. The trimmed value must not exceed 256 bytes. |
| `agent` | query | string |  | Exact match against the agent in the event payload. The trimmed value must not exceed 256 bytes. |
| `page_size` | query | integer (int32) |  | Number of events to return. Defaults to 25; 0 also uses the default. Values above 100 are capped at 100. Negative values are rejected. |
| `page_token` | query | string |  | Opaque cursor from `next_page_token` in the previous response. Preserves the resolved time range; pass it unchanged. |

| Response | Description | Body |
|---|---|---|
| 200 | Paginated audit events. | `ListAuditEventsResponse` |
| 400 | Invalid timestamp, page size, page token, filter, or search window. (`BadRequest`) | `Error` |
| 401 | Missing, malformed, invalid, or expired OAT. (`Unauthenticated`) | `Error` |
| 403 | The OAT lacks permission, lacks organization identity, or belongs to another organization. (`Forbidden`) | `Error` |
| 408 | Request deadline exceeded. (`RequestTimeout`) | `Error` |
| 429 | The organization or source IP address exceeded a request limit. Application responses include the configured quota, window, and stable error code. Gateway responses can use a different body and omit these fields. Honor `Retry-After` when present; otherwise use exponential backoff. (`RateLimited`) | anyOf(`ApplicationRateLimitError`, `Error`) |
| 500 | Unexpected server error. (`InternalError`) | `Error` |
| 503 | The audit store or an authentication dependency is unavailable, or the search timed out. Retry with exponential backoff. For a search timeout, use a narrower time range or a simpler query. (`ServiceUnavailable`) | `Error` |
