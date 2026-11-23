# Stripe API 2023-10-16 — `transfer_schedule` object

| Field | Type | Required | Description |
|---|---|---|---|
| `delay_days` | integer | yes | The number of days charges for the account will be held before being paid out. |
| `interval` | string | yes | How frequently funds will be paid out. One of `manual` (payouts only created via API call), `daily`, `weekly`, or `monthly`. |
| `monthly_anchor` | integer |  | The day of the month funds will be paid out. Only shown if `interval` is monthly. Payouts scheduled between the 29th and 31st of the month are sent on the last day of shorter months. |
| `weekly_anchor` | string |  | The day of the week funds will be paid out, of the style 'monday', 'tuesday', etc. Only shown if `interval` is weekly. |

