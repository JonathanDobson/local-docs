# Stripe API 2023-10-16 — `issuing_dispute_service_not_as_described_evidence` object

Expandable fields (pass `expand[]=<field>`): `additional_documentation`

| Field | Type | Required | Description |
|---|---|---|---|
| `additional_documentation` | string or `file` |  | (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute. |
| `canceled_at` | timestamp (Unix seconds) |  | Date when order was canceled. |
| `cancellation_reason` | string |  | Reason for canceling the order. |
| `explanation` | string |  | Explanation of why the cardholder is disputing this transaction. |
| `received_at` | timestamp (Unix seconds) |  | Date when the product was received. |

