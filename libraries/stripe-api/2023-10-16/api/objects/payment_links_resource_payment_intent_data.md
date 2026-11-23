# Stripe API 2023-10-16 — `payment_links_resource_payment_intent_data` object

| Field | Type | Required | Description |
|---|---|---|---|
| `capture_method` | enum: `automatic`, `automatic_async`, `manual` |  | Indicates when the funds will be captured from the customer's account. |
| `description` | string |  | An arbitrary string attached to the object. Often useful for displaying to users. |
| `metadata` | map (key → value) | yes | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that will set metadata on [Payment Intents](https://stripe.com/docs/api/payment_intents) generated from this payment link. |
| `setup_future_usage` | enum: `off_session`, `on_session` |  | Indicates that you intend to make future payments with the payment method collected during checkout. |
| `statement_descriptor` | string |  | Extra information about the payment. This will appear on your customer's statement when this payment succeeds in creating a charge. |
| `statement_descriptor_suffix` | string |  | Provides information about the charge that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that's set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor. |
| `transfer_group` | string |  | A string that identifies the resulting payment as part of a group. See the PaymentIntents [use case for connected accounts](https://stripe.com/docs/connect/separate-charges-and-transfers) for details. |

