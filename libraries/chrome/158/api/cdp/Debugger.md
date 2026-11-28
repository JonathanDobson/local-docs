# Debugger domain

Debugger domain exposes JavaScript debugging capabilities. It allows setting and removing breakpoints, stepping through execution, exploring stack traces, etc.

Depends on: [Runtime](Runtime.md)

Methods are called as `Debugger.<command>` and events arrive as `Debugger.<event>`.

## Commands

### Debugger.continueToLocation

Continues execution until specific location is reached.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `location` | [Location](#type-location) | Location to continue to. |
| `targetCallFrames` (optional) | enum: `any`, `current` |  |

### Debugger.disable

Disables debugger for given page.

### Debugger.enable

Enables debugger for the given page. Clients should not assume that the debugging has been enabled until the result for this command is received.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `maxScriptsCacheSize` (optional) *(experimental)* | number | The maximum size in bytes of collected scripts (not referenced by other heap objects) the debugger can hold. Puts no limit if parameter is omitted. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `debuggerId` *(experimental)* | [Runtime.UniqueDebuggerId](Runtime.md#type-uniquedebuggerid) | Unique identifier of the debugger. |

### Debugger.evaluateOnCallFrame

Evaluates expression on a given call frame.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `callFrameId` | [CallFrameId](#type-callframeid) | Call frame identifier to evaluate on. |
| `expression` | string | Expression to evaluate. |
| `objectGroup` (optional) | string | String object group name to put result into (allows rapid releasing resulting object handles using `releaseObjectGroup`). |
| `includeCommandLineAPI` (optional) | boolean | Specifies whether command line API should be available to the evaluated expression, defaults to false. |
| `silent` (optional) | boolean | In silent mode exceptions thrown during evaluation are not reported and do not pause execution. Overrides `setPauseOnException` state. |
| `returnByValue` (optional) | boolean | Whether the result is expected to be a JSON object that should be sent by value. |
| `generatePreview` (optional) *(experimental)* | boolean | Whether preview should be generated for the result. |
| `throwOnSideEffect` (optional) | boolean | Whether to throw an exception if side effect cannot be ruled out during evaluation. |
| `timeout` (optional) *(experimental)* | [Runtime.TimeDelta](Runtime.md#type-timedelta) | Terminate execution after timing out (number of milliseconds). |
| `scopeNumber` (optional) *(experimental)* | integer | Specifies the scope number to evaluate the expression in (default: 0, innermost scope). |

**Returns**

| Name | Type | Description |
|---|---|---|
| `result` | [Runtime.RemoteObject](Runtime.md#type-remoteobject) | Object wrapper for the evaluation result. |
| `exceptionDetails` (optional) | [Runtime.ExceptionDetails](Runtime.md#type-exceptiondetails) | Exception details. |

### Debugger.getPossibleBreakpoints

Returns possible locations for breakpoint. scriptId in start and end range locations should be the same.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `start` | [Location](#type-location) | Start of range to search possible breakpoint locations in. |
| `end` (optional) | [Location](#type-location) | End of range to search possible breakpoint locations in (excluding). When not specified, end of scripts is used as end of range. |
| `restrictToFunction` (optional) | boolean | Only consider locations which are in the same (non-nested) function as start. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `locations` | array of [BreakLocation](#type-breaklocation) | List of the possible breakpoint locations. |

### Debugger.getScriptSource

Returns source for the script with given id.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `scriptId` | [Runtime.ScriptId](Runtime.md#type-scriptid) | Id of the script to get source for. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `scriptSource` | string | Script source (empty in case of Wasm bytecode). |
| `bytecode` (optional) | binary | Wasm bytecode. |

### Debugger.disassembleWasmModule *(experimental)*

**Parameters**

| Name | Type | Description |
|---|---|---|
| `scriptId` | [Runtime.ScriptId](Runtime.md#type-scriptid) | Id of the script to disassemble |

**Returns**

| Name | Type | Description |
|---|---|---|
| `streamId` (optional) | string | For large modules, return a stream from which additional chunks of disassembly can be read successively. |
| `totalNumberOfLines` | integer | The total number of lines in the disassembly text. |
| `functionBodyOffsets` | array of integer | The offsets of all function bodies, in the format [start1, end1, start2, end2, ...] where all ends are exclusive. |
| `chunk` | [WasmDisassemblyChunk](#type-wasmdisassemblychunk) | The first chunk of disassembly. |

### Debugger.nextWasmDisassemblyChunk *(experimental)*

Disassemble the next chunk of lines for the module corresponding to the stream. If disassembly is complete, this API will invalidate the streamId and return an empty chunk. Any subsequent calls for the now invalid stream will return errors.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `streamId` | string |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `chunk` | [WasmDisassemblyChunk](#type-wasmdisassemblychunk) | The next chunk of disassembly. |

### Debugger.getWasmBytecode *(deprecated)*

This command is deprecated. Use getScriptSource instead.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `scriptId` | [Runtime.ScriptId](Runtime.md#type-scriptid) | Id of the Wasm script to get source for. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `bytecode` | binary | Script source. |

### Debugger.getStackTrace *(experimental)*

Returns stack trace with given `stackTraceId`.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `stackTraceId` | [Runtime.StackTraceId](Runtime.md#type-stacktraceid) |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `stackTrace` | [Runtime.StackTrace](Runtime.md#type-stacktrace) |  |

### Debugger.pause

Stops on the next JavaScript statement.

### Debugger.pauseOnAsyncCall *(experimental)* *(deprecated)*

**Parameters**

| Name | Type | Description |
|---|---|---|
| `parentStackTraceId` | [Runtime.StackTraceId](Runtime.md#type-stacktraceid) | Debugger will pause when async call with given stack trace is started. |

### Debugger.removeBreakpoint

Removes JavaScript breakpoint.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `breakpointId` | [BreakpointId](#type-breakpointid) |  |

### Debugger.restartFrame

Restarts particular call frame from the beginning. The old, deprecated behavior of `restartFrame` is to stay paused and allow further CDP commands after a restart was scheduled. This can cause problems with restarting, so we now continue execution immediatly after it has been scheduled until we reach the beginning of the restarted frame.  To stay back-wards compatible, `restartFrame` now expects a `mode` parameter to be present. If the `mode` parameter is missing, `restartFrame` errors out.  The various return values are deprecated and `callFrames` is always empty. Use the call frames from the `Debugger#paused` events instead, that fires once V8 pauses at the beginning of the restarted function.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `callFrameId` | [CallFrameId](#type-callframeid) | Call frame identifier to evaluate on. |
| `mode` (optional) *(experimental)* | enum: `StepInto` | The `mode` parameter must be present and set to 'StepInto', otherwise `restartFrame` will error out. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `callFrames` *(deprecated)* | array of [CallFrame](#type-callframe) | New stack trace. |
| `asyncStackTrace` (optional) *(deprecated)* | [Runtime.StackTrace](Runtime.md#type-stacktrace) | Async stack trace, if any. |
| `asyncStackTraceId` (optional) *(deprecated)* | [Runtime.StackTraceId](Runtime.md#type-stacktraceid) | Async stack trace, if any. |

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

**Returns**

| Name | Type | Description |
|---|---|---|
| `result` | array of [SearchMatch](#type-searchmatch) | List of search matches. |

### Debugger.setAsyncCallStackDepth

Enables or disables async call stacks tracking.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `maxDepth` | integer | Maximum depth of async call stacks. Setting to `0` will effectively disable collecting async call stacks (default). |

### Debugger.setBlackboxExecutionContexts *(experimental)*

Replace previous blackbox execution contexts with passed ones. Forces backend to skip stepping/pausing in scripts in these execution contexts. VM will try to leave blackboxed script by performing 'step in' several times, finally resorting to 'step out' if unsuccessful.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `uniqueIds` | array of string | Array of execution context unique ids for the debugger to ignore. |

### Debugger.setBlackboxPatterns *(experimental)*

Replace previous blackbox patterns with passed ones. Forces backend to skip stepping/pausing in scripts with url matching one of the patterns. VM will try to leave blackboxed script by performing 'step in' several times, finally resorting to 'step out' if unsuccessful.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `patterns` | array of string | Array of regexps that will be used to check script url for blackbox state. |
| `skipAnonymous` (optional) | boolean | If true, also ignore scripts with no source url. |

### Debugger.setBlackboxedRanges *(experimental)*

Makes backend skip steps in the script in blackboxed ranges. VM will try leave blacklisted scripts by performing 'step in' several times, finally resorting to 'step out' if unsuccessful. Positions array contains positions where blackbox state is changed. First interval isn't blackboxed. Array should be sorted.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `scriptId` | [Runtime.ScriptId](Runtime.md#type-scriptid) | Id of the script. |
| `positions` | array of [ScriptPosition](#type-scriptposition) |  |

### Debugger.setBreakpoint

Sets JavaScript breakpoint at a given location.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `location` | [Location](#type-location) | Location to set breakpoint in. |
| `condition` (optional) | string | Expression to use as a breakpoint condition. When specified, debugger will only stop on the breakpoint if this expression evaluates to true. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `breakpointId` | [BreakpointId](#type-breakpointid) | Id of the created breakpoint for further reference. |
| `actualLocation` | [Location](#type-location) | Location this breakpoint resolved into. |

### Debugger.setInstrumentationBreakpoint

Sets instrumentation breakpoint.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `instrumentation` | enum: `beforeScriptExecution`, `beforeScriptWithSourceMapExecution` | Instrumentation name. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `breakpointId` | [BreakpointId](#type-breakpointid) | Id of the created breakpoint for further reference. |

### Debugger.setBreakpointByUrl

Sets JavaScript breakpoint at given location specified either by URL or URL regex. Once this command is issued, all existing parsed scripts will have breakpoints resolved and returned in `locations` property. Further matching script parsing will result in subsequent `breakpointResolved` events issued. This logical breakpoint will survive page reloads.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `lineNumber` | integer | Line number to set breakpoint at. |
| `url` (optional) | string | URL of the resources to set breakpoint on. |
| `urlRegex` (optional) | string | Regex pattern for the URLs of the resources to set breakpoints on. Either `url` or `urlRegex` must be specified. |
| `scriptHash` (optional) | string | Script hash of the resources to set breakpoint on. |
| `columnNumber` (optional) | integer | Offset in the line to set breakpoint at. |
| `condition` (optional) | string | Expression to use as a breakpoint condition. When specified, debugger will only stop on the breakpoint if this expression evaluates to true. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `breakpointId` | [BreakpointId](#type-breakpointid) | Id of the created breakpoint for further reference. |
| `locations` | array of [Location](#type-location) | List of the locations this breakpoint resolved into upon addition. |

### Debugger.setBreakpointOnFunctionCall *(experimental)*

Sets JavaScript breakpoint before each call to the given function. If another function was created from the same source as a given one, calling it will also trigger the breakpoint.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `objectId` | [Runtime.RemoteObjectId](Runtime.md#type-remoteobjectid) | Function object id. |
| `condition` (optional) | string | Expression to use as a breakpoint condition. When specified, debugger will stop on the breakpoint if this expression evaluates to true. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `breakpointId` | [BreakpointId](#type-breakpointid) | Id of the created breakpoint for further reference. |

### Debugger.setBreakpointsActive

Activates / deactivates all breakpoints on the page.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `active` | boolean | New value for breakpoints active state. |

### Debugger.setPauseOnExceptions

Defines pause on exceptions state. Can be set to stop on all exceptions, uncaught exceptions, or caught exceptions, no exceptions. Initial pause on exceptions state is `none`.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `state` | enum: `none`, `caught`, `uncaught`, `all` | Pause on exceptions mode. |

### Debugger.setReturnValue *(experimental)*

Changes return value in top frame. Available only at return break position.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `newValue` | [Runtime.CallArgument](Runtime.md#type-callargument) | New return value. |

### Debugger.setScriptSource *(deprecated)*

Live edit is no longer supported and this command always fails with a "no longer available" error.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `scriptId` | [Runtime.ScriptId](Runtime.md#type-scriptid) | Id of the script to edit. |
| `scriptSource` | string | New content of the script. |
| `dryRun` (optional) | boolean | If true the change will not actually be applied. Dry run may be used to get result description without actually modifying the code. |
| `allowTopFrameEditing` (optional) *(experimental)* | boolean | If true, then `scriptSource` is allowed to change the function on top of the stack as long as the top-most stack frame is the only activation of that function. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `callFrames` (optional) *(deprecated)* | array of [CallFrame](#type-callframe) | New stack trace in case editing has happened while VM was stopped. |
| `stackChanged` (optional) *(deprecated)* | boolean | Whether current call stack  was modified after applying the changes. |
| `asyncStackTrace` (optional) *(deprecated)* | [Runtime.StackTrace](Runtime.md#type-stacktrace) | Async stack trace, if any. |
| `asyncStackTraceId` (optional) *(deprecated)* | [Runtime.StackTraceId](Runtime.md#type-stacktraceid) | Async stack trace, if any. |
| `status` *(experimental)* | enum: `Ok`, `CompileError`, `BlockedByActiveGenerator`, `BlockedByActiveFunction`, `BlockedByTopLevelEsModuleChange` | Whether the operation was successful or not. Only `Ok` denotes a successful live edit while the other enum variants denote why the live edit failed. |
| `exceptionDetails` (optional) | [Runtime.ExceptionDetails](Runtime.md#type-exceptiondetails) | Exception details if any. Only present when `status` is `CompileError`. |

### Debugger.setSkipAllPauses

Makes page not interrupt on any pauses (breakpoint, exception, dom exception etc).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `skip` | boolean | New value for skip pauses state. |

### Debugger.setVariableValue

Changes value of variable in a callframe. Object-based scopes are not supported and must be mutated manually.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `scopeNumber` | integer | 0-based number of scope as was listed in scope chain. Only 'local', 'closure' and 'catch' scope types are allowed. Other scopes could be manipulated manually. |
| `variableName` | string | Variable name. |
| `newValue` | [Runtime.CallArgument](Runtime.md#type-callargument) | New variable value. |
| `callFrameId` | [CallFrameId](#type-callframeid) | Id of callframe that holds variable. |

### Debugger.stepInto

Steps into the function call.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `breakOnAsyncCall` (optional) *(experimental)* | boolean | Debugger will pause on the execution of the first async task which was scheduled before next pause. |
| `skipList` (optional) *(experimental)* | array of [LocationRange](#type-locationrange) | The skipList specifies location ranges that should be skipped on step into. |

### Debugger.stepOut

Steps out of the function call.

### Debugger.stepOver

Steps over the statement.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `skipList` (optional) *(experimental)* | array of [LocationRange](#type-locationrange) | The skipList specifies location ranges that should be skipped on step over. |
| `enterRanges` (optional) *(experimental)* | array of [LocationRange](#type-locationrange) | Functions whose source range lies within one of the enterRanges are entered as if by stepInto, even when they are called (directly or indirectly) from a call that is stepped over. |

## Events

### Debugger.breakpointResolved *(deprecated)*

Fired when breakpoint is resolved to an actual script and location. Deprecated in favor of `resolvedBreakpoints` in the `scriptParsed` event.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `breakpointId` | [BreakpointId](#type-breakpointid) | Breakpoint unique identifier. |
| `location` | [Location](#type-location) | Actual breakpoint location. |

### Debugger.paused

Fired when the virtual machine stopped on breakpoint or exception or any other stop criteria.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `callFrames` | array of [CallFrame](#type-callframe) | Call stack the virtual machine stopped on. |
| `reason` | enum: `ambiguous`, `assert`, `CSPViolation`, `debugCommand`, `DOM`, `EventListener`, `exception`, `instrumentation`, `OOM`, `other`, `promiseRejection`, `XHR`, `step` | Pause reason. |
| `data` (optional) | object | Object containing break-specific auxiliary properties. |
| `hitBreakpoints` (optional) | array of string | Hit breakpoints IDs |
| `asyncStackTrace` (optional) | [Runtime.StackTrace](Runtime.md#type-stacktrace) | Async stack trace, if any. |
| `asyncStackTraceId` (optional) *(experimental)* | [Runtime.StackTraceId](Runtime.md#type-stacktraceid) | Async stack trace, if any. |
| `asyncCallStackTraceId` (optional) *(experimental)* *(deprecated)* | [Runtime.StackTraceId](Runtime.md#type-stacktraceid) | Never present, will be removed. |

### Debugger.resumed

Fired when the virtual machine resumed execution.

### Debugger.scriptFailedToParse

Fired when virtual machine fails to parse the script.

**Parameters**

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
| `stackTrace` (optional) *(experimental)* | [Runtime.StackTrace](Runtime.md#type-stacktrace) | JavaScript top stack frame of where the script parsed event was triggered if available. |
| `codeOffset` (optional) *(experimental)* | integer | If the scriptLanguage is WebAssembly, the code section offset in the module. |
| `scriptLanguage` (optional) *(experimental)* | [Debugger.ScriptLanguage](Debugger.md#type-scriptlanguage) | The language of the script. |
| `embedderName` (optional) *(experimental)* | string | The name the embedder supplied for this script. |

### Debugger.scriptParsed

Fired when virtual machine parses script. This event is also fired for all known and uncollected scripts upon enabling debugger.

**Parameters**

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
| `isLiveEdit` (optional) *(experimental)* | boolean | True, if this script is generated as a result of the live edit operation. |
| `sourceMapURL` (optional) | string | URL of source map associated with script (if any). |
| `hasSourceURL` (optional) | boolean | True, if this script has sourceURL. |
| `isModule` (optional) | boolean | True, if this script is ES6 module. |
| `length` (optional) | integer | This script length. |
| `stackTrace` (optional) *(experimental)* | [Runtime.StackTrace](Runtime.md#type-stacktrace) | JavaScript top stack frame of where the script parsed event was triggered if available. |
| `codeOffset` (optional) *(experimental)* | integer | If the scriptLanguage is WebAssembly, the code section offset in the module. |
| `scriptLanguage` (optional) *(experimental)* | [Debugger.ScriptLanguage](Debugger.md#type-scriptlanguage) | The language of the script. |
| `debugSymbols` (optional) *(experimental)* | array of [Debugger.DebugSymbols](Debugger.md#type-debugsymbols) | If the scriptLanguage is WebAssembly, the source of debug symbols for the module. |
| `embedderName` (optional) *(experimental)* | string | The name the embedder supplied for this script. |
| `resolvedBreakpoints` (optional) *(experimental)* | array of [ResolvedBreakpoint](#type-resolvedbreakpoint) | The list of set breakpoints in this script if calls to `setBreakpointByUrl` matches this script's URL or hash. Clients that use this list can ignore the `breakpointResolved` event. They are equivalent. |

## Types

<a id="type-breakpointid"></a>
### Debugger.BreakpointId

Type: string

Breakpoint identifier.

<a id="type-callframeid"></a>
### Debugger.CallFrameId

Type: string

Call frame identifier.

<a id="type-location"></a>
### Debugger.Location

Type: object

Location in the source code.

**Properties**

| Name | Type | Description |
|---|---|---|
| `scriptId` | [Runtime.ScriptId](Runtime.md#type-scriptid) | Script identifier as reported in the `Debugger.scriptParsed`. |
| `lineNumber` | integer | Line number in the script (0-based). |
| `columnNumber` (optional) | integer | Column number in the script (0-based). |

<a id="type-scriptposition"></a>
### Debugger.ScriptPosition *(experimental)*

Type: object

Location in the source code.

**Properties**

| Name | Type | Description |
|---|---|---|
| `lineNumber` | integer |  |
| `columnNumber` | integer |  |

<a id="type-locationrange"></a>
### Debugger.LocationRange *(experimental)*

Type: object

Location range within one script.

**Properties**

| Name | Type | Description |
|---|---|---|
| `scriptId` | [Runtime.ScriptId](Runtime.md#type-scriptid) |  |
| `start` | [ScriptPosition](#type-scriptposition) |  |
| `end` | [ScriptPosition](#type-scriptposition) |  |

<a id="type-callframe"></a>
### Debugger.CallFrame

Type: object

JavaScript call frame. Array of call frames form the call stack.

**Properties**

| Name | Type | Description |
|---|---|---|
| `callFrameId` | [CallFrameId](#type-callframeid) | Call frame identifier. This identifier is only valid while the virtual machine is paused. |
| `functionName` | string | Name of the JavaScript function called on this call frame. |
| `functionLocation` (optional) | [Location](#type-location) | Location in the source code. |
| `location` | [Location](#type-location) | Location in the source code. |
| `url` *(deprecated)* | string | JavaScript script name or url. Deprecated in favor of using the `location.scriptId` to resolve the URL via a previously sent `Debugger.scriptParsed` event. |
| `scopeChain` | array of [Scope](#type-scope) | Scope chain for this call frame. |
| `this` | [Runtime.RemoteObject](Runtime.md#type-remoteobject) | `this` object for this call frame. |
| `returnValue` (optional) | [Runtime.RemoteObject](Runtime.md#type-remoteobject) | The value being returned, if the function is at return point. |
| `canBeRestarted` (optional) *(experimental)* | boolean | Valid only while the VM is paused and indicates whether this frame can be restarted or not. Note that a `true` value here does not guarantee that Debugger#restartFrame with this CallFrameId will be successful, but it is very likely. |

<a id="type-scope"></a>
### Debugger.Scope

Type: object

Scope description.

**Properties**

| Name | Type | Description |
|---|---|---|
| `type` | enum: `global`, `local`, `with`, `closure`, `catch`, `block`, `script`, `eval`, `module`, `wasm-expression-stack` | Scope type. |
| `object` | [Runtime.RemoteObject](Runtime.md#type-remoteobject) | Object representing the scope. For `global` and `with` scopes it represents the actual object; for the rest of the scopes, it is artificial transient object enumerating scope variables as its properties. |
| `name` (optional) | string |  |
| `startLocation` (optional) | [Location](#type-location) | Location in the source code where scope starts |
| `endLocation` (optional) | [Location](#type-location) | Location in the source code where scope ends |
| `emptyReason` (optional) *(experimental)* | enum: `no-variables`, `all-unavailable` | Present if the scope has no variable values to show. Absent means that the scope declares at least one variable with an available value. Empty scopes are retained in the scope chain because they can be targeted via `evaluateOnCallFrame` (using `scopeNumber`) or matched against scopes in source maps. |

<a id="type-searchmatch"></a>
### Debugger.SearchMatch

Type: object

Search match for resource.

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
| `type` (optional) | enum: `debuggerStatement`, `call`, `return` |  |

<a id="type-wasmdisassemblychunk"></a>
### Debugger.WasmDisassemblyChunk *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `lines` | array of string | The next chunk of disassembled lines. |
| `bytecodeOffsets` | array of integer | The bytecode offsets describing the start of each line. |

<a id="type-scriptlanguage"></a>
### Debugger.ScriptLanguage

Type: string

Enum of possible script languages.

Allowed values: `JavaScript`, `WebAssembly`

<a id="type-debugsymbols"></a>
### Debugger.DebugSymbols

Type: object

Debug symbols available for a wasm script.

**Properties**

| Name | Type | Description |
|---|---|---|
| `type` | enum: `SourceMap`, `EmbeddedDWARF`, `ExternalDWARF` | Type of the debug symbols. |
| `externalURL` (optional) | string | URL of the external symbol source. |

<a id="type-resolvedbreakpoint"></a>
### Debugger.ResolvedBreakpoint

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `breakpointId` | [BreakpointId](#type-breakpointid) | Breakpoint unique identifier. |
| `location` | [Location](#type-location) | Actual breakpoint location. |

