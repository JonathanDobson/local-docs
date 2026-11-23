# Stripe API 2023-10-16 — `issuing_authorization_network_data` object

| Field | Type | Required | Description |
|---|---|---|---|
| `acquiring_institution_id` | string |  | Identifier assigned to the acquirer by the card network. Sometimes this value is not provided by the network; in this case, the value will be `null`. |
| `system_trace_audit_number` | string |  | The System Trace Audit Number (STAN) is a 6-digit identifier assigned by the acquirer. Prefer `network_data.transaction_id` if present, unless you have special requirements. |
| `transaction_id` | string |  | Unique identifier for the authorization assigned by the card network used to match subsequent messages, disputes, and transactions. |

