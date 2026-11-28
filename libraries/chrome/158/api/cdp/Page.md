# Page domain

Copyright 2017 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.  Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp Actions and events related to the inspected page belong to the page domain.

Depends on: [Debugger](Debugger.md), [DOM](DOM.md), [IO](IO.md), [Network](Network.md), [Runtime](Runtime.md)

Methods are called as `Page.<command>` and events arrive as `Page.<event>`.

## Commands

### Page.addScriptToEvaluateOnLoad *(experimental)* *(deprecated)*

Deprecated, please use addScriptToEvaluateOnNewDocument instead.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `scriptSource` | string |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `identifier` | [ScriptIdentifier](#type-scriptidentifier) | Identifier of the added script. |

### Page.addScriptToEvaluateOnNewDocument

Evaluates given script in every frame upon creation (before loading frame's scripts).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `source` | string |  |
| `worldName` (optional) *(experimental)* | string | If specified, creates an isolated world with the given name and evaluates given script in it. This world name will be used as the ExecutionContextDescription::name when the corresponding event is emitted. |
| `includeCommandLineAPI` (optional) *(experimental)* | boolean | Specifies whether command line API should be available to the script, defaults to false. |
| `runImmediately` (optional) *(experimental)* | boolean | If true, runs the script immediately on existing execution contexts or worlds. Default: false. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `identifier` | [ScriptIdentifier](#type-scriptidentifier) | Identifier of the added script. |

### Page.bringToFront

Brings page to front (activates tab).

### Page.captureScreenshot

Capture page screenshot.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `format` (optional) | enum: `jpeg`, `png`, `webp` | Image compression format (defaults to png). |
| `quality` (optional) | integer | Compression quality from range [0..100] (jpeg only). |
| `clip` (optional) | [Viewport](#type-viewport) | Capture the screenshot of a given region only. |
| `fromSurface` (optional) *(experimental)* | boolean | Capture the screenshot from the surface, rather than the view. Defaults to true. |
| `captureBeyondViewport` (optional) *(experimental)* | boolean | Capture the screenshot beyond the viewport. Defaults to false. |
| `optimizeForSpeed` (optional) *(experimental)* | boolean | Optimize image encoding for speed, not for resulting size (defaults to false) |

**Returns**

| Name | Type | Description |
|---|---|---|
| `data` | binary | Base64-encoded image data. |

### Page.captureSnapshot *(experimental)*

Returns a snapshot of the page as a string. For MHTML format, the serialization includes iframes, shadow DOM, external resources, and element-inline styles.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `format` (optional) | enum: `mhtml` | Format (defaults to mhtml). |

**Returns**

| Name | Type | Description |
|---|---|---|
| `data` | string | Serialized page data. |

### Page.clearDeviceMetricsOverride *(experimental)* *(deprecated)*

Clears the overridden device metrics.

Redirects to `Emulation`.

### Page.clearDeviceOrientationOverride *(experimental)* *(deprecated)*

Clears the overridden Device Orientation.

Redirects to `DeviceOrientation`.

### Page.clearGeolocationOverride *(deprecated)*

Clears the overridden Geolocation Position and Error.

Redirects to `Emulation`.

### Page.createIsolatedWorld

Creates an isolated world for the given frame.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frameId` | [FrameId](#type-frameid) | Id of the frame in which the isolated world should be created. |
| `worldName` (optional) | string | An optional name which is reported in the Execution Context. |
| `grantUniveralAccess` (optional) | boolean | Whether or not universal access should be granted to the isolated world. This is a powerful option, use with caution. |
| `contentSecurityPolicy` (optional) | string | An optional content security policy to set for the isolated world. If omitted, any existing CSP for the world will be cleared. Note that clearing or updating the CSP does not immediately affect the active context in the same document because LocalDOMWindow caches the ContentSecurityPolicy object. The change takes effect on subsequent navigations when a new window context is created. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `executionContextId` | [Runtime.ExecutionContextId](Runtime.md#type-executioncontextid) | Execution context of the isolated world. |

### Page.deleteCookie *(experimental)* *(deprecated)*

Deletes browser cookie with given name, domain and path.

Redirects to `Network`.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `cookieName` | string | Name of the cookie to remove. |
| `url` | string | URL to match cooke domain and path. |

### Page.disable

Disables page domain notifications.

### Page.enable

Enables page domain notifications.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `enableFileChooserOpenedEvent` (optional) *(experimental)* | boolean | If true, the `Page.fileChooserOpened` event will be emitted regardless of the state set by `Page.setInterceptFileChooserDialog` command (default: false). |

### Page.getAppManifest

Gets the processed manifest for this current document. This API always waits for the manifest to be loaded. If manifestId is provided, and it does not match the manifest of the current document, this API errors out. If there is not a loaded page, this API errors out immediately.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `manifestId` (optional) | string |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `url` | string | Manifest location. |
| `errors` | array of [AppManifestError](#type-appmanifesterror) |  |
| `data` (optional) | string | Manifest content. |
| `parsed` (optional) *(experimental)* *(deprecated)* | [AppManifestParsedProperties](#type-appmanifestparsedproperties) | Parsed manifest properties. Deprecated, use manifest instead. |
| `manifest` *(experimental)* | [WebAppManifest](#type-webappmanifest) |  |

### Page.getInstallabilityErrors *(experimental)*

**Returns**

| Name | Type | Description |
|---|---|---|
| `installabilityErrors` | array of [InstallabilityError](#type-installabilityerror) |  |

### Page.getManifestIcons *(experimental)* *(deprecated)*

Deprecated because it's not guaranteed that the returned icon is in fact the one used for PWA installation.

**Returns**

| Name | Type | Description |
|---|---|---|
| `primaryIcon` (optional) | binary |  |

### Page.getAppId *(experimental)*

Returns the unique (PWA) app id, along with IWA bundle ID and parent app info. Only returns values if the feature flag 'WebAppEnableManifestId' is enabled

**Returns**

| Name | Type | Description |
|---|---|---|
| `appId` (optional) | string | App id, either from manifest's id attribute or computed from start_url |
| `recommendedId` (optional) | string | Recommendation for manifest's id attribute to match current id computed from start_url |
| `bundleId` (optional) | string | The bundle ID for an Isolated Web App (IWA) |
| `parentAppName` (optional) | string | The name of the parent app if this app is a Sub-App |

### Page.getSubApps *(experimental)*

Returns the list of installed child Sub-Apps for the inspected parent app.

**Returns**

| Name | Type | Description |
|---|---|---|
| `subApps` | array of [SubApp](#type-subapp) |  |

### Page.getSiblingSubApps *(experimental)*

Returns the list of sibling Sub-Apps sharing the same parent app if the inspected context is a Sub-App.

**Returns**

| Name | Type | Description |
|---|---|---|
| `subApps` | array of [SubApp](#type-subapp) |  |

### Page.getAdScriptAncestry *(experimental)*

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frameId` | [FrameId](#type-frameid) |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `adScriptAncestry` (optional) | [Network.AdAncestry](Network.md#type-adancestry) | The ancestry chain of ad script identifiers leading to this frame's creation, along with the root script's filterlist rule. The ancestry chain is ordered from the most immediate script (in the frame creation stack) to more distant ancestors (that created the immediately preceding script). Only sent if frame is labelled as an ad and ids are available. |

### Page.getSpellCheckCustomDictionary *(experimental)*

Returns the words that the frame's document added to its spell check custom dictionary with `document.spellCheckCustomDictionary.addWords()`, sorted. Page script cannot read the dictionary back; this lets developers inspect it.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frameId` | [FrameId](#type-frameid) |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `words` | array of string |  |

### Page.getFrameTree

Returns present frame tree structure.

**Returns**

| Name | Type | Description |
|---|---|---|
| `frameTree` | [FrameTree](#type-frametree) | Present frame tree structure. |

### Page.getLayoutMetrics

Returns metrics relating to the layouting of the page, such as viewport bounds/scale.

**Returns**

| Name | Type | Description |
|---|---|---|
| `layoutViewport` *(deprecated)* | [LayoutViewport](#type-layoutviewport) | Deprecated metrics relating to the layout viewport. Is in device pixels. Use `cssLayoutViewport` instead. |
| `visualViewport` *(deprecated)* | [VisualViewport](#type-visualviewport) | Deprecated metrics relating to the visual viewport. Is in device pixels. Use `cssVisualViewport` instead. |
| `contentSize` *(deprecated)* | [DOM.Rect](DOM.md#type-rect) | Deprecated size of scrollable area. Is in DP. Use `cssContentSize` instead. |
| `cssLayoutViewport` | [LayoutViewport](#type-layoutviewport) | Metrics relating to the layout viewport in CSS pixels. |
| `cssVisualViewport` | [VisualViewport](#type-visualviewport) | Metrics relating to the visual viewport in CSS pixels. |
| `cssContentSize` | [DOM.Rect](DOM.md#type-rect) | Size of scrollable area in CSS pixels. |

### Page.getNavigationHistory

Returns navigation history for the current page.

**Returns**

| Name | Type | Description |
|---|---|---|
| `currentIndex` | integer | Index of the current navigation history entry. |
| `entries` | array of [NavigationEntry](#type-navigationentry) | Array of navigation history entries. |

### Page.resetNavigationHistory

Resets navigation history for the current page.

### Page.getResourceContent *(experimental)*

Returns content of the given resource.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frameId` | [FrameId](#type-frameid) | Frame id to get resource for. |
| `url` | string | URL of the resource to get content for. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `content` | string | Resource content. |
| `base64Encoded` | boolean | True, if content was served as base64. |

### Page.getResourceTree *(experimental)*

Returns present frame / resource tree structure.

**Returns**

| Name | Type | Description |
|---|---|---|
| `frameTree` | [FrameResourceTree](#type-frameresourcetree) | Present frame / resource tree structure. |

### Page.handleJavaScriptDialog

Accepts or dismisses a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `accept` | boolean | Whether to accept or dismiss the dialog. |
| `promptText` (optional) | string | The text to enter into the dialog prompt before accepting. Used only if this is a prompt dialog. |

### Page.navigate

Navigates current page to the given URL.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `url` | string | URL to navigate the page to. |
| `referrer` (optional) | string | Referrer URL. |
| `transitionType` (optional) | [TransitionType](#type-transitiontype) | Intended transition type. |
| `frameId` (optional) | [FrameId](#type-frameid) | Frame id to navigate, if not specified navigates the top frame. |
| `referrerPolicy` (optional) *(experimental)* | [ReferrerPolicy](#type-referrerpolicy) | Referrer-policy used for the navigation. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `frameId` | [FrameId](#type-frameid) | Frame id that has navigated (or failed to navigate) |
| `loaderId` (optional) | [Network.LoaderId](Network.md#type-loaderid) | Loader identifier. This is omitted in case of same-document navigation, as the previously committed loaderId would not change. |
| `errorText` (optional) | string | User friendly error message, present if and only if navigation has failed. |
| `isDownload` (optional) *(experimental)* | boolean | Whether the navigation resulted in a download. |

### Page.navigateToHistoryEntry

Navigates current page to the given history entry.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `entryId` | integer | Unique id of the entry to navigate to. |

### Page.printToPDF

Print page as PDF.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `landscape` (optional) | boolean | Paper orientation. Defaults to false. |
| `displayHeaderFooter` (optional) | boolean | Display header and footer. Defaults to false. |
| `printBackground` (optional) | boolean | Print background graphics. Defaults to false. |
| `scale` (optional) | number | Scale of the webpage rendering. Defaults to 1. |
| `paperWidth` (optional) | number | Paper width in inches. Defaults to 8.5 inches. |
| `paperHeight` (optional) | number | Paper height in inches. Defaults to 11 inches. |
| `marginTop` (optional) | number | Top margin in inches. Defaults to 1cm (~0.4 inches). |
| `marginBottom` (optional) | number | Bottom margin in inches. Defaults to 1cm (~0.4 inches). |
| `marginLeft` (optional) | number | Left margin in inches. Defaults to 1cm (~0.4 inches). |
| `marginRight` (optional) | number | Right margin in inches. Defaults to 1cm (~0.4 inches). |
| `pageRanges` (optional) | string | Paper ranges to print, one based, e.g., '1-5, 8, 11-13'. Pages are printed in the document order, not in the order specified, and no more than once. Defaults to empty string, which implies the entire document is printed. The page numbers are quietly capped to actual page count of the document, and ranges beyond the end of the document are ignored. If this results in no pages to print, an error is reported. It is an error to specify a range with start greater than end. |
| `headerTemplate` (optional) | string | HTML template for the print header. Should be valid HTML markup with following classes used to inject printing values into them: - `date`: formatted print date - `title`: document title - `url`: document location - `pageNumber`: current page number - `totalPages`: total pages in the document  For example, `<span class=title></span>` would generate span containing the title. |
| `footerTemplate` (optional) | string | HTML template for the print footer. Should use the same format as the `headerTemplate`. |
| `preferCSSPageSize` (optional) | boolean | Whether or not to prefer page size as defined by css. Defaults to false, in which case the content will be scaled to fit the paper size. |
| `transferMode` (optional) *(experimental)* | enum: `ReturnAsBase64`, `ReturnAsStream` | return as stream |
| `generateTaggedPDF` (optional) *(experimental)* | boolean | Whether or not to generate tagged (accessible) PDF. Defaults to embedder choice. |
| `generateDocumentOutline` (optional) *(experimental)* | boolean | Whether or not to embed the document outline into the PDF. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `data` | binary | Base64-encoded pdf data. Empty if \|returnAsStream\| is specified. |
| `stream` (optional) *(experimental)* | [IO.StreamHandle](IO.md#type-streamhandle) | A handle of the stream that holds resulting PDF data. |

### Page.reload

Reloads given page optionally ignoring the cache.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ignoreCache` (optional) | boolean | If true, browser cache is ignored (as if the user pressed Shift+refresh). |
| `scriptToEvaluateOnLoad` (optional) | string | If set, the script will be injected into all frames of the inspected page after reload. Argument will be ignored if reloading dataURL origin. |
| `loaderId` (optional) *(experimental)* | [Network.LoaderId](Network.md#type-loaderid) | If set, an error will be thrown if the target page's main frame's loader id does not match the provided id. This prevents accidentally reloading an unintended target in case there's a racing navigation. |

### Page.removeScriptToEvaluateOnLoad *(experimental)* *(deprecated)*

Deprecated, please use removeScriptToEvaluateOnNewDocument instead.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `identifier` | [ScriptIdentifier](#type-scriptidentifier) |  |

### Page.removeScriptToEvaluateOnNewDocument

Removes given script from the list.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `identifier` | [ScriptIdentifier](#type-scriptidentifier) |  |

### Page.screencastFrameAck *(experimental)*

Acknowledges that a screencast frame has been received by the frontend.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `sessionId` | integer | Frame number. |

### Page.searchInResource *(experimental)*

Searches for given string in resource content.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frameId` | [FrameId](#type-frameid) | Frame id for resource to search in. |
| `url` | string | URL of the resource to search in. |
| `query` | string | String to search for. |
| `caseSensitive` (optional) | boolean | If true, search is case sensitive. |
| `isRegex` (optional) | boolean | If true, treats string parameter as regex. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `result` | array of [Debugger.SearchMatch](Debugger.md#type-searchmatch) | List of search matches. |

### Page.setAdBlockingEnabled *(experimental)*

Enable Chrome's experimental ad filter on all sites.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `enabled` | boolean | Whether to block ads. |

### Page.setBypassCSP

Enable page Content Security Policy by-passing.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `enabled` | boolean | Whether to bypass page CSP. |

### Page.getPermissionsPolicyState *(experimental)*

Get Permissions Policy state on given frame.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frameId` | [FrameId](#type-frameid) |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `states` | array of [PermissionsPolicyFeatureState](#type-permissionspolicyfeaturestate) |  |

### Page.getOriginTrials *(experimental)*

Get Origin Trials on given frame.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frameId` | [FrameId](#type-frameid) |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `originTrials` | array of [OriginTrial](#type-origintrial) |  |

### Page.setDeviceMetricsOverride *(experimental)* *(deprecated)*

Overrides the values of device screen dimensions (window.screen.width, window.screen.height, window.innerWidth, window.innerHeight, and "device-width"/"device-height"-related CSS media query results).

Redirects to `Emulation`.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `width` | integer | Overriding width value in pixels (minimum 0, maximum 10000000). 0 disables the override. |
| `height` | integer | Overriding height value in pixels (minimum 0, maximum 10000000). 0 disables the override. |
| `deviceScaleFactor` | number | Overriding device scale factor value. 0 disables the override. |
| `mobile` | boolean | Whether to emulate mobile device. This includes viewport meta tag, overlay scrollbars, text autosizing and more. |
| `scale` (optional) | number | Scale to apply to resulting view image. |
| `screenWidth` (optional) | integer | Overriding screen width value in pixels (minimum 0, maximum 10000000). |
| `screenHeight` (optional) | integer | Overriding screen height value in pixels (minimum 0, maximum 10000000). |
| `positionX` (optional) | integer | Overriding view X position on screen in pixels (minimum 0, maximum 10000000). |
| `positionY` (optional) | integer | Overriding view Y position on screen in pixels (minimum 0, maximum 10000000). |
| `dontSetVisibleSize` (optional) | boolean | Do not set visible view size, rely upon explicit setVisibleSize call. |
| `screenOrientation` (optional) | [Emulation.ScreenOrientation](Emulation.md#type-screenorientation) | Screen orientation override. |
| `viewport` (optional) | [Viewport](#type-viewport) | The viewport dimensions and scale. If not set, the override is cleared. |

### Page.setDeviceOrientationOverride *(experimental)* *(deprecated)*

Overrides the Device Orientation.

Redirects to `DeviceOrientation`.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `alpha` | number | Mock alpha |
| `beta` | number | Mock beta |
| `gamma` | number | Mock gamma |

### Page.setFontFamilies *(experimental)*

Set generic font families.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `fontFamilies` | [FontFamilies](#type-fontfamilies) | Specifies font families to set. If a font family is not specified, it won't be changed. |
| `forScripts` (optional) | array of [ScriptFontFamilies](#type-scriptfontfamilies) | Specifies font families to set for individual scripts. |

### Page.setFontSizes *(experimental)*

Set default font sizes.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `fontSizes` | [FontSizes](#type-fontsizes) | Specifies font sizes to set. If a font size is not specified, it won't be changed. |

### Page.setDocumentContent

Sets given markup as the document's HTML.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frameId` | [FrameId](#type-frameid) | Frame id to set HTML for. |
| `html` | string | HTML content to set. |

### Page.setDownloadBehavior *(experimental)* *(deprecated)*

Set the behavior when downloading a file.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `behavior` | enum: `deny`, `allow`, `default` | Whether to allow all or deny all download requests, or use default Chrome behavior if available (otherwise deny). |
| `downloadPath` (optional) | string | The default path to save downloaded files to. This is required if behavior is set to 'allow' |

### Page.setGeolocationOverride *(deprecated)*

Overrides the Geolocation Position or Error. Omitting any of the parameters emulates position unavailable.

Redirects to `Emulation`.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `latitude` (optional) | number | Mock latitude |
| `longitude` (optional) | number | Mock longitude |
| `accuracy` (optional) | number | Mock accuracy |

### Page.setLifecycleEventsEnabled

Controls whether page will emit lifecycle events.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `enabled` | boolean | If true, starts emitting lifecycle events. |

### Page.setTouchEmulationEnabled *(experimental)* *(deprecated)*

Toggles mouse event-based touch event emulation.

Redirects to `Emulation`.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `enabled` | boolean | Whether the touch event emulation should be enabled. |
| `configuration` (optional) | enum: `mobile`, `desktop` | Touch/gesture events configuration. Default: current platform. |

### Page.startScreencast *(experimental)*

Starts sending each frame using the `screencastFrame` event.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `format` (optional) | enum: `jpeg`, `png` | Image compression format. |
| `quality` (optional) | integer | Compression quality from range [0..100]. |
| `maxWidth` (optional) | integer | Maximum screenshot width. |
| `maxHeight` (optional) | integer | Maximum screenshot height. |
| `everyNthFrame` (optional) | integer | Send every n-th frame. Must be a positive integer. |
| `maxFramesInFlight` (optional) | integer | Maximum number of frames sent until screencastFrameAck is required. Defaults to 3. Must be a positive integer. |
| `sendLastFrame` (optional) | boolean | By default, after screencastFrameAck arrives, the next produced frame is sent. Passing this flag enables storing the last produced frame in memory, which is immediately sent upon screencastFrameAck. This way, overall performance is traded for a better latency. |

### Page.startScreenRecording *(experimental)*

Starts screencast video recording.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `audio` (optional) | boolean |  |
| `maxWidth` (optional) | integer | Maximum frame width in pixels. |
| `maxHeight` (optional) | integer | Maximum frame height in pixels. |
| `frameRate` (optional) | integer | Maximum frame rate in frames per second. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `stream` *(experimental)* | [IO.StreamHandle](IO.md#type-streamhandle) | A handle of the stream that holds resulting screencast data. |

### Page.stopScreenRecording *(experimental)*

Stops screencast video recording.

**Returns**

| Name | Type | Description |
|---|---|---|
| `stream` *(experimental)* | [IO.StreamHandle](IO.md#type-streamhandle) | A handle of the stream that holds resulting screencast data. |

### Page.stopLoading

Force the page stop all navigations and pending resource fetches.

### Page.crash *(experimental)*

Crashes renderer on the IO thread, generates minidumps.

### Page.close

Tries to close page, running its beforeunload hooks, if any.

### Page.setWebLifecycleState *(experimental)*

Tries to update the web lifecycle state of the page. It will transition the page to the given state according to: https://github.com/WICG/web-lifecycle/

**Parameters**

| Name | Type | Description |
|---|---|---|
| `state` | enum: `frozen`, `active` | Target lifecycle state |

### Page.stopScreencast *(experimental)*

Stops sending each frame in the `screencastFrame`.

### Page.produceCompilationCache *(experimental)*

Requests backend to produce compilation cache for the specified scripts. `scripts` are appended to the list of scripts for which the cache would be produced. The list may be reset during page navigation. When script with a matching URL is encountered, the cache is optionally produced upon backend discretion, based on internal heuristics. See also: `Page.compilationCacheProduced`.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `scripts` | array of [CompilationCacheParams](#type-compilationcacheparams) |  |

### Page.addCompilationCache *(experimental)*

Seeds compilation cache for given url. Compilation cache does not survive cross-process navigation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `url` | string |  |
| `data` | binary | Base64-encoded data |

### Page.clearCompilationCache *(experimental)*

Clears seeded compilation cache.

### Page.setSPCTransactionMode *(experimental)*

Sets the Secure Payment Confirmation transaction mode. https://w3c.github.io/secure-payment-confirmation/#sctn-automation-set-spc-transaction-mode

**Parameters**

| Name | Type | Description |
|---|---|---|
| `mode` | enum: `none`, `autoAccept`, `autoChooseToAuthAnotherWay`, `autoReject`, `autoOptOut` |  |

### Page.setRPHRegistrationMode *(experimental)*

Extensions for Custom Handlers API: https://html.spec.whatwg.org/multipage/system-state.html#rph-automation

**Parameters**

| Name | Type | Description |
|---|---|---|
| `mode` | enum: `none`, `autoAccept`, `autoReject` |  |

### Page.generateTestReport *(experimental)*

Generates a report for testing.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `message` | string | Message to be displayed in the report. |
| `group` (optional) | string | Specifies the endpoint group to deliver the report to. |

### Page.waitForDebugger *(experimental)*

Pauses page execution. Can be resumed using generic Runtime.runIfWaitingForDebugger.

### Page.setInterceptFileChooserDialog

Intercept file chooser requests and transfer control to protocol clients. When file chooser interception is enabled, native file chooser dialog is not shown. Instead, a protocol event `Page.fileChooserOpened` is emitted.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `enabled` | boolean |  |
| `cancel` (optional) *(experimental)* | boolean | If true, cancels the dialog by emitting relevant events (if any) in addition to not showing it if the interception is enabled (default: false). |

### Page.setPrerenderingAllowed *(experimental)*

Enable/disable prerendering manually.  This command is a short-term solution for https://crbug.com/1440085. See https://docs.google.com/document/d/12HVmFxYj5Jc-eJr5OmWsa2bqTJsbgGLKI6ZIyx0_wpA for more details.  TODO(https://crbug.com/1440085): Remove this once Puppeteer supports tab targets.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `isAllowed` | boolean |  |

### Page.getAnnotatedPageContent *(experimental)*

Get the annotated page content for the main frame. This is an experimental command that is subject to change.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `includeActionableInformation` (optional) | boolean | Whether to include actionable information. Defaults to true. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `content` | binary | The annotated page content as a base64 encoded protobuf. The format is defined by the `AnnotatedPageContent` message in components/optimization_guide/proto/features/common_quality_data.proto |

### Page.setInputVisualization *(experimental)*

Configures input visualization on the page.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `clicks` (optional) | boolean | Whether to enable click visualization. |

## Events

### Page.domContentEventFired

**Parameters**

| Name | Type | Description |
|---|---|---|
| `timestamp` | [Network.MonotonicTime](Network.md#type-monotonictime) |  |

### Page.fileChooserOpened

Emitted only when `page.interceptFileChooser` is enabled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frameId` *(experimental)* | [FrameId](#type-frameid) | Id of the frame containing input node. |
| `mode` | enum: `selectSingle`, `selectMultiple` | Input mode. |
| `backendNodeId` (optional) *(experimental)* | [DOM.BackendNodeId](DOM.md#type-backendnodeid) | Input node id. Only present for file choosers opened via an `<input type="file">` element. |

### Page.frameAttached

Fired when frame has been attached to its parent.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frameId` | [FrameId](#type-frameid) | Id of the frame that has been attached. |
| `parentFrameId` | [FrameId](#type-frameid) | Parent frame identifier. |
| `stack` (optional) | [Runtime.StackTrace](Runtime.md#type-stacktrace) | JavaScript stack trace of when frame was attached, only set if frame initiated from script. |

### Page.frameClearedScheduledNavigation *(deprecated)*

Fired when frame no longer has a scheduled navigation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frameId` | [FrameId](#type-frameid) | Id of the frame that has cleared its scheduled navigation. |

### Page.frameDetached

Fired when frame has been detached from its parent.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frameId` | [FrameId](#type-frameid) | Id of the frame that has been detached. |
| `reason` *(experimental)* | enum: `remove`, `swap` |  |

### Page.frameSubtreeWillBeDetached *(experimental)*

Fired before frame subtree is detached. Emitted before any frame of the subtree is actually detached.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frameId` | [FrameId](#type-frameid) | Id of the frame that is the root of the subtree that will be detached. |

### Page.frameNavigated

Fired once navigation of the frame has completed. Frame is now associated with the new loader.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frame` | [Frame](#type-frame) | Frame object. |
| `type` *(experimental)* | [NavigationType](#type-navigationtype) |  |

### Page.documentOpened *(experimental)*

Fired when opening document to write to.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frame` | [Frame](#type-frame) | Frame object. |

### Page.frameResized *(experimental)*

### Page.frameStartedNavigating *(experimental)*

Fired when a navigation starts. This event is fired for both renderer-initiated and browser-initiated navigations. For renderer-initiated navigations, the event is fired after `frameRequestedNavigation`. Navigation may still be cancelled after the event is issued. Multiple events can be fired for a single navigation, for example, when a same-document navigation becomes a cross-document navigation (such as in the case of a frameset).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frameId` | [FrameId](#type-frameid) | ID of the frame that is being navigated. |
| `url` | string | The URL the navigation started with. The final URL can be different. |
| `loaderId` | [Network.LoaderId](Network.md#type-loaderid) | Loader identifier. Even though it is present in case of same-document navigation, the previously committed loaderId would not change unless the navigation changes from a same-document to a cross-document navigation. |
| `navigationType` | enum: `reload`, `reloadBypassingCache`, `restore`, `restoreWithPost`, `historySameDocument`, `historyDifferentDocument`, `sameDocument`, `differentDocument` |  |

### Page.frameRequestedNavigation *(experimental)*

Fired when a renderer-initiated navigation is requested. Navigation may still be cancelled after the event is issued.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frameId` | [FrameId](#type-frameid) | Id of the frame that is being navigated. |
| `reason` | [ClientNavigationReason](#type-clientnavigationreason) | The reason for the navigation. |
| `url` | string | The destination URL for the requested navigation. |
| `disposition` | [ClientNavigationDisposition](#type-clientnavigationdisposition) | The disposition for the navigation. |

### Page.frameScheduledNavigation *(deprecated)*

Fired when frame schedules a potential navigation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frameId` | [FrameId](#type-frameid) | Id of the frame that has scheduled a navigation. |
| `delay` | number | Delay (in seconds) until the navigation is scheduled to begin. The navigation is not guaranteed to start. |
| `reason` | [ClientNavigationReason](#type-clientnavigationreason) | The reason for the navigation. |
| `url` | string | The destination URL for the scheduled navigation. |

### Page.frameStartedLoading *(experimental)*

Fired when frame has started loading.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frameId` | [FrameId](#type-frameid) | Id of the frame that has started loading. |

### Page.frameStoppedLoading *(experimental)*

Fired when frame has stopped loading.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frameId` | [FrameId](#type-frameid) | Id of the frame that has stopped loading. |

### Page.downloadWillBegin *(experimental)* *(deprecated)*

Fired when page is about to start a download. Deprecated. Use Browser.downloadWillBegin instead.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frameId` | [FrameId](#type-frameid) | Id of the frame that caused download to begin. |
| `guid` | string | Global unique identifier of the download. |
| `url` | string | URL of the resource being downloaded. |
| `suggestedFilename` | string | Suggested file name of the resource (the actual name of the file saved on disk may differ). |

### Page.downloadProgress *(experimental)* *(deprecated)*

Fired when download makes progress. Last call has |done| == true. Deprecated. Use Browser.downloadProgress instead.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `guid` | string | Global unique identifier of the download. |
| `totalBytes` | number | Total expected bytes to download. |
| `receivedBytes` | number | Total bytes received. |
| `state` | enum: `inProgress`, `completed`, `canceled` | Download status. |

### Page.interstitialHidden

Fired when interstitial page was hidden

### Page.interstitialShown

Fired when interstitial page was shown

### Page.javascriptDialogClosed

Fired when a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload) has been closed.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frameId` *(experimental)* | [FrameId](#type-frameid) | Frame id. |
| `result` | boolean | Whether dialog was confirmed. |
| `userInput` | string | User input in case of prompt. |

### Page.javascriptDialogOpening

Fired when a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload) is about to open.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `url` | string | Frame url. |
| `frameId` *(experimental)* | [FrameId](#type-frameid) | Frame id. |
| `message` | string | Message that will be displayed by the dialog. |
| `type` | [DialogType](#type-dialogtype) | Dialog type. |
| `hasBrowserHandler` | boolean | True iff browser is capable showing or acting on the given dialog. When browser has no dialog handler for given target, calling alert while Page domain is engaged will stall the page execution. Execution can be resumed via calling Page.handleJavaScriptDialog. |
| `defaultPrompt` (optional) | string | Default dialog prompt. |

### Page.lifecycleEvent

Fired for lifecycle events (navigation, load, paint, etc) in the current target (including local frames).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frameId` | [FrameId](#type-frameid) | Id of the frame. |
| `loaderId` | [Network.LoaderId](Network.md#type-loaderid) | Loader identifier. Empty string if the request is fetched from worker. |
| `name` | string |  |
| `timestamp` | [Network.MonotonicTime](Network.md#type-monotonictime) |  |

### Page.backForwardCacheNotUsed *(experimental)*

Fired for failed bfcache history navigations if BackForwardCache feature is enabled. Do not assume any ordering with the Page.frameNavigated event. This event is fired only for main-frame history navigation where the document changes (non-same-document navigations), when bfcache navigation fails.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `loaderId` | [Network.LoaderId](Network.md#type-loaderid) | The loader id for the associated navigation. |
| `frameId` | [FrameId](#type-frameid) | The frame id of the associated frame. |
| `notRestoredExplanations` | array of [BackForwardCacheNotRestoredExplanation](#type-backforwardcachenotrestoredexplanation) | Array of reasons why the page could not be cached. This must not be empty. |
| `notRestoredExplanationsTree` (optional) | [BackForwardCacheNotRestoredExplanationTree](#type-backforwardcachenotrestoredexplanationtree) | Tree structure of reasons why the page could not be cached for each frame. |

### Page.loadEventFired

**Parameters**

| Name | Type | Description |
|---|---|---|
| `timestamp` | [Network.MonotonicTime](Network.md#type-monotonictime) |  |

### Page.navigatedWithinDocument *(experimental)*

Fired when same-document navigation happens, e.g. due to history API usage or anchor navigation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frameId` | [FrameId](#type-frameid) | Id of the frame. |
| `url` | string | Frame's new url. |
| `navigationType` | enum: `fragment`, `historyApi`, `other` | Navigation type |

### Page.screencastFrame *(experimental)*

Compressed image data requested by the `startScreencast`.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `data` | binary | Base64-encoded compressed image. |
| `metadata` | [ScreencastFrameMetadata](#type-screencastframemetadata) | Screencast frame metadata. |
| `sessionId` | integer | Frame number. |

### Page.screencastVisibilityChanged *(experimental)*

Fired when the page with currently enabled screencast was shown or hidden `.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `visible` | boolean | True if the page is visible. |

### Page.windowOpen

Fired when a new window is going to be opened, via window.open(), link click, form submission, etc.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `url` | string | The URL for the new window. |
| `windowName` | string | Window name. |
| `windowFeatures` | array of string | An array of enabled window features. |
| `userGesture` | boolean | Whether or not it was triggered by user gesture. |

### Page.compilationCacheProduced *(experimental)*

Issued for every compilation cache generated.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `url` | string |  |
| `data` | binary | Base64-encoded data |

## Types

<a id="type-frameid"></a>
### Page.FrameId

Type: string

Unique frame identifier.

<a id="type-adframetype"></a>
### Page.AdFrameType *(experimental)*

Type: string

Indicates whether a frame has been identified as an ad.

Allowed values: `none`, `child`, `root`

<a id="type-adframeexplanation"></a>
### Page.AdFrameExplanation *(experimental)*

Type: string

Allowed values: `ParentIsAd`, `CreatedByAdScript`, `MatchedBlockingRule`

<a id="type-adframestatus"></a>
### Page.AdFrameStatus *(experimental)*

Type: object

Indicates whether a frame has been identified as an ad and why.

**Properties**

| Name | Type | Description |
|---|---|---|
| `adFrameType` | [AdFrameType](#type-adframetype) |  |
| `explanations` (optional) | array of [AdFrameExplanation](#type-adframeexplanation) |  |

<a id="type-securecontexttype"></a>
### Page.SecureContextType *(experimental)*

Type: string

Indicates whether the frame is a secure context and why it is the case.

Allowed values: `Secure`, `SecureLocalhost`, `InsecureScheme`, `InsecureAncestor`

<a id="type-crossoriginisolatedcontexttype"></a>
### Page.CrossOriginIsolatedContextType *(experimental)*

Type: string

Indicates whether the frame is cross-origin isolated and why it is the case.

Allowed values: `Isolated`, `NotIsolated`, `NotIsolatedFeatureDisabled`

<a id="type-gatedapifeatures"></a>
### Page.GatedAPIFeatures *(experimental)*

Type: string

Allowed values: `SharedArrayBuffers`, `SharedArrayBuffersTransferAllowed`, `PerformanceMeasureMemory`, `PerformanceProfile`

<a id="type-permissionspolicyfeature"></a>
### Page.PermissionsPolicyFeature *(experimental)*

Type: string

All Permissions Policy features. This enum should match the one defined in services/network/public/cpp/permissions_policy/permissions_policy_features.json5. LINT.IfChange(PermissionsPolicyFeature)

Allowed values: `accelerometer`, `all-screens-capture`, `ambient-light-sensor`, `aria-notify`, `autofill`, `autoplay`, `bluetooth`, `browsing-topics`, `camera`, `captured-surface-control`, `ch-dpr`, `ch-device-memory`, `ch-downlink`, `ch-ect`, `ch-prefers-color-scheme`, `ch-prefers-reduced-motion`, `ch-prefers-reduced-transparency`, `ch-rtt`, `ch-save-data`, `ch-ua`, `ch-ua-arch`, `ch-ua-bitness`, `ch-ua-high-entropy-values`, `ch-ua-platform`, `ch-ua-model`, `ch-ua-mobile`, `ch-ua-form-factors`, `ch-ua-full-version`, `ch-ua-full-version-list`, `ch-ua-platform-version`, `ch-ua-wow64`, `ch-viewport-height`, `ch-viewport-width`, `ch-width`, `clipboard-read`, `clipboard-write`, `compute-pressure`, `controlled-frame`, `cross-origin-isolated`, `deferred-fetch`, `deferred-fetch-minimal`, `device-attributes`, `digital-credentials-create`, `digital-credentials-get`, `direct-sockets`, `direct-sockets-multicast`, `display-capture`, `document-domain`, `encrypted-media`, `execution-while-out-of-viewport`, `execution-while-not-rendered`, `focus-without-user-activation`, `fullscreen`, `frobulate`, `gamepad`, `geolocation`, `gyroscope`, `haptics`, `hid`, `identity-credentials-get`, `idle-detection`, `interest-cohort`, `keyboard-map`, `language-detector`, `language-model`, `local-fonts`, `local-network`, `local-network-access`, `loopback-network`, `magnetometer`, `manual-text`, `media-playback-while-not-visible`, `microphone`, `midi`, `on-device-speech-recognition`, `otp-credentials`, `payment`, `picture-in-picture`, `private-state-token-issuance`, `private-state-token-redemption`, `publickey-credentials-create`, `publickey-credentials-get`, `publickey-credentials-remote-client-data-json`, `rewriter`, `screen-wake-lock`, `serial`, `smart-card`, `speaker-selection`, `storage-access`, `sub-apps`, `summarizer`, `sync-xhr`, `tools`, `translator`, `unbounded-element`, `unload`, `usb`, `usb-unrestricted`, `vertical-scroll`, `web-app-installation`, `webnn`, `web-printing`, `web-share`, `window-management`, `writer`, `xr-spatial-tracking`

<a id="type-permissionspolicyblockreason"></a>
### Page.PermissionsPolicyBlockReason *(experimental)*

Type: string

LINT.ThenChange(//services/network/public/cpp/permissions_policy/permissions_policy_features.json5:PermissionsPolicy) Reason for a permissions policy feature to be disabled.

Allowed values: `Header`, `IframeAttribute`, `InFencedFrameTree`, `InIsolatedApp`

<a id="type-permissionspolicyblocklocator"></a>
### Page.PermissionsPolicyBlockLocator *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `frameId` | [FrameId](#type-frameid) |  |
| `blockReason` | [PermissionsPolicyBlockReason](#type-permissionspolicyblockreason) |  |

<a id="type-permissionspolicyfeaturestate"></a>
### Page.PermissionsPolicyFeatureState *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `feature` | [PermissionsPolicyFeature](#type-permissionspolicyfeature) |  |
| `allowed` | boolean |  |
| `locator` (optional) | [PermissionsPolicyBlockLocator](#type-permissionspolicyblocklocator) |  |

<a id="type-origintrialtokenstatus"></a>
### Page.OriginTrialTokenStatus *(experimental)*

Type: string

Origin Trial(https://www.chromium.org/blink/origin-trials) support. Status for an Origin Trial token.

Allowed values: `Success`, `NotSupported`, `Insecure`, `Expired`, `WrongOrigin`, `InvalidSignature`, `Malformed`, `WrongVersion`, `FeatureDisabled`, `TokenDisabled`, `FeatureDisabledForUser`, `UnknownTrial`

<a id="type-origintrialstatus"></a>
### Page.OriginTrialStatus *(experimental)*

Type: string

Status for an Origin Trial.

Allowed values: `Enabled`, `ValidTokenNotProvided`, `OSNotSupported`, `TrialNotAllowed`

<a id="type-origintrialusagerestriction"></a>
### Page.OriginTrialUsageRestriction *(experimental)*

Type: string

Allowed values: `None`, `Subset`

<a id="type-origintrialtoken"></a>
### Page.OriginTrialToken *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `origin` | string |  |
| `matchSubDomains` | boolean |  |
| `trialName` | string |  |
| `expiryTime` | [Network.TimeSinceEpoch](Network.md#type-timesinceepoch) |  |
| `isThirdParty` | boolean |  |
| `usageRestriction` | [OriginTrialUsageRestriction](#type-origintrialusagerestriction) |  |

<a id="type-origintrialtokenwithstatus"></a>
### Page.OriginTrialTokenWithStatus *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `rawTokenText` | string |  |
| `parsedToken` (optional) | [OriginTrialToken](#type-origintrialtoken) | `parsedToken` is present only when the token is extractable and parsable. |
| `status` | [OriginTrialTokenStatus](#type-origintrialtokenstatus) |  |

<a id="type-origintrial"></a>
### Page.OriginTrial *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `trialName` | string |  |
| `status` | [OriginTrialStatus](#type-origintrialstatus) |  |
| `tokensWithStatus` | array of [OriginTrialTokenWithStatus](#type-origintrialtokenwithstatus) |  |

<a id="type-securityorigindetails"></a>
### Page.SecurityOriginDetails *(experimental)*

Type: object

Additional information about the frame document's security origin.

**Properties**

| Name | Type | Description |
|---|---|---|
| `isLocalhost` | boolean | Indicates whether the frame document's security origin is one of the local hostnames (e.g. "localhost") or IP addresses (IPv4 127.0.0.0/8 or IPv6 ::1). |

<a id="type-frame"></a>
### Page.Frame

Type: object

Information about the Frame on the page.

**Properties**

| Name | Type | Description |
|---|---|---|
| `id` | [FrameId](#type-frameid) | Frame unique identifier. |
| `parentId` (optional) | [FrameId](#type-frameid) | Parent frame identifier. |
| `loaderId` | [Network.LoaderId](Network.md#type-loaderid) | Identifier of the loader associated with this frame. |
| `name` (optional) | string | Frame's name as specified in the tag. |
| `url` | string | Frame document's URL without fragment. |
| `urlFragment` (optional) *(experimental)* | string | Frame document's URL fragment including the '#'. |
| `domainAndRegistry` *(experimental)* | string | Frame document's registered domain, taking the public suffixes list into account. Extracted from the Frame's url. Example URLs: http://www.google.com/file.html -> "google.com" http://a.b.co.uk/file.html      -> "b.co.uk" |
| `securityOrigin` | string | Frame document's security origin. |
| `securityOriginDetails` (optional) *(experimental)* | [SecurityOriginDetails](#type-securityorigindetails) | Additional details about the frame document's security origin. |
| `mimeType` | string | Frame document's mimeType as determined by the browser. |
| `unreachableUrl` (optional) *(experimental)* | string | If the frame failed to load, this contains the URL that could not be loaded. Note that unlike url above, this URL may contain a fragment. |
| `adFrameStatus` (optional) *(experimental)* | [AdFrameStatus](#type-adframestatus) | Indicates whether this frame was tagged as an ad and why. |
| `secureContextType` *(experimental)* | [SecureContextType](#type-securecontexttype) | Indicates whether the main document is a secure context and explains why that is the case. |
| `crossOriginIsolatedContextType` *(experimental)* | [CrossOriginIsolatedContextType](#type-crossoriginisolatedcontexttype) | Indicates whether this is a cross origin isolated context. |
| `gatedAPIFeatures` *(experimental)* | array of [GatedAPIFeatures](#type-gatedapifeatures) | Indicated which gated APIs / features are available. |

<a id="type-frameresource"></a>
### Page.FrameResource *(experimental)*

Type: object

Information about the Resource on the page.

**Properties**

| Name | Type | Description |
|---|---|---|
| `url` | string | Resource URL. |
| `type` | [Network.ResourceType](Network.md#type-resourcetype) | Type of this resource. |
| `mimeType` | string | Resource mimeType as determined by the browser. |
| `lastModified` (optional) | [Network.TimeSinceEpoch](Network.md#type-timesinceepoch) | last-modified timestamp as reported by server. |
| `contentSize` (optional) | number | Resource content size. |
| `failed` (optional) | boolean | True if the resource failed to load. |
| `canceled` (optional) | boolean | True if the resource was canceled during loading. |

<a id="type-frameresourcetree"></a>
### Page.FrameResourceTree *(experimental)*

Type: object

Information about the Frame hierarchy along with their cached resources.

**Properties**

| Name | Type | Description |
|---|---|---|
| `frame` | [Frame](#type-frame) | Frame information for this tree item. |
| `childFrames` (optional) | array of [FrameResourceTree](#type-frameresourcetree) | Child frames. |
| `resources` | array of [FrameResource](#type-frameresource) | Information about frame resources. |

<a id="type-frametree"></a>
### Page.FrameTree

Type: object

Information about the Frame hierarchy.

**Properties**

| Name | Type | Description |
|---|---|---|
| `frame` | [Frame](#type-frame) | Frame information for this tree item. |
| `childFrames` (optional) | array of [FrameTree](#type-frametree) | Child frames. |

<a id="type-scriptidentifier"></a>
### Page.ScriptIdentifier

Type: string

Unique script identifier.

<a id="type-transitiontype"></a>
### Page.TransitionType

Type: string

Transition type.

Allowed values: `link`, `typed`, `address_bar`, `auto_bookmark`, `auto_subframe`, `manual_subframe`, `generated`, `auto_toplevel`, `form_submit`, `reload`, `keyword`, `keyword_generated`, `other`

<a id="type-navigationentry"></a>
### Page.NavigationEntry

Type: object

Navigation history entry.

**Properties**

| Name | Type | Description |
|---|---|---|
| `id` | integer | Unique id of the navigation history entry. |
| `url` | string | URL of the navigation history entry. |
| `userTypedURL` | string | URL that the user typed in the url bar. |
| `title` | string | Title of the navigation history entry. |
| `transitionType` | [TransitionType](#type-transitiontype) | Transition type. |

<a id="type-screencastframemetadata"></a>
### Page.ScreencastFrameMetadata *(experimental)*

Type: object

Screencast frame metadata.

**Properties**

| Name | Type | Description |
|---|---|---|
| `offsetTop` | number | Top offset in DIP. |
| `pageScaleFactor` | number | Page scale factor. |
| `deviceWidth` | number | Device screen width in DIP. |
| `deviceHeight` | number | Device screen height in DIP. |
| `scrollOffsetX` | number | Position of horizontal scroll in CSS pixels. |
| `scrollOffsetY` | number | Position of vertical scroll in CSS pixels. |
| `timestamp` (optional) | [Network.TimeSinceEpoch](Network.md#type-timesinceepoch) | Frame swap timestamp. |
| `monotonicTimestamp` (optional) | [Network.MonotonicTime](Network.md#type-monotonictime) | Frame swap timestamp as monotonic time. |

<a id="type-dialogtype"></a>
### Page.DialogType

Type: string

Javascript dialog type.

Allowed values: `alert`, `confirm`, `prompt`, `beforeunload`

<a id="type-appmanifesterror"></a>
### Page.AppManifestError

Type: object

Error while paring app manifest.

**Properties**

| Name | Type | Description |
|---|---|---|
| `message` | string | Error message. |
| `critical` | integer | If critical, this is a non-recoverable parse error. |
| `line` | integer | Error line. |
| `column` | integer | Error column. |

<a id="type-appmanifestparsedproperties"></a>
### Page.AppManifestParsedProperties *(experimental)*

Type: object

Parsed app manifest properties.

**Properties**

| Name | Type | Description |
|---|---|---|
| `scope` | string | Computed scope value |

<a id="type-layoutviewport"></a>
### Page.LayoutViewport

Type: object

Layout viewport position and dimensions.

**Properties**

| Name | Type | Description |
|---|---|---|
| `pageX` | integer | Horizontal offset relative to the document (CSS pixels). |
| `pageY` | integer | Vertical offset relative to the document (CSS pixels). |
| `clientWidth` | integer | Width (CSS pixels), excludes scrollbar if present. |
| `clientHeight` | integer | Height (CSS pixels), excludes scrollbar if present. |

<a id="type-visualviewport"></a>
### Page.VisualViewport

Type: object

Visual viewport position, dimensions, and scale.

**Properties**

| Name | Type | Description |
|---|---|---|
| `offsetX` | number | Horizontal offset relative to the layout viewport (CSS pixels). |
| `offsetY` | number | Vertical offset relative to the layout viewport (CSS pixels). |
| `pageX` | number | Horizontal offset relative to the document (CSS pixels). |
| `pageY` | number | Vertical offset relative to the document (CSS pixels). |
| `clientWidth` | number | Width (CSS pixels), excludes scrollbar if present. |
| `clientHeight` | number | Height (CSS pixels), excludes scrollbar if present. |
| `scale` | number | Scale relative to the ideal viewport (size at width=device-width). |
| `zoom` (optional) | number | Page zoom factor (CSS to device independent pixels ratio). |

<a id="type-viewport"></a>
### Page.Viewport

Type: object

Viewport for capturing screenshot.

**Properties**

| Name | Type | Description |
|---|---|---|
| `x` | number | X offset in device independent pixels (dip). |
| `y` | number | Y offset in device independent pixels (dip). |
| `width` | number | Rectangle width in device independent pixels (dip). |
| `height` | number | Rectangle height in device independent pixels (dip). |
| `scale` | number | Page scale factor. |

<a id="type-fontfamilies"></a>
### Page.FontFamilies *(experimental)*

Type: object

Generic font families collection.

**Properties**

| Name | Type | Description |
|---|---|---|
| `standard` (optional) | string | The standard font-family. |
| `fixed` (optional) | string | The fixed font-family. |
| `serif` (optional) | string | The serif font-family. |
| `sansSerif` (optional) | string | The sansSerif font-family. |
| `cursive` (optional) | string | The cursive font-family. |
| `fantasy` (optional) | string | The fantasy font-family. |
| `math` (optional) | string | The math font-family. |

<a id="type-scriptfontfamilies"></a>
### Page.ScriptFontFamilies *(experimental)*

Type: object

Font families collection for a script.

**Properties**

| Name | Type | Description |
|---|---|---|
| `script` | string | Name of the script which these font families are defined for. |
| `fontFamilies` | [FontFamilies](#type-fontfamilies) | Generic font families collection for the script. |

<a id="type-fontsizes"></a>
### Page.FontSizes *(experimental)*

Type: object

Default font sizes.

**Properties**

| Name | Type | Description |
|---|---|---|
| `standard` (optional) | integer | Default standard font size. |
| `fixed` (optional) | integer | Default fixed font size. |

<a id="type-clientnavigationreason"></a>
### Page.ClientNavigationReason *(experimental)*

Type: string

Allowed values: `anchorClick`, `formSubmissionGet`, `formSubmissionPost`, `httpHeaderRefresh`, `initialFrameNavigation`, `metaTagRefresh`, `other`, `pageBlockInterstitial`, `reload`, `scriptInitiated`

<a id="type-clientnavigationdisposition"></a>
### Page.ClientNavigationDisposition *(experimental)*

Type: string

Allowed values: `currentTab`, `newTab`, `newWindow`, `download`

<a id="type-installabilityerrorargument"></a>
### Page.InstallabilityErrorArgument *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Argument name (e.g. name:'minimum-icon-size-in-pixels'). |
| `value` | string | Argument value (e.g. value:'64'). |

<a id="type-installabilityerror"></a>
### Page.InstallabilityError *(experimental)*

Type: object

The installability error

**Properties**

| Name | Type | Description |
|---|---|---|
| `errorId` | string | The error id (e.g. 'manifest-missing-suitable-icon'). |
| `errorArguments` | array of [InstallabilityErrorArgument](#type-installabilityerrorargument) | The list of error arguments (e.g. {name:'minimum-icon-size-in-pixels', value:'64'}). |

<a id="type-referrerpolicy"></a>
### Page.ReferrerPolicy *(experimental)*

Type: string

The referring-policy used for the navigation.

Allowed values: `noReferrer`, `noReferrerWhenDowngrade`, `origin`, `originWhenCrossOrigin`, `sameOrigin`, `strictOrigin`, `strictOriginWhenCrossOrigin`, `unsafeUrl`

<a id="type-compilationcacheparams"></a>
### Page.CompilationCacheParams *(experimental)*

Type: object

Per-script compilation cache parameters for `Page.produceCompilationCache`

**Properties**

| Name | Type | Description |
|---|---|---|
| `url` | string | The URL of the script to produce a compilation cache entry for. |
| `eager` (optional) | boolean | A hint to the backend whether eager compilation is recommended. (the actual compilation mode used is upon backend discretion). |

<a id="type-filefilter"></a>
### Page.FileFilter *(experimental)*

Type: object

The manifest of a webapp, see https://www.w3.org/TR/appmanifest/#dfn-manifest. Some fields do not appear in the standard since the API is designed to expose more browser internal states.

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` (optional) | string |  |
| `accepts` (optional) | array of string |  |

<a id="type-filehandler"></a>
### Page.FileHandler *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `action` | string |  |
| `name` | string |  |
| `accepts` (optional) | array of [FileFilter](#type-filefilter) | Mimic a map, name is the key, accepts is the value. |
| `launchType` | string | Won't repeat the enums, using string for easy comparison. Same as the other enums below. |

<a id="type-imageresource"></a>
### Page.ImageResource *(experimental)*

Type: object

The image definition used in both icon and screenshot.

**Properties**

| Name | Type | Description |
|---|---|---|
| `url` | string | The src field in the definition, but changing to url in favor of consistency. |
| `sizes` (optional) | string |  |
| `type` (optional) | string |  |

<a id="type-launchhandler"></a>
### Page.LaunchHandler *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `clientMode` | string |  |

<a id="type-protocolhandler"></a>
### Page.ProtocolHandler *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `protocol` | string |  |
| `url` | string |  |

<a id="type-relatedapplication"></a>
### Page.RelatedApplication *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `id` (optional) | string |  |
| `url` | string |  |

<a id="type-scopeextension"></a>
### Page.ScopeExtension *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `origin` | string | Instead of using tuple, this field always returns the serialized string for easy understanding and comparison. |
| `hasOriginWildcard` | boolean |  |

<a id="type-screenshot"></a>
### Page.Screenshot *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `image` | [ImageResource](#type-imageresource) |  |
| `formFactor` | string |  |
| `label` (optional) | string |  |

<a id="type-sharetarget"></a>
### Page.ShareTarget *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `action` | string |  |
| `method` | string |  |
| `enctype` | string |  |
| `title` (optional) | string | Embed the ShareTargetParams |
| `text` (optional) | string |  |
| `url` (optional) | string |  |
| `files` (optional) | array of [FileFilter](#type-filefilter) |  |

<a id="type-shortcut"></a>
### Page.Shortcut *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string |  |
| `url` | string |  |

<a id="type-webappmanifest"></a>
### Page.WebAppManifest *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `backgroundColor` (optional) | string |  |
| `description` (optional) | string | The extra description provided by the manifest. |
| `dir` (optional) | string |  |
| `display` (optional) | string |  |
| `displayOverrides` (optional) | array of string | The overrided display mode controlled by the user. |
| `fileHandlers` (optional) | array of [FileHandler](#type-filehandler) | The handlers to open files. |
| `icons` (optional) | array of [ImageResource](#type-imageresource) |  |
| `id` (optional) | string |  |
| `lang` (optional) | string |  |
| `launchHandler` (optional) | [LaunchHandler](#type-launchhandler) | TODO(crbug.com/1231886): This field is non-standard and part of a Chrome experiment. See: https://github.com/WICG/web-app-launch/blob/main/launch_handler.md |
| `name` (optional) | string |  |
| `orientation` (optional) | string |  |
| `preferRelatedApplications` (optional) | boolean |  |
| `protocolHandlers` (optional) | array of [ProtocolHandler](#type-protocolhandler) | The handlers to open protocols. |
| `relatedApplications` (optional) | array of [RelatedApplication](#type-relatedapplication) |  |
| `scope` (optional) | string |  |
| `scopeExtensions` (optional) | array of [ScopeExtension](#type-scopeextension) | Non-standard, see https://github.com/WICG/manifest-incubations/blob/gh-pages/scope_extensions-explainer.md |
| `screenshots` (optional) | array of [Screenshot](#type-screenshot) | The screenshots used by chromium. |
| `shareTarget` (optional) | [ShareTarget](#type-sharetarget) |  |
| `shortName` (optional) | string |  |
| `shortcuts` (optional) | array of [Shortcut](#type-shortcut) |  |
| `startUrl` (optional) | string |  |
| `themeColor` (optional) | string |  |

<a id="type-subapp"></a>
### Page.SubApp

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Display name of the sub-app. |
| `scope` | string | Scope of the sub-app. |
| `manifestId` | string | Manifest id of the sub-app. |
| `startUrl` | string | Start URL of the sub-app. |

<a id="type-navigationtype"></a>
### Page.NavigationType *(experimental)*

Type: string

The type of a frameNavigated event.

Allowed values: `Navigation`, `BackForwardCacheRestore`

<a id="type-backforwardcachenotrestoredreason"></a>
### Page.BackForwardCacheNotRestoredReason *(experimental)*

Type: string

List of not restored reasons for back-forward cache.

Allowed values: `NotPrimaryMainFrame`, `BackForwardCacheDisabled`, `RelatedActiveContentsExist`, `HTTPStatusNotOK`, `SchemeNotHTTPOrHTTPS`, `Loading`, `WasGrantedMediaAccess`, `DisableForRenderFrameHostCalled`, `DomainNotAllowed`, `HTTPMethodNotGET`, `SubframeIsNavigating`, `Timeout`, `CacheLimit`, `JavaScriptExecution`, `RendererProcessKilled`, `RendererProcessCrashed`, `SchedulerTrackedFeatureUsed`, `ConflictingBrowsingInstance`, `CacheFlushed`, `ServiceWorkerVersionActivation`, `SessionRestored`, `ServiceWorkerPostMessage`, `EnteredBackForwardCacheBeforeServiceWorkerHostAdded`, `RenderFrameHostReused_SameSite`, `RenderFrameHostReused_CrossSite`, `ServiceWorkerClaim`, `IgnoreEventAndEvict`, `HaveInnerContents`, `TimeoutPuttingInCache`, `BackForwardCacheDisabledByLowMemory`, `BackForwardCacheDisabledByCommandLine`, `NetworkRequestDatapipeDrainedAsBytesConsumer`, `NetworkRequestRedirected`, `NetworkRequestTimeout`, `NetworkExceedsBufferLimit`, `NavigationCancelledWhileRestoring`, `NotMostRecentNavigationEntry`, `BackForwardCacheDisabledForPrerender`, `UserAgentOverrideDiffers`, `ForegroundCacheLimit`, `ForwardCacheDisabled`, `BrowsingInstanceNotSwapped`, `BackForwardCacheDisabledForDelegate`, `UnloadHandlerExistsInMainFrame`, `UnloadHandlerExistsInSubFrame`, `ServiceWorkerUnregistration`, `CacheControlNoStore`, `CacheControlNoStoreCookieModified`, `CacheControlNoStoreHTTPOnlyCookieModified`, `NoResponseHead`, `Unknown`, `ActivationNavigationsDisallowedForBug1234857`, `ErrorDocument`, `FencedFramesEmbedder`, `CookieDisabled`, `HTTPAuthRequired`, `CookieFlushed`, `BroadcastChannelOnMessage`, `WebViewSettingsChanged`, `WebViewJavaScriptObjectChanged`, `WebViewMessageListenerInjected`, `WebViewSafeBrowsingAllowlistChanged`, `WebViewDocumentStartJavascriptChanged`, `WebSocket`, `WebTransport`, `WebRTC`, `MainResourceHasCacheControlNoStore`, `MainResourceHasCacheControlNoCache`, `SubresourceHasCacheControlNoStore`, `SubresourceHasCacheControlNoCache`, `ContainsPlugins`, `DocumentLoaded`, `OutstandingNetworkRequestOthers`, `RequestedMIDIPermission`, `RequestedAudioCapturePermission`, `RequestedVideoCapturePermission`, `RequestedBackForwardCacheBlockedSensors`, `RequestedBackgroundWorkPermission`, `BroadcastChannel`, `WebXR`, `SharedWorker`, `SharedWorkerMessage`, `SharedWorkerWithNoActiveClient`, `WebLocks`, `WebLocksContention`, `WebHID`, `WebBluetooth`, `WebShare`, `RequestedStorageAccessGrant`, `WebNfc`, `OutstandingNetworkRequestFetch`, `OutstandingNetworkRequestXHR`, `AppBanner`, `Printing`, `WebDatabase`, `PictureInPicture`, `SpeechRecognizer`, `IdleManager`, `PaymentManager`, `SpeechSynthesis`, `KeyboardLock`, `WebOTPService`, `OutstandingNetworkRequestDirectSocket`, `InjectedJavascript`, `InjectedStyleSheet`, `KeepaliveRequest`, `IndexedDBEvent`, `Dummy`, `JsNetworkRequestReceivedCacheControlNoStoreResource`, `WebRTCUsedWithCCNS`, `WebTransportUsedWithCCNS`, `WebSocketUsedWithCCNS`, `SmartCard`, `LiveMediaStreamTrack`, `UnloadHandler`, `ParserAborted`, `ContentSecurityHandler`, `ContentWebAuthenticationAPI`, `ContentFileChooser`, `ContentSerial`, `ContentFileSystemAccess`, `ContentMediaDevicesDispatcherHost`, `ContentWebBluetooth`, `ContentWebUSB`, `ContentMediaSessionService`, `ContentScreenReader`, `ContentDiscarded`, `EmbedderPopupBlockerTabHelper`, `EmbedderSafeBrowsingTriggeredPopupBlocker`, `EmbedderSafeBrowsingThreatDetails`, `EmbedderAppBannerManager`, `EmbedderDomDistillerViewerSource`, `EmbedderDomDistillerSelfDeletingRequestDelegate`, `EmbedderOomInterventionTabHelper`, `EmbedderOfflinePage`, `EmbedderChromePasswordManagerClientBindCredentialManager`, `EmbedderPermissionRequestManager`, `EmbedderModalDialog`, `EmbedderExtensions`, `EmbedderExtensionMessaging`, `EmbedderExtensionMessagingForOpenPort`, `EmbedderExtensionSentMessageToCachedFrame`, `EmbedderExtensionFrame`, `EmbedderPrivilegedWebContents`, `RequestedByWebViewClient`, `PostMessageByWebViewClient`, `CacheControlNoStoreDeviceBoundSessionTerminated`, `CacheLimitPrunedOnModerateMemoryPressure`, `CacheLimitPrunedOnCriticalMemoryPressure`

<a id="type-backforwardcachenotrestoredreasontype"></a>
### Page.BackForwardCacheNotRestoredReasonType *(experimental)*

Type: string

Types of not restored reasons for back-forward cache.

Allowed values: `SupportPending`, `PageSupportNeeded`, `Circumstantial`

<a id="type-backforwardcacheblockingdetails"></a>
### Page.BackForwardCacheBlockingDetails *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `url` (optional) | string | Url of the file where blockage happened. Optional because of tests. |
| `function` (optional) | string | Function name where blockage happened. Optional because of anonymous functions and tests. |
| `lineNumber` | integer | Line number in the script (0-based). |
| `columnNumber` | integer | Column number in the script (0-based). |

<a id="type-backforwardcachenotrestoredexplanation"></a>
### Page.BackForwardCacheNotRestoredExplanation *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `type` | [BackForwardCacheNotRestoredReasonType](#type-backforwardcachenotrestoredreasontype) | Type of the reason |
| `reason` | [BackForwardCacheNotRestoredReason](#type-backforwardcachenotrestoredreason) | Not restored reason |
| `context` (optional) | string | Context associated with the reason. The meaning of this context is dependent on the reason: - EmbedderExtensionSentMessageToCachedFrame: the extension ID.  |
| `details` (optional) | array of [BackForwardCacheBlockingDetails](#type-backforwardcacheblockingdetails) |  |

<a id="type-backforwardcachenotrestoredexplanationtree"></a>
### Page.BackForwardCacheNotRestoredExplanationTree *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `url` | string | URL of each frame |
| `explanations` | array of [BackForwardCacheNotRestoredExplanation](#type-backforwardcachenotrestoredexplanation) | Not restored reasons of each frame |
| `children` | array of [BackForwardCacheNotRestoredExplanationTree](#type-backforwardcachenotrestoredexplanationtree) | Array of children frame |

