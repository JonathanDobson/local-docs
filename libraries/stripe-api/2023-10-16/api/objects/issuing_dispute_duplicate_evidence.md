# Stripe API 2023-10-16 — `issuing_dispute_duplicate_evidence` object

Expandable fields (pass `expand[]=<field>`): `additional_documentation`, `card_statement`, `cash_receipt`, `check_image`

| Field | Type | Required | Description |
|---|---|---|---|
| `additional_documentation` | string or `file` |  | (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute. |
| `card_statement` | string or `file` |  | (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Copy of the card statement showing that the product had already been paid for. |
| `cash_receipt` | string or `file` |  | (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Copy of the receipt showing that the product had been paid for in cash. |
| `check_image` | string or `file` |  | (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Image of the front and back of the check that was used to pay for the product. |
| `explanation` | string |  | Explanation of why the cardholder is disputing this transaction. |
| `original_transaction` | string |  | Transaction (e.g., ipi_...) that the disputed transaction is a duplicate of. Of the two or more transactions that are copies of each other, this is original undisputed one. |

