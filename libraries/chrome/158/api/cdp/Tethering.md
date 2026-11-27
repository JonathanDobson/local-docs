# Tethering domain *(experimental)*

Copyright 2017 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.  Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp The Tethering domain defines methods and events for browser port binding.

Methods are called as `Tethering.<command>` and events arrive as `Tethering.<event>`.

## Commands

### Tethering.bind

Request browser port binding.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `port` | integer | Port number to bind. |

### Tethering.unbind

Request browser port unbinding.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `port` | integer | Port number to unbind. |

## Events

### Tethering.accepted

Informs that port was successfully bound and got a specified connection id.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `port` | integer | Port number that was successfully bound. |
| `connectionId` | string | Connection id to be used. |

