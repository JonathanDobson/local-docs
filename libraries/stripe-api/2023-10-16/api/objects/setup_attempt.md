# Stripe API 2023-10-16 — `setup_attempt` object

A SetupAttempt describes one attempted confirmation of a SetupIntent,
whether that confirmation is successful or unsuccessful. You can use
SetupAttempts to inspect details of a specific attempt at setting up a
payment method using a SetupIntent.

Expandable fields (pass `expand[]=<field>`): `application`, `customer`, `on_behalf_of`, `payment_method`, `payment_method_details`, `setup_error`, `setup_intent`

| Field | Type | Required | Description |
|---|---|---|---|
| `application` | string or `application` |  | The value of [application](https://stripe.com/docs/api/setup_intents/object#setup_intent_object-application) on the SetupIntent at the time of this confirmation. |
| `attach_to_self` | boolean |  | If present, the SetupIntent's payment method will be attached to the in-context Stripe Account.<br>It can only be used for this Stripe Account’s own money movement flows like InboundTransfer and OutboundTransfers. It cannot be set to true when setting up a PaymentMethod for a Customer, and defaults to false when attaching a PaymentMethod to a Customer. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `customer` | string or `customer` or `deleted_customer` |  | The value of [customer](https://stripe.com/docs/api/setup_intents/object#setup_intent_object-customer) on the SetupIntent at the time of this confirmation. |
| `flow_directions` | array of enum: `inbound`, `outbound` |  | Indicates the directions of money movement for which this payment method is intended to be used.<br>Include `inbound` if you intend to use the payment method as the origin to pull funds from. Include `outbound` if you intend to use the payment method as the destination to send funds to. You can include both if you intend to use the payment method for both purposes. |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `object` | enum: `setup_attempt` | yes | String representing the object's type. Objects of the same type share the same value. |
| `on_behalf_of` | string or `account` |  | The value of [on_behalf_of](https://stripe.com/docs/api/setup_intents/object#setup_intent_object-on_behalf_of) on the SetupIntent at the time of this confirmation. |
| `payment_method` | string or `payment_method` | yes | ID of the payment method used with this SetupAttempt. |
| `payment_method_details` | `setup_attempt_payment_method_details` | yes |  |
| `setup_error` | `api_errors` |  | The error encountered during this attempt to confirm the SetupIntent, if any. |
| `setup_intent` | string or `setup_intent` | yes | ID of the SetupIntent that this attempt belongs to. |
| `status` | string | yes | Status of this SetupAttempt, one of `requires_confirmation`, `requires_action`, `processing`, `succeeded`, `failed`, or `abandoned`. |
| `usage` | string | yes | The value of [usage](https://stripe.com/docs/api/setup_intents/object#setup_intent_object-usage) on the SetupIntent at the time of this confirmation, one of `off_session` or `on_session`. |

