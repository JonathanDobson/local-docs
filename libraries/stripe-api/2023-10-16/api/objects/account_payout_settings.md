# Stripe API 2023-10-16 — `account_payout_settings` object

Expandable fields (pass `expand[]=<field>`): `schedule`

| Field | Type | Required | Description |
|---|---|---|---|
| `debit_negative_balances` | boolean | yes | A Boolean indicating if Stripe should try to reclaim negative balances from an attached bank account. See our [Understanding Connect Account Balances](https://stripe.com/docs/connect/account-balances) documentation for details. Default value is `false` for Custom accounts, otherwise `true`. |
| `schedule` | `transfer_schedule` | yes |  |
| `statement_descriptor` | string |  | The text that appears on the bank account statement for payouts. If not set, this defaults to the platform's bank descriptor as set in the Dashboard. |

