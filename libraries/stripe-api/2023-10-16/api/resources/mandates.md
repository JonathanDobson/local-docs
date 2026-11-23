# Stripe API 2023-10-16 — mandates

Operations under `/v1/mandates` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/mandates/{mandate}

operationId: `GetMandatesMandate`

Retrieves a Mandate object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `mandate (path)` | string | yes |  |

Returns: `mandate`

# Objects returned

## The `mandate` object

A Mandate is a record of the permission that your customer gives you to debit their payment method.

Expandable fields (pass `expand[]=<field>`): `customer_acceptance`, `multi_use`, `payment_method`, `payment_method_details`, `single_use`

| Field | Type | Required | Description |
|---|---|---|---|
| `customer_acceptance` | `customer_acceptance` | yes |  |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `multi_use` | `mandate_multi_use` |  |  |
| `object` | enum: `mandate` | yes | String representing the object's type. Objects of the same type share the same value. |
| `on_behalf_of` | string |  | The account (if any) that the mandate is intended for. |
| `payment_method` | string or `payment_method` | yes | ID of the payment method associated with this mandate. |
| `payment_method_details` | `mandate_payment_method_details` | yes |  |
| `single_use` | `mandate_single_use` |  |  |
| `status` | enum: `active`, `inactive`, `pending` | yes | The mandate status indicates whether or not you can use it to initiate a payment. |
| `type` | enum: `multi_use`, `single_use` | yes | The type of the mandate. |

