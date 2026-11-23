# Stripe API 2023-10-16 — account

Operations under `/v1/account` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/account

operationId: `GetAccount`

Retrieves the details of an account.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `account`

# Objects returned

## The `account` object

This is an object representing a Stripe account. You can retrieve it to see
properties on the account like its current requirements or if the account is
enabled to make live charges or receive payouts.

For Custom accounts, the properties below are always returned. For other accounts, some properties are returned until that
account has started to go through Connect Onboarding. Once you create an [Account Link](https://stripe.com/docs/api/account_links) or [Account Session](https://stripe.com/docs/api/account_sessions),
some properties are only returned for Custom accounts. Learn about the differences [between accounts](https://stripe.com/docs/connect/accounts).

Expandable fields (pass `expand[]=<field>`): `business_profile`, `capabilities`, `company`, `controller`, `external_accounts`, `future_requirements`, `individual`, `requirements`, `settings`, `tos_acceptance`

| Field | Type | Required | Description |
|---|---|---|---|
| `business_profile` | `account_business_profile` |  | Business information about the account. |
| `business_type` | enum: `company`, `government_entity`, `individual`, `non_profit` |  | The business type. Once you create an [Account Link](https://stripe.com/docs/api/account_links) or [Account Session](https://stripe.com/docs/api/account_sessions), this property is only returned for Custom accounts. |
| `capabilities` | `account_capabilities` |  |  |
| `charges_enabled` | boolean |  | Whether the account can create live charges. |
| `company` | `legal_entity_company` |  |  |
| `controller` | `account_unification_account_controller` |  |  |
| `country` | string |  | The account's country. |
| `created` | timestamp (Unix seconds) |  | Time at which the account was connected. Measured in seconds since the Unix epoch. |
| `default_currency` | string |  | Three-letter ISO currency code representing the default currency for the account. This must be a currency that [Stripe supports in the account's country](https://stripe.com/docs/payouts). |
| `details_submitted` | boolean |  | Whether account details have been submitted. Standard accounts cannot receive payouts before this is true. |
| `email` | string |  | An email address associated with the account. It's not used for authentication and Stripe doesn't market to this field without explicit approval from the platform. |
| `external_accounts` | object |  | External accounts (bank accounts and debit cards) currently attached to this account. External accounts are only returned for requests where `controller[is_controller]` is true. |
| `future_requirements` | `account_future_requirements` |  |  |
| `id` | string | yes | Unique identifier for the object. |
| `individual` | `person` |  |  |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `object` | enum: `account` | yes | String representing the object's type. Objects of the same type share the same value. |
| `payouts_enabled` | boolean |  | Whether Stripe can send payouts to this account. |
| `requirements` | `account_requirements` |  |  |
| `settings` | `account_settings` |  | Options for customizing how the account functions within Stripe. |
| `tos_acceptance` | `account_tos_acceptance` |  |  |
| `type` | enum: `custom`, `express`, `standard` |  | The Stripe account type. Can be `standard`, `express`, or `custom`. |

