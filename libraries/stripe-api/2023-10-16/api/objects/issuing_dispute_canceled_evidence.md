# Stripe API 2023-10-16 — `issuing_dispute_canceled_evidence` object

Expandable fields (pass `expand[]=<field>`): `additional_documentation`

| Field | Type | Required | Description |
|---|---|---|---|
| `additional_documentation` | string or `file` |  | (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute. |
| `canceled_at` | timestamp (Unix seconds) |  | Date when order was canceled. |
| `cancellation_policy_provided` | boolean |  | Whether the cardholder was provided with a cancellation policy. |
| `cancellation_reason` | string |  | Reason for canceling the order. |
| `expected_at` | timestamp (Unix seconds) |  | Date when the cardholder expected to receive the product. |
| `explanation` | string |  | Explanation of why the cardholder is disputing this transaction. |
| `product_description` | string |  | Description of the merchandise or service that was purchased. |
| `product_type` | enum: `merchandise`, `service` |  | Whether the product was a merchandise or service. |
| `return_status` | enum: `merchant_rejected`, `successful` |  | Result of cardholder's attempt to return the product. |
| `returned_at` | timestamp (Unix seconds) |  | Date when the product was returned or attempted to be returned. |

