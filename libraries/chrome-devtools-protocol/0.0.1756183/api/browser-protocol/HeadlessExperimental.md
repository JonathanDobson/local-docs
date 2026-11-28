# HeadlessExperimental domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

**Experimental**

This domain provides experimental commands only supported in headless mode.

Depends on: [Page](Page.md), [Runtime](Runtime.md)

3 methods, 0 events, 1 types.

## Methods

### HeadlessExperimental.beginFrame

Sends a BeginFrame to the target and returns when the frame was completed. Optionally captures a
screenshot from the resulting frame. Requires that the target was created with enabled
BeginFrameControl. Designed for use with --run-all-compositor-stages-before-draw, see also
https://goo.gle/chrome-headless-rendering for more background.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frameTimeTicks` (optional) | number | Timestamp of this BeginFrame in Renderer TimeTicks (milliseconds of uptime). If not set, the current time will be used. |
| `interval` (optional) | number | The interval between BeginFrames that is reported to the compositor, in milliseconds. Defaults to a 60 frames/second interval, i.e. about 16.666 milliseconds. |
| `noDisplayUpdates` (optional) | boolean | Whether updates should not be committed and drawn onto the display. False by default. If true, only side effects of the BeginFrame will be run, such as layout and animations, but any visual updates may not be visible on the display or in screenshots. |
| `screenshot` (optional) | [HeadlessExperimental.ScreenshotParams](#type-screenshotparams) | If set, a screenshot of the frame will be captured and returned in the response. Otherwise, no screenshot will be captured. Note that capturing a screenshot can fail, for example, during renderer initialization. In such a case, no screenshot data will be returned. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `hasDamage` | boolean | Whether the BeginFrame resulted in damage and, thus, a new frame was committed to the display. Reported for diagnostic uses, may be removed in the future. |
| `screenshotData` (optional) | string | Base64-encoded image data of the screenshot, if one was requested and successfully taken. (Encoded as a base64 string when passed over JSON) |

### HeadlessExperimental.disable

**Deprecated**

Disables headless events for the target.

No parameters.

### HeadlessExperimental.enable

**Deprecated**

Enables headless events for the target.

No parameters.

## Types

<a id="type-screenshotparams"></a>
### HeadlessExperimental.ScreenshotParams

Encoding options for a screenshot.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `format` (optional) | string | Image compression format (defaults to png). Allowed values: `jpeg`, `png`, `webp` |
| `quality` (optional) | integer | Compression quality from range [0..100] (jpeg and webp only). |
| `optimizeForSpeed` (optional) | boolean | Optimize image encoding for speed, not for resulting size (defaults to false) |
