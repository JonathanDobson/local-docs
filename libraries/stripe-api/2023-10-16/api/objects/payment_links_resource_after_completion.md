# Stripe API 2023-10-16 — `payment_links_resource_after_completion` object

Expandable fields (pass `expand[]=<field>`): `hosted_confirmation`, `redirect`

| Field | Type | Required | Description |
|---|---|---|---|
| `hosted_confirmation` | `payment_links_resource_completion_behavior_confirmation_page` |  |  |
| `redirect` | `payment_links_resource_completion_behavior_redirect` |  |  |
| `type` | enum: `hosted_confirmation`, `redirect` | yes | The specified behavior after the purchase is complete. |

