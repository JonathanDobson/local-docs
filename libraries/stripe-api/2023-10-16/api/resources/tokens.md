# Stripe API 2023-10-16 — tokens

Operations under `/v1/tokens` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## POST /v1/tokens

operationId: `PostTokens`

Creates a single-use token that represents a bank account’s details.
You can use this token with any API method in place of a bank account dictionary. You can only use this token once. To do so, attach it to a [Custom account](#accounts).

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account` | object |  | Information for the account this token represents. |
| `account.business_type` | enum: `company`, `government_entity`, `individual`, `non_profit` |  |  |
| `account.company` | object |  |  |
| `account.company.address` | object |  |  |
| `account.company.address.city` | string |  |  |
| `account.company.address.country` | string |  |  |
| `account.company.address.line1` | string |  |  |
| `account.company.address.line2` | string |  |  |
| `account.company.address.postal_code` | string |  |  |
| `account.company.address.state` | string |  |  |
| `account.company.address_kana` | object |  |  |
| `account.company.address_kana.city` | string |  |  |
| `account.company.address_kana.country` | string |  |  |
| `account.company.address_kana.line1` | string |  |  |
| `account.company.address_kana.line2` | string |  |  |
| `account.company.address_kana.postal_code` | string |  |  |
| `account.company.address_kana.state` | string |  |  |
| `account.company.address_kana.town` | string |  |  |
| `account.company.address_kanji` | object |  |  |
| `account.company.address_kanji.city` | string |  |  |
| `account.company.address_kanji.country` | string |  |  |
| `account.company.address_kanji.line1` | string |  |  |
| `account.company.address_kanji.line2` | string |  |  |
| `account.company.address_kanji.postal_code` | string |  |  |
| `account.company.address_kanji.state` | string |  |  |
| `account.company.address_kanji.town` | string |  |  |
| `account.company.directors_provided` | boolean |  |  |
| `account.company.executives_provided` | boolean |  |  |
| `account.company.export_license_id` | string |  |  |
| `account.company.export_purpose_code` | string |  |  |
| `account.company.name` | string |  |  |
| `account.company.name_kana` | string |  |  |
| `account.company.name_kanji` | string |  |  |
| `account.company.owners_provided` | boolean |  |  |
| `account.company.ownership_declaration` | object |  |  |
| `account.company.ownership_declaration.date` | timestamp (Unix seconds) |  |  |
| `account.company.ownership_declaration.ip` | string |  |  |
| `account.company.ownership_declaration.user_agent` | string |  |  |
| `account.company.ownership_declaration_shown_and_signed` | boolean |  |  |
| `account.company.phone` | string |  |  |
| `account.company.registration_number` | string |  |  |
| `account.company.structure` | enum: ``, `free_zone_establishment`, `free_zone_llc`, `government_instrumentality`, `governmental_unit`, `incorporated_non_profit`, `incorporated_partnership`, `limited_liability_partnership`, `llc`, `multi_member_llc`, `private_company`, `private_corporation`, `private_partnership`, `public_company`, `public_corporation`, `public_partnership`, `registered_charity`, `single_member_llc`, `sole_establishment`, `sole_proprietorship`, `tax_exempt_government_instrumentality`, `unincorporated_association`, `unincorporated_non_profit`, `unincorporated_partnership` |  |  |
| `account.company.tax_id` | string |  |  |
| `account.company.tax_id_registrar` | string |  |  |
| `account.company.vat_id` | string |  |  |
| `account.company.verification` | object |  |  |
| `account.company.verification.document` | object |  |  |
| `account.company.verification.document.back` | string |  |  |
| `account.company.verification.document.front` | string |  |  |
| `account.individual` | object |  |  |
| `account.individual.address` | object |  |  |
| `account.individual.address.city` | string |  |  |
| `account.individual.address.country` | string |  |  |
| `account.individual.address.line1` | string |  |  |
| `account.individual.address.line2` | string |  |  |
| `account.individual.address.postal_code` | string |  |  |
| `account.individual.address.state` | string |  |  |
| `account.individual.address_kana` | object |  |  |
| `account.individual.address_kana.city` | string |  |  |
| `account.individual.address_kana.country` | string |  |  |
| `account.individual.address_kana.line1` | string |  |  |
| `account.individual.address_kana.line2` | string |  |  |
| `account.individual.address_kana.postal_code` | string |  |  |
| `account.individual.address_kana.state` | string |  |  |
| `account.individual.address_kana.town` | string |  |  |
| `account.individual.address_kanji` | object |  |  |
| `account.individual.address_kanji.city` | string |  |  |
| `account.individual.address_kanji.country` | string |  |  |
| `account.individual.address_kanji.line1` | string |  |  |
| `account.individual.address_kanji.line2` | string |  |  |
| `account.individual.address_kanji.postal_code` | string |  |  |
| `account.individual.address_kanji.state` | string |  |  |
| `account.individual.address_kanji.town` | string |  |  |
| `account.individual.dob` | object or "" (to unset) |  |  |
| `account.individual.dob.day` | integer | yes |  |
| `account.individual.dob.month` | integer | yes |  |
| `account.individual.dob.year` | integer | yes |  |
| `account.individual.email` | string |  |  |
| `account.individual.first_name` | string |  |  |
| `account.individual.first_name_kana` | string |  |  |
| `account.individual.first_name_kanji` | string |  |  |
| `account.individual.full_name_aliases` | array of string or "" (to unset) |  |  |
| `account.individual.gender` | string |  |  |
| `account.individual.id_number` | string |  |  |
| `account.individual.id_number_secondary` | string |  |  |
| `account.individual.last_name` | string |  |  |
| `account.individual.last_name_kana` | string |  |  |
| `account.individual.last_name_kanji` | string |  |  |
| `account.individual.maiden_name` | string |  |  |
| `account.individual.metadata` | map (key → value) or "" (to unset) |  |  |
| `account.individual.phone` | string |  |  |
| `account.individual.political_exposure` | enum: `existing`, `none` |  |  |
| `account.individual.registered_address` | object |  |  |
| `account.individual.registered_address.city` | string |  |  |
| `account.individual.registered_address.country` | string |  |  |
| `account.individual.registered_address.line1` | string |  |  |
| `account.individual.registered_address.line2` | string |  |  |
| `account.individual.registered_address.postal_code` | string |  |  |
| `account.individual.registered_address.state` | string |  |  |
| `account.individual.relationship` | object |  |  |
| `account.individual.relationship.director` | boolean |  |  |
| `account.individual.relationship.executive` | boolean |  |  |
| `account.individual.relationship.owner` | boolean |  |  |
| `account.individual.relationship.percent_ownership` | number or "" (to unset) |  |  |
| `account.individual.relationship.title` | string |  |  |
| `account.individual.ssn_last_4` | string |  |  |
| `account.individual.verification` | object |  |  |
| `account.individual.verification.additional_document` | object |  |  |
| `account.individual.verification.additional_document.back` | string |  |  |
| `account.individual.verification.additional_document.front` | string |  |  |
| `account.individual.verification.document` | object |  |  |
| `account.individual.verification.document.back` | string |  |  |
| `account.individual.verification.document.front` | string |  |  |
| `account.tos_shown_and_accepted` | boolean |  |  |
| `bank_account` | object (open enum) |  | The bank account this token will represent. |
| `bank_account.account_holder_name` | string |  |  |
| `bank_account.account_holder_type` | enum: `company`, `individual` |  |  |
| `bank_account.account_number` | string | yes |  |
| `bank_account.account_type` | enum: `checking`, `futsu`, `savings`, `toza` |  |  |
| `bank_account.country` | string | yes |  |
| `bank_account.currency` | string |  |  |
| `bank_account.payment_method` | string |  |  |
| `bank_account.routing_number` | string |  |  |
| `card` | object or string |  | The card this token will represent. If you also pass in a customer, the card must be the ID of a card belonging to the customer. Otherwise, if you do not pass in a customer, this is a dictionary containing a user's credit card details, with the options described below. |
| `card.address_city` | string |  |  |
| `card.address_country` | string |  |  |
| `card.address_line1` | string |  |  |
| `card.address_line2` | string |  |  |
| `card.address_state` | string |  |  |
| `card.address_zip` | string |  |  |
| `card.currency` | string |  |  |
| `card.cvc` | string |  |  |
| `card.exp_month` | string | yes |  |
| `card.exp_year` | string | yes |  |
| `card.name` | string |  |  |
| `card.networks` | object |  |  |
| `card.networks.preferred` | enum: `cartes_bancaires`, `mastercard`, `visa` |  |  |
| `card.number` | string | yes |  |
| `customer` | string |  | Create a token for the customer, which is owned by the application's account. You can only use this with an [OAuth access token](https://stripe.com/docs/connect/standard-accounts) or [Stripe-Account header](https://stripe.com/docs/connect/authentication). Learn more about [cloning saved payment methods](https://stripe.com/docs/connect/cloning-saved-payment-methods). |
| `cvc_update` | object |  | The updated CVC value this token represents. |
| `cvc_update.cvc` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `person` | object |  | Information for the person this token represents. |
| `person.additional_tos_acceptances` | object |  |  |
| `person.additional_tos_acceptances.account` | object |  |  |
| `person.additional_tos_acceptances.account.date` | timestamp (Unix seconds) |  |  |
| `person.additional_tos_acceptances.account.ip` | string |  |  |
| `person.additional_tos_acceptances.account.user_agent` | string or "" (to unset) |  |  |
| `person.address` | object |  |  |
| `person.address.city` | string |  |  |
| `person.address.country` | string |  |  |
| `person.address.line1` | string |  |  |
| `person.address.line2` | string |  |  |
| `person.address.postal_code` | string |  |  |
| `person.address.state` | string |  |  |
| `person.address_kana` | object |  |  |
| `person.address_kana.city` | string |  |  |
| `person.address_kana.country` | string |  |  |
| `person.address_kana.line1` | string |  |  |
| `person.address_kana.line2` | string |  |  |
| `person.address_kana.postal_code` | string |  |  |
| `person.address_kana.state` | string |  |  |
| `person.address_kana.town` | string |  |  |
| `person.address_kanji` | object |  |  |
| `person.address_kanji.city` | string |  |  |
| `person.address_kanji.country` | string |  |  |
| `person.address_kanji.line1` | string |  |  |
| `person.address_kanji.line2` | string |  |  |
| `person.address_kanji.postal_code` | string |  |  |
| `person.address_kanji.state` | string |  |  |
| `person.address_kanji.town` | string |  |  |
| `person.dob` | object or "" (to unset) |  |  |
| `person.dob.day` | integer | yes |  |
| `person.dob.month` | integer | yes |  |
| `person.dob.year` | integer | yes |  |
| `person.documents` | object |  |  |
| `person.documents.company_authorization` | object |  |  |
| `person.documents.company_authorization.files` | array of string or "" (to unset) |  |  |
| `person.documents.passport` | object |  |  |
| `person.documents.passport.files` | array of string or "" (to unset) |  |  |
| `person.documents.visa` | object |  |  |
| `person.documents.visa.files` | array of string or "" (to unset) |  |  |
| `person.email` | string |  |  |
| `person.first_name` | string |  |  |
| `person.first_name_kana` | string |  |  |
| `person.first_name_kanji` | string |  |  |
| `person.full_name_aliases` | array of string or "" (to unset) |  |  |
| `person.gender` | string |  |  |
| `person.id_number` | string |  |  |
| `person.id_number_secondary` | string |  |  |
| `person.last_name` | string |  |  |
| `person.last_name_kana` | string |  |  |
| `person.last_name_kanji` | string |  |  |
| `person.maiden_name` | string |  |  |
| `person.metadata` | map (key → value) or "" (to unset) |  |  |
| `person.nationality` | string |  |  |
| `person.phone` | string |  |  |
| `person.political_exposure` | string |  |  |
| `person.registered_address` | object |  |  |
| `person.registered_address.city` | string |  |  |
| `person.registered_address.country` | string |  |  |
| `person.registered_address.line1` | string |  |  |
| `person.registered_address.line2` | string |  |  |
| `person.registered_address.postal_code` | string |  |  |
| `person.registered_address.state` | string |  |  |
| `person.relationship` | object |  |  |
| `person.relationship.director` | boolean |  |  |
| `person.relationship.executive` | boolean |  |  |
| `person.relationship.legal_guardian` | boolean |  |  |
| `person.relationship.owner` | boolean |  |  |
| `person.relationship.percent_ownership` | number or "" (to unset) |  |  |
| `person.relationship.representative` | boolean |  |  |
| `person.relationship.title` | string |  |  |
| `person.ssn_last_4` | string |  |  |
| `person.verification` | object |  |  |
| `person.verification.additional_document` | object |  |  |
| `person.verification.additional_document.back` | string |  |  |
| `person.verification.additional_document.front` | string |  |  |
| `person.verification.document` | object |  |  |
| `person.verification.document.back` | string |  |  |
| `person.verification.document.front` | string |  |  |
| `pii` | object |  | The PII this token represents. |
| `pii.id_number` | string |  |  |

Returns: `token`

## GET /v1/tokens/{token}

operationId: `GetTokensToken`

Retrieves the token with the given ID.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `token (path)` | string | yes |  |

Returns: `token`

# Objects returned

## The `token` object

Tokenization is the process Stripe uses to collect sensitive card or bank
account details, or personally identifiable information (PII), directly from
your customers in a secure manner. A token representing this information is
returned to your server to use. Use our
[recommended payments integrations](https://stripe.com/docs/payments) to perform this process
on the client-side. This guarantees that no sensitive card data touches your server,
and allows your integration to operate in a PCI-compliant way.

If you can't use client-side tokenization, you can also create tokens using
the API with either your publishable or secret API key. If
your integration uses this method, you're responsible for any PCI compliance
that it might require, and you must keep your secret API key safe. Unlike with
client-side tokenization, your customer's information isn't sent directly to
Stripe, so we can't determine how it's handled or stored.

You can't store or use tokens more than once. To store card or bank account
information for later use, create [Customer](https://stripe.com/docs/api#customers)
objects or [Custom accounts](https://stripe.com/docs/api#external_accounts).
[Radar](https://stripe.com/docs/radar), our integrated solution for automatic fraud protection,
performs best with integrations that use client-side tokenization.

Expandable fields (pass `expand[]=<field>`): `bank_account`, `card`

| Field | Type | Required | Description |
|---|---|---|---|
| `bank_account` | `bank_account` |  |  |
| `card` | `card` |  |  |
| `client_ip` | string |  | IP address of the client that generates the token. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `object` | enum: `token` | yes | String representing the object's type. Objects of the same type share the same value. |
| `type` | string | yes | Type of the token: `account`, `bank_account`, `card`, or `pii`. |
| `used` | boolean | yes | Determines if you have already used this token (you can only use tokens once). |

