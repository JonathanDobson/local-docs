# Stripe API 2023-10-16 — payment method domains

Operations under `/v1/payment_method_domains` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/payment_method_domains

operationId: `GetPaymentMethodDomains`

Lists the details of existing payment method domains.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `domain_name` | string |  | The domain name that this payment method domain object represents. |
| `enabled` | boolean |  | Whether this payment method domain is enabled. If the domain is not enabled, payment methods will not appear in Elements |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/payment_method_domains

operationId: `PostPaymentMethodDomains`

Creates a payment method domain.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `domain_name` | string | yes | The domain name that this payment method domain object represents. |
| `enabled` | boolean |  | Whether this payment method domain is enabled. If the domain is not enabled, payment methods that require a payment method domain will not appear in Elements. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `payment_method_domain`

## GET /v1/payment_method_domains/{payment_method_domain}

operationId: `GetPaymentMethodDomainsPaymentMethodDomain`

Retrieves the details of an existing payment method domain.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `payment_method_domain (path)` | string | yes |  |

Returns: `payment_method_domain`

## POST /v1/payment_method_domains/{payment_method_domain}

operationId: `PostPaymentMethodDomainsPaymentMethodDomain`

Updates an existing payment method domain.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `payment_method_domain (path)` | string | yes |  |
| `enabled` | boolean |  | Whether this payment method domain is enabled. If the domain is not enabled, payment methods that require a payment method domain will not appear in Elements. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `payment_method_domain`

## POST /v1/payment_method_domains/{payment_method_domain}/validate

operationId: `PostPaymentMethodDomainsPaymentMethodDomainValidate`

Some payment methods such as Apple Pay require additional steps to verify a domain. If the requirements weren’t satisfied when the domain was created, the payment method will be inactive on the domain.
The payment method doesn’t appear in Elements for this domain until it is active.

To activate a payment method on an existing payment method domain, complete the required validation steps specific to the payment method, and then validate the payment method domain with this endpoint.

Related guides: [Payment method domains](https://stripe.com/docs/payments/payment-methods/pmd-registration).

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `payment_method_domain (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `payment_method_domain`

# Objects returned

## The `payment_method_domain` object

A payment method domain represents a web domain that you have registered with Stripe.
Stripe Elements use registered payment method domains to control where certain payment methods are shown.

Related guides: [Payment method domains](https://stripe.com/docs/payments/payment-methods/pmd-registration).

Expandable fields (pass `expand[]=<field>`): `apple_pay`, `google_pay`, `link`, `paypal`

| Field | Type | Required | Description |
|---|---|---|---|
| `apple_pay` | `payment_method_domain_resource_payment_method_status` | yes |  |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `domain_name` | string | yes | The domain name that this payment method domain object represents. |
| `enabled` | boolean | yes | Whether this payment method domain is enabled. If the domain is not enabled, payment methods that require a payment method domain will not appear in Elements. |
| `google_pay` | `payment_method_domain_resource_payment_method_status` | yes |  |
| `id` | string | yes | Unique identifier for the object. |
| `link` | `payment_method_domain_resource_payment_method_status` | yes |  |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `object` | enum: `payment_method_domain` | yes | String representing the object's type. Objects of the same type share the same value. |
| `paypal` | `payment_method_domain_resource_payment_method_status` | yes |  |

