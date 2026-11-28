# DOMDebugger domain

Copyright 2017 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.  Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp DOM debugging allows setting breakpoints on particular DOM operations and events. JavaScript execution will stop on these operations as if there was a regular breakpoint set.

Depends on: [DOM](DOM.md), [Runtime](Runtime.md)

Methods are called as `DOMDebugger.<command>` and events arrive as `DOMDebugger.<event>`.

## Commands

### DOMDebugger.getEventListeners

Returns event listeners of the given object.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `objectId` | [Runtime.RemoteObjectId](Runtime.md#type-remoteobjectid) | Identifier of the object to return listeners for. |
| `depth` (optional) | integer | The maximum depth at which Node children should be retrieved, defaults to 1. Use -1 for the entire subtree or provide an integer larger than 0. |
| `pierce` (optional) | boolean | Whether or not iframes and shadow roots should be traversed when returning the subtree (default is false). Reports listeners for all contexts if pierce is enabled. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `listeners` | array of [EventListener](#type-eventlistener) | Array of relevant listeners. |

### DOMDebugger.removeDOMBreakpoint

Removes DOM breakpoint that was set using `setDOMBreakpoint`.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [DOM.NodeId](DOM.md#type-nodeid) | Identifier of the node to remove breakpoint from. |
| `type` | [DOMBreakpointType](#type-dombreakpointtype) | Type of the breakpoint to remove. |

### DOMDebugger.removeEventListenerBreakpoint

Removes breakpoint on particular DOM event.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `eventName` | string | Event name. |
| `targetName` (optional) *(experimental)* | string | EventTarget interface name. |

### DOMDebugger.removeInstrumentationBreakpoint *(experimental)* *(deprecated)*

Removes breakpoint on particular native event.

Redirects to `EventBreakpoints`.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `eventName` | string | Instrumentation name to stop on. |

### DOMDebugger.removeXHRBreakpoint

Removes breakpoint from XMLHttpRequest.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `url` | string | Resource URL substring. |

### DOMDebugger.setBreakOnCSPViolation *(experimental)*

Sets breakpoint on particular CSP violations.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `violationTypes` | array of [CSPViolationType](#type-cspviolationtype) | CSP Violations to stop upon. |

### DOMDebugger.setDOMBreakpoint

Sets breakpoint on particular operation with DOM.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [DOM.NodeId](DOM.md#type-nodeid) | Identifier of the node to set breakpoint on. |
| `type` | [DOMBreakpointType](#type-dombreakpointtype) | Type of the operation to stop upon. |

### DOMDebugger.setEventListenerBreakpoint

Sets breakpoint on particular DOM event.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `eventName` | string | DOM Event name to stop on (any DOM event will do). |
| `targetName` (optional) *(experimental)* | string | EventTarget interface name to stop on. If equal to `"*"` or not provided, will stop on any EventTarget. |

### DOMDebugger.setInstrumentationBreakpoint *(experimental)* *(deprecated)*

Sets breakpoint on particular native event.

Redirects to `EventBreakpoints`.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `eventName` | string | Instrumentation name to stop on. |

### DOMDebugger.setXHRBreakpoint

Sets breakpoint on XMLHttpRequest.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `url` | string | Resource URL substring. All XHRs having this substring in the URL will get stopped upon. |

## Types

<a id="type-dombreakpointtype"></a>
### DOMDebugger.DOMBreakpointType

Type: string

DOM breakpoint type.

Allowed values: `subtree-modified`, `attribute-modified`, `node-removed`

<a id="type-cspviolationtype"></a>
### DOMDebugger.CSPViolationType *(experimental)*

Type: string

CSP Violation type.

Allowed values: `trustedtype-sink-violation`, `trustedtype-policy-violation`

<a id="type-eventlistener"></a>
### DOMDebugger.EventListener

Type: object

Object event listener.

**Properties**

| Name | Type | Description |
|---|---|---|
| `type` | string | `EventListener`'s type. |
| `useCapture` | boolean | `EventListener`'s useCapture. |
| `passive` | boolean | `EventListener`'s passive flag. |
| `once` | boolean | `EventListener`'s once flag. |
| `scriptId` | [Runtime.ScriptId](Runtime.md#type-scriptid) | Script id of the handler code. |
| `lineNumber` | integer | Line number in the script (0-based). |
| `columnNumber` | integer | Column number in the script (0-based). |
| `handler` (optional) | [Runtime.RemoteObject](Runtime.md#type-remoteobject) | Event handler function value. |
| `originalHandler` (optional) | [Runtime.RemoteObject](Runtime.md#type-remoteobject) | Event original handler function value. |
| `backendNodeId` (optional) | [DOM.BackendNodeId](DOM.md#type-backendnodeid) | Node the listener is added to (if any). |

