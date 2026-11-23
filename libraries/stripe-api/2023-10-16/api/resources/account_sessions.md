# Stripe API 2023-10-16 — account sessions

Operations under `/v1/account_sessions` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## POST /v1/account_sessions

operationId: `PostAccountSessions`

Creates a AccountSession object that includes a single-use token that the platform can use on their front-end to grant client-side API access.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account` | string | yes | The identifier of the account to create an Account Session for. |
| `components` | object | yes | Each key of the dictionary represents an embedded component, and each embedded component maps to its configuration (e.g. whether it has been enabled or not). |
| `components.account_onboarding` | object |  |  |
| `components.account_onboarding.enabled` | boolean | yes |  |
| `components.account_onboarding.features` | object |  |  |
| `components.documents` | object |  |  |
| `components.documents.enabled` | boolean | yes |  |
| `components.documents.features` | object |  |  |
| `components.payment_details` | object |  |  |
| `components.payment_details.enabled` | boolean | yes |  |
| `components.payment_details.features` | object |  |  |
| `components.payment_details.features.capture_payments` | boolean |  |  |
| `components.payment_details.features.destination_on_behalf_of_charge_management` | boolean |  |  |
| `components.payment_details.features.dispute_management` | boolean |  |  |
| `components.payment_details.features.refund_management` | boolean |  |  |
| `components.payments` | object |  |  |
| `components.payments.enabled` | boolean | yes |  |
| `components.payments.features` | object |  |  |
| `components.payments.features.capture_payments` | boolean |  |  |
| `components.payments.features.destination_on_behalf_of_charge_management` | boolean |  |  |
| `components.payments.features.dispute_management` | boolean |  |  |
| `components.payments.features.refund_management` | boolean |  |  |
| `components.payouts` | object |  |  |
| `components.payouts.enabled` | boolean | yes |  |
| `components.payouts.features` | object |  |  |
| `components.payouts.features.edit_payout_schedule` | boolean |  |  |
| `components.payouts.features.instant_payouts` | boolean |  |  |
| `components.payouts.features.standard_payouts` | boolean |  |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `account_session`

# Objects returned

## The `account_session` object

An AccountSession allows a Connect platform to grant access to a connected account in Connect embedded components.

We recommend that you create an AccountSession each time you need to display an embedded component
to your user. Do not save AccountSessions to your database as they expire relatively
quickly, and cannot be used more than once.

Related guide: [Connect embedded components](https://stripe.com/docs/connect/get-started-connect-embedded-components)

Expandable fields (pass `expand[]=<field>`): `components`

| Field | Type | Required | Description |
|---|---|---|---|
| `account` | string | yes | The ID of the account the AccountSession was created for |
| `client_secret` | string | yes | The client secret of this AccountSession. Used on the client to set up secure access to the given `account`.<br>The client secret can be used to provide access to `account` from your frontend. It should not be stored, logged, or exposed to anyone other than the connected account. Make sure that you have TLS enabled on any page that includes the client secret.<br>Refer to our docs to [setup Connect embedded components](https://stripe.com/docs/connect/get-started-connect-embedded-components) and learn about how `client_secret` should be handled. |
| `components` | `connect_embedded_account_session_create_components` | yes |  |
| `expires_at` | timestamp (Unix seconds) | yes | The timestamp at which this AccountSession will expire. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `object` | enum: `account_session` | yes | String representing the object's type. Objects of the same type share the same value. |

