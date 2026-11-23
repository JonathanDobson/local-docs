# Stripe API 2023-10-16 — `forwarded_response_details` object

Details about the response from the destination endpoint.

Expandable fields (pass `expand[]=<field>`): `headers`

| Field | Type | Required | Description |
|---|---|---|---|
| `body` | string | yes | The response body from the destination endpoint to Stripe. |
| `headers` | array of `forwarded_request_header` | yes | HTTP headers that the destination endpoint returned. |
| `status` | integer | yes | The HTTP status code that the destination endpoint returned. |

