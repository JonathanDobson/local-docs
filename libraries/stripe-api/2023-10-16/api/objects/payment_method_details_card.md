# Stripe API 2023-10-16 — `payment_method_details_card` object

Expandable fields (pass `expand[]=<field>`): `checks`, `extended_authorization`, `incremental_authorization`, `installments`, `multicapture`, `network_token`, `overcapture`, `three_d_secure`, `wallet`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount_authorized` | integer |  | The authorized amount. |
| `brand` | string |  | Card brand. Can be `amex`, `diners`, `discover`, `eftpos_au`, `jcb`, `mastercard`, `unionpay`, `visa`, or `unknown`. |
| `capture_before` | timestamp (Unix seconds) |  | When using manual capture, a future timestamp at which the charge will be automatically refunded if uncaptured. |
| `checks` | `payment_method_details_card_checks` |  | Check results by Card networks on Card address and CVC at time of payment. |
| `country` | string |  | Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you've collected. |
| `exp_month` | integer | yes | Two-digit number representing the card's expiration month. |
| `exp_year` | integer | yes | Four-digit number representing the card's expiration year. |
| `extended_authorization` | `payment_flows_private_payment_methods_card_details_api_resource_enterprise_features_extended_authorization_extended_authorization` |  |  |
| `fingerprint` | string |  | Uniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.<br>*As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card---one for India and one for the rest of the world.* |
| `funding` | string |  | Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`. |
| `incremental_authorization` | `payment_flows_private_payment_methods_card_details_api_resource_enterprise_features_incremental_authorization_incremental_authorization` |  |  |
| `installments` | `payment_method_details_card_installments` |  | Installment details for this payment (Mexico only).<br>For more information, see the [installments integration guide](https://stripe.com/docs/payments/installments). |
| `last4` | string |  | The last four digits of the card. |
| `mandate` | string |  | ID of the mandate used to make this payment or created by it. |
| `multicapture` | `payment_flows_private_payment_methods_card_details_api_resource_multicapture` |  |  |
| `network` | string |  | Identifies which network this charge was processed on. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `interac`, `jcb`, `mastercard`, `unionpay`, `visa`, or `unknown`. |
| `network_token` | `payment_method_details_card_network_token` |  | If this card has network token credentials, this contains the details of the network token credentials. |
| `overcapture` | `payment_flows_private_payment_methods_card_details_api_resource_enterprise_features_overcapture_overcapture` |  |  |
| `three_d_secure` | `three_d_secure_details_charge` |  | Populated if this transaction used 3D Secure authentication. |
| `wallet` | `payment_method_details_card_wallet` |  | If this Card is part of a card wallet, this contains the details of the card wallet. |

