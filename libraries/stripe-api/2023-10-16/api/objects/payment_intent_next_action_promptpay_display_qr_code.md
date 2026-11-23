# Stripe API 2023-10-16 — `payment_intent_next_action_promptpay_display_qr_code` object

| Field | Type | Required | Description |
|---|---|---|---|
| `data` | string | yes | The raw data string used to generate QR code, it should be used together with QR code library. |
| `hosted_instructions_url` | string | yes | The URL to the hosted PromptPay instructions page, which allows customers to view the PromptPay QR code. |
| `image_url_png` | string | yes | The PNG path used to render the QR code, can be used as the source in an HTML img tag |
| `image_url_svg` | string | yes | The SVG path used to render the QR code, can be used as the source in an HTML img tag |

