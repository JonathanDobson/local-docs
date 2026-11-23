# Stripe API 2023-10-16 — events

Operations under `/v1/events` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/events

operationId: `GetEvents`

List events, going back up to 30 days. Each event data is rendered according to Stripe API version at its creation time, specified in [event object](https://stripe.com/docs/api/events/object) `api_version` attribute (not according to your current Stripe API version or `Stripe-Version` header).

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | object or integer |  | Only return events that were created during the given date interval. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `delivery_success` | boolean |  | Filter events by whether all webhooks were successfully delivered. If false, events which are still pending or have failed all delivery attempts to a webhook endpoint will be returned. |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `type` | string |  | A string containing a specific event name, or group of events using * as a wildcard. The list will be filtered to include only events with a matching event property. |
| `types` | array of string |  | An array of up to 20 strings containing specific event names. The list will be filtered to include only events with a matching event property. You may pass either `type` or `types`, but not both. |

Returns: object

## GET /v1/events/{id}

operationId: `GetEventsId`

Retrieves the details of an event. Supply the unique identifier of the event, which you might have received in a webhook.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `id (path)` | string | yes |  |

Returns: `event`

# Objects returned

## The `event` object

Events are our way of letting you know when something interesting happens in
your account. When an interesting event occurs, we create a new `Event`
object. For example, when a charge succeeds, we create a `charge.succeeded`
event, and when an invoice payment attempt fails, we create an
`invoice.payment_failed` event. Certain API requests might create multiple
events. For example, if you create a new subscription for a
customer, you receive both a `customer.subscription.created` event and a
`charge.succeeded` event.

Events occur when the state of another API resource changes. The event's data
field embeds the resource's state at the time of the change. For
example, a `charge.succeeded` event contains a charge, and an
`invoice.payment_failed` event contains an invoice.

As with other API resources, you can use endpoints to retrieve an
[individual event](https://stripe.com/docs/api#retrieve_event) or a [list of events](https://stripe.com/docs/api#list_events)
from the API. We also have a separate
[webhooks](http://en.wikipedia.org/wiki/Webhook) system for sending the
`Event` objects directly to an endpoint on your server. You can manage
webhooks in your
[account settings](https://dashboard.stripe.com/account/webhooks). Learn how
to [listen for events](https://stripe.com/docs/webhooks)
so that your integration can automatically trigger reactions.

When using [Connect](https://stripe.com/docs/connect), you can also receive event notifications
that occur in connected accounts. For these events, there's an
additional `account` attribute in the received `Event` object.

We only guarantee access to events through the [Retrieve Event API](https://stripe.com/docs/api#retrieve_event)
for 30 days.

Expandable fields (pass `expand[]=<field>`): `data`, `request`

| Field | Type | Required | Description |
|---|---|---|---|
| `account` | string |  | The connected account that originates the event. |
| `api_version` | string |  | The Stripe API version used to render `data`. This property is populated only for events on or after October 31, 2014. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `data` | `notification_event_data` | yes |  |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `object` | enum: `event` | yes | String representing the object's type. Objects of the same type share the same value. |
| `pending_webhooks` | integer | yes | Number of webhooks that haven't been successfully delivered (for example, to return a 20x response) to the URLs you specify. |
| `request` | `notification_event_request` |  | Information on the API request that triggers the event. |
| `type` | string | yes | Description of the event (for example, `invoice.created` or `charge.refunded`). |

