# Stripe API 2023-10-16 — payment method configurations

Operations under `/v1/payment_method_configurations` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/payment_method_configurations

operationId: `GetPaymentMethodConfigurations`

List payment method configurations

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `application` | string or "" (to unset) |  | The Connect application to filter by. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: object

## POST /v1/payment_method_configurations

operationId: `PostPaymentMethodConfigurations`

Creates a payment method configuration

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `acss_debit` | object |  | Canadian pre-authorized debit payments, check this [page](https://stripe.com/docs/payments/acss-debit) for more details like country availability. |
| `acss_debit.display_preference` | object |  |  |
| `acss_debit.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `affirm` | object |  | [Affirm](https://www.affirm.com/) gives your customers a way to split purchases over a series of payments. Depending on the purchase, they can pay with four interest-free payments (Split Pay) or pay over a longer term (Installments), which might include interest. Check this [page](https://stripe.com/docs/payments/affirm) for more details like country availability. |
| `affirm.display_preference` | object |  |  |
| `affirm.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `afterpay_clearpay` | object |  | Afterpay gives your customers a way to pay for purchases in installments, check this [page](https://stripe.com/docs/payments/afterpay-clearpay) for more details like country availability. Afterpay is particularly popular among businesses selling fashion, beauty, and sports products. |
| `afterpay_clearpay.display_preference` | object |  |  |
| `afterpay_clearpay.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `alipay` | object |  | Alipay is a digital wallet in China that has more than a billion active users worldwide. Alipay users can pay on the web or on a mobile device using login credentials or their Alipay app. Alipay has a low dispute rate and reduces fraud by authenticating payments using the customer's login credentials. Check this [page](https://stripe.com/docs/payments/alipay) for more details. |
| `alipay.display_preference` | object |  |  |
| `alipay.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `apple_pay` | object |  | Stripe users can accept [Apple Pay](/payments/apple-pay) in iOS applications in iOS 9 and later, and on the web in Safari starting with iOS 10 or macOS Sierra. There are no additional fees to process Apple Pay payments, and the [pricing](/pricing) is the same as other card transactions. Check this [page](https://stripe.com/docs/apple-pay) for more details. |
| `apple_pay.display_preference` | object |  |  |
| `apple_pay.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `apple_pay_later` | object |  | Apple Pay Later, a payment method for customers to buy now and pay later, gives your customers a way to split purchases into four installments across six weeks. |
| `apple_pay_later.display_preference` | object |  |  |
| `apple_pay_later.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `au_becs_debit` | object |  | Stripe users in Australia can accept Bulk Electronic Clearing System (BECS) direct debit payments from customers with an Australian bank account. Check this [page](https://stripe.com/docs/payments/au-becs-debit) for more details. |
| `au_becs_debit.display_preference` | object |  |  |
| `au_becs_debit.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `bacs_debit` | object |  | Stripe users in the UK can accept Bacs Direct Debit payments from customers with a UK bank account, check this [page](https://stripe.com/docs/payments/payment-methods/bacs-debit) for more details. |
| `bacs_debit.display_preference` | object |  |  |
| `bacs_debit.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `bancontact` | object |  | Bancontact is the most popular online payment method in Belgium, with over 15 million cards in circulation. [Customers](https://stripe.com/docs/api/customers) use a Bancontact card or mobile app linked to a Belgian bank account to make online payments that are secure, guaranteed, and confirmed immediately. Check this [page](https://stripe.com/docs/payments/bancontact) for more details. |
| `bancontact.display_preference` | object |  |  |
| `bancontact.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `blik` | object |  | BLIK is a [single use](https://stripe.com/docs/payments/payment-methods#usage) payment method that requires customers to authenticate their payments. When customers want to pay online using BLIK, they request a six-digit code from their banking application and enter it into the payment collection form. Check this [page](https://stripe.com/docs/payments/blik) for more details. |
| `blik.display_preference` | object |  |  |
| `blik.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `boleto` | object |  | Boleto is an official (regulated by the Central Bank of Brazil) payment method in Brazil. Check this [page](https://stripe.com/docs/payments/boleto) for more details. |
| `boleto.display_preference` | object |  |  |
| `boleto.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `card` | object |  | Cards are a popular way for consumers and businesses to pay online or in person. Stripe supports global and local card networks. |
| `card.display_preference` | object |  |  |
| `card.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `cartes_bancaires` | object |  | Cartes Bancaires is France's local card network. More than 95% of these cards are co-branded with either Visa or Mastercard, meaning you can process these cards over either Cartes Bancaires or the Visa or Mastercard networks. Check this [page](https://stripe.com/docs/payments/cartes-bancaires) for more details. |
| `cartes_bancaires.display_preference` | object |  |  |
| `cartes_bancaires.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `cashapp` | object |  | Cash App is a popular consumer app in the US that allows customers to bank, invest, send, and receive money using their digital wallet. Check this [page](https://stripe.com/docs/payments/cash-app-pay) for more details. |
| `cashapp.display_preference` | object |  |  |
| `cashapp.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `customer_balance` | object |  | Uses a customer’s [cash balance](https://stripe.com/docs/payments/customer-balance) for the payment. The cash balance can be funded via a bank transfer. Check this [page](https://stripe.com/docs/payments/bank-transfers) for more details. |
| `customer_balance.display_preference` | object |  |  |
| `customer_balance.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `eps` | object |  | EPS is an Austria-based payment method that allows customers to complete transactions online using their bank credentials. EPS is supported by all Austrian banks and is accepted by over 80% of Austrian online retailers. Check this [page](https://stripe.com/docs/payments/eps) for more details. |
| `eps.display_preference` | object |  |  |
| `eps.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `fpx` | object |  | Financial Process Exchange (FPX) is a Malaysia-based payment method that allows customers to complete transactions online using their bank credentials. Bank Negara Malaysia (BNM), the Central Bank of Malaysia, and eleven other major Malaysian financial institutions are members of the PayNet Group, which owns and operates FPX. It is one of the most popular online payment methods in Malaysia, with nearly 90 million transactions in 2018 according to BNM. Check this [page](https://stripe.com/docs/payments/fpx) for more details. |
| `fpx.display_preference` | object |  |  |
| `fpx.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `giropay` | object |  | giropay is a German payment method based on online banking, introduced in 2006. It allows customers to complete transactions online using their online banking environment, with funds debited from their bank account. Depending on their bank, customers confirm payments on giropay using a second factor of authentication or a PIN. giropay accounts for 10% of online checkouts in Germany. Check this [page](https://stripe.com/docs/payments/giropay) for more details. |
| `giropay.display_preference` | object |  |  |
| `giropay.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `google_pay` | object |  | Google Pay allows customers to make payments in your app or website using any credit or debit card saved to their Google Account, including those from Google Play, YouTube, Chrome, or an Android device. Use the Google Pay API to request any credit or debit card stored in your customer's Google account. Check this [page](https://stripe.com/docs/google-pay) for more details. |
| `google_pay.display_preference` | object |  |  |
| `google_pay.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `grabpay` | object |  | GrabPay is a payment method developed by [Grab](https://www.grab.com/sg/consumer/finance/pay/). GrabPay is a digital wallet - customers maintain a balance in their wallets that they pay out with. Check this [page](https://stripe.com/docs/payments/grabpay) for more details. |
| `grabpay.display_preference` | object |  |  |
| `grabpay.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `ideal` | object |  | iDEAL is a Netherlands-based payment method that allows customers to complete transactions online using their bank credentials. All major Dutch banks are members of Currence, the scheme that operates iDEAL, making it the most popular online payment method in the Netherlands with a share of online transactions close to 55%. Check this [page](https://stripe.com/docs/payments/ideal) for more details. |
| `ideal.display_preference` | object |  |  |
| `ideal.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `jcb` | object |  | JCB is a credit card company based in Japan. JCB is currently available in Japan to businesses approved by JCB, and available to all businesses in Australia, Canada, Hong Kong, Japan, New Zealand, Singapore, Switzerland, United Kingdom, United States, and all countries in the European Economic Area except Iceland. Check this [page](https://support.stripe.com/questions/accepting-japan-credit-bureau-%28jcb%29-payments) for more details. |
| `jcb.display_preference` | object |  |  |
| `jcb.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `klarna` | object |  | Klarna gives customers a range of [payment options](https://stripe.com/docs/payments/klarna#payment-options) during checkout. Available payment options vary depending on the customer's billing address and the transaction amount. These payment options make it convenient for customers to purchase items in all price ranges. Check this [page](https://stripe.com/docs/payments/klarna) for more details. |
| `klarna.display_preference` | object |  |  |
| `klarna.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `konbini` | object |  | Konbini allows customers in Japan to pay for bills and online purchases at convenience stores with cash. Check this [page](https://stripe.com/docs/payments/konbini) for more details. |
| `konbini.display_preference` | object |  |  |
| `konbini.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `link` | object |  | [Link](https://stripe.com/docs/payments/link) is a payment method network. With Link, users save their payment details once, then reuse that information to pay with one click for any business on the network. |
| `link.display_preference` | object |  |  |
| `link.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `name` | string |  | Configuration name. |
| `oxxo` | object |  | OXXO is a Mexican chain of convenience stores with thousands of locations across Latin America and represents nearly 20% of online transactions in Mexico. OXXO allows customers to pay bills and online purchases in-store with cash. Check this [page](https://stripe.com/docs/payments/oxxo) for more details. |
| `oxxo.display_preference` | object |  |  |
| `oxxo.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `p24` | object |  | Przelewy24 is a Poland-based payment method aggregator that allows customers to complete transactions online using bank transfers and other methods. Bank transfers account for 30% of online payments in Poland and Przelewy24 provides a way for customers to pay with over 165 banks. Check this [page](https://stripe.com/docs/payments/p24) for more details. |
| `p24.display_preference` | object |  |  |
| `p24.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `parent` | string |  | Configuration's parent configuration. Specify to create a child configuration. |
| `paynow` | object |  | PayNow is a Singapore-based payment method that allows customers to make a payment using their preferred app from participating banks and participating non-bank financial institutions. Check this [page](https://stripe.com/docs/payments/paynow) for more details. |
| `paynow.display_preference` | object |  |  |
| `paynow.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `paypal` | object |  | PayPal, a digital wallet popular with customers in Europe, allows your customers worldwide to pay using their PayPal account. Check this [page](https://stripe.com/docs/payments/paypal) for more details. |
| `paypal.display_preference` | object |  |  |
| `paypal.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `promptpay` | object |  | PromptPay is a Thailand-based payment method that allows customers to make a payment using their preferred app from participating banks. Check this [page](https://stripe.com/docs/payments/promptpay) for more details. |
| `promptpay.display_preference` | object |  |  |
| `promptpay.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `revolut_pay` | object |  | Revolut Pay, developed by Revolut, a global finance app, is a digital wallet payment method. Revolut Pay uses the customer’s stored balance or cards to fund the payment, and offers the option for non-Revolut customers to save their details after their first purchase. |
| `revolut_pay.display_preference` | object |  |  |
| `revolut_pay.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `sepa_debit` | object |  | The [Single Euro Payments Area (SEPA)](https://en.wikipedia.org/wiki/Single_Euro_Payments_Area) is an initiative of the European Union to simplify payments within and across member countries. SEPA established and enforced banking standards to allow for the direct debiting of every EUR-denominated bank account within the SEPA region, check this [page](https://stripe.com/docs/payments/sepa-debit) for more details. |
| `sepa_debit.display_preference` | object |  |  |
| `sepa_debit.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `sofort` | object |  | Stripe users in Europe and the United States can use the [Payment Intents API](https://stripe.com/docs/payments/payment-intents)—a single integration path for creating payments using any supported method—to accept [Sofort](https://www.sofort.com/) payments from customers. Check this [page](https://stripe.com/docs/payments/sofort) for more details. |
| `sofort.display_preference` | object |  |  |
| `sofort.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `us_bank_account` | object |  | Stripe users in the United States can accept ACH direct debit payments from customers with a US bank account using the Automated Clearing House (ACH) payments system operated by Nacha. Check this [page](https://stripe.com/docs/payments/ach-debit) for more details. |
| `us_bank_account.display_preference` | object |  |  |
| `us_bank_account.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `wechat_pay` | object |  | WeChat, owned by Tencent, is China's leading mobile app with over 1 billion monthly active users. Chinese consumers can use WeChat Pay to pay for goods and services inside of businesses' apps and websites. WeChat Pay users buy most frequently in gaming, e-commerce, travel, online education, and food/nutrition. Check this [page](https://stripe.com/docs/payments/wechat-pay) for more details. |
| `wechat_pay.display_preference` | object |  |  |
| `wechat_pay.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `zip` | object |  | Zip gives your customers a way to split purchases over a series of payments. Check this [page](https://stripe.com/docs/payments/zip) for more details like country availability. |
| `zip.display_preference` | object |  |  |
| `zip.display_preference.preference` | enum: `none`, `off`, `on` |  |  |

Returns: `payment_method_configuration`

## GET /v1/payment_method_configurations/{configuration}

operationId: `GetPaymentMethodConfigurationsConfiguration`

Retrieve payment method configuration

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `configuration (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `payment_method_configuration`

## POST /v1/payment_method_configurations/{configuration}

operationId: `PostPaymentMethodConfigurationsConfiguration`

Update payment method configuration

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `configuration (path)` | string | yes |  |
| `acss_debit` | object |  | Canadian pre-authorized debit payments, check this [page](https://stripe.com/docs/payments/acss-debit) for more details like country availability. |
| `acss_debit.display_preference` | object |  |  |
| `acss_debit.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `active` | boolean |  | Whether the configuration can be used for new payments. |
| `affirm` | object |  | [Affirm](https://www.affirm.com/) gives your customers a way to split purchases over a series of payments. Depending on the purchase, they can pay with four interest-free payments (Split Pay) or pay over a longer term (Installments), which might include interest. Check this [page](https://stripe.com/docs/payments/affirm) for more details like country availability. |
| `affirm.display_preference` | object |  |  |
| `affirm.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `afterpay_clearpay` | object |  | Afterpay gives your customers a way to pay for purchases in installments, check this [page](https://stripe.com/docs/payments/afterpay-clearpay) for more details like country availability. Afterpay is particularly popular among businesses selling fashion, beauty, and sports products. |
| `afterpay_clearpay.display_preference` | object |  |  |
| `afterpay_clearpay.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `alipay` | object |  | Alipay is a digital wallet in China that has more than a billion active users worldwide. Alipay users can pay on the web or on a mobile device using login credentials or their Alipay app. Alipay has a low dispute rate and reduces fraud by authenticating payments using the customer's login credentials. Check this [page](https://stripe.com/docs/payments/alipay) for more details. |
| `alipay.display_preference` | object |  |  |
| `alipay.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `apple_pay` | object |  | Stripe users can accept [Apple Pay](/payments/apple-pay) in iOS applications in iOS 9 and later, and on the web in Safari starting with iOS 10 or macOS Sierra. There are no additional fees to process Apple Pay payments, and the [pricing](/pricing) is the same as other card transactions. Check this [page](https://stripe.com/docs/apple-pay) for more details. |
| `apple_pay.display_preference` | object |  |  |
| `apple_pay.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `apple_pay_later` | object |  | Apple Pay Later, a payment method for customers to buy now and pay later, gives your customers a way to split purchases into four installments across six weeks. |
| `apple_pay_later.display_preference` | object |  |  |
| `apple_pay_later.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `au_becs_debit` | object |  | Stripe users in Australia can accept Bulk Electronic Clearing System (BECS) direct debit payments from customers with an Australian bank account. Check this [page](https://stripe.com/docs/payments/au-becs-debit) for more details. |
| `au_becs_debit.display_preference` | object |  |  |
| `au_becs_debit.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `bacs_debit` | object |  | Stripe users in the UK can accept Bacs Direct Debit payments from customers with a UK bank account, check this [page](https://stripe.com/docs/payments/payment-methods/bacs-debit) for more details. |
| `bacs_debit.display_preference` | object |  |  |
| `bacs_debit.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `bancontact` | object |  | Bancontact is the most popular online payment method in Belgium, with over 15 million cards in circulation. [Customers](https://stripe.com/docs/api/customers) use a Bancontact card or mobile app linked to a Belgian bank account to make online payments that are secure, guaranteed, and confirmed immediately. Check this [page](https://stripe.com/docs/payments/bancontact) for more details. |
| `bancontact.display_preference` | object |  |  |
| `bancontact.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `blik` | object |  | BLIK is a [single use](https://stripe.com/docs/payments/payment-methods#usage) payment method that requires customers to authenticate their payments. When customers want to pay online using BLIK, they request a six-digit code from their banking application and enter it into the payment collection form. Check this [page](https://stripe.com/docs/payments/blik) for more details. |
| `blik.display_preference` | object |  |  |
| `blik.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `boleto` | object |  | Boleto is an official (regulated by the Central Bank of Brazil) payment method in Brazil. Check this [page](https://stripe.com/docs/payments/boleto) for more details. |
| `boleto.display_preference` | object |  |  |
| `boleto.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `card` | object |  | Cards are a popular way for consumers and businesses to pay online or in person. Stripe supports global and local card networks. |
| `card.display_preference` | object |  |  |
| `card.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `cartes_bancaires` | object |  | Cartes Bancaires is France's local card network. More than 95% of these cards are co-branded with either Visa or Mastercard, meaning you can process these cards over either Cartes Bancaires or the Visa or Mastercard networks. Check this [page](https://stripe.com/docs/payments/cartes-bancaires) for more details. |
| `cartes_bancaires.display_preference` | object |  |  |
| `cartes_bancaires.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `cashapp` | object |  | Cash App is a popular consumer app in the US that allows customers to bank, invest, send, and receive money using their digital wallet. Check this [page](https://stripe.com/docs/payments/cash-app-pay) for more details. |
| `cashapp.display_preference` | object |  |  |
| `cashapp.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `customer_balance` | object |  | Uses a customer’s [cash balance](https://stripe.com/docs/payments/customer-balance) for the payment. The cash balance can be funded via a bank transfer. Check this [page](https://stripe.com/docs/payments/bank-transfers) for more details. |
| `customer_balance.display_preference` | object |  |  |
| `customer_balance.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `eps` | object |  | EPS is an Austria-based payment method that allows customers to complete transactions online using their bank credentials. EPS is supported by all Austrian banks and is accepted by over 80% of Austrian online retailers. Check this [page](https://stripe.com/docs/payments/eps) for more details. |
| `eps.display_preference` | object |  |  |
| `eps.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `fpx` | object |  | Financial Process Exchange (FPX) is a Malaysia-based payment method that allows customers to complete transactions online using their bank credentials. Bank Negara Malaysia (BNM), the Central Bank of Malaysia, and eleven other major Malaysian financial institutions are members of the PayNet Group, which owns and operates FPX. It is one of the most popular online payment methods in Malaysia, with nearly 90 million transactions in 2018 according to BNM. Check this [page](https://stripe.com/docs/payments/fpx) for more details. |
| `fpx.display_preference` | object |  |  |
| `fpx.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `giropay` | object |  | giropay is a German payment method based on online banking, introduced in 2006. It allows customers to complete transactions online using their online banking environment, with funds debited from their bank account. Depending on their bank, customers confirm payments on giropay using a second factor of authentication or a PIN. giropay accounts for 10% of online checkouts in Germany. Check this [page](https://stripe.com/docs/payments/giropay) for more details. |
| `giropay.display_preference` | object |  |  |
| `giropay.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `google_pay` | object |  | Google Pay allows customers to make payments in your app or website using any credit or debit card saved to their Google Account, including those from Google Play, YouTube, Chrome, or an Android device. Use the Google Pay API to request any credit or debit card stored in your customer's Google account. Check this [page](https://stripe.com/docs/google-pay) for more details. |
| `google_pay.display_preference` | object |  |  |
| `google_pay.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `grabpay` | object |  | GrabPay is a payment method developed by [Grab](https://www.grab.com/sg/consumer/finance/pay/). GrabPay is a digital wallet - customers maintain a balance in their wallets that they pay out with. Check this [page](https://stripe.com/docs/payments/grabpay) for more details. |
| `grabpay.display_preference` | object |  |  |
| `grabpay.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `ideal` | object |  | iDEAL is a Netherlands-based payment method that allows customers to complete transactions online using their bank credentials. All major Dutch banks are members of Currence, the scheme that operates iDEAL, making it the most popular online payment method in the Netherlands with a share of online transactions close to 55%. Check this [page](https://stripe.com/docs/payments/ideal) for more details. |
| `ideal.display_preference` | object |  |  |
| `ideal.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `jcb` | object |  | JCB is a credit card company based in Japan. JCB is currently available in Japan to businesses approved by JCB, and available to all businesses in Australia, Canada, Hong Kong, Japan, New Zealand, Singapore, Switzerland, United Kingdom, United States, and all countries in the European Economic Area except Iceland. Check this [page](https://support.stripe.com/questions/accepting-japan-credit-bureau-%28jcb%29-payments) for more details. |
| `jcb.display_preference` | object |  |  |
| `jcb.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `klarna` | object |  | Klarna gives customers a range of [payment options](https://stripe.com/docs/payments/klarna#payment-options) during checkout. Available payment options vary depending on the customer's billing address and the transaction amount. These payment options make it convenient for customers to purchase items in all price ranges. Check this [page](https://stripe.com/docs/payments/klarna) for more details. |
| `klarna.display_preference` | object |  |  |
| `klarna.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `konbini` | object |  | Konbini allows customers in Japan to pay for bills and online purchases at convenience stores with cash. Check this [page](https://stripe.com/docs/payments/konbini) for more details. |
| `konbini.display_preference` | object |  |  |
| `konbini.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `link` | object |  | [Link](https://stripe.com/docs/payments/link) is a payment method network. With Link, users save their payment details once, then reuse that information to pay with one click for any business on the network. |
| `link.display_preference` | object |  |  |
| `link.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `name` | string |  | Configuration name. |
| `oxxo` | object |  | OXXO is a Mexican chain of convenience stores with thousands of locations across Latin America and represents nearly 20% of online transactions in Mexico. OXXO allows customers to pay bills and online purchases in-store with cash. Check this [page](https://stripe.com/docs/payments/oxxo) for more details. |
| `oxxo.display_preference` | object |  |  |
| `oxxo.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `p24` | object |  | Przelewy24 is a Poland-based payment method aggregator that allows customers to complete transactions online using bank transfers and other methods. Bank transfers account for 30% of online payments in Poland and Przelewy24 provides a way for customers to pay with over 165 banks. Check this [page](https://stripe.com/docs/payments/p24) for more details. |
| `p24.display_preference` | object |  |  |
| `p24.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `paynow` | object |  | PayNow is a Singapore-based payment method that allows customers to make a payment using their preferred app from participating banks and participating non-bank financial institutions. Check this [page](https://stripe.com/docs/payments/paynow) for more details. |
| `paynow.display_preference` | object |  |  |
| `paynow.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `paypal` | object |  | PayPal, a digital wallet popular with customers in Europe, allows your customers worldwide to pay using their PayPal account. Check this [page](https://stripe.com/docs/payments/paypal) for more details. |
| `paypal.display_preference` | object |  |  |
| `paypal.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `promptpay` | object |  | PromptPay is a Thailand-based payment method that allows customers to make a payment using their preferred app from participating banks. Check this [page](https://stripe.com/docs/payments/promptpay) for more details. |
| `promptpay.display_preference` | object |  |  |
| `promptpay.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `revolut_pay` | object |  | Revolut Pay, developed by Revolut, a global finance app, is a digital wallet payment method. Revolut Pay uses the customer’s stored balance or cards to fund the payment, and offers the option for non-Revolut customers to save their details after their first purchase. |
| `revolut_pay.display_preference` | object |  |  |
| `revolut_pay.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `sepa_debit` | object |  | The [Single Euro Payments Area (SEPA)](https://en.wikipedia.org/wiki/Single_Euro_Payments_Area) is an initiative of the European Union to simplify payments within and across member countries. SEPA established and enforced banking standards to allow for the direct debiting of every EUR-denominated bank account within the SEPA region, check this [page](https://stripe.com/docs/payments/sepa-debit) for more details. |
| `sepa_debit.display_preference` | object |  |  |
| `sepa_debit.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `sofort` | object |  | Stripe users in Europe and the United States can use the [Payment Intents API](https://stripe.com/docs/payments/payment-intents)—a single integration path for creating payments using any supported method—to accept [Sofort](https://www.sofort.com/) payments from customers. Check this [page](https://stripe.com/docs/payments/sofort) for more details. |
| `sofort.display_preference` | object |  |  |
| `sofort.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `us_bank_account` | object |  | Stripe users in the United States can accept ACH direct debit payments from customers with a US bank account using the Automated Clearing House (ACH) payments system operated by Nacha. Check this [page](https://stripe.com/docs/payments/ach-debit) for more details. |
| `us_bank_account.display_preference` | object |  |  |
| `us_bank_account.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `wechat_pay` | object |  | WeChat, owned by Tencent, is China's leading mobile app with over 1 billion monthly active users. Chinese consumers can use WeChat Pay to pay for goods and services inside of businesses' apps and websites. WeChat Pay users buy most frequently in gaming, e-commerce, travel, online education, and food/nutrition. Check this [page](https://stripe.com/docs/payments/wechat-pay) for more details. |
| `wechat_pay.display_preference` | object |  |  |
| `wechat_pay.display_preference.preference` | enum: `none`, `off`, `on` |  |  |
| `zip` | object |  | Zip gives your customers a way to split purchases over a series of payments. Check this [page](https://stripe.com/docs/payments/zip) for more details like country availability. |
| `zip.display_preference` | object |  |  |
| `zip.display_preference.preference` | enum: `none`, `off`, `on` |  |  |

Returns: `payment_method_configuration`

# Objects returned

## The `payment_method_configuration` object

PaymentMethodConfigurations control which payment methods are displayed to your customers when you don't explicitly specify payment method types. You can have multiple configurations with different sets of payment methods for different scenarios.

There are two types of PaymentMethodConfigurations. Which is used depends on the [charge type](https://stripe.com/docs/connect/charges):

**Direct** configurations apply to payments created on your account, including Connect destination charges, Connect separate charges and transfers, and payments not involving Connect.

**Child** configurations apply to payments created on your connected accounts using direct charges, and charges with the on_behalf_of parameter.

Child configurations have a `parent` that sets default values and controls which settings connected accounts may override. You can specify a parent ID at payment time, and Stripe will automatically resolve the connected account’s associated child configuration. Parent configurations are [managed in the dashboard](https://dashboard.stripe.com/settings/payment_methods/connected_accounts) and are not available in this API.

Related guides:
- [Payment Method Configurations API](https://stripe.com/docs/connect/payment-method-configurations)
- [Multiple configurations on dynamic payment methods](https://stripe.com/docs/payments/multiple-payment-method-configs)
- [Multiple configurations for your Connect accounts](https://stripe.com/docs/connect/multiple-payment-method-configurations)

Expandable fields (pass `expand[]=<field>`): `acss_debit`, `affirm`, `afterpay_clearpay`, `alipay`, `apple_pay`, `au_becs_debit`, `bacs_debit`, `bancontact`, `blik`, `boleto`, `card`, `cartes_bancaires`, `cashapp`, `customer_balance`, `eps`, `fpx`, `giropay`, `google_pay`, `grabpay`, `ideal`, `jcb`, `klarna`, `konbini`, `link`, `oxxo`, `p24`, `paynow`, `paypal`, `promptpay`, `revolut_pay`, `sepa_debit`, `sofort`, `us_bank_account`, `wechat_pay`, `zip`

| Field | Type | Required | Description |
|---|---|---|---|
| `acss_debit` | `payment_method_config_resource_payment_method_properties` |  |  |
| `active` | boolean | yes | Whether the configuration can be used for new payments. |
| `affirm` | `payment_method_config_resource_payment_method_properties` |  |  |
| `afterpay_clearpay` | `payment_method_config_resource_payment_method_properties` |  |  |
| `alipay` | `payment_method_config_resource_payment_method_properties` |  |  |
| `apple_pay` | `payment_method_config_resource_payment_method_properties` |  |  |
| `application` | string |  | For child configs, the Connect application associated with the configuration. |
| `au_becs_debit` | `payment_method_config_resource_payment_method_properties` |  |  |
| `bacs_debit` | `payment_method_config_resource_payment_method_properties` |  |  |
| `bancontact` | `payment_method_config_resource_payment_method_properties` |  |  |
| `blik` | `payment_method_config_resource_payment_method_properties` |  |  |
| `boleto` | `payment_method_config_resource_payment_method_properties` |  |  |
| `card` | `payment_method_config_resource_payment_method_properties` |  |  |
| `cartes_bancaires` | `payment_method_config_resource_payment_method_properties` |  |  |
| `cashapp` | `payment_method_config_resource_payment_method_properties` |  |  |
| `customer_balance` | `payment_method_config_resource_payment_method_properties` |  |  |
| `eps` | `payment_method_config_resource_payment_method_properties` |  |  |
| `fpx` | `payment_method_config_resource_payment_method_properties` |  |  |
| `giropay` | `payment_method_config_resource_payment_method_properties` |  |  |
| `google_pay` | `payment_method_config_resource_payment_method_properties` |  |  |
| `grabpay` | `payment_method_config_resource_payment_method_properties` |  |  |
| `id` | string | yes | Unique identifier for the object. |
| `ideal` | `payment_method_config_resource_payment_method_properties` |  |  |
| `is_default` | boolean | yes | The default configuration is used whenever a payment method configuration is not specified. |
| `jcb` | `payment_method_config_resource_payment_method_properties` |  |  |
| `klarna` | `payment_method_config_resource_payment_method_properties` |  |  |
| `konbini` | `payment_method_config_resource_payment_method_properties` |  |  |
| `link` | `payment_method_config_resource_payment_method_properties` |  |  |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `name` | string | yes | The configuration's name. |
| `object` | enum: `payment_method_configuration` | yes | String representing the object's type. Objects of the same type share the same value. |
| `oxxo` | `payment_method_config_resource_payment_method_properties` |  |  |
| `p24` | `payment_method_config_resource_payment_method_properties` |  |  |
| `parent` | string |  | For child configs, the configuration's parent configuration. |
| `paynow` | `payment_method_config_resource_payment_method_properties` |  |  |
| `paypal` | `payment_method_config_resource_payment_method_properties` |  |  |
| `promptpay` | `payment_method_config_resource_payment_method_properties` |  |  |
| `revolut_pay` | `payment_method_config_resource_payment_method_properties` |  |  |
| `sepa_debit` | `payment_method_config_resource_payment_method_properties` |  |  |
| `sofort` | `payment_method_config_resource_payment_method_properties` |  |  |
| `us_bank_account` | `payment_method_config_resource_payment_method_properties` |  |  |
| `wechat_pay` | `payment_method_config_resource_payment_method_properties` |  |  |
| `zip` | `payment_method_config_resource_payment_method_properties` |  |  |

