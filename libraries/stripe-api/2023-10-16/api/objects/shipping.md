# Stripe API 2023-10-16 — `shipping` object

Expandable fields (pass `expand[]=<field>`): `address`

| Field | Type | Required | Description |
|---|---|---|---|
| `address` | `address` |  |  |
| `carrier` | string |  | The delivery service that shipped a physical product, such as Fedex, UPS, USPS, etc. |
| `name` | string |  | Recipient name. |
| `phone` | string |  | Recipient phone (including extension). |
| `tracking_number` | string |  | The tracking number for a physical product, obtained from the delivery service. If multiple tracking numbers were generated for this purchase, please separate them with commas. |

