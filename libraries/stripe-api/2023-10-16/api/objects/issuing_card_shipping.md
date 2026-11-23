# Stripe API 2023-10-16 — `issuing_card_shipping` object

Expandable fields (pass `expand[]=<field>`): `address`, `customs`

| Field | Type | Required | Description |
|---|---|---|---|
| `address` | `address` | yes |  |
| `carrier` | enum: `dhl`, `fedex`, `royal_mail`, `usps` |  | The delivery company that shipped a card. |
| `customs` | `issuing_card_shipping_customs` |  | Additional information that may be required for clearing customs. |
| `eta` | timestamp (Unix seconds) |  | A unix timestamp representing a best estimate of when the card will be delivered. |
| `name` | string | yes | Recipient name. |
| `phone_number` | string |  | The phone number of the receiver of the shipment. Our courier partners will use this number to contact you in the event of card delivery issues. For individual shipments to the EU/UK, if this field is empty, we will provide them with the phone number provided when the cardholder was initially created. |
| `require_signature` | boolean |  | Whether a signature is required for card delivery. This feature is only supported for US users. Standard shipping service does not support signature on delivery. The default value for standard shipping service is false and for express and priority services is true. |
| `service` | enum: `express`, `priority`, `standard` | yes | Shipment service, such as `standard` or `express`. |
| `status` | enum: `canceled`, `delivered`, `failure`, `pending`, `returned`, `shipped` |  | The delivery status of the card. |
| `tracking_number` | string |  | A tracking number for a card shipment. |
| `tracking_url` | string |  | A link to the shipping carrier's site where you can view detailed information about a card shipment. |
| `type` | enum: `bulk`, `individual` | yes | Packaging options. |

