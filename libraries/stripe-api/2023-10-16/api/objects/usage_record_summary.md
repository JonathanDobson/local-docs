# Stripe API 2023-10-16 — `usage_record_summary` object

Expandable fields (pass `expand[]=<field>`): `period`

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | yes | Unique identifier for the object. |
| `invoice` | string |  | The invoice in which this usage period has been billed for. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `object` | enum: `usage_record_summary` | yes | String representing the object's type. Objects of the same type share the same value. |
| `period` | `period` | yes |  |
| `subscription_item` | string | yes | The ID of the subscription item this summary is describing. |
| `total_usage` | integer | yes | The total usage within this usage period. |

