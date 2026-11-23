# Stripe API 2023-10-16 — `account_capabilities` object

| Field | Type | Required | Description |
|---|---|---|---|
| `acss_debit_payments` | enum: `active`, `inactive`, `pending` |  | The status of the Canadian pre-authorized debits payments capability of the account, or whether the account can directly process Canadian pre-authorized debits charges. |
| `affirm_payments` | enum: `active`, `inactive`, `pending` |  | The status of the Affirm capability of the account, or whether the account can directly process Affirm charges. |
| `afterpay_clearpay_payments` | enum: `active`, `inactive`, `pending` |  | The status of the Afterpay Clearpay capability of the account, or whether the account can directly process Afterpay Clearpay charges. |
| `amazon_pay_payments` | enum: `active`, `inactive`, `pending` |  | The status of the AmazonPay capability of the account, or whether the account can directly process AmazonPay payments. |
| `au_becs_debit_payments` | enum: `active`, `inactive`, `pending` |  | The status of the BECS Direct Debit (AU) payments capability of the account, or whether the account can directly process BECS Direct Debit (AU) charges. |
| `bacs_debit_payments` | enum: `active`, `inactive`, `pending` |  | The status of the Bacs Direct Debits payments capability of the account, or whether the account can directly process Bacs Direct Debits charges. |
| `bancontact_payments` | enum: `active`, `inactive`, `pending` |  | The status of the Bancontact payments capability of the account, or whether the account can directly process Bancontact charges. |
| `bank_transfer_payments` | enum: `active`, `inactive`, `pending` |  | The status of the customer_balance payments capability of the account, or whether the account can directly process customer_balance charges. |
| `blik_payments` | enum: `active`, `inactive`, `pending` |  | The status of the blik payments capability of the account, or whether the account can directly process blik charges. |
| `boleto_payments` | enum: `active`, `inactive`, `pending` |  | The status of the boleto payments capability of the account, or whether the account can directly process boleto charges. |
| `card_issuing` | enum: `active`, `inactive`, `pending` |  | The status of the card issuing capability of the account, or whether you can use Issuing to distribute funds on cards |
| `card_payments` | enum: `active`, `inactive`, `pending` |  | The status of the card payments capability of the account, or whether the account can directly process credit and debit card charges. |
| `cartes_bancaires_payments` | enum: `active`, `inactive`, `pending` |  | The status of the Cartes Bancaires payments capability of the account, or whether the account can directly process Cartes Bancaires card charges in EUR currency. |
| `cashapp_payments` | enum: `active`, `inactive`, `pending` |  | The status of the Cash App Pay capability of the account, or whether the account can directly process Cash App Pay payments. |
| `eps_payments` | enum: `active`, `inactive`, `pending` |  | The status of the EPS payments capability of the account, or whether the account can directly process EPS charges. |
| `fpx_payments` | enum: `active`, `inactive`, `pending` |  | The status of the FPX payments capability of the account, or whether the account can directly process FPX charges. |
| `giropay_payments` | enum: `active`, `inactive`, `pending` |  | The status of the giropay payments capability of the account, or whether the account can directly process giropay charges. |
| `grabpay_payments` | enum: `active`, `inactive`, `pending` |  | The status of the GrabPay payments capability of the account, or whether the account can directly process GrabPay charges. |
| `ideal_payments` | enum: `active`, `inactive`, `pending` |  | The status of the iDEAL payments capability of the account, or whether the account can directly process iDEAL charges. |
| `india_international_payments` | enum: `active`, `inactive`, `pending` |  | The status of the india_international_payments capability of the account, or whether the account can process international charges (non INR) in India. |
| `jcb_payments` | enum: `active`, `inactive`, `pending` |  | The status of the JCB payments capability of the account, or whether the account (Japan only) can directly process JCB credit card charges in JPY currency. |
| `klarna_payments` | enum: `active`, `inactive`, `pending` |  | The status of the Klarna payments capability of the account, or whether the account can directly process Klarna charges. |
| `konbini_payments` | enum: `active`, `inactive`, `pending` |  | The status of the konbini payments capability of the account, or whether the account can directly process konbini charges. |
| `legacy_payments` | enum: `active`, `inactive`, `pending` |  | The status of the legacy payments capability of the account. |
| `link_payments` | enum: `active`, `inactive`, `pending` |  | The status of the link_payments capability of the account, or whether the account can directly process Link charges. |
| `mobilepay_payments` | enum: `active`, `inactive`, `pending` |  | The status of the MobilepPay capability of the account, or whether the account can directly process MobilePay charges. |
| `oxxo_payments` | enum: `active`, `inactive`, `pending` |  | The status of the OXXO payments capability of the account, or whether the account can directly process OXXO charges. |
| `p24_payments` | enum: `active`, `inactive`, `pending` |  | The status of the P24 payments capability of the account, or whether the account can directly process P24 charges. |
| `paynow_payments` | enum: `active`, `inactive`, `pending` |  | The status of the paynow payments capability of the account, or whether the account can directly process paynow charges. |
| `promptpay_payments` | enum: `active`, `inactive`, `pending` |  | The status of the promptpay payments capability of the account, or whether the account can directly process promptpay charges. |
| `revolut_pay_payments` | enum: `active`, `inactive`, `pending` |  | The status of the RevolutPay capability of the account, or whether the account can directly process RevolutPay payments. |
| `sepa_debit_payments` | enum: `active`, `inactive`, `pending` |  | The status of the SEPA Direct Debits payments capability of the account, or whether the account can directly process SEPA Direct Debits charges. |
| `sofort_payments` | enum: `active`, `inactive`, `pending` |  | The status of the Sofort payments capability of the account, or whether the account can directly process Sofort charges. |
| `swish_payments` | enum: `active`, `inactive`, `pending` |  | The status of the Swish capability of the account, or whether the account can directly process Swish payments. |
| `tax_reporting_us_1099_k` | enum: `active`, `inactive`, `pending` |  | The status of the tax reporting 1099-K (US) capability of the account. |
| `tax_reporting_us_1099_misc` | enum: `active`, `inactive`, `pending` |  | The status of the tax reporting 1099-MISC (US) capability of the account. |
| `transfers` | enum: `active`, `inactive`, `pending` |  | The status of the transfers capability of the account, or whether your platform can transfer funds to the account. |
| `treasury` | enum: `active`, `inactive`, `pending` |  | The status of the banking capability, or whether the account can have bank accounts. |
| `us_bank_account_ach_payments` | enum: `active`, `inactive`, `pending` |  | The status of the US bank account ACH payments capability of the account, or whether the account can directly process US bank account charges. |
| `zip_payments` | enum: `active`, `inactive`, `pending` |  | The status of the Zip capability of the account, or whether the account can directly process Zip charges. |

