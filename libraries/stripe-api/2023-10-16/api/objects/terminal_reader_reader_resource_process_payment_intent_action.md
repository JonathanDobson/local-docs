# Stripe API 2023-10-16 — `terminal_reader_reader_resource_process_payment_intent_action` object

Represents a reader action to process a payment intent

Expandable fields (pass `expand[]=<field>`): `payment_intent`, `process_config`

| Field | Type | Required | Description |
|---|---|---|---|
| `payment_intent` | string or `payment_intent` | yes | Most recent PaymentIntent processed by the reader. |
| `process_config` | `terminal_reader_reader_resource_process_config` |  |  |

