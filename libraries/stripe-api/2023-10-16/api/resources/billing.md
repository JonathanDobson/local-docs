# Stripe API 2023-10-16 — billing

Operations under `/v1/billing` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## POST /v1/billing/meter_event_adjustments

operationId: `PostBillingMeterEventAdjustments`

Creates a billing meter event adjustment

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `cancel` | object | yes | Specifies which event to cancel. |
| `cancel.identifier` | string | yes |  |
| `event_name` | string | yes | The name of the meter event. Corresponds with the `event_name` field on a meter. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `type` | enum: `cancel` |  | Specifies whether to cancel a single event or a range of events for a time period. |

Returns: `billing.meter_event_adjustment`

## POST /v1/billing/meter_events

operationId: `PostBillingMeterEvents`

Creates a billing meter event

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `event_name` | string | yes | The name of the meter event. Corresponds with the `event_name` field on a meter. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `identifier` | string |  | A unique identifier for the event. If not provided, one will be generated. We recommend using a globally unique identifier for this. We'll enforce uniqueness within a rolling 24 hour period. |
| `payload` | map (key → value) | yes | The payload of the event. This must contain a field with the event's numerical value and a field to map the event to a customer. |
| `timestamp` | timestamp (Unix seconds) | yes | The time of the event. Measured in seconds since the Unix epoch. |

Returns: `billing.meter_event`

## GET /v1/billing/meters

operationId: `GetBillingMeters`

Retrieve a list of billing meters.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `status` | enum: `active`, `inactive` |  | Filter results to only include meters with the given status. |

Returns: object

## POST /v1/billing/meters

operationId: `PostBillingMeters`

Creates a billing meter

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer_mapping` | object |  | Fields that specify how to map a meter event to a customer. |
| `customer_mapping.event_payload_key` | string | yes |  |
| `customer_mapping.type` | enum: `by_id` | yes |  |
| `default_aggregation` | object | yes | The default settings to aggregate a meter's events with. |
| `default_aggregation.formula` | enum: `count`, `sum` | yes |  |
| `display_name` | string | yes | The meter's name. |
| `event_name` | string | yes | The name of the usage event to record usage for. Corresponds with the `event_name` field on usage events. |
| `event_time_window` | enum: `day`, `hour` |  | The time window to pre-aggregate usage events for, if any. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `value_settings` | object |  | Fields that specify how to calculate a usage event's value. |
| `value_settings.event_payload_key` | string | yes |  |

Returns: `billing.meter`

## GET /v1/billing/meters/{id}

operationId: `GetBillingMetersId`

Retrieves a billing meter given an ID

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `id (path)` | string | yes | Unique identifier for the object. |

Returns: `billing.meter`

## POST /v1/billing/meters/{id}

operationId: `PostBillingMetersId`

Updates a billing meter

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string | yes | Unique identifier for the object. |
| `display_name` | string |  | The meter's name. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `billing.meter`

## POST /v1/billing/meters/{id}/deactivate

operationId: `PostBillingMetersIdDeactivate`

Deactivates a billing meter

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string | yes | Unique identifier for the object. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `billing.meter`

## GET /v1/billing/meters/{id}/event_summaries

operationId: `GetBillingMetersIdEventSummaries`

Retrieve a list of billing meter event summaries.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `customer` | string | yes | The customer for which to fetch event summaries. |
| `end_time` | timestamp (Unix seconds) | yes | The timestamp from when to stop aggregating usage events (exclusive). |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `id (path)` | string | yes | Unique identifier for the object. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `start_time` | timestamp (Unix seconds) | yes | The timestamp from when to start aggregating usage events (inclusive). |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `value_grouping_window` | enum: `hour` |  | Specifies what granularity to use when generating event summaries. If not specified, a single event summary would be returned for the specified time range. |

Returns: object

## POST /v1/billing/meters/{id}/reactivate

operationId: `PostBillingMetersIdReactivate`

Reactivates a billing meter

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string | yes | Unique identifier for the object. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `billing.meter`

# Objects returned

## The `billing.meter_event_adjustment` object

A billing meter event adjustment represents the status of a meter event adjustment.

Expandable fields (pass `expand[]=<field>`): `cancel`

| Field | Type | Required | Description |
|---|---|---|---|
| `cancel` | `billing_meter_resource_billing_meter_event_adjustment_cancel` | yes |  |
| `event_name` | string | yes | The name of the meter event. Corresponds with the `event_name` field on a meter. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `object` | enum: `billing.meter_event_adjustment` | yes | String representing the object's type. Objects of the same type share the same value. |
| `status` | enum: `complete`, `pending` | yes | The meter event adjustment's status. |
| `type` | enum: `cancel` | yes | Specifies whether to cancel a single event or a range of events for a time period. |

## The `billing.meter_event` object

A billing meter event represents a customer's usage of a product. Meter events are used to bill a customer based on their usage.
Meter events are associated with billing meters, which define the shape of the event's payload and how those events are aggregated for billing.

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `event_name` | string | yes | The name of the meter event. Corresponds with the `event_name` field on a meter. |
| `identifier` | string | yes | A unique identifier for the event. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `object` | enum: `billing.meter_event` | yes | String representing the object's type. Objects of the same type share the same value. |
| `payload` | map (key → value) | yes | The payload of the event. |
| `timestamp` | timestamp (Unix seconds) | yes | The timestamp passed in when creating the event. Measured in seconds since the Unix epoch. |

## The `billing.meter` object

A billing meter is a resource that allows you to track usage of a particular event. For example, you might create a billing meter to track the number of API calls made by a particular user. You can then use the billing meter to charge the user for the number of API calls they make.

Expandable fields (pass `expand[]=<field>`): `customer_mapping`, `default_aggregation`, `status_transitions`, `value_settings`

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `customer_mapping` | `billing_meter_resource_customer_mapping_settings` | yes |  |
| `default_aggregation` | `billing_meter_resource_aggregation_settings` | yes |  |
| `display_name` | string | yes | The meter's name. |
| `event_name` | string | yes | The name of the usage event to record usage for. Corresponds with the `event_name` field on usage events. |
| `event_time_window` | enum: `day`, `hour` |  | The time window to pre-aggregate usage events for, if any. |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `object` | enum: `billing.meter` | yes | String representing the object's type. Objects of the same type share the same value. |
| `status` | enum: `active`, `inactive` | yes | The meter's status. |
| `status_transitions` | `billing_meter_resource_billing_meter_status_transitions` | yes |  |
| `updated` | timestamp (Unix seconds) | yes | Time at which the object was last updated. Measured in seconds since the Unix epoch. |
| `value_settings` | `billing_meter_resource_billing_meter_value` | yes |  |

