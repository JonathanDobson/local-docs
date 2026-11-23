# Stripe API 2023-10-16 — `issuing_dispute_fraudulent_evidence` object

Expandable fields (pass `expand[]=<field>`): `additional_documentation`

| Field | Type | Required | Description |
|---|---|---|---|
| `additional_documentation` | string or `file` |  | (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute. |
| `explanation` | string |  | Explanation of why the cardholder is disputing this transaction. |

