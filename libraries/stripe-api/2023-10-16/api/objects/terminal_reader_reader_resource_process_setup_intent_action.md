# Stripe API 2023-10-16 — `terminal_reader_reader_resource_process_setup_intent_action` object

Represents a reader action to process a setup intent

Expandable fields (pass `expand[]=<field>`): `process_config`, `setup_intent`

| Field | Type | Required | Description |
|---|---|---|---|
| `generated_card` | string |  | ID of a card PaymentMethod generated from the card_present PaymentMethod that may be attached to a Customer for future transactions. Only present if it was possible to generate a card PaymentMethod. |
| `process_config` | `terminal_reader_reader_resource_process_setup_config` |  |  |
| `setup_intent` | string or `setup_intent` | yes | Most recent SetupIntent processed by the reader. |

