# Stripe API 2023-10-16 — apps

Operations under `/v1/apps` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/apps/secrets

operationId: `GetAppsSecrets`

List all secrets stored on the given scope.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `scope` | object | yes | Specifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user. |
| `scope.type` | enum: `account`, `user` | yes |  |
| `scope.user` | string |  |  |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/apps/secrets

operationId: `PostAppsSecrets`

Create or replace a secret in the secret store.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `expires_at` | timestamp (Unix seconds) |  | The Unix timestamp for the expiry time of the secret, after which the secret deletes. |
| `name` | string | yes | A name for the secret that's unique within the scope. |
| `payload` | string | yes | The plaintext secret value to be stored. |
| `scope` | object | yes | Specifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user. |
| `scope.type` | enum: `account`, `user` | yes |  |
| `scope.user` | string |  |  |

Returns: `apps.secret`

## POST /v1/apps/secrets/delete

operationId: `PostAppsSecretsDelete`

Deletes a secret from the secret store by name and scope.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `name` | string | yes | A name for the secret that's unique within the scope. |
| `scope` | object | yes | Specifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user. |
| `scope.type` | enum: `account`, `user` | yes |  |
| `scope.user` | string |  |  |

Returns: `apps.secret`

## GET /v1/apps/secrets/find

operationId: `GetAppsSecretsFind`

Finds a secret in the secret store by name and scope.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `name` | string | yes | A name for the secret that's unique within the scope. |
| `scope` | object | yes | Specifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user. |
| `scope.type` | enum: `account`, `user` | yes |  |
| `scope.user` | string |  |  |

Returns: `apps.secret`

# Objects returned

## The `apps.secret` object

Secret Store is an API that allows Stripe Apps developers to securely persist secrets for use by UI Extensions and app backends.

The primary resource in Secret Store is a `secret`. Other apps can't view secrets created by an app. Additionally, secrets are scoped to provide further permission control.

All Dashboard users and the app backend share `account` scoped secrets. Use the `account` scope for secrets that don't change per-user, like a third-party API key.

A `user` scoped secret is accessible by the app backend and one specific Dashboard user. Use the `user` scope for per-user secrets like per-user OAuth tokens, where different users might have different permissions.

Related guide: [Store data between page reloads](https://stripe.com/docs/stripe-apps/store-auth-data-custom-objects)

Expandable fields (pass `expand[]=<field>`): `scope`

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `deleted` | boolean |  | If true, indicates that this secret has been deleted |
| `expires_at` | timestamp (Unix seconds) |  | The Unix timestamp for the expiry time of the secret, after which the secret deletes. |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `name` | string | yes | A name for the secret that's unique within the scope. |
| `object` | enum: `apps.secret` | yes | String representing the object's type. Objects of the same type share the same value. |
| `payload` | string |  | The plaintext secret value to be stored. |
| `scope` | `secret_service_resource_scope` | yes |  |

