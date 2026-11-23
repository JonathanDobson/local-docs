# Stripe API 2023-10-16 — `payment_method_ideal` object

| Field | Type | Required | Description |
|---|---|---|---|
| `bank` | enum: `abn_amro`, `asn_bank`, `bunq`, `handelsbanken`, `ing`, `knab`, `moneyou`, `n26`, `nn`, `rabobank`, `regiobank`, `revolut`, `sns_bank`, `triodos_bank`, `van_lanschot`, `yoursafe` |  | The customer's bank, if provided. Can be one of `abn_amro`, `asn_bank`, `bunq`, `handelsbanken`, `ing`, `knab`, `moneyou`, `n26`, `nn`, `rabobank`, `regiobank`, `revolut`, `sns_bank`, `triodos_bank`, `van_lanschot`, or `yoursafe`. |
| `bic` | enum: `ABNANL2A`, `ASNBNL21`, `BITSNL2A`, `BUNQNL2A`, `FVLBNL22`, `HANDNL2A`, `INGBNL2A`, `KNABNL2H`, `MOYONL21`, `NNBANL2G`, `NTSBDEB1`, `RABONL2U`, `RBRBNL21`, `REVOIE23`, `REVOLT21`, `SNSBNL2A`, `TRIONL2U` |  | The Bank Identifier Code of the customer's bank, if the bank was provided. |

