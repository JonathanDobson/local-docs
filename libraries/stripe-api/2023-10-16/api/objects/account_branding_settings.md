# Stripe API 2023-10-16 — `account_branding_settings` object

Expandable fields (pass `expand[]=<field>`): `icon`, `logo`

| Field | Type | Required | Description |
|---|---|---|---|
| `icon` | string or `file` |  | (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) An icon for the account. Must be square and at least 128px x 128px. |
| `logo` | string or `file` |  | (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) A logo for the account that will be used in Checkout instead of the icon and without the account's name next to it if provided. Must be at least 128px x 128px. |
| `primary_color` | string |  | A CSS hex color value representing the primary branding color for this account |
| `secondary_color` | string |  | A CSS hex color value representing the secondary branding color for this account |

