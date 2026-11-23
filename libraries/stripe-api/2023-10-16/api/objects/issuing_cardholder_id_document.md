# Stripe API 2023-10-16 — `issuing_cardholder_id_document` object

Expandable fields (pass `expand[]=<field>`): `back`, `front`

| Field | Type | Required | Description |
|---|---|---|---|
| `back` | string or `file` |  | The back of a document returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `identity_document`. |
| `front` | string or `file` |  | The front of a document returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `identity_document`. |

