# Stripe API 2023-10-16 — `api_errors` object

Expandable fields (pass `expand[]=<field>`): `payment_intent`, `payment_method`, `setup_intent`, `source`

| Field | Type | Required | Description |
|---|---|---|---|
| `charge` | string |  | For card errors, the ID of the failed charge. |
| `code` | string |  | For some errors that could be handled programmatically, a short string indicating the [error code](https://stripe.com/docs/error-codes) reported. |
| `decline_code` | string |  | For card errors resulting from a card issuer decline, a short string indicating the [card issuer's reason for the decline](https://stripe.com/docs/declines#issuer-declines) if they provide one. |
| `doc_url` | string |  | A URL to more information about the [error code](https://stripe.com/docs/error-codes) reported. |
| `message` | string |  | A human-readable message providing more details about the error. For card errors, these messages can be shown to your users. |
| `param` | string |  | If the error is parameter-specific, the parameter related to the error. For example, you can use this to display a message near the correct form field. |
| `payment_intent` | `payment_intent` |  |  |
| `payment_method` | `payment_method` |  |  |
| `payment_method_type` | string |  | If the error is specific to the type of payment method, the payment method type that had a problem. This field is only populated for invoice-related errors. |
| `request_log_url` | string |  | A URL to the request log entry in your dashboard. |
| `setup_intent` | `setup_intent` |  |  |
| `source` | `bank_account` or `card` or `source` |  | The [source object](https://stripe.com/docs/api/sources/object) for errors returned on a request involving a source. |
| `type` | enum: `api_error`, `card_error`, `idempotency_error`, `invalid_request_error` | yes | The type of error returned. One of `api_error`, `card_error`, `idempotency_error`, or `invalid_request_error` |

