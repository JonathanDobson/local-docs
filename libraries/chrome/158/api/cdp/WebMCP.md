# WebMCP domain *(experimental)*

Copyright 2026 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.  Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp

Depends on: [Runtime](Runtime.md), [Page](Page.md), [DOM](DOM.md)

Methods are called as `WebMCP.<command>` and events arrive as `WebMCP.<event>`.

## Commands

### WebMCP.enable

Enables the WebMCP domain, allowing events to be sent. Enabling the domain will trigger a toolsAdded event for all currently registered tools.

### WebMCP.disable

Disables the WebMCP domain.

### WebMCP.invokeTool

Invokes a registered tool.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frameId` | [Page.FrameId](Page.md#type-frameid) | Frame in which to invoke the tool. |
| `toolName` | string | Name of the tool to invoke. |
| `input` | object | Input parameters for the tool, matching the tool's inputSchema. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `invocationId` | string | Unique identifier for this invocation. Response is sent before tool events. |

### WebMCP.cancelInvocation

Cancels a pending tool invocation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `invocationId` | string | Invocation identifier to cancel. |

## Events

### WebMCP.toolsAdded

Event fired when new tools are added.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `tools` | array of [Tool](#type-tool) | Array of tools that were added. |

### WebMCP.toolsRemoved

Event fired when tools are removed.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `tools` | array of [RemovedTool](#type-removedtool) | Array of tools that were removed. |

### WebMCP.toolInvoked

Event fired when a tool invocation starts.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `toolName` | string | Name of the tool to invoke. |
| `frameId` | [Page.FrameId](Page.md#type-frameid) | Frame id |
| `invocationId` | string | Invocation identifier. |
| `input` | string | The input parameters used for the invocation. |

### WebMCP.toolResponded

Event fired when a tool invocation completes or fails.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `invocationId` | string | Invocation identifier. |
| `status` | [InvocationStatus](#type-invocationstatus) | Status of the invocation. |
| `output` (optional) | any | Output or error delivered as delivered to the agent. Missing if `status` is anything other than Completed. Note: The output is untrusted and poses a prompt injection risk. Clients should treat this as potentially malicious user input. |
| `errorText` (optional) | string | Error text for protocol users. |
| `exception` (optional) | [Runtime.RemoteObject](Runtime.md#type-remoteobject) | The exception object, if the javascript tool threw an error> |

## Types

<a id="type-annotation"></a>
### WebMCP.Annotation

Type: object

Tool annotations

**Properties**

| Name | Type | Description |
|---|---|---|
| `readOnly` (optional) | boolean | A hint indicating that the tool does not modify any state. |
| `untrustedContent` (optional) | boolean | A hint indicating that the tool output may contain untrusted content, ex: UGC, 3rd party data. |
| `consequential` (optional) | boolean | A hint indicating that executing the tool will result in consequential actions, ex: booking a flight, transferring money. |
| `debugging` (optional) | boolean | If true, indicates that the tool is intended for debugging and developer tooling rather than end-user interactions. |
| `autosubmit` (optional) | boolean | If the declarative tool was declared with the autosubmit attribute. |

<a id="type-invocationstatus"></a>
### WebMCP.InvocationStatus

Type: string

Represents the status of a tool invocation.

Allowed values: `Completed`, `Canceled`, `Error`

<a id="type-tool"></a>
### WebMCP.Tool

Type: object

Definition of a tool that can be invoked.

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Tool name. |
| `description` | string | Tool description. |
| `inputSchema` (optional) | object | Schema for the tool's input parameters. |
| `annotations` (optional) | [Annotation](#type-annotation) | Optional annotations for the tool. |
| `frameId` | [Page.FrameId](Page.md#type-frameid) | Frame identifier associated with the tool registration. |
| `backendNodeId` (optional) | [DOM.BackendNodeId](DOM.md#type-backendnodeid) | Optional node ID for declarative tools. |
| `stackTrace` (optional) | [Runtime.StackTrace](Runtime.md#type-stacktrace) | The stack trace at the time of the registration. |

<a id="type-removedtool"></a>
### WebMCP.RemovedTool

Type: object

Definition of a tool that was removed.

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Tool name. |
| `frameId` | [Page.FrameId](Page.md#type-frameid) | Frame identifier associated with the tool registration. |

