# Stripe API 2023-10-16 — accounts

Operations under `/v1/accounts` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/accounts

operationId: `GetAccounts`

Returns a list of accounts connected to your platform via [Connect](https://stripe.com/docs/connect). If you’re not a platform, the list is empty.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | object or integer |  | Only return connected accounts that were created during the given date interval. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/accounts

operationId: `PostAccounts`

With [Connect](https://stripe.com/docs/connect), you can create Stripe accounts for your users.
To do this, you’ll first need to [register your platform](https://dashboard.stripe.com/account/applications/settings).

If you’ve already collected information for your connected accounts, you [can prefill that information](https://stripe.com/docs/connect/best-practices#onboarding) when
creating the account. Connect Onboarding won’t ask for the prefilled information during account onboarding.
You can prefill any information on the account.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account_token` | string |  | An [account token](https://stripe.com/docs/api#create_account_token), used to securely provide details to the account. |
| `bank_account` | object or string |  | Either a token, like the ones returned by [Stripe.js](https://stripe.com/docs/js), or a dictionary containing a user's bank account details. |
| `bank_account.account_holder_name` | string |  |  |
| `bank_account.account_holder_type` | enum: `company`, `individual` |  |  |
| `bank_account.account_number` | string | yes |  |
| `bank_account.account_type` | enum: `checking`, `futsu`, `savings`, `toza` |  |  |
| `bank_account.country` | string | yes |  |
| `bank_account.currency` | string |  |  |
| `bank_account.documents` | object |  |  |
| `bank_account.documents.bank_account_ownership_verification` | object |  |  |
| `bank_account.documents.bank_account_ownership_verification.files` | array of string |  |  |
| `bank_account.object` | enum: `bank_account` |  |  |
| `bank_account.routing_number` | string |  |  |
| `business_profile` | object |  | Business information about the account. |
| `business_profile.annual_revenue` | object |  |  |
| `business_profile.annual_revenue.amount` | integer | yes |  |
| `business_profile.annual_revenue.currency` | string | yes |  |
| `business_profile.annual_revenue.fiscal_year_end` | string | yes |  |
| `business_profile.estimated_worker_count` | integer |  |  |
| `business_profile.mcc` | string |  |  |
| `business_profile.monthly_estimated_revenue` | object |  |  |
| `business_profile.monthly_estimated_revenue.amount` | integer | yes |  |
| `business_profile.monthly_estimated_revenue.currency` | string | yes |  |
| `business_profile.name` | string |  |  |
| `business_profile.product_description` | string |  |  |
| `business_profile.support_address` | object |  |  |
| `business_profile.support_address.city` | string |  |  |
| `business_profile.support_address.country` | string |  |  |
| `business_profile.support_address.line1` | string |  |  |
| `business_profile.support_address.line2` | string |  |  |
| `business_profile.support_address.postal_code` | string |  |  |
| `business_profile.support_address.state` | string |  |  |
| `business_profile.support_email` | string |  |  |
| `business_profile.support_phone` | string |  |  |
| `business_profile.support_url` | string or "" (to unset) |  |  |
| `business_profile.url` | string |  |  |
| `business_type` | enum: `company`, `government_entity`, `individual`, `non_profit` |  | The business type. Once you create an [Account Link](https://docs.stripe.com/api/account_links) or [Account Session](https://docs.stripe.com/api/account_sessions), this property can only be updated for Custom accounts. |
| `capabilities` | object |  | Each key of the dictionary represents a capability, and each capability maps to its settings (e.g. whether it has been requested or not). Each capability will be inactive until you have provided its specific requirements and Stripe has verified them. An account may have some of its requested capabilities be active and some be inactive. |
| `capabilities.acss_debit_payments` | object |  |  |
| `capabilities.acss_debit_payments.requested` | boolean |  |  |
| `capabilities.affirm_payments` | object |  |  |
| `capabilities.affirm_payments.requested` | boolean |  |  |
| `capabilities.afterpay_clearpay_payments` | object |  |  |
| `capabilities.afterpay_clearpay_payments.requested` | boolean |  |  |
| `capabilities.amazon_pay_payments` | object |  |  |
| `capabilities.amazon_pay_payments.requested` | boolean |  |  |
| `capabilities.au_becs_debit_payments` | object |  |  |
| `capabilities.au_becs_debit_payments.requested` | boolean |  |  |
| `capabilities.bacs_debit_payments` | object |  |  |
| `capabilities.bacs_debit_payments.requested` | boolean |  |  |
| `capabilities.bancontact_payments` | object |  |  |
| `capabilities.bancontact_payments.requested` | boolean |  |  |
| `capabilities.bank_transfer_payments` | object |  |  |
| `capabilities.bank_transfer_payments.requested` | boolean |  |  |
| `capabilities.blik_payments` | object |  |  |
| `capabilities.blik_payments.requested` | boolean |  |  |
| `capabilities.boleto_payments` | object |  |  |
| `capabilities.boleto_payments.requested` | boolean |  |  |
| `capabilities.card_issuing` | object |  |  |
| `capabilities.card_issuing.requested` | boolean |  |  |
| `capabilities.card_payments` | object |  |  |
| `capabilities.card_payments.requested` | boolean |  |  |
| `capabilities.cartes_bancaires_payments` | object |  |  |
| `capabilities.cartes_bancaires_payments.requested` | boolean |  |  |
| `capabilities.cashapp_payments` | object |  |  |
| `capabilities.cashapp_payments.requested` | boolean |  |  |
| `capabilities.eps_payments` | object |  |  |
| `capabilities.eps_payments.requested` | boolean |  |  |
| `capabilities.fpx_payments` | object |  |  |
| `capabilities.fpx_payments.requested` | boolean |  |  |
| `capabilities.giropay_payments` | object |  |  |
| `capabilities.giropay_payments.requested` | boolean |  |  |
| `capabilities.grabpay_payments` | object |  |  |
| `capabilities.grabpay_payments.requested` | boolean |  |  |
| `capabilities.ideal_payments` | object |  |  |
| `capabilities.ideal_payments.requested` | boolean |  |  |
| `capabilities.india_international_payments` | object |  |  |
| `capabilities.india_international_payments.requested` | boolean |  |  |
| `capabilities.jcb_payments` | object |  |  |
| `capabilities.jcb_payments.requested` | boolean |  |  |
| `capabilities.klarna_payments` | object |  |  |
| `capabilities.klarna_payments.requested` | boolean |  |  |
| `capabilities.konbini_payments` | object |  |  |
| `capabilities.konbini_payments.requested` | boolean |  |  |
| `capabilities.legacy_payments` | object |  |  |
| `capabilities.legacy_payments.requested` | boolean |  |  |
| `capabilities.link_payments` | object |  |  |
| `capabilities.link_payments.requested` | boolean |  |  |
| `capabilities.mobilepay_payments` | object |  |  |
| `capabilities.mobilepay_payments.requested` | boolean |  |  |
| `capabilities.oxxo_payments` | object |  |  |
| `capabilities.oxxo_payments.requested` | boolean |  |  |
| `capabilities.p24_payments` | object |  |  |
| `capabilities.p24_payments.requested` | boolean |  |  |
| `capabilities.paynow_payments` | object |  |  |
| `capabilities.paynow_payments.requested` | boolean |  |  |
| `capabilities.promptpay_payments` | object |  |  |
| `capabilities.promptpay_payments.requested` | boolean |  |  |
| `capabilities.revolut_pay_payments` | object |  |  |
| `capabilities.revolut_pay_payments.requested` | boolean |  |  |
| `capabilities.sepa_debit_payments` | object |  |  |
| `capabilities.sepa_debit_payments.requested` | boolean |  |  |
| `capabilities.sofort_payments` | object |  |  |
| `capabilities.sofort_payments.requested` | boolean |  |  |
| `capabilities.swish_payments` | object |  |  |
| `capabilities.swish_payments.requested` | boolean |  |  |
| `capabilities.tax_reporting_us_1099_k` | object |  |  |
| `capabilities.tax_reporting_us_1099_k.requested` | boolean |  |  |
| `capabilities.tax_reporting_us_1099_misc` | object |  |  |
| `capabilities.tax_reporting_us_1099_misc.requested` | boolean |  |  |
| `capabilities.transfers` | object |  |  |
| `capabilities.transfers.requested` | boolean |  |  |
| `capabilities.treasury` | object |  |  |
| `capabilities.treasury.requested` | boolean |  |  |
| `capabilities.us_bank_account_ach_payments` | object |  |  |
| `capabilities.us_bank_account_ach_payments.requested` | boolean |  |  |
| `capabilities.zip_payments` | object |  |  |
| `capabilities.zip_payments.requested` | boolean |  |  |
| `company` | object |  | Information about the company or business. This field is available for any `business_type`. Once you create an [Account Link](https://docs.stripe.com/api/account_links) or [Account Session](https://docs.stripe.com/api/account_sessions), this property can only be updated for Custom accounts. |
| `company.address` | object |  |  |
| `company.address.city` | string |  |  |
| `company.address.country` | string |  |  |
| `company.address.line1` | string |  |  |
| `company.address.line2` | string |  |  |
| `company.address.postal_code` | string |  |  |
| `company.address.state` | string |  |  |
| `company.address_kana` | object |  |  |
| `company.address_kana.city` | string |  |  |
| `company.address_kana.country` | string |  |  |
| `company.address_kana.line1` | string |  |  |
| `company.address_kana.line2` | string |  |  |
| `company.address_kana.postal_code` | string |  |  |
| `company.address_kana.state` | string |  |  |
| `company.address_kana.town` | string |  |  |
| `company.address_kanji` | object |  |  |
| `company.address_kanji.city` | string |  |  |
| `company.address_kanji.country` | string |  |  |
| `company.address_kanji.line1` | string |  |  |
| `company.address_kanji.line2` | string |  |  |
| `company.address_kanji.postal_code` | string |  |  |
| `company.address_kanji.state` | string |  |  |
| `company.address_kanji.town` | string |  |  |
| `company.directors_provided` | boolean |  |  |
| `company.executives_provided` | boolean |  |  |
| `company.export_license_id` | string |  |  |
| `company.export_purpose_code` | string |  |  |
| `company.name` | string |  |  |
| `company.name_kana` | string |  |  |
| `company.name_kanji` | string |  |  |
| `company.owners_provided` | boolean |  |  |
| `company.ownership_declaration` | object |  |  |
| `company.ownership_declaration.date` | timestamp (Unix seconds) |  |  |
| `company.ownership_declaration.ip` | string |  |  |
| `company.ownership_declaration.user_agent` | string |  |  |
| `company.phone` | string |  |  |
| `company.registration_number` | string |  |  |
| `company.structure` | enum: ``, `free_zone_establishment`, `free_zone_llc`, `government_instrumentality`, `governmental_unit`, `incorporated_non_profit`, `incorporated_partnership`, `limited_liability_partnership`, `llc`, `multi_member_llc`, `private_company`, `private_corporation`, `private_partnership`, `public_company`, `public_corporation`, `public_partnership`, `registered_charity`, `single_member_llc`, `sole_establishment`, `sole_proprietorship`, `tax_exempt_government_instrumentality`, `unincorporated_association`, `unincorporated_non_profit`, `unincorporated_partnership` |  |  |
| `company.tax_id` | string |  |  |
| `company.tax_id_registrar` | string |  |  |
| `company.vat_id` | string |  |  |
| `company.verification` | object |  |  |
| `company.verification.document` | object |  |  |
| `company.verification.document.back` | string |  |  |
| `company.verification.document.front` | string |  |  |
| `country` | string |  | The country in which the account holder resides, or in which the business is legally established. This should be an ISO 3166-1 alpha-2 country code. For example, if you are in the United States and the business for which you're creating an account is legally represented in Canada, you would use `CA` as the country for the account being created. Available countries include [Stripe's global markets](https://stripe.com/global) as well as countries where [cross-border payouts](https://stripe.com/docs/connect/cross-border-payouts) are supported. |
| `default_currency` | string |  | Three-letter ISO currency code representing the default currency for the account. This must be a currency that [Stripe supports in the account's country](https://docs.stripe.com/payouts). |
| `documents` | object |  | Documents that may be submitted to satisfy various informational requests. |
| `documents.bank_account_ownership_verification` | object |  |  |
| `documents.bank_account_ownership_verification.files` | array of string |  |  |
| `documents.company_license` | object |  |  |
| `documents.company_license.files` | array of string |  |  |
| `documents.company_memorandum_of_association` | object |  |  |
| `documents.company_memorandum_of_association.files` | array of string |  |  |
| `documents.company_ministerial_decree` | object |  |  |
| `documents.company_ministerial_decree.files` | array of string |  |  |
| `documents.company_registration_verification` | object |  |  |
| `documents.company_registration_verification.files` | array of string |  |  |
| `documents.company_tax_id_verification` | object |  |  |
| `documents.company_tax_id_verification.files` | array of string |  |  |
| `documents.proof_of_registration` | object |  |  |
| `documents.proof_of_registration.files` | array of string |  |  |
| `email` | string |  | The email address of the account holder. This is only to make the account easier to identify to you. Stripe only emails Custom accounts with your consent. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `external_account` | string (open enum) |  | A card or bank account to attach to the account for receiving [payouts](https://docs.stripe.com/connect/bank-debit-card-payouts) (you won’t be able to use it for top-ups). You can provide either a token, like the ones returned by [Stripe.js](https://docs.stripe.com/js), or a dictionary, as documented in the `external_account` parameter for [bank account](https://docs.stripe.com/api#account_create_bank_account) creation. <br>By default, providing an external account sets it as the new default external account for its currency, and deletes the old default if one exists. To add additional external accounts without replacing the existing default for the currency, use the [bank account](https://docs.stripe.com/api#account_create_bank_account) or [card creation](https://docs.stripe.com/api#account_create_card) APIs. After you create an [Account Link](https://docs.stripe.com/api/account_links) or [Account Session](https://docs.stripe.com/api/account_sessions), this property can only be updated for Custom accounts. |
| `individual` | object |  | Information about the person represented by the account. This field is null unless `business_type` is set to `individual`. Once you create an [Account Link](https://docs.stripe.com/api/account_links) or [Account Session](https://docs.stripe.com/api/account_sessions), this property can only be updated for Custom accounts. |
| `individual.address` | object |  |  |
| `individual.address.city` | string |  |  |
| `individual.address.country` | string |  |  |
| `individual.address.line1` | string |  |  |
| `individual.address.line2` | string |  |  |
| `individual.address.postal_code` | string |  |  |
| `individual.address.state` | string |  |  |
| `individual.address_kana` | object |  |  |
| `individual.address_kana.city` | string |  |  |
| `individual.address_kana.country` | string |  |  |
| `individual.address_kana.line1` | string |  |  |
| `individual.address_kana.line2` | string |  |  |
| `individual.address_kana.postal_code` | string |  |  |
| `individual.address_kana.state` | string |  |  |
| `individual.address_kana.town` | string |  |  |
| `individual.address_kanji` | object |  |  |
| `individual.address_kanji.city` | string |  |  |
| `individual.address_kanji.country` | string |  |  |
| `individual.address_kanji.line1` | string |  |  |
| `individual.address_kanji.line2` | string |  |  |
| `individual.address_kanji.postal_code` | string |  |  |
| `individual.address_kanji.state` | string |  |  |
| `individual.address_kanji.town` | string |  |  |
| `individual.dob` | object or "" (to unset) |  |  |
| `individual.dob.day` | integer | yes |  |
| `individual.dob.month` | integer | yes |  |
| `individual.dob.year` | integer | yes |  |
| `individual.email` | string |  |  |
| `individual.first_name` | string |  |  |
| `individual.first_name_kana` | string |  |  |
| `individual.first_name_kanji` | string |  |  |
| `individual.full_name_aliases` | array of string or "" (to unset) |  |  |
| `individual.gender` | string |  |  |
| `individual.id_number` | string |  |  |
| `individual.id_number_secondary` | string |  |  |
| `individual.last_name` | string |  |  |
| `individual.last_name_kana` | string |  |  |
| `individual.last_name_kanji` | string |  |  |
| `individual.maiden_name` | string |  |  |
| `individual.metadata` | map (key → value) or "" (to unset) |  |  |
| `individual.phone` | string |  |  |
| `individual.political_exposure` | enum: `existing`, `none` |  |  |
| `individual.registered_address` | object |  |  |
| `individual.registered_address.city` | string |  |  |
| `individual.registered_address.country` | string |  |  |
| `individual.registered_address.line1` | string |  |  |
| `individual.registered_address.line2` | string |  |  |
| `individual.registered_address.postal_code` | string |  |  |
| `individual.registered_address.state` | string |  |  |
| `individual.relationship` | object |  |  |
| `individual.relationship.director` | boolean |  |  |
| `individual.relationship.executive` | boolean |  |  |
| `individual.relationship.owner` | boolean |  |  |
| `individual.relationship.percent_ownership` | number or "" (to unset) |  |  |
| `individual.relationship.title` | string |  |  |
| `individual.ssn_last_4` | string |  |  |
| `individual.verification` | object |  |  |
| `individual.verification.additional_document` | object |  |  |
| `individual.verification.additional_document.back` | string |  |  |
| `individual.verification.additional_document.front` | string |  |  |
| `individual.verification.document` | object |  |  |
| `individual.verification.document.back` | string |  |  |
| `individual.verification.document.front` | string |  |  |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `settings` | object |  | Options for customizing how the account functions within Stripe. |
| `settings.bacs_debit_payments` | object |  |  |
| `settings.bacs_debit_payments.display_name` | string |  |  |
| `settings.branding` | object |  |  |
| `settings.branding.icon` | string |  |  |
| `settings.branding.logo` | string |  |  |
| `settings.branding.primary_color` | string |  |  |
| `settings.branding.secondary_color` | string |  |  |
| `settings.card_issuing` | object |  |  |
| `settings.card_issuing.tos_acceptance` | object |  |  |
| `settings.card_issuing.tos_acceptance.date` | timestamp (Unix seconds) |  |  |
| `settings.card_issuing.tos_acceptance.ip` | string |  |  |
| `settings.card_issuing.tos_acceptance.user_agent` | string or "" (to unset) |  |  |
| `settings.card_payments` | object |  |  |
| `settings.card_payments.decline_on` | object |  |  |
| `settings.card_payments.decline_on.avs_failure` | boolean |  |  |
| `settings.card_payments.decline_on.cvc_failure` | boolean |  |  |
| `settings.card_payments.statement_descriptor_prefix` | string |  |  |
| `settings.card_payments.statement_descriptor_prefix_kana` | string or "" (to unset) |  |  |
| `settings.card_payments.statement_descriptor_prefix_kanji` | string or "" (to unset) |  |  |
| `settings.payments` | object |  |  |
| `settings.payments.statement_descriptor` | string |  |  |
| `settings.payments.statement_descriptor_kana` | string |  |  |
| `settings.payments.statement_descriptor_kanji` | string |  |  |
| `settings.payouts` | object |  |  |
| `settings.payouts.debit_negative_balances` | boolean |  |  |
| `settings.payouts.schedule` | object |  |  |
| `settings.payouts.schedule.delay_days` | enum: `minimum` or integer |  |  |
| `settings.payouts.schedule.interval` | enum: `daily`, `manual`, `monthly`, `weekly` |  |  |
| `settings.payouts.schedule.monthly_anchor` | integer |  |  |
| `settings.payouts.schedule.weekly_anchor` | enum: `friday`, `monday`, `saturday`, `sunday`, `thursday`, `tuesday`, `wednesday` |  |  |
| `settings.payouts.statement_descriptor` | string |  |  |
| `settings.treasury` | object |  |  |
| `settings.treasury.tos_acceptance` | object |  |  |
| `settings.treasury.tos_acceptance.date` | timestamp (Unix seconds) |  |  |
| `settings.treasury.tos_acceptance.ip` | string |  |  |
| `settings.treasury.tos_acceptance.user_agent` | string or "" (to unset) |  |  |
| `tos_acceptance` | object |  | Details on the account's acceptance of the [Stripe Services Agreement](https://docs.stripe.com/connect/updating-accounts#tos-acceptance) This property can only be updated for Custom accounts. |
| `tos_acceptance.date` | timestamp (Unix seconds) |  |  |
| `tos_acceptance.ip` | string |  |  |
| `tos_acceptance.service_agreement` | string |  |  |
| `tos_acceptance.user_agent` | string |  |  |
| `type` | enum: `custom`, `express`, `standard` |  | The type of Stripe account to create. May be one of `custom`, `express` or `standard`. |

Returns: `account`

## GET /v1/accounts/{account}

operationId: `GetAccountsAccount`

Retrieves the details of an account.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `account`

## POST /v1/accounts/{account}

operationId: `PostAccountsAccount`

Updates a [connected account](https://stripe.com/docs/connect/accounts) by setting the values of the parameters passed. Any parameters not provided are
left unchanged.

For Custom accounts, you can update any information on the account. For other accounts, you can update all information until that
account has started to go through Connect Onboarding. Once you create an [Account Link](https://stripe.com/docs/api/account_links) or [Account Session](https://stripe.com/docs/api/account_sessions),
some properties can only be changed or updated for Custom accounts.

To update your own account, use the [Dashboard](https://dashboard.stripe.com/settings/account). Refer to our
[Connect](https://stripe.com/docs/connect/updating-accounts) documentation to learn more about updating accounts.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account (path)` | string | yes |  |
| `account_token` | string |  | An [account token](https://stripe.com/docs/api#create_account_token), used to securely provide details to the account. |
| `business_profile` | object |  | Business information about the account. |
| `business_profile.annual_revenue` | object |  |  |
| `business_profile.annual_revenue.amount` | integer | yes |  |
| `business_profile.annual_revenue.currency` | string | yes |  |
| `business_profile.annual_revenue.fiscal_year_end` | string | yes |  |
| `business_profile.estimated_worker_count` | integer |  |  |
| `business_profile.mcc` | string |  |  |
| `business_profile.monthly_estimated_revenue` | object |  |  |
| `business_profile.monthly_estimated_revenue.amount` | integer | yes |  |
| `business_profile.monthly_estimated_revenue.currency` | string | yes |  |
| `business_profile.name` | string |  |  |
| `business_profile.product_description` | string |  |  |
| `business_profile.support_address` | object |  |  |
| `business_profile.support_address.city` | string |  |  |
| `business_profile.support_address.country` | string |  |  |
| `business_profile.support_address.line1` | string |  |  |
| `business_profile.support_address.line2` | string |  |  |
| `business_profile.support_address.postal_code` | string |  |  |
| `business_profile.support_address.state` | string |  |  |
| `business_profile.support_email` | string |  |  |
| `business_profile.support_phone` | string |  |  |
| `business_profile.support_url` | string or "" (to unset) |  |  |
| `business_profile.url` | string |  |  |
| `business_type` | enum: `company`, `government_entity`, `individual`, `non_profit` |  | The business type. Once you create an [Account Link](https://docs.stripe.com/api/account_links) or [Account Session](https://docs.stripe.com/api/account_sessions), this property can only be updated for Custom accounts. |
| `capabilities` | object |  | Each key of the dictionary represents a capability, and each capability maps to its settings (e.g. whether it has been requested or not). Each capability will be inactive until you have provided its specific requirements and Stripe has verified them. An account may have some of its requested capabilities be active and some be inactive. |
| `capabilities.acss_debit_payments` | object |  |  |
| `capabilities.acss_debit_payments.requested` | boolean |  |  |
| `capabilities.affirm_payments` | object |  |  |
| `capabilities.affirm_payments.requested` | boolean |  |  |
| `capabilities.afterpay_clearpay_payments` | object |  |  |
| `capabilities.afterpay_clearpay_payments.requested` | boolean |  |  |
| `capabilities.amazon_pay_payments` | object |  |  |
| `capabilities.amazon_pay_payments.requested` | boolean |  |  |
| `capabilities.au_becs_debit_payments` | object |  |  |
| `capabilities.au_becs_debit_payments.requested` | boolean |  |  |
| `capabilities.bacs_debit_payments` | object |  |  |
| `capabilities.bacs_debit_payments.requested` | boolean |  |  |
| `capabilities.bancontact_payments` | object |  |  |
| `capabilities.bancontact_payments.requested` | boolean |  |  |
| `capabilities.bank_transfer_payments` | object |  |  |
| `capabilities.bank_transfer_payments.requested` | boolean |  |  |
| `capabilities.blik_payments` | object |  |  |
| `capabilities.blik_payments.requested` | boolean |  |  |
| `capabilities.boleto_payments` | object |  |  |
| `capabilities.boleto_payments.requested` | boolean |  |  |
| `capabilities.card_issuing` | object |  |  |
| `capabilities.card_issuing.requested` | boolean |  |  |
| `capabilities.card_payments` | object |  |  |
| `capabilities.card_payments.requested` | boolean |  |  |
| `capabilities.cartes_bancaires_payments` | object |  |  |
| `capabilities.cartes_bancaires_payments.requested` | boolean |  |  |
| `capabilities.cashapp_payments` | object |  |  |
| `capabilities.cashapp_payments.requested` | boolean |  |  |
| `capabilities.eps_payments` | object |  |  |
| `capabilities.eps_payments.requested` | boolean |  |  |
| `capabilities.fpx_payments` | object |  |  |
| `capabilities.fpx_payments.requested` | boolean |  |  |
| `capabilities.giropay_payments` | object |  |  |
| `capabilities.giropay_payments.requested` | boolean |  |  |
| `capabilities.grabpay_payments` | object |  |  |
| `capabilities.grabpay_payments.requested` | boolean |  |  |
| `capabilities.ideal_payments` | object |  |  |
| `capabilities.ideal_payments.requested` | boolean |  |  |
| `capabilities.india_international_payments` | object |  |  |
| `capabilities.india_international_payments.requested` | boolean |  |  |
| `capabilities.jcb_payments` | object |  |  |
| `capabilities.jcb_payments.requested` | boolean |  |  |
| `capabilities.klarna_payments` | object |  |  |
| `capabilities.klarna_payments.requested` | boolean |  |  |
| `capabilities.konbini_payments` | object |  |  |
| `capabilities.konbini_payments.requested` | boolean |  |  |
| `capabilities.legacy_payments` | object |  |  |
| `capabilities.legacy_payments.requested` | boolean |  |  |
| `capabilities.link_payments` | object |  |  |
| `capabilities.link_payments.requested` | boolean |  |  |
| `capabilities.mobilepay_payments` | object |  |  |
| `capabilities.mobilepay_payments.requested` | boolean |  |  |
| `capabilities.oxxo_payments` | object |  |  |
| `capabilities.oxxo_payments.requested` | boolean |  |  |
| `capabilities.p24_payments` | object |  |  |
| `capabilities.p24_payments.requested` | boolean |  |  |
| `capabilities.paynow_payments` | object |  |  |
| `capabilities.paynow_payments.requested` | boolean |  |  |
| `capabilities.promptpay_payments` | object |  |  |
| `capabilities.promptpay_payments.requested` | boolean |  |  |
| `capabilities.revolut_pay_payments` | object |  |  |
| `capabilities.revolut_pay_payments.requested` | boolean |  |  |
| `capabilities.sepa_debit_payments` | object |  |  |
| `capabilities.sepa_debit_payments.requested` | boolean |  |  |
| `capabilities.sofort_payments` | object |  |  |
| `capabilities.sofort_payments.requested` | boolean |  |  |
| `capabilities.swish_payments` | object |  |  |
| `capabilities.swish_payments.requested` | boolean |  |  |
| `capabilities.tax_reporting_us_1099_k` | object |  |  |
| `capabilities.tax_reporting_us_1099_k.requested` | boolean |  |  |
| `capabilities.tax_reporting_us_1099_misc` | object |  |  |
| `capabilities.tax_reporting_us_1099_misc.requested` | boolean |  |  |
| `capabilities.transfers` | object |  |  |
| `capabilities.transfers.requested` | boolean |  |  |
| `capabilities.treasury` | object |  |  |
| `capabilities.treasury.requested` | boolean |  |  |
| `capabilities.us_bank_account_ach_payments` | object |  |  |
| `capabilities.us_bank_account_ach_payments.requested` | boolean |  |  |
| `capabilities.zip_payments` | object |  |  |
| `capabilities.zip_payments.requested` | boolean |  |  |
| `company` | object |  | Information about the company or business. This field is available for any `business_type`. Once you create an [Account Link](https://docs.stripe.com/api/account_links) or [Account Session](https://docs.stripe.com/api/account_sessions), this property can only be updated for Custom accounts. |
| `company.address` | object |  |  |
| `company.address.city` | string |  |  |
| `company.address.country` | string |  |  |
| `company.address.line1` | string |  |  |
| `company.address.line2` | string |  |  |
| `company.address.postal_code` | string |  |  |
| `company.address.state` | string |  |  |
| `company.address_kana` | object |  |  |
| `company.address_kana.city` | string |  |  |
| `company.address_kana.country` | string |  |  |
| `company.address_kana.line1` | string |  |  |
| `company.address_kana.line2` | string |  |  |
| `company.address_kana.postal_code` | string |  |  |
| `company.address_kana.state` | string |  |  |
| `company.address_kana.town` | string |  |  |
| `company.address_kanji` | object |  |  |
| `company.address_kanji.city` | string |  |  |
| `company.address_kanji.country` | string |  |  |
| `company.address_kanji.line1` | string |  |  |
| `company.address_kanji.line2` | string |  |  |
| `company.address_kanji.postal_code` | string |  |  |
| `company.address_kanji.state` | string |  |  |
| `company.address_kanji.town` | string |  |  |
| `company.directors_provided` | boolean |  |  |
| `company.executives_provided` | boolean |  |  |
| `company.export_license_id` | string |  |  |
| `company.export_purpose_code` | string |  |  |
| `company.name` | string |  |  |
| `company.name_kana` | string |  |  |
| `company.name_kanji` | string |  |  |
| `company.owners_provided` | boolean |  |  |
| `company.ownership_declaration` | object |  |  |
| `company.ownership_declaration.date` | timestamp (Unix seconds) |  |  |
| `company.ownership_declaration.ip` | string |  |  |
| `company.ownership_declaration.user_agent` | string |  |  |
| `company.phone` | string |  |  |
| `company.registration_number` | string |  |  |
| `company.structure` | enum: ``, `free_zone_establishment`, `free_zone_llc`, `government_instrumentality`, `governmental_unit`, `incorporated_non_profit`, `incorporated_partnership`, `limited_liability_partnership`, `llc`, `multi_member_llc`, `private_company`, `private_corporation`, `private_partnership`, `public_company`, `public_corporation`, `public_partnership`, `registered_charity`, `single_member_llc`, `sole_establishment`, `sole_proprietorship`, `tax_exempt_government_instrumentality`, `unincorporated_association`, `unincorporated_non_profit`, `unincorporated_partnership` |  |  |
| `company.tax_id` | string |  |  |
| `company.tax_id_registrar` | string |  |  |
| `company.vat_id` | string |  |  |
| `company.verification` | object |  |  |
| `company.verification.document` | object |  |  |
| `company.verification.document.back` | string |  |  |
| `company.verification.document.front` | string |  |  |
| `default_currency` | string |  | Three-letter ISO currency code representing the default currency for the account. This must be a currency that [Stripe supports in the account's country](https://docs.stripe.com/payouts). |
| `documents` | object |  | Documents that may be submitted to satisfy various informational requests. |
| `documents.bank_account_ownership_verification` | object |  |  |
| `documents.bank_account_ownership_verification.files` | array of string |  |  |
| `documents.company_license` | object |  |  |
| `documents.company_license.files` | array of string |  |  |
| `documents.company_memorandum_of_association` | object |  |  |
| `documents.company_memorandum_of_association.files` | array of string |  |  |
| `documents.company_ministerial_decree` | object |  |  |
| `documents.company_ministerial_decree.files` | array of string |  |  |
| `documents.company_registration_verification` | object |  |  |
| `documents.company_registration_verification.files` | array of string |  |  |
| `documents.company_tax_id_verification` | object |  |  |
| `documents.company_tax_id_verification.files` | array of string |  |  |
| `documents.proof_of_registration` | object |  |  |
| `documents.proof_of_registration.files` | array of string |  |  |
| `email` | string |  | The email address of the account holder. This is only to make the account easier to identify to you. Stripe only emails Custom accounts with your consent. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `external_account` | string (open enum) |  | A card or bank account to attach to the account for receiving [payouts](https://docs.stripe.com/connect/bank-debit-card-payouts) (you won’t be able to use it for top-ups). You can provide either a token, like the ones returned by [Stripe.js](https://docs.stripe.com/js), or a dictionary, as documented in the `external_account` parameter for [bank account](https://docs.stripe.com/api#account_create_bank_account) creation. <br>By default, providing an external account sets it as the new default external account for its currency, and deletes the old default if one exists. To add additional external accounts without replacing the existing default for the currency, use the [bank account](https://docs.stripe.com/api#account_create_bank_account) or [card creation](https://docs.stripe.com/api#account_create_card) APIs. After you create an [Account Link](https://docs.stripe.com/api/account_links) or [Account Session](https://docs.stripe.com/api/account_sessions), this property can only be updated for Custom accounts. |
| `individual` | object |  | Information about the person represented by the account. This field is null unless `business_type` is set to `individual`. Once you create an [Account Link](https://docs.stripe.com/api/account_links) or [Account Session](https://docs.stripe.com/api/account_sessions), this property can only be updated for Custom accounts. |
| `individual.address` | object |  |  |
| `individual.address.city` | string |  |  |
| `individual.address.country` | string |  |  |
| `individual.address.line1` | string |  |  |
| `individual.address.line2` | string |  |  |
| `individual.address.postal_code` | string |  |  |
| `individual.address.state` | string |  |  |
| `individual.address_kana` | object |  |  |
| `individual.address_kana.city` | string |  |  |
| `individual.address_kana.country` | string |  |  |
| `individual.address_kana.line1` | string |  |  |
| `individual.address_kana.line2` | string |  |  |
| `individual.address_kana.postal_code` | string |  |  |
| `individual.address_kana.state` | string |  |  |
| `individual.address_kana.town` | string |  |  |
| `individual.address_kanji` | object |  |  |
| `individual.address_kanji.city` | string |  |  |
| `individual.address_kanji.country` | string |  |  |
| `individual.address_kanji.line1` | string |  |  |
| `individual.address_kanji.line2` | string |  |  |
| `individual.address_kanji.postal_code` | string |  |  |
| `individual.address_kanji.state` | string |  |  |
| `individual.address_kanji.town` | string |  |  |
| `individual.dob` | object or "" (to unset) |  |  |
| `individual.dob.day` | integer | yes |  |
| `individual.dob.month` | integer | yes |  |
| `individual.dob.year` | integer | yes |  |
| `individual.email` | string |  |  |
| `individual.first_name` | string |  |  |
| `individual.first_name_kana` | string |  |  |
| `individual.first_name_kanji` | string |  |  |
| `individual.full_name_aliases` | array of string or "" (to unset) |  |  |
| `individual.gender` | string |  |  |
| `individual.id_number` | string |  |  |
| `individual.id_number_secondary` | string |  |  |
| `individual.last_name` | string |  |  |
| `individual.last_name_kana` | string |  |  |
| `individual.last_name_kanji` | string |  |  |
| `individual.maiden_name` | string |  |  |
| `individual.metadata` | map (key → value) or "" (to unset) |  |  |
| `individual.phone` | string |  |  |
| `individual.political_exposure` | enum: `existing`, `none` |  |  |
| `individual.registered_address` | object |  |  |
| `individual.registered_address.city` | string |  |  |
| `individual.registered_address.country` | string |  |  |
| `individual.registered_address.line1` | string |  |  |
| `individual.registered_address.line2` | string |  |  |
| `individual.registered_address.postal_code` | string |  |  |
| `individual.registered_address.state` | string |  |  |
| `individual.relationship` | object |  |  |
| `individual.relationship.director` | boolean |  |  |
| `individual.relationship.executive` | boolean |  |  |
| `individual.relationship.owner` | boolean |  |  |
| `individual.relationship.percent_ownership` | number or "" (to unset) |  |  |
| `individual.relationship.title` | string |  |  |
| `individual.ssn_last_4` | string |  |  |
| `individual.verification` | object |  |  |
| `individual.verification.additional_document` | object |  |  |
| `individual.verification.additional_document.back` | string |  |  |
| `individual.verification.additional_document.front` | string |  |  |
| `individual.verification.document` | object |  |  |
| `individual.verification.document.back` | string |  |  |
| `individual.verification.document.front` | string |  |  |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `settings` | object |  | Options for customizing how the account functions within Stripe. |
| `settings.bacs_debit_payments` | object |  |  |
| `settings.bacs_debit_payments.display_name` | string |  |  |
| `settings.branding` | object |  |  |
| `settings.branding.icon` | string |  |  |
| `settings.branding.logo` | string |  |  |
| `settings.branding.primary_color` | string |  |  |
| `settings.branding.secondary_color` | string |  |  |
| `settings.card_issuing` | object |  |  |
| `settings.card_issuing.tos_acceptance` | object |  |  |
| `settings.card_issuing.tos_acceptance.date` | timestamp (Unix seconds) |  |  |
| `settings.card_issuing.tos_acceptance.ip` | string |  |  |
| `settings.card_issuing.tos_acceptance.user_agent` | string or "" (to unset) |  |  |
| `settings.card_payments` | object |  |  |
| `settings.card_payments.decline_on` | object |  |  |
| `settings.card_payments.decline_on.avs_failure` | boolean |  |  |
| `settings.card_payments.decline_on.cvc_failure` | boolean |  |  |
| `settings.card_payments.statement_descriptor_prefix` | string |  |  |
| `settings.card_payments.statement_descriptor_prefix_kana` | string or "" (to unset) |  |  |
| `settings.card_payments.statement_descriptor_prefix_kanji` | string or "" (to unset) |  |  |
| `settings.invoices` | object |  |  |
| `settings.invoices.default_account_tax_ids` | array of string or "" (to unset) |  |  |
| `settings.payments` | object |  |  |
| `settings.payments.statement_descriptor` | string |  |  |
| `settings.payments.statement_descriptor_kana` | string |  |  |
| `settings.payments.statement_descriptor_kanji` | string |  |  |
| `settings.payouts` | object |  |  |
| `settings.payouts.debit_negative_balances` | boolean |  |  |
| `settings.payouts.schedule` | object |  |  |
| `settings.payouts.schedule.delay_days` | enum: `minimum` or integer |  |  |
| `settings.payouts.schedule.interval` | enum: `daily`, `manual`, `monthly`, `weekly` |  |  |
| `settings.payouts.schedule.monthly_anchor` | integer |  |  |
| `settings.payouts.schedule.weekly_anchor` | enum: `friday`, `monday`, `saturday`, `sunday`, `thursday`, `tuesday`, `wednesday` |  |  |
| `settings.payouts.statement_descriptor` | string |  |  |
| `settings.treasury` | object |  |  |
| `settings.treasury.tos_acceptance` | object |  |  |
| `settings.treasury.tos_acceptance.date` | timestamp (Unix seconds) |  |  |
| `settings.treasury.tos_acceptance.ip` | string |  |  |
| `settings.treasury.tos_acceptance.user_agent` | string or "" (to unset) |  |  |
| `tos_acceptance` | object |  | Details on the account's acceptance of the [Stripe Services Agreement](https://docs.stripe.com/connect/updating-accounts#tos-acceptance) This property can only be updated for Custom accounts. |
| `tos_acceptance.date` | timestamp (Unix seconds) |  |  |
| `tos_acceptance.ip` | string |  |  |
| `tos_acceptance.service_agreement` | string |  |  |
| `tos_acceptance.user_agent` | string |  |  |

Returns: `account`

## DELETE /v1/accounts/{account}

operationId: `DeleteAccountsAccount`

With [Connect](https://stripe.com/docs/connect), you can delete accounts you manage.

Accounts created using test-mode keys can be deleted at any time. Standard accounts created using live-mode keys cannot be deleted. Custom or Express accounts created using live-mode keys can only be deleted once all balances are zero.

If you want to delete your own account, use the [account information tab in your account settings](https://dashboard.stripe.com/settings/account) instead.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account (path)` | string | yes |  |

Returns: `deleted_account`

## POST /v1/accounts/{account}/bank_accounts

operationId: `PostAccountsAccountBankAccounts`

Create an external account for a given account.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account (path)` | string | yes |  |
| `bank_account` | object or string |  | Either a token, like the ones returned by [Stripe.js](https://stripe.com/docs/js), or a dictionary containing a user's bank account details. |
| `bank_account.account_holder_name` | string |  |  |
| `bank_account.account_holder_type` | enum: `company`, `individual` |  |  |
| `bank_account.account_number` | string | yes |  |
| `bank_account.account_type` | enum: `checking`, `futsu`, `savings`, `toza` |  |  |
| `bank_account.country` | string | yes |  |
| `bank_account.currency` | string |  |  |
| `bank_account.documents` | object |  |  |
| `bank_account.documents.bank_account_ownership_verification` | object |  |  |
| `bank_account.documents.bank_account_ownership_verification.files` | array of string |  |  |
| `bank_account.object` | enum: `bank_account` |  |  |
| `bank_account.routing_number` | string |  |  |
| `default_for_currency` | boolean |  | When set to true, or if this is the first external account added in this currency, this account becomes the default external account for its currency. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `external_account` | string (open enum) |  | Please refer to full [documentation](https://stripe.com/docs/api) instead. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |

Returns: `external_account`

## GET /v1/accounts/{account}/bank_accounts/{id}

operationId: `GetAccountsAccountBankAccountsId`

Retrieve a specified external account for a given account.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `id (path)` | string | yes |  |

Returns: `external_account`

## POST /v1/accounts/{account}/bank_accounts/{id}

operationId: `PostAccountsAccountBankAccountsId`

Updates the metadata, account holder name, account holder type of a bank account belonging to a [Custom account](https://stripe.com/docs/connect/custom-accounts), and optionally sets it as the default for its currency. Other bank account details are not editable by design.

You can re-enable a disabled bank account by performing an update call without providing any arguments or changes.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account (path)` | string | yes |  |
| `id (path)` | string | yes |  |
| `account_holder_name` | string |  | The name of the person or business that owns the bank account. |
| `account_holder_type` | enum: ``, `company`, `individual` |  | The type of entity that holds the account. This can be either `individual` or `company`. |
| `account_type` | enum: `checking`, `futsu`, `savings`, `toza` |  | The bank account type. This can only be `checking` or `savings` in most countries. In Japan, this can only be `futsu` or `toza`. |
| `address_city` | string |  | City/District/Suburb/Town/Village. |
| `address_country` | string |  | Billing address country, if provided when creating card. |
| `address_line1` | string |  | Address line 1 (Street address/PO Box/Company name). |
| `address_line2` | string |  | Address line 2 (Apartment/Suite/Unit/Building). |
| `address_state` | string |  | State/County/Province/Region. |
| `address_zip` | string |  | ZIP or postal code. |
| `default_for_currency` | boolean |  | When set to true, this becomes the default external account for its currency. |
| `documents` | object |  | Documents that may be submitted to satisfy various informational requests. |
| `documents.bank_account_ownership_verification` | object |  |  |
| `documents.bank_account_ownership_verification.files` | array of string |  |  |
| `exp_month` | string |  | Two digit number representing the card’s expiration month. |
| `exp_year` | string |  | Four digit number representing the card’s expiration year. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `name` | string |  | Cardholder name. |

Returns: `external_account`

## DELETE /v1/accounts/{account}/bank_accounts/{id}

operationId: `DeleteAccountsAccountBankAccountsId`

Delete a specified external account for a given account.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account (path)` | string | yes |  |
| `id (path)` | string | yes |  |

Returns: `deleted_external_account`

## GET /v1/accounts/{account}/capabilities

operationId: `GetAccountsAccountCapabilities`

Returns a list of capabilities associated with the account. The capabilities are returned sorted by creation date, with the most recent capability appearing first.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: object

## GET /v1/accounts/{account}/capabilities/{capability}

operationId: `GetAccountsAccountCapabilitiesCapability`

Retrieves information about the specified Account Capability.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account (path)` | string | yes |  |
| `capability (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `capability`

## POST /v1/accounts/{account}/capabilities/{capability}

operationId: `PostAccountsAccountCapabilitiesCapability`

Updates an existing Account Capability. Request or remove a capability by updating its `requested` parameter.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account (path)` | string | yes |  |
| `capability (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `requested` | boolean |  | To request a new capability for an account, pass true. There can be a delay before the requested capability becomes active. If the capability has any activation requirements, the response includes them in the `requirements` arrays.<br>If a capability isn't permanent, you can remove it from the account by passing false. Most capabilities are permanent after they've been requested. Attempting to remove a permanent capability returns an error. |

Returns: `capability`

## GET /v1/accounts/{account}/external_accounts

operationId: `GetAccountsAccountExternalAccounts`

List external accounts for an account.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account (path)` | string | yes |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `object` | enum: `bank_account`, `card` |  | Filter external accounts according to a particular object type. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/accounts/{account}/external_accounts

operationId: `PostAccountsAccountExternalAccounts`

Create an external account for a given account.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account (path)` | string | yes |  |
| `bank_account` | object or string |  | Either a token, like the ones returned by [Stripe.js](https://stripe.com/docs/js), or a dictionary containing a user's bank account details. |
| `bank_account.account_holder_name` | string |  |  |
| `bank_account.account_holder_type` | enum: `company`, `individual` |  |  |
| `bank_account.account_number` | string | yes |  |
| `bank_account.account_type` | enum: `checking`, `futsu`, `savings`, `toza` |  |  |
| `bank_account.country` | string | yes |  |
| `bank_account.currency` | string |  |  |
| `bank_account.documents` | object |  |  |
| `bank_account.documents.bank_account_ownership_verification` | object |  |  |
| `bank_account.documents.bank_account_ownership_verification.files` | array of string |  |  |
| `bank_account.object` | enum: `bank_account` |  |  |
| `bank_account.routing_number` | string |  |  |
| `default_for_currency` | boolean |  | When set to true, or if this is the first external account added in this currency, this account becomes the default external account for its currency. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `external_account` | string (open enum) |  | Please refer to full [documentation](https://stripe.com/docs/api) instead. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |

Returns: `external_account`

## GET /v1/accounts/{account}/external_accounts/{id}

operationId: `GetAccountsAccountExternalAccountsId`

Retrieve a specified external account for a given account.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `id (path)` | string | yes |  |

Returns: `external_account`

## POST /v1/accounts/{account}/external_accounts/{id}

operationId: `PostAccountsAccountExternalAccountsId`

Updates the metadata, account holder name, account holder type of a bank account belonging to a [Custom account](https://stripe.com/docs/connect/custom-accounts), and optionally sets it as the default for its currency. Other bank account details are not editable by design.

You can re-enable a disabled bank account by performing an update call without providing any arguments or changes.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account (path)` | string | yes |  |
| `id (path)` | string | yes |  |
| `account_holder_name` | string |  | The name of the person or business that owns the bank account. |
| `account_holder_type` | enum: ``, `company`, `individual` |  | The type of entity that holds the account. This can be either `individual` or `company`. |
| `account_type` | enum: `checking`, `futsu`, `savings`, `toza` |  | The bank account type. This can only be `checking` or `savings` in most countries. In Japan, this can only be `futsu` or `toza`. |
| `address_city` | string |  | City/District/Suburb/Town/Village. |
| `address_country` | string |  | Billing address country, if provided when creating card. |
| `address_line1` | string |  | Address line 1 (Street address/PO Box/Company name). |
| `address_line2` | string |  | Address line 2 (Apartment/Suite/Unit/Building). |
| `address_state` | string |  | State/County/Province/Region. |
| `address_zip` | string |  | ZIP or postal code. |
| `default_for_currency` | boolean |  | When set to true, this becomes the default external account for its currency. |
| `documents` | object |  | Documents that may be submitted to satisfy various informational requests. |
| `documents.bank_account_ownership_verification` | object |  |  |
| `documents.bank_account_ownership_verification.files` | array of string |  |  |
| `exp_month` | string |  | Two digit number representing the card’s expiration month. |
| `exp_year` | string |  | Four digit number representing the card’s expiration year. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `name` | string |  | Cardholder name. |

Returns: `external_account`

## DELETE /v1/accounts/{account}/external_accounts/{id}

operationId: `DeleteAccountsAccountExternalAccountsId`

Delete a specified external account for a given account.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account (path)` | string | yes |  |
| `id (path)` | string | yes |  |

Returns: `deleted_external_account`

## POST /v1/accounts/{account}/login_links

operationId: `PostAccountsAccountLoginLinks`

Creates a single-use login link for an Express account to access their Stripe dashboard.

**You may only create login links for [Express accounts](https://stripe.com/docs/connect/express-accounts) connected to your platform**.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `login_link`

## GET /v1/accounts/{account}/people

operationId: `GetAccountsAccountPeople`

Returns a list of people associated with the account’s legal entity. The people are returned sorted by creation date, with the most recent people appearing first.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account (path)` | string | yes |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `relationship` | object |  | Filters on the list of people returned based on the person's relationship to the account's company. |
| `relationship.director` | boolean |  |  |
| `relationship.executive` | boolean |  |  |
| `relationship.legal_guardian` | boolean |  |  |
| `relationship.owner` | boolean |  |  |
| `relationship.representative` | boolean |  |  |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/accounts/{account}/people

operationId: `PostAccountsAccountPeople`

Creates a new person.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account (path)` | string | yes |  |
| `additional_tos_acceptances` | object |  | Details on the legal guardian's acceptance of the required Stripe agreements. |
| `additional_tos_acceptances.account` | object |  |  |
| `additional_tos_acceptances.account.date` | timestamp (Unix seconds) |  |  |
| `additional_tos_acceptances.account.ip` | string |  |  |
| `additional_tos_acceptances.account.user_agent` | string or "" (to unset) |  |  |
| `address` | object |  | The person's address. |
| `address.city` | string |  |  |
| `address.country` | string |  |  |
| `address.line1` | string |  |  |
| `address.line2` | string |  |  |
| `address.postal_code` | string |  |  |
| `address.state` | string |  |  |
| `address_kana` | object |  | The Kana variation of the person's address (Japan only). |
| `address_kana.city` | string |  |  |
| `address_kana.country` | string |  |  |
| `address_kana.line1` | string |  |  |
| `address_kana.line2` | string |  |  |
| `address_kana.postal_code` | string |  |  |
| `address_kana.state` | string |  |  |
| `address_kana.town` | string |  |  |
| `address_kanji` | object |  | The Kanji variation of the person's address (Japan only). |
| `address_kanji.city` | string |  |  |
| `address_kanji.country` | string |  |  |
| `address_kanji.line1` | string |  |  |
| `address_kanji.line2` | string |  |  |
| `address_kanji.postal_code` | string |  |  |
| `address_kanji.state` | string |  |  |
| `address_kanji.town` | string |  |  |
| `dob` | object or "" (to unset) |  | The person's date of birth. |
| `dob.day` | integer | yes |  |
| `dob.month` | integer | yes |  |
| `dob.year` | integer | yes |  |
| `documents` | object |  | Documents that may be submitted to satisfy various informational requests. |
| `documents.company_authorization` | object |  |  |
| `documents.company_authorization.files` | array of string or "" (to unset) |  |  |
| `documents.passport` | object |  |  |
| `documents.passport.files` | array of string or "" (to unset) |  |  |
| `documents.visa` | object |  |  |
| `documents.visa.files` | array of string or "" (to unset) |  |  |
| `email` | string |  | The person's email address. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `first_name` | string |  | The person's first name. |
| `first_name_kana` | string |  | The Kana variation of the person's first name (Japan only). |
| `first_name_kanji` | string |  | The Kanji variation of the person's first name (Japan only). |
| `full_name_aliases` | array of string or "" (to unset) |  | A list of alternate names or aliases that the person is known by. |
| `gender` | string |  | The person's gender (International regulations require either "male" or "female"). |
| `id_number` | string |  | The person's ID number, as appropriate for their country. For example, a social security number in the U.S., social insurance number in Canada, etc. Instead of the number itself, you can also provide a [PII token provided by Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii). |
| `id_number_secondary` | string |  | The person's secondary ID number, as appropriate for their country, will be used for enhanced verification checks. In Thailand, this would be the laser code found on the back of an ID card. Instead of the number itself, you can also provide a [PII token provided by Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii). |
| `last_name` | string |  | The person's last name. |
| `last_name_kana` | string |  | The Kana variation of the person's last name (Japan only). |
| `last_name_kanji` | string |  | The Kanji variation of the person's last name (Japan only). |
| `maiden_name` | string |  | The person's maiden name. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `nationality` | string |  | The country where the person is a national. Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)), or "XX" if unavailable. |
| `person_token` | string |  | A [person token](https://docs.stripe.com/connect/account-tokens), used to securely provide details to the person. |
| `phone` | string |  | The person's phone number. |
| `political_exposure` | string |  | Indicates if the person or any of their representatives, family members, or other closely related persons, declares that they hold or have held an important public job or function, in any jurisdiction. |
| `registered_address` | object |  | The person's registered address. |
| `registered_address.city` | string |  |  |
| `registered_address.country` | string |  |  |
| `registered_address.line1` | string |  |  |
| `registered_address.line2` | string |  |  |
| `registered_address.postal_code` | string |  |  |
| `registered_address.state` | string |  |  |
| `relationship` | object |  | The relationship that this person has with the account's legal entity. |
| `relationship.director` | boolean |  |  |
| `relationship.executive` | boolean |  |  |
| `relationship.legal_guardian` | boolean |  |  |
| `relationship.owner` | boolean |  |  |
| `relationship.percent_ownership` | number or "" (to unset) |  |  |
| `relationship.representative` | boolean |  |  |
| `relationship.title` | string |  |  |
| `ssn_last_4` | string |  | The last four digits of the person's Social Security number (U.S. only). |
| `verification` | object |  | The person's verification status. |
| `verification.additional_document` | object |  |  |
| `verification.additional_document.back` | string |  |  |
| `verification.additional_document.front` | string |  |  |
| `verification.document` | object |  |  |
| `verification.document.back` | string |  |  |
| `verification.document.front` | string |  |  |

Returns: `person`

## GET /v1/accounts/{account}/people/{person}

operationId: `GetAccountsAccountPeoplePerson`

Retrieves an existing person.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `person (path)` | string | yes |  |

Returns: `person`

## POST /v1/accounts/{account}/people/{person}

operationId: `PostAccountsAccountPeoplePerson`

Updates an existing person.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account (path)` | string | yes |  |
| `person (path)` | string | yes |  |
| `additional_tos_acceptances` | object |  | Details on the legal guardian's acceptance of the required Stripe agreements. |
| `additional_tos_acceptances.account` | object |  |  |
| `additional_tos_acceptances.account.date` | timestamp (Unix seconds) |  |  |
| `additional_tos_acceptances.account.ip` | string |  |  |
| `additional_tos_acceptances.account.user_agent` | string or "" (to unset) |  |  |
| `address` | object |  | The person's address. |
| `address.city` | string |  |  |
| `address.country` | string |  |  |
| `address.line1` | string |  |  |
| `address.line2` | string |  |  |
| `address.postal_code` | string |  |  |
| `address.state` | string |  |  |
| `address_kana` | object |  | The Kana variation of the person's address (Japan only). |
| `address_kana.city` | string |  |  |
| `address_kana.country` | string |  |  |
| `address_kana.line1` | string |  |  |
| `address_kana.line2` | string |  |  |
| `address_kana.postal_code` | string |  |  |
| `address_kana.state` | string |  |  |
| `address_kana.town` | string |  |  |
| `address_kanji` | object |  | The Kanji variation of the person's address (Japan only). |
| `address_kanji.city` | string |  |  |
| `address_kanji.country` | string |  |  |
| `address_kanji.line1` | string |  |  |
| `address_kanji.line2` | string |  |  |
| `address_kanji.postal_code` | string |  |  |
| `address_kanji.state` | string |  |  |
| `address_kanji.town` | string |  |  |
| `dob` | object or "" (to unset) |  | The person's date of birth. |
| `dob.day` | integer | yes |  |
| `dob.month` | integer | yes |  |
| `dob.year` | integer | yes |  |
| `documents` | object |  | Documents that may be submitted to satisfy various informational requests. |
| `documents.company_authorization` | object |  |  |
| `documents.company_authorization.files` | array of string or "" (to unset) |  |  |
| `documents.passport` | object |  |  |
| `documents.passport.files` | array of string or "" (to unset) |  |  |
| `documents.visa` | object |  |  |
| `documents.visa.files` | array of string or "" (to unset) |  |  |
| `email` | string |  | The person's email address. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `first_name` | string |  | The person's first name. |
| `first_name_kana` | string |  | The Kana variation of the person's first name (Japan only). |
| `first_name_kanji` | string |  | The Kanji variation of the person's first name (Japan only). |
| `full_name_aliases` | array of string or "" (to unset) |  | A list of alternate names or aliases that the person is known by. |
| `gender` | string |  | The person's gender (International regulations require either "male" or "female"). |
| `id_number` | string |  | The person's ID number, as appropriate for their country. For example, a social security number in the U.S., social insurance number in Canada, etc. Instead of the number itself, you can also provide a [PII token provided by Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii). |
| `id_number_secondary` | string |  | The person's secondary ID number, as appropriate for their country, will be used for enhanced verification checks. In Thailand, this would be the laser code found on the back of an ID card. Instead of the number itself, you can also provide a [PII token provided by Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii). |
| `last_name` | string |  | The person's last name. |
| `last_name_kana` | string |  | The Kana variation of the person's last name (Japan only). |
| `last_name_kanji` | string |  | The Kanji variation of the person's last name (Japan only). |
| `maiden_name` | string |  | The person's maiden name. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `nationality` | string |  | The country where the person is a national. Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)), or "XX" if unavailable. |
| `person_token` | string |  | A [person token](https://docs.stripe.com/connect/account-tokens), used to securely provide details to the person. |
| `phone` | string |  | The person's phone number. |
| `political_exposure` | string |  | Indicates if the person or any of their representatives, family members, or other closely related persons, declares that they hold or have held an important public job or function, in any jurisdiction. |
| `registered_address` | object |  | The person's registered address. |
| `registered_address.city` | string |  |  |
| `registered_address.country` | string |  |  |
| `registered_address.line1` | string |  |  |
| `registered_address.line2` | string |  |  |
| `registered_address.postal_code` | string |  |  |
| `registered_address.state` | string |  |  |
| `relationship` | object |  | The relationship that this person has with the account's legal entity. |
| `relationship.director` | boolean |  |  |
| `relationship.executive` | boolean |  |  |
| `relationship.legal_guardian` | boolean |  |  |
| `relationship.owner` | boolean |  |  |
| `relationship.percent_ownership` | number or "" (to unset) |  |  |
| `relationship.representative` | boolean |  |  |
| `relationship.title` | string |  |  |
| `ssn_last_4` | string |  | The last four digits of the person's Social Security number (U.S. only). |
| `verification` | object |  | The person's verification status. |
| `verification.additional_document` | object |  |  |
| `verification.additional_document.back` | string |  |  |
| `verification.additional_document.front` | string |  |  |
| `verification.document` | object |  |  |
| `verification.document.back` | string |  |  |
| `verification.document.front` | string |  |  |

Returns: `person`

## DELETE /v1/accounts/{account}/people/{person}

operationId: `DeleteAccountsAccountPeoplePerson`

Deletes an existing person’s relationship to the account’s legal entity. Any person with a relationship for an account can be deleted through the API, except if the person is the `account_opener`. If your integration is using the `executive` parameter, you cannot delete the only verified `executive` on file.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account (path)` | string | yes |  |
| `person (path)` | string | yes |  |

Returns: `deleted_person`

## GET /v1/accounts/{account}/persons

operationId: `GetAccountsAccountPersons`

Returns a list of people associated with the account’s legal entity. The people are returned sorted by creation date, with the most recent people appearing first.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account (path)` | string | yes |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `relationship` | object |  | Filters on the list of people returned based on the person's relationship to the account's company. |
| `relationship.director` | boolean |  |  |
| `relationship.executive` | boolean |  |  |
| `relationship.legal_guardian` | boolean |  |  |
| `relationship.owner` | boolean |  |  |
| `relationship.representative` | boolean |  |  |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/accounts/{account}/persons

operationId: `PostAccountsAccountPersons`

Creates a new person.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account (path)` | string | yes |  |
| `additional_tos_acceptances` | object |  | Details on the legal guardian's acceptance of the required Stripe agreements. |
| `additional_tos_acceptances.account` | object |  |  |
| `additional_tos_acceptances.account.date` | timestamp (Unix seconds) |  |  |
| `additional_tos_acceptances.account.ip` | string |  |  |
| `additional_tos_acceptances.account.user_agent` | string or "" (to unset) |  |  |
| `address` | object |  | The person's address. |
| `address.city` | string |  |  |
| `address.country` | string |  |  |
| `address.line1` | string |  |  |
| `address.line2` | string |  |  |
| `address.postal_code` | string |  |  |
| `address.state` | string |  |  |
| `address_kana` | object |  | The Kana variation of the person's address (Japan only). |
| `address_kana.city` | string |  |  |
| `address_kana.country` | string |  |  |
| `address_kana.line1` | string |  |  |
| `address_kana.line2` | string |  |  |
| `address_kana.postal_code` | string |  |  |
| `address_kana.state` | string |  |  |
| `address_kana.town` | string |  |  |
| `address_kanji` | object |  | The Kanji variation of the person's address (Japan only). |
| `address_kanji.city` | string |  |  |
| `address_kanji.country` | string |  |  |
| `address_kanji.line1` | string |  |  |
| `address_kanji.line2` | string |  |  |
| `address_kanji.postal_code` | string |  |  |
| `address_kanji.state` | string |  |  |
| `address_kanji.town` | string |  |  |
| `dob` | object or "" (to unset) |  | The person's date of birth. |
| `dob.day` | integer | yes |  |
| `dob.month` | integer | yes |  |
| `dob.year` | integer | yes |  |
| `documents` | object |  | Documents that may be submitted to satisfy various informational requests. |
| `documents.company_authorization` | object |  |  |
| `documents.company_authorization.files` | array of string or "" (to unset) |  |  |
| `documents.passport` | object |  |  |
| `documents.passport.files` | array of string or "" (to unset) |  |  |
| `documents.visa` | object |  |  |
| `documents.visa.files` | array of string or "" (to unset) |  |  |
| `email` | string |  | The person's email address. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `first_name` | string |  | The person's first name. |
| `first_name_kana` | string |  | The Kana variation of the person's first name (Japan only). |
| `first_name_kanji` | string |  | The Kanji variation of the person's first name (Japan only). |
| `full_name_aliases` | array of string or "" (to unset) |  | A list of alternate names or aliases that the person is known by. |
| `gender` | string |  | The person's gender (International regulations require either "male" or "female"). |
| `id_number` | string |  | The person's ID number, as appropriate for their country. For example, a social security number in the U.S., social insurance number in Canada, etc. Instead of the number itself, you can also provide a [PII token provided by Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii). |
| `id_number_secondary` | string |  | The person's secondary ID number, as appropriate for their country, will be used for enhanced verification checks. In Thailand, this would be the laser code found on the back of an ID card. Instead of the number itself, you can also provide a [PII token provided by Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii). |
| `last_name` | string |  | The person's last name. |
| `last_name_kana` | string |  | The Kana variation of the person's last name (Japan only). |
| `last_name_kanji` | string |  | The Kanji variation of the person's last name (Japan only). |
| `maiden_name` | string |  | The person's maiden name. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `nationality` | string |  | The country where the person is a national. Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)), or "XX" if unavailable. |
| `person_token` | string |  | A [person token](https://docs.stripe.com/connect/account-tokens), used to securely provide details to the person. |
| `phone` | string |  | The person's phone number. |
| `political_exposure` | string |  | Indicates if the person or any of their representatives, family members, or other closely related persons, declares that they hold or have held an important public job or function, in any jurisdiction. |
| `registered_address` | object |  | The person's registered address. |
| `registered_address.city` | string |  |  |
| `registered_address.country` | string |  |  |
| `registered_address.line1` | string |  |  |
| `registered_address.line2` | string |  |  |
| `registered_address.postal_code` | string |  |  |
| `registered_address.state` | string |  |  |
| `relationship` | object |  | The relationship that this person has with the account's legal entity. |
| `relationship.director` | boolean |  |  |
| `relationship.executive` | boolean |  |  |
| `relationship.legal_guardian` | boolean |  |  |
| `relationship.owner` | boolean |  |  |
| `relationship.percent_ownership` | number or "" (to unset) |  |  |
| `relationship.representative` | boolean |  |  |
| `relationship.title` | string |  |  |
| `ssn_last_4` | string |  | The last four digits of the person's Social Security number (U.S. only). |
| `verification` | object |  | The person's verification status. |
| `verification.additional_document` | object |  |  |
| `verification.additional_document.back` | string |  |  |
| `verification.additional_document.front` | string |  |  |
| `verification.document` | object |  |  |
| `verification.document.back` | string |  |  |
| `verification.document.front` | string |  |  |

Returns: `person`

## GET /v1/accounts/{account}/persons/{person}

operationId: `GetAccountsAccountPersonsPerson`

Retrieves an existing person.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `person (path)` | string | yes |  |

Returns: `person`

## POST /v1/accounts/{account}/persons/{person}

operationId: `PostAccountsAccountPersonsPerson`

Updates an existing person.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account (path)` | string | yes |  |
| `person (path)` | string | yes |  |
| `additional_tos_acceptances` | object |  | Details on the legal guardian's acceptance of the required Stripe agreements. |
| `additional_tos_acceptances.account` | object |  |  |
| `additional_tos_acceptances.account.date` | timestamp (Unix seconds) |  |  |
| `additional_tos_acceptances.account.ip` | string |  |  |
| `additional_tos_acceptances.account.user_agent` | string or "" (to unset) |  |  |
| `address` | object |  | The person's address. |
| `address.city` | string |  |  |
| `address.country` | string |  |  |
| `address.line1` | string |  |  |
| `address.line2` | string |  |  |
| `address.postal_code` | string |  |  |
| `address.state` | string |  |  |
| `address_kana` | object |  | The Kana variation of the person's address (Japan only). |
| `address_kana.city` | string |  |  |
| `address_kana.country` | string |  |  |
| `address_kana.line1` | string |  |  |
| `address_kana.line2` | string |  |  |
| `address_kana.postal_code` | string |  |  |
| `address_kana.state` | string |  |  |
| `address_kana.town` | string |  |  |
| `address_kanji` | object |  | The Kanji variation of the person's address (Japan only). |
| `address_kanji.city` | string |  |  |
| `address_kanji.country` | string |  |  |
| `address_kanji.line1` | string |  |  |
| `address_kanji.line2` | string |  |  |
| `address_kanji.postal_code` | string |  |  |
| `address_kanji.state` | string |  |  |
| `address_kanji.town` | string |  |  |
| `dob` | object or "" (to unset) |  | The person's date of birth. |
| `dob.day` | integer | yes |  |
| `dob.month` | integer | yes |  |
| `dob.year` | integer | yes |  |
| `documents` | object |  | Documents that may be submitted to satisfy various informational requests. |
| `documents.company_authorization` | object |  |  |
| `documents.company_authorization.files` | array of string or "" (to unset) |  |  |
| `documents.passport` | object |  |  |
| `documents.passport.files` | array of string or "" (to unset) |  |  |
| `documents.visa` | object |  |  |
| `documents.visa.files` | array of string or "" (to unset) |  |  |
| `email` | string |  | The person's email address. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `first_name` | string |  | The person's first name. |
| `first_name_kana` | string |  | The Kana variation of the person's first name (Japan only). |
| `first_name_kanji` | string |  | The Kanji variation of the person's first name (Japan only). |
| `full_name_aliases` | array of string or "" (to unset) |  | A list of alternate names or aliases that the person is known by. |
| `gender` | string |  | The person's gender (International regulations require either "male" or "female"). |
| `id_number` | string |  | The person's ID number, as appropriate for their country. For example, a social security number in the U.S., social insurance number in Canada, etc. Instead of the number itself, you can also provide a [PII token provided by Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii). |
| `id_number_secondary` | string |  | The person's secondary ID number, as appropriate for their country, will be used for enhanced verification checks. In Thailand, this would be the laser code found on the back of an ID card. Instead of the number itself, you can also provide a [PII token provided by Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii). |
| `last_name` | string |  | The person's last name. |
| `last_name_kana` | string |  | The Kana variation of the person's last name (Japan only). |
| `last_name_kanji` | string |  | The Kanji variation of the person's last name (Japan only). |
| `maiden_name` | string |  | The person's maiden name. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `nationality` | string |  | The country where the person is a national. Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)), or "XX" if unavailable. |
| `person_token` | string |  | A [person token](https://docs.stripe.com/connect/account-tokens), used to securely provide details to the person. |
| `phone` | string |  | The person's phone number. |
| `political_exposure` | string |  | Indicates if the person or any of their representatives, family members, or other closely related persons, declares that they hold or have held an important public job or function, in any jurisdiction. |
| `registered_address` | object |  | The person's registered address. |
| `registered_address.city` | string |  |  |
| `registered_address.country` | string |  |  |
| `registered_address.line1` | string |  |  |
| `registered_address.line2` | string |  |  |
| `registered_address.postal_code` | string |  |  |
| `registered_address.state` | string |  |  |
| `relationship` | object |  | The relationship that this person has with the account's legal entity. |
| `relationship.director` | boolean |  |  |
| `relationship.executive` | boolean |  |  |
| `relationship.legal_guardian` | boolean |  |  |
| `relationship.owner` | boolean |  |  |
| `relationship.percent_ownership` | number or "" (to unset) |  |  |
| `relationship.representative` | boolean |  |  |
| `relationship.title` | string |  |  |
| `ssn_last_4` | string |  | The last four digits of the person's Social Security number (U.S. only). |
| `verification` | object |  | The person's verification status. |
| `verification.additional_document` | object |  |  |
| `verification.additional_document.back` | string |  |  |
| `verification.additional_document.front` | string |  |  |
| `verification.document` | object |  |  |
| `verification.document.back` | string |  |  |
| `verification.document.front` | string |  |  |

Returns: `person`

## DELETE /v1/accounts/{account}/persons/{person}

operationId: `DeleteAccountsAccountPersonsPerson`

Deletes an existing person’s relationship to the account’s legal entity. Any person with a relationship for an account can be deleted through the API, except if the person is the `account_opener`. If your integration is using the `executive` parameter, you cannot delete the only verified `executive` on file.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account (path)` | string | yes |  |
| `person (path)` | string | yes |  |

Returns: `deleted_person`

## POST /v1/accounts/{account}/reject

operationId: `PostAccountsAccountReject`

With [Connect](https://stripe.com/docs/connect), you may flag accounts as suspicious.

Test-mode Custom and Express accounts can be rejected at any time. Accounts created using live-mode keys may only be rejected once all balances are zero.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `account (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `reason` | string | yes | The reason for rejecting the account. Can be `fraud`, `terms_of_service`, or `other`. |

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

## The `deleted_account` object

| Field | Type | Required | Description |
|---|---|---|---|
| `deleted` | enum: `True` | yes | Always true for a deleted object |
| `id` | string | yes | Unique identifier for the object. |
| `object` | enum: `account` | yes | String representing the object's type. Objects of the same type share the same value. |

## The `external_account` object

Type: `bank_account` or `card`

## The `deleted_external_account` object

Type: `deleted_bank_account` or `deleted_card`

## The `capability` object

This is an object representing a capability for a Stripe account.

Related guide: [Account capabilities](https://stripe.com/docs/connect/account-capabilities)

Expandable fields (pass `expand[]=<field>`): `account`, `future_requirements`, `requirements`

| Field | Type | Required | Description |
|---|---|---|---|
| `account` | string or `account` | yes | The account for which the capability enables functionality. |
| `future_requirements` | `account_capability_future_requirements` |  |  |
| `id` | string | yes | The identifier for the capability. |
| `object` | enum: `capability` | yes | String representing the object's type. Objects of the same type share the same value. |
| `requested` | boolean | yes | Whether the capability has been requested. |
| `requested_at` | timestamp (Unix seconds) |  | Time at which the capability was requested. Measured in seconds since the Unix epoch. |
| `requirements` | `account_capability_requirements` |  |  |
| `status` | enum: `active`, `disabled`, `inactive`, `pending`, `unrequested` | yes | The status of the capability. Can be `active`, `inactive`, `pending`, or `unrequested`. |

## The `login_link` object

Login Links are single-use login link for an Express account to access their Stripe dashboard.

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `object` | enum: `login_link` | yes | String representing the object's type. Objects of the same type share the same value. |
| `url` | string | yes | The URL for the login link. |

## The `person` object

This is an object representing a person associated with a Stripe account.

A platform cannot access a Standard or Express account's persons after the account starts onboarding, such as after generating an account link for the account.
See the [Standard onboarding](https://stripe.com/docs/connect/standard-accounts) or [Express onboarding documentation](https://stripe.com/docs/connect/express-accounts) for information about platform prefilling and account onboarding steps.

Related guide: [Handling identity verification with the API](https://stripe.com/docs/connect/handling-api-verification#person-information)

Expandable fields (pass `expand[]=<field>`): `additional_tos_acceptances`, `address`, `address_kana`, `address_kanji`, `dob`, `future_requirements`, `registered_address`, `relationship`, `requirements`, `verification`

| Field | Type | Required | Description |
|---|---|---|---|
| `account` | string | yes | The account the person is associated with. |
| `additional_tos_acceptances` | `person_additional_tos_acceptances` |  |  |
| `address` | `address` |  |  |
| `address_kana` | `legal_entity_japan_address` |  |  |
| `address_kanji` | `legal_entity_japan_address` |  |  |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `dob` | `legal_entity_dob` |  |  |
| `email` | string |  | The person's email address. |
| `first_name` | string |  | The person's first name. |
| `first_name_kana` | string |  | The Kana variation of the person's first name (Japan only). |
| `first_name_kanji` | string |  | The Kanji variation of the person's first name (Japan only). |
| `full_name_aliases` | array of string |  | A list of alternate names or aliases that the person is known by. |
| `future_requirements` | `person_future_requirements` |  |  |
| `gender` | string |  | The person's gender (International regulations require either "male" or "female"). |
| `id` | string | yes | Unique identifier for the object. |
| `id_number_provided` | boolean |  | Whether the person's `id_number` was provided. True if either the full ID number was provided or if only the required part of the ID number was provided (ex. last four of an individual's SSN for the US indicated by `ssn_last_4_provided`). |
| `id_number_secondary_provided` | boolean |  | Whether the person's `id_number_secondary` was provided. |
| `last_name` | string |  | The person's last name. |
| `last_name_kana` | string |  | The Kana variation of the person's last name (Japan only). |
| `last_name_kanji` | string |  | The Kanji variation of the person's last name (Japan only). |
| `maiden_name` | string |  | The person's maiden name. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `nationality` | string |  | The country where the person is a national. |
| `object` | enum: `person` | yes | String representing the object's type. Objects of the same type share the same value. |
| `phone` | string |  | The person's phone number. |
| `political_exposure` | enum: `existing`, `none` |  | Indicates if the person or any of their representatives, family members, or other closely related persons, declares that they hold or have held an important public job or function, in any jurisdiction. |
| `registered_address` | `address` |  |  |
| `relationship` | `person_relationship` |  |  |
| `requirements` | `person_requirements` |  |  |
| `ssn_last_4_provided` | boolean |  | Whether the last four digits of the person's Social Security number have been provided (U.S. only). |
| `verification` | `legal_entity_person_verification` |  |  |

## The `deleted_person` object

| Field | Type | Required | Description |
|---|---|---|---|
| `deleted` | enum: `True` | yes | Always true for a deleted object |
| `id` | string | yes | Unique identifier for the object. |
| `object` | enum: `person` | yes | String representing the object's type. Objects of the same type share the same value. |

