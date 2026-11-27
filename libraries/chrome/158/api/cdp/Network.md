# Network domain

Copyright 2017 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.  Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp Network domain allows tracking network activities of the page. It exposes information about http, file, data and other requests and responses, their headers, bodies, timing, etc.

Depends on: [Debugger](Debugger.md), [Runtime](Runtime.md), [Security](Security.md)

Methods are called as `Network.<command>` and events arrive as `Network.<event>`.

## Commands

### Network.canClearBrowserCache *(deprecated)*

Tells whether clearing browser cache is supported.

**Returns**

| Name | Type | Description |
|---|---|---|
| `result` | boolean | True if browser cache can be cleared. |

### Network.canClearBrowserCookies *(deprecated)*

Tells whether clearing browser cookies is supported.

**Returns**

| Name | Type | Description |
|---|---|---|
| `result` | boolean | True if browser cookies can be cleared. |

### Network.canEmulateNetworkConditions *(deprecated)*

Tells whether emulation of network conditions is supported.

**Returns**

| Name | Type | Description |
|---|---|---|
| `result` | boolean | True if emulation of network conditions is supported. |

### Network.clearBrowserCache

Clears browser cache.

### Network.clearBrowserCookies

Clears browser cookies.

### Network.deleteCookies

Deletes browser cookies with matching name and url or domain/path/partitionKey pair.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `name` | string | Name of the cookies to remove. |
| `url` (optional) | string | If specified, deletes all the cookies with the given name where domain and path match provided URL. |
| `domain` (optional) | string | If specified, deletes only cookies with the exact domain. |
| `path` (optional) | string | If specified, deletes only cookies with the exact path. |
| `partitionKey` (optional) *(experimental)* | [CookiePartitionKey](#type-cookiepartitionkey) | If specified, deletes only cookies with the the given name and partitionKey where all partition key attributes match the cookie partition key attribute. |

### Network.disable

Disables network tracking, prevents network events from being sent to the client.

### Network.emulateNetworkConditions *(deprecated)*

Activates emulation of network conditions. This command is deprecated in favor of the emulateNetworkConditionsByRule and overrideNetworkState commands, which can be used together to the same effect.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `offline` | boolean | True to emulate internet disconnection. |
| `latency` | number | Minimum latency from request sent to response headers received (ms). |
| `downloadThroughput` | number | Maximal aggregated download throughput (bytes/sec). -1 disables download throttling. |
| `uploadThroughput` | number | Maximal aggregated upload throughput (bytes/sec).  -1 disables upload throttling. |
| `connectionType` (optional) | [ConnectionType](#type-connectiontype) | Connection type if known. |
| `packetLoss` (optional) *(experimental)* | number | WebRTC packet loss (percent, 0-100). 0 disables packet loss emulation, 100 drops all the packets. |
| `packetQueueLength` (optional) *(experimental)* | integer | WebRTC packet queue length (packet). 0 removes any queue length limitations. |
| `packetReordering` (optional) *(experimental)* | boolean | WebRTC packetReordering feature. |

### Network.emulateNetworkConditionsByRule *(experimental)*

Activates emulation of network conditions for individual requests using URL match patterns. Unlike the deprecated Network.emulateNetworkConditions this method does not affect `navigator` state. Use Network.overrideNetworkState to explicitly modify `navigator` behavior.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `offline` (optional) *(deprecated)* | boolean | True to emulate internet disconnection. Deprecated, use the offline property in matchedNetworkConditions or emulateOfflineServiceWorker instead. |
| `emulateOfflineServiceWorker` (optional) | boolean | True to emulate offline service worker. |
| `matchedNetworkConditions` | array of [NetworkConditions](#type-networkconditions) | Configure conditions for matching requests. If multiple entries match a request, the first entry wins.  Global conditions can be configured by leaving the urlPattern for the conditions empty. These global conditions are also applied for throttling of p2p connections. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `ruleIds` | array of string | An id for each entry in matchedNetworkConditions. The id will be included in the requestWillBeSentExtraInfo for requests affected by a rule. |

### Network.overrideNetworkState *(experimental)*

Override the state of navigator.onLine and navigator.connection.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `offline` | boolean | True to emulate internet disconnection. |
| `latency` | number | Minimum latency from request sent to response headers received (ms). |
| `downloadThroughput` | number | Maximal aggregated download throughput (bytes/sec). -1 disables download throttling. |
| `uploadThroughput` | number | Maximal aggregated upload throughput (bytes/sec).  -1 disables upload throttling. |
| `connectionType` (optional) | [ConnectionType](#type-connectiontype) | Connection type if known. |

### Network.enable

Enables network tracking, network events will now be delivered to the client.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `maxTotalBufferSize` (optional) *(experimental)* | integer | Buffer size in bytes to use when preserving network payloads (XHRs, etc). This is the maximum number of bytes that will be collected by this DevTools session. |
| `maxResourceBufferSize` (optional) *(experimental)* | integer | Per-resource buffer size in bytes to use when preserving network payloads (XHRs, etc). |
| `maxPostDataSize` (optional) | integer | Longest post body size (in bytes) that would be included in requestWillBeSent notification |
| `reportDirectSocketTraffic` (optional) *(experimental)* | boolean | Whether DirectSocket chunk send/receive events should be reported. |
| `enableDurableMessages` (optional) *(experimental)* | boolean | Enable storing response bodies outside of renderer, so that these survive a cross-process navigation. Requires maxTotalBufferSize to be set. Currently defaults to false. This field is being deprecated in favor of the dedicated configureDurableMessages command, due to the possibility of deadlocks when awaiting Network.enable before issuing Runtime.runIfWaitingForDebugger. |

### Network.configureDurableMessages *(experimental)*

Configures storing response bodies outside of renderer, so that these survive a cross-process navigation. If maxTotalBufferSize is not set, durable messages are disabled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `maxTotalBufferSize` (optional) | integer | Buffer size in bytes to use when preserving network payloads (XHRs, etc). |
| `maxResourceBufferSize` (optional) | integer | Per-resource buffer size in bytes to use when preserving network payloads (XHRs, etc). |

### Network.getAllCookies *(deprecated)*

Returns all browser cookies. Depending on the backend support, will return detailed cookie information in the `cookies` field. Deprecated. Use Storage.getCookies instead.

**Returns**

| Name | Type | Description |
|---|---|---|
| `cookies` | array of [Cookie](#type-cookie) | Array of cookie objects. |

### Network.getCertificate *(experimental)*

Returns the DER-encoded certificate.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `origin` | string | Origin to get certificate for. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `tableNames` | array of string |  |

### Network.getCookies

Returns all browser cookies for the current URL. Depending on the backend support, will return detailed cookie information in the `cookies` field.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `urls` (optional) | array of string | The list of URLs for which applicable cookies will be fetched. If not specified, it's assumed to be set to the list containing the URLs of the page and all of its subframes. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `cookies` | array of [Cookie](#type-cookie) | Array of cookie objects. |

### Network.getResponseBody

Returns content served for the given request.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [RequestId](#type-requestid) | Identifier of the network request to get content for. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `body` | string | Response body. |
| `base64Encoded` | boolean | True, if content was sent as base64. |

### Network.getRequestPostData

Returns post data sent with the request. Returns an error when no data was sent with the request.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [RequestId](#type-requestid) | Identifier of the network request to get content for. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `postData` | string | Request body string, omitting files from multipart requests |
| `base64Encoded` | boolean | True, if content was sent as base64. |

### Network.replayXHR *(experimental)*

This method sends a new XMLHttpRequest which is identical to the original one. The following parameters should be identical: method, url, async, request body, extra headers, withCredentials attribute, user, password.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [RequestId](#type-requestid) | Identifier of XHR to replay. |

### Network.searchInResponseBody *(experimental)*

Searches for given string in response content.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [RequestId](#type-requestid) | Identifier of the network response to search. |
| `query` | string | String to search for. |
| `caseSensitive` (optional) | boolean | If true, search is case sensitive. |
| `isRegex` (optional) | boolean | If true, treats string parameter as regex. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `result` | array of [Debugger.SearchMatch](Debugger.md#type-searchmatch) | List of search matches. |

### Network.setBlockedURLs *(experimental)*

Blocks URLs from loading.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `urlPatterns` (optional) | array of [BlockPattern](#type-blockpattern) | Patterns to match in the order in which they are given. These patterns also take precedence over any wildcard patterns defined in `urls`. |
| `urls` (optional) *(deprecated)* | array of string | URL patterns to block. Wildcards ('*') are allowed. |

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
| `sameSite` (optional) | [CookieSameSite](#type-cookiesamesite) | Cookie SameSite type. |
| `expires` (optional) | [TimeSinceEpoch](#type-timesinceepoch) | Cookie expiration date, session cookie if not set |
| `priority` (optional) *(experimental)* | [CookiePriority](#type-cookiepriority) | Cookie Priority type. |
| `sourceScheme` (optional) *(experimental)* | [CookieSourceScheme](#type-cookiesourcescheme) | Cookie source scheme type. |
| `sourcePort` (optional) *(experimental)* | integer | Cookie source port. Valid values are {-1, [1, 65535]}, -1 indicates an unspecified port. An unspecified port value allows protocol clients to emulate legacy cookie scope for the port. This is a temporary ability and it will be removed in the future. |
| `partitionKey` (optional) *(experimental)* | [CookiePartitionKey](#type-cookiepartitionkey) | Cookie partition key. If not set, the cookie will be set as not partitioned. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `success` *(deprecated)* | boolean | Always set to true. If an error occurs, the response indicates protocol error. |

### Network.setCookies

Sets given cookies.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `cookies` | array of [CookieParam](#type-cookieparam) | Cookies to be set. |

### Network.setExtraHTTPHeaders

Specifies whether to always send extra HTTP headers with the requests from this page.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `headers` | [Headers](#type-headers) | Map with extra HTTP headers. |

### Network.setAttachDebugStack *(experimental)*

Specifies whether to attach a page script stack id in requests

**Parameters**

| Name | Type | Description |
|---|---|---|
| `enabled` | boolean | Whether to attach a page script stack for debugging purpose. |

### Network.setUserAgentOverride

Allows overriding user agent with the given string.

Redirects to `Emulation`.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `userAgent` | string | User agent to use. |
| `acceptLanguage` (optional) | string | Browser language to emulate. |
| `platform` (optional) | string | The platform navigator.platform should return. |
| `userAgentMetadata` (optional) *(experimental)* | [Emulation.UserAgentMetadata](Emulation.md#type-useragentmetadata) | To be sent in Sec-CH-UA-* headers and returned in navigator.userAgentData |

### Network.streamResourceContent *(experimental)*

Enables streaming of the response for the given requestId. If enabled, the dataReceived event contains the data that was received during streaming.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [RequestId](#type-requestid) | Identifier of the request to stream. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `bufferedData` | binary | Data that has been buffered until streaming is enabled. |

### Network.getSecurityIsolationStatus *(experimental)*

Returns information about the COEP/COOP isolation status.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frameId` (optional) | [Page.FrameId](Page.md#type-frameid) | If no frameId is provided, the status of the target is provided. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `status` | [SecurityIsolationStatus](#type-securityisolationstatus) |  |

### Network.enableReportingApi *(experimental)*

Enables tracking for the Reporting API, events generated by the Reporting API will now be delivered to the client. Enabling triggers 'reportingApiReportAdded' for all existing reports.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `enable` | boolean | Whether to enable or disable events for the Reporting API |

### Network.enableDeviceBoundSessions *(experimental)*

Sets up tracking device bound sessions and fetching of initial set of sessions.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `enable` | boolean | Whether to enable or disable events. |

### Network.deleteDeviceBoundSession *(experimental)*

Deletes a device bound session.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `key` | [DeviceBoundSessionKey](#type-deviceboundsessionkey) |  |

### Network.fetchSchemefulSite *(experimental)*

Fetches the schemeful site for a specific origin.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `origin` | string | The URL origin. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `schemefulSite` | string | The corresponding schemeful site. |

### Network.loadNetworkResource *(experimental)*

Fetches the resource and returns the content.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frameId` (optional) | [Page.FrameId](Page.md#type-frameid) | Frame id to get the resource for. Mandatory for frame targets, and should be omitted for worker targets. |
| `url` | string | URL of the resource to get content for. |
| `options` | [LoadNetworkResourceOptions](#type-loadnetworkresourceoptions) | Options for the request. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `resource` | [LoadNetworkResourcePageResult](#type-loadnetworkresourcepageresult) |  |

### Network.setCookieControls *(experimental)*

Sets Controls for third-party cookie access Page reload is required before the new cookie behavior will be observed

**Parameters**

| Name | Type | Description |
|---|---|---|
| `enableThirdPartyCookieRestriction` | boolean | Whether 3pc restriction is enabled. |

## Events

### Network.dataReceived

Fired when data chunk was received over the network.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [RequestId](#type-requestid) | Request identifier. |
| `timestamp` | [MonotonicTime](#type-monotonictime) | Timestamp. |
| `dataLength` | integer | Data chunk length. |
| `encodedDataLength` | integer | Actual bytes received (might be less than dataLength for compressed encodings). |
| `data` (optional) *(experimental)* | binary | Data that was received. |

### Network.eventSourceMessageReceived

Fired when EventSource message is received.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [RequestId](#type-requestid) | Request identifier. |
| `timestamp` | [MonotonicTime](#type-monotonictime) | Timestamp. |
| `eventName` | string | Message type. |
| `eventId` | string | Message identifier. |
| `data` | string | Message content. |

### Network.loadingFailed

Fired when HTTP request has failed to load.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [RequestId](#type-requestid) | Request identifier. |
| `timestamp` | [MonotonicTime](#type-monotonictime) | Timestamp. |
| `type` | [ResourceType](#type-resourcetype) | Resource type. |
| `errorText` | string | Error message. List of network errors: https://cs.chromium.org/chromium/src/net/base/net_error_list.h |
| `canceled` (optional) | boolean | True if loading was canceled. |
| `blockedReason` (optional) | [BlockedReason](#type-blockedreason) | The reason why loading was blocked, if any. |
| `corsErrorStatus` (optional) | [CorsErrorStatus](#type-corserrorstatus) | The reason why loading was blocked by CORS, if any. |

### Network.loadingFinished

Fired when HTTP request has finished loading.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [RequestId](#type-requestid) | Request identifier. |
| `timestamp` | [MonotonicTime](#type-monotonictime) | Timestamp. |
| `encodedDataLength` | number | Total number of bytes received for this request. |
| `encodedBodyLength` (optional) *(experimental)* | number | Size of the response body before removing content encodings. Includes cached bodies, but excludes headers and transfer framing. |

### Network.requestServedFromCache

Fired if request ended up loading from cache.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [RequestId](#type-requestid) | Request identifier. |

### Network.requestWillBeSent

Fired when page is about to send HTTP request.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [RequestId](#type-requestid) | Request identifier. |
| `loaderId` | [LoaderId](#type-loaderid) | Loader identifier. Empty string if the request is fetched from worker. |
| `documentURL` | string | URL of the document this request is loaded for. |
| `request` | [Request](#type-request) | Request data. |
| `timestamp` | [MonotonicTime](#type-monotonictime) | Timestamp. |
| `wallTime` | [TimeSinceEpoch](#type-timesinceepoch) | Timestamp. |
| `initiator` | [Initiator](#type-initiator) | Request initiator. |
| `redirectHasExtraInfo` *(experimental)* | boolean | In the case that redirectResponse is populated, this flag indicates whether requestWillBeSentExtraInfo and responseReceivedExtraInfo events will be or were emitted for the request which was just redirected. |
| `redirectResponse` (optional) | [Response](#type-response) | Redirect response data. |
| `type` (optional) | [ResourceType](#type-resourcetype) | Type of this resource. |
| `frameId` (optional) | [Page.FrameId](Page.md#type-frameid) | Frame identifier. |
| `hasUserGesture` (optional) | boolean | Whether the request is initiated by a user gesture. Defaults to false. |
| `renderBlockingBehavior` (optional) *(experimental)* | [RenderBlockingBehavior](#type-renderblockingbehavior) | The render-blocking behavior of the request. |

### Network.resourceChangedPriority *(experimental)*

Fired when resource loading priority is changed

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [RequestId](#type-requestid) | Request identifier. |
| `newPriority` | [ResourcePriority](#type-resourcepriority) | New priority |
| `timestamp` | [MonotonicTime](#type-monotonictime) | Timestamp. |

### Network.signedExchangeReceived *(experimental)*

Fired when a signed exchange was received over the network

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [RequestId](#type-requestid) | Request identifier. |
| `info` | [SignedExchangeInfo](#type-signedexchangeinfo) | Information about the signed exchange response. |

### Network.responseReceived

Fired when HTTP response is available.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [RequestId](#type-requestid) | Request identifier. |
| `loaderId` | [LoaderId](#type-loaderid) | Loader identifier. Empty string if the request is fetched from worker. |
| `timestamp` | [MonotonicTime](#type-monotonictime) | Timestamp. |
| `type` | [ResourceType](#type-resourcetype) | Resource type. |
| `response` | [Response](#type-response) | Response data. |
| `hasExtraInfo` *(experimental)* | boolean | Indicates whether requestWillBeSentExtraInfo and responseReceivedExtraInfo events will be or were emitted for this request. |
| `frameId` (optional) | [Page.FrameId](Page.md#type-frameid) | Frame identifier. |

### Network.webSocketClosed

Fired when WebSocket is closed.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [RequestId](#type-requestid) | Request identifier. |
| `timestamp` | [MonotonicTime](#type-monotonictime) | Timestamp. |

### Network.webSocketCreated

Fired upon WebSocket creation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [RequestId](#type-requestid) | Request identifier. |
| `url` | string | WebSocket request URL. |
| `initiator` (optional) | [Initiator](#type-initiator) | Request initiator. |

### Network.webSocketFrameError

Fired when WebSocket message error occurs.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [RequestId](#type-requestid) | Request identifier. |
| `timestamp` | [MonotonicTime](#type-monotonictime) | Timestamp. |
| `errorMessage` | string | WebSocket error message. |

### Network.webSocketFrameReceived

Fired when WebSocket message is received.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [RequestId](#type-requestid) | Request identifier. |
| `timestamp` | [MonotonicTime](#type-monotonictime) | Timestamp. |
| `response` | [WebSocketFrame](#type-websocketframe) | WebSocket response data. |

### Network.webSocketFrameSent

Fired when WebSocket message is sent.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [RequestId](#type-requestid) | Request identifier. |
| `timestamp` | [MonotonicTime](#type-monotonictime) | Timestamp. |
| `response` | [WebSocketFrame](#type-websocketframe) | WebSocket response data. |

### Network.webSocketHandshakeResponseReceived

Fired when WebSocket handshake response becomes available.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [RequestId](#type-requestid) | Request identifier. |
| `timestamp` | [MonotonicTime](#type-monotonictime) | Timestamp. |
| `response` | [WebSocketResponse](#type-websocketresponse) | WebSocket response data. |

### Network.webSocketWillSendHandshakeRequest

Fired when WebSocket is about to initiate handshake.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [RequestId](#type-requestid) | Request identifier. |
| `timestamp` | [MonotonicTime](#type-monotonictime) | Timestamp. |
| `wallTime` | [TimeSinceEpoch](#type-timesinceepoch) | UTC Timestamp. |
| `request` | [WebSocketRequest](#type-websocketrequest) | WebSocket request data. |

### Network.webTransportCreated

Fired upon WebTransport creation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `transportId` | [RequestId](#type-requestid) | WebTransport identifier. |
| `url` | string | WebTransport request URL. |
| `timestamp` | [MonotonicTime](#type-monotonictime) | Timestamp. |
| `initiator` (optional) | [Initiator](#type-initiator) | Request initiator. |

### Network.webTransportConnectionEstablished

Fired when WebTransport handshake is finished.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `transportId` | [RequestId](#type-requestid) | WebTransport identifier. |
| `timestamp` | [MonotonicTime](#type-monotonictime) | Timestamp. |

### Network.webTransportClosed

Fired when WebTransport is disposed.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `transportId` | [RequestId](#type-requestid) | WebTransport identifier. |
| `timestamp` | [MonotonicTime](#type-monotonictime) | Timestamp. |

### Network.directTCPSocketCreated *(experimental)*

Fired upon direct_socket.TCPSocket creation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `identifier` | [RequestId](#type-requestid) |  |
| `remoteAddr` | string |  |
| `remotePort` | integer | Unsigned int 16. |
| `options` | [DirectTCPSocketOptions](#type-directtcpsocketoptions) |  |
| `timestamp` | [MonotonicTime](#type-monotonictime) |  |
| `initiator` (optional) | [Initiator](#type-initiator) |  |

### Network.directTCPSocketOpened *(experimental)*

Fired when direct_socket.TCPSocket connection is opened.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `identifier` | [RequestId](#type-requestid) |  |
| `remoteAddr` | string |  |
| `remotePort` | integer | Expected to be unsigned integer. |
| `timestamp` | [MonotonicTime](#type-monotonictime) |  |
| `localAddr` (optional) | string |  |
| `localPort` (optional) | integer | Expected to be unsigned integer. |

### Network.directTCPSocketAborted *(experimental)*

Fired when direct_socket.TCPSocket is aborted.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `identifier` | [RequestId](#type-requestid) |  |
| `errorMessage` | [ErrorReason](#type-errorreason) |  |
| `timestamp` | [MonotonicTime](#type-monotonictime) |  |

### Network.directTCPSocketClosed *(experimental)*

Fired when direct_socket.TCPSocket is closed.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `identifier` | [RequestId](#type-requestid) |  |
| `timestamp` | [MonotonicTime](#type-monotonictime) |  |

### Network.directTCPSocketChunkSent *(experimental)*

Fired when data is sent to tcp direct socket stream.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `identifier` | [RequestId](#type-requestid) |  |
| `data` | binary |  |
| `timestamp` | [MonotonicTime](#type-monotonictime) |  |

### Network.directTCPSocketChunkReceived *(experimental)*

Fired when data is received from tcp direct socket stream.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `identifier` | [RequestId](#type-requestid) |  |
| `data` | binary |  |
| `timestamp` | [MonotonicTime](#type-monotonictime) |  |

### Network.directUDPSocketJoinedMulticastGroup *(experimental)*

**Parameters**

| Name | Type | Description |
|---|---|---|
| `identifier` | [RequestId](#type-requestid) |  |
| `IPAddress` | string | Multicast group address. |
| `sourceAddress` (optional) | string | Source address of a source-specific multicast (SSM) membership. Absent for any-source multicast (ASM) memberships. |

### Network.directUDPSocketLeftMulticastGroup *(experimental)*

**Parameters**

| Name | Type | Description |
|---|---|---|
| `identifier` | [RequestId](#type-requestid) |  |
| `IPAddress` | string | Multicast group address. |
| `sourceAddress` (optional) | string | Source address of a source-specific multicast (SSM) membership. Absent for any-source multicast (ASM) memberships. |

### Network.directUDPSocketCreated *(experimental)*

Fired upon direct_socket.UDPSocket creation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `identifier` | [RequestId](#type-requestid) |  |
| `options` | [DirectUDPSocketOptions](#type-directudpsocketoptions) |  |
| `timestamp` | [MonotonicTime](#type-monotonictime) |  |
| `initiator` (optional) | [Initiator](#type-initiator) |  |

### Network.directUDPSocketOpened *(experimental)*

Fired when direct_socket.UDPSocket connection is opened.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `identifier` | [RequestId](#type-requestid) |  |
| `localAddr` | string |  |
| `localPort` | integer | Expected to be unsigned integer. |
| `timestamp` | [MonotonicTime](#type-monotonictime) |  |
| `remoteAddr` (optional) | string |  |
| `remotePort` (optional) | integer | Expected to be unsigned integer. |

### Network.directUDPSocketAborted *(experimental)*

Fired when direct_socket.UDPSocket is aborted.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `identifier` | [RequestId](#type-requestid) |  |
| `errorMessage` | [ErrorReason](#type-errorreason) |  |
| `timestamp` | [MonotonicTime](#type-monotonictime) |  |

### Network.directUDPSocketClosed *(experimental)*

Fired when direct_socket.UDPSocket is closed.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `identifier` | [RequestId](#type-requestid) |  |
| `timestamp` | [MonotonicTime](#type-monotonictime) |  |

### Network.directUDPSocketChunkSent *(experimental)*

Fired when message is sent to udp direct socket stream.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `identifier` | [RequestId](#type-requestid) |  |
| `message` | [DirectUDPMessage](#type-directudpmessage) |  |
| `timestamp` | [MonotonicTime](#type-monotonictime) |  |

### Network.directUDPSocketChunkReceived *(experimental)*

Fired when message is received from udp direct socket stream.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `identifier` | [RequestId](#type-requestid) |  |
| `message` | [DirectUDPMessage](#type-directudpmessage) |  |
| `timestamp` | [MonotonicTime](#type-monotonictime) |  |

### Network.requestWillBeSentExtraInfo *(experimental)*

Fired when additional information about a requestWillBeSent event is available from the network stack. Not every requestWillBeSent event will have an additional requestWillBeSentExtraInfo fired for it, and there is no guarantee whether requestWillBeSent or requestWillBeSentExtraInfo will be fired first for the same request.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [RequestId](#type-requestid) | Request identifier. Used to match this information to an existing requestWillBeSent event. |
| `associatedCookies` | array of [AssociatedCookie](#type-associatedcookie) | A list of cookies potentially associated to the requested URL. This includes both cookies sent with the request and the ones not sent; the latter are distinguished by having blockedReasons field set. |
| `headers` | [Headers](#type-headers) | Raw request headers as they will be sent over the wire. |
| `connectTiming` *(experimental)* | [ConnectTiming](#type-connecttiming) | Connection timing information for the request. |
| `deviceBoundSessionUsages` (optional) | array of [DeviceBoundSessionWithUsage](#type-deviceboundsessionwithusage) | How the request site's device bound sessions were used during this request. |
| `clientSecurityState` (optional) | [ClientSecurityState](#type-clientsecuritystate) | The client security state set for the request. |
| `siteHasCookieInOtherPartition` (optional) | boolean | Whether the site has partitioned cookies stored in a partition different than the current one. |
| `appliedNetworkConditionsId` (optional) | string | The network conditions id if this request was affected by network conditions configured via emulateNetworkConditionsByRule. |

### Network.responseReceivedExtraInfo *(experimental)*

Fired when additional information about a responseReceived event is available from the network stack. Not every responseReceived event will have an additional responseReceivedExtraInfo for it, and responseReceivedExtraInfo may be fired before or after responseReceived.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [RequestId](#type-requestid) | Request identifier. Used to match this information to another responseReceived event. |
| `blockedCookies` | array of [BlockedSetCookieWithReason](#type-blockedsetcookiewithreason) | A list of cookies which were not stored from the response along with the corresponding reasons for blocking. The cookies here may not be valid due to syntax errors, which are represented by the invalid cookie line string instead of a proper cookie. |
| `headers` | [Headers](#type-headers) | Raw response headers as they were received over the wire. Duplicate headers in the response are represented as a single key with their values concatentated using `\n` as the separator. See also `headersText` that contains verbatim text for HTTP/1.*. |
| `resourceIPAddressSpace` | [IPAddressSpace](#type-ipaddressspace) | The IP address space of the resource. The address space can only be determined once the transport established the connection, so we can't send it in `requestWillBeSentExtraInfo`. |
| `statusCode` | integer | The status code of the response. This is useful in cases the request failed and no responseReceived event is triggered, which is the case for, e.g., CORS errors. This is also the correct status code for cached requests, where the status in responseReceived is a 200 and this will be 304. |
| `headersText` (optional) | string | Raw response header text as it was received over the wire. The raw text may not always be available, such as in the case of HTTP/2 or QUIC. |
| `cookiePartitionKey` (optional) *(experimental)* | [CookiePartitionKey](#type-cookiepartitionkey) | The cookie partition key that will be used to store partitioned cookies set in this response. Only sent when partitioned cookies are enabled. |
| `cookiePartitionKeyOpaque` (optional) | boolean | True if partitioned cookies are enabled, but the partition key is not serializable to string. |
| `exemptedCookies` (optional) | array of [ExemptedSetCookieWithReason](#type-exemptedsetcookiewithreason) | A list of cookies which should have been blocked by 3PCD but are exempted and stored from the response with the corresponding reason. |

### Network.responseReceivedEarlyHints *(experimental)*

Fired when 103 Early Hints headers is received in addition to the common response. Not every responseReceived event will have an responseReceivedEarlyHints fired. Only one responseReceivedEarlyHints may be fired for eached responseReceived event.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `requestId` | [RequestId](#type-requestid) | Request identifier. Used to match this information to another responseReceived event. |
| `headers` | [Headers](#type-headers) | Raw response headers as they were received over the wire. Duplicate headers in the response are represented as a single key with their values concatentated using `\n` as the separator. See also `headersText` that contains verbatim text for HTTP/1.*. |

### Network.trustTokenOperationDone *(experimental)*

Fired exactly once for each Trust Token operation. Depending on the type of the operation and whether the operation succeeded or failed, the event is fired before the corresponding request was sent or after the response was received.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `status` | enum: `Ok`, `InvalidArgument`, `MissingIssuerKeys`, `FailedPrecondition`, `ResourceExhausted`, `AlreadyExists`, `ResourceLimited`, `Unauthorized`, `BadResponse`, `InternalError`, `UnknownError`, `FulfilledLocally`, `SiteIssuerLimit` | Detailed success or error status of the operation. 'AlreadyExists' also signifies a successful operation, as the result of the operation already exists und thus, the operation was abort preemptively (e.g. a cache hit). |
| `type` | [TrustTokenOperationType](#type-trusttokenoperationtype) |  |
| `requestId` | [RequestId](#type-requestid) |  |
| `topLevelOrigin` (optional) | string | Top level origin. The context in which the operation was attempted. |
| `issuerOrigin` (optional) | string | Origin of the issuer in case of a "Issuance" or "Redemption" operation. |
| `issuedTokenCount` (optional) | integer | The number of obtained Trust Tokens on a successful "Issuance" operation. |

### Network.policyUpdated *(experimental)*

Fired once security policy has been updated.

### Network.reportingApiReportAdded *(experimental)*

Is sent whenever a new report is added. And after 'enableReportingApi' for all existing reports.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `report` | [ReportingApiReport](#type-reportingapireport) |  |

### Network.reportingApiReportUpdated *(experimental)*

**Parameters**

| Name | Type | Description |
|---|---|---|
| `report` | [ReportingApiReport](#type-reportingapireport) |  |

### Network.reportingApiEndpointsChangedForOrigin *(experimental)*

**Parameters**

| Name | Type | Description |
|---|---|---|
| `origin` | string | Origin of the document(s) which configured the endpoints. |
| `endpoints` | array of [ReportingApiEndpoint](#type-reportingapiendpoint) |  |

### Network.deviceBoundSessionsAdded *(experimental)*

Triggered when the initial set of device bound sessions is added.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `sessions` | array of [DeviceBoundSession](#type-deviceboundsession) | The device bound sessions. |

### Network.deviceBoundSessionEventOccurred *(experimental)*

Triggered when a device bound session event occurs.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `eventId` | [DeviceBoundSessionEventId](#type-deviceboundsessioneventid) | A unique identifier for this session event. |
| `site` | string | The site this session event is associated with. |
| `succeeded` | boolean | Whether this event was considered successful. |
| `sessionId` (optional) | string | The session ID this event is associated with. May not be populated for failed events. |
| `creationEventDetails` (optional) | [CreationEventDetails](#type-creationeventdetails) | The below are the different session event type details. Exactly one is populated. |
| `refreshEventDetails` (optional) | [RefreshEventDetails](#type-refresheventdetails) |  |
| `terminationEventDetails` (optional) | [TerminationEventDetails](#type-terminationeventdetails) |  |
| `challengeEventDetails` (optional) | [ChallengeEventDetails](#type-challengeeventdetails) |  |

## Types

<a id="type-resourcetype"></a>
### Network.ResourceType

Type: string

Resource type as it was perceived by the rendering engine.

Allowed values: `Document`, `Stylesheet`, `Image`, `Media`, `Font`, `Script`, `TextTrack`, `XHR`, `Fetch`, `Prefetch`, `EventSource`, `WebSocket`, `Manifest`, `SignedExchange`, `Ping`, `CSPViolationReport`, `Preflight`, `FedCM`, `Other`

<a id="type-loaderid"></a>
### Network.LoaderId

Type: string

Unique loader identifier.

<a id="type-requestid"></a>
### Network.RequestId

Type: string

Unique network request identifier. Note that this does not identify individual HTTP requests that are part of a network request.

<a id="type-errorreason"></a>
### Network.ErrorReason

Type: string

Network level fetch failure reason.

Allowed values: `Failed`, `Aborted`, `TimedOut`, `AccessDenied`, `ConnectionClosed`, `ConnectionReset`, `ConnectionRefused`, `ConnectionAborted`, `ConnectionFailed`, `NameNotResolved`, `InternetDisconnected`, `AddressUnreachable`, `BlockedByClient`, `BlockedByResponse`

<a id="type-timesinceepoch"></a>
### Network.TimeSinceEpoch

Type: number

UTC time in seconds, counted from January 1, 1970.

<a id="type-monotonictime"></a>
### Network.MonotonicTime

Type: number

Monotonically increasing time in seconds since an arbitrary point in the past.

<a id="type-headers"></a>
### Network.Headers

Type: object

Request / response headers as keys / values of JSON object.

<a id="type-connectiontype"></a>
### Network.ConnectionType

Type: string

The underlying connection technology that the browser is supposedly using.

Allowed values: `none`, `cellular2g`, `cellular3g`, `cellular4g`, `bluetooth`, `ethernet`, `wifi`, `wimax`, `other`

<a id="type-cookiesamesite"></a>
### Network.CookieSameSite

Type: string

Represents the cookie's 'SameSite' status: https://tools.ietf.org/html/draft-west-first-party-cookies

Allowed values: `Strict`, `Lax`, `None`

<a id="type-cookiepriority"></a>
### Network.CookiePriority *(experimental)*

Type: string

Represents the cookie's 'Priority' status: https://tools.ietf.org/html/draft-west-cookie-priority-00

Allowed values: `Low`, `Medium`, `High`

<a id="type-cookiesourcescheme"></a>
### Network.CookieSourceScheme *(experimental)*

Type: string

Represents the source scheme of the origin that originally set the cookie. A value of "Unset" allows protocol clients to emulate legacy cookie scope for the scheme. This is a temporary ability and it will be removed in the future.

Allowed values: `Unset`, `NonSecure`, `Secure`

<a id="type-resourcetiming"></a>
### Network.ResourceTiming

Type: object

Timing information for the request.

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
| `workerStart` *(experimental)* | number | Started running ServiceWorker. |
| `workerReady` *(experimental)* | number | Finished Starting ServiceWorker. |
| `workerFetchStart` *(experimental)* | number | Started fetch event. |
| `workerRespondWithSettled` *(experimental)* | number | Settled fetch event respondWith promise. |
| `workerRouterEvaluationStart` (optional) *(experimental)* | number | Started ServiceWorker static routing source evaluation. |
| `workerCacheLookupStart` (optional) *(experimental)* | number | Started cache lookup when the source was evaluated to `cache`. |
| `sendStart` | number | Started sending request. |
| `sendEnd` | number | Finished sending request. |
| `pushStart` *(experimental)* | number | Time the server started pushing request. |
| `pushEnd` *(experimental)* | number | Time the server finished pushing request. |
| `receiveHeadersStart` *(experimental)* | number | Started receiving response headers. |
| `receiveHeadersEnd` | number | Finished receiving response headers. |

<a id="type-resourcepriority"></a>
### Network.ResourcePriority

Type: string

Loading priority of a resource request.

Allowed values: `VeryLow`, `Low`, `Medium`, `High`, `VeryHigh`

<a id="type-renderblockingbehavior"></a>
### Network.RenderBlockingBehavior *(experimental)*

Type: string

The render-blocking behavior of a resource request.

Allowed values: `Blocking`, `InBodyParserBlocking`, `NonBlocking`, `NonBlockingDynamic`, `PotentiallyBlocking`

<a id="type-postdataentry"></a>
### Network.PostDataEntry

Type: object

Post data entry for HTTP request

**Properties**

| Name | Type | Description |
|---|---|---|
| `bytes` (optional) | binary |  |

<a id="type-request"></a>
### Network.Request

Type: object

HTTP request data.

**Properties**

| Name | Type | Description |
|---|---|---|
| `url` | string | Request URL (without fragment). |
| `urlFragment` (optional) | string | Fragment of the requested URL starting with hash, if present. |
| `method` | string | HTTP request method. |
| `headers` | [Headers](#type-headers) | HTTP request headers. |
| `postData` (optional) *(deprecated)* | string | HTTP POST request data. Use postDataEntries instead. |
| `hasPostData` (optional) | boolean | True when the request has POST data. Note that postData might still be omitted when this flag is true when the data is too long. |
| `postDataEntries` (optional) *(experimental)* | array of [PostDataEntry](#type-postdataentry) | Request body elements (post data broken into individual entries). |
| `mixedContentType` (optional) | [Security.MixedContentType](Security.md#type-mixedcontenttype) | The mixed content type of the request. |
| `initialPriority` | [ResourcePriority](#type-resourcepriority) | Priority of the resource request at the time request is sent. |
| `referrerPolicy` | enum: `unsafe-url`, `no-referrer-when-downgrade`, `no-referrer`, `origin`, `origin-when-cross-origin`, `same-origin`, `strict-origin`, `strict-origin-when-cross-origin` | The referrer policy of the request, as defined in https://www.w3.org/TR/referrer-policy/ |
| `isLinkPreload` (optional) | boolean | Whether is loaded via link preload. |
| `trustTokenParams` (optional) *(experimental)* | [TrustTokenParams](#type-trusttokenparams) | Set for requests when the TrustToken API is used. Contains the parameters passed by the developer (e.g. via "fetch") as understood by the backend. |
| `isSameSite` (optional) *(experimental)* | boolean | True if this resource request is considered to be the 'same site' as the request corresponding to the main frame. |
| `isAdRelated` (optional) *(experimental)* | boolean | True when the resource request is ad-related. |

<a id="type-signedcertificatetimestamp"></a>
### Network.SignedCertificateTimestamp

Type: object

Details of a signed certificate timestamp (SCT).

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

Type: object

Security details about a request.

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
| `validFrom` | [TimeSinceEpoch](#type-timesinceepoch) | Certificate valid from date. |
| `validTo` | [TimeSinceEpoch](#type-timesinceepoch) | Certificate valid to (expiration) date |
| `signedCertificateTimestampList` | array of [SignedCertificateTimestamp](#type-signedcertificatetimestamp) | List of signed certificate timestamps (SCTs). |
| `certificateTransparencyCompliance` | [CertificateTransparencyCompliance](#type-certificatetransparencycompliance) | Whether the request complied with Certificate Transparency policy |
| `serverSignatureAlgorithm` (optional) | integer | The signature algorithm used by the server in the TLS server signature, represented as a TLS SignatureScheme code point. Omitted if not applicable or not known. |
| `encryptedClientHello` | boolean | Whether the connection used Encrypted ClientHello |

<a id="type-certificatetransparencycompliance"></a>
### Network.CertificateTransparencyCompliance

Type: string

Whether the request complied with Certificate Transparency policy.

Allowed values: `unknown`, `not-compliant`, `compliant`

<a id="type-blockedreason"></a>
### Network.BlockedReason

Type: string

The reason why request was blocked.

Allowed values: `other`, `csp`, `mixed-content`, `origin`, `inspector`, `integrity`, `subresource-filter`, `content-type`, `coep-frame-resource-needs-coep-header`, `coop-sandboxed-iframe-cannot-navigate-to-coop-page`, `corp-not-same-origin`, `corp-not-same-origin-after-defaulted-to-same-origin-by-coep`, `corp-not-same-origin-after-defaulted-to-same-origin-by-dip`, `corp-not-same-origin-after-defaulted-to-same-origin-by-coep-and-dip`, `corp-not-same-site`, `sri-message-signature-mismatch`

<a id="type-corserror"></a>
### Network.CorsError

Type: string

The reason why request was blocked.

Allowed values: `DisallowedByMode`, `InvalidResponse`, `WildcardOriginNotAllowed`, `MissingAllowOriginHeader`, `MultipleAllowOriginValues`, `InvalidAllowOriginValue`, `AllowOriginMismatch`, `InvalidAllowCredentials`, `CorsDisabledScheme`, `PreflightInvalidStatus`, `PreflightDisallowedRedirect`, `PreflightWildcardOriginNotAllowed`, `PreflightMissingAllowOriginHeader`, `PreflightMultipleAllowOriginValues`, `PreflightInvalidAllowOriginValue`, `PreflightAllowOriginMismatch`, `PreflightInvalidAllowCredentials`, `PreflightMissingAllowExternal`, `PreflightInvalidAllowExternal`, `InvalidAllowMethodsPreflightResponse`, `InvalidAllowHeadersPreflightResponse`, `MethodDisallowedByPreflightResponse`, `HeaderDisallowedByPreflightResponse`, `RedirectContainsCredentials`, `InsecureLocalNetwork`, `InvalidLocalNetworkAccess`, `NoCorsRedirectModeNotFollow`, `LocalNetworkAccessPermissionDenied`

<a id="type-corserrorstatus"></a>
### Network.CorsErrorStatus

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `corsError` | [CorsError](#type-corserror) |  |
| `failedParameter` | string |  |

<a id="type-serviceworkerresponsesource"></a>
### Network.ServiceWorkerResponseSource

Type: string

Source of serviceworker response.

Allowed values: `cache-storage`, `http-cache`, `fallback-code`, `network`

<a id="type-trusttokenparams"></a>
### Network.TrustTokenParams *(experimental)*

Type: object

Determines what type of Trust Token operation is executed and depending on the type, some additional parameters. The values are specified in third_party/blink/renderer/core/fetch/trust_token.idl.

**Properties**

| Name | Type | Description |
|---|---|---|
| `operation` | [TrustTokenOperationType](#type-trusttokenoperationtype) |  |
| `refreshPolicy` | enum: `UseCached`, `Refresh` | Only set for "token-redemption" operation and determine whether to request a fresh SRR or use a still valid cached SRR. |
| `issuers` (optional) | array of string | Origins of issuers from whom to request tokens or redemption records. |

<a id="type-trusttokenoperationtype"></a>
### Network.TrustTokenOperationType *(experimental)*

Type: string

Allowed values: `Issuance`, `Redemption`, `Signing`

<a id="type-alternateprotocolusage"></a>
### Network.AlternateProtocolUsage *(experimental)*

Type: string

The reason why Chrome uses a specific transport protocol for HTTP semantics.

Allowed values: `alternativeJobWonWithoutRace`, `alternativeJobWonRace`, `mainJobWonRace`, `mappingMissing`, `broken`, `dnsAlpnH3JobWonWithoutRace`, `dnsAlpnH3JobWonRace`, `unspecifiedReason`

<a id="type-serviceworkerroutersource"></a>
### Network.ServiceWorkerRouterSource

Type: string

Source of service worker router.

Allowed values: `network`, `cache`, `fetch-event`, `race-network-and-fetch-handler`, `race-network-and-cache`

<a id="type-serviceworkerrouterinfo"></a>
### Network.ServiceWorkerRouterInfo *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `ruleIdMatched` (optional) | integer | ID of the rule matched. If there is a matched rule, this field will be set, otherwiser no value will be set. |
| `matchedSourceType` (optional) | [ServiceWorkerRouterSource](#type-serviceworkerroutersource) | The router source of the matched rule. If there is a matched rule, this field will be set, otherwise no value will be set. |
| `actualSourceType` (optional) | [ServiceWorkerRouterSource](#type-serviceworkerroutersource) | The actual router source used. |

<a id="type-response"></a>
### Network.Response

Type: object

HTTP response data.

**Properties**

| Name | Type | Description |
|---|---|---|
| `url` | string | Response URL. This URL can be different from CachedResource.url in case of redirect. |
| `status` | integer | HTTP response status code. |
| `statusText` | string | HTTP response status text. |
| `headers` | [Headers](#type-headers) | HTTP response headers. |
| `headersText` (optional) *(deprecated)* | string | HTTP response headers text. This has been replaced by the headers in Network.responseReceivedExtraInfo. |
| `mimeType` | string | Resource mimeType as determined by the browser. |
| `charset` | string | Resource charset as determined by the browser (if applicable). |
| `requestHeaders` (optional) | [Headers](#type-headers) | Refined HTTP request headers that were actually transmitted over the network. |
| `requestHeadersText` (optional) *(deprecated)* | string | HTTP request headers text. This has been replaced by the headers in Network.requestWillBeSentExtraInfo. |
| `connectionReused` | boolean | Specifies whether physical connection was actually reused for this request. |
| `connectionId` | number | Physical connection id that was actually used for this request. |
| `remoteIPAddress` (optional) | string | Remote IP address. |
| `remotePort` (optional) | integer | Remote port. |
| `fromDiskCache` (optional) | boolean | Specifies that the request was served from the disk cache. |
| `fromServiceWorker` (optional) | boolean | Specifies that the request was served from the ServiceWorker. |
| `fromPrefetchCache` (optional) | boolean | Specifies that the request was served from the prefetch cache. |
| `fromEarlyHints` (optional) | boolean | Specifies that the request was served from the prefetch cache. |
| `serviceWorkerRouterInfo` (optional) *(experimental)* | [ServiceWorkerRouterInfo](#type-serviceworkerrouterinfo) | Information about how ServiceWorker Static Router API was used. If this field is set with `matchedSourceType` field, a matching rule is found. If this field is set without `matchedSource`, no matching rule is found. Otherwise, the API is not used. |
| `encodedDataLength` | number | Total number of bytes received for this request so far. |
| `timing` (optional) | [ResourceTiming](#type-resourcetiming) | Timing information for the given request. |
| `serviceWorkerResponseSource` (optional) | [ServiceWorkerResponseSource](#type-serviceworkerresponsesource) | Response source of response from ServiceWorker. |
| `responseTime` (optional) | [TimeSinceEpoch](#type-timesinceepoch) | The time at which the returned response was generated. |
| `cacheStorageCacheName` (optional) | string | Cache Storage Cache Name. |
| `protocol` (optional) | string | Protocol used to fetch this request. |
| `alternateProtocolUsage` (optional) *(experimental)* | [AlternateProtocolUsage](#type-alternateprotocolusage) | The reason why Chrome uses a specific transport protocol for HTTP semantics. |
| `securityState` | [Security.SecurityState](Security.md#type-securitystate) | Security state of the request resource. |
| `securityDetails` (optional) | [SecurityDetails](#type-securitydetails) | Security details for the request. |

<a id="type-websocketrequest"></a>
### Network.WebSocketRequest

Type: object

WebSocket request data.

**Properties**

| Name | Type | Description |
|---|---|---|
| `headers` | [Headers](#type-headers) | HTTP request headers. |

<a id="type-websocketresponse"></a>
### Network.WebSocketResponse

Type: object

WebSocket response data.

**Properties**

| Name | Type | Description |
|---|---|---|
| `status` | integer | HTTP response status code. |
| `statusText` | string | HTTP response status text. |
| `headers` | [Headers](#type-headers) | HTTP response headers. |
| `headersText` (optional) | string | HTTP response headers text. |
| `requestHeaders` (optional) | [Headers](#type-headers) | HTTP request headers. |
| `requestHeadersText` (optional) | string | HTTP request headers text. |

<a id="type-websocketframe"></a>
### Network.WebSocketFrame

Type: object

WebSocket message data. This represents an entire WebSocket message, not just a fragmented frame as the name suggests.

**Properties**

| Name | Type | Description |
|---|---|---|
| `opcode` | number | WebSocket message opcode. |
| `mask` | boolean | WebSocket message mask. |
| `payloadData` | string | WebSocket message payload data. If the opcode is 1, this is a text message and payloadData is a UTF-8 string. If the opcode isn't 1, then payloadData is a base64 encoded string representing binary data. |

<a id="type-cachedresource"></a>
### Network.CachedResource

Type: object

Information about the cached resource.

**Properties**

| Name | Type | Description |
|---|---|---|
| `url` | string | Resource URL. This is the url of the original network request. |
| `type` | [ResourceType](#type-resourcetype) | Type of this resource. |
| `response` (optional) | [Response](#type-response) | Cached response data. |
| `bodySize` | number | Cached response body size. |

<a id="type-initiator"></a>
### Network.Initiator

Type: object

Information about the request initiator.

**Properties**

| Name | Type | Description |
|---|---|---|
| `type` | enum: `parser`, `script`, `preload`, `SignedExchange`, `preflight`, `FedCM`, `other` | Type of this initiator. |
| `stack` (optional) | [Runtime.StackTrace](Runtime.md#type-stacktrace) | Initiator JavaScript stack trace, set for Script only. Requires the Debugger domain to be enabled. |
| `url` (optional) | string | Initiator URL, set for Parser type or for Script type (when script is importing module) or for SignedExchange type. |
| `lineNumber` (optional) | number | Initiator line number, set for Parser type or for Script type (when script is importing module) (0-based). |
| `columnNumber` (optional) | number | Initiator column number, set for Parser type or for Script type (when script is importing module) (0-based). |
| `requestId` (optional) | [RequestId](#type-requestid) | Set if another request triggered this request (e.g. preflight). |

<a id="type-cookiepartitionkey"></a>
### Network.CookiePartitionKey *(experimental)*

Type: object

cookiePartitionKey object The representation of the components of the key that are created by the cookiePartitionKey class contained in net/cookies/cookie_partition_key.h.

**Properties**

| Name | Type | Description |
|---|---|---|
| `topLevelSite` | string | The site of the top-level URL the browser was visiting at the start of the request to the endpoint that set the cookie. |
| `hasCrossSiteAncestor` | boolean | Indicates if the cookie has any ancestors that are cross-site to the topLevelSite. |

<a id="type-cookie"></a>
### Network.Cookie

Type: object

Cookie object

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
| `sameSite` (optional) | [CookieSameSite](#type-cookiesamesite) | Cookie SameSite type. |
| `priority` *(experimental)* | [CookiePriority](#type-cookiepriority) | Cookie Priority |
| `sourceScheme` *(experimental)* | [CookieSourceScheme](#type-cookiesourcescheme) | Cookie source scheme type. |
| `sourcePort` *(experimental)* | integer | Cookie source port. Valid values are {-1, [1, 65535]}, -1 indicates an unspecified port. An unspecified port value allows protocol clients to emulate legacy cookie scope for the port. This is a temporary ability and it will be removed in the future. |
| `partitionKey` (optional) *(experimental)* | [CookiePartitionKey](#type-cookiepartitionkey) | Cookie partition key. |
| `partitionKeyOpaque` (optional) *(experimental)* | boolean | True if cookie partition key is opaque. |

<a id="type-setcookieblockedreason"></a>
### Network.SetCookieBlockedReason *(experimental)*

Type: string

Types of reasons why a cookie may not be stored from a response.

Allowed values: `SecureOnly`, `SameSiteStrict`, `SameSiteLax`, `SameSiteUnspecifiedTreatedAsLax`, `SameSiteNoneInsecure`, `UserPreferences`, `ThirdPartyPhaseout`, `SyntaxError`, `SchemeNotSupported`, `OverwriteSecure`, `InvalidDomain`, `InvalidPrefix`, `UnknownError`, `SchemefulSameSiteStrict`, `SchemefulSameSiteLax`, `SchemefulSameSiteUnspecifiedTreatedAsLax`, `NameValuePairExceedsMaxSize`, `DisallowedCharacter`, `NoCookieContent`

<a id="type-cookieblockedreason"></a>
### Network.CookieBlockedReason *(experimental)*

Type: string

Types of reasons why a cookie may not be sent with a request.

Allowed values: `SecureOnly`, `NotOnPath`, `DomainMismatch`, `SameSiteStrict`, `SameSiteLax`, `SameSiteUnspecifiedTreatedAsLax`, `SameSiteNoneInsecure`, `UserPreferences`, `ThirdPartyPhaseout`, `UnknownError`, `SchemefulSameSiteStrict`, `SchemefulSameSiteLax`, `SchemefulSameSiteUnspecifiedTreatedAsLax`, `NameValuePairExceedsMaxSize`, `PortMismatch`, `SchemeMismatch`, `AnonymousContext`

<a id="type-cookieexemptionreason"></a>
### Network.CookieExemptionReason *(experimental)*

Type: string

Types of reasons why a cookie should have been blocked by 3PCD but is exempted for the request.

Allowed values: `None`, `UserSetting`, `EnterprisePolicy`, `StorageAccess`, `TopLevelStorageAccess`, `Scheme`, `SameSiteNoneCookiesInSandbox`

<a id="type-blockedsetcookiewithreason"></a>
### Network.BlockedSetCookieWithReason *(experimental)*

Type: object

A cookie which was not stored from a response with the corresponding reason.

**Properties**

| Name | Type | Description |
|---|---|---|
| `blockedReasons` | array of [SetCookieBlockedReason](#type-setcookieblockedreason) | The reason(s) this cookie was blocked. |
| `cookieLine` | string | The string representing this individual cookie as it would appear in the header. This is not the entire "cookie" or "set-cookie" header which could have multiple cookies. |
| `cookie` (optional) | [Cookie](#type-cookie) | The cookie object which represents the cookie which was not stored. It is optional because sometimes complete cookie information is not available, such as in the case of parsing errors. |

<a id="type-exemptedsetcookiewithreason"></a>
### Network.ExemptedSetCookieWithReason *(experimental)*

Type: object

A cookie should have been blocked by 3PCD but is exempted and stored from a response with the corresponding reason. A cookie could only have at most one exemption reason.

**Properties**

| Name | Type | Description |
|---|---|---|
| `exemptionReason` | [CookieExemptionReason](#type-cookieexemptionreason) | The reason the cookie was exempted. |
| `cookieLine` | string | The string representing this individual cookie as it would appear in the header. |
| `cookie` | [Cookie](#type-cookie) | The cookie object representing the cookie. |

<a id="type-associatedcookie"></a>
### Network.AssociatedCookie *(experimental)*

Type: object

A cookie associated with the request which may or may not be sent with it. Includes the cookies itself and reasons for blocking or exemption.

**Properties**

| Name | Type | Description |
|---|---|---|
| `cookie` | [Cookie](#type-cookie) | The cookie object representing the cookie which was not sent. |
| `blockedReasons` | array of [CookieBlockedReason](#type-cookieblockedreason) | The reason(s) the cookie was blocked. If empty means the cookie is included. |
| `exemptionReason` (optional) | [CookieExemptionReason](#type-cookieexemptionreason) | The reason the cookie should have been blocked by 3PCD but is exempted. A cookie could only have at most one exemption reason. |

<a id="type-cookieparam"></a>
### Network.CookieParam

Type: object

Cookie parameter object

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
| `sameSite` (optional) | [CookieSameSite](#type-cookiesamesite) | Cookie SameSite type. |
| `expires` (optional) | [TimeSinceEpoch](#type-timesinceepoch) | Cookie expiration date, session cookie if not set |
| `priority` (optional) *(experimental)* | [CookiePriority](#type-cookiepriority) | Cookie Priority. |
| `sourceScheme` (optional) *(experimental)* | [CookieSourceScheme](#type-cookiesourcescheme) | Cookie source scheme type. |
| `sourcePort` (optional) *(experimental)* | integer | Cookie source port. Valid values are {-1, [1, 65535]}, -1 indicates an unspecified port. An unspecified port value allows protocol clients to emulate legacy cookie scope for the port. This is a temporary ability and it will be removed in the future. |
| `partitionKey` (optional) *(experimental)* | [CookiePartitionKey](#type-cookiepartitionkey) | Cookie partition key. If not set, the cookie will be set as not partitioned. |

<a id="type-authchallenge"></a>
### Network.AuthChallenge *(experimental)*

Type: object

Authorization challenge for HTTP status code 401 or 407.

**Properties**

| Name | Type | Description |
|---|---|---|
| `source` (optional) | enum: `Server`, `Proxy` | Source of the authentication challenge. |
| `origin` | string | Origin of the challenger. |
| `scheme` | string | The authentication scheme used, such as basic or digest |
| `realm` | string | The realm of the challenge. May be empty. |

<a id="type-authchallengeresponse"></a>
### Network.AuthChallengeResponse *(experimental)*

Type: object

Response to an AuthChallenge.

**Properties**

| Name | Type | Description |
|---|---|---|
| `response` | enum: `Default`, `CancelAuth`, `ProvideCredentials` | The decision on what to do in response to the authorization challenge.  Default means deferring to the default behavior of the net stack, which will likely either the Cancel authentication or display a popup dialog box. |
| `username` (optional) | string | The username to provide, possibly empty. Should only be set if response is ProvideCredentials. |
| `password` (optional) | string | The password to provide, possibly empty. Should only be set if response is ProvideCredentials. |

<a id="type-signedexchangesignature"></a>
### Network.SignedExchangeSignature *(experimental)*

Type: object

Information about a signed exchange signature. https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-signed-exchanges-impl.html#rfc.section.3.1

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
### Network.SignedExchangeHeader *(experimental)*

Type: object

Information about a signed exchange header. https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-signed-exchanges-impl.html#cbor-representation

**Properties**

| Name | Type | Description |
|---|---|---|
| `requestUrl` | string | Signed exchange request URL. |
| `responseCode` | integer | Signed exchange response code. |
| `responseHeaders` | [Headers](#type-headers) | Signed exchange response headers. |
| `signatures` | array of [SignedExchangeSignature](#type-signedexchangesignature) | Signed exchange response signature. |
| `headerIntegrity` | string | Signed exchange header integrity hash in the form of `sha256-<base64-hash-value>`. |

<a id="type-signedexchangeerrorfield"></a>
### Network.SignedExchangeErrorField *(experimental)*

Type: string

Field type for a signed exchange related error.

Allowed values: `signatureSig`, `signatureIntegrity`, `signatureCertUrl`, `signatureCertSha256`, `signatureValidityUrl`, `signatureTimestamps`

<a id="type-signedexchangeerror"></a>
### Network.SignedExchangeError *(experimental)*

Type: object

Information about a signed exchange response.

**Properties**

| Name | Type | Description |
|---|---|---|
| `message` | string | Error message. |
| `signatureIndex` (optional) | integer | The index of the signature which caused the error. |
| `errorField` (optional) | [SignedExchangeErrorField](#type-signedexchangeerrorfield) | The field which caused the error. |

<a id="type-signedexchangeinfo"></a>
### Network.SignedExchangeInfo *(experimental)*

Type: object

Information about a signed exchange response.

**Properties**

| Name | Type | Description |
|---|---|---|
| `outerResponse` | [Response](#type-response) | The outer response of signed HTTP exchange which was received from network. |
| `hasExtraInfo` | boolean | Whether network response for the signed exchange was accompanied by extra headers. |
| `header` (optional) | [SignedExchangeHeader](#type-signedexchangeheader) | Information about the signed exchange header. |
| `securityDetails` (optional) | [SecurityDetails](#type-securitydetails) | Security details for the signed exchange header. |
| `errors` (optional) | array of [SignedExchangeError](#type-signedexchangeerror) | Errors occurred while handling the signed exchange. |

<a id="type-networkconditions"></a>
### Network.NetworkConditions *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `urlPattern` | string | Only matching requests will be affected by these conditions. Patterns use the URLPattern constructor string syntax (https://urlpattern.spec.whatwg.org/) and must be absolute. If the pattern is empty, all requests are matched (including p2p connections). |
| `latency` | number | Minimum latency from request sent to response headers received (ms). |
| `downloadThroughput` | number | Maximal aggregated download throughput (bytes/sec). -1 disables download throttling. |
| `uploadThroughput` | number | Maximal aggregated upload throughput (bytes/sec).  -1 disables upload throttling. |
| `connectionType` (optional) | [ConnectionType](#type-connectiontype) | Connection type if known. |
| `packetLoss` (optional) | number | WebRTC packet loss (percent, 0-100). 0 disables packet loss emulation, 100 drops all the packets. |
| `packetQueueLength` (optional) | integer | WebRTC packet queue length (packet). 0 removes any queue length limitations. |
| `packetReordering` (optional) | boolean | WebRTC packetReordering feature. |
| `offline` (optional) | boolean | True to emulate internet disconnection. |

<a id="type-blockpattern"></a>
### Network.BlockPattern *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `urlPattern` | string | URL pattern to match. Patterns use the URLPattern constructor string syntax (https://urlpattern.spec.whatwg.org/) and must be absolute. Example: `*://*:*/*.css`. |
| `block` | boolean | Whether or not to block the pattern. If false, a matching request will not be blocked even if it matches a later `BlockPattern`. |

<a id="type-directsocketdnsquerytype"></a>
### Network.DirectSocketDnsQueryType *(experimental)*

Type: string

Allowed values: `ipv4`, `ipv6`

<a id="type-directtcpsocketoptions"></a>
### Network.DirectTCPSocketOptions *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `noDelay` | boolean | TCP_NODELAY option |
| `keepAliveDelay` (optional) | number | Expected to be unsigned integer. |
| `sendBufferSize` (optional) | number | Expected to be unsigned integer. |
| `receiveBufferSize` (optional) | number | Expected to be unsigned integer. |
| `dnsQueryType` (optional) | [DirectSocketDnsQueryType](#type-directsocketdnsquerytype) |  |

<a id="type-directudpsocketoptions"></a>
### Network.DirectUDPSocketOptions *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `remoteAddr` (optional) | string |  |
| `remotePort` (optional) | integer | Unsigned int 16. |
| `localAddr` (optional) | string |  |
| `localPort` (optional) | integer | Unsigned int 16. |
| `dnsQueryType` (optional) | [DirectSocketDnsQueryType](#type-directsocketdnsquerytype) |  |
| `sendBufferSize` (optional) | number | Expected to be unsigned integer. |
| `receiveBufferSize` (optional) | number | Expected to be unsigned integer. |
| `multicastLoopback` (optional) | boolean |  |
| `multicastTimeToLive` (optional) | integer | Unsigned int 8. |
| `multicastAllowAddressSharing` (optional) | boolean |  |

<a id="type-directudpmessage"></a>
### Network.DirectUDPMessage *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `data` | binary |  |
| `remoteAddr` (optional) | string | Null for connected mode. |
| `remotePort` (optional) | integer | Null for connected mode. Expected to be unsigned integer. |

<a id="type-localnetworkaccessrequestpolicy"></a>
### Network.LocalNetworkAccessRequestPolicy *(experimental)*

Type: string

Allowed values: `Allow`, `BlockFromInsecureToMorePrivate`, `WarnFromInsecureToMorePrivate`, `PermissionBlock`, `PermissionWarn`

<a id="type-ipaddressspace"></a>
### Network.IPAddressSpace *(experimental)*

Type: string

Allowed values: `Loopback`, `Local`, `Public`, `Unknown`

<a id="type-connecttiming"></a>
### Network.ConnectTiming *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `requestTime` | number | Timing's requestTime is a baseline in seconds, while the other numbers are ticks in milliseconds relatively to this requestTime. Matches ResourceTiming's requestTime for the same request (but not for redirected requests). |

<a id="type-clientsecuritystate"></a>
### Network.ClientSecurityState *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `initiatorIsSecureContext` | boolean |  |
| `initiatorIPAddressSpace` | [IPAddressSpace](#type-ipaddressspace) |  |
| `localNetworkAccessRequestPolicy` | [LocalNetworkAccessRequestPolicy](#type-localnetworkaccessrequestpolicy) |  |

<a id="type-adscriptidentifier"></a>
### Network.AdScriptIdentifier *(experimental)*

Type: object

Identifies the script on the stack that caused a resource or element to be labeled as an ad. For resources, this indicates the context that triggered the fetch. For elements, this indicates the context that caused the element to be appended to the DOM.

**Properties**

| Name | Type | Description |
|---|---|---|
| `scriptId` | [Runtime.ScriptId](Runtime.md#type-scriptid) | The script's V8 identifier. |
| `debuggerId` | [Runtime.UniqueDebuggerId](Runtime.md#type-uniquedebuggerid) | V8's debugging ID for the v8::Context. |
| `name` | string | The script's url (or generated name based on id if inline script). |

<a id="type-adancestry"></a>
### Network.AdAncestry *(experimental)*

Type: object

Encapsulates the script ancestry and the root script filter list rule that caused the resource or element to be labeled as an ad.

**Properties**

| Name | Type | Description |
|---|---|---|
| `ancestryChain` | array of [AdScriptIdentifier](#type-adscriptidentifier) | A chain of `AdScriptIdentifier`s representing the ancestry of an ad script that led to the creation of a resource or element. The chain is ordered from the script itself (lowest level) up to its root ancestor that was flagged by a filter list. |
| `rootScriptFilterlistRule` (optional) | string | The filter list rule that caused the root (last) script in `ancestryChain` to be tagged as an ad. |

<a id="type-adprovenance"></a>
### Network.AdProvenance *(experimental)*

Type: object

Represents the provenance of an ad resource or element. Only one of `filterlistRule` or `adScriptAncestry` can be set. If `filterlistRule` is provided, the resource URL directly matches a filter list rule. If `adScriptAncestry` is provided, an ad script initiated the resource fetch or appended the element to the DOM. If neither is provided, the entity is known to be an ad, but provenance tracking information is unavailable.

**Properties**

| Name | Type | Description |
|---|---|---|
| `filterlistRule` (optional) | string | The filterlist rule that matched, if any. |
| `adScriptAncestry` (optional) | [AdAncestry](#type-adancestry) | The script ancestry that created the ad, if any. Note: depending on the context, this may represent the full ancestry up to the root script, or it may contain only one script representing the immediate ancestor. |

<a id="type-crossoriginopenerpolicyvalue"></a>
### Network.CrossOriginOpenerPolicyValue *(experimental)*

Type: string

Allowed values: `SameOrigin`, `SameOriginAllowPopups`, `RestrictProperties`, `UnsafeNone`, `SameOriginPlusCoep`, `RestrictPropertiesPlusCoep`, `NoopenerAllowPopups`

<a id="type-crossoriginopenerpolicystatus"></a>
### Network.CrossOriginOpenerPolicyStatus *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `value` | [CrossOriginOpenerPolicyValue](#type-crossoriginopenerpolicyvalue) |  |
| `reportOnlyValue` | [CrossOriginOpenerPolicyValue](#type-crossoriginopenerpolicyvalue) |  |
| `reportingEndpoint` (optional) | string |  |
| `reportOnlyReportingEndpoint` (optional) | string |  |

<a id="type-crossoriginembedderpolicyvalue"></a>
### Network.CrossOriginEmbedderPolicyValue *(experimental)*

Type: string

Allowed values: `None`, `Credentialless`, `RequireCorp`

<a id="type-crossoriginembedderpolicystatus"></a>
### Network.CrossOriginEmbedderPolicyStatus *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `value` | [CrossOriginEmbedderPolicyValue](#type-crossoriginembedderpolicyvalue) |  |
| `reportOnlyValue` | [CrossOriginEmbedderPolicyValue](#type-crossoriginembedderpolicyvalue) |  |
| `reportingEndpoint` (optional) | string |  |
| `reportOnlyReportingEndpoint` (optional) | string |  |

<a id="type-contentsecuritypolicysource"></a>
### Network.ContentSecurityPolicySource *(experimental)*

Type: string

Allowed values: `HTTP`, `Meta`

<a id="type-contentsecuritypolicystatus"></a>
### Network.ContentSecurityPolicyStatus *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `effectiveDirectives` | string |  |
| `isEnforced` | boolean |  |
| `source` | [ContentSecurityPolicySource](#type-contentsecuritypolicysource) |  |

<a id="type-securityisolationstatus"></a>
### Network.SecurityIsolationStatus *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `coop` (optional) | [CrossOriginOpenerPolicyStatus](#type-crossoriginopenerpolicystatus) |  |
| `coep` (optional) | [CrossOriginEmbedderPolicyStatus](#type-crossoriginembedderpolicystatus) |  |
| `csp` (optional) | array of [ContentSecurityPolicyStatus](#type-contentsecuritypolicystatus) |  |

<a id="type-reportstatus"></a>
### Network.ReportStatus *(experimental)*

Type: string

The status of a Reporting API report.

Allowed values: `Queued`, `Pending`, `MarkedForRemoval`, `Success`

<a id="type-reportid"></a>
### Network.ReportId *(experimental)*

Type: string

<a id="type-reportingapireport"></a>
### Network.ReportingApiReport *(experimental)*

Type: object

An object representing a report generated by the Reporting API.

**Properties**

| Name | Type | Description |
|---|---|---|
| `id` | [ReportId](#type-reportid) |  |
| `initiatorUrl` | string | The URL of the document that triggered the report. |
| `destination` | string | The name of the endpoint group that should be used to deliver the report. |
| `type` | string | The type of the report (specifies the set of data that is contained in the report body). |
| `timestamp` | [Network.TimeSinceEpoch](Network.md#type-timesinceepoch) | When the report was generated. |
| `depth` | integer | How many uploads deep the related request was. |
| `completedAttempts` | integer | The number of delivery attempts made so far, not including an active attempt. |
| `body` | object |  |
| `status` | [ReportStatus](#type-reportstatus) |  |

<a id="type-reportingapiendpoint"></a>
### Network.ReportingApiEndpoint *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `url` | string | The URL of the endpoint to which reports may be delivered. |
| `groupName` | string | Name of the endpoint group. |

<a id="type-deviceboundsessionkey"></a>
### Network.DeviceBoundSessionKey *(experimental)*

Type: object

Unique identifier for a device bound session.

**Properties**

| Name | Type | Description |
|---|---|---|
| `site` | string | The site the session is set up for. |
| `id` | string | The id of the session. |

<a id="type-deviceboundsessionwithusage"></a>
### Network.DeviceBoundSessionWithUsage *(experimental)*

Type: object

How a device bound session was used during a request.

**Properties**

| Name | Type | Description |
|---|---|---|
| `sessionKey` | [DeviceBoundSessionKey](#type-deviceboundsessionkey) | The key for the session. |
| `usage` | enum: `NotInScope`, `InScopeRefreshNotYetNeeded`, `InScopeRefreshNotAllowed`, `ProactiveRefreshNotPossible`, `ProactiveRefreshAttempted`, `Deferred` | How the session was used (or not used). |

<a id="type-deviceboundsessioncookiecraving"></a>
### Network.DeviceBoundSessionCookieCraving *(experimental)*

Type: object

A device bound session's cookie craving.

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | The name of the craving. |
| `domain` | string | The domain of the craving. |
| `path` | string | The path of the craving. |
| `secure` | boolean | The `Secure` attribute of the craving attributes. |
| `httpOnly` | boolean | The `HttpOnly` attribute of the craving attributes. |
| `sameSite` (optional) | [CookieSameSite](#type-cookiesamesite) | The `SameSite` attribute of the craving attributes. |

<a id="type-deviceboundsessionurlrule"></a>
### Network.DeviceBoundSessionUrlRule *(experimental)*

Type: object

A device bound session's inclusion URL rule.

**Properties**

| Name | Type | Description |
|---|---|---|
| `ruleType` | enum: `Exclude`, `Include` | See comments on `net::device_bound_sessions::SessionInclusionRules::UrlRule::rule_type`. |
| `hostPattern` | string | See comments on `net::device_bound_sessions::SessionInclusionRules::UrlRule::host_pattern`. |
| `pathPrefix` | string | See comments on `net::device_bound_sessions::SessionInclusionRules::UrlRule::path_prefix`. |

<a id="type-deviceboundsessioninclusionrules"></a>
### Network.DeviceBoundSessionInclusionRules *(experimental)*

Type: object

A device bound session's inclusion rules.

**Properties**

| Name | Type | Description |
|---|---|---|
| `origin` | string | See comments on `net::device_bound_sessions::SessionInclusionRules::origin_`. |
| `includeSite` | boolean | Whether the whole site is included. See comments on `net::device_bound_sessions::SessionInclusionRules::include_site_` for more details; this boolean is true if that value is populated. |
| `urlRules` | array of [DeviceBoundSessionUrlRule](#type-deviceboundsessionurlrule) | See comments on `net::device_bound_sessions::SessionInclusionRules::url_rules_`. |

<a id="type-deviceboundsession"></a>
### Network.DeviceBoundSession *(experimental)*

Type: object

A device bound session.

**Properties**

| Name | Type | Description |
|---|---|---|
| `key` | [DeviceBoundSessionKey](#type-deviceboundsessionkey) | The site and session ID of the session. |
| `refreshUrl` | string | See comments on `net::device_bound_sessions::Session::refresh_url_`. |
| `inclusionRules` | [DeviceBoundSessionInclusionRules](#type-deviceboundsessioninclusionrules) | See comments on `net::device_bound_sessions::Session::inclusion_rules_`. |
| `cookieCravings` | array of [DeviceBoundSessionCookieCraving](#type-deviceboundsessioncookiecraving) | See comments on `net::device_bound_sessions::Session::cookie_cravings_`. |
| `expiryDate` | [Network.TimeSinceEpoch](Network.md#type-timesinceepoch) | See comments on `net::device_bound_sessions::Session::expiry_date_`. |
| `cachedChallenge` (optional) | string | See comments on `net::device_bound_sessions::Session::cached_challenge__`. |
| `allowedRefreshInitiators` | array of string | See comments on `net::device_bound_sessions::Session::allowed_refresh_initiators_`. |

<a id="type-deviceboundsessioneventid"></a>
### Network.DeviceBoundSessionEventId *(experimental)*

Type: string

A unique identifier for a device bound session event.

<a id="type-deviceboundsessionfetchresult"></a>
### Network.DeviceBoundSessionFetchResult *(experimental)*

Type: string

A fetch result for a device bound session creation or refresh. LINT.IfChange(DeviceBoundSessionFetchResult)

Allowed values: `Success`, `SigningKeyGenerationError`, `AttestationKeyGenerationError`, `SigningError`, `TransientSigningError`, `ServerRequestedTermination`, `InvalidSessionId`, `InvalidChallenge`, `TooManyChallenges`, `InvalidFetcherUrl`, `InvalidRefreshUrl`, `TransientHttpError`, `ScopeOriginSameSiteMismatch`, `RefreshUrlSameSiteMismatch`, `MismatchedSessionId`, `MissingScope`, `NoCredentials`, `SubdomainRegistrationWellKnownUnavailable`, `SubdomainRegistrationUnauthorized`, `SubdomainRegistrationWellKnownMalformed`, `SessionProviderWellKnownUnavailable`, `RelyingPartyWellKnownUnavailable`, `FederatedKeyThumbprintMismatch`, `InvalidFederatedSessionUrl`, `InvalidFederatedKey`, `TooManyRelyingOriginLabels`, `BoundCookieSetForbidden`, `NetError`, `ProxyError`, `EmptySessionConfig`, `InvalidCredentialsConfig`, `InvalidCredentialsType`, `InvalidCredentialsEmptyName`, `InvalidCredentialsCookie`, `PersistentHttpError`, `RegistrationAttemptedChallenge`, `InvalidScopeOrigin`, `ScopeOriginContainsPath`, `RefreshInitiatorNotString`, `RefreshInitiatorInvalidHostPattern`, `InvalidScopeSpecification`, `MissingScopeSpecificationType`, `EmptyScopeSpecificationDomain`, `EmptyScopeSpecificationPath`, `InvalidScopeSpecificationType`, `InvalidScopeIncludeSite`, `MissingScopeIncludeSite`, `FederatedNotAuthorizedByProvider`, `FederatedNotAuthorizedByRelyingParty`, `SessionProviderWellKnownMalformed`, `SessionProviderWellKnownHasProviderOrigin`, `RelyingPartyWellKnownMalformed`, `RelyingPartyWellKnownHasRelyingOrigins`, `InvalidFederatedSessionProviderSessionMissing`, `InvalidFederatedSessionWrongProviderOrigin`, `InvalidCredentialsCookieCreationTime`, `InvalidCredentialsCookieName`, `InvalidCredentialsCookieParsing`, `InvalidCredentialsCookieUnpermittedAttribute`, `InvalidCredentialsCookieInvalidDomain`, `InvalidCredentialsCookiePrefix`, `InvalidScopeRulePath`, `InvalidScopeRuleHostPattern`, `ScopeRuleOriginScopedHostPatternMismatch`, `ScopeRuleSiteScopedHostPatternMismatch`, `SigningQuotaExceeded`, `InvalidConfigJson`, `InvalidFederatedSessionProviderFailedToRestoreKey`, `FailedToUnwrapKey`, `SessionDeletedDuringRefresh`, `CrossOriginRegistrationSiteNotIncluded`, `InvalidPreProvisionedKeyInitiatorMissing`, `PreProvisionedKeyAccessNotGranted`, `PreProvisionedKeyNotFound`, `AttestationCertificationError`, `AttestationSigningError`, `FederatedRegistrationRedirected`

<a id="type-deviceboundsessionfailedrequest"></a>
### Network.DeviceBoundSessionFailedRequest *(experimental)*

Type: object

LINT.ThenChange(//content/browser/devtools/protocol/network_handler.cc:DeviceBoundSessionFetchResult) Details about a failed device bound session network request.

**Properties**

| Name | Type | Description |
|---|---|---|
| `requestUrl` | string | The failed request URL. |
| `netError` (optional) | string | The net error of the response if it was not OK. |
| `responseError` (optional) | integer | The response code if the net error was OK and the response code was not 200. |
| `responseErrorBody` (optional) | string | The body of the response if the net error was OK, the response code was not 200, and the response body was not empty. |

<a id="type-creationeventdetails"></a>
### Network.CreationEventDetails *(experimental)*

Type: object

Session event details specific to creation.

**Properties**

| Name | Type | Description |
|---|---|---|
| `fetchResult` | [DeviceBoundSessionFetchResult](#type-deviceboundsessionfetchresult) | The result of the fetch attempt. |
| `newSession` (optional) | [DeviceBoundSession](#type-deviceboundsession) | The session if there was a newly created session. This is populated for all successful creation events. |
| `failedRequest` (optional) | [DeviceBoundSessionFailedRequest](#type-deviceboundsessionfailedrequest) | Details about a failed device bound session network request if there was one. |

<a id="type-refresheventdetails"></a>
### Network.RefreshEventDetails *(experimental)*

Type: object

Session event details specific to refresh.

**Properties**

| Name | Type | Description |
|---|---|---|
| `refreshResult` | enum: `Refreshed`, `InitializedService`, `Unreachable`, `ServerError`, `FatalError`, `SigningQuotaExceeded`, `RefreshedAsWaiter`, `TransientSigningError`, `InScopeRefreshNotYetNeeded`, `Canceled` | The result of a refresh. LINT.IfChange(DeviceBoundSessionRefreshResult) |
| `fetchResult` (optional) | [DeviceBoundSessionFetchResult](#type-deviceboundsessionfetchresult) | LINT.ThenChange(//net/device_bound_sessions/refresh_result.h:DeviceBoundSessionRefreshResult,//content/browser/devtools/protocol/network_handler.cc:DeviceBoundSessionRefreshResult) If there was a fetch attempt, the result of that. |
| `newSession` (optional) | [DeviceBoundSession](#type-deviceboundsession) | The session display if there was a newly created session. This is populated for any refresh event that modifies the session config. |
| `wasFullyProactiveRefresh` | boolean | See comments on `net::device_bound_sessions::RefreshEventResult::was_fully_proactive_refresh`. |
| `failedRequest` (optional) | [DeviceBoundSessionFailedRequest](#type-deviceboundsessionfailedrequest) | Details about a failed device bound session network request if there was one. |

<a id="type-terminationeventdetails"></a>
### Network.TerminationEventDetails *(experimental)*

Type: object

Session event details specific to termination.

**Properties**

| Name | Type | Description |
|---|---|---|
| `deletionReason` | enum: `Expired`, `FailedToRestoreKey`, `FailedToUnwrapKey`, `StoragePartitionCleared`, `ClearBrowsingData`, `ServerRequested`, `InvalidSessionParams`, `RefreshFatalError`, `DevTools`, `Replaced` | The reason for a session being deleted. |

<a id="type-challengeeventdetails"></a>
### Network.ChallengeEventDetails *(experimental)*

Type: object

Session event details specific to challenges.

**Properties**

| Name | Type | Description |
|---|---|---|
| `challengeResult` | enum: `Success`, `NoSessionId`, `NoSessionMatch`, `CantSetBoundCookie` | The result of a challenge. |
| `challenge` | string | The challenge set. |

<a id="type-loadnetworkresourcepageresult"></a>
### Network.LoadNetworkResourcePageResult *(experimental)*

Type: object

An object providing the result of a network resource load.

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
### Network.LoadNetworkResourceOptions *(experimental)*

Type: object

An options object that may be extended later to better support CORS, CORB and streaming.

**Properties**

| Name | Type | Description |
|---|---|---|
| `disableCache` | boolean |  |
| `includeCredentials` | boolean |  |

