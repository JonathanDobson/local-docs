# Stripe API 2023-10-16 — identity

Operations under `/v1/identity` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/identity/verification_reports

operationId: `GetIdentityVerificationReports`

List all verification reports.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `client_reference_id` | string |  | A string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems. |
| `created` | object or integer |  | Only return VerificationReports that were created during the given date interval. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `type` | enum: `document`, `id_number` |  | Only return VerificationReports of this type |
| `verification_session` | string |  | Only return VerificationReports created by this VerificationSession ID. It is allowed to provide a VerificationIntent ID. |

Returns: object

## GET /v1/identity/verification_reports/{report}

operationId: `GetIdentityVerificationReportsReport`

Retrieves an existing VerificationReport

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `report (path)` | string | yes |  |

Returns: `identity.verification_report`

## GET /v1/identity/verification_sessions

operationId: `GetIdentityVerificationSessions`

Returns a list of VerificationSessions

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `client_reference_id` | string |  | A string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems. |
| `created` | object or integer |  | Only return VerificationSessions that were created during the given date interval. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `status` | enum: `canceled`, `processing`, `requires_input`, `verified` |  | Only return VerificationSessions with this status. [Learn more about the lifecycle of sessions](https://stripe.com/docs/identity/how-sessions-work). |

Returns: object

## POST /v1/identity/verification_sessions

operationId: `PostIdentityVerificationSessions`

Creates a VerificationSession object.

After the VerificationSession is created, display a verification modal using the session `client_secret` or send your users to the session’s `url`.

If your API key is in test mode, verification checks won’t actually process, though everything else will occur as if in live mode.

Related guide: [Verify your users’ identity documents](https://stripe.com/docs/identity/verify-identity-documents)

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `client_reference_id` | string |  | A string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `options` | object |  | A set of options for the session’s verification checks. |
| `options.document` | object or "" (to unset) |  |  |
| `options.document.allowed_types` | array of enum: `driving_license`, `id_card`, `passport` |  |  |
| `options.document.require_id_number` | boolean |  |  |
| `options.document.require_live_capture` | boolean |  |  |
| `options.document.require_matching_selfie` | boolean |  |  |
| `options.email` | object or "" (to unset) |  |  |
| `options.email.require_verification` | boolean |  |  |
| `options.phone` | object or "" (to unset) |  |  |
| `options.phone.require_verification` | boolean |  |  |
| `provided_details` | object |  | Details provided about the user being verified. These details may be shown to the user. |
| `provided_details.email` | string |  |  |
| `provided_details.phone` | string |  |  |
| `return_url` | string |  | The URL that the user will be redirected to upon completing the verification flow. |
| `type` | enum: `document`, `id_number` |  | The type of [verification check](https://stripe.com/docs/identity/verification-checks) to be performed. |
| `verification_flow` | string |  | The ID of a Verification Flow from the Dashboard. |

Returns: `identity.verification_session`

## GET /v1/identity/verification_sessions/{session}

operationId: `GetIdentityVerificationSessionsSession`

Retrieves the details of a VerificationSession that was previously created.

When the session status is `requires_input`, you can use this method to retrieve a valid
`client_secret` or `url` to allow re-submission.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `session (path)` | string | yes |  |

Returns: `identity.verification_session`

## POST /v1/identity/verification_sessions/{session}

operationId: `PostIdentityVerificationSessionsSession`

Updates a VerificationSession object.

When the session status is `requires_input`, you can use this method to update the
verification check and options.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `session (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `options` | object |  | A set of options for the session’s verification checks. |
| `options.document` | object or "" (to unset) |  |  |
| `options.document.allowed_types` | array of enum: `driving_license`, `id_card`, `passport` |  |  |
| `options.document.require_id_number` | boolean |  |  |
| `options.document.require_live_capture` | boolean |  |  |
| `options.document.require_matching_selfie` | boolean |  |  |
| `options.email` | object or "" (to unset) |  |  |
| `options.email.require_verification` | boolean |  |  |
| `options.phone` | object or "" (to unset) |  |  |
| `options.phone.require_verification` | boolean |  |  |
| `provided_details` | object |  | Details provided about the user being verified. These details may be shown to the user. |
| `provided_details.email` | string |  |  |
| `provided_details.phone` | string |  |  |
| `type` | enum: `document`, `id_number` |  | The type of [verification check](https://stripe.com/docs/identity/verification-checks) to be performed. |

Returns: `identity.verification_session`

## POST /v1/identity/verification_sessions/{session}/cancel

operationId: `PostIdentityVerificationSessionsSessionCancel`

A VerificationSession object can be canceled when it is in `requires_input` [status](https://stripe.com/docs/identity/how-sessions-work).

Once canceled, future submission attempts are disabled. This cannot be undone. [Learn more](https://stripe.com/docs/identity/verification-sessions#cancel).

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `session (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `identity.verification_session`

## POST /v1/identity/verification_sessions/{session}/redact

operationId: `PostIdentityVerificationSessionsSessionRedact`

Redact a VerificationSession to remove all collected information from Stripe. This will redact
the VerificationSession and all objects related to it, including VerificationReports, Events,
request logs, etc.

A VerificationSession object can be redacted when it is in `requires_input` or `verified`
[status](https://stripe.com/docs/identity/how-sessions-work). Redacting a VerificationSession in `requires_action`
state will automatically cancel it.

The redaction process may take up to four days. When the redaction process is in progress, the
VerificationSession’s `redaction.status` field will be set to `processing`; when the process is
finished, it will change to `redacted` and an `identity.verification_session.redacted` event
will be emitted.

Redaction is irreversible. Redacted objects are still accessible in the Stripe API, but all the
fields that contain personal data will be replaced by the string `[redacted]` or a similar
placeholder. The `metadata` field will also be erased. Redacted objects cannot be updated or
used for any purpose.

[Learn more](https://stripe.com/docs/identity/verification-sessions#redact).

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `session (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `identity.verification_session`

# Objects returned

## The `identity.verification_report` object

A VerificationReport is the result of an attempt to collect and verify data from a user.
The collection of verification checks performed is determined from the `type` and `options`
parameters used. You can find the result of each verification check performed in the
appropriate sub-resource: `document`, `id_number`, `selfie`.

Each VerificationReport contains a copy of any data collected by the user as well as
reference IDs which can be used to access collected images through the [FileUpload](https://stripe.com/docs/api/files)
API. To configure and create VerificationReports, use the
[VerificationSession](https://stripe.com/docs/api/identity/verification_sessions) API.

Related guides: [Accessing verification results](https://stripe.com/docs/identity/verification-sessions#results).

Expandable fields (pass `expand[]=<field>`): `document`, `email`, `id_number`, `options`, `phone`, `selfie`

| Field | Type | Required | Description |
|---|---|---|---|
| `client_reference_id` | string |  | A string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `document` | `gelato_document_report` |  |  |
| `email` | `gelato_email_report` |  |  |
| `id` | string | yes | Unique identifier for the object. |
| `id_number` | `gelato_id_number_report` |  |  |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `object` | enum: `identity.verification_report` | yes | String representing the object's type. Objects of the same type share the same value. |
| `options` | `gelato_verification_report_options` |  |  |
| `phone` | `gelato_phone_report` |  |  |
| `selfie` | `gelato_selfie_report` |  |  |
| `type` | enum: `document`, `id_number`, `verification_flow` | yes | Type of report. |
| `verification_flow` | string |  | The configuration token of a Verification Flow from the dashboard. |
| `verification_session` | string |  | ID of the VerificationSession that created this report. |

## The `identity.verification_session` object

A VerificationSession guides you through the process of collecting and verifying the identities
of your users. It contains details about the type of verification, such as what [verification
check](https://stripe.com/docs/identity/verification-checks) to perform. Only create one VerificationSession for
each verification in your system.

A VerificationSession transitions through [multiple
statuses](https://stripe.com/docs/identity/how-sessions-work) throughout its lifetime as it progresses through
the verification flow. The VerificationSession contains the user's verified data after
verification checks are complete.

Related guide: [The Verification Sessions API](https://stripe.com/docs/identity/verification-sessions)

Expandable fields (pass `expand[]=<field>`): `last_error`, `last_verification_report`, `options`, `provided_details`, `redaction`, `verified_outputs`

| Field | Type | Required | Description |
|---|---|---|---|
| `client_reference_id` | string |  | A string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems. |
| `client_secret` | string |  | The short-lived client secret used by Stripe.js to [show a verification modal](https://stripe.com/docs/js/identity/modal) inside your app. This client secret expires after 24 hours and can only be used once. Don’t store it, log it, embed it in a URL, or expose it to anyone other than the user. Make sure that you have TLS enabled on any page that includes the client secret. Refer to our docs on [passing the client secret to the frontend](https://stripe.com/docs/identity/verification-sessions#client-secret) to learn more. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `id` | string | yes | Unique identifier for the object. |
| `last_error` | `gelato_session_last_error` |  | If present, this property tells you the last error encountered when processing the verification. |
| `last_verification_report` | string or `identity.verification_report` |  | ID of the most recent VerificationReport. [Learn more about accessing detailed verification results.](https://stripe.com/docs/identity/verification-sessions#results) |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) | yes | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `object` | enum: `identity.verification_session` | yes | String representing the object's type. Objects of the same type share the same value. |
| `options` | `gelato_verification_session_options` |  | A set of options for the session’s verification checks. |
| `provided_details` | `gelato_provided_details` |  | Details provided about the user being verified. These details may be shown to the user. |
| `redaction` | `verification_session_redaction` |  | Redaction status of this VerificationSession. If the VerificationSession is not redacted, this field will be null. |
| `status` | enum: `canceled`, `processing`, `requires_input`, `verified` | yes | Status of this VerificationSession. [Learn more about the lifecycle of sessions](https://stripe.com/docs/identity/how-sessions-work). |
| `type` | enum: `document`, `id_number`, `verification_flow` | yes | The type of [verification check](https://stripe.com/docs/identity/verification-checks) to be performed. |
| `url` | string |  | The short-lived URL that you use to redirect a user to Stripe to submit their identity information. This URL expires after 48 hours and can only be used once. Don’t store it, log it, send it in emails or expose it to anyone other than the user. Refer to our docs on [verifying identity documents](https://stripe.com/docs/identity/verify-identity-documents?platform=web&type=redirect) to learn how to redirect users to Stripe. |
| `verification_flow` | string |  | The configuration token of a Verification Flow from the dashboard. |
| `verified_outputs` | `gelato_verified_outputs` |  | The user’s verified data. |

