# Stripe API 2023-10-16 — `payment_links_resource_consent_collection` object

Expandable fields (pass `expand[]=<field>`): `payment_method_reuse_agreement`

| Field | Type | Required | Description |
|---|---|---|---|
| `payment_method_reuse_agreement` | `payment_links_resource_payment_method_reuse_agreement` |  | Settings related to the payment method reuse text shown in the Checkout UI. |
| `promotions` | enum: `auto`, `none` |  | If set to `auto`, enables the collection of customer consent for promotional communications. |
| `terms_of_service` | enum: `none`, `required` |  | If set to `required`, it requires cutomers to accept the terms of service before being able to pay. If set to `none`, customers won't be shown a checkbox to accept the terms of service. |

