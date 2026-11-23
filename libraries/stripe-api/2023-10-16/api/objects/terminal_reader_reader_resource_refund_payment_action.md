# Stripe API 2023-10-16 — `terminal_reader_reader_resource_refund_payment_action` object

Represents a reader action to refund a payment

Expandable fields (pass `expand[]=<field>`): `charge`, `payment_intent`, `refund`, `refund_payment_config`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer |  | The amount being refunded. |
| `charge` | string or `charge` |  | Charge that is being refunded. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `payment_intent` | string or `payment_intent` |  | Payment intent that is being refunded. |
| `reason` | enum: `duplicate`, `fraudulent`, `requested_by_customer` |  | The reason for the refund. |
| `refund` | string or `refund` |  | Unique identifier for the refund object. |
| `refund_application_fee` | boolean |  | Boolean indicating whether the application fee should be refunded when refunding this charge. If a full charge refund is given, the full application fee will be refunded. Otherwise, the application fee will be refunded in an amount proportional to the amount of the charge refunded. An application fee can be refunded only by the application that created the charge. |
| `refund_payment_config` | `terminal_reader_reader_resource_refund_payment_config` |  |  |
| `reverse_transfer` | boolean |  | Boolean indicating whether the transfer should be reversed when refunding this charge. The transfer will be reversed proportionally to the amount being refunded (either the entire or partial amount). A transfer can be reversed only by the application that created the charge. |

