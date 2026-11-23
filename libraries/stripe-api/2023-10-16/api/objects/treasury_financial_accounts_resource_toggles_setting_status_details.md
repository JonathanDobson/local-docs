# Stripe API 2023-10-16 — `treasury_financial_accounts_resource_toggles_setting_status_details` object

Additional details on the FinancialAccount Features information.

| Field | Type | Required | Description |
|---|---|---|---|
| `code` | enum: `activating`, `capability_not_requested`, `financial_account_closed`, `rejected_other`, `rejected_unsupported_business`, `requirements_past_due`, `requirements_pending_verification`, `restricted_by_platform`, `restricted_other` | yes | Represents the reason why the status is `pending` or `restricted`. |
| `resolution` | enum: `contact_stripe`, `provide_information`, `remove_restriction` |  | Represents what the user should do, if anything, to activate the Feature. |
| `restriction` | enum: `inbound_flows`, `outbound_flows` |  | The `platform_restrictions` that are restricting this Feature. |

