# Stripe API 2023-10-16 — `issuing_dispute_merchandise_not_as_described_evidence` object

Expandable fields (pass `expand[]=<field>`): `additional_documentation`

| Field | Type | Required | Description |
|---|---|---|---|
| `additional_documentation` | string or `file` |  | (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute. |
| `explanation` | string |  | Explanation of why the cardholder is disputing this transaction. |
| `received_at` | timestamp (Unix seconds) |  | Date when the product was received. |
| `return_description` | string |  | Description of the cardholder's attempt to return the product. |
| `return_status` | enum: `merchant_rejected`, `successful` |  | Result of cardholder's attempt to return the product. |
| `returned_at` | timestamp (Unix seconds) |  | Date when the product was returned or attempted to be returned. |

