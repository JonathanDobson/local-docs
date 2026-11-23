# Stripe API 2023-10-16 — account links

Operations under `/v1/account_links` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## POST /v1/account_links

operationId: `PostAccountLinks`

Creates an AccountLink object that includes a single-use Stripe URL that the platform can redirect their user to in order to take them through the Connect Onboarding flow.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account` | string | yes | The identifier of the account to create an account link for. |
| `collect` | enum: `currently_due`, `eventually_due` |  | The collect parameter is deprecated. Use `collection_options` instead. |
| `collection_options` | object |  | Specifies the requirements that Stripe collects from connected accounts in the Connect Onboarding flow. |
| `collection_options.fields` | enum: `currently_due`, `eventually_due` | yes |  |
| `collection_options.future_requirements` | enum: `include`, `omit` |  |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `refresh_url` | string |  | The URL the user will be redirected to if the account link is expired, has been previously-visited, or is otherwise invalid. The URL you specify should attempt to generate a new account link with the same parameters used to create the original account link, then redirect the user to the new account link's URL so they can continue with Connect Onboarding. If a new account link cannot be generated or the redirect fails you should display a useful error to the user. |
| `return_url` | string |  | The URL that the user will be redirected to upon leaving or completing the linked flow. |
| `type` | enum: `account_onboarding`, `account_update` | yes | The type of account link the user is requesting. Possible values are `account_onboarding` or `account_update`. |

Returns: `account_link`

# Objects returned

## The `account_link` object

Account Links are the means by which a Connect platform grants a connected account permission to access
Stripe-hosted applications, such as Connect Onboarding.

Related guide: [Connect Onboarding](https://stripe.com/docs/connect/custom/hosted-onboarding)

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `expires_at` | timestamp (Unix seconds) | yes | The timestamp at which this account link will expire. |
| `object` | enum: `account_link` | yes | String representing the object's type. Objects of the same type share the same value. |
| `url` | string | yes | The URL for the account link. |

