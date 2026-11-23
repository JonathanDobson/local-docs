# Stripe API 2023-10-16 — `treasury_financial_accounts_resource_platform_restrictions` object

Restrictions that a Connect Platform has placed on this FinancialAccount.

| Field | Type | Required | Description |
|---|---|---|---|
| `inbound_flows` | enum: `restricted`, `unrestricted` |  | Restricts all inbound money movement. |
| `outbound_flows` | enum: `restricted`, `unrestricted` |  | Restricts all outbound money movement. |

