# Network domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

Network domain allows tracking network activities of the page. It exposes information about http,
file, data and other requests and responses, their headers, bodies, timing, etc.

Depends on: [Debugger](Debugger.md), [Runtime](Runtime.md), [Security](Security.md)

35 methods, 43 events, 89 types.

## Methods

### Network.canClearBrowserCache

**Deprecated**

Tells whether clearing browser cache is supported.

No parameters.

**Return object**

| Name | Type | Description |
|---|---|---|
| `result` | boolean | True if browser cache can be cleared. |

### Network.canClearBrowserCookies

**Deprecated**

Tells whether clearing browser cookies is supported.

No parameters.

**Return object**

| Name | Type | Description |
|---|---|---|
| `result` | boolean | True if browser cookies can be cleared. |

### Network.canEmulateNetworkConditions

**Deprecated**

Tells whether emulation of network conditions is supported.

No parameters.

**Return object**

| Name | Type | Description |
|---|---|---|
| `result` | boolean | True if emulation of network conditions is supported. |

### Network.clearBrowserCache

Clears browser cache.

No parameters.

### Network.clearBrowserCookies

Clears browser cookies.

No parameters.

### Network.deleteCookies

Deletes browser cookies with matching name and url or domain/path/partitionKey pair.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `name` | string | Name of the cookies to remove. |
| `url` (optional) | string | If specified, deletes all the cookies with the given name where domain and path match provided URL. |
| `domain` (optional) | string | If specified, deletes only cookies with the exact domain. |
| `path` (optional) | string | If specified, deletes only cookies with the exact path. |
| `partitionKey` (optional) | [Network.CookiePartitionKey](#type-cookiepartitionkey) | **Experimental** If specified, deletes only cookies with the the given name and partitionKey where all partition key attributes match the cookie partition key attribute. |

### Network.disable

Disables network tracking, prevents network events from being sent to the client.

No parameters.

### Network.emulateNetworkConditions

**Deprecated**

Activates emulation of network conditions. This command is deprecated in favor of the emulateNetworkConditionsByRule
and overrideNetworkState commands, which can be used together to the same effect.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `offline` | boolean | True to emulate internet disconnection. |
| `latency` | number | Minimum latency from request sent to response headers received (ms). |
| `downloadThroughput` | number | Maximal aggregated download throughput (bytes/sec). -1 disables download throttling. |
| `uploadThroughput` | number | Maximal aggregated upload throughput (bytes/sec). -1 disables upload throttling. |
| `connectionType` (optional) | [Network.ConnectionType](#type-connectiontype) | Connection type if known. |
| `packetLoss` (optional) | number | **Experimental** WebRTC packet loss (percent, 0-100). 0 disables packet loss emulation, 100 drops all the packets. |
| `packetQueueLength` (optional) | integer | **Experimental** WebRTC packet queue length (packet). 0 removes any queue length limitations. |
| `packetReordering` (optional) | boolean | **Experimental** WebRTC packetReordering feature. |

### Network.emulateNetworkConditionsByRule

**Experimental**

Activates emulation of network conditions for individual requests using URL match patterns. Unlike the deprecated
Network.emulateNetworkConditions this method does not affect `navigator` state. Use Network.overrideNetworkState to
explicitly modify `navigator` behavior.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `offline` (optional) | boolean | **Deprecated** True to emulate internet disconnection. Deprecated, use the offline property in matchedNetworkConditions or emulateOfflineServiceWorker instead. |
| `emulateOfflineServiceWorker` (optional) | boolean | True to emulate offline service worker. |
| `matchedNetworkConditions` | array of [Network.NetworkConditions](#type-networkconditions) | Configure conditions for matching requests. If multiple entries match a request, the first entry wins. Global conditions can be configured by leaving the urlPattern for the conditions empty. These global conditions are also applied for throttling of p2p connections. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `ruleIds` | array of string | An id for each entry in matchedNetworkConditions. The id will be included in the requestWillBeSentExtraInfo for requests affected by a rule. |

### Network.overrideNetworkState

**Experimental**

Override the state of navigator.onLine and navigator.connection.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `offline` | boolean | True to emulate internet disconnection. |
| `latency` | number | Minimum latency from request sent to response headers received (ms). |
| `downloadThroughput` | number | Maximal aggregated download throughput (bytes/sec). -1 disables download throttling. |
| `uploadThroughput` | number | Maximal aggregated upload throughput (bytes/sec). -1 disables upload throttling. |
| `connectionType` (optional) | [Network.ConnectionType](#type-connectiontype) | Connection type if known. |

### Network.enable

Enables network tracking, network events will now be delivered to the client.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `maxTotalBufferSize` (optional) | integer | **Experimental** Buffer size in bytes to use when preserving network payloads (XHRs, etc). This is the maximum number of bytes that will be collected by this DevTools session. |
| `maxResourceBufferSize` (optional) | integer | **Experimental** Per-resource buffer size in bytes to use when preserving network payloads (XHRs, etc). |
| `maxPostDataSize` (optional) | integer | Longest post body size (in bytes) that would be included in requestWillBeSent notification |
| `reportDirectSocketTraffic` (optional) | boolean | **Experimental** Whether DirectSocket chunk send/receive events should be reported. |
| `enableDurableMessages` (optional) | boolean | **Experimental** Enable storing response bodies outside of renderer, so that these survive a cross-process navigation. Requires maxTotalBufferSize to be set. Currently defaults to false. This field is being deprecated in favor of the dedicated configureDurableMessages command, due to the possibility of deadlocks when awaiting Network.enable before issuing Runtime.runIfWaitingForDebugger. |

### Network.configureDurableMessages

**Experimental**

Configures storing response bodies outside of renderer, so that these survive
a cross-process navigation.
If maxTotalBufferSize is not set, durable messages are disabled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `maxTotalBufferSize` (optional) | integer | Buffer size in bytes to use when preserving network payloads (XHRs, etc). |
| `maxResourceBufferSize` (optional) | integer | Per-resource buffer size in bytes to use when preserving network payloads (XHRs, etc). |

### Network.getAllCookies

**Deprecated**

Returns all browser cookies. Depending on the backend support, will return detailed cookie
information in the `cookies` field.
Deprecated. Use Storage.getCookies instead.

No parameters.

**Return object**

| Name | Type | Description |
|---|---|---|
| `cookies` | array of [Network.Cookie](#type-cookie) | Array of cookie objects. |

### Network.getCertificate

**Experimental**

Returns the DER-encoded certificate.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `origin` | string | Origin to get certificate for. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `tableNames` | array of string |  |

### Network.getCookies

Returns all browser cookies for the current URL. Depending on the backend support, will return
detailed cookie information in the `cookies` field.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `urls` (optional) | array of string | The list of URLs for which applicable cookies will be fetched. If not specified, it's assumed to be set to the list containing the URLs of the page and all of its subframes. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `cookies` | array of [Network.Cookie](#type-cookie) | Array of cookie objects. |

### Network.getResponseBody

Returns content served for the given request.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [Network.RequestId](#type-requestid) | Identifier of the network request to get content for. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `body` | string | Response body. |
| `base64Encoded` | boolean | True, if content was sent as base64. |

### Network.getRequestPostData

Returns post data sent with the request. Returns an error when no data was sent with the request.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [Network.RequestId](#type-requestid) | Identifier of the network request to get content for. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `postData` | string | Request body string, omitting files from multipart requests |
| `base64Encoded` | boolean | True, if content was sent as base64. |

### Network.replayXHR

**Experimental**

This method sends a new XMLHttpRequest which is identical to the original one. The following
parameters should be identical: method, url, async, request body, extra headers, withCredentials
attribute, user, password.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [Network.RequestId](#type-requestid) | Identifier of XHR to replay. |

### Network.searchInResponseBody

**Experimental**

Searches for given string in response content.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [Network.RequestId](#type-requestid) | Identifier of the network response to search. |
| `query` | string | String to search for. |
| `caseSensitive` (optional) | boolean | If true, search is case sensitive. |
| `isRegex` (optional) | boolean | If true, treats string parameter as regex. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `result` | array of [Debugger.SearchMatch](Debugger.md#type-searchmatch) | List of search matches. |

### Network.setBlockedURLs

**Experimental**

Blocks URLs from loading.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `urlPatterns` (optional) | array of [Network.BlockPattern](#type-blockpattern) | Patterns to match in the order in which they are given. These patterns also take precedence over any wildcard patterns defined in `urls`. |
| `urls` (optional) | array of string | **Deprecated** URL patterns to block. Wildcards ('*') are allowed. |

### Network.setBypassServiceWorker

Toggles ignoring of service worker for each request.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bypass` | boolean | Bypass service worker and load from network. |

### Network.setCacheDisabled

Toggles ignoring cache for each request. If `true`, cache will not be used.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `cacheDisabled` | boolean | Cache disabled state. |

### Network.setCookie

Sets a cookie with the given cookie data; may overwrite equivalent cookies if they exist.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `name` | string | Cookie name. |
| `value` | string | Cookie value. |
| `url` (optional) | string | The request-URI to associate with the setting of the cookie. This value can affect the default domain, path, source port, and source scheme values of the created cookie. |
| `domain` (optional) | string | Cookie domain. |
| `path` (optional) | string | Cookie path. |
| `secure` (optional) | boolean | True if cookie is secure. |
| `httpOnly` (optional) | boolean | True if cookie is http-only. |
| `sameSite` (optional) | [Network.CookieSameSite](#type-cookiesamesite) | Cookie SameSite type. |
| `expires` (optional) | [Network.TimeSinceEpoch](#type-timesinceepoch) | Cookie expiration date, session cookie if not set |
| `priority` (optional) | [Network.CookiePriority](#type-cookiepriority) | **Experimental** Cookie Priority type. |
| `sourceScheme` (optional) | [Network.CookieSourceScheme](#type-cookiesourcescheme) | **Experimental** Cookie source scheme type. |
| `sourcePort` (optional) | integer | **Experimental** Cookie source port. Valid values are {-1, [1, 65535]}, -1 indicates an unspecified port. An unspecified port value allows protocol clients to emulate legacy cookie scope for the port. This is a temporary ability and it will be removed in the future. |
| `partitionKey` (optional) | [Network.CookiePartitionKey](#type-cookiepartitionkey) | **Experimental** Cookie partition key. If not set, the cookie will be set as not partitioned. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `success` | boolean | **Deprecated** Always set to true. If an error occurs, the response indicates protocol error. |

### Network.setCookies

Sets given cookies.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `cookies` | array of [Network.CookieParam](#type-cookieparam) | Cookies to be set. |

### Network.setExtraHTTPHeaders

Specifies whether to always send extra HTTP headers with the requests from this page.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `headers` | [Network.Headers](#type-headers) | Map with extra HTTP headers. |

### Network.setAttachDebugStack

**Experimental**

Specifies whether to attach a page script stack id in requests

**Parameters**

| Name | Type | Description |
|---|---|---|
| `enabled` | boolean | Whether to attach a page script stack for debugging purpose. |

### Network.setUserAgentOverride

Allows overriding user agent with the given string.

Implemented by the `Emulation` domain.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `userAgent` | string | User agent to use. |
| `acceptLanguage` (optional) | string | Browser language to emulate. |
| `platform` (optional) | string | The platform navigator.platform should return. |
| `userAgentMetadata` (optional) | [Emulation.UserAgentMetadata](Emulation.md#type-useragentmetadata) | **Experimental** To be sent in Sec-CH-UA-* headers and returned in navigator.userAgentData |

### Network.streamResourceContent

**Experimental**

Enables streaming of the response for the given requestId.
If enabled, the dataReceived event contains the data that was received during streaming.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [Network.RequestId](#type-requestid) | Identifier of the request to stream. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `bufferedData` | string | Data that has been buffered until streaming is enabled. (Encoded as a base64 string when passed over JSON) |

### Network.getSecurityIsolationStatus

**Experimental**

Returns information about the COEP/COOP isolation status.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frameId` (optional) | [Page.FrameId](Page.md#type-frameid) | If no frameId is provided, the status of the target is provided. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `status` | [Network.SecurityIsolationStatus](#type-securityisolationstatus) |  |

### Network.enableReportingApi

**Experimental**

Enables tracking for the Reporting API, events generated by the Reporting API will now be delivered to the client.
Enabling triggers 'reportingApiReportAdded' for all existing reports.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `enable` | boolean | Whether to enable or disable events for the Reporting API |

### Network.enableDeviceBoundSessions

**Experimental**

Sets up tracking device bound sessions and fetching of initial set of sessions.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `enable` | boolean | Whether to enable or disable events. |

### Network.deleteDeviceBoundSession

**Experimental**

Deletes a device bound session.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `key` | [Network.DeviceBoundSessionKey](#type-deviceboundsessionkey) |  |

### Network.fetchSchemefulSite

**Experimental**

Fetches the schemeful site for a specific origin.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `origin` | string | The URL origin. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `schemefulSite` | string | The corresponding schemeful site. |

### Network.loadNetworkResource

**Experimental**

Fetches the resource and returns the content.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frameId` (optional) | [Page.FrameId](Page.md#type-frameid) | Frame id to get the resource for. Mandatory for frame targets, and should be omitted for worker targets. |
| `url` | string | URL of the resource to get content for. |
| `options` | [Network.LoadNetworkResourceOptions](#type-loadnetworkresourceoptions) | Options for the request. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `resource` | [Network.LoadNetworkResourcePageResult](#type-loadnetworkresourcepageresult) |  |

### Network.setCookieControls

**Experimental**

Sets Controls for third-party cookie access
Page reload is required before the new cookie behavior will be observed

**Parameters**

| Name | Type | Description |
|---|---|---|
| `enableThirdPartyCookieRestriction` | boolean | Whether 3pc restriction is enabled. |

## Events

### Network.dataReceived

Fired when data chunk was received over the network.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [Network.RequestId](#type-requestid) | Request identifier. |
| `timestamp` | [Network.MonotonicTime](#type-monotonictime) | Timestamp. |
| `dataLength` | integer | Data chunk length. |
| `encodedDataLength` | integer | Actual bytes received (might be less than dataLength for compressed encodings). |
| `data` (optional) | string | **Experimental** Data that was received. (Encoded as a base64 string when passed over JSON) |

### Network.eventSourceMessageReceived

Fired when EventSource message is received.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [Network.RequestId](#type-requestid) | Request identifier. |
| `timestamp` | [Network.MonotonicTime](#type-monotonictime) | Timestamp. |
| `eventName` | string | Message type. |
| `eventId` | string | Message identifier. |
| `data` | string | Message content. |

### Network.loadingFailed

Fired when HTTP request has failed to load.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [Network.RequestId](#type-requestid) | Request identifier. |
| `timestamp` | [Network.MonotonicTime](#type-monotonictime) | Timestamp. |
| `type` | [Network.ResourceType](#type-resourcetype) | Resource type. |
| `errorText` | string | Error message. List of network errors: https://cs.chromium.org/chromium/src/net/base/net_error_list.h |
| `canceled` (optional) | boolean | True if loading was canceled. |
| `blockedReason` (optional) | [Network.BlockedReason](#type-blockedreason) | The reason why loading was blocked, if any. |
| `corsErrorStatus` (optional) | [Network.CorsErrorStatus](#type-corserrorstatus) | The reason why loading was blocked by CORS, if any. |

### Network.loadingFinished

Fired when HTTP request has finished loading.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [Network.RequestId](#type-requestid) | Request identifier. |
| `timestamp` | [Network.MonotonicTime](#type-monotonictime) | Timestamp. |
| `encodedDataLength` | number | Total number of bytes received for this request. |
| `encodedBodyLength` (optional) | number | **Experimental** Size of the response body before removing content encodings. Includes cached bodies, but excludes headers and transfer framing. |

### Network.requestServedFromCache

Fired if request ended up loading from cache.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [Network.RequestId](#type-requestid) | Request identifier. |

### Network.requestWillBeSent

Fired when page is about to send HTTP request.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [Network.RequestId](#type-requestid) | Request identifier. |
| `loaderId` | [Network.LoaderId](#type-loaderid) | Loader identifier. Empty string if the request is fetched from worker. |
| `documentURL` | string | URL of the document this request is loaded for. |
| `request` | [Network.Request](#type-request) | Request data. |
| `timestamp` | [Network.MonotonicTime](#type-monotonictime) | Timestamp. |
| `wallTime` | [Network.TimeSinceEpoch](#type-timesinceepoch) | Timestamp. |
| `initiator` | [Network.Initiator](#type-initiator) | Request initiator. |
| `redirectHasExtraInfo` | boolean | **Experimental** In the case that redirectResponse is populated, this flag indicates whether requestWillBeSentExtraInfo and responseReceivedExtraInfo events will be or were emitted for the request which was just redirected. |
| `redirectResponse` (optional) | [Network.Response](#type-response) | Redirect response data. |
| `type` (optional) | [Network.ResourceType](#type-resourcetype) | Type of this resource. |
| `frameId` (optional) | [Page.FrameId](Page.md#type-frameid) | Frame identifier. |
| `hasUserGesture` (optional) | boolean | Whether the request is initiated by a user gesture. Defaults to false. |
| `renderBlockingBehavior` (optional) | [Network.RenderBlockingBehavior](#type-renderblockingbehavior) | **Experimental** The render-blocking behavior of the request. |

### Network.resourceChangedPriority

**Experimental**

Fired when resource loading priority is changed

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [Network.RequestId](#type-requestid) | Request identifier. |
| `newPriority` | [Network.ResourcePriority](#type-resourcepriority) | New priority |
| `timestamp` | [Network.MonotonicTime](#type-monotonictime) | Timestamp. |

### Network.signedExchangeReceived

**Experimental**

Fired when a signed exchange was received over the network

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [Network.RequestId](#type-requestid) | Request identifier. |
| `info` | [Network.SignedExchangeInfo](#type-signedexchangeinfo) | Information about the signed exchange response. |

### Network.responseReceived

Fired when HTTP response is available.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [Network.RequestId](#type-requestid) | Request identifier. |
| `loaderId` | [Network.LoaderId](#type-loaderid) | Loader identifier. Empty string if the request is fetched from worker. |
| `timestamp` | [Network.MonotonicTime](#type-monotonictime) | Timestamp. |
| `type` | [Network.ResourceType](#type-resourcetype) | Resource type. |
| `response` | [Network.Response](#type-response) | Response data. |
| `hasExtraInfo` | boolean | **Experimental** Indicates whether requestWillBeSentExtraInfo and responseReceivedExtraInfo events will be or were emitted for this request. |
| `frameId` (optional) | [Page.FrameId](Page.md#type-frameid) | Frame identifier. |

### Network.webSocketClosed

Fired when WebSocket is closed.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [Network.RequestId](#type-requestid) | Request identifier. |
| `timestamp` | [Network.MonotonicTime](#type-monotonictime) | Timestamp. |

### Network.webSocketCreated

Fired upon WebSocket creation.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [Network.RequestId](#type-requestid) | Request identifier. |
| `url` | string | WebSocket request URL. |
| `initiator` (optional) | [Network.Initiator](#type-initiator) | Request initiator. |

### Network.webSocketFrameError

Fired when WebSocket message error occurs.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [Network.RequestId](#type-requestid) | Request identifier. |
| `timestamp` | [Network.MonotonicTime](#type-monotonictime) | Timestamp. |
| `errorMessage` | string | WebSocket error message. |

### Network.webSocketFrameReceived

Fired when WebSocket message is received.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [Network.RequestId](#type-requestid) | Request identifier. |
| `timestamp` | [Network.MonotonicTime](#type-monotonictime) | Timestamp. |
| `response` | [Network.WebSocketFrame](#type-websocketframe) | WebSocket response data. |

### Network.webSocketFrameSent

Fired when WebSocket message is sent.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [Network.RequestId](#type-requestid) | Request identifier. |
| `timestamp` | [Network.MonotonicTime](#type-monotonictime) | Timestamp. |
| `response` | [Network.WebSocketFrame](#type-websocketframe) | WebSocket response data. |

### Network.webSocketHandshakeResponseReceived

Fired when WebSocket handshake response becomes available.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [Network.RequestId](#type-requestid) | Request identifier. |
| `timestamp` | [Network.MonotonicTime](#type-monotonictime) | Timestamp. |
| `response` | [Network.WebSocketResponse](#type-websocketresponse) | WebSocket response data. |

### Network.webSocketWillSendHandshakeRequest

Fired when WebSocket is about to initiate handshake.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [Network.RequestId](#type-requestid) | Request identifier. |
| `timestamp` | [Network.MonotonicTime](#type-monotonictime) | Timestamp. |
| `wallTime` | [Network.TimeSinceEpoch](#type-timesinceepoch) | UTC Timestamp. |
| `request` | [Network.WebSocketRequest](#type-websocketrequest) | WebSocket request data. |

### Network.webTransportCreated

Fired upon WebTransport creation.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `transportId` | [Network.RequestId](#type-requestid) | WebTransport identifier. |
| `url` | string | WebTransport request URL. |
| `timestamp` | [Network.MonotonicTime](#type-monotonictime) | Timestamp. |
| `initiator` (optional) | [Network.Initiator](#type-initiator) | Request initiator. |

### Network.webTransportConnectionEstablished

Fired when WebTransport handshake is finished.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `transportId` | [Network.RequestId](#type-requestid) | WebTransport identifier. |
| `timestamp` | [Network.MonotonicTime](#type-monotonictime) | Timestamp. |

### Network.webTransportClosed

Fired when WebTransport is disposed.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `transportId` | [Network.RequestId](#type-requestid) | WebTransport identifier. |
| `timestamp` | [Network.MonotonicTime](#type-monotonictime) | Timestamp. |

### Network.directTCPSocketCreated

**Experimental**

Fired upon direct_socket.TCPSocket creation.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `identifier` | [Network.RequestId](#type-requestid) |  |
| `remoteAddr` | string |  |
| `remotePort` | integer | Unsigned int 16. |
| `options` | [Network.DirectTCPSocketOptions](#type-directtcpsocketoptions) |  |
| `timestamp` | [Network.MonotonicTime](#type-monotonictime) |  |
| `initiator` (optional) | [Network.Initiator](#type-initiator) |  |

### Network.directTCPSocketOpened

**Experimental**

Fired when direct_socket.TCPSocket connection is opened.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `identifier` | [Network.RequestId](#type-requestid) |  |
| `remoteAddr` | string |  |
| `remotePort` | integer | Expected to be unsigned integer. |
| `timestamp` | [Network.MonotonicTime](#type-monotonictime) |  |
| `localAddr` (optional) | string |  |
| `localPort` (optional) | integer | Expected to be unsigned integer. |

### Network.directTCPSocketAborted

**Experimental**

Fired when direct_socket.TCPSocket is aborted.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `identifier` | [Network.RequestId](#type-requestid) |  |
| `errorMessage` | [Network.ErrorReason](#type-errorreason) |  |
| `timestamp` | [Network.MonotonicTime](#type-monotonictime) |  |

### Network.directTCPSocketClosed

**Experimental**

Fired when direct_socket.TCPSocket is closed.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `identifier` | [Network.RequestId](#type-requestid) |  |
| `timestamp` | [Network.MonotonicTime](#type-monotonictime) |  |

### Network.directTCPSocketChunkSent

**Experimental**

Fired when data is sent to tcp direct socket stream.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `identifier` | [Network.RequestId](#type-requestid) |  |
| `data` | string |  |
| `timestamp` | [Network.MonotonicTime](#type-monotonictime) |  |

### Network.directTCPSocketChunkReceived

**Experimental**

Fired when data is received from tcp direct socket stream.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `identifier` | [Network.RequestId](#type-requestid) |  |
| `data` | string |  |
| `timestamp` | [Network.MonotonicTime](#type-monotonictime) |  |

### Network.directUDPSocketJoinedMulticastGroup

**Experimental**

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `identifier` | [Network.RequestId](#type-requestid) |  |
| `IPAddress` | string | Multicast group address. |
| `sourceAddress` (optional) | string | Source address of a source-specific multicast (SSM) membership. Absent for any-source multicast (ASM) memberships. |

### Network.directUDPSocketLeftMulticastGroup

**Experimental**

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `identifier` | [Network.RequestId](#type-requestid) |  |
| `IPAddress` | string | Multicast group address. |
| `sourceAddress` (optional) | string | Source address of a source-specific multicast (SSM) membership. Absent for any-source multicast (ASM) memberships. |

### Network.directUDPSocketCreated

**Experimental**

Fired upon direct_socket.UDPSocket creation.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `identifier` | [Network.RequestId](#type-requestid) |  |
| `options` | [Network.DirectUDPSocketOptions](#type-directudpsocketoptions) |  |
| `timestamp` | [Network.MonotonicTime](#type-monotonictime) |  |
| `initiator` (optional) | [Network.Initiator](#type-initiator) |  |

### Network.directUDPSocketOpened

**Experimental**

Fired when direct_socket.UDPSocket connection is opened.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `identifier` | [Network.RequestId](#type-requestid) |  |
| `localAddr` | string |  |
| `localPort` | integer | Expected to be unsigned integer. |
| `timestamp` | [Network.MonotonicTime](#type-monotonictime) |  |
| `remoteAddr` (optional) | string |  |
| `remotePort` (optional) | integer | Expected to be unsigned integer. |

### Network.directUDPSocketAborted

**Experimental**

Fired when direct_socket.UDPSocket is aborted.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `identifier` | [Network.RequestId](#type-requestid) |  |
| `errorMessage` | [Network.ErrorReason](#type-errorreason) |  |
| `timestamp` | [Network.MonotonicTime](#type-monotonictime) |  |

### Network.directUDPSocketClosed

**Experimental**

Fired when direct_socket.UDPSocket is closed.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `identifier` | [Network.RequestId](#type-requestid) |  |
| `timestamp` | [Network.MonotonicTime](#type-monotonictime) |  |

### Network.directUDPSocketChunkSent

**Experimental**

Fired when message is sent to udp direct socket stream.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `identifier` | [Network.RequestId](#type-requestid) |  |
| `message` | [Network.DirectUDPMessage](#type-directudpmessage) |  |
| `timestamp` | [Network.MonotonicTime](#type-monotonictime) |  |

### Network.directUDPSocketChunkReceived

**Experimental**

Fired when message is received from udp direct socket stream.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `identifier` | [Network.RequestId](#type-requestid) |  |
| `message` | [Network.DirectUDPMessage](#type-directudpmessage) |  |
| `timestamp` | [Network.MonotonicTime](#type-monotonictime) |  |

### Network.requestWillBeSentExtraInfo

**Experimental**

Fired when additional information about a requestWillBeSent event is available from the
network stack. Not every requestWillBeSent event will have an additional
requestWillBeSentExtraInfo fired for it, and there is no guarantee whether requestWillBeSent
or requestWillBeSentExtraInfo will be fired first for the same request.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [Network.RequestId](#type-requestid) | Request identifier. Used to match this information to an existing requestWillBeSent event. |
| `associatedCookies` | array of [Network.AssociatedCookie](#type-associatedcookie) | A list of cookies potentially associated to the requested URL. This includes both cookies sent with the request and the ones not sent; the latter are distinguished by having blockedReasons field set. |
| `headers` | [Network.Headers](#type-headers) | Raw request headers as they will be sent over the wire. |
| `connectTiming` | [Network.ConnectTiming](#type-connecttiming) | **Experimental** Connection timing information for the request. |
| `deviceBoundSessionUsages` (optional) | array of [Network.DeviceBoundSessionWithUsage](#type-deviceboundsessionwithusage) | How the request site's device bound sessions were used during this request. |
| `clientSecurityState` (optional) | [Network.ClientSecurityState](#type-clientsecuritystate) | The client security state set for the request. |
| `siteHasCookieInOtherPartition` (optional) | boolean | Whether the site has partitioned cookies stored in a partition different than the current one. |
| `appliedNetworkConditionsId` (optional) | string | The network conditions id if this request was affected by network conditions configured via emulateNetworkConditionsByRule. |

### Network.responseReceivedExtraInfo

**Experimental**

Fired when additional information about a responseReceived event is available from the network
stack. Not every responseReceived event will have an additional responseReceivedExtraInfo for
it, and responseReceivedExtraInfo may be fired before or after responseReceived.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [Network.RequestId](#type-requestid) | Request identifier. Used to match this information to another responseReceived event. |
| `blockedCookies` | array of [Network.BlockedSetCookieWithReason](#type-blockedsetcookiewithreason) | A list of cookies which were not stored from the response along with the corresponding reasons for blocking. The cookies here may not be valid due to syntax errors, which are represented by the invalid cookie line string instead of a proper cookie. |
| `headers` | [Network.Headers](#type-headers) | Raw response headers as they were received over the wire. Duplicate headers in the response are represented as a single key with their values concatentated using `\n` as the separator. See also `headersText` that contains verbatim text for HTTP/1.*. |
| `resourceIPAddressSpace` | [Network.IPAddressSpace](#type-ipaddressspace) | The IP address space of the resource. The address space can only be determined once the transport established the connection, so we can't send it in `requestWillBeSentExtraInfo`. |
| `statusCode` | integer | The status code of the response. This is useful in cases the request failed and no responseReceived event is triggered, which is the case for, e.g., CORS errors. This is also the correct status code for cached requests, where the status in responseReceived is a 200 and this will be 304. |
| `headersText` (optional) | string | Raw response header text as it was received over the wire. The raw text may not always be available, such as in the case of HTTP/2 or QUIC. |
| `cookiePartitionKey` (optional) | [Network.CookiePartitionKey](#type-cookiepartitionkey) | **Experimental** The cookie partition key that will be used to store partitioned cookies set in this response. Only sent when partitioned cookies are enabled. |
| `cookiePartitionKeyOpaque` (optional) | boolean | True if partitioned cookies are enabled, but the partition key is not serializable to string. |
| `exemptedCookies` (optional) | array of [Network.ExemptedSetCookieWithReason](#type-exemptedsetcookiewithreason) | A list of cookies which should have been blocked by 3PCD but are exempted and stored from the response with the corresponding reason. |

### Network.responseReceivedEarlyHints

**Experimental**

Fired when 103 Early Hints headers is received in addition to the common response.
Not every responseReceived event will have an responseReceivedEarlyHints fired.
Only one responseReceivedEarlyHints may be fired for eached responseReceived event.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [Network.RequestId](#type-requestid) | Request identifier. Used to match this information to another responseReceived event. |
| `headers` | [Network.Headers](#type-headers) | Raw response headers as they were received over the wire. Duplicate headers in the response are represented as a single key with their values concatentated using `\n` as the separator. See also `headersText` that contains verbatim text for HTTP/1.*. |

### Network.trustTokenOperationDone

**Experimental**

Fired exactly once for each Trust Token operation. Depending on
the type of the operation and whether the operation succeeded or
failed, the event is fired before the corresponding request was sent
or after the response was received.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `status` | string | Detailed success or error status of the operation. 'AlreadyExists' also signifies a successful operation, as the result of the operation already exists und thus, the operation was abort preemptively (e.g. a cache hit). Allowed values: `Ok`, `InvalidArgument`, `MissingIssuerKeys`, `FailedPrecondition`, `ResourceExhausted`, `AlreadyExists`, `ResourceLimited`, `Unauthorized`, `BadResponse`, `InternalError`, `UnknownError`, `FulfilledLocally`, `SiteIssuerLimit` |
| `type` | [Network.TrustTokenOperationType](#type-trusttokenoperationtype) |  |
| `requestId` | [Network.RequestId](#type-requestid) |  |
| `topLevelOrigin` (optional) | string | Top level origin. The context in which the operation was attempted. |
| `issuerOrigin` (optional) | string | Origin of the issuer in case of a "Issuance" or "Redemption" operation. |
| `issuedTokenCount` (optional) | integer | The number of obtained Trust Tokens on a successful "Issuance" operation. |

### Network.policyUpdated

**Experimental**

Fired once security policy has been updated.

### Network.reportingApiReportAdded

**Experimental**

Is sent whenever a new report is added.
And after 'enableReportingApi' for all existing reports.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `report` | [Network.ReportingApiReport](#type-reportingapireport) |  |

### Network.reportingApiReportUpdated

**Experimental**

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `report` | [Network.ReportingApiReport](#type-reportingapireport) |  |

### Network.reportingApiEndpointsChangedForOrigin

**Experimental**

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `origin` | string | Origin of the document(s) which configured the endpoints. |
| `endpoints` | array of [Network.ReportingApiEndpoint](#type-reportingapiendpoint) |  |

### Network.deviceBoundSessionsAdded

**Experimental**

Triggered when the initial set of device bound sessions is added.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `sessions` | array of [Network.DeviceBoundSession](#type-deviceboundsession) | The device bound sessions. |

### Network.deviceBoundSessionEventOccurred

**Experimental**

Triggered when a device bound session event occurs.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `eventId` | [Network.DeviceBoundSessionEventId](#type-deviceboundsessioneventid) | A unique identifier for this session event. |
| `site` | string | The site this session event is associated with. |
| `succeeded` | boolean | Whether this event was considered successful. |
| `sessionId` (optional) | string | The session ID this event is associated with. May not be populated for failed events. |
| `creationEventDetails` (optional) | [Network.CreationEventDetails](#type-creationeventdetails) | The below are the different session event type details. Exactly one is populated. |
| `refreshEventDetails` (optional) | [Network.RefreshEventDetails](#type-refresheventdetails) |  |
| `terminationEventDetails` (optional) | [Network.TerminationEventDetails](#type-terminationeventdetails) |  |
| `challengeEventDetails` (optional) | [Network.ChallengeEventDetails](#type-challengeeventdetails) |  |

## Types

<a id="type-resourcetype"></a>
### Network.ResourceType

Resource type as it was perceived by the rendering engine.

Type: string

Allowed values: `Document`, `Stylesheet`, `Image`, `Media`, `Font`, `Script`, `TextTrack`, `XHR`, `Fetch`, `Prefetch`, `EventSource`, `WebSocket`, `Manifest`, `SignedExchange`, `Ping`, `CSPViolationReport`, `Preflight`, `FedCM`, `EmailVerification`, `Other`

<a id="type-loaderid"></a>
### Network.LoaderId

Unique loader identifier.

Type: string

<a id="type-requestid"></a>
### Network.RequestId

Unique network request identifier.
Note that this does not identify individual HTTP requests that are part of
a network request.

Type: string

<a id="type-errorreason"></a>
### Network.ErrorReason

Network level fetch failure reason.

Type: string

Allowed values: `Failed`, `Aborted`, `TimedOut`, `AccessDenied`, `ConnectionClosed`, `ConnectionReset`, `ConnectionRefused`, `ConnectionAborted`, `ConnectionFailed`, `NameNotResolved`, `InternetDisconnected`, `AddressUnreachable`, `BlockedByClient`, `BlockedByResponse`

<a id="type-timesinceepoch"></a>
### Network.TimeSinceEpoch

UTC time in seconds, counted from January 1, 1970.

Type: number

<a id="type-monotonictime"></a>
### Network.MonotonicTime

Monotonically increasing time in seconds since an arbitrary point in the past.

Type: number

<a id="type-headers"></a>
### Network.Headers

Request / response headers as keys / values of JSON object.

Type: object

<a id="type-connectiontype"></a>
### Network.ConnectionType

The underlying connection technology that the browser is supposedly using.

Type: string

Allowed values: `none`, `cellular2g`, `cellular3g`, `cellular4g`, `bluetooth`, `ethernet`, `wifi`, `wimax`, `other`

<a id="type-cookiesamesite"></a>
### Network.CookieSameSite

Represents the cookie's 'SameSite' status:
https://tools.ietf.org/html/draft-west-first-party-cookies

Type: string

Allowed values: `Strict`, `Lax`, `None`

<a id="type-cookiepriority"></a>
### Network.CookiePriority

**Experimental**

Represents the cookie's 'Priority' status:
https://tools.ietf.org/html/draft-west-cookie-priority-00

Type: string

Allowed values: `Low`, `Medium`, `High`

<a id="type-cookiesourcescheme"></a>
### Network.CookieSourceScheme

**Experimental**

Represents the source scheme of the origin that originally set the cookie.
A value of "Unset" allows protocol clients to emulate legacy cookie scope for the scheme.
This is a temporary ability and it will be removed in the future.

Type: string

Allowed values: `Unset`, `NonSecure`, `Secure`

<a id="type-resourcetiming"></a>
### Network.ResourceTiming

Timing information for the request.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `requestTime` | number | Timing's requestTime is a baseline in seconds, while the other numbers are ticks in milliseconds relatively to this requestTime. |
| `proxyStart` | number | Started resolving proxy. |
| `proxyEnd` | number | Finished resolving proxy. |
| `dnsStart` | number | Started DNS address resolve. |
| `dnsEnd` | number | Finished DNS address resolve. |
| `connectStart` | number | Started connecting to the remote host. |
| `connectEnd` | number | Connected to the remote host. |
| `sslStart` | number | Started SSL handshake. |
| `sslEnd` | number | Finished SSL handshake. |
| `workerStart` | number | **Experimental** Started running ServiceWorker. |
| `workerReady` | number | **Experimental** Finished Starting ServiceWorker. |
| `workerFetchStart` | number | **Experimental** Started fetch event. |
| `workerRespondWithSettled` | number | **Experimental** Settled fetch event respondWith promise. |
| `workerRouterEvaluationStart` (optional) | number | **Experimental** Started ServiceWorker static routing source evaluation. |
| `workerCacheLookupStart` (optional) | number | **Experimental** Started cache lookup when the source was evaluated to `cache`. |
| `sendStart` | number | Started sending request. |
| `sendEnd` | number | Finished sending request. |
| `pushStart` | number | **Experimental** Time the server started pushing request. |
| `pushEnd` | number | **Experimental** Time the server finished pushing request. |
| `receiveHeadersStart` | number | **Experimental** Started receiving response headers. |
| `receiveHeadersEnd` | number | Finished receiving response headers. |

<a id="type-resourcepriority"></a>
### Network.ResourcePriority

Loading priority of a resource request.

Type: string

Allowed values: `VeryLow`, `Low`, `Medium`, `High`, `VeryHigh`

<a id="type-renderblockingbehavior"></a>
### Network.RenderBlockingBehavior

**Experimental**

The render-blocking behavior of a resource request.

Type: string

Allowed values: `Blocking`, `InBodyParserBlocking`, `NonBlocking`, `NonBlockingDynamic`, `PotentiallyBlocking`

<a id="type-postdataentry"></a>
### Network.PostDataEntry

Post data entry for HTTP request

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `bytes` (optional) | string |  |

<a id="type-request"></a>
### Network.Request

HTTP request data.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `url` | string | Request URL (without fragment). |
| `urlFragment` (optional) | string | Fragment of the requested URL starting with hash, if present. |
| `method` | string | HTTP request method. |
| `headers` | [Network.Headers](#type-headers) | HTTP request headers. |
| `postData` (optional) | string | **Deprecated** HTTP POST request data. Use postDataEntries instead. |
| `hasPostData` (optional) | boolean | True when the request has POST data. Note that postData might still be omitted when this flag is true when the data is too long. |
| `postDataEntries` (optional) | array of [Network.PostDataEntry](#type-postdataentry) | **Experimental** Request body elements (post data broken into individual entries). |
| `mixedContentType` (optional) | [Security.MixedContentType](Security.md#type-mixedcontenttype) | The mixed content type of the request. |
| `initialPriority` | [Network.ResourcePriority](#type-resourcepriority) | Priority of the resource request at the time request is sent. |
| `referrerPolicy` | string | The referrer policy of the request, as defined in https://www.w3.org/TR/referrer-policy/ Allowed values: `unsafe-url`, `no-referrer-when-downgrade`, `no-referrer`, `origin`, `origin-when-cross-origin`, `same-origin`, `strict-origin`, `strict-origin-when-cross-origin` |
| `isLinkPreload` (optional) | boolean | Whether is loaded via link preload. |
| `trustTokenParams` (optional) | [Network.TrustTokenParams](#type-trusttokenparams) | **Experimental** Set for requests when the TrustToken API is used. Contains the parameters passed by the developer (e.g. via "fetch") as understood by the backend. |
| `isSameSite` (optional) | boolean | **Experimental** True if this resource request is considered to be the 'same site' as the request corresponding to the main frame. |
| `isAdRelated` (optional) | boolean | **Experimental** True when the resource request is ad-related. |
| `adProvenance` (optional) | [Network.AdProvenance](#type-adprovenance) | **Experimental** The provenance of an ad resource request, if it is ad-related and provenance is available. |

<a id="type-signedcertificatetimestamp"></a>
### Network.SignedCertificateTimestamp

Details of a signed certificate timestamp (SCT).

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `status` | string | Validation status. |
| `origin` | string | Origin. |
| `logDescription` | string | Log name / description. |
| `logId` | string | Log ID. |
| `timestamp` | number | Issuance date. Unlike TimeSinceEpoch, this contains the number of milliseconds since January 1, 1970, UTC, not the number of seconds. |
| `hashAlgorithm` | string | Hash algorithm. |
| `signatureAlgorithm` | string | Signature algorithm. |
| `signatureData` | string | Signature data. |

<a id="type-securitydetails"></a>
### Network.SecurityDetails

Security details about a request.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `protocol` | string | Protocol name (e.g. "TLS 1.2" or "QUIC"). |
| `keyExchange` | string | Key Exchange used by the connection, or the empty string if not applicable. |
| `keyExchangeGroup` (optional) | string | (EC)DH group used by the connection, if applicable. |
| `cipher` | string | Cipher name. |
| `mac` (optional) | string | TLS MAC. Note that AEAD ciphers do not have separate MACs. |
| `certificateId` | [Security.CertificateId](Security.md#type-certificateid) | Certificate ID value. |
| `subjectName` | string | Certificate subject name. |
| `sanList` | array of string | Subject Alternative Name (SAN) DNS names and IP addresses. |
| `issuer` | string | Name of the issuing CA. |
| `validFrom` | [Network.TimeSinceEpoch](#type-timesinceepoch) | Certificate valid from date. |
| `validTo` | [Network.TimeSinceEpoch](#type-timesinceepoch) | Certificate valid to (expiration) date |
| `signedCertificateTimestampList` | array of [Network.SignedCertificateTimestamp](#type-signedcertificatetimestamp) | List of signed certificate timestamps (SCTs). |
| `certificateTransparencyCompliance` | [Network.CertificateTransparencyCompliance](#type-certificatetransparencycompliance) | Whether the request complied with Certificate Transparency policy |
| `serverSignatureAlgorithm` (optional) | integer | The signature algorithm used by the server in the TLS server signature, represented as a TLS SignatureScheme code point. Omitted if not applicable or not known. |
| `encryptedClientHello` | boolean | Whether the connection used Encrypted ClientHello |

<a id="type-certificatetransparencycompliance"></a>
### Network.CertificateTransparencyCompliance

Whether the request complied with Certificate Transparency policy.

Type: string

Allowed values: `unknown`, `not-compliant`, `compliant`

<a id="type-blockedreason"></a>
### Network.BlockedReason

The reason why request was blocked.

Type: string

Allowed values: `other`, `csp`, `mixed-content`, `origin`, `inspector`, `integrity`, `subresource-filter`, `content-type`, `coep-frame-resource-needs-coep-header`, `coop-sandboxed-iframe-cannot-navigate-to-coop-page`, `corp-not-same-origin`, `corp-not-same-origin-after-defaulted-to-same-origin-by-coep`, `corp-not-same-origin-after-defaulted-to-same-origin-by-dip`, `corp-not-same-origin-after-defaulted-to-same-origin-by-coep-and-dip`, `corp-not-same-site`, `sri-message-signature-mismatch`

<a id="type-corserror"></a>
### Network.CorsError

The reason why request was blocked.

Type: string

Allowed values: `DisallowedByMode`, `InvalidResponse`, `WildcardOriginNotAllowed`, `MissingAllowOriginHeader`, `MultipleAllowOriginValues`, `InvalidAllowOriginValue`, `AllowOriginMismatch`, `InvalidAllowCredentials`, `CorsDisabledScheme`, `PreflightInvalidStatus`, `PreflightDisallowedRedirect`, `PreflightWildcardOriginNotAllowed`, `PreflightMissingAllowOriginHeader`, `PreflightMultipleAllowOriginValues`, `PreflightInvalidAllowOriginValue`, `PreflightAllowOriginMismatch`, `PreflightInvalidAllowCredentials`, `PreflightMissingAllowExternal`, `PreflightInvalidAllowExternal`, `InvalidAllowMethodsPreflightResponse`, `InvalidAllowHeadersPreflightResponse`, `MethodDisallowedByPreflightResponse`, `HeaderDisallowedByPreflightResponse`, `RedirectContainsCredentials`, `InsecureLocalNetwork`, `InvalidLocalNetworkAccess`, `NoCorsRedirectModeNotFollow`, `LocalNetworkAccessPermissionDenied`

<a id="type-corserrorstatus"></a>
### Network.CorsErrorStatus

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `corsError` | [Network.CorsError](#type-corserror) |  |
| `failedParameter` | string |  |

<a id="type-serviceworkerresponsesource"></a>
### Network.ServiceWorkerResponseSource

Source of serviceworker response.

Type: string

Allowed values: `cache-storage`, `http-cache`, `fallback-code`, `network`

<a id="type-trusttokenparams"></a>
### Network.TrustTokenParams

**Experimental**

Determines what type of Trust Token operation is executed and
depending on the type, some additional parameters. The values
are specified in third_party/blink/renderer/core/fetch/trust_token.idl.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `operation` | [Network.TrustTokenOperationType](#type-trusttokenoperationtype) |  |
| `refreshPolicy` | string | Only set for "token-redemption" operation and determine whether to request a fresh SRR or use a still valid cached SRR. Allowed values: `UseCached`, `Refresh` |
| `issuers` (optional) | array of string | Origins of issuers from whom to request tokens or redemption records. |

<a id="type-trusttokenoperationtype"></a>
### Network.TrustTokenOperationType

**Experimental**

Type: string

Allowed values: `Issuance`, `Redemption`, `Signing`

<a id="type-alternateprotocolusage"></a>
### Network.AlternateProtocolUsage

**Experimental**

The reason why Chrome uses a specific transport protocol for HTTP semantics.

Type: string

Allowed values: `alternativeJobWonWithoutRace`, `alternativeJobWonRace`, `mainJobWonRace`, `mappingMissing`, `broken`, `dnsAlpnH3JobWonWithoutRace`, `dnsAlpnH3JobWonRace`, `unspecifiedReason`

<a id="type-serviceworkerroutersource"></a>
### Network.ServiceWorkerRouterSource

Source of service worker router.

Type: string

Allowed values: `network`, `cache`, `fetch-event`, `race-network-and-fetch-handler`, `race-network-and-cache`

<a id="type-serviceworkerrouterinfo"></a>
### Network.ServiceWorkerRouterInfo

**Experimental**

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `ruleIdMatched` (optional) | integer | ID of the rule matched. If there is a matched rule, this field will be set, otherwiser no value will be set. |
| `matchedSourceType` (optional) | [Network.ServiceWorkerRouterSource](#type-serviceworkerroutersource) | The router source of the matched rule. If there is a matched rule, this field will be set, otherwise no value will be set. |
| `actualSourceType` (optional) | [Network.ServiceWorkerRouterSource](#type-serviceworkerroutersource) | The actual router source used. |

<a id="type-response"></a>
### Network.Response

HTTP response data.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `url` | string | Response URL. This URL can be different from CachedResource.url in case of redirect. |
| `status` | integer | HTTP response status code. |
| `statusText` | string | HTTP response status text. |
| `headers` | [Network.Headers](#type-headers) | HTTP response headers. |
| `headersText` (optional) | string | **Deprecated** HTTP response headers text. This has been replaced by the headers in Network.responseReceivedExtraInfo. |
| `mimeType` | string | Resource mimeType as determined by the browser. |
| `charset` | string | Resource charset as determined by the browser (if applicable). |
| `requestHeaders` (optional) | [Network.Headers](#type-headers) | Refined HTTP request headers that were actually transmitted over the network. |
| `requestHeadersText` (optional) | string | **Deprecated** HTTP request headers text. This has been replaced by the headers in Network.requestWillBeSentExtraInfo. |
| `connectionReused` | boolean | Specifies whether physical connection was actually reused for this request. |
| `connectionId` | number | Physical connection id that was actually used for this request. |
| `remoteIPAddress` (optional) | string | Remote IP address. |
| `remotePort` (optional) | integer | Remote port. |
| `fromDiskCache` (optional) | boolean | Specifies that the request was served from the disk cache. |
| `fromServiceWorker` (optional) | boolean | Specifies that the request was served from the ServiceWorker. |
| `fromPrefetchCache` (optional) | boolean | Specifies that the request was served from the prefetch cache. |
| `fromEarlyHints` (optional) | boolean | Specifies that the request was served from the prefetch cache. |
| `serviceWorkerRouterInfo` (optional) | [Network.ServiceWorkerRouterInfo](#type-serviceworkerrouterinfo) | **Experimental** Information about how ServiceWorker Static Router API was used. If this field is set with `matchedSourceType` field, a matching rule is found. If this field is set without `matchedSource`, no matching rule is found. Otherwise, the API is not used. |
| `encodedDataLength` | number | Total number of bytes received for this request so far. |
| `timing` (optional) | [Network.ResourceTiming](#type-resourcetiming) | Timing information for the given request. |
| `serviceWorkerResponseSource` (optional) | [Network.ServiceWorkerResponseSource](#type-serviceworkerresponsesource) | Response source of response from ServiceWorker. |
| `responseTime` (optional) | [Network.TimeSinceEpoch](#type-timesinceepoch) | The time at which the returned response was generated. |
| `cacheStorageCacheName` (optional) | string | Cache Storage Cache Name. |
| `protocol` (optional) | string | Protocol used to fetch this request. |
| `alternateProtocolUsage` (optional) | [Network.AlternateProtocolUsage](#type-alternateprotocolusage) | **Experimental** The reason why Chrome uses a specific transport protocol for HTTP semantics. |
| `securityState` | [Security.SecurityState](Security.md#type-securitystate) | Security state of the request resource. |
| `securityDetails` (optional) | [Network.SecurityDetails](#type-securitydetails) | Security details for the request. |

<a id="type-websocketrequest"></a>
### Network.WebSocketRequest

WebSocket request data.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `headers` | [Network.Headers](#type-headers) | HTTP request headers. |

<a id="type-websocketresponse"></a>
### Network.WebSocketResponse

WebSocket response data.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `status` | integer | HTTP response status code. |
| `statusText` | string | HTTP response status text. |
| `headers` | [Network.Headers](#type-headers) | HTTP response headers. |
| `headersText` (optional) | string | HTTP response headers text. |
| `requestHeaders` (optional) | [Network.Headers](#type-headers) | HTTP request headers. |
| `requestHeadersText` (optional) | string | HTTP request headers text. |

<a id="type-websocketframe"></a>
### Network.WebSocketFrame

WebSocket message data. This represents an entire WebSocket message, not just a fragmented frame as the name suggests.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `opcode` | number | WebSocket message opcode. |
| `mask` | boolean | WebSocket message mask. |
| `payloadData` | string | WebSocket message payload data. If the opcode is 1, this is a text message and payloadData is a UTF-8 string. If the opcode isn't 1, then payloadData is a base64 encoded string representing binary data. |

<a id="type-cachedresource"></a>
### Network.CachedResource

Information about the cached resource.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `url` | string | Resource URL. This is the url of the original network request. |
| `type` | [Network.ResourceType](#type-resourcetype) | Type of this resource. |
| `response` (optional) | [Network.Response](#type-response) | Cached response data. |
| `bodySize` | number | Cached response body size. |

<a id="type-initiator"></a>
### Network.Initiator

Information about the request initiator.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `type` | string | Type of this initiator. Allowed values: `parser`, `script`, `preload`, `SignedExchange`, `preflight`, `FedCM`, `EmailVerification`, `other` |
| `stack` (optional) | [Runtime.StackTrace](Runtime.md#type-stacktrace) | Initiator JavaScript stack trace, set for Script only. Requires the Debugger domain to be enabled. |
| `url` (optional) | string | Initiator URL, set for Parser type or for Script type (when script is importing module) or for SignedExchange type. |
| `lineNumber` (optional) | number | Initiator line number, set for Parser type or for Script type (when script is importing module) (0-based). |
| `columnNumber` (optional) | number | Initiator column number, set for Parser type or for Script type (when script is importing module) (0-based). |
| `requestId` (optional) | [Network.RequestId](#type-requestid) | Set if another request triggered this request (e.g. preflight). |

<a id="type-cookiepartitionkey"></a>
### Network.CookiePartitionKey

**Experimental**

cookiePartitionKey object
The representation of the components of the key that are created by the cookiePartitionKey class contained in net/cookies/cookie_partition_key.h.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `topLevelSite` | string | The site of the top-level URL the browser was visiting at the start of the request to the endpoint that set the cookie. |
| `hasCrossSiteAncestor` | boolean | Indicates if the cookie has any ancestors that are cross-site to the topLevelSite. |

<a id="type-cookie"></a>
### Network.Cookie

Cookie object

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Cookie name. |
| `value` | string | Cookie value. |
| `domain` | string | Cookie domain. |
| `path` | string | Cookie path. |
| `expires` | number | Cookie expiration date as the number of seconds since the UNIX epoch. The value is set to -1 if the expiry date is not set. The value can be null for values that cannot be represented in JSON (±Inf). |
| `size` | integer | Cookie size. |
| `httpOnly` | boolean | True if cookie is http-only. |
| `secure` | boolean | True if cookie is secure. |
| `session` | boolean | True in case of session cookie. |
| `sameSite` (optional) | [Network.CookieSameSite](#type-cookiesamesite) | Cookie SameSite type. |
| `priority` | [Network.CookiePriority](#type-cookiepriority) | **Experimental** Cookie Priority |
| `sourceScheme` | [Network.CookieSourceScheme](#type-cookiesourcescheme) | **Experimental** Cookie source scheme type. |
| `sourcePort` | integer | **Experimental** Cookie source port. Valid values are {-1, [1, 65535]}, -1 indicates an unspecified port. An unspecified port value allows protocol clients to emulate legacy cookie scope for the port. This is a temporary ability and it will be removed in the future. |
| `partitionKey` (optional) | [Network.CookiePartitionKey](#type-cookiepartitionkey) | **Experimental** Cookie partition key. |
| `partitionKeyOpaque` (optional) | boolean | **Experimental** True if cookie partition key is opaque. |

<a id="type-setcookieblockedreason"></a>
### Network.SetCookieBlockedReason

**Experimental**

Types of reasons why a cookie may not be stored from a response.

Type: string

Allowed values: `SecureOnly`, `SameSiteStrict`, `SameSiteLax`, `SameSiteUnspecifiedTreatedAsLax`, `SameSiteNoneInsecure`, `UserPreferences`, `ThirdPartyPhaseout`, `SyntaxError`, `SchemeNotSupported`, `OverwriteSecure`, `InvalidDomain`, `InvalidPrefix`, `UnknownError`, `SchemefulSameSiteStrict`, `SchemefulSameSiteLax`, `SchemefulSameSiteUnspecifiedTreatedAsLax`, `NameValuePairExceedsMaxSize`, `DisallowedCharacter`, `NoCookieContent`

<a id="type-cookieblockedreason"></a>
### Network.CookieBlockedReason

**Experimental**

Types of reasons why a cookie may not be sent with a request.

Type: string

Allowed values: `SecureOnly`, `NotOnPath`, `DomainMismatch`, `SameSiteStrict`, `SameSiteLax`, `SameSiteUnspecifiedTreatedAsLax`, `SameSiteNoneInsecure`, `UserPreferences`, `ThirdPartyPhaseout`, `UnknownError`, `SchemefulSameSiteStrict`, `SchemefulSameSiteLax`, `SchemefulSameSiteUnspecifiedTreatedAsLax`, `NameValuePairExceedsMaxSize`, `PortMismatch`, `SchemeMismatch`, `AnonymousContext`

<a id="type-cookieexemptionreason"></a>
### Network.CookieExemptionReason

**Experimental**

Types of reasons why a cookie should have been blocked by 3PCD but is exempted for the request.

Type: string

Allowed values: `None`, `UserSetting`, `EnterprisePolicy`, `StorageAccess`, `TopLevelStorageAccess`, `Scheme`, `SameSiteNoneCookiesInSandbox`

<a id="type-blockedsetcookiewithreason"></a>
### Network.BlockedSetCookieWithReason

**Experimental**

A cookie which was not stored from a response with the corresponding reason.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `blockedReasons` | array of [Network.SetCookieBlockedReason](#type-setcookieblockedreason) | The reason(s) this cookie was blocked. |
| `cookieLine` | string | The string representing this individual cookie as it would appear in the header. This is not the entire "cookie" or "set-cookie" header which could have multiple cookies. |
| `cookie` (optional) | [Network.Cookie](#type-cookie) | The cookie object which represents the cookie which was not stored. It is optional because sometimes complete cookie information is not available, such as in the case of parsing errors. |

<a id="type-exemptedsetcookiewithreason"></a>
### Network.ExemptedSetCookieWithReason

**Experimental**

A cookie should have been blocked by 3PCD but is exempted and stored from a response with the
corresponding reason. A cookie could only have at most one exemption reason.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `exemptionReason` | [Network.CookieExemptionReason](#type-cookieexemptionreason) | The reason the cookie was exempted. |
| `cookieLine` | string | The string representing this individual cookie as it would appear in the header. |
| `cookie` | [Network.Cookie](#type-cookie) | The cookie object representing the cookie. |

<a id="type-associatedcookie"></a>
### Network.AssociatedCookie

**Experimental**

A cookie associated with the request which may or may not be sent with it.
Includes the cookies itself and reasons for blocking or exemption.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `cookie` | [Network.Cookie](#type-cookie) | The cookie object representing the cookie which was not sent. |
| `blockedReasons` | array of [Network.CookieBlockedReason](#type-cookieblockedreason) | The reason(s) the cookie was blocked. If empty means the cookie is included. |
| `exemptionReason` (optional) | [Network.CookieExemptionReason](#type-cookieexemptionreason) | The reason the cookie should have been blocked by 3PCD but is exempted. A cookie could only have at most one exemption reason. |

<a id="type-cookieparam"></a>
### Network.CookieParam

Cookie parameter object

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Cookie name. |
| `value` | string | Cookie value. |
| `url` (optional) | string | The request-URI to associate with the setting of the cookie. This value can affect the default domain, path, source port, and source scheme values of the created cookie. |
| `domain` (optional) | string | Cookie domain. |
| `path` (optional) | string | Cookie path. |
| `secure` (optional) | boolean | True if cookie is secure. |
| `httpOnly` (optional) | boolean | True if cookie is http-only. |
| `sameSite` (optional) | [Network.CookieSameSite](#type-cookiesamesite) | Cookie SameSite type. |
| `expires` (optional) | [Network.TimeSinceEpoch](#type-timesinceepoch) | Cookie expiration date, session cookie if not set |
| `priority` (optional) | [Network.CookiePriority](#type-cookiepriority) | **Experimental** Cookie Priority. |
| `sourceScheme` (optional) | [Network.CookieSourceScheme](#type-cookiesourcescheme) | **Experimental** Cookie source scheme type. |
| `sourcePort` (optional) | integer | **Experimental** Cookie source port. Valid values are {-1, [1, 65535]}, -1 indicates an unspecified port. An unspecified port value allows protocol clients to emulate legacy cookie scope for the port. This is a temporary ability and it will be removed in the future. |
| `partitionKey` (optional) | [Network.CookiePartitionKey](#type-cookiepartitionkey) | **Experimental** Cookie partition key. If not set, the cookie will be set as not partitioned. |

<a id="type-authchallenge"></a>
### Network.AuthChallenge

**Experimental**

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
### Network.AuthChallengeResponse

**Experimental**

Response to an AuthChallenge.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `response` | string | The decision on what to do in response to the authorization challenge. Default means deferring to the default behavior of the net stack, which will likely either the Cancel authentication or display a popup dialog box. Allowed values: `Default`, `CancelAuth`, `ProvideCredentials` |
| `username` (optional) | string | The username to provide, possibly empty. Should only be set if response is ProvideCredentials. |
| `password` (optional) | string | The password to provide, possibly empty. Should only be set if response is ProvideCredentials. |

<a id="type-signedexchangesignature"></a>
### Network.SignedExchangeSignature

**Experimental**

Information about a signed exchange signature.
https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-signed-exchanges-impl.html#rfc.section.3.1

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `label` | string | Signed exchange signature label. |
| `signature` | string | The hex string of signed exchange signature. |
| `integrity` | string | Signed exchange signature integrity. |
| `certUrl` (optional) | string | Signed exchange signature cert Url. |
| `certSha256` (optional) | string | The hex string of signed exchange signature cert sha256. |
| `validityUrl` | string | Signed exchange signature validity Url. |
| `date` | integer | Signed exchange signature date. |
| `expires` | integer | Signed exchange signature expires. |
| `certificates` (optional) | array of string | The encoded certificates. |

<a id="type-signedexchangeheader"></a>
### Network.SignedExchangeHeader

**Experimental**

Information about a signed exchange header.
https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-signed-exchanges-impl.html#cbor-representation

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `requestUrl` | string | Signed exchange request URL. |
| `responseCode` | integer | Signed exchange response code. |
| `responseHeaders` | [Network.Headers](#type-headers) | Signed exchange response headers. |
| `signatures` | array of [Network.SignedExchangeSignature](#type-signedexchangesignature) | Signed exchange response signature. |
| `headerIntegrity` | string | Signed exchange header integrity hash in the form of `sha256-<base64-hash-value>`. |

<a id="type-signedexchangeerrorfield"></a>
### Network.SignedExchangeErrorField

**Experimental**

Field type for a signed exchange related error.

Type: string

Allowed values: `signatureSig`, `signatureIntegrity`, `signatureCertUrl`, `signatureCertSha256`, `signatureValidityUrl`, `signatureTimestamps`

<a id="type-signedexchangeerror"></a>
### Network.SignedExchangeError

**Experimental**

Information about a signed exchange response.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `message` | string | Error message. |
| `signatureIndex` (optional) | integer | The index of the signature which caused the error. |
| `errorField` (optional) | [Network.SignedExchangeErrorField](#type-signedexchangeerrorfield) | The field which caused the error. |

<a id="type-signedexchangeinfo"></a>
### Network.SignedExchangeInfo

**Experimental**

Information about a signed exchange response.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `outerResponse` | [Network.Response](#type-response) | The outer response of signed HTTP exchange which was received from network. |
| `hasExtraInfo` | boolean | Whether network response for the signed exchange was accompanied by extra headers. |
| `header` (optional) | [Network.SignedExchangeHeader](#type-signedexchangeheader) | Information about the signed exchange header. |
| `securityDetails` (optional) | [Network.SecurityDetails](#type-securitydetails) | Security details for the signed exchange header. |
| `errors` (optional) | array of [Network.SignedExchangeError](#type-signedexchangeerror) | Errors occurred while handling the signed exchange. |

<a id="type-networkconditions"></a>
### Network.NetworkConditions

**Experimental**

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `urlPattern` | string | Only matching requests will be affected by these conditions. Patterns use the URLPattern constructor string syntax (https://urlpattern.spec.whatwg.org/) and must be absolute. If the pattern is empty, all requests are matched (including p2p connections). |
| `latency` | number | Minimum latency from request sent to response headers received (ms). |
| `downloadThroughput` | number | Maximal aggregated download throughput (bytes/sec). -1 disables download throttling. |
| `uploadThroughput` | number | Maximal aggregated upload throughput (bytes/sec). -1 disables upload throttling. |
| `connectionType` (optional) | [Network.ConnectionType](#type-connectiontype) | Connection type if known. |
| `packetLoss` (optional) | number | WebRTC packet loss (percent, 0-100). 0 disables packet loss emulation, 100 drops all the packets. |
| `packetQueueLength` (optional) | integer | WebRTC packet queue length (packet). 0 removes any queue length limitations. |
| `packetReordering` (optional) | boolean | WebRTC packetReordering feature. |
| `offline` (optional) | boolean | True to emulate internet disconnection. |

<a id="type-blockpattern"></a>
### Network.BlockPattern

**Experimental**

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `urlPattern` | string | URL pattern to match. Patterns use the URLPattern constructor string syntax (https://urlpattern.spec.whatwg.org/) and must be absolute. Example: `*://*:*/*.css`. |
| `block` | boolean | Whether or not to block the pattern. If false, a matching request will not be blocked even if it matches a later `BlockPattern`. |

<a id="type-directsocketdnsquerytype"></a>
### Network.DirectSocketDnsQueryType

**Experimental**

Type: string

Allowed values: `ipv4`, `ipv6`

<a id="type-directtcpsocketoptions"></a>
### Network.DirectTCPSocketOptions

**Experimental**

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `noDelay` | boolean | TCP_NODELAY option |
| `keepAliveDelay` (optional) | number | Expected to be unsigned integer. |
| `sendBufferSize` (optional) | number | Expected to be unsigned integer. |
| `receiveBufferSize` (optional) | number | Expected to be unsigned integer. |
| `dnsQueryType` (optional) | [Network.DirectSocketDnsQueryType](#type-directsocketdnsquerytype) |  |

<a id="type-directudpsocketoptions"></a>
### Network.DirectUDPSocketOptions

**Experimental**

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `remoteAddr` (optional) | string |  |
| `remotePort` (optional) | integer | Unsigned int 16. |
| `localAddr` (optional) | string |  |
| `localPort` (optional) | integer | Unsigned int 16. |
| `dnsQueryType` (optional) | [Network.DirectSocketDnsQueryType](#type-directsocketdnsquerytype) |  |
| `sendBufferSize` (optional) | number | Expected to be unsigned integer. |
| `receiveBufferSize` (optional) | number | Expected to be unsigned integer. |
| `multicastLoopback` (optional) | boolean |  |
| `multicastTimeToLive` (optional) | integer | Unsigned int 8. |
| `multicastAllowAddressSharing` (optional) | boolean |  |

<a id="type-directudpmessage"></a>
### Network.DirectUDPMessage

**Experimental**

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `data` | string |  |
| `remoteAddr` (optional) | string | Null for connected mode. |
| `remotePort` (optional) | integer | Null for connected mode. Expected to be unsigned integer. |

<a id="type-localnetworkaccessrequestpolicy"></a>
### Network.LocalNetworkAccessRequestPolicy

**Experimental**

Type: string

Allowed values: `Allow`, `BlockFromInsecureToMorePrivate`, `WarnFromInsecureToMorePrivate`, `PermissionBlock`, `PermissionWarn`

<a id="type-ipaddressspace"></a>
### Network.IPAddressSpace

**Experimental**

Type: string

Allowed values: `Loopback`, `Local`, `Public`, `Unknown`

<a id="type-connecttiming"></a>
### Network.ConnectTiming

**Experimental**

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `requestTime` | number | Timing's requestTime is a baseline in seconds, while the other numbers are ticks in milliseconds relatively to this requestTime. Matches ResourceTiming's requestTime for the same request (but not for redirected requests). |

<a id="type-clientsecuritystate"></a>
### Network.ClientSecurityState

**Experimental**

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `initiatorIsSecureContext` | boolean |  |
| `initiatorIPAddressSpace` | [Network.IPAddressSpace](#type-ipaddressspace) |  |
| `localNetworkAccessRequestPolicy` | [Network.LocalNetworkAccessRequestPolicy](#type-localnetworkaccessrequestpolicy) |  |

<a id="type-adscriptidentifier"></a>
### Network.AdScriptIdentifier

**Experimental**

Identifies the script on the stack that caused a resource or element to be
labeled as an ad. For resources, this indicates the context that triggered
the fetch. For elements, this indicates the context that caused the element
to be appended to the DOM.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `scriptId` | [Runtime.ScriptId](Runtime.md#type-scriptid) | The script's V8 identifier. |
| `debuggerId` | [Runtime.UniqueDebuggerId](Runtime.md#type-uniquedebuggerid) | V8's debugging ID for the v8::Context. |
| `name` | string | The script's url (or generated name based on id if inline script). |

<a id="type-adancestry"></a>
### Network.AdAncestry

**Experimental**

Encapsulates the script ancestry and the root script filter list rule that
caused the resource or element to be labeled as an ad.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `ancestryChain` | array of [Network.AdScriptIdentifier](#type-adscriptidentifier) | A chain of `AdScriptIdentifier`s representing the ancestry of an ad script that led to the creation of a resource or element. The chain is ordered from the script itself (lowest level) up to its root ancestor that was flagged by a filter list. |
| `rootScriptFilterlistRule` (optional) | string | The filter list rule that caused the root (last) script in `ancestryChain` to be tagged as an ad. |

<a id="type-adprovenance"></a>
### Network.AdProvenance

**Experimental**

Represents the provenance of an ad resource or element. Only one of
`filterlistRule` or `adScriptAncestry` can be set. If `filterlistRule`
is provided, the resource URL directly matches a filter list rule. If
`adScriptAncestry` is provided, an ad script initiated the resource fetch or
appended the element to the DOM. If neither is provided, the entity is
known to be an ad, but provenance tracking information is unavailable.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `filterlistRule` (optional) | string | The filterlist rule that matched, if any. |
| `adScriptAncestry` (optional) | [Network.AdAncestry](#type-adancestry) | The script ancestry that created the ad, if any. Note: depending on the context, this may represent the full ancestry up to the root script, or it may contain only one script representing the immediate ancestor. |

<a id="type-crossoriginopenerpolicyvalue"></a>
### Network.CrossOriginOpenerPolicyValue

**Experimental**

Type: string

Allowed values: `SameOrigin`, `SameOriginAllowPopups`, `RestrictProperties`, `UnsafeNone`, `SameOriginPlusCoep`, `RestrictPropertiesPlusCoep`, `NoopenerAllowPopups`

<a id="type-crossoriginopenerpolicystatus"></a>
### Network.CrossOriginOpenerPolicyStatus

**Experimental**

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `value` | [Network.CrossOriginOpenerPolicyValue](#type-crossoriginopenerpolicyvalue) |  |
| `reportOnlyValue` | [Network.CrossOriginOpenerPolicyValue](#type-crossoriginopenerpolicyvalue) |  |
| `reportingEndpoint` (optional) | string |  |
| `reportOnlyReportingEndpoint` (optional) | string |  |

<a id="type-crossoriginembedderpolicyvalue"></a>
### Network.CrossOriginEmbedderPolicyValue

**Experimental**

Type: string

Allowed values: `None`, `Credentialless`, `RequireCorp`

<a id="type-crossoriginembedderpolicystatus"></a>
### Network.CrossOriginEmbedderPolicyStatus

**Experimental**

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `value` | [Network.CrossOriginEmbedderPolicyValue](#type-crossoriginembedderpolicyvalue) |  |
| `reportOnlyValue` | [Network.CrossOriginEmbedderPolicyValue](#type-crossoriginembedderpolicyvalue) |  |
| `reportingEndpoint` (optional) | string |  |
| `reportOnlyReportingEndpoint` (optional) | string |  |

<a id="type-contentsecuritypolicysource"></a>
### Network.ContentSecurityPolicySource

**Experimental**

Type: string

Allowed values: `HTTP`, `Meta`

<a id="type-contentsecuritypolicystatus"></a>
### Network.ContentSecurityPolicyStatus

**Experimental**

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `effectiveDirectives` | string |  |
| `isEnforced` | boolean |  |
| `source` | [Network.ContentSecurityPolicySource](#type-contentsecuritypolicysource) |  |

<a id="type-securityisolationstatus"></a>
### Network.SecurityIsolationStatus

**Experimental**

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `coop` (optional) | [Network.CrossOriginOpenerPolicyStatus](#type-crossoriginopenerpolicystatus) |  |
| `coep` (optional) | [Network.CrossOriginEmbedderPolicyStatus](#type-crossoriginembedderpolicystatus) |  |
| `csp` (optional) | array of [Network.ContentSecurityPolicyStatus](#type-contentsecuritypolicystatus) |  |

<a id="type-reportstatus"></a>
### Network.ReportStatus

**Experimental**

The status of a Reporting API report.

Type: string

Allowed values: `Queued`, `Pending`, `MarkedForRemoval`, `Success`

<a id="type-reportid"></a>
### Network.ReportId

**Experimental**

Type: string

<a id="type-reportingapireport"></a>
### Network.ReportingApiReport

**Experimental**

An object representing a report generated by the Reporting API.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `id` | [Network.ReportId](#type-reportid) |  |
| `initiatorUrl` | string | The URL of the document that triggered the report. |
| `destination` | string | The name of the endpoint group that should be used to deliver the report. |
| `type` | string | The type of the report (specifies the set of data that is contained in the report body). |
| `timestamp` | [Network.TimeSinceEpoch](Network.md#type-timesinceepoch) | When the report was generated. |
| `depth` | integer | How many uploads deep the related request was. |
| `completedAttempts` | integer | The number of delivery attempts made so far, not including an active attempt. |
| `body` | object |  |
| `status` | [Network.ReportStatus](#type-reportstatus) |  |

<a id="type-reportingapiendpoint"></a>
### Network.ReportingApiEndpoint

**Experimental**

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `url` | string | The URL of the endpoint to which reports may be delivered. |
| `groupName` | string | Name of the endpoint group. |

<a id="type-deviceboundsessionkey"></a>
### Network.DeviceBoundSessionKey

**Experimental**

Unique identifier for a device bound session.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `site` | string | The site the session is set up for. |
| `id` | string | The id of the session. |

<a id="type-deviceboundsessionwithusage"></a>
### Network.DeviceBoundSessionWithUsage

**Experimental**

How a device bound session was used during a request.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `sessionKey` | [Network.DeviceBoundSessionKey](#type-deviceboundsessionkey) | The key for the session. |
| `usage` | string | How the session was used (or not used). Allowed values: `NotInScope`, `InScopeRefreshNotYetNeeded`, `InScopeRefreshNotAllowed`, `ProactiveRefreshNotPossible`, `ProactiveRefreshAttempted`, `Deferred` |

<a id="type-deviceboundsessioncookiecraving"></a>
### Network.DeviceBoundSessionCookieCraving

**Experimental**

A device bound session's cookie craving.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | The name of the craving. |
| `domain` | string | The domain of the craving. |
| `path` | string | The path of the craving. |
| `secure` | boolean | The `Secure` attribute of the craving attributes. |
| `httpOnly` | boolean | The `HttpOnly` attribute of the craving attributes. |
| `sameSite` (optional) | [Network.CookieSameSite](#type-cookiesamesite) | The `SameSite` attribute of the craving attributes. |

<a id="type-deviceboundsessionurlrule"></a>
### Network.DeviceBoundSessionUrlRule

**Experimental**

A device bound session's inclusion URL rule.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `ruleType` | string | See comments on `net::device_bound_sessions::SessionInclusionRules::UrlRule::rule_type`. Allowed values: `Exclude`, `Include` |
| `hostPattern` | string | See comments on `net::device_bound_sessions::SessionInclusionRules::UrlRule::host_pattern`. |
| `pathPrefix` | string | See comments on `net::device_bound_sessions::SessionInclusionRules::UrlRule::path_prefix`. |

<a id="type-deviceboundsessioninclusionrules"></a>
### Network.DeviceBoundSessionInclusionRules

**Experimental**

A device bound session's inclusion rules.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `origin` | string | See comments on `net::device_bound_sessions::SessionInclusionRules::origin_`. |
| `includeSite` | boolean | Whether the whole site is included. See comments on `net::device_bound_sessions::SessionInclusionRules::include_site_` for more details; this boolean is true if that value is populated. |
| `urlRules` | array of [Network.DeviceBoundSessionUrlRule](#type-deviceboundsessionurlrule) | See comments on `net::device_bound_sessions::SessionInclusionRules::url_rules_`. |

<a id="type-deviceboundsession"></a>
### Network.DeviceBoundSession

**Experimental**

A device bound session.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `key` | [Network.DeviceBoundSessionKey](#type-deviceboundsessionkey) | The site and session ID of the session. |
| `refreshUrl` | string | See comments on `net::device_bound_sessions::Session::refresh_url_`. |
| `inclusionRules` | [Network.DeviceBoundSessionInclusionRules](#type-deviceboundsessioninclusionrules) | See comments on `net::device_bound_sessions::Session::inclusion_rules_`. |
| `cookieCravings` | array of [Network.DeviceBoundSessionCookieCraving](#type-deviceboundsessioncookiecraving) | See comments on `net::device_bound_sessions::Session::cookie_cravings_`. |
| `expiryDate` | [Network.TimeSinceEpoch](Network.md#type-timesinceepoch) | See comments on `net::device_bound_sessions::Session::expiry_date_`. |
| `cachedChallenge` (optional) | string | See comments on `net::device_bound_sessions::Session::cached_challenge__`. |
| `allowedRefreshInitiators` | array of string | See comments on `net::device_bound_sessions::Session::allowed_refresh_initiators_`. |

<a id="type-deviceboundsessioneventid"></a>
### Network.DeviceBoundSessionEventId

**Experimental**

A unique identifier for a device bound session event.

Type: string

<a id="type-deviceboundsessionfetchresult"></a>
### Network.DeviceBoundSessionFetchResult

**Experimental**

A fetch result for a device bound session creation or refresh.
LINT.IfChange(DeviceBoundSessionFetchResult)

Type: string

Allowed values: `Success`, `SigningKeyGenerationError`, `AttestationKeyGenerationError`, `SigningError`, `TransientSigningError`, `ServerRequestedTermination`, `InvalidSessionId`, `InvalidChallenge`, `TooManyChallenges`, `InvalidFetcherUrl`, `InvalidRefreshUrl`, `TransientHttpError`, `ScopeOriginSameSiteMismatch`, `RefreshUrlSameSiteMismatch`, `MismatchedSessionId`, `MissingScope`, `NoCredentials`, `SubdomainRegistrationWellKnownUnavailable`, `SubdomainRegistrationUnauthorized`, `SubdomainRegistrationWellKnownMalformed`, `SessionProviderWellKnownUnavailable`, `RelyingPartyWellKnownUnavailable`, `FederatedKeyThumbprintMismatch`, `InvalidFederatedSessionUrl`, `InvalidFederatedKey`, `TooManyRelyingOriginLabels`, `BoundCookieSetForbidden`, `NetError`, `ProxyError`, `EmptySessionConfig`, `InvalidCredentialsConfig`, `InvalidCredentialsType`, `InvalidCredentialsEmptyName`, `InvalidCredentialsCookie`, `PersistentHttpError`, `RegistrationAttemptedChallenge`, `InvalidScopeOrigin`, `ScopeOriginContainsPath`, `RefreshInitiatorNotString`, `RefreshInitiatorInvalidHostPattern`, `InvalidScopeSpecification`, `MissingScopeSpecificationType`, `EmptyScopeSpecificationDomain`, `EmptyScopeSpecificationPath`, `InvalidScopeSpecificationType`, `InvalidScopeIncludeSite`, `MissingScopeIncludeSite`, `FederatedNotAuthorizedByProvider`, `FederatedNotAuthorizedByRelyingParty`, `SessionProviderWellKnownMalformed`, `SessionProviderWellKnownHasProviderOrigin`, `RelyingPartyWellKnownMalformed`, `RelyingPartyWellKnownHasRelyingOrigins`, `InvalidFederatedSessionProviderSessionMissing`, `InvalidFederatedSessionWrongProviderOrigin`, `InvalidCredentialsCookieCreationTime`, `InvalidCredentialsCookieName`, `InvalidCredentialsCookieParsing`, `InvalidCredentialsCookieUnpermittedAttribute`, `InvalidCredentialsCookieInvalidDomain`, `InvalidCredentialsCookiePrefix`, `InvalidScopeRulePath`, `InvalidScopeRuleHostPattern`, `ScopeRuleOriginScopedHostPatternMismatch`, `ScopeRuleSiteScopedHostPatternMismatch`, `SigningQuotaExceeded`, `InvalidConfigJson`, `InvalidFederatedSessionProviderFailedToRestoreKey`, `FailedToUnwrapKey`, `SessionDeletedDuringRefresh`, `CrossOriginRegistrationSiteNotIncluded`, `InvalidPreProvisionedKeyInitiatorMissing`, `PreProvisionedKeyAccessNotGranted`, `PreProvisionedKeyNotFound`, `AttestationCertificationError`, `AttestationSigningError`, `FederatedRegistrationRedirected`, `CrossSiteRefreshSessionConfig`

<a id="type-deviceboundsessionfailedrequest"></a>
### Network.DeviceBoundSessionFailedRequest

**Experimental**

Details about a failed device bound session network request.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `requestUrl` | string | The failed request URL. |
| `netError` (optional) | string | The net error of the response if it was not OK. |
| `responseError` (optional) | integer | The response code if the net error was OK and the response code was not 200. |
| `responseErrorBody` (optional) | string | The body of the response if the net error was OK, the response code was not 200, and the response body was not empty. |

<a id="type-creationeventdetails"></a>
### Network.CreationEventDetails

**Experimental**

Session event details specific to creation.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `fetchResult` | [Network.DeviceBoundSessionFetchResult](#type-deviceboundsessionfetchresult) | The result of the fetch attempt. |
| `newSession` (optional) | [Network.DeviceBoundSession](#type-deviceboundsession) | The session if there was a newly created session. This is populated for all successful creation events. |
| `failedRequest` (optional) | [Network.DeviceBoundSessionFailedRequest](#type-deviceboundsessionfailedrequest) | Details about a failed device bound session network request if there was one. |

<a id="type-refresheventdetails"></a>
### Network.RefreshEventDetails

**Experimental**

Session event details specific to refresh.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `refreshResult` | string | The result of a refresh. LINT.IfChange(DeviceBoundSessionRefreshResult) Allowed values: `Refreshed`, `InitializedService`, `Unreachable`, `ServerError`, `FatalError`, `SigningQuotaExceeded`, `RefreshedAsWaiter`, `TransientSigningError`, `InScopeRefreshNotYetNeeded`, `Canceled` |
| `fetchResult` (optional) | [Network.DeviceBoundSessionFetchResult](#type-deviceboundsessionfetchresult) | LINT.ThenChange(//net/device_bound_sessions/refresh_result.h:DeviceBoundSessionRefreshResult,//content/browser/devtools/protocol/network_handler.cc:DeviceBoundSessionRefreshResult) If there was a fetch attempt, the result of that. |
| `newSession` (optional) | [Network.DeviceBoundSession](#type-deviceboundsession) | The session display if there was a newly created session. This is populated for any refresh event that modifies the session config. |
| `wasFullyProactiveRefresh` | boolean | See comments on `net::device_bound_sessions::RefreshEventResult::was_fully_proactive_refresh`. |
| `failedRequest` (optional) | [Network.DeviceBoundSessionFailedRequest](#type-deviceboundsessionfailedrequest) | Details about a failed device bound session network request if there was one. |

<a id="type-terminationeventdetails"></a>
### Network.TerminationEventDetails

**Experimental**

Session event details specific to termination.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `deletionReason` | string | The reason for a session being deleted. Allowed values: `Expired`, `FailedToRestoreKey`, `FailedToUnwrapKey`, `StoragePartitionCleared`, `ClearBrowsingData`, `ServerRequested`, `InvalidSessionParams`, `RefreshFatalError`, `DevTools`, `Replaced` |

<a id="type-challengeeventdetails"></a>
### Network.ChallengeEventDetails

**Experimental**

Session event details specific to challenges.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `challengeResult` | string | The result of a challenge. Allowed values: `Success`, `NoSessionId`, `NoSessionMatch`, `CantSetBoundCookie` |
| `challenge` | string | The challenge set. |

<a id="type-loadnetworkresourcepageresult"></a>
### Network.LoadNetworkResourcePageResult

**Experimental**

An object providing the result of a network resource load.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `success` | boolean |  |
| `netError` (optional) | number | Optional values used for error reporting. |
| `netErrorName` (optional) | string |  |
| `httpStatusCode` (optional) | number |  |
| `stream` (optional) | [IO.StreamHandle](IO.md#type-streamhandle) | If successful, one of the following two fields holds the result. |
| `headers` (optional) | [Network.Headers](Network.md#type-headers) | Response headers. |

<a id="type-loadnetworkresourceoptions"></a>
### Network.LoadNetworkResourceOptions

**Experimental**

An options object that may be extended later to better support CORS,
CORB and streaming.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `disableCache` | boolean |  |
| `includeCredentials` | boolean |  |
