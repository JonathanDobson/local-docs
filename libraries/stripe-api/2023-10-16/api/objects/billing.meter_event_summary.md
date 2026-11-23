# Stripe API 2023-10-16 — `billing.meter_event_summary` object

A billing meter event summary represents an aggregated view of a customer's billing meter events within a specified timeframe. It indicates how much
usage was accrued by a customer for that period.

| Field | Type | Required | Description |
|---|---|---|---|
| `aggregated_value` | number | yes | Aggregated value of all the events within start_time (inclusive) and end_time (inclusive). The aggregation strategy is defined on meter via `default_aggregation``. |
| `end_time` | timestamp (Unix seconds) | yes | End timestamp for this usage summary (inclusive). |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `meter` | string | yes | The meter associated with this usage summary. |
| `object` | enum: `billing.meter_event_summary` | yes | String representing the object's type. Objects of the same type share the same value. |
| `start_time` | timestamp (Unix seconds) | yes | Start timestamp for this usage summary (inclusive). |

