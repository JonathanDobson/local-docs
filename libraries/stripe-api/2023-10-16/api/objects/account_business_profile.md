# Stripe API 2023-10-16 — `account_business_profile` object

Expandable fields (pass `expand[]=<field>`): `annual_revenue`, `monthly_estimated_revenue`, `support_address`

| Field | Type | Required | Description |
|---|---|---|---|
| `annual_revenue` | `account_annual_revenue` |  | The applicant's gross annual revenue for its preceding fiscal year. |
| `estimated_worker_count` | integer |  | An estimated upper bound of employees, contractors, vendors, etc. currently working for the business. |
| `mcc` | string |  | [The merchant category code for the account](https://stripe.com/docs/connect/setting-mcc). MCCs are used to classify businesses based on the goods or services they provide. |
| `monthly_estimated_revenue` | `account_monthly_estimated_revenue` |  |  |
| `name` | string |  | The customer-facing business name. |
| `product_description` | string |  | Internal-only description of the product sold or service provided by the business. It's used by Stripe for risk and underwriting purposes. |
| `support_address` | `address` |  | A publicly available mailing address for sending support issues to. |
| `support_email` | string |  | A publicly available email address for sending support issues to. |
| `support_phone` | string |  | A publicly available phone number to call with support issues. |
| `support_url` | string |  | A publicly available website for handling support issues. |
| `url` | string |  | The business's publicly available website. |

