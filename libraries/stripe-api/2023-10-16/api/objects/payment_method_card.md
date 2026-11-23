# Stripe API 2023-10-16 — `payment_method_card` object

Expandable fields (pass `expand[]=<field>`): `checks`, `generated_from`, `networks`, `three_d_secure_usage`, `wallet`

| Field | Type | Required | Description |
|---|---|---|---|
| `brand` | string | yes | Card brand. Can be `amex`, `diners`, `discover`, `eftpos_au`, `jcb`, `mastercard`, `unionpay`, `visa`, or `unknown`. |
| `checks` | `payment_method_card_checks` |  | Checks on Card address and CVC if provided. |
| `country` | string |  | Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you've collected. |
| `display_brand` | string |  | The brand to use when displaying the card, this accounts for customer's brand choice on dual-branded cards. Can be `american_express`, `cartes_bancaires`, `diners_club`, `discover`, `eftpos_australia`, `interac`, `jcb`, `mastercard`, `union_pay`, `visa`, or `other` and may contain more values in the future. |
| `exp_month` | integer | yes | Two-digit number representing the card's expiration month. |
| `exp_year` | integer | yes | Four-digit number representing the card's expiration year. |
| `fingerprint` | string |  | Uniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.<br>*As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card---one for India and one for the rest of the world.* |
| `funding` | string | yes | Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`. |
| `generated_from` | `payment_method_card_generated_card` |  | Details of the original PaymentMethod that created this object. |
| `last4` | string | yes | The last four digits of the card. |
| `networks` | `networks` |  | Contains information about card networks that can be used to process the payment. |
| `three_d_secure_usage` | `three_d_secure_usage` |  | Contains details on how this Card may be used for 3D Secure authentication. |
| `wallet` | `payment_method_card_wallet` |  | If this Card is part of a card wallet, this contains the details of the card wallet. |

