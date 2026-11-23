# Stripe API 2023-10-16 — `issuing_dispute_other_evidence` object

Expandable fields (pass `expand[]=<field>`): `additional_documentation`

| Field | Type | Required | Description |
|---|---|---|---|
| `additional_documentation` | string or `file` |  | (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute. |
| `explanation` | string |  | Explanation of why the cardholder is disputing this transaction. |
| `product_description` | string |  | Description of the merchandise or service that was purchased. |
| `product_type` | enum: `merchandise`, `service` |  | Whether the product was a merchandise or service. |

