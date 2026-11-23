# Stripe API 2023-10-16 — confirmation tokens

Operations under `/v1/confirmation_tokens` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/confirmation_tokens/{confirmation_token}

operationId: `GetConfirmationTokensConfirmationToken`

Retrieves an existing ConfirmationToken object

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `confirmation_token (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `confirmation_token`

# Objects returned

## The `confirmation_token` object

ConfirmationTokens help transport client side data collected by Stripe JS over
to your server for confirming a PaymentIntent or SetupIntent. If the confirmation
is successful, values present on the ConfirmationToken are written onto the Intent.

To learn more about how to use ConfirmationToken, visit the related guides:
- [Finalize payments on the server](https://stripe.com/docs/payments/finalize-payments-on-the-server)
- [Build two-step confirmation](https://stripe.com/docs/payments/build-a-two-step-confirmation).

Expandable fields (pass `expand[]=<field>`): `mandate_data`, `payment_method_preview`, `shipping`

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `expires_at` | timestamp (Unix seconds) |  | Time at which this ConfirmationToken expires and can no longer be used to confirm a PaymentIntent or SetupIntent. This is set to null once this ConfirmationToken has been used. |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `mandate_data` | `confirmation_tokens_resource_mandate_data` |  | Data used for generating a Mandate. |
| `object` | enum: `confirmation_token` | yes | String representing the object's type. Objects of the same type share the same value. |
| `payment_intent` | string |  | ID of the PaymentIntent that this ConfirmationToken was used to confirm, or null if this ConfirmationToken has not yet been used. |
| `payment_method_preview` | `confirmation_tokens_resource_payment_method_preview` |  | Payment details collected by the Payment Element, used to create a PaymentMethod when a PaymentIntent or SetupIntent is confirmed with this ConfirmationToken. |
| `return_url` | string |  | Return URL used to confirm the Intent. |
| `setup_future_usage` | enum: `off_session`, `on_session` |  | Indicates that you intend to make future payments with this ConfirmationToken's payment method.<br>The presence of this property will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. |
| `setup_intent` | string |  | ID of the SetupIntent that this ConfirmationToken was used to confirm, or null if this ConfirmationToken has not yet been used. |
| `shipping` | `confirmation_tokens_resource_shipping` |  | Shipping information collected on this ConfirmationToken. |
| `use_stripe_sdk` | boolean | yes | Indicates whether the Stripe SDK is used to handle confirmation flow. Defaults to `true` on ConfirmationToken. |

