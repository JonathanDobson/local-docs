# Stripe API 2023-10-16 — `issuing_authorization_merchant_data` object

| Field | Type | Required | Description |
|---|---|---|---|
| `category` | string | yes | A categorization of the seller's type of business. See our [merchant categories guide](https://stripe.com/docs/issuing/merchant-categories) for a list of possible values. |
| `category_code` | string | yes | The merchant category code for the seller’s business |
| `city` | string |  | City where the seller is located |
| `country` | string |  | Country where the seller is located |
| `name` | string |  | Name of the seller |
| `network_id` | string | yes | Identifier assigned to the seller by the card network. Different card networks may assign different network_id fields to the same merchant. |
| `postal_code` | string |  | Postal code where the seller is located |
| `state` | string |  | State where the seller is located |
| `terminal_id` | string |  | An ID assigned by the seller to the location of the sale. |
| `url` | string |  | URL provided by the merchant on a 3DS request |

