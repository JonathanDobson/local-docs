# Stripe API 2023-10-16 — `setup_attempt_payment_method_details_card` object

Expandable fields (pass `expand[]=<field>`): `checks`, `three_d_secure`, `wallet`

| Field | Type | Required | Description |
|---|---|---|---|
| `brand` | string |  | Card brand. Can be `amex`, `diners`, `discover`, `eftpos_au`, `jcb`, `mastercard`, `unionpay`, `visa`, or `unknown`. |
| `checks` | `setup_attempt_payment_method_details_card_checks` |  | Check results by Card networks on Card address and CVC at the time of authorization |
| `country` | string |  | Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you've collected. |
| `exp_month` | integer |  | Two-digit number representing the card's expiration month. |
| `exp_year` | integer |  | Four-digit number representing the card's expiration year. |
| `fingerprint` | string |  | Uniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.<br>*As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card---one for India and one for the rest of the world.* |
| `funding` | string |  | Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`. |
| `last4` | string |  | The last four digits of the card. |
| `network` | string |  | Identifies which network this charge was processed on. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `interac`, `jcb`, `mastercard`, `unionpay`, `visa`, or `unknown`. |
| `three_d_secure` | `three_d_secure_details` |  | Populated if this authorization used 3D Secure authentication. |
| `wallet` | `setup_attempt_payment_method_details_card_wallet` |  | If this Card is part of a card wallet, this contains the details of the card wallet. |

