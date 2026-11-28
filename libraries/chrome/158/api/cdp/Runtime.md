# Runtime domain

Runtime domain exposes JavaScript runtime by means of remote evaluation and mirror objects. Evaluation results are returned as mirror object that expose object type, string representation and unique identifier that can be used for further object reference. Original objects are maintained in memory unless they are either explicitly released or are released along with the other objects in their object group.

Methods are called as `Runtime.<command>` and events arrive as `Runtime.<event>`.

## Commands

### Runtime.awaitPromise

Add handler to promise with given promise object id.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `promiseObjectId` | [RemoteObjectId](#type-remoteobjectid) | Identifier of the promise. |
| `returnByValue` (optional) | boolean | Whether the result is expected to be a JSON object that should be sent by value. |
| `generatePreview` (optional) | boolean | Whether preview should be generated for the result. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `result` | [RemoteObject](#type-remoteobject) | Promise result. Will contain rejected value if promise was rejected. |
| `exceptionDetails` (optional) | [ExceptionDetails](#type-exceptiondetails) | Exception details if stack strace is available. |

### Runtime.callFunctionOn

Calls function with given declaration on the given object. Object group of the result is inherited from the target object.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `functionDeclaration` | string | Declaration of the function to call. |
| `objectId` (optional) | [RemoteObjectId](#type-remoteobjectid) | Identifier of the object to call function on. Either objectId or executionContextId should be specified. |
| `arguments` (optional) | array of [CallArgument](#type-callargument) | Call arguments. All call arguments must belong to the same JavaScript world as the target object. |
| `silent` (optional) | boolean | In silent mode exceptions thrown during evaluation are not reported and do not pause execution. Overrides `setPauseOnException` state. |
| `returnByValue` (optional) | boolean | Whether the result is expected to be a JSON object which should be sent by value. Can be overriden by `serializationOptions`. |
| `generatePreview` (optional) *(experimental)* | boolean | Whether preview should be generated for the result. |
| `userGesture` (optional) | boolean | Whether execution should be treated as initiated by user in the UI. |
| `awaitPromise` (optional) | boolean | Whether execution should `await` for resulting value and return once awaited promise is resolved. |
| `executionContextId` (optional) | [ExecutionContextId](#type-executioncontextid) | Specifies execution context which global object will be used to call function on. Either executionContextId or objectId should be specified. |
| `objectGroup` (optional) | string | Symbolic group name that can be used to release multiple objects. If objectGroup is not specified and objectId is, objectGroup will be inherited from object. |
| `throwOnSideEffect` (optional) *(experimental)* | boolean | Whether to throw an exception if side effect cannot be ruled out during evaluation. |
| `uniqueContextId` (optional) *(experimental)* | string | An alternative way to specify the execution context to call function on. Compared to contextId that may be reused across processes, this is guaranteed to be system-unique, so it can be used to prevent accidental function call in context different than intended (e.g. as a result of navigation across process boundaries). This is mutually exclusive with `executionContextId`. |
| `serializationOptions` (optional) *(experimental)* | [SerializationOptions](#type-serializationoptions) | Specifies the result serialization. If provided, overrides `generatePreview` and `returnByValue`. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `result` | [RemoteObject](#type-remoteobject) | Call result. |
| `exceptionDetails` (optional) | [ExceptionDetails](#type-exceptiondetails) | Exception details. |

### Runtime.compileScript

Compiles expression.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `expression` | string | Expression to compile. |
| `sourceURL` | string | Source url to be set for the script. |
| `persistScript` | boolean | Specifies whether the compiled script should be persisted. |
| `executionContextId` (optional) | [ExecutionContextId](#type-executioncontextid) | Specifies in which execution context to perform script run. If the parameter is omitted the evaluation will be performed in the context of the inspected page. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `scriptId` (optional) | [ScriptId](#type-scriptid) | Id of the script. |
| `exceptionDetails` (optional) | [ExceptionDetails](#type-exceptiondetails) | Exception details. |

### Runtime.disable

Disables reporting of execution contexts creation.

### Runtime.discardConsoleEntries

Discards collected exceptions and console API calls.

### Runtime.enable

Enables reporting of execution contexts creation by means of `executionContextCreated` event. When the reporting gets enabled the event will be sent immediately for each existing execution context.

### Runtime.evaluate

Evaluates expression on global object.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `expression` | string | Expression to evaluate. |
| `objectGroup` (optional) | string | Symbolic group name that can be used to release multiple objects. |
| `includeCommandLineAPI` (optional) | boolean | Determines whether Command Line API should be available during the evaluation. |
| `silent` (optional) | boolean | In silent mode exceptions thrown during evaluation are not reported and do not pause execution. Overrides `setPauseOnException` state. |
| `contextId` (optional) | [ExecutionContextId](#type-executioncontextid) | Specifies in which execution context to perform evaluation. If the parameter is omitted the evaluation will be performed in the context of the inspected page. This is mutually exclusive with `uniqueContextId`, which offers an alternative way to identify the execution context that is more reliable in a multi-process environment. |
| `returnByValue` (optional) | boolean | Whether the result is expected to be a JSON object that should be sent by value. |
| `generatePreview` (optional) *(experimental)* | boolean | Whether preview should be generated for the result. |
| `userGesture` (optional) | boolean | Whether execution should be treated as initiated by user in the UI. |
| `awaitPromise` (optional) | boolean | Whether execution should `await` for resulting value and return once awaited promise is resolved. |
| `throwOnSideEffect` (optional) *(experimental)* | boolean | Whether to throw an exception if side effect cannot be ruled out during evaluation. This implies `disableBreaks` below. |
| `timeout` (optional) *(experimental)* | [TimeDelta](#type-timedelta) | Terminate execution after timing out (number of milliseconds). |
| `disableBreaks` (optional) *(experimental)* | boolean | Disable breakpoints during execution. |
| `replMode` (optional) *(experimental)* | boolean | Setting this flag to true enables `let` re-declaration and top-level `await`. Note that `let` variables can only be re-declared if they originate from `replMode` themselves. |
| `allowUnsafeEvalBlockedByCSP` (optional) *(experimental)* | boolean | The Content Security Policy (CSP) for the target might block 'unsafe-eval' which includes eval(), Function(), setTimeout() and setInterval() when called with non-callable arguments. This flag bypasses CSP for this evaluation and allows unsafe-eval. Defaults to true. |
| `uniqueContextId` (optional) *(experimental)* | string | An alternative way to specify the execution context to evaluate in. Compared to contextId that may be reused across processes, this is guaranteed to be system-unique, so it can be used to prevent accidental evaluation of the expression in context different than intended (e.g. as a result of navigation across process boundaries). This is mutually exclusive with `contextId`. |
| `serializationOptions` (optional) *(experimental)* | [SerializationOptions](#type-serializationoptions) | Specifies the result serialization. If provided, overrides `generatePreview` and `returnByValue`. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `result` | [RemoteObject](#type-remoteobject) | Evaluation result. |
| `exceptionDetails` (optional) | [ExceptionDetails](#type-exceptiondetails) | Exception details. |

### Runtime.getIsolateId *(experimental)*

Returns the isolate id.

**Returns**

| Name | Type | Description |
|---|---|---|
| `id` | string | The isolate id. |

### Runtime.getHeapUsage *(experimental)*

Returns the JavaScript heap usage. It is the total usage of the corresponding isolate not scoped to a particular Runtime.

**Returns**

| Name | Type | Description |
|---|---|---|
| `usedSize` | number | Used JavaScript heap size in bytes. |
| `totalSize` | number | Allocated JavaScript heap size in bytes. |
| `embedderHeapUsedSize` | number | Used size in bytes in the embedder's garbage-collected heap. |
| `backingStorageSize` | number | Size in bytes of backing storage for array buffers and external strings. |

### Runtime.getProperties

Returns properties of a given object. Object group of the result is inherited from the target object.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `objectId` | [RemoteObjectId](#type-remoteobjectid) | Identifier of the object to return properties for. |
| `ownProperties` (optional) | boolean | If true, returns properties belonging only to the element itself, not to its prototype chain. |
| `accessorPropertiesOnly` (optional) *(experimental)* | boolean | If true, returns accessor properties (with getter/setter) only; internal properties are not returned either. |
| `generatePreview` (optional) *(experimental)* | boolean | Whether preview should be generated for the results. |
| `nonIndexedPropertiesOnly` (optional) *(experimental)* | boolean | If true, returns non-indexed properties only. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `result` | array of [PropertyDescriptor](#type-propertydescriptor) | Object properties. |
| `internalProperties` (optional) | array of [InternalPropertyDescriptor](#type-internalpropertydescriptor) | Internal object properties (only of the element itself). |
| `privateProperties` (optional) *(experimental)* | array of [PrivatePropertyDescriptor](#type-privatepropertydescriptor) | Object private properties. |
| `exceptionDetails` (optional) | [ExceptionDetails](#type-exceptiondetails) | Exception details. |

### Runtime.globalLexicalScopeNames

Returns all let, const and class variables from global scope.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `executionContextId` (optional) | [ExecutionContextId](#type-executioncontextid) | Specifies in which execution context to lookup global scope variables. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `names` | array of string |  |

### Runtime.queryObjects

**Parameters**

| Name | Type | Description |
|---|---|---|
| `prototypeObjectId` | [RemoteObjectId](#type-remoteobjectid) | Identifier of the prototype to return objects for. |
| `objectGroup` (optional) | string | Symbolic group name that can be used to release the results. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `objects` | [RemoteObject](#type-remoteobject) | Array with objects. |

### Runtime.releaseObject

Releases remote object with given id.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `objectId` | [RemoteObjectId](#type-remoteobjectid) | Identifier of the object to release. |

### Runtime.releaseObjectGroup

Releases all remote objects that belong to a given group.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `objectGroup` | string | Symbolic object group name. |

### Runtime.runIfWaitingForDebugger

Tells inspected instance to run if it was waiting for debugger to attach.

### Runtime.runScript

Runs script with given id in a given context.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `scriptId` | [ScriptId](#type-scriptid) | Id of the script to run. |
| `executionContextId` (optional) | [ExecutionContextId](#type-executioncontextid) | Specifies in which execution context to perform script run. If the parameter is omitted the evaluation will be performed in the context of the inspected page. |
| `objectGroup` (optional) | string | Symbolic group name that can be used to release multiple objects. |
| `silent` (optional) | boolean | In silent mode exceptions thrown during evaluation are not reported and do not pause execution. Overrides `setPauseOnException` state. |
| `includeCommandLineAPI` (optional) | boolean | Determines whether Command Line API should be available during the evaluation. |
| `returnByValue` (optional) | boolean | Whether the result is expected to be a JSON object which should be sent by value. |
| `generatePreview` (optional) | boolean | Whether preview should be generated for the result. |
| `awaitPromise` (optional) | boolean | Whether execution should `await` for resulting value and return once awaited promise is resolved. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `result` | [RemoteObject](#type-remoteobject) | Run result. |
| `exceptionDetails` (optional) | [ExceptionDetails](#type-exceptiondetails) | Exception details. |

### Runtime.setAsyncCallStackDepth

Enables or disables async call stacks tracking.

Redirects to `Debugger`.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `maxDepth` | integer | Maximum depth of async call stacks. Setting to `0` will effectively disable collecting async call stacks (default). |

### Runtime.setCustomObjectFormatterEnabled *(experimental)*

**Parameters**

| Name | Type | Description |
|---|---|---|
| `enabled` | boolean |  |

### Runtime.setMaxCallStackSizeToCapture *(experimental)*

**Parameters**

| Name | Type | Description |
|---|---|---|
| `size` | integer |  |

### Runtime.terminateExecution *(experimental)*

Terminate current or next JavaScript execution. Will cancel the termination when the outer-most script execution ends.

### Runtime.addBinding

If executionContextId is empty, adds binding with the given name on the global objects of all inspected contexts, including those created later, bindings survive reloads. Binding function takes exactly one argument, this argument should be string, in case of any other input, function throws an exception. Each binding function call produces Runtime.bindingCalled notification.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `name` | string |  |
| `executionContextId` (optional) *(experimental)* *(deprecated)* | [ExecutionContextId](#type-executioncontextid) | If specified, the binding would only be exposed to the specified execution context. If omitted and `executionContextName` is not set, the binding is exposed to all execution contexts of the target. This parameter is mutually exclusive with `executionContextName`. Deprecated in favor of `executionContextName` due to an unclear use case and bugs in implementation (crbug.com/1169639). `executionContextId` will be removed in the future. |
| `executionContextName` (optional) | string | If specified, the binding is exposed to the executionContext with matching name, even for contexts created after the binding is added. See also `ExecutionContext.name` and `worldName` parameter to `Page.addScriptToEvaluateOnNewDocument`. This parameter is mutually exclusive with `executionContextId`. |

### Runtime.removeBinding

This method does not remove binding function from global object but unsubscribes current runtime agent from Runtime.bindingCalled notifications.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `name` | string |  |

### Runtime.getExceptionDetails *(experimental)*

This method tries to lookup and populate exception details for a JavaScript Error object. Note that the stackTrace portion of the resulting exceptionDetails will only be populated if the Runtime domain was enabled at the time when the Error was thrown.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `errorObjectId` | [RemoteObjectId](#type-remoteobjectid) | The error object for which to resolve the exception details. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `exceptionDetails` (optional) | [ExceptionDetails](#type-exceptiondetails) |  |

## Events

### Runtime.bindingCalled *(experimental)*

Notification is issued every time when binding is called.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `name` | string |  |
| `payload` | string |  |
| `executionContextId` | [ExecutionContextId](#type-executioncontextid) | Identifier of the context where the call was made. |

### Runtime.consoleAPICalled

Issued when console API was called.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `type` | enum: `log`, `debug`, `info`, `error`, `warning`, `dir`, `dirxml`, `table`, `trace`, `clear`, `startGroup`, `startGroupCollapsed`, `endGroup`, `assert`, `profile`, `profileEnd`, `count`, `timeEnd` | Type of the call. |
| `args` | array of [RemoteObject](#type-remoteobject) | Call arguments. |
| `executionContextId` | [ExecutionContextId](#type-executioncontextid) | Identifier of the context where the call was made. |
| `timestamp` | [Timestamp](#type-timestamp) | Call timestamp. |
| `stackTrace` (optional) | [StackTrace](#type-stacktrace) | Stack trace captured when the call was made. The async stack chain is automatically reported for the following call types: `assert`, `error`, `trace`, `warning`. For other types the async call chain can be retrieved using `Debugger.getStackTrace` and `stackTrace.parentId` field. |
| `context` (optional) *(experimental)* | string | Console context descriptor for calls on non-default console context (not console.*): 'anonymous#unique-logger-id' for call on unnamed context, 'name#unique-logger-id' for call on named context. |

### Runtime.exceptionRevoked

Issued when unhandled exception was revoked.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `reason` | string | Reason describing why exception was revoked. |
| `exceptionId` | integer | The id of revoked exception, as reported in `exceptionThrown`. |

### Runtime.exceptionThrown

Issued when exception was thrown and unhandled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `timestamp` | [Timestamp](#type-timestamp) | Timestamp of the exception. |
| `exceptionDetails` | [ExceptionDetails](#type-exceptiondetails) |  |

### Runtime.executionContextCreated

Issued when new execution context is created.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `context` | [ExecutionContextDescription](#type-executioncontextdescription) | A newly created execution context. |

### Runtime.executionContextDestroyed

Issued when execution context is destroyed.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `executionContextId` *(deprecated)* | [ExecutionContextId](#type-executioncontextid) | Id of the destroyed context |
| `executionContextUniqueId` *(experimental)* | string | Unique Id of the destroyed context |

### Runtime.executionContextsCleared

Issued when all executionContexts were cleared in browser

### Runtime.inspectRequested

Issued when object should be inspected (for example, as a result of inspect() command line API call).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `object` | [RemoteObject](#type-remoteobject) |  |
| `hints` | object |  |
| `executionContextId` (optional) *(experimental)* | [ExecutionContextId](#type-executioncontextid) | Identifier of the context where the call was made. |

## Types

<a id="type-scriptid"></a>
### Runtime.ScriptId

Type: string

Unique script identifier.

<a id="type-serializationoptions"></a>
### Runtime.SerializationOptions

Type: object

Represents options for serialization. Overrides `generatePreview` and `returnByValue`.

**Properties**

| Name | Type | Description |
|---|---|---|
| `serialization` | enum: `deep`, `json`, `idOnly` |  |
| `maxDepth` (optional) | integer | Deep serialization depth. Default is full depth. Respected only in `deep` serialization mode. |
| `additionalParameters` (optional) | object | Embedder-specific parameters. For example if connected to V8 in Chrome these control DOM serialization via `maxNodeDepth: integer` and `includeShadowTree: "none" \| "open" \| "all"`. Values can be only of type string or integer. |

<a id="type-deepserializedvalue"></a>
### Runtime.DeepSerializedValue

Type: object

Represents deep serialized value.

**Properties**

| Name | Type | Description |
|---|---|---|
| `type` | enum: `undefined`, `null`, `string`, `number`, `boolean`, `bigint`, `regexp`, `date`, `symbol`, `array`, `object`, `function`, `map`, `set`, `weakmap`, `weakset`, `error`, `proxy`, `promise`, `typedarray`, `arraybuffer`, `node`, `window`, `generator` |  |
| `value` (optional) | any |  |
| `objectId` (optional) | string |  |
| `weakLocalObjectReference` (optional) | integer | Set if value reference met more then once during serialization. In such case, value is provided only to one of the serialized values. Unique per value in the scope of one CDP call. |

<a id="type-remoteobjectid"></a>
### Runtime.RemoteObjectId

Type: string

Unique object identifier.

<a id="type-unserializablevalue"></a>
### Runtime.UnserializableValue

Type: string

Primitive value which cannot be JSON-stringified. Includes values `-0`, `NaN`, `Infinity`, `-Infinity`, and bigint literals.

<a id="type-remoteobject"></a>
### Runtime.RemoteObject

Type: object

Mirror object referencing original JavaScript object.

**Properties**

| Name | Type | Description |
|---|---|---|
| `type` | enum: `object`, `function`, `undefined`, `string`, `number`, `boolean`, `symbol`, `bigint` | Object type. |
| `subtype` (optional) | enum: `array`, `null`, `node`, `regexp`, `date`, `map`, `set`, `weakmap`, `weakset`, `iterator`, `generator`, `error`, `proxy`, `promise`, `typedarray`, `arraybuffer`, `dataview`, `webassemblymemory`, `wasmvalue`, `deferredmodule`, `trustedtype` | Object subtype hint. Specified for `object` type values only. NOTE: If you change anything here, make sure to also update `subtype` in `ObjectPreview` and `PropertyPreview` below. |
| `className` (optional) | string | Object class (constructor) name. Specified for `object` type values only. |
| `value` (optional) | any | Remote object value in case of primitive values or JSON values (if it was requested). |
| `unserializableValue` (optional) | [UnserializableValue](#type-unserializablevalue) | Primitive value which can not be JSON-stringified does not have `value`, but gets this property. |
| `description` (optional) | string | String representation of the object. |
| `deepSerializedValue` (optional) *(experimental)* | [DeepSerializedValue](#type-deepserializedvalue) | Deep serialized value. |
| `objectId` (optional) | [RemoteObjectId](#type-remoteobjectid) | Unique object identifier (for non-primitive values). |
| `preview` (optional) *(experimental)* | [ObjectPreview](#type-objectpreview) | Preview containing abbreviated property values. Specified for `object` type values only. |
| `customPreview` (optional) *(experimental)* | [CustomPreview](#type-custompreview) |  |

<a id="type-custompreview"></a>
### Runtime.CustomPreview *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `header` | string | The JSON-stringified result of formatter.header(object, config) call. It contains json ML array that represents RemoteObject. |
| `bodyGetterId` (optional) | [RemoteObjectId](#type-remoteobjectid) | If formatter returns true as a result of formatter.hasBody call then bodyGetterId will contain RemoteObjectId for the function that returns result of formatter.body(object, config) call. The result value is json ML array. |

<a id="type-objectpreview"></a>
### Runtime.ObjectPreview *(experimental)*

Type: object

Object containing abbreviated remote object value.

**Properties**

| Name | Type | Description |
|---|---|---|
| `type` | enum: `object`, `function`, `undefined`, `string`, `number`, `boolean`, `symbol`, `bigint` | Object type. |
| `subtype` (optional) | enum: `array`, `null`, `node`, `regexp`, `date`, `map`, `set`, `weakmap`, `weakset`, `iterator`, `generator`, `error`, `proxy`, `promise`, `typedarray`, `arraybuffer`, `dataview`, `webassemblymemory`, `wasmvalue`, `deferredmodule`, `trustedtype` | Object subtype hint. Specified for `object` type values only. |
| `description` (optional) | string | String representation of the object. |
| `overflow` | boolean | True iff some of the properties or entries of the original object did not fit. |
| `properties` | array of [PropertyPreview](#type-propertypreview) | List of the properties. |
| `entries` (optional) | array of [EntryPreview](#type-entrypreview) | List of the entries. Specified for `map` and `set` subtype values only. |

<a id="type-propertypreview"></a>
### Runtime.PropertyPreview *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Property name. |
| `type` | enum: `object`, `function`, `undefined`, `string`, `number`, `boolean`, `symbol`, `accessor`, `bigint` | Object type. Accessor means that the property itself is an accessor property. |
| `value` (optional) | string | User-friendly property value string. |
| `valuePreview` (optional) | [ObjectPreview](#type-objectpreview) | Nested value preview. |
| `subtype` (optional) | enum: `array`, `null`, `node`, `regexp`, `date`, `map`, `set`, `weakmap`, `weakset`, `iterator`, `generator`, `error`, `proxy`, `promise`, `typedarray`, `arraybuffer`, `dataview`, `webassemblymemory`, `wasmvalue`, `deferredmodule`, `trustedtype` | Object subtype hint. Specified for `object` type values only. |

<a id="type-entrypreview"></a>
### Runtime.EntryPreview *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `key` (optional) | [ObjectPreview](#type-objectpreview) | Preview of the key. Specified for map-like collection entries. |
| `value` | [ObjectPreview](#type-objectpreview) | Preview of the value. |

<a id="type-propertydescriptor"></a>
### Runtime.PropertyDescriptor

Type: object

Object property descriptor.

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Property name or symbol description. |
| `value` (optional) | [RemoteObject](#type-remoteobject) | The value associated with the property. |
| `writable` (optional) | boolean | True if the value associated with the property may be changed (data descriptors only). |
| `get` (optional) | [RemoteObject](#type-remoteobject) | A function which serves as a getter for the property, or `undefined` if there is no getter (accessor descriptors only). |
| `set` (optional) | [RemoteObject](#type-remoteobject) | A function which serves as a setter for the property, or `undefined` if there is no setter (accessor descriptors only). |
| `configurable` | boolean | True if the type of this property descriptor may be changed and if the property may be deleted from the corresponding object. |
| `enumerable` | boolean | True if this property shows up during enumeration of the properties on the corresponding object. |
| `wasThrown` (optional) | boolean | True if the result was thrown during the evaluation. |
| `isOwn` (optional) | boolean | True if the property is owned for the object. |
| `symbol` (optional) | [RemoteObject](#type-remoteobject) | Property symbol object, if the property is of the `symbol` type. |

<a id="type-internalpropertydescriptor"></a>
### Runtime.InternalPropertyDescriptor

Type: object

Object internal property descriptor. This property isn't normally visible in JavaScript code.

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Conventional property name. |
| `value` (optional) | [RemoteObject](#type-remoteobject) | The value associated with the property. |

<a id="type-privatepropertydescriptor"></a>
### Runtime.PrivatePropertyDescriptor *(experimental)*

Type: object

Object private field descriptor.

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Private property name. |
| `value` (optional) | [RemoteObject](#type-remoteobject) | The value associated with the private property. |
| `get` (optional) | [RemoteObject](#type-remoteobject) | A function which serves as a getter for the private property, or `undefined` if there is no getter (accessor descriptors only). |
| `set` (optional) | [RemoteObject](#type-remoteobject) | A function which serves as a setter for the private property, or `undefined` if there is no setter (accessor descriptors only). |

<a id="type-callargument"></a>
### Runtime.CallArgument

Type: object

Represents function call argument. Either remote object id `objectId`, primitive `value`, unserializable primitive value or neither of (for undefined) them should be specified.

**Properties**

| Name | Type | Description |
|---|---|---|
| `value` (optional) | any | Primitive value or serializable javascript object. |
| `unserializableValue` (optional) | [UnserializableValue](#type-unserializablevalue) | Primitive value which can not be JSON-stringified. |
| `objectId` (optional) | [RemoteObjectId](#type-remoteobjectid) | Remote object handle. |

<a id="type-executioncontextid"></a>
### Runtime.ExecutionContextId

Type: integer

Id of an execution context.

<a id="type-executioncontextdescription"></a>
### Runtime.ExecutionContextDescription

Type: object

Description of an isolated world.

**Properties**

| Name | Type | Description |
|---|---|---|
| `id` | [ExecutionContextId](#type-executioncontextid) | Unique id of the execution context. It can be used to specify in which execution context script evaluation should be performed. |
| `origin` | string | Execution context origin. |
| `name` | string | Human readable name describing given context. |
| `uniqueId` *(experimental)* | string | A system-unique execution context identifier. Unlike the id, this is unique across multiple processes, so can be reliably used to identify specific context while backend performs a cross-process navigation. |
| `auxData` (optional) | object | Embedder-specific auxiliary data likely matching {isDefault: boolean, type: 'default'\|'isolated'\|'worker', frameId: string} |

<a id="type-exceptiondetails"></a>
### Runtime.ExceptionDetails

Type: object

Detailed information about exception (or error) that was thrown during script compilation or execution.

**Properties**

| Name | Type | Description |
|---|---|---|
| `exceptionId` | integer | Exception id. |
| `text` | string | Exception text, which should be used together with exception object when available. |
| `lineNumber` | integer | Line number of the exception location (0-based). |
| `columnNumber` | integer | Column number of the exception location (0-based). |
| `scriptId` (optional) | [ScriptId](#type-scriptid) | Script ID of the exception location. |
| `url` (optional) | string | URL of the exception location, to be used when the script was not reported. |
| `stackTrace` (optional) | [StackTrace](#type-stacktrace) | JavaScript stack trace if available. |
| `exception` (optional) | [RemoteObject](#type-remoteobject) | Exception object if available. |
| `executionContextId` (optional) | [ExecutionContextId](#type-executioncontextid) | Identifier of the context where exception happened. |
| `exceptionMetaData` (optional) *(experimental)* | object | Dictionary with entries of meta data that the client associated with this exception, such as information about associated network requests, etc. |

<a id="type-timestamp"></a>
### Runtime.Timestamp

Type: number

Number of milliseconds since epoch.

<a id="type-timedelta"></a>
### Runtime.TimeDelta

Type: number

Number of milliseconds.

<a id="type-callframe"></a>
### Runtime.CallFrame

Type: object

Stack entry for runtime errors and assertions.

**Properties**

| Name | Type | Description |
|---|---|---|
| `functionName` | string | JavaScript function name. |
| `scriptId` | [ScriptId](#type-scriptid) | JavaScript script id. |
| `url` | string | JavaScript script name or url. |
| `lineNumber` | integer | JavaScript script line number (0-based). |
| `columnNumber` | integer | JavaScript script column number (0-based). |

<a id="type-stacktrace"></a>
### Runtime.StackTrace

Type: object

Call frames for assertions or error messages.

**Properties**

| Name | Type | Description |
|---|---|---|
| `description` (optional) | string | String label of this stack trace. For async traces this may be a name of the function that initiated the async call. |
| `callFrames` | array of [CallFrame](#type-callframe) | JavaScript function name. |
| `parent` (optional) | [StackTrace](#type-stacktrace) | Asynchronous JavaScript stack trace that preceded this stack, if available. |
| `parentId` (optional) *(experimental)* | [StackTraceId](#type-stacktraceid) | Asynchronous JavaScript stack trace that preceded this stack, if available. |

<a id="type-uniquedebuggerid"></a>
### Runtime.UniqueDebuggerId *(experimental)*

Type: string

Unique identifier of current debugger.

<a id="type-stacktraceid"></a>
### Runtime.StackTraceId *(experimental)*

Type: object

If `debuggerId` is set stack trace comes from another debugger and can be resolved there. This allows to track cross-debugger calls. See `Runtime.StackTrace` and `Debugger.paused` for usages.

**Properties**

| Name | Type | Description |
|---|---|---|
| `id` | string |  |
| `debuggerId` (optional) | [UniqueDebuggerId](#type-uniquedebuggerid) |  |

