# Target domain

Copyright 2017 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.  Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp Supports additional targets discovery and allows to attach to them.

Methods are called as `Target.<command>` and events arrive as `Target.<event>`.

## Commands

### Target.activateTarget

Activates (focuses) the target.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `targetId` | [TargetID](#type-targetid) |  |

### Target.attachToTarget

Attaches to the target with given id.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `targetId` | [TargetID](#type-targetid) |  |
| `flatten` (optional) | boolean | Enables "flat" access to the session via specifying sessionId attribute in the commands. We plan to make this the default, deprecate non-flattened mode, and eventually retire it. See crbug.com/991325. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `sessionId` | [SessionID](#type-sessionid) | Id assigned to the session. |

### Target.attachToBrowserTarget *(experimental)*

Attaches to the browser target, only uses flat sessionId mode.

**Returns**

| Name | Type | Description |
|---|---|---|
| `sessionId` | [SessionID](#type-sessionid) | Id assigned to the session. |

### Target.closeTarget

Closes the target. If the target is a page that gets closed too.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `targetId` | [TargetID](#type-targetid) |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `success` *(deprecated)* | boolean | Always set to true. If an error occurs, the response indicates protocol error. |

### Target.exposeDevToolsProtocol *(experimental)*

Inject object to the target's main frame that provides a communication channel with browser target.  Injected object will be available as `window[bindingName]`.  The object has the following API: - `binding.send(json)` - a method to send messages over the remote debugging protocol - `binding.onmessage = json => handleMessage(json)` - a callback that will be called for the protocol notifications and command responses.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `targetId` | [TargetID](#type-targetid) |  |
| `bindingName` (optional) | string | Binding name, 'cdp' if not specified. |
| `inheritPermissions` (optional) | boolean | If true, inherits the current root session's permissions (default: false). |

### Target.createBrowserContext

Creates a new empty BrowserContext. Similar to an incognito profile but you can have more than one.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `disposeOnDetach` (optional) *(experimental)* | boolean | If specified, disposes this context when debugging session disconnects. |
| `proxyServer` (optional) *(experimental)* | string | Proxy server, similar to the one passed to --proxy-server |
| `proxyBypassList` (optional) *(experimental)* | string | Proxy bypass list, similar to the one passed to --proxy-bypass-list |
| `originsWithUniversalNetworkAccess` (optional) *(experimental)* | array of string | An optional list of origins to grant unlimited cross-origin access to. Parts of the URL other than those constituting origin are ignored. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `browserContextId` | [Browser.BrowserContextID](Browser.md#type-browsercontextid) | The id of the context created. |

### Target.getBrowserContexts

Returns all browser contexts created with `Target.createBrowserContext` method.

**Returns**

| Name | Type | Description |
|---|---|---|
| `browserContextIds` | array of [Browser.BrowserContextID](Browser.md#type-browsercontextid) | An array of browser context ids. |
| `defaultBrowserContextId` (optional) *(experimental)* | [Browser.BrowserContextID](Browser.md#type-browsercontextid) | The id of the default browser context if available. |

### Target.createTarget

Creates a new page.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `url` | string | The initial URL the page will be navigated to. An empty string indicates about:blank. |
| `left` (optional) *(experimental)* | integer | Frame left origin in DIP (requires newWindow to be true or headless shell). |
| `top` (optional) *(experimental)* | integer | Frame top origin in DIP (requires newWindow to be true or headless shell). |
| `width` (optional) | integer | Frame width in DIP (requires newWindow to be true or headless shell). |
| `height` (optional) | integer | Frame height in DIP (requires newWindow to be true or headless shell). |
| `windowState` (optional) | [WindowState](#type-windowstate) | Frame window state (requires newWindow to be true or headless shell). Default is normal. |
| `browserContextId` (optional) *(experimental)* | [Browser.BrowserContextID](Browser.md#type-browsercontextid) | The browser context to create the page in. |
| `enableBeginFrameControl` (optional) *(experimental)* | boolean | Whether BeginFrames for this target will be controlled via DevTools (headless shell only, not supported on MacOS yet, false by default). |
| `newWindow` (optional) | boolean | Whether to create a new Window or Tab (false by default, not supported by headless shell). |
| `background` (optional) | boolean | Whether to create the target in background or foreground (false by default, not supported by headless shell). |
| `forTab` (optional) *(experimental)* | boolean | Whether to create the target of type "tab". |
| `hidden` (optional) *(experimental)* | boolean | Whether to create a hidden target. The hidden target is observable via protocol, but not present in the tab UI strip. Cannot be created with `forTab: true`, `newWindow: true` or `background: false`. The life-time of the tab is limited to the life-time of the session. |
| `focus` (optional) *(experimental)* | boolean | If specified, determines whether the new target should be focused. By default, the focus behavior depends on the `background` parameter: - If `background` is false (default) and `focus` is omitted, the new target is focused and the browser window is brought to the foreground. - If `background` is false and `focus` is false, the target is opened but the browser window's focus remains unchanged (e.g., if the window was in the background, it stays there). - If `background` is true, setting `focus` to true is not supported and will result in an error. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `targetId` | [TargetID](#type-targetid) | The id of the page opened. |

### Target.detachFromTarget

Detaches session with given id.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `sessionId` (optional) | [SessionID](#type-sessionid) | Session to detach. |
| `targetId` (optional) *(deprecated)* | [TargetID](#type-targetid) | Deprecated. |

### Target.disposeBrowserContext

Deletes a BrowserContext. All the belonging pages will be closed without calling their beforeunload hooks.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `browserContextId` | [Browser.BrowserContextID](Browser.md#type-browsercontextid) |  |

### Target.getTargetInfo *(experimental)*

Returns information about a target.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `targetId` (optional) | [TargetID](#type-targetid) |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `targetInfo` | [TargetInfo](#type-targetinfo) |  |

### Target.getTargets

Retrieves a list of available targets.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `filter` (optional) *(experimental)* | [TargetFilter](#type-targetfilter) | Only targets matching filter will be reported. If filter is not specified and target discovery is currently enabled, a filter used for target discovery is used for consistency. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `targetInfos` | array of [TargetInfo](#type-targetinfo) | The list of targets. |

### Target.sendMessageToTarget *(deprecated)*

Sends protocol message over session with given id. Consider using flat mode instead; see commands attachToTarget, setAutoAttach, and crbug.com/991325.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `message` | string |  |
| `sessionId` (optional) | [SessionID](#type-sessionid) | Identifier of the session. |
| `targetId` (optional) *(deprecated)* | [TargetID](#type-targetid) | Deprecated. |

### Target.setAutoAttach

Controls whether to automatically attach to new targets which are considered to be directly related to this one (for example, iframes or workers). When turned on, attaches to all existing related targets as well. When turned off, automatically detaches from all currently attached targets. This also clears all targets added by `autoAttachRelated` from the list of targets to watch for creation of related targets. You might want to call this recursively for auto-attached targets to attach to all available targets.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `autoAttach` | boolean | Whether to auto-attach to related targets. |
| `waitForDebuggerOnStart` | boolean | Whether to pause new targets when attaching to them. Use `Runtime.runIfWaitingForDebugger` to run paused targets. |
| `flatten` (optional) *(experimental)* | boolean | Enables "flat" access to the session via specifying sessionId attribute in the commands. We plan to make this the default, deprecate non-flattened mode, and eventually retire it. See crbug.com/991325. |
| `filter` (optional) *(experimental)* | [TargetFilter](#type-targetfilter) | Only targets matching filter will be attached. |

### Target.autoAttachRelated *(experimental)*

Adds the specified target to the list of targets that will be monitored for any related target creation (such as child frames, child workers and new versions of service worker) and reported through `attachedToTarget`. The specified target is also auto-attached. This cancels the effect of any previous `setAutoAttach` and is also cancelled by subsequent `setAutoAttach`. Only available at the Browser target.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `targetId` | [TargetID](#type-targetid) |  |
| `waitForDebuggerOnStart` | boolean | Whether to pause new targets when attaching to them. Use `Runtime.runIfWaitingForDebugger` to run paused targets. |
| `filter` (optional) *(experimental)* | [TargetFilter](#type-targetfilter) | Only targets matching filter will be attached. |

### Target.setDiscoverTargets

Controls whether to discover available targets and notify via `targetCreated/targetInfoChanged/targetDestroyed` events.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `discover` | boolean | Whether to discover available targets. |
| `filter` (optional) *(experimental)* | [TargetFilter](#type-targetfilter) | Only targets matching filter will be attached. If `discover` is false, `filter` must be omitted or empty. |

### Target.setRemoteLocations *(experimental)*

Enables target discovery for the specified locations, when `setDiscoverTargets` was set to `true`.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `locations` | array of [RemoteLocation](#type-remotelocation) | List of remote locations. |

### Target.getDevToolsTarget *(experimental)*

Gets the targetId of the DevTools page target opened for the given target (if any).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `targetId` | [TargetID](#type-targetid) | Page or tab target ID. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `targetId` (optional) | [TargetID](#type-targetid) | The targetId of DevTools page target if exists. |

### Target.openDevTools *(experimental)*

Opens a DevTools window for the target.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `targetId` | [TargetID](#type-targetid) | This can be the page or tab target ID. |
| `panelId` (optional) | string | The id of the panel we want DevTools to open initially. Currently supported panels are elements, console, network, sources, resources, timeline, chrome-recorder, heap-profiler, lighthouse, and security. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `targetId` | [TargetID](#type-targetid) | The targetId of DevTools page target. |

## Events

### Target.attachedToTarget *(experimental)*

Issued when attached to target because of auto-attach or `attachToTarget` command.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `sessionId` | [SessionID](#type-sessionid) | Identifier assigned to the session used to send/receive messages. |
| `targetInfo` | [TargetInfo](#type-targetinfo) |  |
| `waitingForDebugger` | boolean |  |

### Target.detachedFromTarget *(experimental)*

Issued when detached from target for any reason (including `detachFromTarget` command). Can be issued multiple times per target if multiple sessions have been attached to it.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `sessionId` | [SessionID](#type-sessionid) | Detached session identifier. |
| `targetId` (optional) *(deprecated)* | [TargetID](#type-targetid) | Deprecated. |

### Target.receivedMessageFromTarget

Notifies about a new protocol message received from the session (as reported in `attachedToTarget` event).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `sessionId` | [SessionID](#type-sessionid) | Identifier of a session which sends a message. |
| `message` | string |  |
| `targetId` (optional) *(deprecated)* | [TargetID](#type-targetid) | Deprecated. |

### Target.targetCreated

Issued when a possible inspection target is created.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `targetInfo` | [TargetInfo](#type-targetinfo) |  |

### Target.targetDestroyed

Issued when a target is destroyed.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `targetId` | [TargetID](#type-targetid) |  |

### Target.targetCrashed

Issued when a target has crashed.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `targetId` | [TargetID](#type-targetid) |  |
| `status` | string | Termination status type. |
| `errorCode` | integer | Termination error code. |

### Target.targetInfoChanged

Issued when some information about a target has changed. This only happens between `targetCreated` and `targetDestroyed`.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `targetInfo` | [TargetInfo](#type-targetinfo) |  |

## Types

<a id="type-targetid"></a>
### Target.TargetID

Type: string

<a id="type-sessionid"></a>
### Target.SessionID

Type: string

Unique identifier of attached debugging session.

<a id="type-targetinfo"></a>
### Target.TargetInfo

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `targetId` | [TargetID](#type-targetid) |  |
| `type` | string | List of types: https://source.chromium.org/chromium/chromium/src/+/main:content/browser/devtools/devtools_agent_host_impl.cc?ss=chromium&q=f:devtools%20-f:out%20%22::kTypeTab%5B%5D%22 |
| `title` | string |  |
| `url` | string |  |
| `attached` | boolean | Whether the target has an attached client. |
| `parentId` (optional) | [TargetID](#type-targetid) | Id of the parent target, if any. For example, "iframe" target may have a "page" parent. |
| `openerId` (optional) | [TargetID](#type-targetid) | Opener target Id |
| `canAccessOpener` *(experimental)* | boolean | Whether the target has access to the originating window. |
| `openerFrameId` (optional) *(experimental)* | [Page.FrameId](Page.md#type-frameid) | Frame id of originating window (is only set if target has an opener). |
| `parentFrameId` (optional) *(experimental)* | [Page.FrameId](Page.md#type-frameid) | Id of the parent frame, present for "iframe" and "worker" targets. For nested workers, this is the "ancestor" frame that created the first worker in the nested chain. |
| `browserContextId` (optional) *(experimental)* | [Browser.BrowserContextID](Browser.md#type-browsercontextid) |  |
| `subtype` (optional) *(experimental)* | string | Provides additional details for specific target types. For example, for the type of "page", this may be set to "prerender". |
| `embedderData` (optional) *(experimental)* | object | Embedder-specific target metadata. This is only set for targets of type "tab". |

<a id="type-filterentry"></a>
### Target.FilterEntry *(experimental)*

Type: object

A filter used by target query/discovery/auto-attach operations.

**Properties**

| Name | Type | Description |
|---|---|---|
| `exclude` (optional) | boolean | If set, causes exclusion of matching targets from the list. |
| `type` (optional) | string | If not present, matches any type. |

<a id="type-targetfilter"></a>
### Target.TargetFilter *(experimental)*

Type: array of FilterEntry

The entries in TargetFilter are matched sequentially against targets and the first entry that matches determines if the target is included or not, depending on the value of `exclude` field in the entry. If filter is not specified, the one assumed is [{type: "browser", exclude: true}, {type: "tab", exclude: true}, {}] (i.e. include everything but `browser` and `tab`).

<a id="type-remotelocation"></a>
### Target.RemoteLocation *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `host` | string |  |
| `port` | integer |  |

<a id="type-windowstate"></a>
### Target.WindowState *(experimental)*

Type: string

The state of the target window.

Allowed values: `normal`, `minimized`, `maximized`, `fullscreen`

