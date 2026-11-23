# Stripe API 2023-10-16 — billing portal

Operations under `/v1/billing_portal` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/billing_portal/configurations

operationId: `GetBillingPortalConfigurations`

Returns a list of configurations that describe the functionality of the customer portal.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `active` | boolean |  | Only return configurations that are active or inactive (e.g., pass `true` to only list active configurations). |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `is_default` | boolean |  | Only return the default or non-default configurations (e.g., pass `true` to only list the default configuration). |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/billing_portal/configurations

operationId: `PostBillingPortalConfigurations`

Creates a configuration that describes the functionality and behavior of a PortalSession

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `business_profile` | object | yes | The business information shown to customers in the portal. |
| `business_profile.headline` | string or "" (to unset) |  |  |
| `business_profile.privacy_policy_url` | string |  |  |
| `business_profile.terms_of_service_url` | string |  |  |
| `default_return_url` | string or "" (to unset) |  | The default URL to redirect customers to when they click on the portal's link to return to your website. This can be [overriden](https://stripe.com/docs/api/customer_portal/sessions/create#create_portal_session-return_url) when creating the session. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `features` | object | yes | Information about the features available in the portal. |
| `features.customer_update` | object |  |  |
| `features.customer_update.allowed_updates` | array of enum: `address`, `email`, `name`, `phone`, `shipping`, `tax_id` or "" (to unset) |  |  |
| `features.customer_update.enabled` | boolean | yes |  |
| `features.invoice_history` | object |  |  |
| `features.invoice_history.enabled` | boolean | yes |  |
| `features.payment_method_update` | object |  |  |
| `features.payment_method_update.enabled` | boolean | yes |  |
| `features.subscription_cancel` | object |  |  |
| `features.subscription_cancel.cancellation_reason` | object |  |  |
| `features.subscription_cancel.cancellation_reason.enabled` | boolean | yes |  |
| `features.subscription_cancel.cancellation_reason.options` | array of enum: `customer_service`, `low_quality`, `missing_features`, `other`, `switched_service`, `too_complex`, `too_expensive`, `unused` or "" (to unset) | yes |  |
| `features.subscription_cancel.enabled` | boolean | yes |  |
| `features.subscription_cancel.mode` | enum: `at_period_end`, `immediately` |  |  |
| `features.subscription_cancel.proration_behavior` | enum: `always_invoice`, `create_prorations`, `none` |  |  |
| `features.subscription_update` | object |  |  |
| `features.subscription_update.default_allowed_updates` | array of enum: `price`, `promotion_code`, `quantity` or "" (to unset) | yes |  |
| `features.subscription_update.enabled` | boolean | yes |  |
| `features.subscription_update.products` | array of object or "" (to unset) | yes |  |
| `features.subscription_update.products[].prices` | array of string | yes |  |
| `features.subscription_update.products[].product` | string | yes |  |
| `features.subscription_update.proration_behavior` | enum: `always_invoice`, `create_prorations`, `none` |  |  |
| `login_page` | object |  | The hosted login page for this configuration. Learn more about the portal login page in our [integration docs](https://stripe.com/docs/billing/subscriptions/integrating-customer-portal#share). |
| `login_page.enabled` | boolean | yes |  |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |

Returns: `billing_portal.configuration`

## GET /v1/billing_portal/configurations/{configuration}

operationId: `GetBillingPortalConfigurationsConfiguration`

Retrieves a configuration that describes the functionality of the customer portal.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `configuration (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `billing_portal.configuration`

## POST /v1/billing_portal/configurations/{configuration}

operationId: `PostBillingPortalConfigurationsConfiguration`

Updates a configuration that describes the functionality of the customer portal.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `configuration (path)` | string | yes |  |
| `active` | boolean |  | Whether the configuration is active and can be used to create portal sessions. |
| `business_profile` | object |  | The business information shown to customers in the portal. |
| `business_profile.headline` | string or "" (to unset) |  |  |
| `business_profile.privacy_policy_url` | string or "" (to unset) |  |  |
| `business_profile.terms_of_service_url` | string or "" (to unset) |  |  |
| `default_return_url` | string or "" (to unset) |  | The default URL to redirect customers to when they click on the portal's link to return to your website. This can be [overriden](https://stripe.com/docs/api/customer_portal/sessions/create#create_portal_session-return_url) when creating the session. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `features` | object |  | Information about the features available in the portal. |
| `features.customer_update` | object |  |  |
| `features.customer_update.allowed_updates` | array of enum: `address`, `email`, `name`, `phone`, `shipping`, `tax_id` or "" (to unset) |  |  |
| `features.customer_update.enabled` | boolean |  |  |
| `features.invoice_history` | object |  |  |
| `features.invoice_history.enabled` | boolean | yes |  |
| `features.payment_method_update` | object |  |  |
| `features.payment_method_update.enabled` | boolean | yes |  |
| `features.subscription_cancel` | object |  |  |
| `features.subscription_cancel.cancellation_reason` | object |  |  |
| `features.subscription_cancel.cancellation_reason.enabled` | boolean | yes |  |
| `features.subscription_cancel.cancellation_reason.options` | array of enum: `customer_service`, `low_quality`, `missing_features`, `other`, `switched_service`, `too_complex`, `too_expensive`, `unused` or "" (to unset) |  |  |
| `features.subscription_cancel.enabled` | boolean |  |  |
| `features.subscription_cancel.mode` | enum: `at_period_end`, `immediately` |  |  |
| `features.subscription_cancel.proration_behavior` | enum: `always_invoice`, `create_prorations`, `none` |  |  |
| `features.subscription_update` | object |  |  |
| `features.subscription_update.default_allowed_updates` | array of enum: `price`, `promotion_code`, `quantity` or "" (to unset) |  |  |
| `features.subscription_update.enabled` | boolean |  |  |
| `features.subscription_update.products` | array of object or "" (to unset) |  |  |
| `features.subscription_update.products[].prices` | array of string | yes |  |
| `features.subscription_update.products[].product` | string | yes |  |
| `features.subscription_update.proration_behavior` | enum: `always_invoice`, `create_prorations`, `none` |  |  |
| `login_page` | object |  | The hosted login page for this configuration. Learn more about the portal login page in our [integration docs](https://stripe.com/docs/billing/subscriptions/integrating-customer-portal#share). |
| `login_page.enabled` | boolean | yes |  |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |

Returns: `billing_portal.configuration`

## POST /v1/billing_portal/sessions

operationId: `PostBillingPortalSessions`

Creates a session of the customer portal.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `configuration` | string |  | The ID of an existing [configuration](https://stripe.com/docs/api/customer_portal/configuration) to use for this session, describing its functionality and features. If not specified, the session uses the default configuration. |
| `customer` | string | yes | The ID of an existing customer. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `flow_data` | object |  | Information about a specific flow for the customer to go through. See the [docs](https://stripe.com/docs/customer-management/portal-deep-links) to learn more about using customer portal deep links and flows. |
| `flow_data.after_completion` | object |  |  |
| `flow_data.after_completion.hosted_confirmation` | object |  |  |
| `flow_data.after_completion.hosted_confirmation.custom_message` | string |  |  |
| `flow_data.after_completion.redirect` | object |  |  |
| `flow_data.after_completion.redirect.return_url` | string | yes |  |
| `flow_data.after_completion.type` | enum: `hosted_confirmation`, `portal_homepage`, `redirect` | yes |  |
| `flow_data.subscription_cancel` | object |  |  |
| `flow_data.subscription_cancel.retention` | object |  |  |
| `flow_data.subscription_cancel.retention.coupon_offer` | object | yes |  |
| `flow_data.subscription_cancel.retention.coupon_offer.coupon` | string | yes |  |
| `flow_data.subscription_cancel.retention.type` | enum: `coupon_offer` | yes |  |
| `flow_data.subscription_cancel.subscription` | string | yes |  |
| `flow_data.subscription_update` | object |  |  |
| `flow_data.subscription_update.subscription` | string | yes |  |
| `flow_data.subscription_update_confirm` | object |  |  |
| `flow_data.subscription_update_confirm.discounts` | array of object |  |  |
| `flow_data.subscription_update_confirm.discounts[].coupon` | string |  |  |
| `flow_data.subscription_update_confirm.discounts[].promotion_code` | string |  |  |
| `flow_data.subscription_update_confirm.items` | array of object | yes |  |
| `flow_data.subscription_update_confirm.items[].id` | string | yes |  |
| `flow_data.subscription_update_confirm.items[].price` | string |  |  |
| `flow_data.subscription_update_confirm.items[].quantity` | integer |  |  |
| `flow_data.subscription_update_confirm.subscription` | string | yes |  |
| `flow_data.type` | enum: `payment_method_update`, `subscription_cancel`, `subscription_update`, `subscription_update_confirm` | yes |  |
| `locale` | enum: `auto`, `bg`, `cs`, `da`, `de`, `el`, `en`, `en-AU`, `en-CA`, `en-GB`, `en-IE`, `en-IN`, `en-NZ`, `en-SG`, `es`, `es-419`, `et`, `fi`, `fil`, `fr`, `fr-CA`, `hr`, `hu`, `id`, `it`, `ja`, `ko`, `lt`, `lv`, `ms`, `mt`, `nb`, `nl`, `pl`, `pt`, `pt-BR`, `ro`, `ru`, `sk`, `sl`, `sv`, `th`, `tr`, `vi`, `zh`, `zh-HK`, `zh-TW` |  | The IETF language tag of the locale customer portal is displayed in. If blank or auto, the customer’s `preferred_locales` or browser’s locale is used. |
| `on_behalf_of` | string |  | The `on_behalf_of` account to use for this session. When specified, only subscriptions and invoices with this `on_behalf_of` account appear in the portal. For more information, see the [docs](https://stripe.com/docs/connect/separate-charges-and-transfers#on-behalf-of). Use the [Accounts API](https://stripe.com/docs/api/accounts/object#account_object-settings-branding) to modify the `on_behalf_of` account's branding settings, which the portal displays. |
| `return_url` | string |  | The default URL to redirect customers to when they click on the portal's link to return to your website. |

Returns: `billing_portal.session`

# Objects returned

## The `billing_portal.configuration` object

A portal configuration describes the functionality and behavior of a portal session.

Expandable fields (pass `expand[]=<field>`): `application`, `business_profile`, `features`, `login_page`

| Field | Type | Required | Description |
|---|---|---|---|
| `active` | boolean | yes | Whether the configuration is active and can be used to create portal sessions. |
| `application` | string or `application` or `deleted_application` |  | ID of the Connect Application that created the configuration. |
| `business_profile` | `portal_business_profile` | yes |  |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `default_return_url` | string |  | The default URL to redirect customers to when they click on the portal's link to return to your website. This can be [overriden](https://stripe.com/docs/api/customer_portal/sessions/create#create_portal_session-return_url) when creating the session. |
| `features` | `portal_features` | yes |  |
| `id` | string | yes | Unique identifier for the object. |
| `is_default` | boolean | yes | Whether the configuration is the default. If `true`, this configuration can be managed in the Dashboard and portal sessions will use this configuration unless it is overriden when creating the session. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `login_page` | `portal_login_page` | yes |  |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `object` | enum: `billing_portal.configuration` | yes | String representing the object's type. Objects of the same type share the same value. |
| `updated` | timestamp (Unix seconds) | yes | Time at which the object was last updated. Measured in seconds since the Unix epoch. |

## The `billing_portal.session` object

The Billing customer portal is a Stripe-hosted UI for subscription and
billing management.

A portal configuration describes the functionality and features that you
want to provide to your customers through the portal.

A portal session describes the instantiation of the customer portal for
a particular customer. By visiting the session's URL, the customer
can manage their subscriptions and billing details. For security reasons,
sessions are short-lived and will expire if the customer does not visit the URL.
Create sessions on-demand when customers intend to manage their subscriptions
and billing details.

Learn more in the [integration guide](https://stripe.com/docs/billing/subscriptions/integrating-customer-portal).

Expandable fields (pass `expand[]=<field>`): `configuration`, `flow`

| Field | Type | Required | Description |
|---|---|---|---|
| `configuration` | string or `billing_portal.configuration` | yes | The configuration used by this session, describing the features available. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `customer` | string | yes | The ID of the customer for this session. |
| `flow` | `portal_flows_flow` |  | Information about a specific flow for the customer to go through. See the [docs](https://stripe.com/docs/customer-management/portal-deep-links) to learn more about using customer portal deep links and flows. |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `locale` | enum: `auto`, `bg`, `cs`, `da`, `de`, `el`, `en`, `en-AU`, `en-CA`, `en-GB`, `en-IE`, `en-IN`, `en-NZ`, `en-SG`, `es`, `es-419`, `et`, `fi`, `fil`, `fr`, `fr-CA`, `hr`, `hu`, `id`, `it`, `ja`, `ko`, `lt`, `lv`, `ms`, `mt`, `nb`, `nl`, `pl`, `pt`, `pt-BR`, `ro`, `ru`, `sk`, `sl`, `sv`, `th`, `tr`, `vi`, `zh`, `zh-HK`, `zh-TW` |  | The IETF language tag of the locale Customer Portal is displayed in. If blank or auto, the customer’s `preferred_locales` or browser’s locale is used. |
| `object` | enum: `billing_portal.session` | yes | String representing the object's type. Objects of the same type share the same value. |
| `on_behalf_of` | string |  | The account for which the session was created on behalf of. When specified, only subscriptions and invoices with this `on_behalf_of` account appear in the portal. For more information, see the [docs](https://stripe.com/docs/connect/separate-charges-and-transfers#on-behalf-of). Use the [Accounts API](https://stripe.com/docs/api/accounts/object#account_object-settings-branding) to modify the `on_behalf_of` account's branding settings, which the portal displays. |
| `return_url` | string |  | The URL to redirect customers to when they click on the portal's link to return to your website. |
| `url` | string | yes | The short-lived URL of the session that gives customers access to the customer portal. |

