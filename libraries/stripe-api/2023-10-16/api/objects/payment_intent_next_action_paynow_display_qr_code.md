# Stripe API 2023-10-16 — `payment_intent_next_action_paynow_display_qr_code` object

| Field | Type | Required | Description |
|---|---|---|---|
| `data` | string | yes | The raw data string used to generate QR code, it should be used together with QR code library. |
| `hosted_instructions_url` | string |  | The URL to the hosted PayNow instructions page, which allows customers to view the PayNow QR code. |
| `image_url_png` | string | yes | The image_url_png string used to render QR code |
| `image_url_svg` | string | yes | The image_url_svg string used to render QR code |

