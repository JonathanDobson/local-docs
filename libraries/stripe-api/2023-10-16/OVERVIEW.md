# Stripe API reference, version 2023-10-16

Stripe's REST API reference for **API version 2023-10-16**. That is the version
the Node `stripe` package 14.x sends on every request (14.25.0 pins it in
`cjs/apiVersion.js`), so it describes what the legacy API's Stripe calls actually
get back. Generated from Stripe's official OpenAPI spec, `github.com/stripe/openapi`
tag **v934** (commit `0ba185f`), the last spec tag whose `info.version` is
2023-10-16. MIT licensed.

The prose guides, curl examples and the current (2026-11-18.endive) API reference
from docs.stripe.com are in the separate, local-only **`stripe-guides`** set. The
browser SDK (Stripe.js / React Stripe.js) is in **`stripe-js`**.

## Layout

| Path | What it holds |
|---|---|
| `api/resources/<resource>.md` | One page per resource: every operation under `/v1/<resource>` (method, path, description, every query/form parameter with type, enum values and description), then the object(s) those operations return, field by field. Test helpers are `test_helpers.<x>.md`. |
| `api/objects/<schema>.md` | Every other object in the spec (sub-objects such as `payment_intent_next_action`, `notification_event_data`, `invoice_setting_customer_setting`). |
| `api/spec3.json` | The official spec, unchanged: the source of truth. |
| `api/spec3.sdk.json` | Same spec with SDK annotations (`x-stripeOperations` method names). |
| `api/fixtures3.json` | Stripe's example object for each resource. |

Parameters are shown with their form-encoded names: nested fields use dots
(`payment_settings.save_default_payment_method`) and array items use `[]`
(`items[].price`). On the wire that is `items[0][price]=...`.

## Where to look for…

| Task | File |
|---|---|
| Retrieve an event / list events (`GET /v1/events/{id}`) and the `event` object | `api/resources/events.md` |
| What's in `event.data` (`object`, `previous_attributes`) | `api/objects/notification_event_data.md` |
| Every event type name (`invoice.payment_failed`, `customer.subscription.updated`, …) | `enabled_events` enum in `api/resources/webhook_endpoints.md` |
| Create/update webhook endpoints, the endpoint's `api_version` | `api/resources/webhook_endpoints.md` |
| Customers: create, update, search, delete, list a customer's payment methods, delete a discount | `api/resources/customers.md` |
| Subscriptions: create with `payment_behavior`, `trial_period_days`, `trial_end`, `coupon` / `promotion_code`; update, cancel, resume, search | `api/resources/subscriptions.md` |
| Subscription items and proration | `api/resources/subscription_items.md` |
| Invoices: upcoming invoice, finalize, pay, void, the `invoice` object (incl. `payment_intent`) | `api/resources/invoices.md` |
| Prices and products | `api/resources/prices.md`, `api/resources/products.md` |
| Coupons and promotion codes | `api/resources/coupons.md`, `api/resources/promotion_codes.md` |
| Payment methods: create, attach to a customer, detach | `api/resources/payment_methods.md` |
| Payment intents: create/confirm, `status` values incl. `requires_action`, `next_action` | `api/resources/payment_intents.md`, `api/objects/payment_intent_next_action.md` |
| Setup intents (saving a card without paying) | `api/resources/setup_intents.md` |
| Payment method configurations | `api/resources/payment_method_configurations.md` |
| Error object (`type`, `code`, `decline_code`) | `api/objects/api_errors.md` |

## Version notes

- **2023-10-16** is the newest API version in this spec. `webhook_endpoints`
  `api_version` accepts every dated version from `2011-01-01` up to
  `2023-10-16`.
- Subscription `payment_behavior` values: `allow_incomplete` (documented as the
  default), `default_incomplete`, `error_if_incomplete`, `pending_if_incomplete`
  (updates only). With `default_incomplete`, a subscription whose first
  invoice's PaymentIntent isn't confirmed within 23 hours becomes
  `incomplete_expired`.
- Subscription `status` values: `active`, `canceled`, `incomplete`,
  `incomplete_expired`, `past_due`, `paused`, `trialing`, `unpaid`.
- PaymentIntent `status` values: `requires_payment_method`,
  `requires_confirmation`, `requires_action`, `processing`, `requires_capture`,
  `canceled`, `succeeded`.
- Newer API versions changed much of this. For example, `2025-03-31.basil`
  removed `payment_intent`, `charge` and `paid` from the Invoice object
  (replaced by `invoice.payments`), removed the singular `coupon` /
  `promotion_code` parameters in favour of `discounts`, and deprecated
  subscription-level `current_period_start` / `current_period_end`. Before
  assuming a field still exists in the current API, check the API changelog
  under `content/changelog/` in the `stripe-guides` set (these three are in
  `changelog/basil/2025-03-31/`).
- Webhook payloads are rendered in the **endpoint's** `api_version`, which may
  differ from 2023-10-16.

## Search tips

- Resource pages are named by URL segment, with underscores: `payment_intents`,
  `payment_methods`, `webhook_endpoints`, `payment_method_configurations`,
  `subscription_items`, `invoiceitems`.
- Search by operationId too (`GetEventsId`, `PostSubscriptions`,
  `PostPaymentMethodsPaymentMethodAttach`).
- Path parameters keep Stripe's names, which aren't always `{id}`:
  `/v1/subscriptions/{subscription_exposed_id}`, `/v1/payment_methods/{payment_method}`.
- "Expandable fields" on each object list what `expand[]` accepts (for example
  `latest_invoice` on a subscription, then `latest_invoice.payment_intent`).
- Links inside descriptions point at `stripe.com/docs/...`; the same pages are
  in `stripe-guides` under `content/` without the `/docs` prefix.
