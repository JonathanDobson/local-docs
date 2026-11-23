# Stripe API 2023-10-16 — radar

Operations under `/v1/radar` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/radar/early_fraud_warnings

operationId: `GetRadarEarlyFraudWarnings`

Returns a list of early fraud warnings.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `charge` | string |  | Only return early fraud warnings for the charge specified by this charge ID. |
| `created` | object or integer |  | Only return early fraud warnings that were created during the given date interval. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `payment_intent` | string |  | Only return early fraud warnings for charges that were created by the PaymentIntent specified by this PaymentIntent ID. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## GET /v1/radar/early_fraud_warnings/{early_fraud_warning}

operationId: `GetRadarEarlyFraudWarningsEarlyFraudWarning`

Retrieves the details of an early fraud warning that has previously been created. 

Please refer to the [early fraud warning](#early_fraud_warning_object) object reference for more details.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `early_fraud_warning (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `radar.early_fraud_warning`

## GET /v1/radar/value_list_items

operationId: `GetRadarValueListItems`

Returns a list of `ValueListItem` objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | object or integer |  | Only return items that were created during the given date interval. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `value` | string |  | Return items belonging to the parent list whose value matches the specified value (using an "is like" match). |
| `value_list` | string | yes | Identifier for the parent value list this item belongs to. |

Returns: object

## POST /v1/radar/value_list_items

operationId: `PostRadarValueListItems`

Creates a new `ValueListItem` object, which is added to the specified parent value list.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `value` | string | yes | The value of the item (whose type must match the type of the parent value list). |
| `value_list` | string | yes | The identifier of the value list which the created item will be added to. |

Returns: `radar.value_list_item`

## GET /v1/radar/value_list_items/{item}

operationId: `GetRadarValueListItemsItem`

Retrieves a `ValueListItem` object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `item (path)` | string | yes |  |

Returns: `radar.value_list_item`

## DELETE /v1/radar/value_list_items/{item}

operationId: `DeleteRadarValueListItemsItem`

Deletes a `ValueListItem` object, removing it from its parent value list.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `item (path)` | string | yes |  |

Returns: `deleted_radar.value_list_item`

## GET /v1/radar/value_lists

operationId: `GetRadarValueLists`

Returns a list of `ValueList` objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `alias` | string |  | The alias used to reference the value list when writing rules. |
| `contains` | string |  | A value contained within a value list - returns all value lists containing this value. |
| `created` | object or integer |  | Only return value lists that were created during the given date interval. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/radar/value_lists

operationId: `PostRadarValueLists`

Creates a new `ValueList` object, which can then be referenced in rules.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `alias` | string | yes | The name of the value list for use in rules. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `item_type` | enum: `card_bin`, `card_fingerprint`, `case_sensitive_string`, `country`, `customer_id`, `email`, `ip_address`, `sepa_debit_fingerprint`, `string`, `us_bank_account_fingerprint` |  | Type of the items in the value list. One of `card_fingerprint`, `us_bank_account_fingerprint`, `sepa_debit_fingerprint`, `card_bin`, `email`, `ip_address`, `country`, `string`, `case_sensitive_string`, or `customer_id`. Use `string` if the item type is unknown or mixed. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `name` | string | yes | The human-readable name of the value list. |

Returns: `radar.value_list`

## GET /v1/radar/value_lists/{value_list}

operationId: `GetRadarValueListsValueList`

Retrieves a `ValueList` object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `value_list (path)` | string | yes |  |

Returns: `radar.value_list`

## POST /v1/radar/value_lists/{value_list}

operationId: `PostRadarValueListsValueList`

Updates a `ValueList` object by setting the values of the parameters passed. Any parameters not provided will be left unchanged. Note that `item_type` is immutable.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `value_list (path)` | string | yes |  |
| `alias` | string |  | The name of the value list for use in rules. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `name` | string |  | The human-readable name of the value list. |

Returns: `radar.value_list`

## DELETE /v1/radar/value_lists/{value_list}

operationId: `DeleteRadarValueListsValueList`

Deletes a `ValueList` object, also deleting any items contained within the value list. To be deleted, a value list must not be referenced in any rules.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `value_list (path)` | string | yes |  |

Returns: `deleted_radar.value_list`

# Objects returned

## The `radar.early_fraud_warning` object

An early fraud warning indicates that the card issuer has notified us that a
charge may be fraudulent.

Related guide: [Early fraud warnings](https://stripe.com/docs/disputes/measuring#early-fraud-warnings)

Expandable fields (pass `expand[]=<field>`): `charge`, `payment_intent`

| Field | Type | Required | Description |
|---|---|---|---|
| `actionable` | boolean | yes | An EFW is actionable if it has not received a dispute and has not been fully refunded. You may wish to proactively refund a charge that receives an EFW, in order to avoid receiving a dispute later. |
| `charge` | string or `charge` | yes | ID of the charge this early fraud warning is for, optionally expanded. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `fraud_type` | string | yes | The type of fraud labelled by the issuer. One of `card_never_received`, `fraudulent_card_application`, `made_with_counterfeit_card`, `made_with_lost_card`, `made_with_stolen_card`, `misc`, `unauthorized_use_of_card`. |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `object` | enum: `radar.early_fraud_warning` | yes | String representing the object's type. Objects of the same type share the same value. |
| `payment_intent` | string or `payment_intent` |  | ID of the Payment Intent this early fraud warning is for, optionally expanded. |

## The `radar.value_list_item` object

Value list items allow you to add specific values to a given Radar value list, which can then be used in rules.

Related guide: [Managing list items](https://stripe.com/docs/radar/lists#managing-list-items)

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `created_by` | string | yes | The name or email address of the user who added this item to the value list. |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `object` | enum: `radar.value_list_item` | yes | String representing the object's type. Objects of the same type share the same value. |
| `value` | string | yes | The value of the item. |
| `value_list` | string | yes | The identifier of the value list this item belongs to. |

## The `deleted_radar.value_list_item` object

| Field | Type | Required | Description |
|---|---|---|---|
| `deleted` | enum: `True` | yes | Always true for a deleted object |
| `id` | string | yes | Unique identifier for the object. |
| `object` | enum: `radar.value_list_item` | yes | String representing the object's type. Objects of the same type share the same value. |

## The `radar.value_list` object

Value lists allow you to group values together which can then be referenced in rules.

Related guide: [Default Stripe lists](https://stripe.com/docs/radar/lists#managing-list-items)

Expandable fields (pass `expand[]=<field>`): `list_items`

| Field | Type | Required | Description |
|---|---|---|---|
| `alias` | string | yes | The name of the value list for use in rules. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `created_by` | string | yes | The name or email address of the user who created this value list. |
| `id` | string | yes | Unique identifier for the object. |
| `item_type` | enum: `card_bin`, `card_fingerprint`, `case_sensitive_string`, `country`, `customer_id`, `email`, `ip_address`, `sepa_debit_fingerprint`, `string`, `us_bank_account_fingerprint` | yes | The type of items in the value list. One of `card_fingerprint`, `us_bank_account_fingerprint`, `sepa_debit_fingerprint`, `card_bin`, `email`, `ip_address`, `country`, `string`, `case_sensitive_string`, or `customer_id`. |
| `list_items` | object | yes | List of items contained within this value list. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) | yes | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `name` | string | yes | The name of the value list. |
| `object` | enum: `radar.value_list` | yes | String representing the object's type. Objects of the same type share the same value. |

## The `deleted_radar.value_list` object

| Field | Type | Required | Description |
|---|---|---|---|
| `deleted` | enum: `True` | yes | Always true for a deleted object |
| `id` | string | yes | Unique identifier for the object. |
| `object` | enum: `radar.value_list` | yes | String representing the object's type. Objects of the same type share the same value. |

