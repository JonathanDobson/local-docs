# Stripe API 2023-10-16 — `portal_flows_flow_after_completion` object

Expandable fields (pass `expand[]=<field>`): `hosted_confirmation`, `redirect`

| Field | Type | Required | Description |
|---|---|---|---|
| `hosted_confirmation` | `portal_flows_after_completion_hosted_confirmation` |  | Configuration when `after_completion.type=hosted_confirmation`. |
| `redirect` | `portal_flows_after_completion_redirect` |  | Configuration when `after_completion.type=redirect`. |
| `type` | enum: `hosted_confirmation`, `portal_homepage`, `redirect` | yes | The specified type of behavior after the flow is completed. |

