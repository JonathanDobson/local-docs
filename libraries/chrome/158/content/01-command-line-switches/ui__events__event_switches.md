# Command-line switches: `ui/events/event_switches`

Generated from `ui/events/event_switches.h` and `ui/events/event_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

7 switches.

## `--compensate-for-unstable-pinch-zoom`

- Constant: `kCompensateForUnstablePinchZoom`

Enable compensation for unstable pinch zoom. Some touch screens display significant amount of wobble when moving a finger in a straight line. This makes two finger scroll trigger an oscillating pinch zoom. See crbug.com/394380 for details.

## `--touch-slop-distance`

- Constant: `kTouchSlopDistance`

Overrides touch slop distance for gesture detection. The touch slop distance is the maximum distance from the starting point of a touch sequence that a gesture can travel before it can no longer be considered a tap. Scroll gestures can only begin after this distance has been travelled. The switch value is a floating point number that is interpreted as a distance in pixels.

## `--touch-devices`

- Constant: `kTouchDevices`
- Condition: `BUILDFLAG(IS_LINUX) || BUILDFLAG(IS_CHROMEOS)`

Tells chrome to interpret events from these devices as touch events. Only available with XInput 2 (i.e. X server 1.8 or above). The id's of the devices can be retrieved from 'xinput list'.

## `--pen-devices`

- Constant: `kPenDevices`
- Condition: `BUILDFLAG(IS_LINUX) || BUILDFLAG(IS_CHROMEOS)`

Tells chrome to interpret events from these devices as pen events. Only available with XInput 2 (i.e. X server 1.8 or above). The id's of the devices can be retrieved from 'xinput list'.

## `--edge-touch-filtering`

- Constant: `kEdgeTouchFiltering`
- Condition: `BUILDFLAG(IS_OZONE)`

Tells Chrome to do edge touch filtering. Useful for convertible tablet.

## `--disable-cancel-all-touches`

- Constant: `kDisableCancelAllTouches`
- Condition: `BUILDFLAG(IS_OZONE)`

Disable CancelAllTouches() function for the implementation on cancel single touches.

## `--enable-microphone-mute-switch-device`

- Constant: `kEnableMicrophoneMuteSwitchDeviceSwitch`
- Condition: `BUILDFLAG(IS_OZONE)`

Enables logic to detect microphone mute switch device state, which disables internal audio input when toggled.
