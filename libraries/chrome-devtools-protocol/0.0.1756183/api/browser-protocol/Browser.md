# Browser domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

The Browser domain defines methods and events for browser managing.

21 methods, 2 events, 10 types.

## Methods

### Browser.setPermission

**Experimental**

Set permission settings for given embedding and embedded origins.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `permission` | [Browser.PermissionDescriptor](#type-permissiondescriptor) | Descriptor of permission to override. |
| `setting` | [Browser.PermissionSetting](#type-permissionsetting) | Setting of the permission. |
| `origin` (optional) | string | Embedding origin the permission applies to, all origins if not specified. |
| `embeddedOrigin` (optional) | string | Embedded origin the permission applies to. It is ignored unless the embedding origin is present and valid. If the embedding origin is provided but the embedded origin isn't, the embedding origin is used as the embedded origin. |
| `browserContextId` (optional) | [Browser.BrowserContextID](#type-browsercontextid) | Context to override. When omitted, default browser context is used. |

### Browser.grantPermissions

**Experimental** · **Deprecated**

Grant specific permissions to the given origin and reject all others. Deprecated. Use
setPermission instead.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `permissions` | array of [Browser.PermissionType](#type-permissiontype) |  |
| `origin` (optional) | string | Origin the permission applies to, all origins if not specified. |
| `browserContextId` (optional) | [Browser.BrowserContextID](#type-browsercontextid) | BrowserContext to override permissions. When omitted, default browser context is used. |

### Browser.resetPermissions

Reset all permission management for all origins.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `browserContextId` (optional) | [Browser.BrowserContextID](#type-browsercontextid) | BrowserContext to reset permissions. When omitted, default browser context is used. |

### Browser.setDownloadBehavior

**Experimental**

Set the behavior when downloading a file.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `behavior` | string | Whether to allow all or deny all download requests, or use default Chrome behavior if available (otherwise deny). \|allowAndName\| allows download and names files according to their download guids. Allowed values: `deny`, `allow`, `allowAndName`, `default` |
| `browserContextId` (optional) | [Browser.BrowserContextID](#type-browsercontextid) | BrowserContext to set download behavior. When omitted, default browser context is used. |
| `downloadPath` (optional) | string | The default path to save downloaded files to. This is required if behavior is set to 'allow' or 'allowAndName'. |
| `eventsEnabled` (optional) | boolean | Whether to emit download events (defaults to false). |

### Browser.cancelDownload

**Experimental**

Cancel a download if in progress

**Parameters**

| Name | Type | Description |
|---|---|---|
| `guid` | string | Global unique identifier of the download. |
| `browserContextId` (optional) | [Browser.BrowserContextID](#type-browsercontextid) | BrowserContext to perform the action in. When omitted, default browser context is used. |

### Browser.close

Close browser gracefully.

No parameters.

### Browser.crash

**Experimental**

Crashes browser on the main thread.

No parameters.

### Browser.crashGpuProcess

**Experimental**

Crashes GPU process.

No parameters.

### Browser.getVersion

Returns version information.

No parameters.

**Return object**

| Name | Type | Description |
|---|---|---|
| `protocolVersion` | string | Protocol version. |
| `product` | string | Product name. |
| `revision` | string | Product revision. |
| `userAgent` | string | User-Agent. |
| `jsVersion` | string | V8 version. |

### Browser.getBrowserCommandLine

**Experimental**

Returns the command line switches for the browser process if, and only if
--enable-automation is on the commandline.

No parameters.

**Return object**

| Name | Type | Description |
|---|---|---|
| `arguments` | array of string | Commandline parameters |

### Browser.addMockCamera

**Experimental**

Adds a mock camera in the shared video capture device list for
test automation. The mock camera is not scoped to a particular page or
frame and is removed when the DevTools session that created it disconnects.
Returns success after the video capture service confirms registration.
Does not wait for device-list updates or devicechange events in pages.
Registration failures are reported as errors.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `deviceId` | string | Required non-empty identifier for the mock camera within the current DevTools session. Different sessions can use the same identifier without replacing each other's cameras. This is not the MediaDeviceInfo.deviceId exposed to the page. An identifier that is already registered or being registered in this session is rejected. The existing camera or registration attempt is left unchanged, including any active streams. |

### Browser.getHistograms

**Experimental**

Get Chrome histograms.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `query` (optional) | string | Requested substring in name. Only histograms which have query as a substring in their name are extracted. An empty or absent query returns all histograms. |
| `delta` (optional) | boolean | If true, retrieve delta since last delta call. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `histograms` | array of [Browser.Histogram](#type-histogram) | Histograms. |

### Browser.getHistogram

**Experimental**

Get a Chrome histogram by name.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `name` | string | Requested histogram name. |
| `delta` (optional) | boolean | If true, retrieve delta since last delta call. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `histogram` | [Browser.Histogram](#type-histogram) | Histogram. |

### Browser.getWindowBounds

**Experimental**

Get position and size of the browser window.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `windowId` | [Browser.WindowID](#type-windowid) | Browser window id. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `bounds` | [Browser.Bounds](#type-bounds) | Bounds information of the window. When window state is 'minimized', the restored window position and size are returned. |

### Browser.getWindowForTarget

**Experimental**

Get the browser window that contains the devtools target.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `targetId` (optional) | [Target.TargetID](Target.md#type-targetid) | Devtools agent host id. If called as a part of the session, associated targetId is used. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `windowId` | [Browser.WindowID](#type-windowid) | Browser window id. |
| `bounds` | [Browser.Bounds](#type-bounds) | Bounds information of the window. When window state is 'minimized', the restored window position and size are returned. |

### Browser.setWindowBounds

**Experimental**

Set position and/or size of the browser window.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `windowId` | [Browser.WindowID](#type-windowid) | Browser window id. |
| `bounds` | [Browser.Bounds](#type-bounds) | New window bounds. The 'minimized', 'maximized' and 'fullscreen' states cannot be combined with 'left', 'top', 'width' or 'height'. Leaves unspecified fields unchanged. |

### Browser.setContentsSize

**Experimental**

Set size of the browser contents resizing browser window as necessary.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `windowId` | [Browser.WindowID](#type-windowid) | Browser window id. |
| `width` (optional) | integer | The window contents width in DIP. Assumes current width if omitted. Must be specified if 'height' is omitted. |
| `height` (optional) | integer | The window contents height in DIP. Assumes current height if omitted. Must be specified if 'width' is omitted. |

### Browser.setDockTile

**Experimental**

Set dock tile details, platform-specific.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `badgeLabel` (optional) | string |  |
| `image` (optional) | string | Png encoded image. (Encoded as a base64 string when passed over JSON) |

### Browser.executeBrowserCommand

**Experimental**

Invoke custom browser commands used by telemetry.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `commandId` | [Browser.BrowserCommandId](#type-browsercommandid) |  |

### Browser.getGlobalPrivacyControl

**Experimental**

Gets the current globally-applied privacy control status
See https://www.w3.org/TR/gpc/#get-global-privacy-control

No parameters.

**Return object**

| Name | Type | Description |
|---|---|---|
| `gpc` | boolean |  |

### Browser.setGlobalPrivacyControl

**Experimental**

Sets and then gets the current globally-applied privacy control status
See https://www.w3.org/TR/gpc/#set-global-privacy-control

**Parameters**

| Name | Type | Description |
|---|---|---|
| `gpc` | boolean |  |

**Return object**

| Name | Type | Description |
|---|---|---|
| `gpc` | boolean |  |

## Events

### Browser.downloadWillBegin

**Experimental**

Fired when page is about to start a download.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `frameId` | [Page.FrameId](Page.md#type-frameid) | Id of the frame that caused the download to begin. |
| `guid` | string | Global unique identifier of the download. |
| `url` | string | URL of the resource being downloaded. |
| `suggestedFilename` | string | Suggested file name of the resource (the actual name of the file saved on disk may differ). |

### Browser.downloadProgress

**Experimental**

Fired when download makes progress. Last call has |done| == true.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `guid` | string | Global unique identifier of the download. |
| `totalBytes` | number | Total expected bytes to download. |
| `receivedBytes` | number | Total bytes received. |
| `state` | string | Download status. Allowed values: `inProgress`, `completed`, `canceled` |
| `filePath` (optional) | string | **Experimental** If download is "completed", provides the path of the downloaded file. Depending on the platform, it is not guaranteed to be set, nor the file is guaranteed to exist. |

## Types

<a id="type-browsercontextid"></a>
### Browser.BrowserContextID

**Experimental**

Type: string

<a id="type-windowid"></a>
### Browser.WindowID

**Experimental**

Type: integer

<a id="type-windowstate"></a>
### Browser.WindowState

**Experimental**

The state of the browser window.

Type: string

Allowed values: `normal`, `minimized`, `maximized`, `fullscreen`

<a id="type-bounds"></a>
### Browser.Bounds

**Experimental**

Browser window bounds information

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `left` (optional) | integer | The offset from the left edge of the screen to the window in pixels. |
| `top` (optional) | integer | The offset from the top edge of the screen to the window in pixels. |
| `width` (optional) | integer | The window width in pixels. |
| `height` (optional) | integer | The window height in pixels. |
| `windowState` (optional) | [Browser.WindowState](#type-windowstate) | The window state. Default to normal. |

<a id="type-permissiontype"></a>
### Browser.PermissionType

**Experimental**

Type: string

Allowed values: `ar`, `audioCapture`, `automaticFullscreen`, `backgroundFetch`, `backgroundSync`, `cameraPanTiltZoom`, `capturedSurfaceControl`, `clipboardReadWrite`, `clipboardSanitizedWrite`, `displayCapture`, `durableStorage`, `geolocation`, `handTracking`, `idleDetection`, `keyboardLock`, `localFonts`, `localNetwork`, `localNetworkAccess`, `loopbackNetwork`, `midi`, `midiSysex`, `nfc`, `notifications`, `paymentHandler`, `periodicBackgroundSync`, `pointerLock`, `protectedMediaIdentifier`, `sensors`, `smartCard`, `speakerSelection`, `storageAccess`, `videoCapture`, `vr`, `wakeLockScreen`, `wakeLockSystem`, `webAppInstallation`, `webPrinting`, `windowManagement`

<a id="type-permissionsetting"></a>
### Browser.PermissionSetting

**Experimental**

Type: string

Allowed values: `granted`, `denied`, `prompt`

<a id="type-permissiondescriptor"></a>
### Browser.PermissionDescriptor

**Experimental**

Definition of PermissionDescriptor defined in the Permissions API:
https://w3c.github.io/permissions/#dom-permissiondescriptor.

Type: object

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
### Browser.BrowserCommandId

**Experimental**

Browser command ids used by executeBrowserCommand.

Type: string

Allowed values: `openTabSearch`, `closeTabSearch`, `openGlic`

<a id="type-bucket"></a>
### Browser.Bucket

**Experimental**

Chrome histogram bucket.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `low` | integer | Minimum value (inclusive). |
| `high` | integer | Maximum value (exclusive). |
| `count` | integer | Number of samples. |

<a id="type-histogram"></a>
### Browser.Histogram

**Experimental**

Chrome histogram.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Name. |
| `sum` | integer | Sum of sample values. |
| `count` | integer | Total number of samples. |
| `buckets` | array of [Browser.Bucket](#type-bucket) | Buckets. |
