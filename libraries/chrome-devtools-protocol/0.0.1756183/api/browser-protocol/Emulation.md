# Emulation domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

This domain emulates different environments for the page.

Depends on: [DOM](DOM.md), [Page](Page.md), [Runtime](Runtime.md)

48 methods, 2 events, 21 types.

## Methods

### Emulation.canEmulate

**Deprecated**

Tells whether emulation is supported.

No parameters.

**Return object**

| Name | Type | Description |
|---|---|---|
| `result` | boolean | True if emulation is supported. |

### Emulation.clearDeviceMetricsOverride

Clears the overridden device metrics.

No parameters.

### Emulation.clearGeolocationOverride

Clears the overridden Geolocation Position and Error.

No parameters.

### Emulation.resetPageScaleFactor

**Experimental**

Requests that page scale factor is reset to initial values.

No parameters.

### Emulation.setFocusEmulationEnabled

**Experimental**

Enables or disables simulating a focused and active page.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `enabled` | boolean | Whether to enable to disable focus emulation. |

### Emulation.setAutoDarkModeOverride

**Experimental**

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

Sets or clears an override of the default background color of the frame. This override is used
if the content does not specify one.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `color` (optional) | [DOM.RGBA](DOM.md#type-rgba) | RGBA of the default background color. If not specified, any existing override will be cleared. |

### Emulation.setSafeAreaInsetsOverride

**Experimental**

Overrides the values for env(safe-area-inset-*) and env(safe-area-max-inset-*). Unset values will cause the
respective variables to be undefined, even if previously overridden.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `insets` | [Emulation.SafeAreaInsets](#type-safeareainsets) |  |

### Emulation.setDeviceMetricsOverride

Overrides the values of device screen dimensions (window.screen.width, window.screen.height,
window.innerWidth, window.innerHeight, and "device-width"/"device-height"-related CSS media
query results).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `width` | integer | Overriding width value in pixels (minimum 0, maximum 10000000). 0 disables the override. |
| `height` | integer | Overriding height value in pixels (minimum 0, maximum 10000000). 0 disables the override. |
| `deviceScaleFactor` | number | Overriding device scale factor value. 0 disables the override. |
| `mobile` | boolean | Whether to emulate mobile device. This includes viewport meta tag, overlay scrollbars, text autosizing and more. |
| `scale` (optional) | number | **Experimental** Scale to apply to resulting view image. |
| `screenWidth` (optional) | integer | **Experimental** Overriding screen width value in pixels (minimum 0, maximum 10000000). |
| `screenHeight` (optional) | integer | **Experimental** Overriding screen height value in pixels (minimum 0, maximum 10000000). |
| `positionX` (optional) | integer | **Experimental** Overriding view X position on screen in pixels (minimum 0, maximum 10000000). |
| `positionY` (optional) | integer | **Experimental** Overriding view Y position on screen in pixels (minimum 0, maximum 10000000). |
| `dontSetVisibleSize` (optional) | boolean | **Experimental** Do not set visible view size, rely upon explicit setVisibleSize call. |
| `screenOrientation` (optional) | [Emulation.ScreenOrientation](#type-screenorientation) | Screen orientation override. |
| `viewport` (optional) | [Page.Viewport](Page.md#type-viewport) | **Experimental** If set, the visible area of the page will be overridden to this viewport. This viewport change is not observed by the page, e.g. viewport-relative elements do not change positions. |
| `displayFeature` (optional) | [Emulation.DisplayFeature](#type-displayfeature) | **Experimental** · **Deprecated** If set, the display feature of a multi-segment screen. If not set, multi-segment support is turned-off. Deprecated, use Emulation.setDisplayFeaturesOverride. |
| `devicePosture` (optional) | [Emulation.DevicePosture](#type-deviceposture) | **Experimental** · **Deprecated** If set, the posture of a foldable device. If not set the posture is set to continuous. Deprecated, use Emulation.setDevicePostureOverride. |
| `scrollbarType` (optional) | string | **Experimental** Scrollbar type. Default: `default`. Allowed values: `overlay`, `default` |
| `screenOrientationLockEmulation` (optional) | boolean | **Experimental** If set to true, enables screen orientation lock emulation, which intercepts screen.orientation.lock() calls from the page and reports orientation changes via screenOrientationLockChanged events. This is useful for emulating mobile device orientation lock behavior in responsive design mode. |
| `viewportMeta` (optional) | string | **Experimental** Viewport meta tag behavior. Default: `default`. Note: if `mobile` is `true`, the viewport meta tag is always enabled. Allowed values: `enable`, `default` |
| `textLayoutMode` (optional) | string | **Experimental** Text layout mode. Default: `default`. Note: if `mobile` is `true`, mobile text layout mode (text autosizing) is always enabled. Allowed values: `mobile`, `default` |

### Emulation.setDevicePostureOverride

**Experimental**

Start reporting the given posture value to the Device Posture API.
This override can also be set in setDeviceMetricsOverride().

**Parameters**

| Name | Type | Description |
|---|---|---|
| `posture` | [Emulation.DevicePosture](#type-deviceposture) |  |

### Emulation.clearDevicePostureOverride

**Experimental**

Clears a device posture override set with either setDeviceMetricsOverride()
or setDevicePostureOverride() and starts using posture information from the
platform again.
Does nothing if no override is set.

No parameters.

### Emulation.setDisplayFeaturesOverride

**Experimental**

Start using the given display features to pupulate the Viewport Segments API.
This override can also be set in setDeviceMetricsOverride().

**Parameters**

| Name | Type | Description |
|---|---|---|
| `features` | array of [Emulation.DisplayFeature](#type-displayfeature) |  |

### Emulation.clearDisplayFeaturesOverride

**Experimental**

Clears the display features override set with either setDeviceMetricsOverride()
or setDisplayFeaturesOverride() and starts using display features from the
platform again.
Does nothing if no override is set.

No parameters.

### Emulation.setScrollbarsHidden

**Experimental**

**Parameters**

| Name | Type | Description |
|---|---|---|
| `hidden` | boolean | Whether scrollbars should be always hidden. |

### Emulation.setDocumentCookieDisabled

**Experimental**

**Parameters**

| Name | Type | Description |
|---|---|---|
| `disabled` | boolean | Whether document.coookie API should be disabled. |

### Emulation.setEmitTouchEventsForMouse

**Experimental**

**Parameters**

| Name | Type | Description |
|---|---|---|
| `enabled` | boolean | Whether touch emulation based on mouse input should be enabled. |
| `configuration` (optional) | string | Touch/gesture events configuration. Default: current platform. Allowed values: `mobile`, `desktop` |

### Emulation.setEmulatedMedia

Emulates the given media type or media feature for CSS media queries.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `media` (optional) | string | Media type to emulate. Empty string disables the override. |
| `features` (optional) | array of [Emulation.MediaFeature](#type-mediafeature) | Media features to emulate. |

### Emulation.setEmulatedVisionDeficiency

Emulates the given vision deficiency.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `type` | string | Vision deficiency to emulate. Order: best-effort emulations come first, followed by any physiologically accurate emulations for medically recognized color vision deficiencies. Allowed values: `none`, `blurredVision`, `reducedContrast`, `achromatopsia`, `deuteranopia`, `protanopia`, `tritanopia` |

### Emulation.setEmulatedOSTextScale

Emulates the given OS text scale.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `scale` (optional) | number |  |

### Emulation.setGeolocationOverride

Overrides the Geolocation Position or Error. Omitting latitude, longitude or
accuracy emulates position unavailable.

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

### Emulation.getOverriddenSensorInformation

**Experimental**

**Parameters**

| Name | Type | Description |
|---|---|---|
| `type` | [Emulation.SensorType](#type-sensortype) |  |

**Return object**

| Name | Type | Description |
|---|---|---|
| `requestedSamplingFrequency` | number |  |

### Emulation.setSensorOverrideEnabled

**Experimental**

Overrides a platform sensor of a given type. If |enabled| is true, calls to
Sensor.start() will use a virtual sensor as backend rather than fetching
data from a real hardware sensor. Otherwise, existing virtual
sensor-backend Sensor objects will fire an error event and new calls to
Sensor.start() will attempt to use a real sensor instead.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `enabled` | boolean |  |
| `type` | [Emulation.SensorType](#type-sensortype) |  |
| `metadata` (optional) | [Emulation.SensorMetadata](#type-sensormetadata) |  |

### Emulation.setSensorOverrideReadings

**Experimental**

Updates the sensor readings reported by a sensor type previously overridden
by setSensorOverrideEnabled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `type` | [Emulation.SensorType](#type-sensortype) |  |
| `reading` | [Emulation.SensorReading](#type-sensorreading) |  |

### Emulation.setPressureSourceOverrideEnabled

**Experimental**

Overrides a pressure source of a given type, as used by the Compute
Pressure API, so that updates to PressureObserver.observe() are provided
via setPressureStateOverride instead of being retrieved from
platform-provided telemetry data.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `enabled` | boolean |  |
| `source` | [Emulation.PressureSource](#type-pressuresource) |  |
| `metadata` (optional) | [Emulation.PressureMetadata](#type-pressuremetadata) |  |

### Emulation.setPressureStateOverride

**Experimental**

Provides a given pressure state that will be processed and eventually be
delivered to PressureObserver users. |source| must have been previously
overridden by setPressureSourceOverrideEnabled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `source` | [Emulation.PressureSource](#type-pressuresource) |  |
| `state` | [Emulation.PressureState](#type-pressurestate) |  |

### Emulation.setIdleOverride

Overrides the Idle state.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `isUserActive` | boolean | Mock isUserActive |
| `isScreenUnlocked` | boolean | Mock isScreenUnlocked |

### Emulation.clearIdleOverride

Clears Idle state overrides.

No parameters.

### Emulation.setNavigatorOverrides

**Experimental** · **Deprecated**

Overrides value returned by the javascript navigator object.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `platform` | string | The platform navigator.platform should return. |

### Emulation.setPageScaleFactor

**Experimental**

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

### Emulation.setVirtualTimePolicy

**Experimental**

Turns on virtual time for all frames (replacing real-time with a synthetic time source) and sets
the current virtual time policy.  Note this supersedes any previous time budget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `policy` | [Emulation.VirtualTimePolicy](#type-virtualtimepolicy) |  |
| `budget` (optional) | number | If set, after this many virtual milliseconds have elapsed virtual time will be paused and a virtualTimeBudgetExpired event is sent. |
| `maxVirtualTimeTaskStarvationCount` (optional) | integer | If set this specifies the maximum number of tasks that can be run before virtual is forced forwards to prevent deadlock. |
| `initialVirtualTime` (optional) | [Network.TimeSinceEpoch](Network.md#type-timesinceepoch) | If set, base::Time::Now will be overridden to initially return this value. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `virtualTimeTicksBase` | number | Absolute timestamp at which virtual time was first enabled (up time in milliseconds). |

### Emulation.setLocaleOverride

**Experimental**

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

### Emulation.setVisibleSize

**Experimental** · **Deprecated**

Resizes the frame/viewport of the page. Note that this does not affect the frame's container
(e.g. browser window). Can be used to produce screenshots of the specified size. Not supported
on Android.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `width` | integer | Frame width (DIP). |
| `height` | integer | Frame height (DIP). |

### Emulation.setDisabledImageTypes

**Experimental**

**Parameters**

| Name | Type | Description |
|---|---|---|
| `imageTypes` | array of [Emulation.DisabledImageType](#type-disabledimagetype) | Image types to disable. |

### Emulation.setDataSaverOverride

**Experimental**

Override the value of navigator.connection.saveData

**Parameters**

| Name | Type | Description |
|---|---|---|
| `dataSaverEnabled` (optional) | boolean | Override value. Omitting the parameter disables the override. |

### Emulation.setHardwareConcurrencyOverride

**Experimental**

**Parameters**

| Name | Type | Description |
|---|---|---|
| `hardwareConcurrency` | integer | Hardware concurrency to report |

### Emulation.setCPUPerformanceOverride

**Experimental**

Overrides the value of navigator.cpuPerformance

**Parameters**

| Name | Type | Description |
|---|---|---|
| `performanceTier` (optional) | string | Override value. Omitting the parameter disables the override. Allowed values: `unknown`, `low`, `mid`, `high`, `ultra` |

### Emulation.setUserAgentOverride

Allows overriding user agent with the given string.
`userAgentMetadata` must be set for Client Hint headers to be sent.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `userAgent` | string | User agent to use. |
| `acceptLanguage` (optional) | string | Browser language to emulate. |
| `platform` (optional) | string | The platform navigator.platform should return. |
| `userAgentMetadata` (optional) | [Emulation.UserAgentMetadata](#type-useragentmetadata) | **Experimental** To be sent in Sec-CH-UA-* headers and returned in navigator.userAgentData |

### Emulation.setAutomationOverride

**Experimental**

Allows overriding the automation flag.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `enabled` | boolean | Whether the override should be enabled. |

### Emulation.setSmallViewportHeightDifferenceOverride

**Experimental**

Allows overriding the difference between the small and large viewport sizes, which determine the
value of the `svh` and `lvh` unit, respectively. Only supported for top-level frames.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `difference` | integer | This will cause an element of size 100svh to be `difference` pixels smaller than an element of size 100lvh. |

### Emulation.getScreenInfos

**Experimental**

Returns device's screen configuration. In headful mode, the physical screens configuration is returned,
whereas in headless mode, a virtual headless screen configuration is provided instead.

No parameters.

**Return object**

| Name | Type | Description |
|---|---|---|
| `screenInfos` | array of [Emulation.ScreenInfo](#type-screeninfo) |  |

### Emulation.addScreen

**Experimental**

Add a new screen to the device. Only supported in headless mode.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `left` | integer | Offset of the left edge of the screen in pixels. |
| `top` | integer | Offset of the top edge of the screen in pixels. |
| `width` | integer | The width of the screen in pixels. |
| `height` | integer | The height of the screen in pixels. |
| `workAreaInsets` (optional) | [Emulation.WorkAreaInsets](#type-workareainsets) | Specifies the screen's work area. Default is entire screen. |
| `devicePixelRatio` (optional) | number | Specifies the screen's device pixel ratio. Default is 1. |
| `rotation` (optional) | integer | Specifies the screen's rotation angle. Available values are 0, 90, 180 and 270. Default is 0. |
| `colorDepth` (optional) | integer | Specifies the screen's color depth in bits. Default is 24. |
| `label` (optional) | string | Specifies the descriptive label for the screen. Default is none. |
| `isInternal` (optional) | boolean | Indicates whether the screen is internal to the device or external, attached to the device. Default is false. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `screenInfo` | [Emulation.ScreenInfo](#type-screeninfo) |  |

### Emulation.updateScreen

**Experimental**

Updates specified screen parameters. Only supported in headless mode.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `screenId` | [Emulation.ScreenId](#type-screenid) | Target screen identifier. |
| `left` (optional) | integer | Offset of the left edge of the screen in pixels. |
| `top` (optional) | integer | Offset of the top edge of the screen in pixels. |
| `width` (optional) | integer | The width of the screen in pixels. |
| `height` (optional) | integer | The height of the screen in pixels. |
| `workAreaInsets` (optional) | [Emulation.WorkAreaInsets](#type-workareainsets) | Specifies the screen's work area. |
| `devicePixelRatio` (optional) | number | Specifies the screen's device pixel ratio. |
| `rotation` (optional) | integer | Specifies the screen's rotation angle. Available values are 0, 90, 180 and 270. |
| `colorDepth` (optional) | integer | Specifies the screen's color depth in bits. |
| `label` (optional) | string | Specifies the descriptive label for the screen. |
| `isInternal` (optional) | boolean | Indicates whether the screen is internal to the device or external, attached to the device. Default is false. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `screenInfo` | [Emulation.ScreenInfo](#type-screeninfo) |  |

### Emulation.removeScreen

**Experimental**

Remove screen from the device. Only supported in headless mode.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `screenId` | [Emulation.ScreenId](#type-screenid) |  |

### Emulation.setPrimaryScreen

**Experimental**

Set primary screen. Only supported in headless mode.
Note that this changes the coordinate system origin to the top-left
of the new primary screen, updating the bounds and work areas
of all existing screens accordingly.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `screenId` | [Emulation.ScreenId](#type-screenid) |  |

## Events

### Emulation.virtualTimeBudgetExpired

**Experimental**

Notification sent after the virtual time budget for the current VirtualTimePolicy has run out.

### Emulation.screenOrientationLockChanged

**Experimental**

Fired when a page calls screen.orientation.lock() or screen.orientation.unlock()
while device emulation is enabled. This allows the DevTools frontend to update the
emulated device orientation accordingly.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `locked` | boolean | Whether the screen orientation is currently locked. |
| `orientation` (optional) | [Emulation.ScreenOrientation](#type-screenorientation) | The orientation lock type requested by the page. Only set when locked is true. |

## Types

<a id="type-safeareainsets"></a>
### Emulation.SafeAreaInsets

**Experimental**

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

Screen orientation.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `type` | string | Orientation type. Allowed values: `portraitPrimary`, `portraitSecondary`, `landscapePrimary`, `landscapeSecondary` |
| `angle` | integer | Orientation angle. |

<a id="type-displayfeature"></a>
### Emulation.DisplayFeature

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `orientation` | string | Orientation of a display feature in relation to screen Allowed values: `vertical`, `horizontal` |
| `offset` | integer | The offset from the screen origin in either the x (for vertical orientation) or y (for horizontal orientation) direction. |
| `maskLength` | integer | A display feature may mask content such that it is not physically displayed - this length along with the offset describes this area. A display feature that only splits content will have a 0 mask_length. |

<a id="type-deviceposture"></a>
### Emulation.DevicePosture

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `type` | string | Current posture of the device Allowed values: `continuous`, `folded` |

<a id="type-mediafeature"></a>
### Emulation.MediaFeature

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string |  |
| `value` | string |  |

<a id="type-virtualtimepolicy"></a>
### Emulation.VirtualTimePolicy

**Experimental**

advance: If the scheduler runs out of immediate work, the virtual time base may fast forward to
allow the next delayed task (if any) to run; pause: The virtual time base may not advance;
pauseIfNetworkFetchesPending: The virtual time base may not advance if there are any pending
resource fetches.

Type: string

Allowed values: `advance`, `pause`, `pauseIfNetworkFetchesPending`

<a id="type-useragentbrandversion"></a>
### Emulation.UserAgentBrandVersion

**Experimental**

Used to specify User Agent Client Hints to emulate. See https://wicg.github.io/ua-client-hints

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `brand` | string |  |
| `version` | string |  |

<a id="type-useragentmetadata"></a>
### Emulation.UserAgentMetadata

**Experimental**

Used to specify User Agent Client Hints to emulate. See https://wicg.github.io/ua-client-hints
Missing optional values will be filled in by the target with what it would normally use.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `brands` (optional) | array of [Emulation.UserAgentBrandVersion](#type-useragentbrandversion) | Brands appearing in Sec-CH-UA. |
| `fullVersionList` (optional) | array of [Emulation.UserAgentBrandVersion](#type-useragentbrandversion) | Brands appearing in Sec-CH-UA-Full-Version-List. |
| `fullVersion` (optional) | string | **Deprecated** |
| `platform` | string |  |
| `platformVersion` | string |  |
| `architecture` | string |  |
| `model` | string |  |
| `mobile` | boolean |  |
| `bitness` (optional) | string |  |
| `wow64` (optional) | boolean |  |
| `formFactors` (optional) | array of string | Used to specify User Agent form-factor values. See https://wicg.github.io/ua-client-hints/#sec-ch-ua-form-factors |

<a id="type-sensortype"></a>
### Emulation.SensorType

**Experimental**

Used to specify sensor types to emulate.
See https://w3c.github.io/sensors/#automation for more information.

Type: string

Allowed values: `absolute-orientation`, `accelerometer`, `ambient-light`, `gravity`, `gyroscope`, `linear-acceleration`, `magnetometer`, `relative-orientation`

<a id="type-sensormetadata"></a>
### Emulation.SensorMetadata

**Experimental**

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `available` (optional) | boolean |  |
| `minimumFrequency` (optional) | number |  |
| `maximumFrequency` (optional) | number |  |

<a id="type-sensorreadingsingle"></a>
### Emulation.SensorReadingSingle

**Experimental**

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `value` | number |  |

<a id="type-sensorreadingxyz"></a>
### Emulation.SensorReadingXYZ

**Experimental**

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `x` | number |  |
| `y` | number |  |
| `z` | number |  |

<a id="type-sensorreadingquaternion"></a>
### Emulation.SensorReadingQuaternion

**Experimental**

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `x` | number |  |
| `y` | number |  |
| `z` | number |  |
| `w` | number |  |

<a id="type-sensorreading"></a>
### Emulation.SensorReading

**Experimental**

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `single` (optional) | [Emulation.SensorReadingSingle](#type-sensorreadingsingle) |  |
| `xyz` (optional) | [Emulation.SensorReadingXYZ](#type-sensorreadingxyz) |  |
| `quaternion` (optional) | [Emulation.SensorReadingQuaternion](#type-sensorreadingquaternion) |  |

<a id="type-pressuresource"></a>
### Emulation.PressureSource

**Experimental**

Type: string

Allowed values: `cpu`

<a id="type-pressurestate"></a>
### Emulation.PressureState

**Experimental**

Type: string

Allowed values: `nominal`, `fair`, `serious`, `critical`

<a id="type-pressuremetadata"></a>
### Emulation.PressureMetadata

**Experimental**

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `available` (optional) | boolean |  |

<a id="type-workareainsets"></a>
### Emulation.WorkAreaInsets

**Experimental**

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `top` (optional) | integer | Work area top inset in pixels. Default is 0; |
| `left` (optional) | integer | Work area left inset in pixels. Default is 0; |
| `bottom` (optional) | integer | Work area bottom inset in pixels. Default is 0; |
| `right` (optional) | integer | Work area right inset in pixels. Default is 0; |

<a id="type-screenid"></a>
### Emulation.ScreenId

**Experimental**

Type: string

<a id="type-screeninfo"></a>
### Emulation.ScreenInfo

**Experimental**

Screen information similar to the one returned by window.getScreenDetails() method,
see https://w3c.github.io/window-management/#screendetailed.

Type: object

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
| `orientation` | [Emulation.ScreenOrientation](#type-screenorientation) | Specifies the screen's orientation. |
| `colorDepth` | integer | Specifies the screen's color depth in bits. |
| `isExtended` | boolean | Indicates whether the device has multiple screens. |
| `isInternal` | boolean | Indicates whether the screen is internal to the device or external, attached to the device. |
| `isPrimary` | boolean | Indicates whether the screen is set as the the operating system primary screen. |
| `label` | string | Specifies the descriptive label for the screen. |
| `id` | [Emulation.ScreenId](#type-screenid) | Specifies the unique identifier of the screen. |

<a id="type-disabledimagetype"></a>
### Emulation.DisabledImageType

**Experimental**

Enum of image types that can be disabled.

Type: string

Allowed values: `avif`, `jxl`, `webp`
