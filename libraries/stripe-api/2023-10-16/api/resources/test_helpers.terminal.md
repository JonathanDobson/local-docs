# Stripe API 2023-10-16 — test helpers / terminal

Operations under `/v1/test_helpers/terminal` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## POST /v1/test_helpers/terminal/readers/{reader}/present_payment_method

operationId: `PostTestHelpersTerminalReadersReaderPresentPaymentMethod`

Presents a payment method on a simulated reader. Can be used to simulate accepting a payment, saving a card or refunding a transaction.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `reader (path)` | string | yes |  |
| `amount_tip` | integer |  | Simulated on-reader tip amount. |
| `card_present` | object |  | Simulated data for the card_present payment method. |
| `card_present.number` | string |  |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `interac_present` | object |  | Simulated data for the interac_present payment method. |
| `interac_present.number` | string |  |  |
| `type` | enum: `card_present`, `interac_present` |  | Simulated payment type. |

Returns: `terminal.reader`

# Objects returned

## The `terminal.reader` object

A Reader represents a physical device for accepting payment details.

Related guide: [Connecting to a reader](https://stripe.com/docs/terminal/payments/connect-reader)

Expandable fields (pass `expand[]=<field>`): `action`, `location`

| Field | Type | Required | Description |
|---|---|---|---|
| `action` | `terminal_reader_reader_resource_reader_action` |  | The most recent action performed by the reader. |
| `device_sw_version` | string |  | The current software version of the reader. |
| `device_type` | enum: `bbpos_chipper2x`, `bbpos_wisepad3`, `bbpos_wisepos_e`, `mobile_phone_reader`, `simulated_wisepos_e`, `stripe_m2`, `verifone_P400` | yes | Type of reader, one of `bbpos_wisepad3`, `stripe_m2`, `bbpos_chipper2x`, `bbpos_wisepos_e`, `verifone_P400`, `simulated_wisepos_e`, or `mobile_phone_reader`. |
| `id` | string | yes | Unique identifier for the object. |
| `ip_address` | string |  | The local IP address of the reader. |
| `label` | string | yes | Custom label given to the reader for easier identification. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `location` | string or `terminal.location` |  | The location identifier of the reader. |
| `metadata` | map (key → value) | yes | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `object` | enum: `terminal.reader` | yes | String representing the object's type. Objects of the same type share the same value. |
| `serial_number` | string | yes | Serial number of the reader. |
| `status` | enum: `offline`, `online` |  | The networking status of the reader. |

