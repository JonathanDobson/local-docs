# Stripe API 2023-10-16 — `payment_pages_checkout_session_consent_collection` object

Expandable fields (pass `expand[]=<field>`): `payment_method_reuse_agreement`

| Field | Type | Required | Description |
|---|---|---|---|
| `payment_method_reuse_agreement` | `payment_pages_checkout_session_payment_method_reuse_agreement` |  | If set to `hidden`, it will hide legal text related to the reuse of a payment method. |
| `promotions` | enum: `auto`, `none` |  | If set to `auto`, enables the collection of customer consent for promotional communications. The Checkout Session will determine whether to display an option to opt into promotional communication from the merchant depending on the customer's locale. Only available to US merchants. |
| `terms_of_service` | enum: `none`, `required` |  | If set to `required`, it requires customers to accept the terms of service before being able to pay. |

