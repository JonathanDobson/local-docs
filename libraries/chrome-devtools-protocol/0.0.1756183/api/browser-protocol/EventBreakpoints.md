# EventBreakpoints domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

**Experimental**

EventBreakpoints permits setting JavaScript breakpoints on operations and events
occurring in native code invoked from JavaScript. Once breakpoint is hit, it is
reported through Debugger domain, similarly to regular breakpoints being hit.

3 methods, 0 events, 0 types.

## Methods

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

No parameters.
