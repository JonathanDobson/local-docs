# Stripe API 2023-10-16 — `portal_login_page` object

| Field | Type | Required | Description |
|---|---|---|---|
| `enabled` | boolean | yes | If `true`, a shareable `url` will be generated that will take your customers to a hosted login page for the customer portal.<br>If `false`, the previously generated `url`, if any, will be deactivated. |
| `url` | string |  | A shareable URL to the hosted portal login page. Your customers will be able to log in with their [email](https://stripe.com/docs/api/customers/object#customer_object-email) and receive a link to their customer portal. |

