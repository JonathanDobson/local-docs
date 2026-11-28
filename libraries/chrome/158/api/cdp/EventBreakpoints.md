# EventBreakpoints domain *(experimental)*

Copyright 2017 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.  Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp EventBreakpoints permits setting JavaScript breakpoints on operations and events occurring in native code invoked from JavaScript. Once breakpoint is hit, it is reported through Debugger domain, similarly to regular breakpoints being hit.

Methods are called as `EventBreakpoints.<command>` and events arrive as `EventBreakpoints.<event>`.

## Commands

### EventBreakpoints.setInstrumentationBreakpoint

Sets breakpoint on particular native event.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `eventName` | string | Instrumentation name to stop on. |

### EventBreakpoints.removeInstrumentationBreakpoint

Removes breakpoint on particular native event.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `eventName` | string | Instrumentation name to stop on. |

### EventBreakpoints.disable

Removes all breakpoints

