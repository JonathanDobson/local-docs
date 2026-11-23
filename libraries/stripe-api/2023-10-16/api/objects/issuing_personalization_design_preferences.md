# Stripe API 2023-10-16 — `issuing_personalization_design_preferences` object

| Field | Type | Required | Description |
|---|---|---|---|
| `is_default` | boolean | yes | Whether we use this personalization design to create cards when one isn't specified. A connected account uses the Connect platform's default design if no personalization design is set as the default design. |
| `is_platform_default` | boolean |  | Whether this personalization design is used to create cards when one is not specified and a default for this connected account does not exist. |

