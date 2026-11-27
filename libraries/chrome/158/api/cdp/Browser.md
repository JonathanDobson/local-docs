# Browser domain

Copyright 2017 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.  Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp The Browser domain defines methods and events for browser managing.

Methods are called as `Browser.<command>` and events arrive as `Browser.<event>`.

## Commands

### Browser.setPermission *(experimental)*

Set permission settings for given embedding and embedded origins.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `permission` | [PermissionDescriptor](#type-permissiondescriptor) | Descriptor of permission to override. |
| `setting` | [PermissionSetting](#type-permissionsetting) | Setting of the permission. |
| `origin` (optional) | string | Embedding origin the permission applies to, all origins if not specified. |
| `embeddedOrigin` (optional) | string | Embedded origin the permission applies to. It is ignored unless the embedding origin is present and valid. If the embedding origin is provided but the embedded origin isn't, the embedding origin is used as the embedded origin. |
| `browserContextId` (optional) | [BrowserContextID](#type-browsercontextid) | Context to override. When omitted, default browser context is used. |

### Browser.grantPermissions *(experimental)* *(deprecated)*

Grant specific permissions to the given origin and reject all others. Deprecated. Use setPermission instead.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `permissions` | array of [PermissionType](#type-permissiontype) |  |
| `origin` (optional) | string | Origin the permission applies to, all origins if not specified. |
| `browserContextId` (optional) | [BrowserContextID](#type-browsercontextid) | BrowserContext to override permissions. When omitted, default browser context is used. |

### Browser.resetPermissions

Reset all permission management for all origins.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `browserContextId` (optional) | [BrowserContextID](#type-browsercontextid) | BrowserContext to reset permissions. When omitted, default browser context is used. |

### Browser.setDownloadBehavior *(experimental)*

Set the behavior when downloading a file.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `behavior` | enum: `deny`, `allow`, `allowAndName`, `default` | Whether to allow all or deny all download requests, or use default Chrome behavior if available (otherwise deny). \|allowAndName\| allows download and names files according to their download guids. |
| `browserContextId` (optional) | [BrowserContextID](#type-browsercontextid) | BrowserContext to set download behavior. When omitted, default browser context is used. |
| `downloadPath` (optional) | string | The default path to save downloaded files to. This is required if behavior is set to 'allow' or 'allowAndName'. |
| `eventsEnabled` (optional) | boolean | Whether to emit download events (defaults to false). |

### Browser.cancelDownload *(experimental)*

Cancel a download if in progress

**Parameters**

| Name | Type | Description |
|---|---|---|
| `guid` | string | Global unique identifier of the download. |
| `browserContextId` (optional) | [BrowserContextID](#type-browsercontextid) | BrowserContext to perform the action in. When omitted, default browser context is used. |

### Browser.close

Close browser gracefully.

### Browser.crash *(experimental)*

Crashes browser on the main thread.

### Browser.crashGpuProcess *(experimental)*

Crashes GPU process.

### Browser.getVersion

Returns version information.

**Returns**

| Name | Type | Description |
|---|---|---|
| `protocolVersion` | string | Protocol version. |
| `product` | string | Product name. |
| `revision` | string | Product revision. |
| `userAgent` | string | User-Agent. |
| `jsVersion` | string | V8 version. |

### Browser.getBrowserCommandLine *(experimental)*

Returns the command line switches for the browser process if, and only if --enable-automation is on the commandline.

**Returns**

| Name | Type | Description |
|---|---|---|
| `arguments` | array of string | Commandline parameters |

### Browser.addMockCamera *(experimental)*

Adds or updates a mock camera in the shared video capture device list for test automation. The mock camera is not scoped to a particular page or frame and is removed when the DevTools session that created it disconnects.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `deviceId` | string | Required non-empty identifier for the mock camera within the current DevTools session. Different sessions can use the same identifier without replacing each other's cameras. This is not the MediaDeviceInfo.deviceId exposed to the page. |

### Browser.getHistograms *(experimental)*

Get Chrome histograms.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `query` (optional) | string | Requested substring in name. Only histograms which have query as a substring in their name are extracted. An empty or absent query returns all histograms. |
| `delta` (optional) | boolean | If true, retrieve delta since last delta call. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `histograms` | array of [Histogram](#type-histogram) | Histograms. |

### Browser.getHistogram *(experimental)*

Get a Chrome histogram by name.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `name` | string | Requested histogram name. |
| `delta` (optional) | boolean | If true, retrieve delta since last delta call. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `histogram` | [Histogram](#type-histogram) | Histogram. |

### Browser.getWindowBounds *(experimental)*

Get position and size of the browser window.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `windowId` | [WindowID](#type-windowid) | Browser window id. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `bounds` | [Bounds](#type-bounds) | Bounds information of the window. When window state is 'minimized', the restored window position and size are returned. |

### Browser.getWindowForTarget *(experimental)*

Get the browser window that contains the devtools target.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `targetId` (optional) | [Target.TargetID](Target.md#type-targetid) | Devtools agent host id. If called as a part of the session, associated targetId is used. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `windowId` | [WindowID](#type-windowid) | Browser window id. |
| `bounds` | [Bounds](#type-bounds) | Bounds information of the window. When window state is 'minimized', the restored window position and size are returned. |

### Browser.setWindowBounds *(experimental)*

Set position and/or size of the browser window.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `windowId` | [WindowID](#type-windowid) | Browser window id. |
| `bounds` | [Bounds](#type-bounds) | New window bounds. The 'minimized', 'maximized' and 'fullscreen' states cannot be combined with 'left', 'top', 'width' or 'height'. Leaves unspecified fields unchanged. |

### Browser.setContentsSize *(experimental)*

Set size of the browser contents resizing browser window as necessary.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `windowId` | [WindowID](#type-windowid) | Browser window id. |
| `width` (optional) | integer | The window contents width in DIP. Assumes current width if omitted. Must be specified if 'height' is omitted. |
| `height` (optional) | integer | The window contents height in DIP. Assumes current height if omitted. Must be specified if 'width' is omitted. |

### Browser.setDockTile *(experimental)*

Set dock tile details, platform-specific.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `badgeLabel` (optional) | string |  |
| `image` (optional) | binary | Png encoded image. |

### Browser.executeBrowserCommand *(experimental)*

Invoke custom browser commands used by telemetry.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `commandId` | [BrowserCommandId](#type-browsercommandid) |  |

### Browser.addPrivacySandboxEnrollmentOverride

Allows a site to use privacy sandbox features that require enrollment without the site actually being enrolled. Only supported on page targets.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `url` | string |  |

### Browser.getGlobalPrivacyControl *(experimental)*

Gets the current globally-applied privacy control status See https://www.w3.org/TR/gpc/#get-global-privacy-control

**Returns**

| Name | Type | Description |
|---|---|---|
| `gpc` | boolean |  |

### Browser.setGlobalPrivacyControl *(experimental)*

Sets and then gets the current globally-applied privacy control status See https://www.w3.org/TR/gpc/#set-global-privacy-control

**Parameters**

| Name | Type | Description |
|---|---|---|
| `gpc` | boolean |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `gpc` | boolean |  |

## Events

### Browser.downloadWillBegin *(experimental)*

Fired when page is about to start a download.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frameId` | [Page.FrameId](Page.md#type-frameid) | Id of the frame that caused the download to begin. |
| `guid` | string | Global unique identifier of the download. |
| `url` | string | URL of the resource being downloaded. |
| `suggestedFilename` | string | Suggested file name of the resource (the actual name of the file saved on disk may differ). |

### Browser.downloadProgress *(experimental)*

Fired when download makes progress. Last call has |done| == true.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `guid` | string | Global unique identifier of the download. |
| `totalBytes` | number | Total expected bytes to download. |
| `receivedBytes` | number | Total bytes received. |
| `state` | enum: `inProgress`, `completed`, `canceled` | Download status. |
| `filePath` (optional) *(experimental)* | string | If download is "completed", provides the path of the downloaded file. Depending on the platform, it is not guaranteed to be set, nor the file is guaranteed to exist. |

## Types

<a id="type-browsercontextid"></a>
### Browser.BrowserContextID *(experimental)*

Type: string

<a id="type-windowid"></a>
### Browser.WindowID *(experimental)*

Type: integer

<a id="type-windowstate"></a>
### Browser.WindowState *(experimental)*

Type: string

The state of the browser window.

Allowed values: `normal`, `minimized`, `maximized`, `fullscreen`

<a id="type-bounds"></a>
### Browser.Bounds *(experimental)*

Type: object

Browser window bounds information

**Properties**

| Name | Type | Description |
|---|---|---|
| `left` (optional) | integer | The offset from the left edge of the screen to the window in pixels. |
| `top` (optional) | integer | The offset from the top edge of the screen to the window in pixels. |
| `width` (optional) | integer | The window width in pixels. |
| `height` (optional) | integer | The window height in pixels. |
| `windowState` (optional) | [WindowState](#type-windowstate) | The window state. Default to normal. |

<a id="type-permissiontype"></a>
### Browser.PermissionType *(experimental)*

Type: string

Allowed values: `ar`, `audioCapture`, `automaticFullscreen`, `backgroundFetch`, `backgroundSync`, `cameraPanTiltZoom`, `capturedSurfaceControl`, `clipboardReadWrite`, `clipboardSanitizedWrite`, `displayCapture`, `durableStorage`, `geolocation`, `handTracking`, `idleDetection`, `keyboardLock`, `localFonts`, `localNetwork`, `localNetworkAccess`, `loopbackNetwork`, `midi`, `midiSysex`, `nfc`, `notifications`, `paymentHandler`, `periodicBackgroundSync`, `pointerLock`, `protectedMediaIdentifier`, `sensors`, `smartCard`, `speakerSelection`, `storageAccess`, `topLevelStorageAccess`, `videoCapture`, `vr`, `wakeLockScreen`, `wakeLockSystem`, `webAppInstallation`, `webPrinting`, `windowManagement`

<a id="type-permissionsetting"></a>
### Browser.PermissionSetting *(experimental)*

Type: string

Allowed values: `granted`, `denied`, `prompt`

<a id="type-permissiondescriptor"></a>
### Browser.PermissionDescriptor *(experimental)*

Type: object

Definition of PermissionDescriptor defined in the Permissions API: https://w3c.github.io/permissions/#dom-permissiondescriptor.

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Name of permission. See https://cs.chromium.org/chromium/src/third_party/blink/renderer/modules/permissions/permission_descriptor.idl for valid permission names. |
| `sysex` (optional) | boolean | For "midi" permission, may also specify sysex control. |
| `userVisibleOnly` (optional) | boolean | For "push" permission, may specify userVisibleOnly. Note that userVisibleOnly = true is the only currently supported type. |
| `allowWithoutSanitization` (optional) | boolean | For "clipboard" permission, may specify allowWithoutSanitization. |
| `allowWithoutGesture` (optional) | boolean | For "fullscreen" permission, must specify allowWithoutGesture:true. |
| `panTiltZoom` (optional) | boolean | For "camera" permission, may specify panTiltZoom. |

<a id="type-browsercommandid"></a>
### Browser.BrowserCommandId *(experimental)*

Type: string

Browser command ids used by executeBrowserCommand.

Allowed values: `openTabSearch`, `closeTabSearch`, `openGlic`

<a id="type-bucket"></a>
### Browser.Bucket *(experimental)*

Type: object

Chrome histogram bucket.

**Properties**

| Name | Type | Description |
|---|---|---|
| `low` | integer | Minimum value (inclusive). |
| `high` | integer | Maximum value (exclusive). |
| `count` | integer | Number of samples. |

<a id="type-histogram"></a>
### Browser.Histogram *(experimental)*

Type: object

Chrome histogram.

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Name. |
| `sum` | integer | Sum of sample values. |
| `count` | integer | Total number of samples. |
| `buckets` | array of [Bucket](#type-bucket) | Buckets. |

