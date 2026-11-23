# Stripe API 2023-10-16 — `terminal_reader_reader_resource_reader_action` object

Represents an action performed by the reader

Expandable fields (pass `expand[]=<field>`): `process_payment_intent`, `process_setup_intent`, `refund_payment`, `set_reader_display`

| Field | Type | Required | Description |
|---|---|---|---|
| `failure_code` | string |  | Failure code, only set if status is `failed`. |
| `failure_message` | string |  | Detailed failure message, only set if status is `failed`. |
| `process_payment_intent` | `terminal_reader_reader_resource_process_payment_intent_action` |  |  |
| `process_setup_intent` | `terminal_reader_reader_resource_process_setup_intent_action` |  |  |
| `refund_payment` | `terminal_reader_reader_resource_refund_payment_action` |  |  |
| `set_reader_display` | `terminal_reader_reader_resource_set_reader_display_action` |  |  |
| `status` | enum: `failed`, `in_progress`, `succeeded` | yes | Status of the action performed by the reader. |
| `type` | enum: `process_payment_intent`, `process_setup_intent`, `refund_payment`, `set_reader_display` | yes | Type of action performed by the reader. |

