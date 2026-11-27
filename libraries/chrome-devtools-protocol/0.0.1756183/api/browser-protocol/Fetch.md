# Fetch domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

A domain for letting clients substitute browser's network layer with client code.

Depends on: [Network](Network.md), [IO](IO.md), [Page](Page.md)

9 methods, 2 events, 6 types.

## Methods

### Fetch.disable

Disables the fetch domain.

No parameters.

### Fetch.enable

Enables issuing of requestPaused events. A request will be paused until client
calls one of failRequest, fulfillRequest or continueRequest/continueWithAuth.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `patterns` (optional) | array of [Fetch.RequestPattern](#type-requestpattern) | If specified, only requests matching any of these patterns will produce fetchRequested event and will be paused until clients response. If not set, all requests will be affected. |
| `handleAuthRequests` (optional) | boolean | If true, authRequired events will be issued and requests will be paused expecting a call to continueWithAuth. |

### Fetch.failRequest

Causes the request to fail with specified reason.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [Fetch.RequestId](#type-requestid) | An id the client received in requestPaused event. |
| `errorReason` | [Network.ErrorReason](Network.md#type-errorreason) | Causes the request to fail with the given reason. |

### Fetch.fulfillRequest

Provides response to the request.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [Fetch.RequestId](#type-requestid) | An id the client received in requestPaused event. |
| `responseCode` | integer | An HTTP response code. |
| `responseHeaders` (optional) | array of [Fetch.HeaderEntry](#type-headerentry) | Response headers. |
| `binaryResponseHeaders` (optional) | string | Alternative way of specifying response headers as a \0-separated series of name: value pairs. Prefer the above method unless you need to represent some non-UTF8 values that can't be transmitted over the protocol as text. (Encoded as a base64 string when passed over JSON) |
| `body` (optional) | string | A response body. If absent, original response body will be used if the request is intercepted at the response stage and empty body will be used if the request is intercepted at the request stage. (Encoded as a base64 string when passed over JSON) |
| `responsePhrase` (optional) | string | A textual representation of responseCode. If absent, a standard phrase matching responseCode is used. |

### Fetch.continueRequest

Continues the request, optionally modifying some of its parameters.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [Fetch.RequestId](#type-requestid) | An id the client received in requestPaused event. |
| `url` (optional) | string | If set, the request url will be modified in a way that's not observable by page. |
| `method` (optional) | string | If set, the request method is overridden. |
| `postData` (optional) | string | If set, overrides the post data in the request. (Encoded as a base64 string when passed over JSON) |
| `headers` (optional) | array of [Fetch.HeaderEntry](#type-headerentry) | If set, overrides the request headers. Note that the overrides do not extend to subsequent redirect hops, if a redirect happens. Another override may be applied to a different request produced by a redirect. |
| `interceptResponse` (optional) | boolean | **Experimental** If set, overrides response interception behavior for this request. |

### Fetch.continueWithAuth

Continues a request supplying authChallengeResponse following authRequired event.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [Fetch.RequestId](#type-requestid) | An id the client received in authRequired event. |
| `authChallengeResponse` | [Fetch.AuthChallengeResponse](#type-authchallengeresponse) | Response to with an authChallenge. |

### Fetch.continueResponse

**Experimental**

Continues loading of the paused response, optionally modifying the
response headers. If either responseCode or headers are modified, all of them
must be present.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [Fetch.RequestId](#type-requestid) | An id the client received in requestPaused event. |
| `responseCode` (optional) | integer | An HTTP response code. If absent, original response code will be used. |
| `responsePhrase` (optional) | string | A textual representation of responseCode. If absent, a standard phrase matching responseCode is used. |
| `responseHeaders` (optional) | array of [Fetch.HeaderEntry](#type-headerentry) | Response headers. If absent, original response headers will be used. |
| `binaryResponseHeaders` (optional) | string | Alternative way of specifying response headers as a \0-separated series of name: value pairs. Prefer the above method unless you need to represent some non-UTF8 values that can't be transmitted over the protocol as text. (Encoded as a base64 string when passed over JSON) |

### Fetch.getResponseBody

Causes the body of the response to be received from the server and
returned as a single string. May only be issued for a request that
is paused in the Response stage and is mutually exclusive with
takeResponseBodyForInterceptionAsStream. Calling other methods that
affect the request or disabling fetch domain before body is received
results in an undefined behavior.
Note that the response body is not available for redirects. Requests
paused in the _redirect received_ state may be differentiated by
`responseCode` and presence of `location` response header, see
comments to `requestPaused` for details.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [Fetch.RequestId](#type-requestid) | Identifier for the intercepted request to get body for. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `body` | string | Response body. |
| `base64Encoded` | boolean | True, if content was sent as base64. |

### Fetch.takeResponseBodyAsStream

Returns a handle to the stream representing the response body.
The request must be paused in the HeadersReceived stage.
Note that after this command the request can't be continued
as is -- client either needs to cancel it or to provide the
response body.
The stream only supports sequential read, IO.read will fail if the position
is specified.
This method is mutually exclusive with getResponseBody.
Calling other methods that affect the request or disabling fetch
domain before body is received results in an undefined behavior.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [Fetch.RequestId](#type-requestid) |  |

**Return object**

| Name | Type | Description |
|---|---|---|
| `stream` | [IO.StreamHandle](IO.md#type-streamhandle) |  |

## Events

### Fetch.requestPaused

Issued when the domain is enabled and the request URL matches the
specified filter. The request is paused until the client responds
with one of continueRequest, failRequest or fulfillRequest.
The stage of the request can be determined by presence of responseErrorReason
and responseStatusCode -- the request is at the response stage if either
of these fields is present and in the request stage otherwise.
Redirect responses and subsequent requests are reported similarly to regular
responses and requests. Redirect responses may be distinguished by the value
of `responseStatusCode` (which is one of 301, 302, 303, 307, 308) along with
presence of the `location` header. Requests resulting from a redirect will
have `redirectedRequestId` field set.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [Fetch.RequestId](#type-requestid) | Each request the page makes will have a unique id. |
| `request` | [Network.Request](Network.md#type-request) | The details of the request. |
| `frameId` | [Page.FrameId](Page.md#type-frameid) | The id of the frame that initiated the request. |
| `resourceType` | [Network.ResourceType](Network.md#type-resourcetype) | How the requested resource will be used. |
| `responseErrorReason` (optional) | [Network.ErrorReason](Network.md#type-errorreason) | Response error if intercepted at response stage. |
| `responseStatusCode` (optional) | integer | Response code if intercepted at response stage. |
| `responseStatusText` (optional) | string | Response status text if intercepted at response stage. |
| `responseHeaders` (optional) | array of [Fetch.HeaderEntry](#type-headerentry) | Response headers if intercepted at the response stage. |
| `networkId` (optional) | [Network.RequestId](Network.md#type-requestid) | If the intercepted request had a corresponding Network.requestWillBeSent event fired for it, then this networkId will be the same as the requestId present in the requestWillBeSent event. |
| `redirectedRequestId` (optional) | [Fetch.RequestId](#type-requestid) | **Experimental** If the request is due to a redirect response from the server, the id of the request that has caused the redirect. |

### Fetch.authRequired

Issued when the domain is enabled with handleAuthRequests set to true.
The request is paused until client responds with continueWithAuth.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [Fetch.RequestId](#type-requestid) | Each request the page makes will have a unique id. |
| `request` | [Network.Request](Network.md#type-request) | The details of the request. |
| `frameId` | [Page.FrameId](Page.md#type-frameid) | The id of the frame that initiated the request. |
| `resourceType` | [Network.ResourceType](Network.md#type-resourcetype) | How the requested resource will be used. |
| `authChallenge` | [Fetch.AuthChallenge](#type-authchallenge) | Details of the Authorization Challenge encountered. If this is set, client should respond with continueRequest that contains AuthChallengeResponse. |

## Types

<a id="type-requestid"></a>
### Fetch.RequestId

Unique request identifier.
Note that this does not identify individual HTTP requests that are part of
a network request.

Type: string

<a id="type-requeststage"></a>
### Fetch.RequestStage

Stages of the request to handle. Request will intercept before the request is
sent. Response will intercept after the response is received (but before response
body is received).

Type: string

Allowed values: `Request`, `Response`

<a id="type-requestpattern"></a>
### Fetch.RequestPattern

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `urlPattern` (optional) | string | Wildcards (`'*'` -> zero or more, `'?'` -> exactly one) are allowed. Escape character is backslash. Omitting is equivalent to `"*"`. |
| `resourceType` (optional) | [Network.ResourceType](Network.md#type-resourcetype) | If set, only requests for matching resource types will be intercepted. |
| `requestStage` (optional) | [Fetch.RequestStage](#type-requeststage) | Stage at which to begin intercepting requests. Default is Request. |

<a id="type-headerentry"></a>
### Fetch.HeaderEntry

Response HTTP header entry

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string |  |
| `value` | string |  |

<a id="type-authchallenge"></a>
### Fetch.AuthChallenge

Authorization challenge for HTTP status code 401 or 407.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `source` (optional) | string | Source of the authentication challenge. Allowed values: `Server`, `Proxy` |
| `origin` | string | Origin of the challenger. |
| `scheme` | string | The authentication scheme used, such as basic or digest |
| `realm` | string | The realm of the challenge. May be empty. |

<a id="type-authchallengeresponse"></a>
### Fetch.AuthChallengeResponse

Response to an AuthChallenge.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `response` | string | The decision on what to do in response to the authorization challenge. Default means deferring to the default behavior of the net stack, which will likely either the Cancel authentication or display a popup dialog box. Allowed values: `Default`, `CancelAuth`, `ProvideCredentials` |
| `username` (optional) | string | The username to provide, possibly empty. Should only be set if response is ProvideCredentials. |
| `password` (optional) | string | The password to provide, possibly empty. Should only be set if response is ProvideCredentials. |
