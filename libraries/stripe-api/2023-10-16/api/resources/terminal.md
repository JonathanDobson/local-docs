# Stripe API 2023-10-16 — terminal

Operations under `/v1/terminal` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/terminal/configurations

operationId: `GetTerminalConfigurations`

Returns a list of `Configuration` objects.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `is_account_default` | boolean |  | if present, only return the account default or non-default configurations. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/terminal/configurations

operationId: `PostTerminalConfigurations`

Creates a new `Configuration` object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `bbpos_wisepos_e` | object |  | An object containing device type specific settings for BBPOS WisePOS E readers |
| `bbpos_wisepos_e.splashscreen` | string or "" (to unset) |  |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `name` | string |  | Name of the configuration |
| `offline` | object or "" (to unset) |  | Configurations for collecting transactions offline. |
| `offline.enabled` | boolean | yes |  |
| `tipping` | object or "" (to unset) |  | Tipping configurations for readers supporting on-reader tips |
| `tipping.aud` | object |  |  |
| `tipping.aud.fixed_amounts` | array of integer |  |  |
| `tipping.aud.percentages` | array of integer |  |  |
| `tipping.aud.smart_tip_threshold` | integer |  |  |
| `tipping.cad` | object |  |  |
| `tipping.cad.fixed_amounts` | array of integer |  |  |
| `tipping.cad.percentages` | array of integer |  |  |
| `tipping.cad.smart_tip_threshold` | integer |  |  |
| `tipping.chf` | object |  |  |
| `tipping.chf.fixed_amounts` | array of integer |  |  |
| `tipping.chf.percentages` | array of integer |  |  |
| `tipping.chf.smart_tip_threshold` | integer |  |  |
| `tipping.czk` | object |  |  |
| `tipping.czk.fixed_amounts` | array of integer |  |  |
| `tipping.czk.percentages` | array of integer |  |  |
| `tipping.czk.smart_tip_threshold` | integer |  |  |
| `tipping.dkk` | object |  |  |
| `tipping.dkk.fixed_amounts` | array of integer |  |  |
| `tipping.dkk.percentages` | array of integer |  |  |
| `tipping.dkk.smart_tip_threshold` | integer |  |  |
| `tipping.eur` | object |  |  |
| `tipping.eur.fixed_amounts` | array of integer |  |  |
| `tipping.eur.percentages` | array of integer |  |  |
| `tipping.eur.smart_tip_threshold` | integer |  |  |
| `tipping.gbp` | object |  |  |
| `tipping.gbp.fixed_amounts` | array of integer |  |  |
| `tipping.gbp.percentages` | array of integer |  |  |
| `tipping.gbp.smart_tip_threshold` | integer |  |  |
| `tipping.hkd` | object |  |  |
| `tipping.hkd.fixed_amounts` | array of integer |  |  |
| `tipping.hkd.percentages` | array of integer |  |  |
| `tipping.hkd.smart_tip_threshold` | integer |  |  |
| `tipping.myr` | object |  |  |
| `tipping.myr.fixed_amounts` | array of integer |  |  |
| `tipping.myr.percentages` | array of integer |  |  |
| `tipping.myr.smart_tip_threshold` | integer |  |  |
| `tipping.nok` | object |  |  |
| `tipping.nok.fixed_amounts` | array of integer |  |  |
| `tipping.nok.percentages` | array of integer |  |  |
| `tipping.nok.smart_tip_threshold` | integer |  |  |
| `tipping.nzd` | object |  |  |
| `tipping.nzd.fixed_amounts` | array of integer |  |  |
| `tipping.nzd.percentages` | array of integer |  |  |
| `tipping.nzd.smart_tip_threshold` | integer |  |  |
| `tipping.sek` | object |  |  |
| `tipping.sek.fixed_amounts` | array of integer |  |  |
| `tipping.sek.percentages` | array of integer |  |  |
| `tipping.sek.smart_tip_threshold` | integer |  |  |
| `tipping.sgd` | object |  |  |
| `tipping.sgd.fixed_amounts` | array of integer |  |  |
| `tipping.sgd.percentages` | array of integer |  |  |
| `tipping.sgd.smart_tip_threshold` | integer |  |  |
| `tipping.usd` | object |  |  |
| `tipping.usd.fixed_amounts` | array of integer |  |  |
| `tipping.usd.percentages` | array of integer |  |  |
| `tipping.usd.smart_tip_threshold` | integer |  |  |
| `verifone_p400` | object |  | An object containing device type specific settings for Verifone P400 readers |
| `verifone_p400.splashscreen` | string or "" (to unset) |  |  |

Returns: `terminal.configuration`

## GET /v1/terminal/configurations/{configuration}

operationId: `GetTerminalConfigurationsConfiguration`

Retrieves a `Configuration` object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `configuration (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `terminal.configuration` or `deleted_terminal.configuration`

## POST /v1/terminal/configurations/{configuration}

operationId: `PostTerminalConfigurationsConfiguration`

Updates a new `Configuration` object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `configuration (path)` | string | yes |  |
| `bbpos_wisepos_e` | object or "" (to unset) |  | An object containing device type specific settings for BBPOS WisePOS E readers |
| `bbpos_wisepos_e.splashscreen` | string or "" (to unset) |  |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `name` | string |  | Name of the configuration |
| `offline` | object or "" (to unset) |  | Configurations for collecting transactions offline. |
| `offline.enabled` | boolean | yes |  |
| `tipping` | object or "" (to unset) |  | Tipping configurations for readers supporting on-reader tips |
| `tipping.aud` | object |  |  |
| `tipping.aud.fixed_amounts` | array of integer |  |  |
| `tipping.aud.percentages` | array of integer |  |  |
| `tipping.aud.smart_tip_threshold` | integer |  |  |
| `tipping.cad` | object |  |  |
| `tipping.cad.fixed_amounts` | array of integer |  |  |
| `tipping.cad.percentages` | array of integer |  |  |
| `tipping.cad.smart_tip_threshold` | integer |  |  |
| `tipping.chf` | object |  |  |
| `tipping.chf.fixed_amounts` | array of integer |  |  |
| `tipping.chf.percentages` | array of integer |  |  |
| `tipping.chf.smart_tip_threshold` | integer |  |  |
| `tipping.czk` | object |  |  |
| `tipping.czk.fixed_amounts` | array of integer |  |  |
| `tipping.czk.percentages` | array of integer |  |  |
| `tipping.czk.smart_tip_threshold` | integer |  |  |
| `tipping.dkk` | object |  |  |
| `tipping.dkk.fixed_amounts` | array of integer |  |  |
| `tipping.dkk.percentages` | array of integer |  |  |
| `tipping.dkk.smart_tip_threshold` | integer |  |  |
| `tipping.eur` | object |  |  |
| `tipping.eur.fixed_amounts` | array of integer |  |  |
| `tipping.eur.percentages` | array of integer |  |  |
| `tipping.eur.smart_tip_threshold` | integer |  |  |
| `tipping.gbp` | object |  |  |
| `tipping.gbp.fixed_amounts` | array of integer |  |  |
| `tipping.gbp.percentages` | array of integer |  |  |
| `tipping.gbp.smart_tip_threshold` | integer |  |  |
| `tipping.hkd` | object |  |  |
| `tipping.hkd.fixed_amounts` | array of integer |  |  |
| `tipping.hkd.percentages` | array of integer |  |  |
| `tipping.hkd.smart_tip_threshold` | integer |  |  |
| `tipping.myr` | object |  |  |
| `tipping.myr.fixed_amounts` | array of integer |  |  |
| `tipping.myr.percentages` | array of integer |  |  |
| `tipping.myr.smart_tip_threshold` | integer |  |  |
| `tipping.nok` | object |  |  |
| `tipping.nok.fixed_amounts` | array of integer |  |  |
| `tipping.nok.percentages` | array of integer |  |  |
| `tipping.nok.smart_tip_threshold` | integer |  |  |
| `tipping.nzd` | object |  |  |
| `tipping.nzd.fixed_amounts` | array of integer |  |  |
| `tipping.nzd.percentages` | array of integer |  |  |
| `tipping.nzd.smart_tip_threshold` | integer |  |  |
| `tipping.sek` | object |  |  |
| `tipping.sek.fixed_amounts` | array of integer |  |  |
| `tipping.sek.percentages` | array of integer |  |  |
| `tipping.sek.smart_tip_threshold` | integer |  |  |
| `tipping.sgd` | object |  |  |
| `tipping.sgd.fixed_amounts` | array of integer |  |  |
| `tipping.sgd.percentages` | array of integer |  |  |
| `tipping.sgd.smart_tip_threshold` | integer |  |  |
| `tipping.usd` | object |  |  |
| `tipping.usd.fixed_amounts` | array of integer |  |  |
| `tipping.usd.percentages` | array of integer |  |  |
| `tipping.usd.smart_tip_threshold` | integer |  |  |
| `verifone_p400` | object or "" (to unset) |  | An object containing device type specific settings for Verifone P400 readers |
| `verifone_p400.splashscreen` | string or "" (to unset) |  |  |

Returns: `terminal.configuration` or `deleted_terminal.configuration`

## DELETE /v1/terminal/configurations/{configuration}

operationId: `DeleteTerminalConfigurationsConfiguration`

Deletes a `Configuration` object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `configuration (path)` | string | yes |  |

Returns: `deleted_terminal.configuration`

## POST /v1/terminal/connection_tokens

operationId: `PostTerminalConnectionTokens`

To connect to a reader the Stripe Terminal SDK needs to retrieve a short-lived connection token from Stripe, proxied through your server. On your backend, add an endpoint that creates and returns a connection token.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `location` | string |  | The id of the location that this connection token is scoped to. If specified the connection token will only be usable with readers assigned to that location, otherwise the connection token will be usable with all readers. Note that location scoping only applies to internet-connected readers. For more details, see [the docs on scoping connection tokens](https://stripe.com/docs/terminal/fleet/locations#connection-tokens). |

Returns: `terminal.connection_token`

## GET /v1/terminal/locations

operationId: `GetTerminalLocations`

Returns a list of `Location` objects.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/terminal/locations

operationId: `PostTerminalLocations`

Creates a new `Location` object.
For further details, including which address fields are required in each country, see the [Manage locations](https://stripe.com/docs/terminal/fleet/locations) guide.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `address` | object | yes | The full address of the location. |
| `address.city` | string |  |  |
| `address.country` | string | yes |  |
| `address.line1` | string |  |  |
| `address.line2` | string |  |  |
| `address.postal_code` | string |  |  |
| `address.state` | string |  |  |
| `configuration_overrides` | string |  | The ID of a configuration that will be used to customize all readers in this location. |
| `display_name` | string | yes | A name for the location. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |

Returns: `terminal.location`

## GET /v1/terminal/locations/{location}

operationId: `GetTerminalLocationsLocation`

Retrieves a `Location` object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `location (path)` | string | yes |  |

Returns: `terminal.location` or `deleted_terminal.location`

## POST /v1/terminal/locations/{location}

operationId: `PostTerminalLocationsLocation`

Updates a `Location` object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `location (path)` | string | yes |  |
| `address` | object |  | The full address of the location. |
| `address.city` | string |  |  |
| `address.country` | string |  |  |
| `address.line1` | string |  |  |
| `address.line2` | string |  |  |
| `address.postal_code` | string |  |  |
| `address.state` | string |  |  |
| `configuration_overrides` | string or "" (to unset) |  | The ID of a configuration that will be used to customize all readers in this location. |
| `display_name` | string |  | A name for the location. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |

Returns: `terminal.location` or `deleted_terminal.location`

## DELETE /v1/terminal/locations/{location}

operationId: `DeleteTerminalLocationsLocation`

Deletes a `Location` object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `location (path)` | string | yes |  |

Returns: `deleted_terminal.location`

## GET /v1/terminal/readers

operationId: `GetTerminalReaders`

Returns a list of `Reader` objects.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `device_type` | enum: `bbpos_chipper2x`, `bbpos_wisepad3`, `bbpos_wisepos_e`, `mobile_phone_reader`, `simulated_wisepos_e`, `stripe_m2`, `verifone_P400` |  | Filters readers by device type |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `location` | string |  | A location ID to filter the response list to only readers at the specific location |
| `serial_number` | string |  | Filters readers by serial number |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `status` | enum: `offline`, `online` |  | A status filter to filter readers to only offline or online readers |

Returns: object

## POST /v1/terminal/readers

operationId: `PostTerminalReaders`

Creates a new `Reader` object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `label` | string |  | Custom label given to the reader for easier identification. If no label is specified, the registration code will be used. |
| `location` | string |  | The location to assign the reader to. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `registration_code` | string | yes | A code generated by the reader used for registering to an account. |

Returns: `terminal.reader`

## GET /v1/terminal/readers/{reader}

operationId: `GetTerminalReadersReader`

Retrieves a `Reader` object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `reader (path)` | string | yes |  |

Returns: `terminal.reader` or `deleted_terminal.reader`

## POST /v1/terminal/readers/{reader}

operationId: `PostTerminalReadersReader`

Updates a `Reader` object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `reader (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `label` | string or "" (to unset) |  | The new label of the reader. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |

Returns: `terminal.reader` or `deleted_terminal.reader`

## DELETE /v1/terminal/readers/{reader}

operationId: `DeleteTerminalReadersReader`

Deletes a `Reader` object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `reader (path)` | string | yes |  |

Returns: `deleted_terminal.reader`

## POST /v1/terminal/readers/{reader}/cancel_action

operationId: `PostTerminalReadersReaderCancelAction`

Cancels the current reader action.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `reader (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `terminal.reader`

## POST /v1/terminal/readers/{reader}/process_payment_intent

operationId: `PostTerminalReadersReaderProcessPaymentIntent`

Initiates a payment flow on a Reader.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `reader (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `payment_intent` | string | yes | PaymentIntent ID |
| `process_config` | object |  | Configuration overrides |
| `process_config.enable_customer_cancellation` | boolean |  |  |
| `process_config.skip_tipping` | boolean |  |  |
| `process_config.tipping` | object |  |  |
| `process_config.tipping.amount_eligible` | integer |  |  |

Returns: `terminal.reader`

## POST /v1/terminal/readers/{reader}/process_setup_intent

operationId: `PostTerminalReadersReaderProcessSetupIntent`

Initiates a setup intent flow on a Reader.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `reader (path)` | string | yes |  |
| `customer_consent_collected` | boolean | yes | Customer Consent Collected |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `process_config` | object |  | Configuration overrides |
| `process_config.enable_customer_cancellation` | boolean |  |  |
| `setup_intent` | string | yes | SetupIntent ID |

Returns: `terminal.reader`

## POST /v1/terminal/readers/{reader}/refund_payment

operationId: `PostTerminalReadersReaderRefundPayment`

Initiates a refund on a Reader

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `reader (path)` | string | yes |  |
| `amount` | integer |  | A positive integer in __cents__ representing how much of this charge to refund. |
| `charge` | string |  | ID of the Charge to refund. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `payment_intent` | string |  | ID of the PaymentIntent to refund. |
| `refund_application_fee` | boolean |  | Boolean indicating whether the application fee should be refunded when refunding this charge. If a full charge refund is given, the full application fee will be refunded. Otherwise, the application fee will be refunded in an amount proportional to the amount of the charge refunded. An application fee can be refunded only by the application that created the charge. |
| `refund_payment_config` | object |  | Configuration overrides |
| `refund_payment_config.enable_customer_cancellation` | boolean |  |  |
| `reverse_transfer` | boolean |  | Boolean indicating whether the transfer should be reversed when refunding this charge. The transfer will be reversed proportionally to the amount being refunded (either the entire or partial amount). A transfer can be reversed only by the application that created the charge. |

Returns: `terminal.reader`

## POST /v1/terminal/readers/{reader}/set_reader_display

operationId: `PostTerminalReadersReaderSetReaderDisplay`

Sets reader display to show cart details.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `reader (path)` | string | yes |  |
| `cart` | object |  | Cart |
| `cart.currency` | string | yes |  |
| `cart.line_items` | array of object | yes |  |
| `cart.line_items[].amount` | integer | yes |  |
| `cart.line_items[].description` | string | yes |  |
| `cart.line_items[].quantity` | integer | yes |  |
| `cart.tax` | integer |  |  |
| `cart.total` | integer | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `type` | enum: `cart` | yes | Type |

Returns: `terminal.reader`

# Objects returned

## The `terminal.configuration` object

A Configurations object represents how features should be configured for terminal readers.

Expandable fields (pass `expand[]=<field>`): `bbpos_wisepos_e`, `offline`, `tipping`, `verifone_p400`

| Field | Type | Required | Description |
|---|---|---|---|
| `bbpos_wisepos_e` | `terminal_configuration_configuration_resource_device_type_specific_config` |  |  |
| `id` | string | yes | Unique identifier for the object. |
| `is_account_default` | boolean |  | Whether this Configuration is the default for your account |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `name` | string |  | String indicating the name of the Configuration object, set by the user |
| `object` | enum: `terminal.configuration` | yes | String representing the object's type. Objects of the same type share the same value. |
| `offline` | `terminal_configuration_configuration_resource_offline_config` |  |  |
| `tipping` | `terminal_configuration_configuration_resource_tipping` |  |  |
| `verifone_p400` | `terminal_configuration_configuration_resource_device_type_specific_config` |  |  |

## The `deleted_terminal.configuration` object

| Field | Type | Required | Description |
|---|---|---|---|
| `deleted` | enum: `True` | yes | Always true for a deleted object |
| `id` | string | yes | Unique identifier for the object. |
| `object` | enum: `terminal.configuration` | yes | String representing the object's type. Objects of the same type share the same value. |

## The `terminal.connection_token` object

A Connection Token is used by the Stripe Terminal SDK to connect to a reader.

Related guide: [Fleet management](https://stripe.com/docs/terminal/fleet/locations)

| Field | Type | Required | Description |
|---|---|---|---|
| `location` | string |  | The id of the location that this connection token is scoped to. Note that location scoping only applies to internet-connected readers. For more details, see [the docs on scoping connection tokens](https://stripe.com/docs/terminal/fleet/locations#connection-tokens). |
| `object` | enum: `terminal.connection_token` | yes | String representing the object's type. Objects of the same type share the same value. |
| `secret` | string | yes | Your application should pass this token to the Stripe Terminal SDK. |

## The `terminal.location` object

A Location represents a grouping of readers.

Related guide: [Fleet management](https://stripe.com/docs/terminal/fleet/locations)

Expandable fields (pass `expand[]=<field>`): `address`

| Field | Type | Required | Description |
|---|---|---|---|
| `address` | `address` | yes |  |
| `configuration_overrides` | string |  | The ID of a configuration that will be used to customize all readers in this location. |
| `display_name` | string | yes | The display name of the location. |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) | yes | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `object` | enum: `terminal.location` | yes | String representing the object's type. Objects of the same type share the same value. |

## The `deleted_terminal.location` object

| Field | Type | Required | Description |
|---|---|---|---|
| `deleted` | enum: `True` | yes | Always true for a deleted object |
| `id` | string | yes | Unique identifier for the object. |
| `object` | enum: `terminal.location` | yes | String representing the object's type. Objects of the same type share the same value. |

## The `terminal.reader` object

A Reader represents a physical device for accepting payment details.

Related guide: [Connecting to a reader](https://stripe.com/docs/terminal/payments/connect-reader)

Expandable fields (pass `expand[]=<field>`): `action`, `location`

| Field | Type | Required | Description |
|---|---|---|---|
| `action` | `terminal_reader_reader_resource_reader_action` |  | The most recent action performed by the reader. |
| `device_sw_version` | string |  | The current software version of the reader. |
| `device_type` | enum: `bbpos_chipper2x`, `bbpos_wisepad3`, `bbpos_wisepos_e`, `mobile_phone_reader`, `simulated_wisepos_e`, `stripe_m2`, `verifone_P400` | yes | Type of reader, one of `bbpos_wisepad3`, `stripe_m2`, `bbpos_chipper2x`, `bbpos_wisepos_e`, `verifone_P400`, `simulated_wisepos_e`, or `mobile_phone_reader`. |
| `id` | string | yes | Unique identifier for the object. |
| `ip_address` | string |  | The local IP address of the reader. |
| `label` | string | yes | Custom label given to the reader for easier identification. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `location` | string or `terminal.location` |  | The location identifier of the reader. |
| `metadata` | map (key → value) | yes | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `object` | enum: `terminal.reader` | yes | String representing the object's type. Objects of the same type share the same value. |
| `serial_number` | string | yes | Serial number of the reader. |
| `status` | enum: `offline`, `online` |  | The networking status of the reader. |

## The `deleted_terminal.reader` object

| Field | Type | Required | Description |
|---|---|---|---|
| `deleted` | enum: `True` | yes | Always true for a deleted object |
| `id` | string | yes | Unique identifier for the object. |
| `object` | enum: `terminal.reader` | yes | String representing the object's type. Objects of the same type share the same value. |

