# Stripe API 2023-10-16 — `issuing_authorization_request` object

Expandable fields (pass `expand[]=<field>`): `amount_details`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | The `pending_request.amount` at the time of the request, presented in your card's currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). Stripe held this amount from your account to fund the authorization if the request was approved. |
| `amount_details` | `issuing_authorization_amount_details` |  | Detailed breakdown of amount components. These amounts are denominated in `currency` and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). |
| `approved` | boolean | yes | Whether this request was approved. |
| `authorization_code` | string |  | A code created by Stripe which is shared with the merchant to validate the authorization. This field will be populated if the authorization message was approved. The code typically starts with the letter "S", followed by a six-digit number. For example, "S498162". Please note that the code is not guaranteed to be unique across authorizations. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `merchant_amount` | integer | yes | The `pending_request.merchant_amount` at the time of the request, presented in the `merchant_currency` and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). |
| `merchant_currency` | string | yes | The currency that was collected by the merchant and presented to the cardholder for the authorization. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `network_risk_score` | integer |  | The card network's estimate of the likelihood that an authorization is fraudulent. Takes on values between 1 and 99. |
| `reason` | enum: `account_disabled`, `card_active`, `card_inactive`, `cardholder_inactive`, `cardholder_verification_required`, `insufficient_funds`, `not_allowed`, `spending_controls`, `suspected_fraud`, `verification_failed`, `webhook_approved`, `webhook_declined`, `webhook_error`, `webhook_timeout` | yes | When an authorization is approved or declined by you or by Stripe, this field provides additional detail on the reason for the outcome. |
| `reason_message` | string |  | If the `request_history.reason` is `webhook_error` because the direct webhook response is invalid (for example, parsing errors or missing parameters), we surface a more detailed error message via this field. |
| `requested_at` | timestamp (Unix seconds) |  | Time when the card network received an authorization request from the acquirer in UTC. Referred to by networks as transmission time. |

