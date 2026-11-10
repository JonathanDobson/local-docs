# Docker AI Governance Audit Logs API 1 — schemas

## ApplicationRateLimitError

Type: allOf(`Error`, object)

## AuditEvent

| Field | Type | Required | Description |
|---|---|---|---|
| `audit_event_id` | string (uuid) | yes | Unique audit event ID. |
| `org_id` | string (uuid) | yes | ID of the organization that owns the event. |
| `event_type` | string | yes | Fully qualified event schema name. |
| `category` | string |  | Audit event category. |
| `decision` | string |  | Governance decision for evaluation records. |
| `action_type` | string |  | Action-specific payload discriminator. |
| `enforcement_mode` | string |  | Enforcement mode in effect for the decision. |
| `audit_session_id` | string |  | Session that produced the event. |
| `username` | string |  | Docker username associated with the event. |
| `created_at` | string (date-time) |  | Time Docker recorded the event. |
| `ingested_at` | string (date-time) |  | Time Docker ingested the event into cloud storage. |
| `payload` | object |  | Event-specific audit record fields. |

## Error

| Field | Type | Required | Description |
|---|---|---|---|
| `error` | string | yes | Human-readable error message. |

## ListAuditEventsResponse

| Field | Type | Required | Description |
|---|---|---|---|
| `events` | array of `AuditEvent` | yes |  |
| `next_page_token` | string | yes | Opaque cursor for the next page. Empty when no more events remain. |

