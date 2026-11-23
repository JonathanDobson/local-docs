# Stripe API 2023-10-16 — `payment_method_config_resource_display_preference` object

| Field | Type | Required | Description |
|---|---|---|---|
| `overridable` | boolean |  | For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used. |
| `preference` | enum: `none`, `off`, `on` | yes | The account's display preference. |
| `value` | enum: `off`, `on` | yes | The effective display preference value. |

