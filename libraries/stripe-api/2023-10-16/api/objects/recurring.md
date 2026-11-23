# Stripe API 2023-10-16 — `recurring` object

| Field | Type | Required | Description |
|---|---|---|---|
| `aggregate_usage` | enum: `last_during_period`, `last_ever`, `max`, `sum` |  | Specifies a usage aggregation strategy for prices of `usage_type=metered`. Defaults to `sum`. |
| `interval` | enum: `day`, `month`, `week`, `year` | yes | The frequency at which a subscription is billed. One of `day`, `week`, `month` or `year`. |
| `interval_count` | integer | yes | The number of intervals (specified in the `interval` attribute) between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months. |
| `meter` | string |  | The meter tracking the usage of a metered price |
| `usage_type` | enum: `licensed`, `metered` | yes | Configures how the quantity per period should be determined. Can be either `metered` or `licensed`. `licensed` automatically bills the `quantity` set when adding it to a subscription. `metered` aggregates the total usage based on usage records. Defaults to `licensed`. |

