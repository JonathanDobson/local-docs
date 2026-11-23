# Stripe API 2023-10-16 — reviews

Operations under `/v1/reviews` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/reviews

operationId: `GetReviews`

Returns a list of `Review` objects that have `open` set to `true`. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | object or integer |  | Only return reviews that were created during the given date interval. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## GET /v1/reviews/{review}

operationId: `GetReviewsReview`

Retrieves a `Review` object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `review (path)` | string | yes |  |

Returns: `review`

## POST /v1/reviews/{review}/approve

operationId: `PostReviewsReviewApprove`

Approves a `Review` object, closing it and removing it from the list of reviews.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `review (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `review`

# Objects returned

## The `review` object

Reviews can be used to supplement automated fraud detection with human expertise.

Learn more about [Radar](/radar) and reviewing payments
[here](https://stripe.com/docs/radar/reviews).

Expandable fields (pass `expand[]=<field>`): `charge`, `ip_address_location`, `payment_intent`, `session`

| Field | Type | Required | Description |
|---|---|---|---|
| `billing_zip` | string |  | The ZIP or postal code of the card used, if applicable. |
| `charge` | string or `charge` |  | The charge associated with this review. |
| `closed_reason` | enum: `approved`, `disputed`, `redacted`, `refunded`, `refunded_as_fraud` |  | The reason the review was closed, or null if it has not yet been closed. One of `approved`, `refunded`, `refunded_as_fraud`, `disputed`, or `redacted`. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `id` | string | yes | Unique identifier for the object. |
| `ip_address` | string |  | The IP address where the payment originated. |
| `ip_address_location` | `radar_review_resource_location` |  | Information related to the location of the payment. Note that this information is an approximation and attempts to locate the nearest population center - it should not be used to determine a specific address. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `object` | enum: `review` | yes | String representing the object's type. Objects of the same type share the same value. |
| `open` | boolean | yes | If `true`, the review needs action. |
| `opened_reason` | enum: `manual`, `rule` | yes | The reason the review was opened. One of `rule` or `manual`. |
| `payment_intent` | string or `payment_intent` |  | The PaymentIntent ID associated with this review, if one exists. |
| `reason` | string | yes | The reason the review is currently open or closed. One of `rule`, `manual`, `approved`, `refunded`, `refunded_as_fraud`, `disputed`, or `redacted`. |
| `session` | `radar_review_resource_session` |  | Information related to the browsing session of the user who initiated the payment. |

