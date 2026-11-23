# Stripe API 2023-10-16 — `payment_method_details_card_present` object

Expandable fields (pass `expand[]=<field>`): `offline`, `receipt`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount_authorized` | integer |  | The authorized amount |
| `brand` | string |  | Card brand. Can be `amex`, `diners`, `discover`, `eftpos_au`, `jcb`, `mastercard`, `unionpay`, `visa`, or `unknown`. |
| `capture_before` | timestamp (Unix seconds) |  | When using manual capture, a future timestamp after which the charge will be automatically refunded if uncaptured. |
| `cardholder_name` | string |  | The cardholder name as read from the card, in [ISO 7813](https://en.wikipedia.org/wiki/ISO/IEC_7813) format. May include alphanumeric characters, special characters and first/last name separator (`/`). In some cases, the cardholder name may not be available depending on how the issuer has configured the card. Cardholder name is typically not available on swipe or contactless payments, such as those made with Apple Pay and Google Pay. |
| `country` | string |  | Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you've collected. |
| `emv_auth_data` | string |  | Authorization response cryptogram. |
| `exp_month` | integer | yes | Two-digit number representing the card's expiration month. |
| `exp_year` | integer | yes | Four-digit number representing the card's expiration year. |
| `fingerprint` | string |  | Uniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.<br>*As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card---one for India and one for the rest of the world.* |
| `funding` | string |  | Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`. |
| `generated_card` | string |  | ID of a card PaymentMethod generated from the card_present PaymentMethod that may be attached to a Customer for future transactions. Only present if it was possible to generate a card PaymentMethod. |
| `incremental_authorization_supported` | boolean | yes | Whether this [PaymentIntent](https://stripe.com/docs/api/payment_intents) is eligible for incremental authorizations. Request support using [request_incremental_authorization_support](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-payment_method_options-card_present-request_incremental_authorization_support). |
| `last4` | string |  | The last four digits of the card. |
| `network` | string |  | Identifies which network this charge was processed on. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `interac`, `jcb`, `mastercard`, `unionpay`, `visa`, or `unknown`. |
| `offline` | `payment_method_details_card_present_offline` |  | Details about payments collected offline. |
| `overcapture_supported` | boolean | yes | Defines whether the authorized amount can be over-captured or not |
| `read_method` | enum: `contact_emv`, `contactless_emv`, `contactless_magstripe_mode`, `magnetic_stripe_fallback`, `magnetic_stripe_track2` |  | How card details were read in this transaction. |
| `receipt` | `payment_method_details_card_present_receipt` |  | A collection of fields required to be displayed on receipts. Only required for EMV transactions. |

