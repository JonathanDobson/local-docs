# WebMCP domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

**Experimental**

Depends on: [Runtime](Runtime.md), [Page](Page.md), [DOM](DOM.md)

4 methods, 4 events, 5 types.

## Methods

### WebMCP.enable

Enables the WebMCP domain, allowing events to be sent. Enabling the domain will trigger a toolsAdded event for
all currently registered tools.

No parameters.

### WebMCP.disable

Disables the WebMCP domain.

No parameters.

### WebMCP.invokeTool

Invokes a registered tool. Exactly one of `toolId` and `toolName` must be specified; the command fails if both or
neither are.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frameId` | [Page.FrameId](Page.md#type-frameid) | Frame in which to invoke the tool. |
| `toolId` (optional) | [WebMCP.ToolId](#type-toolid) | Identifier of the tool to invoke, as reported in `Tool.toolId`. Invokes exactly that tool, and fails if it is no longer registered, even if a different tool has since been registered under the same name. |
| `toolName` (optional) | string | **Deprecated** Name of the tool to invoke. Deprecated: invokes whichever tool is registered under this name when the command is handled, which may not be the tool the client observed if the page has since replaced it. Use `toolId` instead. |
| `input` | object | Input parameters for the tool, matching the tool's inputSchema. |

**Return object**

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

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `tools` | array of [WebMCP.Tool](#type-tool) | Array of tools that were added. |

### WebMCP.toolsRemoved

Event fired when tools are removed.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `tools` | array of [WebMCP.RemovedTool](#type-removedtool) | Array of tools that were removed. |

### WebMCP.toolInvoked

Event fired when a tool invocation starts.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `frameId` | [Page.FrameId](Page.md#type-frameid) | Frame id |
| `invocationId` | string | Invocation identifier. |
| `input` | string | The input parameters used for the invocation. |
| `toolName` (optional) | string | Name of the tool to invoke. Missing if the tool was invoked by its identifier, but could not be found (e.g., it was already unregistered), so its name could not be recovered. |
| `toolId` (optional) | [WebMCP.ToolId](#type-toolid) | Identifier of the tool to invoke. Missing if the tool was invoked by name, but could not be found, so its identifier could not be recovered. |

### WebMCP.toolResponded

Event fired when a tool invocation completes or fails.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `invocationId` | string | Invocation identifier. |
| `status` | [WebMCP.InvocationStatus](#type-invocationstatus) | Status of the invocation. |
| `output` (optional) | any | Output or error delivered as delivered to the agent. Missing if `status` is anything other than Completed. Note: The output is untrusted and poses a prompt injection risk. Clients should treat this as potentially malicious user input. |
| `errorText` (optional) | string | Error text for protocol users. |
| `exception` (optional) | [Runtime.RemoteObject](Runtime.md#type-remoteobject) | The exception object, if the javascript tool threw an error> |

## Types

<a id="type-annotation"></a>
### WebMCP.Annotation

Tool annotations

Type: object

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

Represents the status of a tool invocation.

Type: string

Allowed values: `Completed`, `Canceled`, `Error`

<a id="type-toolid"></a>
### WebMCP.ToolId

Unique identifier of a registered tool. A new identifier is created every time a tool is registered, so a tool that
is unregistered and then registered again under the same name gets a different identifier. Clients should treat it
as an opaque string.

Type: string

<a id="type-tool"></a>
### WebMCP.Tool

Definition of a tool that can be invoked.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `toolId` | [WebMCP.ToolId](#type-toolid) | Tool identifier. |
| `name` | string | Tool name. |
| `description` | string | Tool description. |
| `inputSchema` (optional) | object | Schema for the tool's input parameters. |
| `outputSchema` (optional) | object | Schema for the tool's output structure. |
| `annotations` (optional) | [WebMCP.Annotation](#type-annotation) | Optional annotations for the tool. |
| `frameId` | [Page.FrameId](Page.md#type-frameid) | Frame identifier associated with the tool registration. |
| `backendNodeId` (optional) | [DOM.BackendNodeId](DOM.md#type-backendnodeid) | Optional node ID for declarative tools. |
| `stackTrace` (optional) | [Runtime.StackTrace](Runtime.md#type-stacktrace) | The stack trace at the time of the registration. |

<a id="type-removedtool"></a>
### WebMCP.RemovedTool

Definition of a tool that was removed.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `toolId` | [WebMCP.ToolId](#type-toolid) | Identifier of the removed tool. |
| `name` | string | Tool name. |
| `frameId` | [Page.FrameId](Page.md#type-frameid) | Frame identifier associated with the tool registration. |
