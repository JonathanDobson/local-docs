# Stripe API 2023-10-16 — test helpers / test clocks

Operations under `/v1/test_helpers/test_clocks` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/test_helpers/test_clocks

operationId: `GetTestHelpersTestClocks`

Returns a list of your test clocks.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/test_helpers/test_clocks

operationId: `PostTestHelpersTestClocks`

Creates a new test clock that can be attached to new customers and quotes.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `frozen_time` | timestamp (Unix seconds) | yes | The initial frozen time for this test clock. |
| `name` | string |  | The name for this test clock. |

Returns: `test_helpers.test_clock`

## GET /v1/test_helpers/test_clocks/{test_clock}

operationId: `GetTestHelpersTestClocksTestClock`

Retrieves a test clock.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `test_clock (path)` | string | yes |  |

Returns: `test_helpers.test_clock`

## DELETE /v1/test_helpers/test_clocks/{test_clock}

operationId: `DeleteTestHelpersTestClocksTestClock`

Deletes a test clock.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `test_clock (path)` | string | yes |  |

Returns: `deleted_test_helpers.test_clock`

## POST /v1/test_helpers/test_clocks/{test_clock}/advance

operationId: `PostTestHelpersTestClocksTestClockAdvance`

Starts advancing a test clock to a specified time in the future. Advancement is done when status changes to `Ready`.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `test_clock (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `frozen_time` | timestamp (Unix seconds) | yes | The time to advance the test clock. Must be after the test clock's current frozen time. Cannot be more than two intervals in the future from the shortest subscription in this test clock. If there are no subscriptions in this test clock, it cannot be more than two years in the future. |

Returns: `test_helpers.test_clock`

# Objects returned

## The `test_helpers.test_clock` object

A test clock enables deterministic control over objects in testmode. With a test clock, you can create
objects at a frozen time in the past or future, and advance to a specific future time to observe webhooks and state changes. After the clock advances,
you can either validate the current state of your scenario (and test your assumptions), change the current state of your scenario (and test more complex scenarios), or keep advancing forward in time.

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `deletes_after` | timestamp (Unix seconds) | yes | Time at which this clock is scheduled to auto delete. |
| `frozen_time` | timestamp (Unix seconds) | yes | Time at which all objects belonging to this clock are frozen. |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `name` | string |  | The custom name supplied at creation. |
| `object` | enum: `test_helpers.test_clock` | yes | String representing the object's type. Objects of the same type share the same value. |
| `status` | enum: `advancing`, `internal_failure`, `ready` | yes | The status of the Test Clock. |

## The `deleted_test_helpers.test_clock` object

| Field | Type | Required | Description |
|---|---|---|---|
| `deleted` | enum: `True` | yes | Always true for a deleted object |
| `id` | string | yes | Unique identifier for the object. |
| `object` | enum: `test_helpers.test_clock` | yes | String representing the object's type. Objects of the same type share the same value. |

