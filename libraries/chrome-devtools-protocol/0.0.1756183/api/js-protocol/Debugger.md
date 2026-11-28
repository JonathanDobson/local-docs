# Debugger domain

Chrome DevTools Protocol, JavaScript / V8 inspector protocol (protocol 1.3).

Debugger domain exposes JavaScript debugging capabilities. It allows setting and removing
breakpoints, stepping through execution, exploring stack traces, etc.

Depends on: [Runtime](Runtime.md)

34 methods, 5 events, 13 types.

## Methods

### Debugger.continueToLocation

Continues execution until specific location is reached.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `location` | [Debugger.Location](#type-location) | Location to continue to. |
| `targetCallFrames` (optional) | string | Allowed values: `any`, `current` |

### Debugger.disable

Disables debugger for given page.

No parameters.

### Debugger.enable

Enables debugger for the given page. Clients should not assume that the debugging has been
enabled until the result for this command is received.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `maxScriptsCacheSize` (optional) | number | **Experimental** The maximum size in bytes of collected scripts (not referenced by other heap objects) the debugger can hold. Puts no limit if parameter is omitted. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `debuggerId` | [Runtime.UniqueDebuggerId](Runtime.md#type-uniquedebuggerid) | **Experimental** Unique identifier of the debugger. |

### Debugger.evaluateOnCallFrame

Evaluates expression on a given call frame.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `callFrameId` | [Debugger.CallFrameId](#type-callframeid) | Call frame identifier to evaluate on. |
| `expression` | string | Expression to evaluate. |
| `objectGroup` (optional) | string | String object group name to put result into (allows rapid releasing resulting object handles using `releaseObjectGroup`). |
| `includeCommandLineAPI` (optional) | boolean | Specifies whether command line API should be available to the evaluated expression, defaults to false. |
| `silent` (optional) | boolean | In silent mode exceptions thrown during evaluation are not reported and do not pause execution. Overrides `setPauseOnException` state. |
| `returnByValue` (optional) | boolean | Whether the result is expected to be a JSON object that should be sent by value. |
| `generatePreview` (optional) | boolean | **Experimental** Whether preview should be generated for the result. |
| `throwOnSideEffect` (optional) | boolean | Whether to throw an exception if side effect cannot be ruled out during evaluation. |
| `timeout` (optional) | [Runtime.TimeDelta](Runtime.md#type-timedelta) | **Experimental** Terminate execution after timing out (number of milliseconds). |
| `scopeNumber` (optional) | integer | **Experimental** Specifies the scope number to evaluate the expression in (default: 0, innermost scope). |

**Return object**

| Name | Type | Description |
|---|---|---|
| `result` | [Runtime.RemoteObject](Runtime.md#type-remoteobject) | Object wrapper for the evaluation result. |
| `exceptionDetails` (optional) | [Runtime.ExceptionDetails](Runtime.md#type-exceptiondetails) | Exception details. |

### Debugger.getPossibleBreakpoints

Returns possible locations for breakpoint. scriptId in start and end range locations should be
the same.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `start` | [Debugger.Location](#type-location) | Start of range to search possible breakpoint locations in. |
| `end` (optional) | [Debugger.Location](#type-location) | End of range to search possible breakpoint locations in (excluding). When not specified, end of scripts is used as end of range. |
| `restrictToFunction` (optional) | boolean | Only consider locations which are in the same (non-nested) function as start. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `locations` | array of [Debugger.BreakLocation](#type-breaklocation) | List of the possible breakpoint locations. |

### Debugger.getScopeChain

**Experimental**

Returns the current scope chain of the given call frame. Unlike the scope chain reported
with the `paused` event, it reflects changes made to variables since then (e.g. via
`evaluateOnCallFrame` or `setVariableValue`).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `callFrameId` | [Debugger.CallFrameId](#type-callframeid) | Call frame identifier to get the scope chain for. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `scopeChain` | array of [Debugger.Scope](#type-scope) | Scope chain for the call frame. |

### Debugger.getScriptSource

Returns source for the script with given id.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `scriptId` | [Runtime.ScriptId](Runtime.md#type-scriptid) | Id of the script to get source for. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `scriptSource` | string | Script source (empty in case of Wasm bytecode). |
| `bytecode` (optional) | string | Wasm bytecode. (Encoded as a base64 string when passed over JSON) |

### Debugger.disassembleWasmModule

**Experimental**

**Parameters**

| Name | Type | Description |
|---|---|---|
| `scriptId` | [Runtime.ScriptId](Runtime.md#type-scriptid) | Id of the script to disassemble |

**Return object**

| Name | Type | Description |
|---|---|---|
| `streamId` (optional) | string | For large modules, return a stream from which additional chunks of disassembly can be read successively. |
| `totalNumberOfLines` | integer | The total number of lines in the disassembly text. |
| `functionBodyOffsets` | array of integer | The offsets of all function bodies, in the format [start1, end1, start2, end2, ...] where all ends are exclusive. |
| `chunk` | [Debugger.WasmDisassemblyChunk](#type-wasmdisassemblychunk) | The first chunk of disassembly. |

### Debugger.nextWasmDisassemblyChunk

**Experimental**

Disassemble the next chunk of lines for the module corresponding to the
stream. If disassembly is complete, this API will invalidate the streamId
and return an empty chunk. Any subsequent calls for the now invalid stream
will return errors.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `streamId` | string |  |

**Return object**

| Name | Type | Description |
|---|---|---|
| `chunk` | [Debugger.WasmDisassemblyChunk](#type-wasmdisassemblychunk) | The next chunk of disassembly. |

### Debugger.getWasmBytecode

**Deprecated**

This command is deprecated. Use getScriptSource instead.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `scriptId` | [Runtime.ScriptId](Runtime.md#type-scriptid) | Id of the Wasm script to get source for. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `bytecode` | string | Script source. (Encoded as a base64 string when passed over JSON) |

### Debugger.getStackTrace

**Experimental**

Returns stack trace with given `stackTraceId`.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `stackTraceId` | [Runtime.StackTraceId](Runtime.md#type-stacktraceid) |  |

**Return object**

| Name | Type | Description |
|---|---|---|
| `stackTrace` | [Runtime.StackTrace](Runtime.md#type-stacktrace) |  |

### Debugger.pause

Stops on the next JavaScript statement.

No parameters.

### Debugger.pauseOnAsyncCall

**Experimental** · **Deprecated**

**Parameters**

| Name | Type | Description |
|---|---|---|
| `parentStackTraceId` | [Runtime.StackTraceId](Runtime.md#type-stacktraceid) | Debugger will pause when async call with given stack trace is started. |

### Debugger.removeBreakpoint

Removes JavaScript breakpoint.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `breakpointId` | [Debugger.BreakpointId](#type-breakpointid) |  |

### Debugger.restartFrame

Restarts particular call frame from the beginning. The old, deprecated
behavior of `restartFrame` is to stay paused and allow further CDP commands
after a restart was scheduled. This can cause problems with restarting, so
we now continue execution immediatly after it has been scheduled until we
reach the beginning of the restarted frame.

To stay back-wards compatible, `restartFrame` now expects a `mode`
parameter to be present. If the `mode` parameter is missing, `restartFrame`
errors out.

The various return values are deprecated and `callFrames` is always empty.
Use the call frames from the `Debugger#paused` events instead, that fires
once V8 pauses at the beginning of the restarted function.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `callFrameId` | [Debugger.CallFrameId](#type-callframeid) | Call frame identifier to evaluate on. |
| `mode` (optional) | string | **Experimental** The `mode` parameter must be present and set to 'StepInto', otherwise `restartFrame` will error out. Allowed values: `StepInto` |

**Return object**

| Name | Type | Description |
|---|---|---|
| `callFrames` | array of [Debugger.CallFrame](#type-callframe) | **Deprecated** New stack trace. |
| `asyncStackTrace` (optional) | [Runtime.StackTrace](Runtime.md#type-stacktrace) | **Deprecated** Async stack trace, if any. |
| `asyncStackTraceId` (optional) | [Runtime.StackTraceId](Runtime.md#type-stacktraceid) | **Deprecated** Async stack trace, if any. |

### Debugger.resume

Resumes JavaScript execution.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `terminateOnResume` (optional) | boolean | Set to true to terminate execution upon resuming execution. In contrast to Runtime.terminateExecution, this will allows to execute further JavaScript (i.e. via evaluation) until execution of the paused code is actually resumed, at which point termination is triggered. If execution is currently not paused, this parameter has no effect. |

### Debugger.searchInContent

Searches for given string in script content.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `scriptId` | [Runtime.ScriptId](Runtime.md#type-scriptid) | Id of the script to search in. |
| `query` | string | String to search for. |
| `caseSensitive` (optional) | boolean | If true, search is case sensitive. |
| `isRegex` (optional) | boolean | If true, treats string parameter as regex. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `result` | array of [Debugger.SearchMatch](#type-searchmatch) | List of search matches. |

### Debugger.setAsyncCallStackDepth

Enables or disables async call stacks tracking.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `maxDepth` | integer | Maximum depth of async call stacks. Setting to `0` will effectively disable collecting async call stacks (default). |

### Debugger.setBlackboxExecutionContexts

**Experimental**

Replace previous blackbox execution contexts with passed ones. Forces backend to skip
stepping/pausing in scripts in these execution contexts. VM will try to leave blackboxed script by
performing 'step in' several times, finally resorting to 'step out' if unsuccessful.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `uniqueIds` | array of string | Array of execution context unique ids for the debugger to ignore. |

### Debugger.setBlackboxPatterns

**Experimental**

Replace previous blackbox patterns with passed ones. Forces backend to skip stepping/pausing in
scripts with url matching one of the patterns. VM will try to leave blackboxed script by
performing 'step in' several times, finally resorting to 'step out' if unsuccessful.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `patterns` | array of string | Array of regexps that will be used to check script url for blackbox state. |
| `skipAnonymous` (optional) | boolean | If true, also ignore scripts with no source url. |

### Debugger.setBlackboxedRanges

**Experimental**

Makes backend skip steps in the script in blackboxed ranges. VM will try leave blacklisted
scripts by performing 'step in' several times, finally resorting to 'step out' if unsuccessful.
Positions array contains positions where blackbox state is changed. First interval isn't
blackboxed. Array should be sorted.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `scriptId` | [Runtime.ScriptId](Runtime.md#type-scriptid) | Id of the script. |
| `positions` | array of [Debugger.ScriptPosition](#type-scriptposition) |  |

### Debugger.setBreakpoint

Sets JavaScript breakpoint at a given location.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `location` | [Debugger.Location](#type-location) | Location to set breakpoint in. |
| `condition` (optional) | string | Expression to use as a breakpoint condition. When specified, debugger will only stop on the breakpoint if this expression evaluates to true. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `breakpointId` | [Debugger.BreakpointId](#type-breakpointid) | Id of the created breakpoint for further reference. |
| `actualLocation` | [Debugger.Location](#type-location) | Location this breakpoint resolved into. |

### Debugger.setInstrumentationBreakpoint

Sets instrumentation breakpoint.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `instrumentation` | string | Instrumentation name. Allowed values: `beforeScriptExecution`, `beforeScriptWithSourceMapExecution` |

**Return object**

| Name | Type | Description |
|---|---|---|
| `breakpointId` | [Debugger.BreakpointId](#type-breakpointid) | Id of the created breakpoint for further reference. |

### Debugger.setBreakpointByUrl

Sets JavaScript breakpoint at given location specified either by URL or URL regex. Once this
command is issued, all existing parsed scripts will have breakpoints resolved and returned in
`locations` property. Further matching script parsing will result in subsequent
`breakpointResolved` events issued. This logical breakpoint will survive page reloads.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `lineNumber` | integer | Line number to set breakpoint at. |
| `url` (optional) | string | URL of the resources to set breakpoint on. |
| `urlRegex` (optional) | string | Regex pattern for the URLs of the resources to set breakpoints on. Either `url` or `urlRegex` must be specified. |
| `scriptHash` (optional) | string | Script hash of the resources to set breakpoint on. |
| `columnNumber` (optional) | integer | Offset in the line to set breakpoint at. |
| `condition` (optional) | string | Expression to use as a breakpoint condition. When specified, debugger will only stop on the breakpoint if this expression evaluates to true. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `breakpointId` | [Debugger.BreakpointId](#type-breakpointid) | Id of the created breakpoint for further reference. |
| `locations` | array of [Debugger.Location](#type-location) | List of the locations this breakpoint resolved into upon addition. |

### Debugger.setBreakpointOnFunctionCall

**Experimental**

Sets JavaScript breakpoint before each call to the given function.
If another function was created from the same source as a given one,
calling it will also trigger the breakpoint.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `objectId` | [Runtime.RemoteObjectId](Runtime.md#type-remoteobjectid) | Function object id. |
| `condition` (optional) | string | Expression to use as a breakpoint condition. When specified, debugger will stop on the breakpoint if this expression evaluates to true. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `breakpointId` | [Debugger.BreakpointId](#type-breakpointid) | Id of the created breakpoint for further reference. |

### Debugger.setBreakpointsActive

Activates / deactivates all breakpoints on the page.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `active` | boolean | New value for breakpoints active state. |

### Debugger.setPauseOnExceptions

Defines pause on exceptions state. Can be set to stop on all exceptions, uncaught exceptions,
or caught exceptions, no exceptions. Initial pause on exceptions state is `none`.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `state` | string | Pause on exceptions mode. Allowed values: `none`, `caught`, `uncaught`, `all` |

### Debugger.setReturnValue

**Experimental**

Changes return value in top frame. Available only at return break position.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `newValue` | [Runtime.CallArgument](Runtime.md#type-callargument) | New return value. |

### Debugger.setScriptSource

**Deprecated**

Live edit is no longer supported and this command always fails with a "no longer available" error.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `scriptId` | [Runtime.ScriptId](Runtime.md#type-scriptid) | Id of the script to edit. |
| `scriptSource` | string | New content of the script. |
| `dryRun` (optional) | boolean | If true the change will not actually be applied. Dry run may be used to get result description without actually modifying the code. |
| `allowTopFrameEditing` (optional) | boolean | **Experimental** If true, then `scriptSource` is allowed to change the function on top of the stack as long as the top-most stack frame is the only activation of that function. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `callFrames` (optional) | array of [Debugger.CallFrame](#type-callframe) | **Deprecated** New stack trace in case editing has happened while VM was stopped. |
| `stackChanged` (optional) | boolean | **Deprecated** Whether current call stack was modified after applying the changes. |
| `asyncStackTrace` (optional) | [Runtime.StackTrace](Runtime.md#type-stacktrace) | **Deprecated** Async stack trace, if any. |
| `asyncStackTraceId` (optional) | [Runtime.StackTraceId](Runtime.md#type-stacktraceid) | **Deprecated** Async stack trace, if any. |
| `status` | string | **Experimental** Whether the operation was successful or not. Only `Ok` denotes a successful live edit while the other enum variants denote why the live edit failed. Allowed values: `Ok`, `CompileError`, `BlockedByActiveGenerator`, `BlockedByActiveFunction`, `BlockedByTopLevelEsModuleChange` |
| `exceptionDetails` (optional) | [Runtime.ExceptionDetails](Runtime.md#type-exceptiondetails) | Exception details if any. Only present when `status` is `CompileError`. |

### Debugger.setSkipAllPauses

Makes page not interrupt on any pauses (breakpoint, exception, dom exception etc).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `skip` | boolean | New value for skip pauses state. |

### Debugger.setVariableValue

Changes value of variable in a callframe. Object-based scopes are not supported and must be
mutated manually.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `scopeNumber` | integer | 0-based number of scope as was listed in scope chain. Only 'local', 'closure' and 'catch' scope types are allowed. Other scopes could be manipulated manually. |
| `variableName` | string | Variable name. |
| `newValue` | [Runtime.CallArgument](Runtime.md#type-callargument) | New variable value. |
| `callFrameId` | [Debugger.CallFrameId](#type-callframeid) | Id of callframe that holds variable. |

### Debugger.stepInto

Steps into the function call.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `breakOnAsyncCall` (optional) | boolean | **Experimental** Debugger will pause on the execution of the first async task which was scheduled before next pause. |
| `skipList` (optional) | array of [Debugger.LocationRange](#type-locationrange) | **Experimental** The skipList specifies location ranges that should be skipped on step into. |

### Debugger.stepOut

Steps out of the function call.

No parameters.

### Debugger.stepOver

Steps over the statement.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `skipList` (optional) | array of [Debugger.LocationRange](#type-locationrange) | **Experimental** The skipList specifies location ranges that should be skipped on step over. |
| `enterRanges` (optional) | array of [Debugger.LocationRange](#type-locationrange) | **Experimental** Functions whose source range lies within one of the enterRanges are entered as if by stepInto, even when they are called (directly or indirectly) from a call that is stepped over. |

## Events

### Debugger.breakpointResolved

**Deprecated**

Fired when breakpoint is resolved to an actual script and location.
Deprecated in favor of `resolvedBreakpoints` in the `scriptParsed` event.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `breakpointId` | [Debugger.BreakpointId](#type-breakpointid) | Breakpoint unique identifier. |
| `location` | [Debugger.Location](#type-location) | Actual breakpoint location. |

### Debugger.paused

Fired when the virtual machine stopped on breakpoint or exception or any other stop criteria.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `callFrames` | array of [Debugger.CallFrame](#type-callframe) | Call stack the virtual machine stopped on. |
| `reason` | string | Pause reason. Allowed values: `ambiguous`, `assert`, `CSPViolation`, `debugCommand`, `DOM`, `EventListener`, `exception`, `instrumentation`, `OOM`, `other`, `promiseRejection`, `XHR`, `step` |
| `data` (optional) | object | Object containing break-specific auxiliary properties. |
| `hitBreakpoints` (optional) | array of string | Hit breakpoints IDs |
| `asyncStackTrace` (optional) | [Runtime.StackTrace](Runtime.md#type-stacktrace) | Async stack trace, if any. |
| `asyncStackTraceId` (optional) | [Runtime.StackTraceId](Runtime.md#type-stacktraceid) | **Experimental** Async stack trace, if any. |
| `asyncCallStackTraceId` (optional) | [Runtime.StackTraceId](Runtime.md#type-stacktraceid) | **Experimental** · **Deprecated** Never present, will be removed. |

### Debugger.resumed

Fired when the virtual machine resumed execution.

### Debugger.scriptFailedToParse

Fired when virtual machine fails to parse the script.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `scriptId` | [Runtime.ScriptId](Runtime.md#type-scriptid) | Identifier of the script parsed. |
| `url` | string | URL or name of the script parsed (if any). |
| `startLine` | integer | Line offset of the script within the resource with given URL (for script tags). |
| `startColumn` | integer | Column offset of the script within the resource with given URL. |
| `endLine` | integer | Last line of the script. |
| `endColumn` | integer | Length of the last line of the script. |
| `executionContextId` | [Runtime.ExecutionContextId](Runtime.md#type-executioncontextid) | Specifies script creation context. |
| `hash` | string | Content hash of the script, SHA-256. |
| `buildId` | string | For Wasm modules, the content of the `build_id` custom section. For JavaScript the `debugId` magic comment. |
| `executionContextAuxData` (optional) | object | Embedder-specific auxiliary data likely matching {isDefault: boolean, type: 'default'\|'isolated'\|'worker', frameId: string} |
| `sourceMapURL` (optional) | string | URL of source map associated with script (if any). |
| `hasSourceURL` (optional) | boolean | True, if this script has sourceURL. |
| `isModule` (optional) | boolean | True, if this script is ES6 module. |
| `length` (optional) | integer | This script length. |
| `stackTrace` (optional) | [Runtime.StackTrace](Runtime.md#type-stacktrace) | **Experimental** JavaScript top stack frame of where the script parsed event was triggered if available. |
| `codeOffset` (optional) | integer | **Experimental** If the scriptLanguage is WebAssembly, the code section offset in the module. |
| `scriptLanguage` (optional) | [Debugger.ScriptLanguage](Debugger.md#type-scriptlanguage) | **Experimental** The language of the script. |
| `embedderName` (optional) | string | **Experimental** The name the embedder supplied for this script. |

### Debugger.scriptParsed

Fired when virtual machine parses script. This event is also fired for all known and uncollected
scripts upon enabling debugger.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `scriptId` | [Runtime.ScriptId](Runtime.md#type-scriptid) | Identifier of the script parsed. |
| `url` | string | URL or name of the script parsed (if any). |
| `startLine` | integer | Line offset of the script within the resource with given URL (for script tags). |
| `startColumn` | integer | Column offset of the script within the resource with given URL. |
| `endLine` | integer | Last line of the script. |
| `endColumn` | integer | Length of the last line of the script. |
| `executionContextId` | [Runtime.ExecutionContextId](Runtime.md#type-executioncontextid) | Specifies script creation context. |
| `hash` | string | Content hash of the script, SHA-256. |
| `buildId` | string | For Wasm modules, the content of the `build_id` custom section. For JavaScript the `debugId` magic comment. |
| `executionContextAuxData` (optional) | object | Embedder-specific auxiliary data likely matching {isDefault: boolean, type: 'default'\|'isolated'\|'worker', frameId: string} |
| `isLiveEdit` (optional) | boolean | **Experimental** True, if this script is generated as a result of the live edit operation. |
| `sourceMapURL` (optional) | string | URL of source map associated with script (if any). |
| `hasSourceURL` (optional) | boolean | True, if this script has sourceURL. |
| `isModule` (optional) | boolean | True, if this script is ES6 module. |
| `length` (optional) | integer | This script length. |
| `stackTrace` (optional) | [Runtime.StackTrace](Runtime.md#type-stacktrace) | **Experimental** JavaScript top stack frame of where the script parsed event was triggered if available. |
| `codeOffset` (optional) | integer | **Experimental** If the scriptLanguage is WebAssembly, the code section offset in the module. |
| `scriptLanguage` (optional) | [Debugger.ScriptLanguage](Debugger.md#type-scriptlanguage) | **Experimental** The language of the script. |
| `debugSymbols` (optional) | array of [Debugger.DebugSymbols](Debugger.md#type-debugsymbols) | **Experimental** If the scriptLanguage is WebAssembly, the source of debug symbols for the module. |
| `embedderName` (optional) | string | **Experimental** The name the embedder supplied for this script. |
| `resolvedBreakpoints` (optional) | array of [Debugger.ResolvedBreakpoint](#type-resolvedbreakpoint) | **Experimental** The list of set breakpoints in this script if calls to `setBreakpointByUrl` matches this script's URL or hash. Clients that use this list can ignore the `breakpointResolved` event. They are equivalent. |

## Types

<a id="type-breakpointid"></a>
### Debugger.BreakpointId

Breakpoint identifier.

Type: string

<a id="type-callframeid"></a>
### Debugger.CallFrameId

Call frame identifier.

Type: string

<a id="type-location"></a>
### Debugger.Location

Location in the source code.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `scriptId` | [Runtime.ScriptId](Runtime.md#type-scriptid) | Script identifier as reported in the `Debugger.scriptParsed`. |
| `lineNumber` | integer | Line number in the script (0-based). |
| `columnNumber` (optional) | integer | Column number in the script (0-based). |

<a id="type-scriptposition"></a>
### Debugger.ScriptPosition

**Experimental**

Location in the source code.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `lineNumber` | integer |  |
| `columnNumber` | integer |  |

<a id="type-locationrange"></a>
### Debugger.LocationRange

**Experimental**

Location range within one script.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `scriptId` | [Runtime.ScriptId](Runtime.md#type-scriptid) |  |
| `start` | [Debugger.ScriptPosition](#type-scriptposition) |  |
| `end` | [Debugger.ScriptPosition](#type-scriptposition) |  |

<a id="type-callframe"></a>
### Debugger.CallFrame

JavaScript call frame. Array of call frames form the call stack.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `callFrameId` | [Debugger.CallFrameId](#type-callframeid) | Call frame identifier. This identifier is only valid while the virtual machine is paused. |
| `functionName` | string | Name of the JavaScript function called on this call frame. |
| `functionLocation` (optional) | [Debugger.Location](#type-location) | Location in the source code. |
| `location` | [Debugger.Location](#type-location) | Location in the source code. |
| `url` | string | **Deprecated** JavaScript script name or url. Deprecated in favor of using the `location.scriptId` to resolve the URL via a previously sent `Debugger.scriptParsed` event. |
| `scopeChain` | array of [Debugger.Scope](#type-scope) | Scope chain for this call frame. |
| `this` | [Runtime.RemoteObject](Runtime.md#type-remoteobject) | `this` object for this call frame. |
| `returnValue` (optional) | [Runtime.RemoteObject](Runtime.md#type-remoteobject) | The value being returned, if the function is at return point. |
| `canBeRestarted` (optional) | boolean | **Experimental** Valid only while the VM is paused and indicates whether this frame can be restarted or not. Note that a `true` value here does not guarantee that Debugger#restartFrame with this CallFrameId will be successful, but it is very likely. |

<a id="type-scope"></a>
### Debugger.Scope

Scope description.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `type` | string | Scope type. Allowed values: `global`, `local`, `with`, `closure`, `catch`, `block`, `script`, `eval`, `module`, `wasm-expression-stack` |
| `object` | [Runtime.RemoteObject](Runtime.md#type-remoteobject) | Object representing the scope. For `global` and `with` scopes it represents the actual object; for the rest of the scopes, it is artificial transient object enumerating scope variables as its properties. |
| `name` (optional) | string |  |
| `startLocation` (optional) | [Debugger.Location](#type-location) | Location in the source code where scope starts |
| `endLocation` (optional) | [Debugger.Location](#type-location) | Location in the source code where scope ends |
| `emptyReason` (optional) | string | **Experimental** Present if the scope has no variable values to show. Absent means that the scope declares at least one variable with an available value. Empty scopes are retained in the scope chain because they can be targeted via `evaluateOnCallFrame` (using `scopeNumber`) or matched against scopes in source maps. Allowed values: `no-variables`, `all-unavailable` |

<a id="type-searchmatch"></a>
### Debugger.SearchMatch

Search match for resource.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `lineNumber` | number | Line number in resource content. |
| `lineContent` | string | Line with match content. |

<a id="type-breaklocation"></a>
### Debugger.BreakLocation

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `scriptId` | [Runtime.ScriptId](Runtime.md#type-scriptid) | Script identifier as reported in the `Debugger.scriptParsed`. |
| `lineNumber` | integer | Line number in the script (0-based). |
| `columnNumber` (optional) | integer | Column number in the script (0-based). |
| `type` (optional) | string | Allowed values: `debuggerStatement`, `call`, `return` |

<a id="type-wasmdisassemblychunk"></a>
### Debugger.WasmDisassemblyChunk

**Experimental**

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `lines` | array of string | The next chunk of disassembled lines. |
| `bytecodeOffsets` | array of integer | The bytecode offsets describing the start of each line. |

<a id="type-scriptlanguage"></a>
### Debugger.ScriptLanguage

Enum of possible script languages.

Type: string

Allowed values: `JavaScript`, `WebAssembly`

<a id="type-debugsymbols"></a>
### Debugger.DebugSymbols

Debug symbols available for a wasm script.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `type` | string | Type of the debug symbols. Allowed values: `SourceMap`, `EmbeddedDWARF`, `ExternalDWARF` |
| `externalURL` (optional) | string | URL of the external symbol source. |

<a id="type-resolvedbreakpoint"></a>
### Debugger.ResolvedBreakpoint

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `breakpointId` | [Debugger.BreakpointId](#type-breakpointid) | Breakpoint unique identifier. |
| `location` | [Debugger.Location](#type-location) | Actual breakpoint location. |
