# Emulation domain

Copyright 2017 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.  Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp This domain emulates different environments for the page.

Depends on: [DOM](DOM.md), [Page](Page.md), [Runtime](Runtime.md)

Methods are called as `Emulation.<command>` and events arrive as `Emulation.<event>`.

## Commands

### Emulation.canEmulate *(deprecated)*

Tells whether emulation is supported.

**Returns**

| Name | Type | Description |
|---|---|---|
| `result` | boolean | True if emulation is supported. |

### Emulation.clearDeviceMetricsOverride

Clears the overridden device metrics.

### Emulation.clearGeolocationOverride

Clears the overridden Geolocation Position and Error.

### Emulation.resetPageScaleFactor *(experimental)*

Requests that page scale factor is reset to initial values.

### Emulation.setFocusEmulationEnabled *(experimental)*

Enables or disables simulating a focused and active page.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `enabled` | boolean | Whether to enable to disable focus emulation. |

### Emulation.setAutoDarkModeOverride *(experimental)*

Automatically render all web contents using a dark theme.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `enabled` (optional) | boolean | Whether to enable or disable automatic dark mode. If not specified, any existing override will be cleared. |

### Emulation.setCPUThrottlingRate

Enables CPU throttling to emulate slow CPUs.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `rate` | number | Throttling rate as a slowdown factor (1 is no throttle, 2 is 2x slowdown, etc). |

### Emulation.setDefaultBackgroundColorOverride

Sets or clears an override of the default background color of the frame. This override is used if the content does not specify one.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `color` (optional) | [DOM.RGBA](DOM.md#type-rgba) | RGBA of the default background color. If not specified, any existing override will be cleared. |

### Emulation.setSafeAreaInsetsOverride *(experimental)*

Overrides the values for env(safe-area-inset-*) and env(safe-area-max-inset-*). Unset values will cause the respective variables to be undefined, even if previously overridden.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `insets` | [SafeAreaInsets](#type-safeareainsets) |  |

### Emulation.setVirtualKeyboardGeometryOverride *(experimental)*

Overrides virtual keyboard geometry in CSS pixels, relative to the top-level viewport. The provided rect is used for navigator.virtualKeyboard.boundingRect, geometrychange events, and env(keyboard-inset-*) values on the inspected frame. The override applies independently of navigator.virtualKeyboard.overlaysContent so clients can preview overlay geometry without mutating page state. Values are rounded to the nearest CSS pixel. Omitting the rect clears the override.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `keyboardRect` (optional) | [DOM.Rect](DOM.md#type-rect) |  |

### Emulation.setDeviceMetricsOverride

Overrides the values of device screen dimensions (window.screen.width, window.screen.height, window.innerWidth, window.innerHeight, and "device-width"/"device-height"-related CSS media query results).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `width` | integer | Overriding width value in pixels (minimum 0, maximum 10000000). 0 disables the override. |
| `height` | integer | Overriding height value in pixels (minimum 0, maximum 10000000). 0 disables the override. |
| `deviceScaleFactor` | number | Overriding device scale factor value. 0 disables the override. |
| `mobile` | boolean | Whether to emulate mobile device. This includes viewport meta tag, overlay scrollbars, text autosizing and more. |
| `scale` (optional) *(experimental)* | number | Scale to apply to resulting view image. |
| `screenWidth` (optional) *(experimental)* | integer | Overriding screen width value in pixels (minimum 0, maximum 10000000). |
| `screenHeight` (optional) *(experimental)* | integer | Overriding screen height value in pixels (minimum 0, maximum 10000000). |
| `positionX` (optional) *(experimental)* | integer | Overriding view X position on screen in pixels (minimum 0, maximum 10000000). |
| `positionY` (optional) *(experimental)* | integer | Overriding view Y position on screen in pixels (minimum 0, maximum 10000000). |
| `dontSetVisibleSize` (optional) *(experimental)* | boolean | Do not set visible view size, rely upon explicit setVisibleSize call. |
| `screenOrientation` (optional) | [ScreenOrientation](#type-screenorientation) | Screen orientation override. |
| `viewport` (optional) *(experimental)* | [Page.Viewport](Page.md#type-viewport) | If set, the visible area of the page will be overridden to this viewport. This viewport change is not observed by the page, e.g. viewport-relative elements do not change positions. |
| `displayFeature` (optional) *(experimental)* *(deprecated)* | [DisplayFeature](#type-displayfeature) | If set, the display feature of a multi-segment screen. If not set, multi-segment support is turned-off. Deprecated, use Emulation.setDisplayFeaturesOverride. |
| `devicePosture` (optional) *(experimental)* *(deprecated)* | [DevicePosture](#type-deviceposture) | If set, the posture of a foldable device. If not set the posture is set to continuous. Deprecated, use Emulation.setDevicePostureOverride. |
| `scrollbarType` (optional) *(experimental)* | enum: `overlay`, `default` | Scrollbar type. Default: `default`. |
| `screenOrientationLockEmulation` (optional) *(experimental)* | boolean | If set to true, enables screen orientation lock emulation, which intercepts screen.orientation.lock() calls from the page and reports orientation changes via screenOrientationLockChanged events. This is useful for emulating mobile device orientation lock behavior in responsive design mode. |
| `viewportMeta` (optional) *(experimental)* | enum: `enable`, `default` | Viewport meta tag behavior. Default: `default`. Note: if `mobile` is `true`, the viewport meta tag is always enabled. |
| `textLayoutMode` (optional) *(experimental)* | enum: `mobile`, `default` | Text layout mode. Default: `default`. Note: if `mobile` is `true`, mobile text layout mode (text autosizing) is always enabled. |

### Emulation.setDevicePostureOverride *(experimental)*

Start reporting the given posture value to the Device Posture API. This override can also be set in setDeviceMetricsOverride().

**Parameters**

| Name | Type | Description |
|---|---|---|
| `posture` | [DevicePosture](#type-deviceposture) |  |

### Emulation.clearDevicePostureOverride *(experimental)*

Clears a device posture override set with either setDeviceMetricsOverride() or setDevicePostureOverride() and starts using posture information from the platform again. Does nothing if no override is set.

### Emulation.setDisplayFeaturesOverride *(experimental)*

Start using the given display features to pupulate the Viewport Segments API. This override can also be set in setDeviceMetricsOverride().

**Parameters**

| Name | Type | Description |
|---|---|---|
| `features` | array of [DisplayFeature](#type-displayfeature) |  |

### Emulation.clearDisplayFeaturesOverride *(experimental)*

Clears the display features override set with either setDeviceMetricsOverride() or setDisplayFeaturesOverride() and starts using display features from the platform again. Does nothing if no override is set.

### Emulation.setScrollbarsHidden *(experimental)*

**Parameters**

| Name | Type | Description |
|---|---|---|
| `hidden` | boolean | Whether scrollbars should be always hidden. |

### Emulation.setDocumentCookieDisabled *(experimental)*

**Parameters**

| Name | Type | Description |
|---|---|---|
| `disabled` | boolean | Whether document.coookie API should be disabled. |

### Emulation.setEmitTouchEventsForMouse *(experimental)*

**Parameters**

| Name | Type | Description |
|---|---|---|
| `enabled` | boolean | Whether touch emulation based on mouse input should be enabled. |
| `configuration` (optional) | enum: `mobile`, `desktop` | Touch/gesture events configuration. Default: current platform. |

### Emulation.setEmulatedMedia

Emulates the given media type or media feature for CSS media queries.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `media` (optional) | string | Media type to emulate. Empty string disables the override. |
| `features` (optional) | array of [MediaFeature](#type-mediafeature) | Media features to emulate. |

### Emulation.setEmulatedVisionDeficiency

Emulates the given vision deficiency.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `type` | enum: `none`, `blurredVision`, `reducedContrast`, `achromatopsia`, `deuteranopia`, `protanopia`, `tritanopia` | Vision deficiency to emulate. Order: best-effort emulations come first, followed by any physiologically accurate emulations for medically recognized color vision deficiencies. |

### Emulation.setEmulatedOSTextScale

Emulates the given OS text scale.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `scale` (optional) | number |  |

### Emulation.setGeolocationOverride

Overrides the Geolocation Position or Error. Omitting latitude, longitude or accuracy emulates position unavailable.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `latitude` (optional) | number | Mock latitude |
| `longitude` (optional) | number | Mock longitude |
| `accuracy` (optional) | number | Mock accuracy |
| `altitude` (optional) | number | Mock altitude |
| `altitudeAccuracy` (optional) | number | Mock altitudeAccuracy |
| `heading` (optional) | number | Mock heading |
| `speed` (optional) | number | Mock speed |

### Emulation.getOverriddenSensorInformation *(experimental)*

**Parameters**

| Name | Type | Description |
|---|---|---|
| `type` | [SensorType](#type-sensortype) |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `requestedSamplingFrequency` | number |  |

### Emulation.setSensorOverrideEnabled *(experimental)*

Overrides a platform sensor of a given type. If |enabled| is true, calls to Sensor.start() will use a virtual sensor as backend rather than fetching data from a real hardware sensor. Otherwise, existing virtual sensor-backend Sensor objects will fire an error event and new calls to Sensor.start() will attempt to use a real sensor instead.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `enabled` | boolean |  |
| `type` | [SensorType](#type-sensortype) |  |
| `metadata` (optional) | [SensorMetadata](#type-sensormetadata) |  |

### Emulation.setSensorOverrideReadings *(experimental)*

Updates the sensor readings reported by a sensor type previously overridden by setSensorOverrideEnabled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `type` | [SensorType](#type-sensortype) |  |
| `reading` | [SensorReading](#type-sensorreading) |  |

### Emulation.setPressureSourceOverrideEnabled *(experimental)*

Overrides a pressure source of a given type, as used by the Compute Pressure API, so that updates to PressureObserver.observe() are provided via setPressureStateOverride instead of being retrieved from platform-provided telemetry data.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `enabled` | boolean |  |
| `source` | [PressureSource](#type-pressuresource) |  |
| `metadata` (optional) | [PressureMetadata](#type-pressuremetadata) |  |

### Emulation.setPressureStateOverride *(experimental)*

Provides a given pressure state that will be processed and eventually be delivered to PressureObserver users. |source| must have been previously overridden by setPressureSourceOverrideEnabled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `source` | [PressureSource](#type-pressuresource) |  |
| `state` | [PressureState](#type-pressurestate) |  |

### Emulation.setIdleOverride

Overrides the Idle state.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `isUserActive` | boolean | Mock isUserActive |
| `isScreenUnlocked` | boolean | Mock isScreenUnlocked |

### Emulation.clearIdleOverride

Clears Idle state overrides.

### Emulation.setNavigatorOverrides *(experimental)* *(deprecated)*

Overrides value returned by the javascript navigator object.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `platform` | string | The platform navigator.platform should return. |

### Emulation.setPageScaleFactor *(experimental)*

Sets a specified page scale factor.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `pageScaleFactor` | number | Page scale factor. |

### Emulation.setScriptExecutionDisabled

Switches script execution in the page.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `value` | boolean | Whether script execution should be disabled in the page. |

### Emulation.setTouchEmulationEnabled

Enables touch on platforms which do not support them.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `enabled` | boolean | Whether the touch event emulation should be enabled. |
| `maxTouchPoints` (optional) | integer | Maximum touch points supported. Defaults to one. |

### Emulation.setVirtualTimePolicy *(experimental)*

Turns on virtual time for all frames (replacing real-time with a synthetic time source) and sets the current virtual time policy.  Note this supersedes any previous time budget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `policy` | [VirtualTimePolicy](#type-virtualtimepolicy) |  |
| `budget` (optional) | number | If set, after this many virtual milliseconds have elapsed virtual time will be paused and a virtualTimeBudgetExpired event is sent. |
| `maxVirtualTimeTaskStarvationCount` (optional) | integer | If set this specifies the maximum number of tasks that can be run before virtual is forced forwards to prevent deadlock. |
| `initialVirtualTime` (optional) | [Network.TimeSinceEpoch](Network.md#type-timesinceepoch) | If set, base::Time::Now will be overridden to initially return this value. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `virtualTimeTicksBase` | number | Absolute timestamp at which virtual time was first enabled (up time in milliseconds). |

### Emulation.setLocaleOverride *(experimental)*

Overrides default host system locale with the specified one.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `locale` (optional) | string | ICU style C locale (e.g. "en_US"). If not specified or empty, disables the override and restores default host system locale. |

### Emulation.setTimezoneOverride

Overrides default host system timezone with the specified one.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `timezoneId` | string | The timezone identifier. List of supported timezones: https://source.chromium.org/chromium/chromium/deps/icu.git/+/faee8bc70570192d82d2978a71e2a615788597d1:source/data/misc/metaZones.txt If empty, disables the override and restores default host system timezone. |

### Emulation.setVisibleSize *(experimental)* *(deprecated)*

Resizes the frame/viewport of the page. Note that this does not affect the frame's container (e.g. browser window). Can be used to produce screenshots of the specified size. Not supported on Android.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `width` | integer | Frame width (DIP). |
| `height` | integer | Frame height (DIP). |

### Emulation.setDisabledImageTypes *(experimental)*

**Parameters**

| Name | Type | Description |
|---|---|---|
| `imageTypes` | array of [DisabledImageType](#type-disabledimagetype) | Image types to disable. |

### Emulation.setDataSaverOverride *(experimental)*

Override the value of navigator.connection.saveData

**Parameters**

| Name | Type | Description |
|---|---|---|
| `dataSaverEnabled` (optional) | boolean | Override value. Omitting the parameter disables the override. |

### Emulation.setHardwareConcurrencyOverride *(experimental)*

**Parameters**

| Name | Type | Description |
|---|---|---|
| `hardwareConcurrency` | integer | Hardware concurrency to report |

### Emulation.setCPUPerformanceOverride *(experimental)*

Overrides the value of navigator.cpuPerformance

**Parameters**

| Name | Type | Description |
|---|---|---|
| `performanceTier` (optional) | enum: `unknown`, `low`, `mid`, `high`, `ultra` | Override value. Omitting the parameter disables the override. |

### Emulation.setUserAgentOverride

Allows overriding user agent with the given string. `userAgentMetadata` must be set for Client Hint headers to be sent.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `userAgent` | string | User agent to use. |
| `acceptLanguage` (optional) | string | Browser language to emulate. |
| `platform` (optional) | string | The platform navigator.platform should return. |
| `userAgentMetadata` (optional) *(experimental)* | [UserAgentMetadata](#type-useragentmetadata) | To be sent in Sec-CH-UA-* headers and returned in navigator.userAgentData |

### Emulation.setAutomationOverride *(experimental)*

Allows overriding the automation flag.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `enabled` | boolean | Whether the override should be enabled. |

### Emulation.setSmallViewportHeightDifferenceOverride *(experimental)*

Allows overriding the difference between the small and large viewport sizes, which determine the value of the `svh` and `lvh` unit, respectively. Only supported for top-level frames.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `difference` | integer | This will cause an element of size 100svh to be `difference` pixels smaller than an element of size 100lvh. |

### Emulation.getScreenInfos *(experimental)*

Returns device's screen configuration. In headful mode, the physical screens configuration is returned, whereas in headless mode, a virtual headless screen configuration is provided instead.

**Returns**

| Name | Type | Description |
|---|---|---|
| `screenInfos` | array of [ScreenInfo](#type-screeninfo) |  |

### Emulation.addScreen *(experimental)*

Add a new screen to the device. Only supported in headless mode.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `left` | integer | Offset of the left edge of the screen in pixels. |
| `top` | integer | Offset of the top edge of the screen in pixels. |
| `width` | integer | The width of the screen in pixels. |
| `height` | integer | The height of the screen in pixels. |
| `workAreaInsets` (optional) | [WorkAreaInsets](#type-workareainsets) | Specifies the screen's work area. Default is entire screen. |
| `devicePixelRatio` (optional) | number | Specifies the screen's device pixel ratio. Default is 1. |
| `rotation` (optional) | integer | Specifies the screen's rotation angle. Available values are 0, 90, 180 and 270. Default is 0. |
| `colorDepth` (optional) | integer | Specifies the screen's color depth in bits. Default is 24. |
| `label` (optional) | string | Specifies the descriptive label for the screen. Default is none. |
| `isInternal` (optional) | boolean | Indicates whether the screen is internal to the device or external, attached to the device. Default is false. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `screenInfo` | [ScreenInfo](#type-screeninfo) |  |

### Emulation.updateScreen *(experimental)*

Updates specified screen parameters. Only supported in headless mode.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `screenId` | [ScreenId](#type-screenid) | Target screen identifier. |
| `left` (optional) | integer | Offset of the left edge of the screen in pixels. |
| `top` (optional) | integer | Offset of the top edge of the screen in pixels. |
| `width` (optional) | integer | The width of the screen in pixels. |
| `height` (optional) | integer | The height of the screen in pixels. |
| `workAreaInsets` (optional) | [WorkAreaInsets](#type-workareainsets) | Specifies the screen's work area. |
| `devicePixelRatio` (optional) | number | Specifies the screen's device pixel ratio. |
| `rotation` (optional) | integer | Specifies the screen's rotation angle. Available values are 0, 90, 180 and 270. |
| `colorDepth` (optional) | integer | Specifies the screen's color depth in bits. |
| `label` (optional) | string | Specifies the descriptive label for the screen. |
| `isInternal` (optional) | boolean | Indicates whether the screen is internal to the device or external, attached to the device. Default is false. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `screenInfo` | [ScreenInfo](#type-screeninfo) |  |

### Emulation.removeScreen *(experimental)*

Remove screen from the device. Only supported in headless mode.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `screenId` | [ScreenId](#type-screenid) |  |

### Emulation.setPrimaryScreen *(experimental)*

Set primary screen. Only supported in headless mode. Note that this changes the coordinate system origin to the top-left of the new primary screen, updating the bounds and work areas of all existing screens accordingly.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `screenId` | [ScreenId](#type-screenid) |  |

## Events

### Emulation.virtualTimeBudgetExpired *(experimental)*

Notification sent after the virtual time budget for the current VirtualTimePolicy has run out.

### Emulation.screenOrientationLockChanged *(experimental)*

Fired when a page calls screen.orientation.lock() or screen.orientation.unlock() while device emulation is enabled. This allows the DevTools frontend to update the emulated device orientation accordingly.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `locked` | boolean | Whether the screen orientation is currently locked. |
| `orientation` (optional) | [ScreenOrientation](#type-screenorientation) | The orientation lock type requested by the page. Only set when locked is true. |

## Types

<a id="type-safeareainsets"></a>
### Emulation.SafeAreaInsets *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `top` (optional) | integer | Overrides safe-area-inset-top. |
| `topMax` (optional) | integer | Overrides safe-area-max-inset-top. |
| `left` (optional) | integer | Overrides safe-area-inset-left. |
| `leftMax` (optional) | integer | Overrides safe-area-max-inset-left. |
| `bottom` (optional) | integer | Overrides safe-area-inset-bottom. |
| `bottomMax` (optional) | integer | Overrides safe-area-max-inset-bottom. |
| `right` (optional) | integer | Overrides safe-area-inset-right. |
| `rightMax` (optional) | integer | Overrides safe-area-max-inset-right. |

<a id="type-screenorientation"></a>
### Emulation.ScreenOrientation

Type: object

Screen orientation.

**Properties**

| Name | Type | Description |
|---|---|---|
| `type` | enum: `portraitPrimary`, `portraitSecondary`, `landscapePrimary`, `landscapeSecondary` | Orientation type. |
| `angle` | integer | Orientation angle. |

<a id="type-displayfeature"></a>
### Emulation.DisplayFeature

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `orientation` | enum: `vertical`, `horizontal` | Orientation of a display feature in relation to screen |
| `offset` | integer | The offset from the screen origin in either the x (for vertical orientation) or y (for horizontal orientation) direction. |
| `maskLength` | integer | A display feature may mask content such that it is not physically displayed - this length along with the offset describes this area. A display feature that only splits content will have a 0 mask_length. |

<a id="type-deviceposture"></a>
### Emulation.DevicePosture

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `type` | enum: `continuous`, `folded` | Current posture of the device |

<a id="type-mediafeature"></a>
### Emulation.MediaFeature

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string |  |
| `value` | string |  |

<a id="type-virtualtimepolicy"></a>
### Emulation.VirtualTimePolicy *(experimental)*

Type: string

advance: If the scheduler runs out of immediate work, the virtual time base may fast forward to allow the next delayed task (if any) to run; pause: The virtual time base may not advance; pauseIfNetworkFetchesPending: The virtual time base may not advance if there are any pending resource fetches.

Allowed values: `advance`, `pause`, `pauseIfNetworkFetchesPending`

<a id="type-useragentbrandversion"></a>
### Emulation.UserAgentBrandVersion *(experimental)*

Type: object

Used to specify User Agent Client Hints to emulate. See https://wicg.github.io/ua-client-hints

**Properties**

| Name | Type | Description |
|---|---|---|
| `brand` | string |  |
| `version` | string |  |

<a id="type-useragentmetadata"></a>
### Emulation.UserAgentMetadata *(experimental)*

Type: object

Used to specify User Agent Client Hints to emulate. See https://wicg.github.io/ua-client-hints Missing optional values will be filled in by the target with what it would normally use.

**Properties**

| Name | Type | Description |
|---|---|---|
| `brands` (optional) | array of [UserAgentBrandVersion](#type-useragentbrandversion) | Brands appearing in Sec-CH-UA. |
| `fullVersionList` (optional) | array of [UserAgentBrandVersion](#type-useragentbrandversion) | Brands appearing in Sec-CH-UA-Full-Version-List. |
| `fullVersion` (optional) *(deprecated)* | string |  |
| `platform` | string |  |
| `platformVersion` | string |  |
| `architecture` | string |  |
| `model` | string |  |
| `mobile` | boolean |  |
| `bitness` (optional) | string |  |
| `wow64` (optional) | boolean |  |
| `formFactors` (optional) | array of string | Used to specify User Agent form-factor values. See https://wicg.github.io/ua-client-hints/#sec-ch-ua-form-factors |

<a id="type-sensortype"></a>
### Emulation.SensorType *(experimental)*

Type: string

Used to specify sensor types to emulate. See https://w3c.github.io/sensors/#automation for more information.

Allowed values: `absolute-orientation`, `accelerometer`, `ambient-light`, `gravity`, `gyroscope`, `linear-acceleration`, `magnetometer`, `relative-orientation`

<a id="type-sensormetadata"></a>
### Emulation.SensorMetadata *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `available` (optional) | boolean |  |
| `minimumFrequency` (optional) | number |  |
| `maximumFrequency` (optional) | number |  |

<a id="type-sensorreadingsingle"></a>
### Emulation.SensorReadingSingle *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `value` | number |  |

<a id="type-sensorreadingxyz"></a>
### Emulation.SensorReadingXYZ *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `x` | number |  |
| `y` | number |  |
| `z` | number |  |

<a id="type-sensorreadingquaternion"></a>
### Emulation.SensorReadingQuaternion *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `x` | number |  |
| `y` | number |  |
| `z` | number |  |
| `w` | number |  |

<a id="type-sensorreading"></a>
### Emulation.SensorReading *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `single` (optional) | [SensorReadingSingle](#type-sensorreadingsingle) |  |
| `xyz` (optional) | [SensorReadingXYZ](#type-sensorreadingxyz) |  |
| `quaternion` (optional) | [SensorReadingQuaternion](#type-sensorreadingquaternion) |  |

<a id="type-pressuresource"></a>
### Emulation.PressureSource *(experimental)*

Type: string

Allowed values: `cpu`

<a id="type-pressurestate"></a>
### Emulation.PressureState *(experimental)*

Type: string

Allowed values: `nominal`, `fair`, `serious`, `critical`

<a id="type-pressuremetadata"></a>
### Emulation.PressureMetadata *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `available` (optional) | boolean |  |

<a id="type-workareainsets"></a>
### Emulation.WorkAreaInsets *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `top` (optional) | integer | Work area top inset in pixels. Default is 0; |
| `left` (optional) | integer | Work area left inset in pixels. Default is 0; |
| `bottom` (optional) | integer | Work area bottom inset in pixels. Default is 0; |
| `right` (optional) | integer | Work area right inset in pixels. Default is 0; |

<a id="type-screenid"></a>
### Emulation.ScreenId *(experimental)*

Type: string

<a id="type-screeninfo"></a>
### Emulation.ScreenInfo *(experimental)*

Type: object

Screen information similar to the one returned by window.getScreenDetails() method, see https://w3c.github.io/window-management/#screendetailed.

**Properties**

| Name | Type | Description |
|---|---|---|
| `left` | integer | Offset of the left edge of the screen. |
| `top` | integer | Offset of the top edge of the screen. |
| `width` | integer | Width of the screen. |
| `height` | integer | Height of the screen. |
| `availLeft` | integer | Offset of the left edge of the available screen area. |
| `availTop` | integer | Offset of the top edge of the available screen area. |
| `availWidth` | integer | Width of the available screen area. |
| `availHeight` | integer | Height of the available screen area. |
| `devicePixelRatio` | number | Specifies the screen's device pixel ratio. |
| `orientation` | [ScreenOrientation](#type-screenorientation) | Specifies the screen's orientation. |
| `colorDepth` | integer | Specifies the screen's color depth in bits. |
| `isExtended` | boolean | Indicates whether the device has multiple screens. |
| `isInternal` | boolean | Indicates whether the screen is internal to the device or external, attached to the device. |
| `isPrimary` | boolean | Indicates whether the screen is set as the the operating system primary screen. |
| `label` | string | Specifies the descriptive label for the screen. |
| `id` | [ScreenId](#type-screenid) | Specifies the unique identifier of the screen. |

<a id="type-disabledimagetype"></a>
### Emulation.DisabledImageType *(experimental)*

Type: string

Enum of image types that can be disabled.

Allowed values: `avif`, `jxl`, `webp`

