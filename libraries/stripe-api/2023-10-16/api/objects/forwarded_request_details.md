# Stripe API 2023-10-16 — `forwarded_request_details` object

Details about the request forwarded to the destination endpoint.

Expandable fields (pass `expand[]=<field>`): `headers`

| Field | Type | Required | Description |
|---|---|---|---|
| `body` | string | yes | The body payload to send to the destination endpoint. |
| `headers` | array of `forwarded_request_header` | yes | The headers to include in the forwarded request. Can be omitted if no additional headers (excluding Stripe-generated ones such as the Content-Type header) should be included. |
| `http_method` | enum: `POST` | yes | The HTTP method used to call the destination endpoint. |

