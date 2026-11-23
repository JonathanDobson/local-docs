# Stripe API 2023-10-16 — `tax_product_resource_jurisdiction` object

| Field | Type | Required | Description |
|---|---|---|---|
| `country` | string | yes | Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)). |
| `display_name` | string | yes | A human-readable name for the jurisdiction imposing the tax. |
| `level` | enum: `city`, `country`, `county`, `district`, `state` | yes | Indicates the level of the jurisdiction imposing the tax. |
| `state` | string |  | [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2:US), without country prefix. For example, "NY" for New York, United States. |

