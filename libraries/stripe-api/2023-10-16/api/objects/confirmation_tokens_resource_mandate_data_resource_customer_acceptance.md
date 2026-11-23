# Stripe API 2023-10-16 — `confirmation_tokens_resource_mandate_data_resource_customer_acceptance` object

This hash contains details about the customer acceptance of the Mandate.

Expandable fields (pass `expand[]=<field>`): `online`

| Field | Type | Required | Description |
|---|---|---|---|
| `online` | `confirmation_tokens_resource_mandate_data_resource_customer_acceptance_resource_online` |  | If this is a Mandate accepted online, this hash contains details about the online acceptance. |
| `type` | string | yes | The type of customer acceptance information included with the Mandate. |

