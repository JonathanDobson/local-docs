# Stripe API 2023-10-16 — sigma

Operations under `/v1/sigma` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/sigma/scheduled_query_runs

operationId: `GetSigmaScheduledQueryRuns`

Returns a list of scheduled query runs.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## GET /v1/sigma/scheduled_query_runs/{scheduled_query_run}

operationId: `GetSigmaScheduledQueryRunsScheduledQueryRun`

Retrieves the details of an scheduled query run.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `scheduled_query_run (path)` | string | yes |  |

Returns: `scheduled_query_run`

# Objects returned

## The `scheduled_query_run` object

If you have [scheduled a Sigma query](https://stripe.com/docs/sigma/scheduled-queries), you'll
receive a `sigma.scheduled_query_run.created` webhook each time the query
runs. The webhook contains a `ScheduledQueryRun` object, which you can use to
retrieve the query results.

Expandable fields (pass `expand[]=<field>`): `error`, `file`

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `data_load_time` | timestamp (Unix seconds) | yes | When the query was run, Sigma contained a snapshot of your Stripe data at this time. |
| `error` | `sigma_scheduled_query_run_error` |  |  |
| `file` | `file` |  | The file object representing the results of the query. |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `object` | enum: `scheduled_query_run` | yes | String representing the object's type. Objects of the same type share the same value. |
| `result_available_until` | timestamp (Unix seconds) | yes | Time at which the result expires and is no longer available for download. |
| `sql` | string | yes | SQL for the query. |
| `status` | string | yes | The query's execution status, which will be `completed` for successful runs, and `canceled`, `failed`, or `timed_out` otherwise. |
| `title` | string | yes | Title of the query. |

