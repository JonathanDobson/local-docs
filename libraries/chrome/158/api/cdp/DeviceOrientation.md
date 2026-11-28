# DeviceOrientation domain *(experimental)*

Copyright 2017 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.  Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp

Methods are called as `DeviceOrientation.<command>` and events arrive as `DeviceOrientation.<event>`.

## Commands

### DeviceOrientation.clearDeviceOrientationOverride

Clears the overridden Device Orientation.

### DeviceOrientation.setDeviceOrientationOverride

Overrides the Device Orientation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `alpha` | number | Mock alpha |
| `beta` | number | Mock beta |
| `gamma` | number | Mock gamma |

