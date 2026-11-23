# Stripe API 2023-10-16 — `tax_product_resource_postal_address` object

| Field | Type | Required | Description |
|---|---|---|---|
| `city` | string |  | City, district, suburb, town, or village. |
| `country` | string | yes | Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)). |
| `line1` | string |  | Address line 1 (e.g., street, PO Box, or company name). |
| `line2` | string |  | Address line 2 (e.g., apartment, suite, unit, or building). |
| `postal_code` | string |  | ZIP or postal code. |
| `state` | string |  | State/province as an [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) subdivision code, without country prefix. Example: "NY" or "TX". |

