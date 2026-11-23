# Stripe API 2023-10-16 — `payment_method_domain_resource_payment_method_status` object

Indicates the status of a specific payment method on a payment method domain.

Expandable fields (pass `expand[]=<field>`): `status_details`

| Field | Type | Required | Description |
|---|---|---|---|
| `status` | enum: `active`, `inactive` | yes | The status of the payment method on the domain. |
| `status_details` | `payment_method_domain_resource_payment_method_status_details` |  |  |

