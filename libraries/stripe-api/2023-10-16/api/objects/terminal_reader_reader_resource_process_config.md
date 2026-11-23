# Stripe API 2023-10-16 — `terminal_reader_reader_resource_process_config` object

Represents a per-transaction override of a reader configuration

Expandable fields (pass `expand[]=<field>`): `tipping`

| Field | Type | Required | Description |
|---|---|---|---|
| `enable_customer_cancellation` | boolean |  | Enable customer initiated cancellation when processing this payment. |
| `skip_tipping` | boolean |  | Override showing a tipping selection screen on this transaction. |
| `tipping` | `terminal_reader_reader_resource_tipping_config` |  |  |

